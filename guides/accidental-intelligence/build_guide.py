"""Build the pocket guide PDF.

Run from anywhere:  python3 build_guide.py [output.pdf]
Default output:     accidental-intelligence.pdf in the current directory.

Everything the build needs is in this folder: content.py (all text), this script (layout),
and fonts/ (the exact font files used). Output is deterministic (ReportLab invariant mode),
so a rebuild with the pinned packages in requirements.txt is byte-identical to the shipped
PDF. The SHA-256 of the expected PDF is in expected.sha256.
"""
import hashlib, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.colors import HexColor, white

# ---------- fonts: TeX Gyre Heros (Helvetica clone) converted CFF -> TrueType ----------
HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
# Source fonts: TeX Gyre Heros 2.004 (OpenType/CFF) and Liberation Mono 1.07.4 (TrueType).
GYRE = os.path.join(FONT_DIR, "texgyreheros-{}.otf")
MONO = os.path.join(FONT_DIR, "LiberationMono-Regular.ttf")

def otf_to_ttf(src, dst):
    from fontTools.ttLib import TTFont as FT, newTable
    from fontTools.pens.cu2quPen import Cu2QuPen
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    f = FT(src); gs = f.getGlyphSet(); glyf = {}
    for n in f.getGlyphOrder():
        p = TTGlyphPen(gs); gs[n].draw(Cu2QuPen(p, 1.0, reverse_direction=True)); glyf[n] = p.glyph()
    f["loca"] = newTable("loca"); f["glyf"] = g = newTable("glyf")
    g.glyphOrder = f.getGlyphOrder(); g.glyphs = glyf
    del f["CFF "]
    f["maxp"] = m = newTable("maxp"); m.tableVersion = 0x00010000
    for a in ("maxZones", "maxTwilightPoints", "maxStorage", "maxFunctionDefs", "maxInstructionDefs",
              "maxStackElements", "maxSizeOfInstructions", "maxComponentElements"):
        setattr(m, a, 0)
    m.maxZones = 1
    post = f["post"]; post.formatType = 2.0; post.extraNames = []; post.mapping = {}
    post.glyphOrder = f.getGlyphOrder()
    f["head"].glyphDataFormat = 0
    f.sfntVersion = "\x00\x01\x00\x00"
    f.save(dst)  # note: fontTools stamps head.modified; the shipped .ttf files are the ones used

os.makedirs(FONT_DIR, exist_ok=True)
for s in ("regular", "bold", "italic"):
    dst = f"{FONT_DIR}/heros-{s}.ttf"
    if not os.path.exists(dst):
        otf_to_ttf(GYRE.format(s), dst)
pdfmetrics.registerFont(TTFont("Sans", f"{FONT_DIR}/heros-regular.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Bold", f"{FONT_DIR}/heros-bold.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Italic", f"{FONT_DIR}/heros-italic.ttf"))
pdfmetrics.registerFont(TTFont("Serif-Italic", f"{FONT_DIR}/newsreader-italic.ttf"))
pdfmetrics.registerFont(TTFont("Mono", MONO))
addMapping("Sans", 0, 0, "Sans"); addMapping("Sans", 1, 0, "Sans-Bold")
addMapping("Sans", 0, 1, "Sans-Italic"); addMapping("Sans", 1, 1, "Sans-Bold")

# ---------- page geometry (4.5 x 7.5 in) ----------
PW, PH = 324, 540
ML, MR, MT, MB = 24, 24, 28, 36
W = PW - ML - MR
LABW, GAP = 62, 8
TX = ML + LABW + GAP
TW = PW - MR - TX

INK = HexColor("#111111")
GREY = HexColor("#5f5f5f")
HAIR = HexColor("#bdbdbd")

# Colorway from the supplied swatch (bg tokens): base, darker secondary, text colour.
def _dark(h, f=0.80):
    h = h.lstrip("#"); r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return HexColor("#%02x%02x%02x" % (int(r * f), int(g * f), int(b * f)))
TOKENS = {  # token: base hex
    "brand": "#0D99FF", "figjam": "#9747FF", "danger": "#F24822",
    "warning": "#FFCD29", "success": "#14AE5C", "assistive": "#E83FBF",
}
# The color families: each color is one kind of thing, the same for every guide in the series
# (see packages/editorial/registry.md). The catalog's own tiles are the six families,
# keyed as in guide.md; every part on the map takes its family's color. The family for each
# color was picked to keep the most parts at the color they had under the entry-number rule.
FAMILY_TOKEN = {"Ru": "warning", "Wr": "brand", "Ck": "figjam", "Us": "danger", "Dm": "success",
                "Nu": "assistive"}
assert set(FAMILY_TOKEN) == {f["key"] for f in C.FAMILIES}
PART_TOKEN = dict(FAMILY_TOKEN)
for _p in C.PARTS:
    assert PART_TOKEN.setdefault(_p["key"], FAMILY_TOKEN[_p["family"]]) == FAMILY_TOKEN[_p["family"]], _p
def colors(mono_key):
    t = PART_TOKEN[mono_key]; base = TOKENS[t]
    fg = INK if t == "warning" else white
    return HexColor(base), _dark(base, 0.86 if t == "warning" else 0.80), fg
# Guide names have no tile: the tiles in tables belong to the parts and the families.
NAME2MONO = {}
# The cover sets the title on these lines.
COVER_LINES = ("Accidental", "Intelligence")
assert " ".join(COVER_LINES) == C.TITLE, C.TITLE

# ---------- vertical rhythm (points) ----------
# One set of spacings used on every page so the pages read the same way.
SP_TITLE = 26      # title baseline area to first content
SP_PARA = 6        # between paragraphs
SP_SECTION = 16    # before a subhead or a labelled group

BODY = ParagraphStyle("body", fontName="Sans", fontSize=7.6, leading=10.4, textColor=INK)
SMALL = ParagraphStyle("small", fontName="Sans", fontSize=7.0, leading=9.4, textColor=INK)
SMALLG = ParagraphStyle("smallg", parent=SMALL, textColor=GREY)
SMALLB = ParagraphStyle("smallb", parent=SMALL, fontName="Sans-Bold")
LABEL = ParagraphStyle("label", fontName="Sans-Bold", fontSize=6.8, leading=9.4, textColor=INK)
LEAD = ParagraphStyle("lead", fontName="Sans", fontSize=8.6, leading=11.8, textColor=INK)
CELL = ParagraphStyle("cell", fontName="Sans", fontSize=6.6, leading=8.6, textColor=INK)
CELLG = ParagraphStyle("cellg", parent=CELL, textColor=GREY)
CELLB = ParagraphStyle("cellb", parent=CELL, fontName="Sans-Bold")
CELLH = ParagraphStyle("cellh", parent=CELL, fontName="Sans-Bold", textColor=GREY)

MONO_RE = re.compile(r"(?<![\w/.<])((?:\.?[\w-]+/)+[\w.-]*|[\w-]+\.(?:md|sh|yml|yaml)\b|/[a-z][\w-]+)")

def mono(text, size):
    return MONO_RE.sub(lambda m: f'<font name="Mono" size="{size*0.9:.2f}">{m.group(1)}</font>', text)

PROBLEMS = []

def para(c, text, style, x, ytop, w):
    p = Paragraph(mono(text, style.fontSize), style)
    _, h = p.wrap(w, 1000)
    p.drawOn(c, x, ytop - h)
    return ytop - h

def rule(c, y, x0=ML, x1=PW - MR, weight=0.3, color=HAIR):
    c.setStrokeColor(color); c.setLineWidth(weight); c.line(x0, y, x1, y)

def row(c, label, text, y, style=SMALL, pad=4.5, weight=0.3, color=HAIR, lstyle=LABEL):
    rule(c, y, weight=weight, color=color)
    y -= pad
    yl = para(c, label, lstyle, ML, y, LABW)
    yt = para(c, text, style, TX, y, TW)
    return min(yl, yt) - pad + 1

def first(i):
    return dict(weight=(1 if i == 0 else 0.3), color=(INK if i == 0 else HAIR))

def title(c, text, y=None):
    y = PH - MT if y is None else y
    c.setFillColor(INK); c.setFont("Sans-Bold", 17)
    c.drawString(ML, y - 15, text)
    return y - 26

def avatar(c, key, x, y, size, number=None):
    """Two-tone monogram tile; (x, y) is the lower-left corner."""
    if key not in PART_TOKEN:
        return  # not a part or a family: no tile
    base, dark, fg = colors(key)
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

def tag(c, name, x, ytop, size=10, style=LABEL, w=LABW):
    """Small colour tile followed by a part name; returns bottom y."""
    key = NAME2MONO.get(name)
    if key is not None:
        avatar(c, key, x, ytop - size, size)
        return para(c, name, style, x + size + 4, ytop - 0.5, w - size - 4)
    return para(c, name, style, x, ytop, w)

def footer(c, n):
    c.setFont("Sans", 6); c.setFillColor(GREY)
    c.drawString(ML, MB - 16, C.RUNNING_FOOTER)
    c.drawRightString(PW - MR, MB - 16, str(n))

def check(name, y):
    if y < MB:
        PROBLEMS.append(f"{name}: content reaches y={y:.1f}, below bottom margin {MB}")
    return y

def subhead(c, text, y, with_rule=True):
    """Subhead. With a rule, the heavy rule sits directly under the subhead text. Tables skip
    the rule because their column header row carries it."""
    c.setFillColor(INK); c.setFont("Sans-Bold", 11); c.drawString(ML, y - 10, text)
    y -= 16
    if not with_rule:
        return y - 2
    rule(c, y, weight=1, color=INK)
    return y - 6

TITLE_ST = ParagraphStyle("title", fontName="Sans-Bold", fontSize=17, leading=19, textColor=INK)

def plain_title(c, text):
    """A page title with no corner tile that may break with <br/>. One line sits exactly where
    title() puts it, and content starts the same distance below the last line."""
    p = Paragraph(text, TITLE_ST)
    _, h = p.wrap(W, 200)
    p.drawOn(c, ML, PH - MT - h + 2)
    return PH - MT - h + 2 - 9

def arrow_head(c, x, y, direction):
    s = 3.2
    p = c.beginPath()
    if direction == "down":
        p.moveTo(x, y); p.lineTo(x - s * 0.7, y + s); p.lineTo(x + s * 0.7, y + s)
    elif direction == "up":
        p.moveTo(x, y); p.lineTo(x - s * 0.7, y - s); p.lineTo(x + s * 0.7, y - s)
    elif direction == "right":
        p.moveTo(x, y); p.lineTo(x - s, y + s * 0.7); p.lineTo(x - s, y - s * 0.7)
    else:  # left
        p.moveTo(x, y); p.lineTo(x + s, y + s * 0.7); p.lineTo(x + s, y - s * 0.7)
    p.close(); c.setFillColor(INK); c.drawPath(p, stroke=0, fill=1)

def note(c, text, y, style=SMALL):
    """A closing note under a heavy rule."""
    rule(c, y, weight=1, color=INK)
    return para(c, text, style, ML, y - 6, W)

def table(c, cols, rows, widths, y):
    xs = [ML]
    for w_ in widths[:-1]:
        xs.append(xs[-1] + w_)
    # A header can wrap; the first row starts under the deepest one.
    low = y
    for j, h in enumerate(cols):
        low = min(low, para(c, h, CELLH, xs[j], y, widths[j] - 6))
    y = low - 3.4
    for i, r in enumerate(rows):
        rule(c, y, **first(i))
        y -= 3.5
        low = y
        for j, v in enumerate(r):
            if j == 0:
                low = min(low, tag(c, v, xs[0], y, size=9, style=CELLB, w=widths[0] - 4))
            else:
                low = min(low, para(c, v, CELL, xs[j], y, widths[j] - 6))
        y = low - 3
    return y

# ---------- pages ----------
FAM_ORDER = [f["key"] for f in C.FAMILIES]

def parts_of(guide):
    """A guide's parts from the map, in family order, then in the order guide.md lists them."""
    ps = [p for p in C.PARTS if p["guide"] == guide]
    return sorted(ps, key=lambda p: FAM_ORDER.index(p["family"]))

def members(fam):
    """Each part name in a family once, in map order."""
    seen = []
    for p in C.PARTS:
        if p["family"] == fam and p["name"] not in seen:
            seen.append(p["name"])
    return seen

def page_cover(c):
    c.setFillColor(INK); c.setFont("Sans-Bold", 9)
    c.drawString(ML, PH - MT - 8, C.KICKER)
    y = PH - MT - 22
    st = ParagraphStyle("t", fontName="Sans-Bold", fontSize=27, leading=29, textColor=INK)
    y = para(c, "<br/>".join(COVER_LINES), st, ML, y, W)
    y = para(c, C.SUBTITLE, LEAD, ML, y - 8, W * 0.8)
    size, colw = 38, W / 3
    top = 214
    for i, f in enumerate(C.FAMILIES):
        col, r = i % 3, i // 3
        x = ML + col * colw
        yb = top - r * 80 - size
        avatar(c, f["key"], x, yb, size)
        c.setFillColor(INK); c.setFont("Sans-Bold", 7.6)
        c.drawString(x, yb - 11, f["name"])
        c.setFillColor(GREY); c.setFont("Sans", 6.6)
        c.drawString(x, yb - 20, f"{len(members(f['key']))} parts")
    rule(c, MB + 4, weight=1, color=INK)
    c.setFont("Sans", 6.4); c.setFillColor(GREY)
    c.drawString(ML, MB - 6, f"{C.COVER_FOOTER} · Version {C.VERSION}")
    tagline(c)
    check("cover", y)

WHY_WIDTHS = [104, W - 150, 46]

def page_why(c, n):
    y = plain_title(c, C.WHY_TITLE)
    for t in C.WHY_INTRO:
        y = para(c, t, BODY, ML, y, W) - SP_PARA
    y -= SP_SECTION - SP_PARA - 4
    y = table(c, C.WHY_COLS, C.WHY_ROWS, WHY_WIDTHS, y)
    footer(c, n); check("why", y)

# The reading-order diagram: guides as boxes on a three-column grid, arrows between them.
# build_docx.py crops the same box out of the PDF, using start_layout().
BOX_W, BOX_H = 80, 42
ROW_GAP = 20
SQ = 5            # one small square per part, in its family's color

def start_layout():
    """Top of the diagram, the top of each row, the bottom of the diagram, and each column's
    centre."""
    top = PH - MT - 30
    rows = [top - i * (BOX_H + ROW_GAP) for i in range(len(C.START_GRID))]
    cols = [ML + BOX_W / 2 + i * (W - BOX_W) / 2 for i in range(3)]
    return top, rows, rows[-1] - BOX_H, cols

GUIDE_BOX = ParagraphStyle("guidebox", fontName="Sans-Bold", fontSize=6.6, leading=7.8, textColor=INK)

def guide_box(c, name, xc, ytop):
    x = xc - BOX_W / 2
    c.setFillColor(white); c.setStrokeColor(INK); c.setLineWidth(0.8)
    if name in C.DRAFTS:
        c.setDash(2, 1.6)
    c.rect(x, ytop - BOX_H, BOX_W, BOX_H, stroke=1, fill=1)
    c.setDash()
    para(c, name, GUIDE_BOX, x + 5, ytop - 4.5, BOX_W - 10)
    for i, p in enumerate(parts_of(name)):
        base, _, _ = colors(p["key"])
        c.setFillColor(base)
        c.rect(x + 5 + i * (SQ + 1.6), ytop - BOX_H + 5, SQ, SQ, stroke=0, fill=1)

def page_start(c, n):
    title(c, C.START_TITLE)
    top, rows, bottom, cols = start_layout()
    where = {}
    for r, cells in enumerate(C.START_GRID):
        for k, name in enumerate(cells):
            if name:
                where[name] = (cols[k], rows[r])
    # Arrows first, so the boxes sit on top of them.
    c.setStrokeColor(INK); c.setLineWidth(0.6)
    for a, b in C.START_NEXT:
        (xa, ya), (xb, yb) = where[a], where[b]
        if ya == yb:  # the same row: across, from one box's side to the other's
            s = 1 if xb > xa else -1
            x0, x1, ym = xa + s * BOX_W / 2, xb - s * BOX_W / 2, ya - BOX_H / 2
            c.line(x0, ym, x1 - s * 3, ym); arrow_head(c, x1, ym, "right" if s > 0 else "left")
        else:  # down to the middle of the gap, across, and down into the box
            y0 = ya - BOX_H; ym = (y0 + yb) / 2
            c.line(xa, y0, xa, ym); c.line(xa, ym, xb, ym); c.line(xb, ym, xb, yb + 3)
            arrow_head(c, xb, yb, "down")
    for name, (x, yt) in where.items():
        guide_box(c, name, x, yt)
    y = note(c, C.START_NOTE, bottom - 14) - SP_SECTION
    y = table(c, C.START_COLS, C.START_ROWS, START_WIDTHS, y)
    footer(c, n); check("start", y)

START_WIDTHS = [124, W - 124]

FAM_TILE = 24

def page_colours(c, n):
    y = plain_title(c, C.COL_TITLE)
    for t in C.COL_INTRO:
        y = para(c, t, BODY, ML, y, W) - SP_PARA
    y -= SP_SECTION - SP_PARA - 4
    tx = ML + FAM_TILE + 10; tw = PW - MR - tx
    for i, f in enumerate(C.FAMILIES):
        rule(c, y, **first(i))
        y -= 5
        avatar(c, f["key"], ML, y - FAM_TILE, FAM_TILE)
        yt = para(c, f["name"], SMALLB, tx, y, tw)
        yt = para(c, f["holds"], SMALL, tx, yt, tw)
        yt = para(c, ", ".join(members(f["key"])), CELLG, tx, yt - 1.5, tw)
        y = min(y - FAM_TILE, yt) - 5
    y = note(c, C.COL_NOTE, y - 4)
    footer(c, n); check("colours", y)

MAP_TAG = 9         # tile size on the map
MAP_LINE = 12.5     # one line of tiles and names

def map_rows(c, y):
    """One group per guide: its short title, then its parts as tiles and names, wrapped.
    With c None, only measures. Returns the bottom."""
    for i, g in enumerate(C.GUIDES):
        if c: rule(c, y, **first(i))
        y -= 4
        label = g + ("  (draft)" if g in C.DRAFTS else "")
        if c:
            c.setFillColor(INK); c.setFont("Sans-Bold", 6.8); c.drawString(ML, y - 6.8, g)
            if g in C.DRAFTS:
                c.setFillColor(GREY); c.setFont("Sans", 6.4)
                c.drawString(ML + pdfmetrics.stringWidth(g + "  ", "Sans-Bold", 6.8), y - 6.8, "draft")
        y -= 11
        x = ML
        for p in parts_of(g):
            w = MAP_TAG + 3 + pdfmetrics.stringWidth(p["name"], "Sans", 6.6)
            if x > ML and x + w > PW - MR:
                x = ML; y -= MAP_LINE
            if c:
                avatar(c, p["key"], x, y - MAP_TAG, MAP_TAG)
                c.setFillColor(INK); c.setFont("Sans", 6.6); c.drawString(x + MAP_TAG + 3, y - 6.9, p["name"])
            x += w + 9
        y -= MAP_LINE + 1
    return y

def map_layout():
    """Top and bottom of the map, for build_docx.py, which crops it out of the PDF."""
    y = PH - MT - 26
    p = Paragraph(mono(C.MAP_INTRO, BODY.fontSize), BODY)
    _, h = p.wrap(W, 1000)
    top = y - h - SP_SECTION + 4
    return top, map_rows(None, top)

def page_map(c, n):
    title(c, C.MAP_TITLE)
    para(c, C.MAP_INTRO, BODY, ML, PH - MT - 26, W)
    top, _ = map_layout()
    y = map_rows(c, top)
    y = note(c, C.MAP_NOTE, y - 4)
    footer(c, n); check("map", y)

VERSION_OF = {r[0]: r[2] for r in C.WHY_ROWS}

def page_cards(c, n, pg):
    """A guide per card: its short title with its version on the right, then rows."""
    y = title(c, pg["title"]) - 4
    for k, card in enumerate(pg["cards"]):
        if k:
            y -= SP_SECTION - 4
        c.setFillColor(GREY); c.setFont("Sans", 6.4)
        c.drawRightString(PW - MR, y - 10, f"version {VERSION_OF[card['name']]}")
        y = subhead(c, card["name"], y, with_rule=False)
        items = [("Parts", ", ".join(p["name"] for p in C.PARTS if p["guide"] == card["name"]))]
        items += card["rows"]
        for i, (l, t) in enumerate(items):
            y = row(c, l, t, y, **first(i))
    footer(c, n); check(f"cards {pg['title']}", y)

STAR_LABEL, STAR_TEXT, STAR_URL = "Leave a star: ", "accidental.info/star", "https://accidental.info/star/"

TAGLINE = "My friend has a lot of questions."

def tagline(c):
    """The series' line, right-aligned above the footer's rule on the cover and the end page.
    It is the only serif in a guide: Newsreader Italic."""
    c.setFillColor(INK); c.setFont("Serif-Italic", 9)
    c.drawRightString(ML + W, MB + 15, TAGLINE)

def link(c, x, y, text, font, size, url):
    """Draw text at (x, y) in the current colour and make just that text a link to url."""
    c.setFont(font, size)
    c.drawString(x, y, text)
    w = pdfmetrics.stringWidth(text, font, size)
    c.linkURL(url, (x, y - 0.25 * size, x + w, y + 0.8 * size), relative=0, thickness=0)

def page_end(c):
    """End page: a note on versions at the top, colophon at the bottom. No page number."""
    y = title(c, C.END_TITLE)
    for t in C.END_INTRO:
        y = para(c, t, BODY, ML, y, W) - SP_PARA
    size, gap = 20, 6
    yb = MB + 64
    check("end", y)
    # colophon
    for i, f in enumerate(C.FAMILIES):
        avatar(c, f["key"], ML + i * (size + gap), yb, size)
    c.setFillColor(GREY); c.setFont("Sans", 6.4)
    c.drawString(ML, yb - 12, C.KICKER)
    c.setFillColor(INK); c.setFont("Sans-Bold", 7.6)
    c.drawString(ML, yb - 22, C.TITLE)
    c.setFillColor(GREY); c.setFont("Sans", 6.4)
    c.drawString(ML, yb - 31, C.SUBTITLE)
    c.drawString(ML, yb - 40, "Written and reviewed by a person. AI does the grunt work. Set in TeX Gyre Heros and Newsreader.")
    c.drawString(ML, yb - 49, STAR_LABEL)
    link(c, ML + pdfmetrics.stringWidth(STAR_LABEL, "Sans", 6.4), yb - 49, STAR_TEXT,
         "Mono", 5.9, STAR_URL)  # mono at the size of the sources' addresses
    rule(c, MB + 4, weight=1, color=INK)
    c.setFont("Sans", 6.4); c.setFillColor(GREY)
    tagline(c)
    c.setFont("Sans", 6.4); c.setFillColor(GREY)
    mail = C.EDITION.split(" · ")[0]
    if "@" in mail:  # the address for mistakes opens a new email
        link(c, ML, MB - 6, mail, "Sans", 6.4, f"mailto:{mail}")
        c.setFont("Sans", 6.4)
        c.drawString(ML + pdfmetrics.stringWidth(mail, "Sans", 6.4), MB - 6, C.EDITION[len(mail):])
    else:
        c.drawString(ML, MB - 6, C.EDITION)

def build(out):
    c = canvas.Canvas(out, pagesize=(PW, PH), invariant=1)
    c.setTitle(C.TITLE); c.setAuthor("Accidental Guides"); c.setSubject(C.SUBTITLE)
    page_cover(c); c.showPage()
    n = 2
    for fn in (page_why, page_start, page_colours, page_map):
        fn(c, n); c.showPage(); n += 1
    for pg in C.CARD_PAGES:
        page_cards(c, n, pg); c.showPage(); n += 1
    page_end(c); c.showPage(); n += 1
    c.save()
    return n - 1

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "accidental-intelligence.pdf"
    pages = build(out)
    print(f"wrote {out}: {pages} pages")
    print("\n".join(PROBLEMS) if PROBLEMS else "no overflow")
    digest = hashlib.sha256(open(out, "rb").read()).hexdigest()
    print(f"sha256 {digest}")
    exp = os.path.join(HERE, "expected.sha256")
    if os.path.exists(exp):
        want = open(exp).read().split()[0]
        print("matches expected.sha256" if digest == want else f"DIFFERS from expected.sha256 ({want})")
