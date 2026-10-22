"""B-prime: a Unigrid-style band across the top, and direction B's part grid below.

Reuses the study's kit (page geometry, fonts, tiles, data) from ../../scripts.
Usage: bprime.py [variant]    render B' covers, shelves and the site mock into ../img
"""
import io, os, sys
from PIL import Image
import pypdfium2 as pdfium
from reportlab.pdfgen import canvas
from reportlab.lib.colors import white, HexColor
from reportlab.pdfbase import pdfmetrics

HERE_BP = os.path.dirname(os.path.abspath(__file__))
STUDY = os.path.normpath(os.path.join(HERE_BP, "..", ".."))
sys.path.insert(0, f"{STUDY}/scripts")
from kit import *  # noqa  (PW, PH, ML, MR, MT, MB, W, INK, GREY, tile, colors, ...)
from covers import render, shelf, SHELF, cover_grid

IMG = os.path.normpath(os.path.join(HERE_BP, "..", "img"))
WORK = os.path.normpath(os.path.join(HERE_BP, "..", "work"))
BAND_GREY = HexColor("#a8a8a8")   # secondary text on the black band


# ------------------------------------------------------------------ the part grid, as in B
def part_grid(c, g, y0=MB + 16):
    """Direction B's grid, unchanged: six family columns, one row per entry."""
    cell = W / 6; gut = 1.5
    top = y0 + 6 * cell
    c.setStrokeColor(INK); c.setLineWidth(0.6); c.line(ML, top + 14, PW - MR, top + 14)
    present = {p["family"] for p in g["parts"]}
    for j, f in enumerate(FAMILY_ORDER):
        hx = ML + j * cell + gut / 2
        if f in present:
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
    return top + 14   # the head rule


# ------------------------------------------------------------------ the band
def band(c, g, h, fill=INK, fg=white, sub=BAND_GREY, mark=18, kicker_size=9, row=None):
    """Full-bleed band, height h, from the top edge. Kicker left; collection name and
    number right, then the collection mark, hung from one top line like Unigrid's."""
    coll = COLL[g["collection"]]
    row = row or h / 2
    c.setFillColor(fill); c.rect(0, PH - h, PW, h, stroke=0, fill=1)
    axis = PH - row              # the row's centre line
    base = axis - kicker_size * 0.36
    c.setFillColor(fg); c.setFont("Sans-Bold", kicker_size)
    c.drawString(ML, base, "An Accidental Guide to…")
    # the mark: right margin, centred on the axis
    mx = PW - MR - mark
    coll_mark(c, g["collection"], mx, axis - mark / 2, mark, fg)
    x = mx - 8
    num = f"{g['number']:02d}"
    c.setFont("Sans-Bold", kicker_size); c.setFillColor(fg)
    c.drawRightString(x, base, num)
    x -= pdfmetrics.stringWidth(num, "Sans-Bold", kicker_size) + 6
    c.setFont("Sans", kicker_size * 0.84); c.setFillColor(sub)
    c.drawRightString(x, base, coll["name"])


# ------------------------------------------------------------------ the covers
GRID_Y0 = MB + 12  # B's grid, unchanged, set 4 pt lower (B: MB + 16) to make room for the band
BAND = 150         # fixed for every guide, as Unigrid's band is
BAND_ROW = 24      # centre of the kicker row, from the top edge
TITLE_FOOT = 16    # last title baseline above the band's foot


def cover_bprime(c, g, fill=INK):
    """B': kicker, collection, number and mark in the band's top row; the title, white,
    set on the band's foot; the subtitle on white below; B's part grid in the field."""
    band(c, g, BAND, fill=fill, mark=16, kicker_size=9, row=BAND_ROW)
    n = len(g["lines"])
    base = PH - BAND + TITLE_FOOT
    text_lines(c, g["lines"], ML, base + 27 * 0.76 + 29 * (n - 1), "Sans-Bold", 27, 29, white)
    sub = wrap(g["subtitle"], "Sans", 9.4, W * 0.8)
    text_lines(c, sub, ML, PH - BAND - 12, "Sans", 9.4, 12.2, INK)
    part_grid(c, g, GRID_Y0)
    edition(c, g)


def cover_thin(c, g, h=52):
    """The alternative tried: a thin band (kicker, collection, mark) with the title on white."""
    band(c, g, h, mark=20, kicker_size=9.5)
    title_block(c, g, PH - h - 18)
    part_grid(c, g, GRID_Y0)
    edition(c, g)


def main():
    for d in ("b-prime", "b-prime-all", "b-extra", "thin", "shelves"):
        os.makedirs(f"{IMG}/{d}", exist_ok=True)
    ims = [render(lambda c: cover_bprime(c, guide(s)), f"{IMG}/b-prime/{s}.png") for s in SHELF]
    shelf(ims, f"{IMG}/shelves/b-prime.png")
    shelf(ims, f"{IMG}/shelves/b-prime-thumb.png", w=96, gap=10, pad=16)
    # siblings, at 2x, for the identity pair: B' and B
    for s in ("claude-desktop", "copilot-cli", "codex"):
        render(lambda c: cover_bprime(c, guide(s)), f"{IMG}/b-prime/{s}.png")
        render(lambda c: cover_grid(c, guide(s)), f"{IMG}/b-extra/{s}.png")
    # every guide, at 1x, for the site mock
    order = [s for coll in DATA["collections"] for s in coll["guides"] if s in DATA["guides"]]
    for s in order:
        render(lambda c: cover_bprime(c, guide(s)), f"{IMG}/b-prime-all/{s}.png", scale=1)
    # the thin-band alternative, for two guides
    for s in ("agents-harnesses-skills-tools", "claude-code"):
        render(lambda c: cover_thin(c, guide(s)), f"{IMG}/thin/{s}.png")
    print("rendered", len(order), "guides")


if __name__ == "__main__":
    main()
