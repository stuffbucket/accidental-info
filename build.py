"""Build every guide in guides/ into dist/.

Each guide folder has a guide.md (the text), a content.py that reads it, a
build_guide.py (the PDF layout) and, optionally, a build_docx.py (the Word layout).
This writes dist/<guide>.pdf and dist/<guide>.docx for each, and dist/guides.json with
each guide's title, subtitle, edition, version, page count, blurb and files, which the site
reads. The build fails if any PDF page has content past its bottom margin. The .docx
is built after the PDF because it places the PDF's diagrams.
"""
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIST = HERE / "dist"


def main():
    DIST.mkdir(exist_ok=True)
    guides = []
    for folder in sorted((HERE / "guides").iterdir()):
        if not (folder / "build_guide.py").exists():
            continue
        pdf = DIST / f"{folder.name}.pdf"
        run = subprocess.run([sys.executable, "build_guide.py", str(pdf)], cwd=folder,
                             capture_output=True, text=True)
        sys.stdout.write(run.stdout)
        sys.stderr.write(run.stderr)
        if run.returncode != 0:
            sys.exit(f"{folder.name}: build_guide.py failed")
        if "no overflow" not in run.stdout:
            sys.exit(f"{folder.name}: content runs past the bottom margin")
        docx = None
        if (folder / "build_docx.py").exists():
            docx = DIST / f"{folder.name}.docx"
            run = subprocess.run([sys.executable, "build_docx.py", str(pdf), str(docx)], cwd=folder,
                                 capture_output=True, text=True)
            sys.stdout.write(run.stdout)
            sys.stderr.write(run.stderr)
            if run.returncode != 0:
                sys.exit(f"{folder.name}: build_docx.py failed")
        spec = importlib.util.spec_from_file_location(f"{folder.name}_content", folder / "content.py")
        content = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(content)
        guides.append({
            "id": folder.name,
            "title": content.TITLE,
            "kicker": content.KICKER,
            "subtitle": content.SUBTITLE,
            "edition": content.EDITION,
            "version": content.VERSION,
            "blurb": content.BLURB,
            "pdf": pdf.name,
            "docx": docx.name if docx else None,
            "pages": int(re.search(r": (\d+) pages", run.stdout).group(1)),
        })
    (DIST / "guides.json").write_text(json.dumps(guides, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {DIST / 'guides.json'}: {len(guides)} guides")


if __name__ == "__main__":
    main()
