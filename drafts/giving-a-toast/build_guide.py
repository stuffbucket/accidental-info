"""Build the pocket guide PDF.

Run from anywhere:  python3 build_guide.py [output.pdf]
Default output:     giving-a-toast.pdf in the current directory.

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
# The opening, the story and the last line are words you prepare (things you write down).
# The length is a number.
PART_FAMILY = {"Op": "Wr", "Sy": "Wr", "Lt": "Wr", "Ln": "Nu"}
PART_TOKEN = {k: FAMILY_TOKEN[f] for k, f in PART_FAMILY.items()}
def colors(mono_key):
    t = PART_TOKEN[mono_key]; base = TOKENS[t]
    fg = INK if t == "warning" else white
    return HexColor(base), _dark(base, 0.86 if t == "warning" else 0.80), fg
NAME2MONO = {"Opening": "Op", "Story": "Sy", "Stories": "Sy", "Last line": "Lt", "Length": "Ln"}
# Any other name, such as the host, the honoree or a roast, is plain text with no tile.
# The cover sets the title on these lines.
COVER_LINES = ("Giving a", "Toast")
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

# Nothing in a cooking guide is a file name or a command, so nothing is set in mono.
MONO_RE = re.compile(r"(?!x)x")

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
SEQ_TILE = "Lt"

def para(c, text, style, x, ytop, w):
    p = Paragraph(mono(text, style.fontSize), style)
    _, h = p.wrap(w, 1000)
    p.drawOn(c, x, ytop - h)
    return ytop - h

def rule(c, y, x0=ML, x1=PW - MR, weight=0.3, color=HAIR):
    if not weight:
        return
    c.setStrokeColor(color); c.setLineWidth(weight); c.line(x0, y, x1, y)

def row(c, label, text, y, style=SMALL, pad=4.5, weight=0, color=HAIR, lstyle=LABEL):
    rule(c, y, weight=weight, color=color)
    y -= pad
    yl = para(c, label, lstyle, ML, y, LABW)
    yt = para(c, text, style, TX, y, TW)
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

def plain_title(c, text):
    """A page title with no corner tile that may break with <br/>. One line sits exactly where
    title() puts it, and content starts the same distance below the last line."""
    p = Paragraph(text, TITLE_ST)
    _, h = p.wrap(W, 200)
    p.drawOn(c, ML, PH - MT - h + 2)
    return PH - MT - h + 2 - 9

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

def blocks(c, items, y, grey=False):
    """A section's paragraphs, two-column tables, grey blocks and callouts, in order. A table is
    drawn as rows, with no rules on a grey block. Returns the bottom y."""
    for b in items:
        if b[0] == "p":
            y = para(c, b[1], SMALL if grey else BODY, ML, y, W) - SP_PARA
        elif b[0] == "table":
            for i, (label, text) in enumerate(b[2]):
                y = row(c, label, text, y, **({} if grey else first(i)))
            y -= SP_PARA
        elif b[0] == "grey":
            y = on_grey(c, y, lambda c_, y_, b=b: blocks(c_, b[1], y_, grey=True) + SP_PARA) - SP_PARA - 4
        elif b[0] == "callout":
            y = callout(c, b[1], b[2], y) - SP_PARA - 4
    return y

def page_meaning(c, n):
    y = plain_title(c, C.MEAN_TITLE)
    for t in C.MEAN_INTRO:
        y = para(c, t, BODY, ML, y, W) - SP_PARA
    y -= SP_SECTION - SP_PARA - 4
    y = table(c, C.MEAN_COLS, C.MEAN_ROWS, MEAN_WIDTHS, y)
    y = note(c, C.MEAN_NOTE, y)
    footer(c, n); check("meaning", y)

MEAN_WIDTHS = [72, 128, W - 200]

def page_modes(c, n):
    y = plain_title(c, C.MODES_TITLE)
    for t in C.MODES_INTRO:
        y = para(c, t, BODY, ML, y, W) - SP_PARA
    y -= SP_SECTION - SP_PARA - 4
    y = table(c, C.MODES_COLS, C.MODES_ROWS, MODES_WIDTHS, y)
    y = note(c, C.MODES_NOTE, y)
    footer(c, n); check("modes", y)

MODES_WIDTHS = [66, 70, 70, W - 206]

LEVELS_WIDTHS = [28, W - 28]

def page_levels(c, n):
    y = plain_title(c, C.LEVELS_TITLE)
    y = para(c, C.LEVELS_INTRO, BODY, ML, y, W) - SP_SECTION
    y = subhead(c, C.LEVELS_HEAD_A, y, with_rule=False)
    y = table(c, C.LEVELS_COLS_A, C.LEVELS_ROWS_A, LEVELS_WIDTHS, y)
    y -= SP_SECTION - 6
    y = subhead(c, C.LEVELS_HEAD_B, y, with_rule=False)
    y = para(c, C.LEVELS_STAGES, BODY, ML, y, W) - SP_PARA
    y = table(c, C.LEVELS_COLS_B, C.LEVELS_ROWS_B, LEVELS_WIDTHS, y)
    y = note(c, C.LEVELS_NOTE, y)
    footer(c, n); check("levels", y)

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

# The overview page: paragraphs, one grey block and a callout. No diagram is drawn in code.
def hline(c, x0, x1, y, head=True):
    c.setStrokeColor(INK); c.setLineWidth(0.6); c.line(x0, y, x1, y)
    if head:
        arrow_head(c, x1, y, "right" if x1 > x0 else "left")

def page_fit(c, n):
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

NAMES_WIDTHS = [62, 104, 74, W - 240]

def page_side(c, n):
    y = title(c, C.SIDE_TITLE)
    w0 = 62; rest = (W - w0) / 3
    y = table(c, C.SIDE_COLS, C.SIDE_ROWS, [w0, rest, rest, rest], y)
    y -= 14
    rest2 = (W - w0) / 2
    y = table(c, C.SIDE_COLS2, C.SIDE_ROWS2, [w0, rest2, rest2], y)
    y = note(c, C.SIDE_NOTE, y - 10, BODY)
    footer(c, n); check("side", y)

def page_names(c, n):
    y = title(c, C.NAMES_TITLE)
    y = table(c, C.NAMES_COLS, C.NAMES_ROWS, NAMES_WIDTHS, y)
    footer(c, n); check("names", y)

# ---------- entries and terms, packed onto pages ----------
# The entries, then "Easy to mix up" and "Related terms", go down the page one after another,
# and a new page starts only when the next one doesn't fit.
FLOW_GAP = 22

def flow_parts():
    return [("entry", i) for i in range(len(C.ENTRIES))] + [(x,) for x in ("apart", "other") if x in HAVE]

def draw_part(c, part, y):
    if part[0] == "entry":
        return entry(c, C.ENTRIES[part[1]], part[1], y)
    text, items = (C.APART_TITLE, C.APART_BLOCKS) if part[0] == "apart" else (C.OTHER_TITLE, C.OTHER_BLOCKS)
    return blocks(c, items, title(c, text, y)) + SP_PARA

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
    """End page: sources at the top, colophon at the bottom. No page number."""
    y = title(c, C.END_TITLE)
    y = para(c, C.END_INTRO, BODY, ML, y, W) - SP_PARA - 2
    for i, (name, date, address) in enumerate(C.END_SOURCES):
        rule(c, y, **first(i))
        y -= 2.3
        y = para(c, name, CELLB, ML, y, W) + 0.6
        y = para(c, source_line(date, address), DATE, ML, y, W) - 2
    size, gap = 20, 6
    yb = MB + 64
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
    for fn in [{"why": page_why, "meaning": page_meaning, "fit": page_fit}[x] for x in FRONT_IDS]:
        fn(c, n); c.showPage(); n += 1
    assert n == ENTRY_START, (n, ENTRY_START)
    for parts in PAGES:
        page_parts(c, parts, n); c.showPage(); n += 1
    back = (("modes", page_modes), ("seq", page_seq), ("levels", page_levels), ("flow", page_flow),
            ("side", page_side), ("names", page_names))
    for sid, fn in back:
        if sid in HAVE:
            fn(c, n); c.showPage(); n += 1
    page_end(c); c.showPage(); n += 1
    c.save()
    return n - 1

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "giving-a-toast.pdf"
    pages = build(out)
    print(f"wrote {out}: {pages} pages")
    print("\n".join(PROBLEMS) if PROBLEMS else "no overflow")
    digest = hashlib.sha256(open(out, "rb").read()).hexdigest()
    print(f"sha256 {digest}")
    exp = os.path.join(HERE, "expected.sha256")
    if os.path.exists(exp):
        want = open(exp).read().split()[0]
        print("matches expected.sha256" if digest == want else f"DIFFERS from expected.sha256 ({want})")
