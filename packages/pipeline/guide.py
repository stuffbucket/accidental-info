"""Build one guide folder into its dist/.

Usage: python guide.py <guide folder>

The folder has a guide.md (the text), a content.py that reads it, a build_guide.py (the
PDF layout) and, optionally, a build_docx.py (the Word layout). This writes
<folder>/dist/<slug>.pdf, <folder>/dist/<slug>.docx and <folder>/dist/guide.json with the
guide's title, subtitle, edition, version, page count, blurb, files and status, which the
site reads. A guide under drafts/ has status "draft"; any other has status "published".

The build fails if a page has content past its bottom margin, or if the PDF differs from
the guide's expected.sha256. The .docx is built after the PDF because it places the PDF's
diagrams.
"""
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path


def run(args, folder):
    result = subprocess.run([sys.executable, *args], cwd=folder, capture_output=True, text=True)
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    return result


def main(folder):
    folder = folder.resolve()
    slug = folder.name
    dist = folder / "dist"
    dist.mkdir(exist_ok=True)
    pdf = dist / f"{slug}.pdf"
    built = run(["build_guide.py", str(pdf)], folder)
    if built.returncode != 0:
        sys.exit(f"{slug}: build_guide.py failed")
    if "no overflow" not in built.stdout:
        sys.exit(f"{slug}: content runs past the bottom margin")
    if "DIFFERS from expected.sha256" in built.stdout:
        sys.exit(f"{slug}: the PDF differs from expected.sha256; if the change is intended, "
                 "write the new hash into expected.sha256")
    pages = int(re.search(r": (\d+) pages", built.stdout).group(1))
    docx = None
    if (folder / "build_docx.py").exists():
        docx = dist / f"{slug}.docx"
        if run(["build_docx.py", str(pdf), str(docx)], folder).returncode != 0:
            sys.exit(f"{slug}: build_docx.py failed")
    spec = importlib.util.spec_from_file_location(f"{slug}_content", folder / "content.py")
    content = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(content)
    guide = {
        "id": slug,
        "status": "draft" if folder.parent.name == "drafts" else "published",
        "title": content.TITLE,
        "kicker": content.KICKER,
        "subtitle": content.SUBTITLE,
        "edition": content.EDITION,
        "version": content.VERSION,
        "blurb": content.BLURB,
        "pdf": pdf.name,
        "docx": docx.name if docx else None,
        "pages": pages,
    }
    (dist / "guide.json").write_text(json.dumps(guide, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {dist / 'guide.json'}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(Path(sys.argv[1]))
