"""Build the pocket guide PDF.

Run from anywhere:  python3 build_guide.py [output.pdf]
Default output:     plugins-and-marketplaces.pdf in the current directory.

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
# The series rule: the entry number sets the colour, in every guide of the series, so a writer
# doesn't have to look it up and the thumb tabs and cover grid look the same in each guide.
# 01 brand, 02 success, 03 figjam, 04 warning, 05 assistive, 06 danger. The token names carry
# no meaning.
PART_TOKEN = {"Tl": "brand", "In": "success", "Hk": "figjam", "Pk": "warning", "Mk": "assistive"}
def colors(mono_key):
    t = PART_TOKEN[mono_key]; base = TOKENS[t]
    fg = INK if t == "warning" else white
    return HexColor(base), _dark(base, 0.86 if t == "warning" else 0.80), fg
NAME2MONO = {}  # filled in from the entries' names, below COVER_LINES
# Any other name, such as a product, is plain text with no tile.
# Tiles per row on the cover: two rows of two for four parts, otherwise rows of three.
COVER_COLS = 2 if len(C.ENTRIES) == 4 else 3
# The cover sets the title on these lines.
COVER_LINES = ("Plugins,", "Connectors, and", "Marketplaces")
assert " ".join(COVER_LINES) == C.TITLE, C.TITLE
# Each entry is one line on the map, and its name gets its tile wherever it labels a row. So
# does each name on the map that sits on only one line, along with its other names.
_lines_at = {}
for _key, _name, _stops in C.MAP_LINES:
    for _stop in _stops:
        _lines_at.setdefault(_stop, []).append(_key)
for _stop, _keys in _lines_at.items():
    if len(_keys) == 1:
        for _n in [_stop] + [o for o, _w in C.MAP_ALSO.get(_stop, ())]:
            NAME2MONO[_n] = _keys[0]
NAME2MONO.update({e["name"]: e["mono"] for e in C.ENTRIES})

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

MONO_RE = re.compile(r"(?<![\w/.<])((?:\.?[\w-]+/)+[\w.-]*|\.?[\w-]+(?:\.[\w-]+)*\.(?:md|json|toml|mcpb|sh|yml|yaml)\b|/[a-z][\w-]+)")

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
FRONT_IDS = [x for x in ("why", "meaning", "fit", "map") if x in HAVE]
ENTRY_START = 2 + len(FRONT_IDS)  # cover, the front pages present, then entries
# The corner tile on the sequence page: the diagram follows one work item.
SEQ_TILE = "Sn"

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

# ---------- pages ----------
def page_cover(c):
    c.setFillColor(INK); c.setFont("Sans-Bold", 9)
    c.drawString(ML, PH - MT - 8, C.KICKER)
    y = PH - MT - 22
    st = ParagraphStyle("t", fontName="Sans-Bold", fontSize=27, leading=29, textColor=INK)
    y = para(c, "<br/>".join(COVER_LINES), st, ML, y, W)
    y = para(c, C.SUBTITLE, LEAD, ML, y - 8, W * 0.8)
    size, colw = 38, W / COVER_COLS
    top = 214
    for i, e in enumerate(C.ENTRIES):
        col, r = i % COVER_COLS, i // COVER_COLS
        x = ML + col * colw
        yb = top - r * 80 - size
        avatar(c, e["mono"], x, yb, size, number=e["num"])
        c.setFillColor(INK); c.setFont("Sans-Bold", 7.6)
        c.drawString(x, yb - 11, e["name"])
        c.setFillColor(GREY); c.setFont("Sans", 6.6)
        c.drawString(x, yb - 20, f"page {ENTRY_START + i}")
    rule(c, MB + 4, weight=1, color=INK)
    c.setFont("Sans", 6.4); c.setFillColor(GREY)
    c.drawString(ML, MB - 6, f"{C.COVER_FOOTER} · Version {C.VERSION}")
    check("cover", y)

def page_why(c, n):
    y = plain_title(c, C.WHY_TITLE)
    for t in C.WHY_INTRO:
        y = para(c, t, BODY, ML, y, W) - 5
    if C.WHY_ROWS:
        y -= 4
        c.setFont("Sans-Bold", 6.8); c.setFillColor(GREY)
        c.drawString(ML, y - 7, C.WHY_HEAD[0]); c.drawString(TX, y - 7, C.WHY_HEAD[1])
        y -= 11
    for i, (term, meaning) in enumerate(C.WHY_ROWS):
        rule(c, y, **first(i))
        y -= 4.5
        yl = para(c, term, LABEL, ML, y, LABW)
        yt = para(c, meaning, SMALL, TX, y, TW)
        y = min(yl, yt) - 3.5
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
    y = table(c, t["cols"], t["rows"], TABLE_WIDTHS[sid], y, TABLE_CELL.get(sid))
    y = note(c, t["note"], y - 4)
    footer(c, n); check(sid, y)

# Column widths for each table page; the last column takes the rest of the text block.
# The product table has seven columns, so its cells are set smaller.
TABLE_CELL = {"who": ParagraphStyle("cells", parent=CELL, fontSize=6.0, leading=7.6)}
TABLE_WIDTHS = {"levels": [40, 132, W - 172], "shown": [92, W - 92], "who": [52] + [(W - 52) / 6] * 6}

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

# The overview diagram: one change, judged with nobody reading it, and failures coming back.
# Rows of the diagram, top of each row, measured from the top of the drawing. build_docx.py
# crops the same box out of the PDF, using fit_layout().
FIT_ROW = 67          # one 28 pt tile, its name and caption, and the arrow to the next row

def fit_layout():
    top = PH - MT - 26 - 4
    rows = [top - i * FIT_ROW for i in range(4)]
    bottom = rows[3] - 30
    return top, rows, bottom

# Every word in the diagram. Things that aren't one of the four parts are plain text.
FIT_PEOPLE = ("People", ("write the spec", "and the scenarios"))
FIT_SESSION = ("Agent session", ("writes the code and its tests",))
FIT_IN_USE = ("In use", ("released to users",))
FIT_WORK = "work items"
FIT_CHANGE = "a change"
FIT_SCENARIO = "kept where agents can\u2019t see"
FIT_TWIN = ("copies of the services", "the software calls")
FIT_RUNS = "run against"
FIT_JUDGED = "many runs, each judged"
FIT_SATISFACTION = "share of runs a user would accept"
FIT_RELEASED = "high enough"
FIT_LOOP = ("failures in use come", "back as new work")

def hline(c, x0, x1, y, head=True):
    c.setStrokeColor(INK); c.setLineWidth(0.6); c.line(x0, y, x1, y)
    if head:
        arrow_head(c, x1, y, "right" if x1 > x0 else "left")

def grey_label(c, text, x, y, align="left"):
    c.setFillColor(GREY); c.setFont("Sans", 6.2)
    if align == "left": c.drawString(x, y, text)
    elif align == "right": c.drawRightString(x, y, text)
    else: c.drawCentredString(x, y, text)

def text_node(c, xc, ytop, name, captions):
    """Something that isn't one of the parts: its name and caption in plain text, set where a
    tile's middle would be. Returns half the name's width, for the arrows that meet it."""
    c.setFillColor(INK); c.setFont("Sans-Bold", 7.4); c.drawCentredString(xc, ytop - 16, name)
    for k, cap in enumerate(captions):
        grey_label(c, cap, xc, ytop - 24 - 7.5 * k, "center")
    return pdfmetrics.stringWidth(name, "Sans-Bold", 7.4) / 2

def node_lines(c, e, xc, ytop, captions, size=28):
    avatar(c, e["mono"], xc - size / 2, ytop - size, size)
    c.setFillColor(INK); c.setFont("Sans-Bold", 7); c.drawCentredString(xc, ytop - size - 9, e["name"])
    for k, cap in enumerate(captions):
        grey_label(c, cap, xc, ytop - size - 17 - 7.5 * k, "center")

def page_fit(c, n):
    title(c, C.FIT_TITLE)
    E = {e["mono"]: e for e in C.ENTRIES}
    top, (r1, r2, r3, r4), bottom = fit_layout()
    xl, xc, xr = ML + 36, PW / 2, PW - MR - 14
    half = 14
    mid = 13   # a plain-text node's line, measured down from its row's top
    # Row 1: people write the work; an agent session does it.
    hp = text_node(c, xl, r1, *FIT_PEOPLE)
    hs = text_node(c, xc, r1, *FIT_SESSION)
    hline(c, xl + hp + 4, xc - hs - 4, r1 - mid)
    grey_label(c, FIT_WORK, (xl + hp + xc - hs) / 2, r1 - mid + 4, "center")
    # Row 2: the change is tried against the scenarios, with digital twins in place of outside
    # services.
    vline(c, xc, r1 - 30, r2 + 2)
    grey_label(c, FIT_CHANGE, xc + 6, (r1 - 30 + r2) / 2 - 1)
    node_lines(c, E["Sn"], xc, r2, (FIT_SCENARIO,))
    node_lines(c, E["Dt"], xl, r2, FIT_TWIN)
    hline(c, xc - half - 3, xl + half + 3, r2 - half)
    grey_label(c, FIT_RUNS, (xl + xc) / 2, r2 - half + 4, "center")
    # Row 3: satisfaction, from many judged runs.
    vline(c, xc, r2 - 28 - 21, r3 + 2)
    grey_label(c, FIT_JUDGED, xc + 6, (r2 - 28 - 21 + r3) / 2 - 1)
    node_lines(c, E["Sa"], xc, r3, (FIT_SATISFACTION,))
    # Row 4: released, with no person in between.
    hu = text_node(c, xc, r4, *FIT_IN_USE)
    vline(c, xc, r3 - 28 - 21, r4 - 8)
    grey_label(c, FIT_RELEASED, xc + 6, (r3 - 28 - 21 + r4 - 8) / 2 - 1)
    # The closed loop: from use, up the right side, back to an agent session.
    c.setStrokeColor(INK); c.setLineWidth(0.6)
    c.line(xc + hu + 4, r4 - mid, xr, r4 - mid); c.line(xr, r4 - mid, xr, r1 - mid)
    hline(c, xr, xc + hs + 4, r1 - mid)
    fb = r3 - 4
    avatar(c, E["Cl"]["mono"], xr - half, fb - 28, 28)
    c.setFillColor(INK); c.setFont("Sans-Bold", 7); c.drawRightString(xr - half - 5, fb - 9, E["Cl"]["name"])
    for k, cap in enumerate(FIT_LOOP):
        grey_label(c, cap, xr - half - 5, fb - 17 - 7.5 * k, "right")
    y = bottom - 12
    for t in C.FIT_BODY:
        y = para(c, t, BODY, ML, y, W) - 5
    footer(c, n); check("fit", y)

# The map: one line per entry, in the entry's colour, through a station for each name. Where
# the stations sit, and every word on the map, come from the {#map} block in guide.md. A
# station on two lines is an interchange: one name used for different things. A station with
# other names listed under it is an interchange too: one thing with several names.
# build_docx.py crops the same box out of the PDF, using map_layout().
MAP_TRACK = 3.4        # width of a line
MAP_DOT = 3.0          # radius of a station on one line
MAP_HUB = 4.6          # radius of an interchange
MAP_NAME = ParagraphStyle("mapname", fontName="Sans-Bold", fontSize=6.6, leading=7.6, textColor=INK)
MAP_CAP = ParagraphStyle("mapcap", fontName="Sans", fontSize=5.6, leading=6.6, textColor=GREY)
MAP_ALSO = ParagraphStyle("mapalso", fontName="Sans-Bold", fontSize=5.9, leading=6.9, textColor=INK)
MAP_LABEL_W = 104      # how wide a station's name and caption may run before wrapping
MAP_KEY_ROW = 12       # one row of the key under the map

def map_layout():
    """Top and bottom of the drawing (the map and its key), the grid step, and the grid's
    origin. The grid is as wide as the text block, less room for labels at either side."""
    y = PH - MT - 26
    y = para_height(C.MAP_INTRO, BODY, W, y) - SP_SECTION + 4
    top = y
    cols = max(s["col"] for s in C.MAP_STATIONS.values())
    rows = max(s["row"] for s in C.MAP_STATIONS.values())
    x0, x1 = ML + 26, PW - MR - 22
    dx = (x1 - x0) / cols
    dy = 34
    grid_top = top - 28  # room for the tiles at the top of the lines
    grid = (x0, grid_top, dx, dy)
    # The key starts under the lowest station or label.
    low = min(min(map_xy(n, grid)[1] - MAP_HUB,
                  map_label(None, n, *map_xy(n, grid), st["side"], st["caption"], C.MAP_ALSO.get(n, ())))
              for n, st in C.MAP_STATIONS.items())
    key_top = low - 16
    keys = len(C.MAP_LINES)
    bottom = key_top - ((keys + 1) // 2 + 1) * MAP_KEY_ROW
    return top, bottom, grid, key_top

def para_height(text, style, w, ytop):
    """Where a paragraph drawn at ytop would end, without drawing it."""
    p = Paragraph(mono(text, style.fontSize), style)
    _, h = p.wrap(w, 1000)
    return ytop - h

def map_xy(name, grid):
    x0, y0, dx, dy = grid
    st = C.MAP_STATIONS[name]
    return x0 + st["col"] * dx, y0 - st["row"] * dy

def map_path(c, pts):
    """A line through the stations: along the grid first, then at 45 degrees into the next
    station, as on a printed transit map."""
    p = c.beginPath(); p.moveTo(*pts[0])
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        dx, dy = bx - ax, by - ay
        d = min(abs(dx), abs(dy))
        if d > 0.5:
            sx, sy = (1 if dx > 0 else -1), (1 if dy > 0 else -1)
            p.lineTo(bx - sx * d, by - sy * d)
        p.lineTo(bx, by)
    c.drawPath(p, stroke=1, fill=0)

def map_label(c, name, x, y, side, caption, also=()):
    """A station's name in bold, then any other names for the same thing, each with where
    it's used in grey, then the caption in grey, on the given side of the station: r, l, a
    (above) or b (below), or above or below and running right (ar, br) or left (al, bl)."""
    align = {"r": 0, "l": 2, "a": 1, "b": 1, "ar": 0, "br": 0, "al": 2, "bl": 2}[side]
    names = ParagraphStyle("n", parent=MAP_NAME, alignment=align)
    caps = ParagraphStyle("c", parent=MAP_CAP, alignment=align)
    others = ParagraphStyle("o", parent=MAP_ALSO, alignment=align)
    grey = GREY.hexval().replace("0x", "#")
    lines = [Paragraph(mono(name, MAP_NAME.fontSize), names)]
    for other, where in also:
        tail = f' <font name="Sans" color="{grey}">{where}</font>' if where else ""
        lines.append(Paragraph(mono(other, MAP_ALSO.fontSize) + tail, others))
    pn = lines
    pc = Paragraph(mono(caption, MAP_CAP.fontSize), caps) if caption else None
    w = MAP_LABEL_W
    hn = sum(p_.wrap(w, 100)[1] for p_ in pn)
    hc = pc.wrap(w, 100)[1] if pc else 0
    gap = MAP_HUB + 3
    if side == "r":
        lx, top = x + gap, y + MAP_NAME.fontSize * 0.62
    elif side == "l":
        lx, top = x - gap - w, y + MAP_NAME.fontSize * 0.62
    else:
        lx = {"a": x - w / 2, "b": x - w / 2, "ar": x - 3, "br": x - 3, "al": x + 3 - w, "bl": x + 3 - w}[side]
        top = y + gap + hn + hc if side[0] == "a" else y - gap + 1
    if c is None:  # measuring only
        return top - hn - hc
    yy = top
    for p_ in pn:
        yy -= p_.height
        p_.drawOn(c, lx, yy)
    if pc:
        pc.drawOn(c, lx, top - hn - hc)
    return top - hn - hc

def page_map(c, n):
    y = title(c, C.MAP_TITLE)
    para(c, C.MAP_INTRO, BODY, ML, y, W)
    top, bottom, grid, key_top = map_layout()
    E = {e["mono"]: e for e in C.ENTRIES}
    stops = {}  # station name: the keys of the lines through it
    for key, _name, names in C.MAP_LINES:
        for s_ in names:
            stops.setdefault(s_, []).append(key)
    c.setLineCap(1); c.setLineJoin(1)
    # The lines, each starting at its tile.
    for key, _name, names in C.MAP_LINES:
        pts = [map_xy(s_, grid) for s_ in names]
        # The tile sits back along the first stretch of line; a line with one station starts
        # from the left.
        (ax, ay), (bx, by) = pts[0], (pts[1] if len(pts) > 1 else (pts[0][0] + 1, pts[0][1]))
        ux, uy = (0, (1 if ay > by else -1)) if abs(by - ay) >= abs(bx - ax) else ((1 if ax > bx else -1), 0)
        t = 12
        tx, ty = ax + ux * 20, ay + uy * 20
        c.setStrokeColor(colors(key)[0]); c.setLineWidth(MAP_TRACK)
        map_path(c, [(tx, ty)] + pts)
        avatar(c, key, tx - t / 2, ty - t / 2, t)
    # Stations, then their names on top of everything. An interchange is a larger white
    # circle with a black ring.
    for name, keys in stops.items():
        x, y_ = map_xy(name, grid)
        hub = len(keys) > 1 or name in C.MAP_ALSO
        c.setFillColor(white)
        c.setStrokeColor(INK if hub else colors(keys[0])[0])
        c.setLineWidth(1.4 if hub else 1.2)
        c.circle(x, y_, MAP_HUB if hub else MAP_DOT, stroke=1, fill=1)
    for name in stops:
        st = C.MAP_STATIONS[name]
        x, y_ = map_xy(name, grid)
        map_label(c, name, x, y_, st["side"], st["caption"], C.MAP_ALSO.get(name, ()))
    # The key: the lines in two columns, then the interchange across the full width.
    items = [(k, nm) for k, nm, _ in C.MAP_LINES]
    half = (len(items) + 1) // 2
    rule(c, key_top + 8, weight=0.3, color=HAIR)
    for i, (k, text) in enumerate(items):
        x = ML + (i // half) * (W / 2)
        yk = key_top - (i % half) * MAP_KEY_ROW
        c.setStrokeColor(colors(k)[0]); c.setLineWidth(MAP_TRACK)
        c.line(x + 9, yk, x + 18, yk)
        avatar(c, k, x, yk - 5, 10)
        c.setFillColor(INK); c.setFont("Sans", 6.4)
        c.drawString(x + 22, yk - 2.2, text)
    yk = key_top - half * MAP_KEY_ROW
    c.setFillColor(white); c.setStrokeColor(INK); c.setLineWidth(1.4)
    c.circle(ML + 5, yk, MAP_HUB, stroke=1, fill=1)
    c.setFillColor(INK); c.setFont("Sans", 6.4)
    c.drawString(ML + 22, yk - 2.2, MAP_KEY_HUB)
    c.setLineCap(0); c.setLineJoin(0)
    y = note(c, C.MAP_NOTE, bottom - 6)
    footer(c, n); check("map", y)

# The key's words for an interchange.
MAP_KEY_HUB = "Interchange: one name for different things, or one thing with several names"

def page_entry(c, e, idx, n):
    size = 46
    corner_avatar(c, e["mono"], number=e["num"], size=size)
    thumb_tab(c, e["mono"], idx)
    c.setFillColor(INK); c.setFont("Sans-Bold", 24); c.drawString(ML, PH - MT - size + 1, e["name"])
    y = PH - MT - size - 10
    # The Identify by row is optional.
    if e["identify"]:
        y = row(c, "Identify by", e["identify"], y, style=SMALL, weight=1, color=INK)
    y = row(c, "What", bold_first(e["what"]), y, style=BODY, **({} if e["identify"] else first(0)))
    y = row(c, "So what", bold_first(e["sowhat"]), y, style=BODY)
    y -= 8
    y = group_label(c, e["names_head"], y) - 2
    y = table(c, e["names_cols"], e["names"], NAMES_WIDTHS, y)
    y -= 8
    other, test = e["confused"]
    rule(c, y, weight=1, color=INK); y -= 4.5
    yl = para(c, "Confused with", LABEL, ML, y, LABW)
    yt = tag(c, other, TX, y, style=SMALLB, w=TW)
    yt = para(c, test, SMALL, TX, yt - 1, TW)
    y = min(yl, yt)
    footer(c, n); check(f"entry {e['name']}", y)

# The names table on an entry page: the name and what it is.
NAMES_WIDTHS = [LABW + GAP, W - LABW - GAP]

FLOW_X = (ML + 11, ML + 72, ML + 170, ML + 236)
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

def table(c, cols, rows, widths, y, cell=None):
    cell = cell or CELL
    head = ParagraphStyle("h", parent=cell, fontName="Sans-Bold", textColor=GREY)
    xs = [ML]
    for w_ in widths[:-1]:
        xs.append(xs[-1] + w_)
    # A header can wrap; the first row starts under the deepest one.
    low = y
    for j, h in enumerate(cols):
        low = min(low, para(c, h, head, xs[j], y, widths[j] - 6))
    y = low - 3.4
    for i, r in enumerate(rows):
        rule(c, y, **first(i))
        y -= 3.5
        low = y
        for j, v in enumerate(r):
            if j == 0:
                low = min(low, tag(c, v, xs[0], y, size=9,
                                   style=ParagraphStyle("b", parent=cell, fontName="Sans-Bold"), w=widths[0] - 4))
            else:
                low = min(low, para(c, v, cell, xs[j], y, widths[j] - 6))
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

def page_apart(c, n):
    y = title(c, C.APART_TITLE)
    y = subhead(c, C.APART_HEAD, y, with_rule=False)
    for i, (q, t) in enumerate(C.APART_ROWS):
        y = row(c, q, t, y, **first(i))
    y -= 14
    y = subhead(c, C.OTHER_TITLE, y, with_rule=False)
    for i, (l, t) in enumerate(C.OTHER_ROWS):
        y = row(c, l, t, y, **first(i))
    footer(c, n); check("apart+other", y)

URL = ParagraphStyle("url", fontName="Mono", fontSize=5.9, leading=8.2, textColor=GREY)
DATE = ParagraphStyle("date", fontName="Sans", fontSize=6.2, leading=7.8, textColor=GREY)

def source_line(date, address):
    """The grey line under a source: the date, then the address. A web address is set in mono;
    an internal source is named by its site, in the body face."""
    if " " in address:
        return f"{date} · {address}"
    return f'{date} · <font name="Mono" size="{URL.fontSize}">{address}</font>'

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
    c.drawString(ML, yb - 40, "Set in TeX Gyre Heros. Built with ReportLab.")
    rule(c, MB + 4, weight=1, color=INK)
    c.setFont("Sans", 6.4); c.setFillColor(GREY)
    c.drawString(ML, MB - 6, C.EDITION)

def build(out):
    c = canvas.Canvas(out, pagesize=(PW, PH), invariant=1)
    c.setTitle(C.TITLE); c.setAuthor("bstucker"); c.setSubject(C.SUBTITLE)
    page_cover(c); c.showPage()
    n = 2
    for fn in [{"why": page_why, "meaning": page_meaning, "fit": page_fit, "map": page_map}[x] for x in FRONT_IDS]:
        fn(c, n); c.showPage(); n += 1
    assert n == ENTRY_START, (n, ENTRY_START)
    for i, e in enumerate(C.ENTRIES):
        page_entry(c, e, i, n); c.showPage(); n += 1
    back = (("seq", page_seq), ("levels", lambda c, n: page_table(c, n, "levels")),
            ("shown", lambda c, n: page_table(c, n, "shown")),
            ("who", lambda c, n: page_table(c, n, "who")), ("flow", page_flow),
            ("side", page_side), ("apart", page_apart))
    for sid, fn in back:
        if sid in HAVE:
            fn(c, n); c.showPage(); n += 1
    page_end(c); c.showPage(); n += 1
    c.save()
    return n - 1

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "plugins-and-marketplaces.pdf"
    pages = build(out)
    print(f"wrote {out}: {pages} pages")
    print("\n".join(PROBLEMS) if PROBLEMS else "no overflow")
    digest = hashlib.sha256(open(out, "rb").read()).hexdigest()
    print(f"sha256 {digest}")
    exp = os.path.join(HERE, "expected.sha256")
    if os.path.exists(exp):
        want = open(exp).read().split()[0]
        print("matches expected.sha256" if digest == want else f"DIFFERS from expected.sha256 ({want})")
