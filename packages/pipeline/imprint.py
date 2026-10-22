"""Give a guide folder the series' public imprint, then rebuild its expected.sha256.

Usage: python imprint.py <guide folder> [<guide folder> ...]

The cover's footer gets the general address, the end page's footer the address for
mistakes and the text's license, and the PDF's and Word document's author is the series:

    cover_footer: hi@accidental.info · <month>
    edition: oops@accidental.info · CC BY 4.0 · <month>
    author "Accidental Guides" in build_guide.py and build_docx.py

<month> is the last part of the guide's current edition, such as "October 2026". A
folder that already has the imprint is left as it is. The PDF is then built once to a
temporary file and its hash written to expected.sha256, so the guide's own build checks
against the imprinted text. Run it with the Python that has the pipeline's packages.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HI = "hi@accidental.info"
OOPS = "oops@accidental.info"
LICENSE = "CC BY 4.0"
AUTHOR = "Accidental Guides"


def front_matter(text, key):
    match = re.search(rf"^{key}: (.*)$", text.split("\n---\n", 1)[0], re.M)
    if not match:
        raise SystemExit(f"no {key}: in the front matter")
    return match


def imprint_text(text):
    edition = front_matter(text, "edition")
    month = edition.group(1).split(" · ")[-1]
    text = text[:edition.start(1)] + f"{OOPS} · {LICENSE} · {month}" + text[edition.end(1):]
    cover = front_matter(text, "cover_footer")
    return text[:cover.start(1)] + f"{HI} · {month}" + text[cover.end(1):]


def imprint_builder(text):
    return re.sub(r'"bstucker"', f'"{AUTHOR}"', text)


def rehash(folder):
    with tempfile.TemporaryDirectory() as tmp:
        pdf = Path(tmp) / f"{folder.name}.pdf"
        run = subprocess.run([sys.executable, "build_guide.py", str(pdf)], cwd=folder,
                             capture_output=True, text=True)
        if run.returncode != 0 or "no overflow" not in run.stdout:
            sys.stderr.write(run.stdout + run.stderr)
            raise SystemExit(f"{folder.name}: the imprinted guide doesn't build")
        digest = re.search(r"^sha256 ([0-9a-f]{64})$", run.stdout, re.M).group(1)
    (folder / "expected.sha256").write_text(f"{digest}  {folder.name}.pdf\n")
    return digest


def main(folders):
    for folder in map(Path, folders):
        folder = folder.resolve()
        changed = False
        md = folder / "guide.md"
        text = md.read_text(encoding="utf-8")
        new = imprint_text(text)
        if new != text:
            md.write_text(new, encoding="utf-8")
            changed = True
        for name in ("build_guide.py", "build_docx.py"):
            path = folder / name
            if path.exists():
                text = path.read_text(encoding="utf-8")
                new = imprint_builder(text)
                if new != text:
                    path.write_text(new, encoding="utf-8")
                    changed = True
        if changed:
            print(f"{folder.name}: imprinted, sha256 {rehash(folder)}")
        else:
            print(f"{folder.name}: already imprinted")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
