"""Render sample covers for each design direction, plus shelves.

Usage: covers.py            render everything into ../img
Every cover is drawn with ReportLab at 324 x 540 pt and rasterised at 2x with pypdfium2,
the same way the guides are built and rendered.
"""
import io, os, sys
from collections import Counter
from PIL import Image
import pypdfium2 as pdfium
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import white, HexColor
from reportlab.pdfbase import pdfmetrics

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *  # noqa
import pictograms as P

ROOT = os.path.normpath(os.path.join(HERE, ".."))
IMG = f"{ROOT}/img"
ENGR = os.path.expanduser("~/Claude/accidental-guides/engravings/clean")

SHELF = ["accidental-intelligence", "agents-harnesses-skills-tools", "context-windows", "claude-code",
         "specs-and-reviews", "chirping-smoke-detector", "grilled-cheese", "chess-first-move"]
FEATURE = ["specs-and-reviews", "chirping-smoke-detector", "chess-first-move", "accidental-intelligence"]

# Engraving per guide (from the shortlist's top picks), with a crop for direction D:
# (centre x, centre y, side as a fraction of the image's shorter side), normalised.
ENGRAVING = {
    "accidental-intelligence": ("collection-ai-1", True, (0.5, 0.42, 0.62)),
    "agents-harnesses-skills-tools": ("agents-2", False, (0.5, 0.22, 0.9)),
    "context-windows": ("context-1", False, (0.42, 0.62, 0.78)),
    "claude-code": ("harnesses-2", False, (0.42, 0.62, 0.8)),
    "specs-and-reviews": ("project-1", False, (0.5, 0.2, 0.95)),
    "chirping-smoke-detector": ("collection-house-2", True, (0.5, 0.42, 0.82)),
    "grilled-cheese": ("collection-table-1", True, (0.5, 0.36, 0.9)),
    "chess-first-move": ("collection-games-1", True, (0.62, 0.4, 0.75)),
}


def render(draw, path, scale=2):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(PW, PH)); draw(c); c.showPage(); c.save()
    im = pdfium.PdfDocument(buf.getvalue())[0].render(scale=scale).to_pil()
    im.save(path)
    return im


_cache = {}
def engraving(name, color=None, crop=None, max_px=900):
    """Clean engraving as an RGBA image, optionally recoloured and cropped square."""
    key = (name, color, crop)
    if key in _cache:
        return _cache[key]
    im = Image.open(f"{ENGR}/{name}.png").convert("RGBA")
    if crop:
        cx, cy, f = crop
        w, h = im.size; s = int(min(w, h) * f)
        x0 = int(min(max(cx * w - s / 2, 0), w - s)); y0 = int(min(max(cy * h - s / 2, 0), h - s))
        im = im.crop((x0, y0, x0 + s, y0 + s))
    im.thumbnail((max_px, max_px), Image.LANCZOS)
    if color:
        a = im.split()[3]
        im = Image.new("RGBA", im.size, color); im.putalpha(a)
    _cache[key] = im
    return im


def draw_rgba(c, im, x, y, w, h):
    c.drawImage(ImageReader(im), x, y, w, h, mask="auto")


def dominant_family(g):
    fams = [p["family"] for p in g["parts"]]
    cnt = Counter(fams); top = max(cnt.values())
    return next(f for f in fams if cnt[f] == top)


# ------------------------------------------------------------------ now
def cover_now(c, g):
    kicker(c)
    title_block(c, g, PH - MT - 22)
    current_tiles(c, g)
    edition(c, g)


# ------------------------------------------------------------------ engravings, as proposed
def cover_engraving(c, g):
    """The sample covers in engravings/covers/: the current cover with the engraving
    right-aligned in the band between the subtitle and the tiles (top at 180 pt)."""
    cover_now(c, g)
    name, is_coll, _ = ENGRAVING[g["slug"]]
    im = engraving(name)
    wmax = PW * (0.32 if is_coll else 0.27); hmax = 125 if is_coll else 120
    w, h = im.size; s = min(wmax / w, hmax / h)
    draw_rgba(c, im, PW - MR - w * s, PH - 180 - h * s, w * s, h * s)


# ------------------------------------------------------------------ A: signs
def cover_signs(c, g):
    kicker(c); series_line(c, g, PH - MT - 8)
    title_block(c, g, PH - MT - 22)
    side = 2 * W / 3; x = PW - MR - side; y = MB + 16
    c.setFillColor(BLOCK); c.rect(x, y, side, side, stroke=0, fill=1)
    P.draw(c, g["slug"], x, y, side, INK, paper=BLOCK, pad=2.5)
    contents_list(c, g, ML, y + side, W / 3 - 8)
    edition(c, g)


# ------------------------------------------------------------------ B: the part grid
def cover_grid(c, g, field_top=None):
    """Six columns, one per family, in the series' fixed order; one row per entry.
    A part's tile sits where its family column meets its entry row, so every guide's
    cover is a different pattern on the same grid."""
    kicker(c); series_line(c, g, PH - MT - 8)
    title_block(c, g, PH - MT - 22)
    cell = W / 6; gut = 1.5
    y0 = MB + 16; top = y0 + 6 * cell
    # column heads: the six families, always in this order, each with its colour
    c.setStrokeColor(INK); c.setLineWidth(0.6); c.line(ML, top + 14, PW - MR, top + 14)
    present = {p["family"] for p in g["parts"]}
    for j, f in enumerate(FAMILY_ORDER):
        hx = ML + j * cell + gut / 2
        if f in present:   # as design-direction.md asks: covered families filled, others outlined
            c.setFillColor(colors(f)[0]); c.rect(hx, top + 4.2, 4.6, 4.6, stroke=0, fill=1)
            c.setFont("Sans", 5.8); c.setFillColor(GREY)
        else:
            c.setStrokeColor(HexColor("#b8b8b8")); c.setLineWidth(0.5)
            c.rect(hx + 0.25, top + 4.45, 4.1, 4.1, stroke=1, fill=0)
            c.setFont("Sans", 5.8); c.setFillColor(HexColor("#a6a6a6"))
        c.drawString(hx + 7, top + 5, FAMILY_WORD[f])
    for i, p in enumerate(g["parts"]):
        j = FAMILY_ORDER.index(p["family"])
        x = ML + j * cell + gut / 2; y = top - (i + 1) * cell + gut / 2
        tile(c, p["key"], p["family"], x, y, cell - gut, number=p["num"])
        sub = f"{p['count']} parts" if "count" in p else f"page {p['page']}"
        ty = y + (cell - gut) / 2
        need = max(pdfmetrics.stringWidth(p["name"], "Sans-Bold", 7.2),
                   pdfmetrics.stringWidth(sub, "Sans", 6.4))
        if x + cell - gut + 5 + need <= PW - MR:
            tx = x + cell - gut / 2 + 5
            c.setFillColor(INK); c.setFont("Sans-Bold", 7.2); c.drawString(tx, ty + 1.5, p["name"])
            c.setFillColor(GREY); c.setFont("Sans", 6.4); c.drawString(tx, ty - 7, sub)
        else:
            tx = x - gut - 4
            c.setFillColor(INK); c.setFont("Sans-Bold", 7.2); c.drawRightString(tx, ty + 1.5, p["name"])
            c.setFillColor(GREY); c.setFont("Sans", 6.4); c.drawRightString(tx, ty - 7, sub)
    edition(c, g)


# ------------------------------------------------------------------ C: band and number
def cover_number(c, g):
    band = 176
    c.setFillColor(INK); c.rect(0, PH - band, PW, band, stroke=0, fill=1)
    kicker(c, color=white); series_line(c, g, PH - MT - 8, color=white, numbered=False,
                                         grey=white)
    n = len(g["lines"])
    text_lines(c, g["lines"], ML, PH - band + 14 + 27 * 0.24 + 29 * (n - 1) + 27, "Sans-Bold",
               27, 29, white)
    sub = wrap(g["subtitle"], "Sans", 9.4, W * 0.8)
    text_lines(c, sub, ML, PH - band - 14, "Sans", 9.4, 12.2, INK)
    num = f"{g['number']:02d}"
    size = 160
    c.setFillColor(INK); c.setFont("Sans-Bold", size)
    c.drawString(ML - size * 0.045, MB + 16, num)
    contents_list(c, g, ML + 2 * W / 3, MB + 16 + 6 * 27 - 4, W / 3)
    edition(c, g)


# ------------------------------------------------------------------ D: engraving, one colour, cropped
def cover_duotone(c, g):
    kicker(c); series_line(c, g, PH - MT - 8)
    title_block(c, g, PH - MT - 22)
    side = 2 * W / 3; x = PW - MR - side; y = MB + 16
    fam = dominant_family(g)
    name, _, crop = ENGRAVING[g["slug"]]
    base, _, fg = colors(fam)
    c.setFillColor(base); c.rect(x, y, side, side, stroke=0, fill=1)
    im = engraving(name, color="#111111" if fam == "Ru" else "#ffffff", crop=crop)
    draw_rgba(c, im, x, y, side, side)
    contents_list(c, g, ML, y + side, W / 3 - 8)
    edition(c, g)


def cover_duotone_mono(c, g):
    """The most restrained hybrid: ink lines on the grey block, cropped square."""
    kicker(c); series_line(c, g, PH - MT - 8)
    title_block(c, g, PH - MT - 22)
    side = 2 * W / 3; x = PW - MR - side; y = MB + 16
    name, _, crop = ENGRAVING[g["slug"]]
    c.setFillColor(BLOCK); c.rect(x, y, side, side, stroke=0, fill=1)
    draw_rgba(c, engraving(name, color="#111111", crop=crop), x, y, side, side)
    contents_list(c, g, ML, y + side, W / 3 - 8)
    edition(c, g)


DIRECTIONS = {
    "now": cover_now,
    "engraving": cover_engraving,
    "a-signs": cover_signs,
    "b-grid": cover_grid,
    "c-numbers": cover_number,
    "d-duotone": cover_duotone,
    "d-mono": cover_duotone_mono,
}


def shelf(images, path, w=240, gap=14, pad=28, bg=(236, 236, 234)):
    ims = [im.convert("RGB").resize((w, round(im.height * w / im.width)), Image.LANCZOS)
           for im in images]
    h = ims[0].height
    out = Image.new("RGB", (pad * 2 + len(ims) * w + (len(ims) - 1) * gap, pad * 2 + h), bg)
    for i, im in enumerate(ims):
        x = pad + i * (w + gap)
        out.paste((214, 214, 212), (x - 1, pad - 1, x + w + 1, pad + h + 1))
        out.paste(im, (x, pad))
    out.save(path)


def main(only=None):
    for d, fn in DIRECTIONS.items():
        if only and d not in only:
            continue
        os.makedirs(f"{IMG}/{d}", exist_ok=True)
        ims = []
        for slug in SHELF:
            ims.append(render(lambda c: fn(c, guide(slug)), f"{IMG}/{d}/{slug}.png"))
        shelf(ims, f"{IMG}/shelves/{d}.png")
        shelf(ims, f"{IMG}/shelves/{d}-thumb.png", w=96, gap=10, pad=16)
        print("rendered", d)


def series_b():
    """Direction B for every guide in the repo, and its pattern alone as a small mark."""
    os.makedirs(f"{IMG}/b-all", exist_ok=True)
    order = [s for coll in DATA["collections"] for s in coll["guides"] if s in DATA["guides"]]
    ims = [render(lambda c: cover_grid(c, guide(s)), f"{IMG}/b-all/{s}.png", scale=1) for s in order]
    shelf(ims[:12], f"{IMG}/shelves/b-all-1.png", w=150, gap=10, pad=16)
    shelf(ims[12:], f"{IMG}/shelves/b-all-2.png", w=150, gap=10, pad=16)
    # marks: the 6 x 6 pattern alone, for the site's lists, tabs and favicons
    cols, pitch_x, pitch_y, m = 8, 74, 84, 48
    rows = (len(order) + cols - 1) // cols
    W2, H2 = 14 + cols * pitch_x, rows * pitch_y + 10
    def marks(c):
        for k, s in enumerate(order):
            g = guide(s); u = m / 6
            ox = 14 + (k % cols) * pitch_x; oy = H2 - 12 - m - (k // cols) * pitch_y
            c.setStrokeColor(HAIR); c.setLineWidth(0.5); c.rect(ox, oy, m, m, stroke=1, fill=0)
            for i, p in enumerate(g["parts"]):
                j = FAMILY_ORDER.index(p["family"])
                c.setFillColor(colors(p["family"])[0])
                c.rect(ox + j * u, oy + m - (i + 1) * u, u, u, stroke=0, fill=1)
            c.setFillColor(INK); c.setFont("Sans", 5.4)
            for n, ln in enumerate(wrap(g["title"], "Sans", 5.4, 62)[:2]):
                c.drawString(ox, oy - 8 - n * 6.6, ln)
    buf = io.BytesIO(); cv = canvas.Canvas(buf, pagesize=(W2, H2))
    marks(cv); cv.showPage(); cv.save()
    pdfium.PdfDocument(buf.getvalue())[0].render(scale=2).to_pil().save(f"{IMG}/b-marks.png")
    print(len(order), "guides")


if __name__ == "__main__":
    if sys.argv[1:] == ["all-b"]:
        series_b()
    else:
        main(sys.argv[1:] or None)
