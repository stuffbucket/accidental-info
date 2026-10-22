"""Pictogram specimen: each sign on its construction grid, and at small sizes."""
import os, sys, io
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
import pypdfium2 as pdfium
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import INK, BLOCK, GREY
import pictograms as P

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "img", "signs")

def render(draw_fn, w, h, path, scale=2):
    buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=(w, h)); draw_fn(c); c.showPage(); c.save()
    pdfium.PdfDocument(buf.getvalue())[0].render(scale=scale).to_pil().save(path)

def sign_on_grid(slug, path, size=240):
    def fn(c):
        c.setFillColor(BLOCK); c.rect(0, 0, size, size, stroke=0, fill=1)
        u = size / 16
        c.setStrokeColor(HexColor("#c9c9c9")); c.setLineWidth(0.4)
        for i in range(17):
            c.line(i * u, 0, i * u, size); c.line(0, i * u, size, i * u)
        c.setStrokeColor(HexColor("#9a9a9a")); c.setLineWidth(0.8)
        c.rect(2 * u, 2 * u, 12 * u, 12 * u, stroke=1, fill=0)
        P.draw(c, slug, 0, 0, size, INK, paper=BLOCK)
    render(fn, size, size, path)

def sign_plain(slug, path, size=240, bg=BLOCK, ink=INK):
    def fn(c):
        c.setFillColor(bg); c.rect(0, 0, size, size, stroke=0, fill=1)
        P.draw(c, slug, 0, 0, size, ink, paper=bg)
    render(fn, size, size, path)

for s in P.SIGNS:
    sign_on_grid(s, f"{OUT}/{s}-grid.png")
    sign_plain(s, f"{OUT}/{s}.png")
    sign_plain(s, f"{OUT}/{s}-32.png", size=32)
print("ok")
