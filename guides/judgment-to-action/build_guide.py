"""Build the pocket guide PDF.

Run from anywhere:  python3 build_guide.py [output.pdf]
Default output:     judgment-to-action.pdf in the current directory.

Everything the build needs is in this folder: content.py (all text), this script (layout),
and fonts/ (the exact font files used). Output is deterministic (ReportLab invariant mode),
so a rebuild with the pinned packages in requirements.txt is byte-identical to the shipped
PDF. The SHA-256 of the expected PDF is in expected.sha256.
"""
import hashlib, io, os, re, sys
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
PANEL = HexColor("#ebebeb")  # the background of a grey block
PAD = 7                      # inside a grey block or callout; the box reaches this far into the margin

# Colorway from the supplied swatch (bg tokens): base, darker secondary, text colour.
def _dark(h, f=0.80):
    h = h.lstrip("#"); r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return HexColor("#%02x%02x%02x" % (int(r * f), int(g * f), int(b * f)))
TOKENS = {  # token: base hex
    "brand": "#0D99FF", "figjam": "#9747FF", "danger": "#F24822",
    "warning": "#FFCD29", "success": "#14AE5C", "assistive": "#E83FBF",
}
# Each color is one family, the same in every guide of the series
# (packages/editorial/registry.md).
FAMILY_TOKEN = {"Ru": "warning", "Wr": "figjam", "Ck": "success", "Us": "danger", "Dm": "assistive",
                "Nu": "brand"}
PART_FAMILY = {
    "Po": "Dm",
    "Td": "Dm",
    "Rp": "Dm",
    "Lc": "Wr",
}
PART_TOKEN = {k: FAMILY_TOKEN[f] for k, f in PART_FAMILY.items()}
def colors(mono_key):
    t = PART_TOKEN[mono_key]; base = TOKENS[t]
    fg = INK if t == "warning" else white
    return HexColor(base), _dark(base, 0.86 if t == "warning" else 0.80), fg
NAME2MONO = {
    "Policy": "Po",
    "Policies": "Po",
    "Threshold": "Td",
    "Thresholds": "Td",
    "Review path": "Rp",
    "Review paths": "Rp",
    "Labeled case": "Lc",
    "Labeled cases": "Lc",
}
# Any other name is plain text with no tile.
# The cover sets the title on these lines.
COVER_LINES = ("From", "Judgment to", "Action")
assert " ".join(COVER_LINES) == C.TITLE, C.TITLE

# ---------- vertical rhythm (points) ----------
# One set of spacings used on every page so the pages read the same way.
SP_TITLE = 26      # title baseline area to first content
SP_TILE = 18       # bottom of a corner tile to first content
SP_PARA = 6        # between paragraphs
SP_SECTION = 16    # before a subhead or a labelled group
TILE = 46

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

def bold_first(text):
    i = text.find(". ")
    return text if i < 0 else f"<b>{text[:i + 1]}</b>{text[i + 1:]}"

def short_detail(short, detail):
    return f"<b>{short}.</b> {detail}" if detail else f"<b>{short}.</b>"

PROBLEMS = []
# Pilot: a page is built only if its section is in guide.md.
HAVE = {sec.id for sec in C.SECTIONS}
FRONT_IDS = [x for x in ("why", "meaning", "fit") if x in HAVE]
ENTRY_START = 2 + len(FRONT_IDS)  # cover, the front pages present, then entries
# The corner tile on the sequence page: the diagram follows one work item.
SEQ_TILE = "Sn"

def para(c, text, style, x, ytop, w):
    p = Paragraph(mono(text, style.fontSize), style)
    _, h = p.wrap(w, 1000)
    p.drawOn(c, x, ytop - h)
    return ytop - h

def rule(c, y, x0=ML, x1=PW - MR, weight=0.3, color=HAIR):
    if not weight:
        return
    c.setStrokeColor(color); c.setLineWidth(weight); c.line(x0, y, x1, y)

def row(c, label, text, y, style=SMALL, pad=4.5, weight=0, color=HAIR, lstyle=LABEL, labw=LABW):
    rule(c, y, weight=weight, color=color)
    y -= pad
    yl = para(c, label, lstyle, ML, y, labw)
    yt = para(c, text, style, ML + labw + GAP, y, W - labw - GAP)
    return min(yl, yt) - pad + 1

def first(i):
    """A heavy rule over the first row of a group and none between the rows: the space between
    rows is enough to tell them apart."""
    return dict(weight=(1 if i == 0 else 0), color=INK)

def title(c, text, y=None):
    y = PH - MT if y is None else y
    c.setFillColor(INK); c.setFont("Sans-Bold", 17)
    c.drawString(ML, y - 15, text)
    return y - 26

def avatar(c, key, x, y, size, number=None):
    """Two-tone monogram tile; (x, y) is the lower-left corner."""
    if key not in PART_TOKEN:
        return  # not one of the parts, such as a person: no tile
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

def thumb_tab(c, key, index):
    base, _, _ = colors(key)
    step = 58; h = 50
    top = PH - 70 - index * step
    c.setFillColor(base); c.rect(PW - 6, top - h, 6, h, stroke=0, fill=1)

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

def group_label(c, text, y):
    """Small grey label that names the rows below it. The first row draws the heavy rule."""
    c.setFont("Sans-Bold", 6.8); c.setFillColor(GREY); c.drawString(ML, y - 6, text)
    return y - 10

TITLE_ST = ParagraphStyle("title", fontName="Sans-Bold", fontSize=17, leading=19, textColor=INK)

def plain_title(c, text, y=PH - MT):
    """A page title with no corner tile that may break with <br/>. One line sits exactly where
    title() puts it, and content starts the same distance below the last line."""
    p = Paragraph(text, TITLE_ST)
    _, h = p.wrap(W, 200)
    p.drawOn(c, ML, y - h + 2)
    return y - h + 2 - 9

def tile_title(c, text, key):
    """Page title with the part's tile in the top-right corner. The title wraps short of the
    tile, and content starts below whichever is lower: the tile or the title."""
    corner_avatar(c, key, size=TILE)
    p = Paragraph(text, TITLE_ST)
    _, h = p.wrap(W - TILE - 12, 200)
    p.drawOn(c, ML, PH - MT - h + 2)
    return min(PH - MT - TILE, PH - MT - h) - SP_TILE

# ---------- the cover: a black band over the part grid ----------
# The design is B′ in packages/editorial/design/cover-study/b-prime/. A black band across the
# top holds the kicker, the collection, the guide's number and the collection's mark in its top
# row, and the title in white on its foot. Below it are the subtitle, the six families in the
# series' order, and one row per part with its tile in its family's column, so the tiles step
# across the page by family. The collection, its mark and the number are in guide.md's front
# matter, which pnpm sync keeps in step with site/src/data/collections.json.
BAND = 150            # the band's height, the same on every guide
BAND_ROW = 24         # the centre of the band's top row, from the top edge
BAND_MARK = 16        # the collection's mark, on the right margin
BAND_TEXT = 9         # the kicker and the number; the collection's name is 84% of this
TITLE_FOOT = 16       # the title's last baseline, above the band's foot
BAND_GREY = HexColor("#a8a8a8")   # the collection's name, on black
COVER_SUB = 9.4, 12.2             # the subtitle: size and leading
GRID_CELL, GRID_GUT = W / 6, 1.5  # six columns, one per family; one row per part
GRID_Y0 = MB + 12                 # the grid's foot, unless the tagline needs the room
TAG_CLEAR = 4                     # space between the grid and the tagline
# The six families in the series' order, with the word the cover prints and the colour
# token each family has in every guide (packages/editorial/registry.md).
COVER_FAMILIES = (("Ru", "Runs", "warning"), ("Wr", "Written", "figjam"), ("Ck", "Checks", "success"),
                  ("Us", "Used", "danger"), ("Dm", "Decided", "assistive"), ("Nu", "Counted", "brand"))
COVER_FAMILY_ORDER = [f for f, _, _ in COVER_FAMILIES]


def family_colors(fam):
    """A family's colours, as colors() gives a part's: base, darker band, text."""
    t = dict((f, tok) for f, _, tok in COVER_FAMILIES)[fam]; base = TOKENS[t]
    fg = INK if t == "warning" else white
    return HexColor(base), _dark(base, 0.86 if t == "warning" else 0.80), fg


def family_tile(c, key, fam, x, y, size, number=None):
    """A part's two-tone tile on the cover; (x, y) is the lower-left corner. It takes the colour the
    part has on its own pages, so the cover and the pages agree; the family only places it."""
    base, dark, fg = colors(key) if key in PART_TOKEN else family_colors(fam)
    c.setFillColor(base); c.rect(x, y, size, size, stroke=0, fill=1)
    band = size * 0.26
    c.setFillColor(dark); c.rect(x, y, size, band, stroke=0, fill=1)
    fs = size * 0.40
    c.setFillColor(fg); c.setFont("Sans-Bold", fs)
    c.drawString(x + size * 0.13, y + band + (size - band) / 2 - fs * 0.34, key)
    if number:
        c.setFont("Sans-Bold", max(5.5, size * 0.14))
        c.drawString(x + size * 0.13, y + band * 0.30, number)


def collection_mark(c, x, y, s, color=white, mark=None):
    """The collection's mark in an s x s box, lower-left (x, y): square, triangle, circle or
    diamond."""
    mark = mark or C.COLLECTION_MARK
    c.setFillColor(color)
    if mark == "square":
        c.rect(x, y, s, s, stroke=0, fill=1)
        return
    if mark == "circle":
        c.circle(x + s / 2, y + s / 2, s / 2, stroke=0, fill=1)
        return
    p = c.beginPath()
    if mark == "triangle":
        p.moveTo(x, y); p.lineTo(x + s, y); p.lineTo(x + s / 2, y + s * 0.92)
    else:  # diamond
        p.moveTo(x + s / 2, y); p.lineTo(x + s, y + s / 2); p.lineTo(x + s / 2, y + s); p.lineTo(x, y + s / 2)
    p.close(); c.drawPath(p, stroke=0, fill=1)


def wrap_words(text, font, size, width):
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


def cover_label(p):
    """Where a part's name and page go: right of its tile if they fit before the margin, else
    left of it. Returns (x, align, x0, x1), x0 and x1 being the label's extent."""
    j = COVER_FAMILY_ORDER.index(p["family"])
    x = ML + j * GRID_CELL + GRID_GUT / 2
    need = max(pdfmetrics.stringWidth(p["name"], "Sans-Bold", 7.2), pdfmetrics.stringWidth(p["sub"], "Sans", 6.4))
    if x + GRID_CELL - GRID_GUT + 5 + need <= PW - MR:
        tx = x + GRID_CELL - GRID_GUT / 2 + 5
        return tx, "left", tx, tx + need
    tx = x - GRID_GUT - 4
    return tx, "right", tx - need, tx


def grid_foot(parts):
    """The grid's foot: GRID_Y0, or higher if a row's tile or label would reach the tagline,
    which is right-aligned above the footer rule."""
    tag_x0 = ML + W - pdfmetrics.stringWidth(TAGLINE, "Serif-Italic", 9)
    tag_top = MB + 15 + pdfmetrics.getAscent("Serif-Italic", 9)
    y0 = GRID_Y0
    for i, p in enumerate(parts):
        j = COVER_FAMILY_ORDER.index(p["family"])
        x = ML + j * GRID_CELL + GRID_GUT / 2
        _, _, l0, l1 = cover_label(p)
        if max(x + GRID_CELL - GRID_GUT, l1) > tag_x0:
            bottom = GRID_Y0 + (5 - i) * GRID_CELL + GRID_GUT / 2
            y0 = max(y0, GRID_Y0 + tag_top + TAG_CLEAR - bottom)
    return y0


def part_grid(c, parts, y0):
    """The six family columns, each headed by its square and word, filled where the guide
    has parts in that family; then one row per part, in entry order, from the top of a grid six
    rows high. Returns the head rule's y."""
    if len(parts) > 6:
        PROBLEMS.append(f"cover: {len(parts)} parts, and the grid has room for six")
    top = y0 + 6 * GRID_CELL
    c.setStrokeColor(INK); c.setLineWidth(0.6); c.line(ML, top + 14, PW - MR, top + 14)
    present = {p["family"] for p in parts}
    for j, (f, word, _) in enumerate(COVER_FAMILIES):
        hx = ML + j * GRID_CELL + GRID_GUT / 2
        if f in present:
            c.setFillColor(family_colors(f)[0]); c.rect(hx, top + 4.2, 4.6, 4.6, stroke=0, fill=1)
            c.setFont("Sans", 5.8); c.setFillColor(GREY)
        else:
            c.setStrokeColor(HexColor("#b8b8b8")); c.setLineWidth(0.5)
            c.rect(hx + 0.25, top + 4.45, 4.1, 4.1, stroke=1, fill=0)
            c.setFont("Sans", 5.8); c.setFillColor(HexColor("#a6a6a6"))
        c.drawString(hx + 7, top + 5, word)
    for i, p in enumerate(parts):
        j = COVER_FAMILY_ORDER.index(p["family"])
        x = ML + j * GRID_CELL + GRID_GUT / 2; y = top - (i + 1) * GRID_CELL + GRID_GUT / 2
        family_tile(c, p["key"], p["family"], x, y, GRID_CELL - GRID_GUT, number=p["num"])
        ty = y + (GRID_CELL - GRID_GUT) / 2
        tx, align, _, _ = cover_label(p)
        draw = c.drawString if align == "left" else c.drawRightString
        c.setFillColor(INK); c.setFont("Sans-Bold", 7.2); draw(tx, ty + 1.5, p["name"])
        c.setFillColor(GREY); c.setFont("Sans", 6.4); draw(tx, ty - 7, p["sub"])
    return top + 14


def cover_layout(parts):
    """The cover's measures, shared with build_docx.py: the subtitle's lines, the grid's foot
    and its head rule."""
    sub = wrap_words(C.SUBTITLE, "Sans", COVER_SUB[0], W * 0.8)
    y0 = grid_foot(parts)
    return dict(sub=sub, y0=y0, head=y0 + 6 * GRID_CELL + 14)


def band(c):
    """The full-bleed band with its top row: the kicker on the left; the collection's name, the
    guide's number and the collection's mark on the right."""
    c.setFillColor(INK); c.rect(0, PH - BAND, PW, BAND, stroke=0, fill=1)
    axis = PH - BAND_ROW
    base = axis - BAND_TEXT * 0.36
    c.setFillColor(white); c.setFont("Sans-Bold", BAND_TEXT)
    c.drawString(ML, base, C.KICKER)
    mx = PW - MR - BAND_MARK
    collection_mark(c, mx, axis - BAND_MARK / 2, BAND_MARK)
    x = mx - 8
    c.setFont("Sans-Bold", BAND_TEXT); c.drawRightString(x, base, C.NUMBER)
    x -= pdfmetrics.stringWidth(C.NUMBER, "Sans-Bold", BAND_TEXT) + 6
    c.setFont("Sans", BAND_TEXT * 0.84); c.setFillColor(BAND_GREY)
    c.drawRightString(x, base, C.COLLECTION)
    left = x - pdfmetrics.stringWidth(C.COLLECTION, "Sans", BAND_TEXT * 0.84)
    if left < ML + pdfmetrics.stringWidth(C.KICKER, "Sans-Bold", BAND_TEXT) + 12:
        PROBLEMS.append("cover: the collection's name runs into the kicker")


# ---------- pages ----------
def page_cover(c):
    parts = cover_parts()
    band(c)
    n = len(COVER_LINES)
    base = PH - BAND + TITLE_FOOT
    c.setFillColor(white); c.setFont("Sans-Bold", 27)
    for k, line in enumerate(COVER_LINES):
        c.drawString(ML, base + 29 * (n - 1 - k), line)
        if pdfmetrics.stringWidth(line, "Sans-Bold", 27) > W:
            PROBLEMS.append(f"cover: title line {line!r} is wider than the page")
    # The title fits the band if its first line stays clear of the band's top row.
    if base + 29 * (n - 1) + 27 * 0.72 > PH - BAND_ROW - BAND_MARK / 2 - 8:
        PROBLEMS.append(f"cover: the title's {n} lines run into the band's top row")
    lay = cover_layout(parts)
    size, leading = COVER_SUB
    c.setFillColor(INK); c.setFont("Sans", size)
    y = PH - BAND - 12 - size * 0.76
    for line in lay["sub"]:
        c.drawString(ML, y, line); y -= leading
    sub_bottom = y + leading - size * 0.24
    head = part_grid(c, parts, lay["y0"])
    if sub_bottom - head < 4:
        PROBLEMS.append(f"cover: the subtitle reaches y={sub_bottom:.1f}, into the family row at {head:.1f}")
    rule(c, MB + 4, weight=1, color=INK)
    c.setFont("Sans", 6.4); c.setFillColor(GREY)
    c.drawString(ML, MB - 6, f"{C.COVER_FOOTER} · Version {C.VERSION}")
    tagline(c)
    check("cover", lay["y0"])


def cover_parts():
    """The parts on the cover, in entry order: tile key, family, number, name, the line under
    the name, and the entry's index for the Word document's page reference."""
    return [dict(key=e["mono"], family=PART_FAMILY[e["mono"]], num=e["num"], name=e["name"],
                 sub=f"page {ENTRY_PAGE[i]}", ref=i) for i, e in enumerate(C.ENTRIES)]



def page_why(c, n):
    y = plain_title(c, C.WHY_TITLE)
    y = blocks(c, C.WHY_BLOCKS, y)
    footer(c, n); check("why", y)

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

def vline(c, x, y0, y1, heads=("down",)):
    c.setStrokeColor(INK); c.setLineWidth(0.6); c.line(x, y0, x, y1)
    lo, hi = min(y0, y1), max(y0, y1)
    if "down" in heads: arrow_head(c, x, lo, "down")
    if "up" in heads: arrow_head(c, x, hi, "up")

def node(c, e, xc, ytop, caption, size=28, name=None):
    avatar(c, e["mono"], xc - size / 2, ytop - size, size)
    c.setFillColor(INK); c.setFont("Sans-Bold", 7); c.drawCentredString(xc, ytop - size - 9, name or e["name"])
    c.setFillColor(GREY); c.setFont("Sans", 6.2); c.drawCentredString(xc, ytop - size - 17, caption)
    return ytop - size

def corner_avatar(c, key, number=None, size=46):
    avatar(c, key, PW - MR - size, PH - MT - size, size, number=number)

def note(c, text, y, style=SMALL):
    """A closing note under a heavy rule."""
    rule(c, y, weight=1, color=INK)
    return para(c, text, style, ML, y - 6, W)

def on_grey(c, y, draw):
    """A grey block: draw(c, y) on a grey panel, which reaches PAD into the side margins so the
    text keeps its left edge. draw returns the bottom y; it runs once on a scratch canvas first
    to measure the panel."""
    bottom = draw(canvas.Canvas(io.BytesIO()), y - PAD)
    c.setFillColor(PANEL); c.rect(ML - PAD, bottom - PAD, W + 2 * PAD, y - bottom + PAD, stroke=0, fill=1)
    draw(c, y - PAD)
    return bottom - PAD

def callout(c, label, text, y):
    """One tip or warning in an outlined box, led by its label in bold."""
    p = Paragraph(mono(f"<b>{label}.</b> {text}", SMALL.fontSize), SMALL)
    _, h = p.wrap(W, 1000)
    c.setStrokeColor(INK); c.setLineWidth(0.8)
    c.rect(ML - PAD, y - h - 2 * PAD, W + 2 * PAD, h + 2 * PAD, stroke=1, fill=0)
    p.drawOn(c, ML, y - PAD - h)
    return y - h - 2 * PAD

def blocks(c, items, y, grey=False, labw=LABW):
    """A section's paragraphs, two-column tables, grey blocks and callouts, in order. A table is
    drawn as rows, with no rules on a grey block, and labw is the width of its labels. Returns
    the bottom y."""
    for b in items:
        if b[0] == "p":
            y = para(c, b[1], SMALL if grey else BODY, ML, y, W) - SP_PARA
        elif b[0] == "table":
            for i, (label, text) in enumerate(b[2]):
                y = row(c, label, text, y, labw=labw, **({} if grey else first(i)))
            y -= SP_PARA
        elif b[0] == "grey":
            y = on_grey(c, y, lambda c_, y_, b=b: blocks(c_, b[1], y_, grey=True, labw=labw) + SP_PARA) - SP_PARA - 4
        elif b[0] == "callout":
            y = callout(c, b[1], b[2], y) - SP_PARA - 4
        elif b[0] == "diagram":
            y = figure(c, b[1], y - 2) - SP_SECTION + 2
    return y

# ---------- figures ----------
# A fenced diagram block in guide.md is drawn here, one line per item: the first word names the
# item and "|" separates its fields. FIGURES records where each figure lands in the built PDF so
# build_docx.py can place the same drawing in the Word document.
FIGURES = []
LIVE = {"canvas": None, "page": 0}
PROB = HexColor(TOKENS[FAMILY_TOKEN["Nu"]])  # bars are scores, in the Probability family's colour
TRACK = HexColor("#e2e2e2")
NAME_OF = {e["mono"]: e["name"] for e in C.ENTRIES}

def fig_items(lines):
    items = []
    for line in lines:
        if line.strip():
            kind, _, rest = line.strip().partition(" ")
            items.append((kind, [f.strip() for f in rest.split("|")]))
    return items

def figure(c, lines, y):
    items = fig_items(lines)
    kinds = {k for k, _ in items}
    draws = (("ask", fig_answers), ("step", fig_steps), ("input", fig_io), ("missing", fig_state),
             ("side", fig_sides), ("shape", fig_shapes), ("case", fig_cases), ("scores", fig_decision),
             ("row", fig_sorted), ("yes", fig_threshold), ("ruleset", fig_rulesets), ("field", fig_record))
    draw = next((fn for k, fn in draws if k in kinds), None)
    if draw is None:
        raise SystemExit(f"unknown diagram starting {lines[:1]}")
    bottom = draw(c, items, y)
    if c is LIVE["canvas"]:
        FIGURES.append((LIVE["page"], (ML - PAD - 1, bottom - 3, PW - MR + PAD + 1, y + 2)))
    return bottom

def figure_boxes():
    """Build the PDF in memory and return where each figure landed: (page, box) in order."""
    FIGURES.clear()
    build(io.BytesIO())
    PROBLEMS.clear()
    return list(FIGURES)

def message_card(c, label, text, y):
    """A message as the customer sent it: an outlined card with a small grey header."""
    p = Paragraph(text, BODY)
    _, h = p.wrap(W, 1000)
    head = 10
    total = PAD + head + h + PAD - 1
    c.setStrokeColor(INK); c.setLineWidth(0.6); c.setFillColor(white)
    c.roundRect(ML - PAD, y - total, W + 2 * PAD, total, 3, stroke=1, fill=1)
    c.setFillColor(GREY); c.setFont("Sans", 6.2); c.drawString(ML, y - PAD - 5, label)
    p.drawOn(c, ML, y - PAD - head - h + 1)
    return y - total

ANS_LABW, ANS_VALW, ANS_ROW, BAR_H = 54, 22, 10.5, 5.6

def chosen(items):
    """The answers that count as picked: the top score for a pick-one question, otherwise every
    score of 0.5 or more."""
    out, k = set(), 0
    while k < len(items):
        if items[k][0] == "ask":
            j = k + 1
            while j < len(items) and items[j][0] == "answer":
                j += 1
            group = list(range(k + 1, j))
            scores = {i: float(items[i][1][1]) for i in group}
            if len(items[k][1]) > 1 and items[k][1][1] == "pick one" and scores:
                out.add(max(scores, key=scores.get))
            else:
                out |= {i for i, s in scores.items() if s >= 0.5}
            k = j
        else:
            k += 1
    return out

def fig_answers(c, items, y):
    """A message, then each question with its allowed answers drawn as score bars."""
    prev, picked = None, chosen(items)
    for i, (kind, f) in enumerate(items):
        if kind == "message":
            y = message_card(c, f[0], f[1], y) - 3
            x = ML + 5
            vline(c, x, y, y - 17)
            avatar(c, "Dj", x + 7, y - 14, 10)
            c.setFillColor(GREY); c.setFont("Sans", 6.4)
            c.drawString(x + 21, y - 11.5, "The decision model scores each answer.")
            y -= 27
        elif kind == "ask":
            if prev == "answer":
                y -= 8
            c.setFillColor(INK); c.setFont("Sans-Bold", 7.4); c.drawString(ML, y - 7, f[0])
            if len(f) > 1:
                w = pdfmetrics.stringWidth(f[0], "Sans-Bold", 7.4)
                c.setFillColor(GREY); c.setFont("Sans", 6.2); c.drawString(ML + w + 5, y - 7, f[1])
            y -= 14
        elif kind == "answer":
            label, score = f[0], float(f[1])
            strong = i in picked
            font, ink = ("Sans-Bold", INK) if strong else ("Sans", GREY)
            c.setFillColor(ink); c.setFont(font, 6.8); c.drawString(ML, y - 6.6, label)
            x0, x1 = ML + ANS_LABW, PW - MR - ANS_VALW
            c.setFillColor(TRACK); c.rect(x0, y - 7.4, x1 - x0, BAR_H, stroke=0, fill=1)
            c.setFillColor(PROB); c.rect(x0, y - 7.4, max(0.8, (x1 - x0) * score), BAR_H, stroke=0, fill=1)
            c.setFillColor(ink); c.setFont(font, 6.8); c.drawRightString(PW - MR, y - 6.6, f"{score:.2f}")
            y -= ANS_ROW
        prev = kind
    return y

STEP_NAMEW, STEP_TILE = 96, 12
STEP_TEXT = ParagraphStyle("steptext", parent=CELL, fontSize=7.0, leading=9.2)
SCORE = re.compile(r"(\S+) (0\.\d+|1\.0+)")

def step_value(c, key, text, x, ytop, w, draw=True):
    """A step's value inside its grey box, drawn the way the first page draws it: scores as bars,
    allowed answers as outlined chips, anything else as text. Returns the height used."""
    pairs = [SCORE.fullmatch(s.strip()) for s in text.split(",")]
    if all(pairs):  # scores
        for k, m in enumerate(pairs):
            y = ytop - k * 9.5
            score = float(m.group(2))
            if draw:
                c.setFillColor(INK); c.setFont("Sans", 6.4); c.drawString(x, y - 6.4, m.group(1))
                x0, x1 = x + 36, x + w - 18
                c.setFillColor(white); c.rect(x0, y - 7.2, x1 - x0, 5, stroke=0, fill=1)
                c.setFillColor(PROB); c.rect(x0, y - 7.2, max(0.8, (x1 - x0) * score), 5, stroke=0, fill=1)
                c.setFillColor(INK); c.drawRightString(x + w, y - 6.4, m.group(2))
        return len(pairs) * 9.5 - 1.5
    if key == "Al":  # allowed answers
        cx, cy = x, ytop
        for word in (s.strip() for s in text.split(",")):
            cw = pdfmetrics.stringWidth(word, "Sans-Bold", 6.6) + 10
            if cx + cw > x + w:
                cx, cy = x, cy - 14
            if draw:
                c.setFillColor(white); c.setStrokeColor(INK); c.setLineWidth(0.6)
                c.roundRect(cx, cy - 10.5, cw, 10.5, 5.25, stroke=1, fill=1)
                c.setFillColor(INK); c.setFont("Sans-Bold", 6.6); c.drawString(cx + 5, cy - 7.4, word)
            cx += cw + 4
        return ytop - cy + 10.5
    p = Paragraph(text, STEP_TEXT)
    _, h = p.wrap(w, 1000)
    if draw:
        p.drawOn(c, x, ytop - h)
    return h

def fig_steps(c, items, y):
    """Groups of steps: each step is a part's tile and name beside its value in the example.
    An arrow joins one group to the next."""
    first_group = True
    for kind, f in items:
        if kind == "group":
            key, text = (f[0], f[1]) if len(f) > 1 else (None, f[0])
            if not first_group:
                vline(c, ML + STEP_NAMEW + (W - STEP_NAMEW) / 2, y + 2, y - 12)
                y -= 15
            first_group = False
            x = ML
            if key:
                avatar(c, key, ML, y - 11, 11)
                x += 15
            c.setFillColor(INK); c.setFont("Sans-Bold", 8.2); c.drawString(x, y - 8.6, text)
            y -= 13
            rule(c, y, weight=1, color=INK)
            y -= 6
        elif kind == "step":
            key, text = f
            ty = y - 2.5  # the tile and the name line up with the first line in the box
            nx = ML  # a step that isn't one of the guide's parts, such as ordinary code, has no tile
            if key in PART_TOKEN:
                avatar(c, key, ML, ty - STEP_TILE, STEP_TILE)
                nx += STEP_TILE + 5
            yn = para(c, NAME_OF.get(key, key), LABEL, nx, ty - 0.5, STEP_NAMEW - (nx - ML) - 10)
            bx, bw = ML + STEP_NAMEW, W - STEP_NAMEW
            h = step_value(c, key, text, bx + 6, y - 5, bw - 12, draw=False)
            box_h = h + 10
            c.setFillColor(PANEL); c.roundRect(bx, y - box_h, bw, box_h, 2, stroke=0, fill=1)
            step_value(c, key, text, bx + 6, y - 5, bw - 12)
            y = min(y - box_h, yn, ty - STEP_TILE) - 6
    return y + 6

# Small figures on the entry pages, each drawn from the same support example.
def scores(text):
    return [(m.group(1), float(m.group(2))) for m in (SCORE.fullmatch(s.strip()) for s in text.split(","))]

def bars(c, pairs, x, ytop, w, labw=36, row=9.5, size=6.4, top=True):
    """Labelled score bars. The picked answers are set in bold: the top score when top is true,
    otherwise every score of 0.5 or more. Returns the bottom y."""
    best = max(s for _, s in pairs)
    for k, (label, score) in enumerate(pairs):
        y = ytop - k * row
        picked = score == best if top else score >= 0.5
        font, ink = ("Sans-Bold", INK) if picked else ("Sans", GREY)
        c.setFillColor(ink); c.setFont(font, size); c.drawString(x, y - 6.4, label)
        x0, x1 = x + labw, x + w - 18
        c.setFillColor(TRACK); c.rect(x0, y - 7.2, x1 - x0, 5, stroke=0, fill=1)
        c.setFillColor(PROB); c.rect(x0, y - 7.2, max(0.8, (x1 - x0) * score), 5, stroke=0, fill=1)
        c.setFillColor(ink); c.setFont(font, size); c.drawRightString(x + w, y - 6.4, f"{score:.2f}")
    return ytop - len(pairs) * row + 1.5

def chip(c, word, x, ytop, filled=False, size=6.6):
    """An answer as an outlined chip, filled in ink when it is the one picked. Returns its width."""
    w = pdfmetrics.stringWidth(word, "Sans-Bold", size) + 10
    c.setStrokeColor(INK); c.setLineWidth(0.6); c.setFillColor(INK if filled else white)
    c.roundRect(x, ytop - 10.5, w, 10.5, 5.25, stroke=1, fill=1)
    c.setFillColor(white if filled else INK); c.setFont("Sans-Bold", size); c.drawString(x + 5, ytop - 7.4, word)
    return w

def arrow_right(c, x0, x1, y):
    c.setStrokeColor(INK); c.setLineWidth(0.6); c.line(x0, y, x1 - 3, y)
    arrow_head(c, x1, y, "right")

def small_name(c, key, x, ytop, size=9):
    """A part's small tile and its name in bold. Returns the bottom y."""
    avatar(c, key, x, ytop - size, size)
    c.setFillColor(INK); c.setFont("Sans-Bold", 6.6); c.drawString(x + size + 4, ytop - size + 1.8, NAME_OF.get(key, key))
    return ytop - size

def fig_io(c, items, y):
    """What goes into a decision model and what comes out, left to right."""
    inputs = [f for k, f in items if k == "input"]
    key_out, out = next(f for k, f in items if k == "output")
    lw, mx, mw = 100, ML + 114, 48
    rx = mx + mw + 16
    yy = y
    for key, text in inputs:
        yy = small_name(c, key, ML, yy) - 2
        yy = para(c, text, CELLG, ML + 13, yy, lw - 13) - 6
    bottom = yy + 6
    mid = (y + bottom) / 2
    size = 26
    avatar(c, "Dj", mx + (mw - size) / 2, mid - size / 2 + 6, size)
    c.setFillColor(INK); c.setFont("Sans-Bold", 6.4); c.drawCentredString(mx + mw / 2, mid - size / 2 - 2, "Decision model")
    arrow_right(c, ML + lw + 2, mx - 2, mid + 6)
    arrow_right(c, mx + mw + 2, rx - 4, mid + 6)
    pairs = scores(out)
    oy = mid + 6 + (len(pairs) * 9.5 + 13) / 2
    oy = small_name(c, key_out, rx, oy) - 4
    bars(c, pairs, rx, oy, PW - MR - rx, labw=32, row=9, top=False)
    return bottom

def fig_state(c, items, y):
    """What the software sent, and what it left out, as two cards."""
    for kind, f in items:
        if kind == "message":
            y = message_card(c, f[0], f[1], y) - 8
        elif kind == "missing":
            p = Paragraph(f[1], ParagraphStyle("miss", parent=BODY, textColor=GREY))
            _, h = p.wrap(W, 1000)
            total = PAD + 10 + h + PAD - 1
            c.setStrokeColor(GREY); c.setLineWidth(0.6); c.setDash(2, 1.6)
            c.roundRect(ML - PAD, y - total, W + 2 * PAD, total, 3, stroke=1, fill=0)
            c.setDash()
            c.setFillColor(GREY); c.setFont("Sans", 6.2); c.drawString(ML, y - PAD - 5, f[0])
            p.drawOn(c, ML, y - PAD - 10 - h + 1)
            y -= total + 8
    return y + 8

def fig_sides(c, items, y):
    """Two columns of questions about the same message, each with its answer."""
    names = list(dict.fromkeys(f[0] for k, f in items if k == "side"))
    cw = (W - 14) / len(names)
    bottoms = []
    for n, name in enumerate(names):
        x = ML + n * (cw + 14)
        c.setFillColor(INK); c.setFont("Sans-Bold", 7.2); c.drawString(x, y - 7, name)
        rule(c, y - 11, x0=x, x1=x + cw, weight=1, color=INK)
        yy = y - 16
        for k, f in items:
            if k == "side" and f[0] == name:
                yy = para(c, f[1], CELL, x, yy, cw) - 2
                yy = bars(c, scores(f[2]), x, yy, cw, labw=44) - 7
        bottoms.append(yy + 7)
    return min(bottoms)

def fig_shapes(c, items, y):
    """The common shapes of allowed answers. A picked answer is filled. Answers joined by > are
    an ordered level, drawn on a line."""
    lw = 66
    for k, f in items:
        if k != "shape":
            continue
        label, text = f
        ordered = ">" in text
        words = [w.strip() for w in re.split(r"[>,]", text)]
        c.setFillColor(INK); c.setFont("Sans-Bold", 6.8); c.drawString(ML, y - 7.6, label)
        x = ML + lw
        if ordered:  # a line behind the chips shows the order, ending in an arrow
            total = sum(pdfmetrics.stringWidth(w.rstrip("*"), "Sans-Bold", 6.6) + 10 for w in words) + 14 * (len(words) - 1)
            c.setStrokeColor(GREY); c.setLineWidth(0.6); c.line(x + 4, y - 5.25, x + total + 9, y - 5.25)
            c.setFillColor(GREY)
            p = c.beginPath(); p.moveTo(x + total + 12, y - 5.25); p.lineTo(x + total + 8, y - 3); p.lineTo(x + total + 8, y - 7.5); p.close()
            c.drawPath(p, stroke=0, fill=1)
        for w in words:
            x += chip(c, w.rstrip("*"), x, y, filled=w.endswith("*")) + (14 if ordered else 4)
        y -= 17
    return y + 4

def fig_cases(c, items, y):
    """Scores for two messages side by side, such as a clear case and a close call."""
    cases = [f for k, f in items if k == "case"]
    cw = (W - 14) / len(cases)
    bottoms = []
    for n, (name, text) in enumerate(cases):
        x = ML + n * (cw + 14)
        c.setFillColor(INK); c.setFont("Sans-Bold", 7.2); c.drawString(x, y - 7, name)
        rule(c, y - 11, x0=x, x1=x + cw, weight=1, color=INK)
        bottoms.append(bars(c, scores(text), x, y - 16, cw, labw=34))
    return min(bottoms)

# Figures for turning answers into actions.
def tint(key_or_hex, a):
    """A family colour mixed with white: a = 1 is the colour, 0 is white."""
    h = TOKENS.get(FAMILY_TOKEN.get(key_or_hex, ""), key_or_hex).lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return HexColor("#%02x%02x%02x" % tuple(round(255 - (255 - v) * a) for v in (r, g, b)))

CASE_INK = HexColor(TOKENS[FAMILY_TOKEN["Wr"]])   # labeled cases are written down
ZONE = tint("Dm", 0.16)                            # where the rules act without a person
ZONE_CENTER = ParagraphStyle("zone", fontName="Sans-Bold", fontSize=6.4, leading=7.6, textColor=INK, alignment=1)

def head(c, text, x, y, w, key=None):
    """A column heading over a heavy rule, with an optional part tile. Returns the y below it."""
    if key in PART_TOKEN:
        avatar(c, key, x, y - 10, 10)
        x, w = x + 14, w - 14
    c.setFillColor(INK); c.setFont("Sans-Bold", 7.2); c.drawString(x, y - 7.6, text)
    rule(c, y - 12, x0=x - (14 if key in PART_TOKEN else 0), x1=x + w, weight=1, color=INK)
    return y - 17

def dot(c, x, y, filled, r=2.6):
    c.setStrokeColor(CASE_INK); c.setLineWidth(0.9); c.setFillColor(CASE_INK if filled else white)
    c.circle(x, y, r, stroke=1, fill=1)

def values(text):
    return [float(v) for v in text.split(",")]

def rule_rows(c, rows, x, y, w):
    """Rules as condition, then an arrow to the action. A rule that applies is set in ink with a
    filled marker; the rest are grey with an open one. Returns the bottom y."""
    for cond, action, applies in rows:
        ink = INK if applies else GREY
        c.setStrokeColor(ink); c.setLineWidth(0.7); c.setFillColor(ink if applies else white)
        c.circle(x + 2.5, y - 4.4, 2.2, stroke=1, fill=1)
        yc = para(c, cond, CELL if applies else CELLG, x + 9, y, w - 9)
        arrow_right(c, x + 9, x + 21, yc - 3.4)
        ya = para(c, action, CELLB if applies else CELLG, x + 25, yc + 1.5, w - 25)
        y = ya - 5
    return y + 5

DEC_GAP = 14
DEC_HEAD = ParagraphStyle("dechead", fontName="Sans-Bold", fontSize=7.0, leading=8.6, textColor=GREY)
DEC_CELL = ParagraphStyle("deccell", parent=CELL, fontSize=7.4, leading=9.6)
DEC_CELLB = ParagraphStyle("deccellb", parent=DEC_CELL, fontName="Sans-Bold")
DEC_RESULT = ParagraphStyle("decresult", fontName="Sans-Bold", fontSize=9.2, leading=11, textColor=white, alignment=1)

def tick(c, x, y, size=6.5):
    """A check mark with its lower-left at (x, y)."""
    c.setStrokeColor(INK); c.setLineWidth(1.3); c.setLineCap(1); c.setLineJoin(1)
    p = c.beginPath(); p.moveTo(x, y + size * 0.5); p.lineTo(x + size * 0.36, y + size * 0.12)
    p.lineTo(x + size, y + size * 0.95)
    c.drawPath(p, stroke=1, fill=0)
    c.setLineCap(0); c.setLineJoin(0)

def dec_cell(c, kind, f, x, y, w):
    """One cell of the decision grid. Returns its bottom y."""
    if kind == "scores":  # a question, then its answer as a score bar
        q, ans = f
        y = para(c, q, CELLG, x, y, w) - 1
        return bars(c, scores(ans), x, y, w, labw=26, top=False)
    if kind == "checks":  # each check on its own line, ticked
        for item in f:
            tick(c, x, y - 7.5)
            y = para(c, item, DEC_CELL, x + 11, y, w - 11) - 2.5
        return y + 2.5
    if kind == "results":  # the action, as a solid block
        p = Paragraph(f, DEC_RESULT)
        _, h = p.wrap(w - 12, 1000)
        c.setFillColor(INK); c.roundRect(x, y - h - 14, w, h + 14, 3, stroke=0, fill=1)
        p.drawOn(c, x + 6, y - 7 - h)
        return y - h - 14
    return para(c, f, DEC_CELLB if kind == "facts" else DEC_CELL, x, y, w)

def fig_decision(c, items, y):
    """One message followed down two columns, one per action: what the model answered, what the
    account system shows, the rule people wrote, the checks code ran and what happens. Every
    number the rule needs sits in the same column as the rule."""
    cw = (W - DEC_GAP) / 2
    xs = (ML, ML + cw + DEC_GAP)
    first = True
    # "check N | text" lines fill the checks row's column N.
    checks = [[f[1] for k, f in items if k == "check" and f[0] == str(n)] for n in (1, 2)]
    for kind, f in items:
        if kind == "check":
            continue
        if kind == "checks":
            f = [f[0], *checks]
        if kind == "message":  # the message, then a fork into the two columns
            y = message_card(c, f[0], f[1], y)
            c.setStrokeColor(INK); c.setLineWidth(0.6)
            c.line(ML + W / 2, y, ML + W / 2, y - 6)
            c.line(xs[0] + cw / 2, y - 6, xs[1] + cw / 2, y - 6)
            for x in xs:
                vline(c, x + cw / 2, y - 6, y - 15)
            y -= 19
            continue
        if kind == "else":
            p = Paragraph(f[0], SMALLG)
            _, h = p.wrap(W, 1000)
            y -= 9
            p.drawOn(c, ML, y - h)
            y -= h
            continue
        head, cells = f[0], f[1:]
        if kind == "scores":
            cells = [cells[0:2], cells[2:4]]
        if kind == "results":  # an arrow into each action
            for x in xs:
                vline(c, x + cw / 2, y - 3, y - 13)
            y -= 16
        elif not first:
            y -= 13
        first = False
        # The row's heading spans both columns, with the part's tile when it has one.
        hx = ML
        key = NAME2MONO.get("Policy") if kind == "rules" else None  # the rules row is the policy
        if key in PART_TOKEN:
            avatar(c, key, ML, y - 9, 9)
            hx += 12
        if kind != "results":
            yh = para(c, head, DEC_HEAD, hx, y - 0.5, W - (hx - ML))
            rule(c, yh - 1.5, weight=0.4, color=HAIR)
            y = yh - 5
        bottoms = [dec_cell(c, kind, cell, x, y, cw) for x, cell in zip(xs, cells)]
        y = min(bottoms)
    return y

def fig_threshold(c, items, y):
    """Labeled cases on a line by score, with the thresholds that split the line into actions.
    With try lines instead of cut lines: one small strip per cut-off, with what it would do."""
    one = lambda k: next((f for kk, f in items if kk == k), None)
    yes, no = one("yes"), one("no")
    ys, ns = values(yes[1]), values(no[1])
    tries = [float(f[0]) for k, f in items if k == "try"]
    if tries:
        return fig_cutoffs(c, yes, no, ys, ns, tries, y)
    # the key
    for label, filled in ((yes[0], True), (no[0], False)):
        dot(c, ML + 3, y - 4, filled)
        c.setFillColor(INK); c.setFont("Sans", 6.6); c.drawString(ML + 10, y - 6.3, label)
        y -= 11
    cuts = [float(f[0]) for k, f in items if k == "cut"]
    zones = one("zone")
    y -= 14
    x0, x1 = ML + 3, PW - MR - 3
    X = lambda v: x0 + v * (x1 - x0)
    top, bottom = y, y - 34
    c.setFillColor(PANEL); c.rect(X(cuts[0]), bottom, X(cuts[-1]) - X(cuts[0]), top - bottom, stroke=0, fill=1)
    c.setFillColor(ZONE); c.rect(X(cuts[-1]), bottom, x1 - X(cuts[-1]), top - bottom, stroke=0, fill=1)
    for v in cuts:
        c.setStrokeColor(INK); c.setLineWidth(1); c.line(X(v), bottom, X(v), top + 3)
        label = f"{v:.2f}"
        lw = pdfmetrics.stringWidth(label, "Sans-Bold", 6.6)
        avatar(c, "Td", X(v) - (lw + 11) / 2, top + 5, 8)
        c.setFillColor(INK); c.setFont("Sans-Bold", 6.6); c.drawString(X(v) - (lw + 11) / 2 + 11, top + 6, label)
    for v in ys:
        dot(c, X(v), top - 10, True)
    for v in ns:
        dot(c, X(v), top - 24, False)
    c.setStrokeColor(INK); c.setLineWidth(0.5); c.line(x0, bottom, x1, bottom)
    c.setFillColor(GREY); c.setFont("Sans", 5.8)
    for v in (0, 0.25, 0.5, 0.75, 1):
        c.line(X(v), bottom, X(v), bottom - 2.5)
        c.drawCentredString(X(v), bottom - 9, f"{v:g}")
    axis = one("axis")
    if axis:
        c.drawCentredString((x0 + x1) / 2, bottom - 17, axis[0])
    y = bottom - 24
    edges = [0, *cuts, 1]
    low = y
    for k, name in enumerate(zones):
        a, b = X(edges[k]), X(edges[k + 1])
        key = NAME2MONO.get(name)
        if key in PART_TOKEN:
            avatar(c, key, (a + b) / 2 - 4, y - 8, 8)
        # A narrow zone's label may run wider than the zone; the end zones keep to the line's ends.
        w = max(b - a - 2, max(pdfmetrics.stringWidth(word, "Sans-Bold", 6.4) for word in name.split()) + 2)
        x = a + 1 if k == 0 else b - 1 - w if k == len(zones) - 1 else (a + b - w) / 2
        style = ParagraphStyle("z", parent=ZONE_CENTER, alignment=0 if k == 0 else 2 if k == len(zones) - 1 else 1)
        low = min(low, para(c, name, style, x, y - 11, w))
    return low

SORT_SCOREW, SORT_MSGX, SORT_CHIPX = 22, 32, 190
SORT_MSG = ParagraphStyle("sortmsg", parent=CELL, fontSize=7.4, leading=9.2)
SORT_NOTE = ParagraphStyle("sortnote", fontName="Sans-Bold", fontSize=6.8, leading=8.4, textColor=INK)
SAID_YES = tint("Wr", 0.22)  # the person's label is a written record: the Labeled case family
SORT_TINTS = (ZONE, PANEL, None)  # bands in order: the action with no person first, then review, then none

def label_chip(c, text, x, ytop, yes, mistake=False, size=6.4, width=None):
    """A person's label as a chip: yes on a light tint, no on white, both in ink with the same
    outline weight so neither looks smaller. A mistake has a heavy ink outline. width sets a
    common width for chips that sit in one column, with the text centred. Returns the width."""
    w = width or pdfmetrics.stringWidth(text, "Sans-Bold", size) + 10
    c.setFillColor(SAID_YES if yes else white)
    c.setStrokeColor(INK if mistake else CASE_INK if yes else GREY); c.setLineWidth(1.3 if mistake else 0.7)
    c.roundRect(x, ytop - 10.5, w, 10.5, 5.25, stroke=1, fill=1)
    c.setFillColor(INK); c.setFont("Sans-Bold", size)
    c.drawCentredString(x + w / 2, ytop - 7.4, text)
    return w

def fig_cutoffs(c, yes, no, ys, ns, tries, y):
    """For each cut-off, the saved messages it would refund automatically, as score chips in the
    person's-label style. A chip with a heavy outline is a refund nobody asked for."""
    x = ML
    x += label_chip(c, yes[0], x, y, True) + 5
    x += label_chip(c, no[0], x, y, False) + 5
    label_chip(c, "Refunded by mistake", x, y, False, mistake=True)
    y -= 19
    c.setFillColor(GREY); c.setFont("Sans-Bold", 6.2)
    c.drawString(ML, y - 6, "Threshold"); c.drawString(ML + 46, y - 6, "Refunded automatically")
    y -= 10
    for t in tries:
        rule(c, y, weight=0.3, color=HAIR)
        y -= 5
        picks = sorted([(v, True) for v in ys if v >= t] + [(v, False) for v in ns if v >= t], reverse=True)
        avatar(c, "Td", ML, y - 10, 10)
        c.setFillColor(INK); c.setFont("Sans-Bold", 7.4); c.drawString(ML + 14, y - 8, f"{t:.2f}")
        cx = ML + 46
        for v, ok in picks:
            cx += label_chip(c, f"{v:.2f}", cx, y, ok, mistake=not ok, size=6.2) + 3
        wrong = sum(not ok for _, ok in picks)
        c.setFillColor(INK); c.setFont("Sans-Bold", 6.6)
        c.drawRightString(PW - MR, y - 4.5, f"{len(picks)} refund{'s' * (len(picks) != 1)}")
        c.setFillColor(GREY); c.setFont("Sans", 6.4); c.drawRightString(PW - MR, y - 12, f"{wrong} by mistake")
        y -= 17
    return y

def sorted_row(c, f, labels, y, draw=True):
    """One message: its score, its text with any mistake note under it, and the person's label as
    a chip, filled for yes. Returns the bottom y."""
    score, text, said = f[0], f[1], f[2]
    note = f[3] if len(f) > 3 else None
    if draw:
        c.setFillColor(INK); c.setFont("Sans-Bold", 7.6)
        c.drawRightString(ML + SORT_SCOREW, y - 7.4, score)
        # Quiet chips, so the actions and the mistakes are what the eye finds first: yes on a
        # light tint in ink, no in grey on white.
        width = max(pdfmetrics.stringWidth(v, "Sans-Bold", 6.4) for v in labels.values()) + 12
        label_chip(c, labels[said], ML + SORT_CHIPX, y + 0.3, said == "yes", width=width)
    p = Paragraph(text, SORT_MSG)
    _, h = p.wrap(SORT_CHIPX - SORT_MSGX - 8, 1000)
    if draw:
        p.drawOn(c, ML + SORT_MSGX, y - 0.5 - h)
    bottom = y - 0.5 - h
    if note:
        q = Paragraph(note, SORT_NOTE)
        _, hn = q.wrap(W - SORT_MSGX, 1000)
        if draw:
            q.drawOn(c, ML + SORT_MSGX, bottom - 2 - hn)
        bottom -= 2 + hn
    return min(bottom, y - 11) - 5.5

def sorted_band(c, band, rows, labels, y, draw=True):
    """A band: the action in large type, then its messages. A row with a note is a mistake, set
    in a white box with an ink outline. Returns the bottom y."""
    key, label = (band[0], band[1]) if len(band) > 1 else (None, band[0])
    y -= 11
    x = ML
    if key in PART_TOKEN:
        if draw:
            avatar(c, key, ML, y - 12, 12)
        x += 16
    if draw:
        c.setFillColor(INK); c.setFont("Sans-Bold", 11.5); c.drawString(x, y - 10.5, label)
    y -= 21
    for f in rows:
        if len(f) > 3:  # a mistake: measure, box it, then draw
            bottom = sorted_row(canvas.Canvas(io.BytesIO()), f, labels, y - 3, draw=False)
            if draw:
                c.setFillColor(white); c.setStrokeColor(INK); c.setLineWidth(1.2)
                c.roundRect(ML - 3, bottom + 1, W + 6, y - bottom - 1, 3, stroke=1, fill=1)
            y = sorted_row(c, f, labels, y - 3, draw) - 3 if draw else bottom - 3
        else:
            y = sorted_row(c, f, labels, y, draw)
    return y - 8

def fig_sorted(c, items, y):
    """Messages sorted by score into one band per action. The thresholds are the heavy lines
    between bands. Built for a reader who sees the whole page at once: the actions first, then
    the boxed mistakes, then the messages."""
    labels = {f[0]: f[1] for k, f in items if k == "label"}
    head_ = next((f for k, f in items if k == "head"), None)
    if head_:
        c.setFillColor(GREY); c.setFont("Sans-Bold", 6.2)
        c.drawRightString(ML + SORT_SCOREW, y - 6, head_[0])
        c.drawString(ML + SORT_MSGX, y - 6, head_[1])
        c.drawString(ML + SORT_CHIPX, y - 6, head_[2])
        y -= 10
    bands, cuts = [], []  # bands: [band fields, rows]; cuts[i] follows bands[i]
    for k, f in items:
        if k == "band":
            bands.append([f, []])
        elif k == "row":
            bands[-1][1].append(f)
        elif k == "cut":
            cuts.append((len(bands) - 1, f[0]))
    lines = []
    for i, (band, rows) in enumerate(bands):
        bottom = sorted_band(canvas.Canvas(io.BytesIO()), band, rows, labels, y, draw=False)
        tint = SORT_TINTS[i] if i < len(SORT_TINTS) else None
        if tint is not None:
            c.setFillColor(tint); c.rect(ML - PAD, bottom, W + 2 * PAD, y - bottom, stroke=0, fill=1)
        sorted_band(c, band, rows, labels, y)
        y = bottom
        lines += [(y, value) for j, value in cuts if j == i]
    for ly, value in lines:  # the thresholds, over the band edges
        c.setStrokeColor(INK); c.setLineWidth(1.4); c.line(ML - PAD, ly, PW - MR + PAD, ly)
        text = f"Threshold {value}"
        tw = pdfmetrics.stringWidth(text, "Sans-Bold", 6.6)
        x1 = PW - MR
        x0 = x1 - tw - 18
        c.setFillColor(white); c.setStrokeColor(INK); c.setLineWidth(1.0)
        c.roundRect(x0, ly - 6.5, x1 - x0, 13, 2, stroke=1, fill=1)
        avatar(c, "Td", x0 + 4, ly - 4, 8)
        c.setFillColor(INK); c.setFont("Sans-Bold", 6.6); c.drawString(x0 + 15, ly - 2.3, text)
    return y

def fig_rulesets(c, items, y):
    """Two versions of the rules side by side, as columns."""
    names = list(dict.fromkeys(f[0] for k, f in items if k == "ruleset"))
    cw = (W - 14) / len(names)
    bottoms = []
    for n, name in enumerate(names):
        x = ML + n * (cw + 14)
        yy = head(c, name, x, y, cw)
        bottoms.append(rule_rows(c, [(f[1], f[2], True) for k, f in items if k == "ruleset" and f[0] == name],
                                 x, yy, cw))
    return min(bottoms)

def fig_record(c, items, y):
    """One saved record: a card of labelled fields."""
    title = next((f for k, f in items if k == "record"), None)
    rows = [f for k, f in items if k == "field"]
    lw = 74

    def draw(c, y):
        if title:
            y = head(c, title[0], ML, y, W, NAME2MONO.get(title[0]))
        for i, (label, value) in enumerate(rows):
            yl = para(c, label, CELLG, ML, y, lw - 6)
            yv = para(c, value, CELL, ML + lw, y, W - lw)
            y = min(yl, yv) - 4
        return y + 4
    bottom = draw(canvas.Canvas(io.BytesIO()), y - PAD)
    c.setStrokeColor(INK); c.setLineWidth(0.6); c.setFillColor(white)
    c.roundRect(ML - PAD, bottom - PAD, W + 2 * PAD, y - bottom + PAD, 3, stroke=1, fill=1)
    draw(c, y - PAD)
    return bottom - PAD

def page_meaning(c, n):
    y = plain_title(c, C.MEAN_TITLE)
    for t in C.MEAN_INTRO:
        y = para(c, t, BODY, ML, y, W) - SP_PARA
    y -= SP_SECTION - SP_PARA - 4
    y = table(c, C.MEAN_COLS, C.MEAN_ROWS, MEAN_WIDTHS, y)
    y = note(c, C.MEAN_NOTE, y)
    footer(c, n); check("meaning", y)

MEAN_WIDTHS = [72, 128, W - 200]

def page_table(c, n, sid):
    """A plain page: title, paragraphs, a table with a header row, and a closing note."""
    t = C.TABLE_PAGES[sid]
    y = plain_title(c, t["title"])
    for p in t["intro"]:
        y = para(c, p, BODY, ML, y, W) - SP_PARA
    y -= SP_SECTION - SP_PARA - 4
    y = table(c, t["cols"], t["rows"], TABLE_WIDTHS[sid], y)
    y = note(c, t["note"], y - 4)
    footer(c, n); check(sid, y)

# Column widths for each table page; the last column takes the rest of the text block.
TABLE_WIDTHS = {"levels": [40, 132, W - 172]}
# The width of the labels in the sections drawn after the entries.
BACK_LABW = {"shown": 92}

SEQ_FONT = 5.9

def label_box(c, text, xc, y, font="Sans", size=SEQ_FONT, color=INK, align="center"):
    """Text on a white backing so lifelines don't run through it."""
    w = pdfmetrics.stringWidth(text, font, size)
    x = xc - w / 2 if align == "center" else xc
    c.setFillColor(white); c.rect(x - 1.5, y - 1.6, w + 3, size + 1.8, stroke=0, fill=1)
    c.setFillColor(color); c.setFont(font, size); c.drawString(x, y, text)

def seq_columns():
    """x of each part's lifeline, evenly spaced across the text block."""
    k = len(C.SEQ_PARTS) - 1
    x0, x1 = ML + 18, PW - MR - 20
    return [x0 + i * (x1 - x0) / k for i in range(k + 1)]

def page_seq(c, n):
    y = tile_title(c, C.SEQ_TITLE, SEQ_TILE)
    y = para(c, C.SEQ_INTRO, BODY, ML, y, W) - SP_SECTION
    xs = seq_columns()
    head = y
    tsz = 12
    for (name, key, cap), x in zip(C.SEQ_PARTS, xs):
        avatar(c, key, x - tsz / 2, head - tsz, tsz)
        c.setFillColor(INK); c.setFont("Sans-Bold", 6.4); c.drawCentredString(x, head - tsz - 8, name)
        if cap:
            c.setFillColor(GREY); c.setFont("Sans", 5.8); c.drawCentredString(x, head - tsz - 15, cap)
    top = head - tsz - 20
    # measure the steps first so the lifelines end where the last step does
    step_h = {"msg": 14.5, "note": 9.5, "band": 14.5}
    bottom = top - 6 - sum(step_h[s[0]] for s in C.SEQ_STEPS) + 4
    c.setStrokeColor(HAIR); c.setLineWidth(0.5); c.setDash(1.5, 1.5)
    for x in xs:
        c.line(x, top, x, bottom)
    c.setDash()
    ym = top - 10
    for s in C.SEQ_STEPS:
        kind = s[0]
        if kind == "band":
            ym -= 3
            rule(c, ym + 7, weight=0.3, color=HAIR)
            label_box(c, s[1], ML, ym, font="Sans-Bold", size=6, color=GREY, align="left")
            ym -= step_h["band"] - 3
        elif kind == "note":
            # Left of the lifeline when the note would run past the right margin.
            x = xs[s[1]] + 3
            w = pdfmetrics.stringWidth(s[2], "Sans-Italic", 5.6)
            if x + w > PW - MR:
                x = xs[s[1]] - 3 - w
            label_box(c, s[2], x, ym + 2, font="Sans-Italic", size=5.6, color=GREY, align="left")
            ym -= step_h["note"]
        else:
            _, a, b, text, dashed = s
            x0, x1 = xs[a], xs[b]
            c.setStrokeColor(INK); c.setLineWidth(0.6)
            if dashed: c.setDash(2, 1.6)
            c.line(x0, ym, x1 + (-3 if x1 > x0 else 3), ym)
            c.setDash()
            arrow_head(c, x1, ym, "right" if x1 > x0 else "left")
            label_box(c, text, (x0 + x1) / 2, ym + 2.6)
            ym -= step_h["msg"]
    # Key: a solid arrow is a request, a dashed arrow a result.
    ky = bottom - 9
    c.setStrokeColor(INK); c.setLineWidth(0.6)
    c.line(ML, ky + 2, ML + 18, ky + 2); arrow_head(c, ML + 21, ky + 2, "right")
    label_box(c, "request", ML + 25, ky, color=GREY, align="left")
    c.setDash(2, 1.6); c.line(ML + 62, ky + 2, ML + 80, ky + 2); c.setDash()
    arrow_head(c, ML + 83, ky + 2, "right")
    label_box(c, "result", ML + 87, ky, color=GREY, align="left")
    y = ky - 10
    rule(c, y, weight=1, color=INK)
    y = para(c, C.SEQ_NOTE, SMALL, ML, y - 6, W)
    footer(c, n); check("sequence", y)

def page_fit(c, n):
    """How the parts fit: a title and its blocks. A guide built from the template draws its own
    diagram here."""
    y = plain_title(c, C.FIT_TITLE)
    y = blocks(c, C.FIT_BLOCKS, y)
    footer(c, n); check("fit", y)

ENTRY_TILE = 34

def entry(c, e, idx, ytop):
    """One entry, from ytop down: its name and numbered tile, the three rows, the field marks
    and Confused with. Returns the bottom y."""
    avatar(c, e["mono"], PW - MR - ENTRY_TILE, ytop - ENTRY_TILE, ENTRY_TILE, number=e["num"])
    thumb_tab(c, e["mono"], idx)
    c.setFillColor(INK); c.setFont("Sans-Bold", 20); c.drawString(ML, ytop - ENTRY_TILE + 1, e["name"])
    y = ytop - ENTRY_TILE - 8
    y = row(c, "Identify by", e["identify"], y, style=SMALL, weight=1, color=INK)
    y = row(c, "What", bold_first(e["what"]), y, style=BODY)
    y = row(c, "So what", bold_first(e["sowhat"]), y, style=BODY)
    for lines in e["figures"]:
        y = figure(c, lines, y - 8) - 4
    y -= 6
    if e["marks_grey"]:
        y = on_grey(c, y, lambda c_, y_: marks_grid(c_, e["marks"], y_)) - 8
    else:
        c.setFont("Sans-Bold", 6.8); c.setFillColor(GREY); c.drawString(ML, y - 6, "Field marks"); y -= 10
        for i, (l, s_, d) in enumerate(e["marks"]):
            y = row(c, l, short_detail(s_, d), y, **first(i))
        y -= 8
    other, test = e["confused"]
    rule(c, y, weight=1, color=INK); y -= 4.5
    yl = para(c, "Confused with", LABEL, ML, y, LABW)
    yt = tag(c, other, TX, y, style=SMALLB, w=TW)
    yt = para(c, test, SMALL, TX, yt - 1, TW)
    return min(yl, yt)

LABELG = ParagraphStyle("labelg", parent=LABEL, textColor=GREY)

def marks_grid(c, marks, y):
    """Field marks on a grey block, in three columns: each label over its short answer."""
    c.setFont("Sans-Bold", 6.8); c.setFillColor(GREY); c.drawString(ML, y - 6, "Field marks")
    y -= 13
    colw = W / 3
    for k in range(0, len(marks), 3):
        low = y
        for j, (l, s_, d) in enumerate(marks[k:k + 3]):
            x = ML + j * colw
            yl = para(c, l, LABELG, x, y, colw - 8)
            low = min(low, para(c, short_detail(s_, d), SMALL, x, yl, colw - 8))
        y = low - 5
    return y + 5

FLOW_X = (ML, ML + 11, ML + 72, ML + 170, ML + 236)
FLOW_W = (59, 94, 64, PW - MR - (ML + 236))

def page_flow(c, n):
    y = title(c, C.FLOW_TITLE)
    y = para(c, C.FLOW_INTRO, BODY, ML, y, W) - SP_SECTION + 4
    # columns: step number, who, what happens, part used, minutes
    x_num, x_who, x_what, x_part, x_add = FLOW_X
    w_who, w_what, w_part, w_add = FLOW_W
    low = y
    for x, w_, h in zip((x_who, x_what, x_part, x_add), (w_who, w_what, w_part, w_add), C.FLOW_COLS[1:]):
        low = min(low, para(c, h, CELLH, x, y, w_))
    y = low - 3.4
    for i, (who, what, parts, added) in enumerate(C.FLOW_STEPS):
        rule(c, y, **first(i))
        y -= 4
        c.setFillColor(GREY); c.setFont("Sans-Bold", 6.6); c.drawString(x_num, y - 6.6, str(i + 1))
        low = tag(c, who, x_who, y, size=9, style=CELLB, w=w_who)
        low = min(low, para(c, what, CELL, x_what, y, w_what))
        yp = y
        for p in parts:
            yp = tag(c, p, x_part, yp, size=9, style=CELL, w=w_part) - 2
        low = min(low, yp + 2)
        low = min(low, para(c, added, CELLG, x_add, y, w_add))
        y = low - 3.5
    rule(c, y, weight=1, color=INK)
    y = para(c, C.FLOW_NOTE, SMALL, ML, y - 6, W) - SP_SECTION - 4
    y = subhead(c, C.FLOW_CMP_HEAD, y, with_rule=False)
    y = table(c, C.FLOW_CMP_COLS, C.FLOW_CMP, FLOW_CMP_WIDTHS, y)
    y = note(c, C.FLOW_CMP_NOTE, y)
    footer(c, n); check("flow", y)

FLOW_CMP_WIDTHS = [112, 74, W - 186]

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

def page_side(c, n):
    y = title(c, C.SIDE_TITLE)
    w0 = 62; rest = (W - w0) / 3
    y = table(c, C.SIDE_COLS, C.SIDE_ROWS, [w0, rest, rest, rest], y)
    y -= 14
    rest2 = (W - w0) / 2
    y = table(c, C.SIDE_COLS2, C.SIDE_ROWS2, [w0, rest2, rest2], y)
    y = note(c, C.SIDE_NOTE, y - 10, BODY)
    footer(c, n); check("side", y)

# ---------- entries and terms, packed onto pages ----------
# The entries, then the sections in BACK (such as "What has been shown?" or "Easy to mix up"),
# go down the page one after another, and a new page starts only when the next one doesn't fit.
FLOW_GAP = 22

def flow_parts():
    return [("entry", i) for i in range(len(C.ENTRIES))] + [(x,) for x in C.BACK]

def draw_part(c, part, y):
    if part[0] == "entry":
        return entry(c, C.ENTRIES[part[1]], part[1], y)
    text, items = C.BACK[part[0]]
    return blocks(c, items, plain_title(c, text, y), labw=BACK_LABW.get(part[0], LABW)) + SP_PARA

def pack():
    """The flow parts, as pages: each a list of parts that fit on one page."""
    pages, y = [], MB
    for part in flow_parts():
        h = PH - draw_part(canvas.Canvas(io.BytesIO()), part, PH)
        if pages and y - FLOW_GAP - h >= MB:
            pages[-1].append(part)
            y -= FLOW_GAP + h
        else:
            pages.append([part])
            y = PH - MT - h
    return pages

PAGES = pack()
ENTRY_PAGE = {part[1]: ENTRY_START + k for k, parts in enumerate(PAGES) for part in parts if part[0] == "entry"}

def page_parts(c, parts, n):
    y = PH - MT
    for k, part in enumerate(parts):
        y = draw_part(c, part, y - (FLOW_GAP if k else 0))
    footer(c, n); check(f"page {n}", y)

URL = ParagraphStyle("url", fontName="Mono", fontSize=5.9, leading=8.2, textColor=GREY)
DATE = ParagraphStyle("date", fontName="Sans", fontSize=6.2, leading=7.8, textColor=GREY)

def source_line(date, address):
    """The grey line under a source: the date, then the address. A web address is set in mono;
    an internal source is named by its site, in the body face."""
    if " " in address:
        return f"{date} · {address}"
    return f'{date} · <font name="Mono" size="{URL.fontSize}">{address}</font>'

STAR_LABEL, STAR_TEXT, STAR_URL = "Leave a star: ", "accidental.info/star", "https://accidental.info/star/"
CONTACT_EMAIL = "friend@accidental.info"
_EDITION_PARTS = [part for part in C.EDITION.split(" · ") if "@" not in part]
END_FOOTER = " · ".join([CONTACT_EMAIL, *_EDITION_PARTS])

TAGLINE = "My friend has some questions."

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
    """End page: sources at the top, colophon at the bottom. No page number."""
    y = title(c, C.END_TITLE)
    y = para(c, C.END_INTRO, BODY, ML, y, W) - SP_PARA - 2
    for i, (name, date, address) in enumerate(C.END_SOURCES):
        rule(c, y, **first(i))
        y -= 2.3
        y = para(c, name, CELLB, ML, y, W) + 0.6
        y = para(c, source_line(date, address), DATE, ML, y, W) - 2
    size, gap = 20, 6
    yb = MB + 93
    if y < yb + size + 8:
        PROBLEMS.append(f"end: sources reach y={y:.1f}, into the colophon at {yb + size}")
    check("end", y)
    # colophon
    for i, e in enumerate(C.ENTRIES):
        avatar(c, e["mono"], ML + i * (size + gap), yb, size)
    c.setFillColor(GREY); c.setFont("Sans", 6.4)
    c.drawString(ML, yb - 12, C.KICKER)
    c.setFillColor(INK); c.setFont("Sans-Bold", 7.6)
    c.drawString(ML, yb - 22, C.TITLE)
    c.setFillColor(GREY); c.setFont("Sans", 6.4)
    colophon_y = yb - 31
    for line in wrap_words(C.SUBTITLE, "Sans", 6.4, W):
        c.drawString(ML, colophon_y, line)
        colophon_y -= 7.8
    colophon_y -= 1.2
    c.drawString(ML, colophon_y, "Written and reviewed by a person. AI does the grunt work.")
    colophon_y -= 9
    c.drawString(ML, colophon_y, "Set in TeX Gyre Heros and Newsreader.")
    colophon_y -= 10
    c.drawString(ML, colophon_y, STAR_LABEL)
    link(c, ML + pdfmetrics.stringWidth(STAR_LABEL, "Sans", 6.4), colophon_y, STAR_TEXT,
         "Mono", 5.9, STAR_URL)  # mono at the size of the sources' addresses
    rule(c, MB + 4, weight=1, color=INK)
    c.setFont("Sans", 6.4); c.setFillColor(GREY)
    tagline(c)
    c.setFont("Sans", 6.4); c.setFillColor(GREY)
    link(c, ML, MB - 6, CONTACT_EMAIL, "Sans", 6.4, f"mailto:{CONTACT_EMAIL}")
    c.setFont("Sans", 6.4)
    c.drawString(ML + pdfmetrics.stringWidth(CONTACT_EMAIL, "Sans", 6.4), MB - 6,
                 END_FOOTER[len(CONTACT_EMAIL):])

def build(out):
    c = canvas.Canvas(out, pagesize=(PW, PH), invariant=1)
    c.setTitle(C.TITLE); c.setAuthor("Accidental Guides"); c.setSubject(C.SUBTITLE)
    LIVE["canvas"] = c
    page_cover(c); c.showPage()
    n = 2
    for fn in [{"why": page_why, "meaning": page_meaning, "fit": page_fit}[x] for x in FRONT_IDS]:
        LIVE["page"] = n
        fn(c, n); c.showPage(); n += 1
    assert n == ENTRY_START, (n, ENTRY_START)
    for parts in PAGES:
        LIVE["page"] = n
        page_parts(c, parts, n); c.showPage(); n += 1
    back = (("seq", page_seq), ("levels", lambda c, n: page_table(c, n, "levels")), ("flow", page_flow),
            ("side", page_side))
    for sid, fn in back:
        if sid in HAVE:
            LIVE["page"] = n
            fn(c, n); c.showPage(); n += 1
    page_end(c); c.showPage(); n += 1
    c.save()
    return n - 1

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "judgment-to-action.pdf"
    pages = build(out)
    print(f"wrote {out}: {pages} pages")
    print("\n".join(PROBLEMS) if PROBLEMS else "no overflow")
    digest = hashlib.sha256(open(out, "rb").read()).hexdigest()
    print(f"sha256 {digest}")
    exp = os.path.join(HERE, "expected.sha256")
    if os.path.exists(exp):
        want = open(exp).read().split()[0]
        print("matches expected.sha256" if digest == want else f"DIFFERS from expected.sha256 ({want})")
