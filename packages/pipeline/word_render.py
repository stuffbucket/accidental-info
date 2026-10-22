"""Render guides' .docx files with Microsoft Word and compare them with the PDFs.

The PDF is the oracle. This opens each guide's .docx in Microsoft Word (macOS, through
AppleScript), saves it as PDF with Word's own renderer, rasterises that PDF and the
reference PDF with pypdfium2, and writes, per page, a side-by-side comparison image:

    reference PDF | Word | overlay (reference in red, Word in cyan; where they agree, grey)

It also writes a pixel-difference score per page, so the pages that differ most can be
looked at first, and a page-count check: Word must give as many pages as the PDF.

Usage (from the repo root):

    .venv/bin/python packages/pipeline/word_render.py OUT_DIR GUIDE_FOLDER [GUIDE_FOLDER ...]
        [--build]        build the PDF and .docx into OUT_DIR first, with the folder's own
                         build_guide.py and build_docx.py (dist/ is not touched)
        [--dpi N]        raster resolution (default 110)
        [--pages 2,5]    only these pages in the comparison images
        [--keep]         keep the Word-exported PDFs (always kept as OUT_DIR/<slug>/word.pdf)

    .venv/bin/python packages/pipeline/word_render.py OUT_DIR --all [--build]
        every guide folder: guides/*, drafts/*, packages/template

Without --build it compares <folder>/dist/<slug>.pdf with <folder>/dist/<slug>.docx.

Output, per guide: OUT_DIR/<slug>/p01.png … (comparisons), word.pdf, ref.pdf (when
built), and scores.json; and for the run OUT_DIR/scores.md, a table of every page's score.

Word for Mac is sandboxed: the .docx is copied to WORK (/private/tmp/docxfid/work), a folder
Word can be granted access to. If Word asks for access ("Grant File Access"), the script
presses "Select…", which grants the file it names. Each document is closed without saving
after the export, and documents Word already had open are left alone.

Score: the share of pixels, in percent, whose grey level differs by more than 48 of 255
after both pages are blurred by one pixel (so anti-aliasing and sub-pixel text placement
don't count). Text set by two different engines never matches exactly; a page of correct
text typically scores 2-6, a misplaced, missing or doubled diagram 8 or more.
"""
import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image, ImageChops, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
WORK = Path("/private/tmp/docxfid/work")
PY = sys.executable

EXPORT = r'''
on run argv
  set inPath to item 1 of argv
  set outPath to item 2 of argv
  set docName to item 3 of argv
  tell application "Microsoft Word"
    with timeout of 10 seconds
      try
        open (POSIX file inPath)
      end try
    end timeout
  end tell
  -- Word may stop to ask for access to the file: grant it.
  repeat 240 times
    tell application "Microsoft Word" to set names to name of every document
    if names contains docName then exit repeat
    try
      tell application "System Events" to tell process "Microsoft Word"
        if exists window "Grant File Access" then click button "Select..." of window "Grant File Access"
      end tell
    end try
    delay 0.5
  end repeat
  delay 1
  set saved to false
  set lastErr to ""
  repeat 10 times
    try
      tell application "Microsoft Word"
        with timeout of 300 seconds
          save as document docName file name outPath file format format PDF
        end timeout
      end tell
      set saved to true
      exit repeat
    on error e
      set lastErr to e
      delay 1
    end try
  end repeat
  closeIt(docName)
  if not saved then error "save as PDF failed: " & lastErr
end run

on closeIt(docName)
  repeat 10 times
    try
      tell application "Microsoft Word"
        if (name of every document) does not contain docName then return
        close document docName saving no
      end tell
      return
    on error
      delay 1
    end try
  end repeat
end closeIt
'''


def folders_all():
    out = sorted((ROOT / "guides").iterdir()) + sorted((ROOT / "drafts").iterdir())
    out.append(ROOT / "packages" / "template")
    return [f for f in out if (f / "build_docx.py").exists()]


def build(folder, dest):
    """Build the PDF and the .docx into dest with the folder's own builders."""
    pdf, docx = dest / "ref.pdf", dest / f"{folder.name}.docx"
    r = subprocess.run([PY, "build_guide.py", str(pdf)], cwd=folder, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f"{folder.name}: build_guide.py failed\n{r.stderr[-2000:]}")
    if "DIFFERS" in r.stdout:
        print(f"  warning: {folder.name}: the PDF differs from expected.sha256")
    r = subprocess.run([PY, "build_docx.py", str(pdf), str(docx)], cwd=folder, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f"{folder.name}: build_docx.py failed\n{r.stderr[-2000:]}")
    return pdf, docx


def word_export(docx, out_pdf, retry=2):
    """Save docx as PDF with Microsoft Word."""
    WORK.mkdir(parents=True, exist_ok=True)
    name = f"fid-{docx.stem}.docx"
    src = WORK / name
    shutil.copyfile(docx, src)
    tmp_pdf = WORK / f"fid-{docx.stem}.pdf"
    tmp_pdf.unlink(missing_ok=True)
    script = WORK / "export.applescript"
    script.write_text(EXPORT)
    t = time.time()
    r = subprocess.run(["osascript", str(script), str(src), str(tmp_pdf), name],
                       capture_output=True, text=True, timeout=600)
    if r.returncode or not tmp_pdf.exists():
        # Don't leave the document open in Word.
        subprocess.run(["osascript", "-e", f'tell application "Microsoft Word" to close document "{name}" saving no'],
                       capture_output=True)
        if retry:
            return word_export(docx, out_pdf, retry - 1)
        raise RuntimeError(f"Word export failed for {docx.name}: {r.stderr.strip()}")
    shutil.move(tmp_pdf, out_pdf)
    src.unlink(missing_ok=True)
    return time.time() - t


def raster(pdf_path, dpi):
    pdf = pdfium.PdfDocument(str(pdf_path))
    pages = [p.render(scale=dpi / 72).to_pil().convert("RGB") for p in pdf]
    pdf.close()
    return pages


def score(a, b):
    """Percent of pixels whose blurred grey level differs by more than 48."""
    if b.size != a.size:
        b = b.resize(a.size)
    ga = a.convert("L").filter(ImageFilter.GaussianBlur(1))
    gb = b.convert("L").filter(ImageFilter.GaussianBlur(1))
    d = ImageChops.difference(ga, gb).point(lambda v: 255 if v > 48 else 0)
    hist = d.histogram()
    return 100 * hist[255] / (a.size[0] * a.size[1])


def overlay(a, b):
    """Reference in red, Word in cyan: ink both have is dark, ink only one has is coloured."""
    if b.size != a.size:
        b = b.resize(a.size)
    la, lb = a.convert("L"), b.convert("L")
    return Image.merge("RGB", (lb, la, la))


def panel(img, label, w, h):
    out = Image.new("RGB", (w, h + 22), "white")
    if img is not None:
        out.paste(img.resize((w, h)) if img.size != (w, h) else img, (0, 22))
        ImageDraw.Draw(out).rectangle([0, 22, w - 1, h + 21], outline=(170, 170, 170))
    else:
        ImageDraw.Draw(out).text((10, h // 2), "(no page)", fill=(200, 0, 0))
    ImageDraw.Draw(out).text((4, 5), label, fill=(0, 0, 0))
    return out


def compare(slug, ref_pdf, word_pdf, dest, dpi, only=None):
    ref, word = raster(ref_pdf, dpi), raster(word_pdf, dpi)
    w, h = ref[0].size
    rows = []
    for i in range(max(len(ref), len(word))):
        n = i + 1
        a = ref[i] if i < len(ref) else None
        b = word[i] if i < len(word) else None
        s = score(a, b) if a is not None and b is not None else 100.0
        rows.append({"page": n, "score": round(s, 2)})
        if only and n not in only:
            continue
        ov = overlay(a, b) if a is not None and b is not None else None
        sheet = Image.new("RGB", (3 * w + 20, h + 22), "white")
        sheet.paste(panel(a, f"{slug} p{n}  PDF (reference)", w, h), (0, 0))
        sheet.paste(panel(b, f"Word export  score {s:.1f}", w, h), (w + 10, 0))
        sheet.paste(panel(ov, "overlay: red = PDF only, cyan = Word only", w, h), (2 * w + 20, 0))
        sheet.save(dest / f"p{n:02d}.png", optimize=True)
    result = {"slug": slug, "ref_pages": len(ref), "word_pages": len(word), "pages": rows}
    (dest / "scores.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out")
    ap.add_argument("folders", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--dpi", type=int, default=110)
    ap.add_argument("--pages", default="")
    a = ap.parse_args()
    folders = folders_all() if a.all else [Path(f).resolve() for f in a.folders]
    if not folders:
        sys.exit("no guide folders given")
    only = {int(x) for x in a.pages.split(",") if x}
    out = Path(a.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    results = []
    for folder in folders:
        slug = folder.name
        dest = out / slug
        dest.mkdir(parents=True, exist_ok=True)
        for old in dest.glob("p*.png"):
            old.unlink()
        try:
            if a.build:
                ref_pdf, docx = build(folder, dest)
            else:
                ref_pdf, docx = folder / "dist" / f"{slug}.pdf", folder / "dist" / f"{slug}.docx"
            secs = word_export(docx, dest / "word.pdf")
            r = compare(slug, ref_pdf, dest / "word.pdf", dest, a.dpi, only)
        except Exception as e:  # report and go on to the next guide
            print(f"{slug}: FAILED: {e}")
            results.append({"slug": slug, "error": str(e)})
            continue
        worst = sorted(r["pages"], key=lambda p: -p["score"])[:3]
        flag = "" if r["ref_pages"] == r["word_pages"] else "  PAGE COUNT DIFFERS"
        print(f"{slug}: PDF {r['ref_pages']} pages, Word {r['word_pages']} ({secs:.0f}s); worst "
              + ", ".join(f"p{p['page']} {p['score']}" for p in worst) + flag)
        results.append(r)
    lines = ["| guide | PDF pages | Word pages | per-page score (p1, p2, …) | max |", "|---|---|---|---|---|"]
    for r in results:
        if "error" in r:
            lines.append(f"| {r['slug']} | | | FAILED: {r['error'][:80]} | |")
            continue
        s = [p["score"] for p in r["pages"]]
        lines.append(f"| {r['slug']} | {r['ref_pages']} | {r['word_pages']} | "
                     + " ".join(f"{x:.1f}" for x in s) + f" | {max(s):.1f} |")
    (out / "scores.md").write_text("\n".join(lines) + "\n")
    (out / "scores.json").write_text(json.dumps(results, indent=2) + "\n")
    print(f"wrote {out / 'scores.md'}")


if __name__ == "__main__":
    main()
