#!/usr/bin/env python3
"""Make a new draft guide folder by copying an existing guide.

Usage:
  new_guide.py SOURCE NEW --title "New Title" [--guide-md FILE] [--month "Month Year"]

SOURCE is a guide that builds, as a folder or a slug (looked up in guides/ and then
drafts/), such as lights-off-software-factories or specs-and-reviews. NEW is the new slug,
or a folder path. A bare slug makes drafts/<slug> at the repository root. The slug is
lowercase words joined by hyphens, and it names the output files.

What it does:
  - copies every file except dist/, node_modules/, __pycache__, built PDFs and .docx files,
    package.json (pnpm sync writes a new one) and expected.sha256;
  - replaces the old slug and the old title with the new ones in build_guide.py,
    build_docx.py and README.md;
  - sets COVER_LINES in build_guide.py from the new title;
  - sets the PDF's and the Word document's author to "Accidental Guides";
  - in guide.md (copied, or taken from --guide-md), sets title to the new title, version to
    0.1.0, and the public imprint:
        edition: oops@accidental.info · CC BY 4.0 · <Month Year>
        cover_footer: hi@accidental.info · <Month Year>
    with this month unless --month is given.

It then prints what still has to change by hand, and the next steps (pnpm sync, then the
build). Standard library only.
"""
import argparse
import datetime
import re
import shutil
import sys
from pathlib import Path

SKIP_DIRS = {"__pycache__", "dist", "node_modules", ".turbo"}
SKIP_SUFFIXES = {".pdf", ".docx", ".pyc"}
SKIP_NAMES = {"expected.sha256", ".DS_Store", "package.json"}
TEXT_FILES = ("build_guide.py", "build_docx.py", "README.md")
AUTHOR = "Accidental Guides"


def repo_root():
    for start in (Path(__file__).resolve().parent, Path.cwd()):
        for d in (start, *start.parents):
            if (d / "packages" / "pipeline" / "guide.py").is_file():
                return d
    sys.exit("can't find the repository root (the folder with packages/pipeline/guide.py)")


def front_matter(text):
    """Return the front matter lines and the line index of the closing ---."""
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        sys.exit("guide.md must start with --- on line 1")
    for i in range(1, len(lines)):
        if lines[i] == "---":
            return lines, i
    sys.exit("guide.md front matter has no closing ---")


def set_key(lines, key, value):
    _, end = front_matter("\n".join(lines))
    for i in range(1, end):
        if lines[i].split(":", 1)[0].strip() == key:
            lines[i] = f"{key}: {value}"
            return
    lines.insert(end, f"{key}: {value}")


def cover_lines(title, width=12):
    """Split a title into short lines for the cover, about `width` characters each."""
    out, line = [], ""
    for word in title.split():
        if line and len(line) + 1 + len(word) > width:
            out.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    out.append(line)
    return out


def set_author(text):
    text = re.sub(r'setAuthor\("[^"]*"\)', f'setAuthor("{AUTHOR}")', text)
    text = re.sub(r'^(\s*props\.title, props\.subject, props\.author = .*, )"[^"]*"\s*$',
                  rf'\1"{AUTHOR}"', text, flags=re.M)
    return re.sub(r'^(\s*props\.last_modified_by, props\.revision = )"[^"]*"',
                  rf'\1"{AUTHOR}"', text, flags=re.M)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("dest")
    ap.add_argument("--title", required=True, help="the new guide's title, without the kicker")
    ap.add_argument("--guide-md", type=Path, help="start from this guide.md instead of the source's")
    ap.add_argument("--month", default=datetime.date.today().strftime("%B %Y"),
                    help='the month for the imprint, such as "October 2026" (default: this month)')
    args = ap.parse_args()
    root = repo_root()

    src = Path(args.source)
    if not (src / "guide.md").is_file():
        src = next((root / k / args.source for k in ("guides", "drafts")
                    if (root / k / args.source / "guide.md").is_file()), src)
    src = src.resolve()
    for name in ("guide.md", "content.py", "build_guide.py"):
        if not (src / name).exists():
            sys.exit(f"{src} has no {name}; pass a guide folder or slug that builds")
    dst = Path(args.dest)
    dst = (root / "drafts" / args.dest if len(dst.parts) == 1 else dst).resolve()
    if dst.exists():
        sys.exit(f"{dst} already exists")
    old_slug, new_slug = src.name, dst.name
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", new_slug):
        sys.exit(f"slug {new_slug!r} should be lowercase words joined by hyphens")
    if dst.parent.name not in ("drafts", "guides") or dst.parent.parent != root:
        print(f"note: {dst} isn't in drafts/ or guides/, so pnpm sync won't add it to the workspace")

    old_lines, old_end = front_matter((src / "guide.md").read_text(encoding="utf-8"))
    old_meta = dict(l.split(":", 1) for l in old_lines[1:old_end] if ":" in l)
    old_title = old_meta.get("title", "").strip()

    def ignore(folder, names):
        return [n for n in names if n in SKIP_DIRS or n in SKIP_NAMES or Path(n).suffix in SKIP_SUFFIXES]

    shutil.copytree(src, dst, ignore=ignore)

    for name in TEXT_FILES:
        path = dst / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        text = text.replace(old_slug, new_slug)
        if old_title:
            text = text.replace(old_title, args.title)
        if name == "build_guide.py":
            parts = cover_lines(args.title)
            tup = ", ".join(f'"{p}"' for p in parts) + ("," if len(parts) == 1 else "")
            text, n = re.subn(r"^COVER_LINES = \(.*\)$", lambda m: f"COVER_LINES = ({tup})", text,
                              count=1, flags=re.M)
            if not n:
                print("note: build_guide.py has no COVER_LINES line; set the cover title by hand")
        if name in ("build_guide.py", "build_docx.py"):
            text = set_author(text)
        path.write_text(text, encoding="utf-8")

    guide = (args.guide_md or src / "guide.md").read_text(encoding="utf-8")
    lines, _ = front_matter(guide)
    set_key(lines, "title", args.title)
    set_key(lines, "version", "0.1.0")
    set_key(lines, "edition", f"oops@accidental.info · CC BY 4.0 · {args.month}")
    set_key(lines, "cover_footer", f"hi@accidental.info · {args.month}")
    (dst / "guide.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    rel = dst.relative_to(root) if dst.is_relative_to(root) else dst
    print(f"made {rel} from {src.relative_to(root) if src.is_relative_to(root) else src}")
    print("still to change by hand:")
    print("  guide.md        every word, the subtitle and running_footer (keep the section ids and")
    print("                  table shapes content.py reads)")
    print("  content.py      the voice comment at the top; slots if the sections change")
    print("  build_guide.py  PART_TOKEN, NAME2MONO, MONO_RE, the FIT_* labels and page_fit(), page order")
    print("  build_docx.py   page order, fit_box() or fit_layout() if the diagram moved")
    print("  README.md       what's here, how to rebuild, and the Markdown section, if they differ")
    print("then, from the repository root:")
    print("  pnpm sync                                   # adds the folder to the workspace")
    print(f"  packages/editorial/skills/accidental-guide-build/scripts/build_one.sh {rel} --update-hash")


if __name__ == "__main__":
    main()
