"""Render covers and a few pages of the existing guides for reference."""
import sys, glob, os, pypdfium2 as pdfium
REPO = os.path.expanduser("~/github/stuffbucket/accidental-info")
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for pdf in sorted(glob.glob(f"{REPO}/guides/*/dist/*.pdf") + glob.glob(f"{REPO}/drafts/*/dist/*.pdf")):
    slug = os.path.basename(pdf)[:-4]
    doc = pdfium.PdfDocument(pdf)
    pages = [0, 1, 2, 3] if slug in ("specs-and-reviews", "context-windows", "accidental-intelligence", "grilled-cheese") else [0]
    for i in pages:
        if i < len(doc):
            doc[i].render(scale=1.0).to_pil().save(f"{out}/{slug}-p{i}.png")
    print(slug, len(doc), doc[0].get_size())
