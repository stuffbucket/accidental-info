"""Give the built template its download names.

guide.py names a build after its folder (dist/template.pdf, dist/template.docx). This renames
them to dist/accidental-guide-template.pdf and .docx, and removes dist/guide.json, which is
only for the site's list of guides.
"""
from pathlib import Path

DIST = Path(__file__).with_name("dist")
for ext in ("pdf", "docx"):
    (DIST / f"template.{ext}").replace(DIST / f"accidental-guide-template.{ext}")
(DIST / "guide.json").unlink(missing_ok=True)
