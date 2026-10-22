"""Shared drawing kit for the cover mockups.

Geometry, type, colours and the two-tone tile follow the guides' build_guide.py
(page 324 x 540 pt, margins 24/24/28/36, TeX Gyre Heros, INK #111111), so every
mockup differs from the real covers only where a direction says it should.
"""
import json, os
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = f"{HERE}/fonts"
pdfmetrics.registerFont(TTFont("Sans", f"{FONT_DIR}/heros-regular.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Bold", f"{FONT_DIR}/heros-bold.ttf"))
pdfmetrics.registerFont(TTFont("Mono", f"{FONT_DIR}/LiberationMono-Regular.ttf"))

PW, PH = 324, 540
ML, MR, MT, MB = 24, 24, 28, 36
W = PW - ML - MR
INK = HexColor("#111111")
GREY = HexColor("#5f5f5f")
BLOCK = HexColor("#ebebeb")   # the grey block from design-direction.md
HAIR = HexColor("#d4d4d4")

DATA = json.load(open(f"{HERE}/data.json"))
FAMILIES = DATA["families"]
FAM = {f["key"]: f for f in FAMILIES}
FAMILY_ORDER = [f["key"] for f in FAMILIES]
# One word per family, for column heads.
FAMILY_WORD = {"Ru": "Runs", "Wr": "Written", "Ck": "Checks", "Us": "Used", "Dm": "Decided",
               "Nu": "Counted"}
COLL = {c["id"]: c for c in DATA["collections"]}


def guide(slug):
    return DATA["guides"][slug]


def _dark(hexstr, f):
    h = hexstr.lstrip("#"); r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return HexColor("#%02x%02x%02x" % (int(r * f), int(g * f), int(b * f)))


def colors(family):
    base = FAM[family]["hex"]
    yellow = family == "Ru"
    return HexColor(base), _dark(base, 0.86 if yellow else 0.80), (INK if yellow else white)


def tile(c, key, family, x, y, size, number=None):
    """The guides' two-tone tile; (x, y) is the lower-left corner."""
    base, dark, fg = colors(family)
    c.setFillColor(base); c.rect(x, y, size, size, stroke=0, fill=1)
    if size >= 22:
        band = size * 0.26
        c.setFillColor(dark); c.rect(x, y, size, band, stroke=0, fill=1)
        fs = size * 0.40
        c.setFillColor(fg); c.setFont("Sans-Bold", fs)
        c.drawString(x + size * 0.13, y + band + (size - band) / 2 - fs * 0.34, key)
        if number:
            c.setFont("Sans-Bold", max(5.5, size * 0.14))
            c.drawString(x + size * 0.13, y + band * 0.30, number)
    else:
        fs = size * 0.46
        c.setFillColor(fg); c.setFont("Sans-Bold", fs)
        c.drawCentredString(x + size / 2, y + size / 2 - fs * 0.36, key)


def wrap(text, font, size, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


def text_lines(c, lines, x, ytop, font, size, leading, color=INK):
    """Draw lines with the first baseline at ytop - size*0.76; returns y below the block."""
    c.setFillColor(color); c.setFont(font, size)
    y = ytop - size * 0.76
    for ln in lines:
        c.drawString(x, y, ln); y -= leading
    return y + leading - size * 0.24


def kicker(c, color=INK, y=None):
    c.setFillColor(color); c.setFont("Sans-Bold", 9)
    c.drawString(ML, y if y is not None else PH - MT - 8, "An Accidental Guide to…")


def title_block(c, g, ytop, size=27, leading=29, sub_w=W * 0.8, color=INK, sub_color=INK,
                x=ML):
    y = text_lines(c, g["lines"], x, ytop, "Sans-Bold", size, leading, color)
    sub = wrap(g["subtitle"], "Sans", 9.4, sub_w)
    return text_lines(c, sub, x, y - 7, "Sans", 9.4, 12.2, sub_color)


def edition(c, g, y=MB - 6, rule_y=MB + 4, color=GREY):
    if rule_y is not None:
        c.setStrokeColor(INK); c.setLineWidth(1); c.line(ML, rule_y, PW - MR, rule_y)
    c.setFont("Sans", 6.4); c.setFillColor(color)
    c.drawString(ML, y, f"hi@accidental.info · October 2026 · Version {g['version']}")


# ---------- collection marks: the four Bauhaus primaries ----------
def coll_mark(c, coll_id, x, y, s, color=INK):
    """A collection's mark in an s x s box, lower-left (x, y)."""
    c.setFillColor(color)
    if coll_id == "intelligence":
        c.rect(x, y, s, s, stroke=0, fill=1)
    elif coll_id == "around-the-house":
        p = c.beginPath(); p.moveTo(x, y); p.lineTo(x + s, y); p.lineTo(x + s / 2, y + s * 0.92)
        p.close(); c.drawPath(p, stroke=0, fill=1)
    elif coll_id == "at-the-table":
        c.circle(x + s / 2, y + s / 2, s / 2, stroke=0, fill=1)
    else:
        p = c.beginPath(); p.moveTo(x + s / 2, y); p.lineTo(x + s, y + s / 2)
        p.lineTo(x + s / 2, y + s); p.lineTo(x, y + s / 2); p.close()
        c.drawPath(p, stroke=0, fill=1)


def series_line(c, g, y, color=INK, numbered=True, grey=GREY):
    """Right-aligned: [mark] Collection name  No. 11"""
    coll = COLL[g["collection"]]
    num = f"{g['number']:02d}"
    c.setFont("Sans-Bold", 7); c.setFillColor(color)
    x = PW - MR
    if numbered:
        c.drawRightString(x, y, num)
        x -= pdfmetrics.stringWidth(num, "Sans-Bold", 7) + 6
    c.setFont("Sans", 7); c.setFillColor(grey)
    c.drawRightString(x, y, coll["name"])
    x -= pdfmetrics.stringWidth(coll["name"], "Sans", 7) + 5
    coll_mark(c, g["collection"], x - 6.2, y - 0.4, 6.2, color)


def contents_list(c, g, x, ytop, width, tsize=15, row=27):
    """A compact contents list: small tile, name, page."""
    y = ytop
    for p in g["parts"]:
        tile(c, p["key"], p["family"], x, y - tsize, tsize)
        tx = x + tsize + 6
        fs = min(7.2, 7.2 * (width - tsize - 6) / pdfmetrics.stringWidth(p["name"], "Sans-Bold", 7.2))
        c.setFillColor(INK); c.setFont("Sans-Bold", fs)
        c.drawString(tx, y - 6.4, p["name"])
        c.setFillColor(GREY); c.setFont("Sans", 6.4)
        sub = f"{p['count']} parts" if "count" in p else f"page {p['page']}"
        c.drawString(tx, y - 14.4, sub)
        y -= row
    return y


def current_tiles(c, g, top=214):
    """The tile block exactly as page_cover draws it now."""
    size, colw = 38, W / 3
    for i, p in enumerate(g["parts"]):
        col, r = i % 3, i // 3
        x = ML + col * colw
        yb = top - r * 80 - size
        tile(c, p["key"], p["family"], x, yb, size, number=p["num"])
        c.setFillColor(INK); c.setFont("Sans-Bold", 7.6)
        c.drawString(x, yb - 11, p["name"])
        c.setFillColor(GREY); c.setFont("Sans", 6.6)
        c.drawString(x, yb - 20, f"{p['count']} parts" if "count" in p else f"page {p['page']}")
