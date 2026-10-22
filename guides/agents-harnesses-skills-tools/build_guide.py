"""Build the pocket guide PDF.

Run from anywhere:  python3 build_guide.py [output.pdf]
Default output:     agents-harnesses-skills-tools.pdf in the current directory.

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
# Parts mapped to the colours they already have in the team's diagram where possible.
PART_TOKEN = {"Mo": "warning", "Ha": "brand", "Ag": "success", "Sk": "figjam", "To": "assistive", "Mc": "danger"}
def colors(mono_key):
    t = PART_TOKEN[mono_key]; base = TOKENS[t]
    fg = INK if t == "warning" else white
    return HexColor(base), _dark(base, 0.86 if t == "warning" else 0.80), fg
NAME2MONO = {"Model": "Mo", "Harness": "Ha", "Agent": "Ag", "Agents": "Ag", "Sub-agent": "Ag",
             "Sub-agents": "Ag", "Skill": "Sk", "Tool": "To", "MCP server": "Mc"}

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

MONO_RE = re.compile(r"(?<![\w/.<])((?:\.?[\w-]+/)+[\w.-]*|[\w-]+\.(?:md|sh)\b|/[a-z][\w-]+|git diff)")

def mono(text, size):
    return MONO_RE.sub(lambda m: f'<font name="Mono" size="{size*0.9:.2f}">{m.group(1)}</font>', text)

def bold_first(text):
    i = text.find(". ")
    return text if i < 0 else f"<b>{text[:i + 1]}</b>{text[i + 1:]}"

def short_detail(short, detail):
    return f"<b>{short}.</b> {detail}" if detail else f"<b>{short}.</b>"

PROBLEMS = []
ENTRY_START = 6  # cover, words, model and context, fit, legend, then entries

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
    if key:
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
    y = para(c, "Agents<br/>Harnesses<br/>Skills and Tools", st, ML, y, W)
    y = para(c, C.SUBTITLE, LEAD, ML, y - 8, W * 0.8)
    size, colw = 38, W / 3
    top = 214
    for i, e in enumerate(C.ENTRIES):
        col, r = i % 3, i // 3
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
    y = title(c, C.WHY_TITLE)
    for t in C.WHY_INTRO:
        y = para(c, t, BODY, ML, y, W) - 5
    y -= 4
    c.setFont("Sans-Bold", 6.8); c.setFillColor(GREY)
    c.drawString(ML, y - 7, C.WHY_HEAD[0]); c.drawString(TX, y - 7, C.WHY_HEAD[1])
    y -= 11
    for i, (part, symptom, fix) in enumerate(C.WHY_ROWS):
        rule(c, y, **first(i))
        y -= 4.5
        yl = tag(c, part, ML, y)
        yt = para(c, symptom, SMALLB, TX, y, TW)
        yt = para(c, fix, SMALL, TX, yt - 1, TW)
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

def page_context(c, n):
    y = tile_title(c, C.CTX_TITLE, "Mo")
    for t in C.CTX_INTRO:
        y = para(c, t, BODY, ML, y, W) - SP_PARA
    y -= SP_SECTION - SP_PARA
    y = subhead(c, C.CTX_HEAD, y, with_rule=False)
    w0 = 84; rest = W - w0
    y = table(c, C.CTX_COLS, C.CTX_ROWS, [w0, rest * 0.42, rest * 0.58], y)
    rule(c, y, weight=1, color=INK)
    y = para(c, C.CTX_NOTE, SMALL, ML, y - 6, W)
    footer(c, n); check("context", y)

def page_tools_a(c, n):
    y = tile_title(c, C.TOOLS_TITLE, "To")
    y = para(c, C.TOOLS_INTRO, BODY, ML, y, W) - SP_SECTION
    y = subhead(c, C.TOOLS_CALL_HEAD, y)
    for t in C.TOOLS_CALL:
        y = para(c, bold_first(t) if t is C.TOOLS_CALL[0] else t, BODY, ML, y, W) - SP_PARA
    y -= SP_SECTION - SP_PARA
    y = subhead(c, C.TOOLS_KINDS_HEAD, y, with_rule=False)
    w0 = 62; rest = W - w0
    y = table(c, C.TOOLS_KINDS_COLS, C.TOOLS_KINDS, [w0, rest * 0.58, rest * 0.42], y)
    footer(c, n); check("tools a", y)

SEQ_FONT = 5.9

def label_box(c, text, xc, y, font="Sans", size=SEQ_FONT, color=INK, align="center"):
    """Text on a white backing so lifelines don't run through it."""
    w = pdfmetrics.stringWidth(text, font, size)
    x = xc - w / 2 if align == "center" else xc
    c.setFillColor(white); c.rect(x - 1.5, y - 1.6, w + 3, size + 1.8, stroke=0, fill=1)
    c.setFillColor(color); c.setFont(font, size); c.drawString(x, y, text)

def page_seq(c, n):
    y = tile_title(c, C.SEQ_TITLE, "To")
    y = para(c, C.SEQ_INTRO, BODY, ML, y, W) - SP_SECTION
    xs = [ML + 16, ML + 84, ML + 144, ML + 200, ML + 252]
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
            label_box(c, s[2], xs[s[1]] + 3, ym + 2, font="Sans-Italic", size=5.6, color=GREY, align="left")
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
    y = bottom - 10
    rule(c, y, weight=1, color=INK)
    y = para(c, C.SEQ_NOTE, SMALL, ML, y - 6, W)
    footer(c, n); check("sequence", y)

def page_tools_b(c, n):
    y = tile_title(c, C.TOOLS_FOLLOWS_HEAD, "To")
    y = group_label(c, C.TOOLS_CTX_LABEL, y)
    for i, (l, s_, d) in enumerate(C.TOOLS_CTX):
        y = row(c, l, short_detail(s_, d), y, **first(i))
    y -= SP_SECTION - 4
    y = group_label(c, C.TOOLS_USE_LABEL, y)
    for i, (l, s_, d) in enumerate(C.TOOLS_USE):
        y = row(c, l, short_detail(s_, d), y, **first(i))
    footer(c, n); check("tools b", y)

def page_fit(c, n):
    y = title(c, C.FIT_TITLE)
    E = {e["name"]: e for e in C.ENTRIES}
    top = y - 4
    xc = PW / 2
    xl, xs, xr = ML + 40, ML + 128, PW - MR - 40
    mb = node(c, E["Model"], xc, top, "reads and writes text")
    c.setFillColor(INK); c.setFont("Sans-Bold", 7); c.drawCentredString(xl, top - 16, "You")
    c.setFillColor(GREY); c.setFont("Sans", 6.2); c.drawCentredString(xl, top - 24, "start a session")
    bt = mb - 44; bh = 20
    vline(c, xc, mb - 22, bt, heads=("down", "up"))
    c.setFillColor(GREY); c.setFont("Sans", 6.2)
    c.drawString(xc + 6, mb - 30, "context in;")
    c.drawString(xc + 6, mb - 37.5, "text and tool calls out")
    vline(c, xl, top - 28, bt, heads=("down",))
    hb, hd, hf = colors("Ha")
    c.setFillColor(hb); c.rect(ML, bt - bh, W, bh, stroke=0, fill=1)
    c.setFillColor(hd); c.rect(ML, bt - bh, W, 4, stroke=0, fill=1)
    c.setFillColor(hf); c.setFont("Sans-Bold", 8.4)
    c.drawString(ML + 8, bt - bh / 2 - 1.5, "Harness")
    c.setFont("Sans", 6.2)
    c.drawRightString(PW - MR - 8, bt - bh / 2 - 1, "runs the main agent’s loop and every tool call")
    rowtop = bt - bh - 22
    for name, label, x, cap in (("Agent", "Sub-agent", xl, "separate loop, own context"),
                                ("Skill", "Skill", xs, "procedure the model reads")):
        vline(c, x, bt - bh, rowtop, heads=("down",))
        node(c, E[name], x, rowtop, cap, name=label)
    tt = rowtop - 28 - 17 - 16
    th = 66
    vline(c, xr, bt - bh, tt, heads=("down",))
    c.setFillColor(GREY); c.setFont("Sans", 6.2)
    c.drawRightString(xr - 5, (bt - bh + tt) / 2 + 2, "tool calls")
    c.setStrokeColor(INK); c.setLineWidth(1); c.rect(ML, tt - th, W, th, stroke=1, fill=0)
    avatar(c, "To", ML + 6, tt - 18, 12)
    c.setFillColor(INK); c.setFont("Sans-Bold", 8.4); c.drawString(ML + 24, tt - 15, "Tools")
    c.setFillColor(GREY); c.setFont("Sans", 6.2)
    c.drawRightString(PW - MR - 6, tt - 14, "everything the session acts with")
    rule(c, tt - 23, ML, PW - MR, weight=0.3, color=HAIR)
    cw = W / 3
    cells = [("Built-in tools", None, "Read, Edit, Bash, WebSearch"),
             ("MCP tools", "Mc", "exposed by MCP servers such as workiq"),
             ("Scripts and CLIs", None, "run through Bash: detect-linter.sh, git, gh")]
    for i, (h, k, t) in enumerate(cells):
        x = ML + i * cw
        if i:
            c.setStrokeColor(HAIR); c.setLineWidth(0.3); c.line(x, tt - 23, x, tt - th)
        hx = x + 6
        if k:
            avatar(c, k, hx, tt - 36, 9); hx += 13
        yy = para(c, h, CELLB, hx, tt - 27, cw - 12)
        para(c, t, CELLG, x + 6, yy - 1, cw - 12)
    y = tt - th - 14
    for t in C.FIT_BODY:
        y = para(c, t, BODY, ML, y, W) - 5
    footer(c, n); check("fit", y)

def page_legend(c, n):
    y = title(c, C.LEGEND_TITLE)
    y = para(c, C.LEGEND_INTRO, BODY, ML, y, W) - 8
    for i, (l, t) in enumerate(C.LEGEND_ROWS):
        y = row(c, l, t, y, **first(i))
    y -= 14
    c.setFont("Sans-Bold", 6.8); c.setFillColor(GREY); c.drawString(ML, y, "Entries"); y -= 6
    for i, e in enumerate(C.ENTRIES):
        rule(c, y, **first(i))
        avatar(c, e["mono"], ML, y - 17, 13)
        c.setFillColor(GREY); c.setFont("Sans-Bold", 7); c.drawString(ML + 20, y - 12.5, e["num"])
        c.setFillColor(INK); c.setFont("Sans-Bold", 7.6); c.drawString(TX, y - 12.5, e["name"])
        c.setFont("Sans", 7); c.setFillColor(GREY); c.drawRightString(PW - MR, y - 12.5, str(ENTRY_START + i))
        y -= 21
    footer(c, n); check("legend", y)

def page_entry(c, e, idx, n):
    size = 46
    corner_avatar(c, e["mono"], number=e["num"], size=size)
    thumb_tab(c, e["mono"], idx)
    c.setFillColor(INK); c.setFont("Sans-Bold", 24); c.drawString(ML, PH - MT - size + 1, e["name"])
    y = PH - MT - size - 10
    y = row(c, "Identify by", e["identify"], y, style=SMALL, weight=1, color=INK)
    y = row(c, "What", bold_first(e["what"]), y, style=BODY)
    y = row(c, "So what", bold_first(e["sowhat"]), y, style=BODY)
    y -= 8
    c.setFont("Sans-Bold", 6.8); c.setFillColor(GREY); c.drawString(ML, y - 6, "Field marks"); y -= 10
    for i, (l, s_, d) in enumerate(e["marks"]):
        y = row(c, l, short_detail(s_, d), y, **first(i))
    y -= 8
    other, test = e["confused"]
    rule(c, y, weight=1, color=INK); y -= 4.5
    yl = para(c, "Confused with", LABEL, ML, y, LABW)
    yt = tag(c, other, TX, y, style=SMALLB, w=TW)
    yt = para(c, test, SMALL, TX, yt - 1, TW)
    y = min(yl, yt)
    footer(c, n); check(f"entry {e['name']}", y)

def page_flow(c, n):
    y = title(c, C.FLOW_TITLE)
    y = para(c, C.FLOW_INTRO, BODY, ML, y, W) - SP_SECTION + 4
    # columns: step number, who, what happens, part used, added to the context
    x_num, x_who, x_what, x_part, x_add = ML, ML + 11, ML + 66, ML + 166, ML + 212
    w_who, w_what, w_part, w_add = 53, 96, 44, PW - MR - x_add
    for x, w_, h in zip((x_who, x_what, x_part, x_add), (w_who, w_what, w_part, w_add), C.FLOW_COLS[1:]):
        para(c, h, CELLH, x, y, w_)
    y -= 12
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
    y = para(c, C.FLOW_NOTE, SMALL, ML, y - 6, W)
    footer(c, n); check("flow", y)

def table(c, cols, rows, widths, y):
    xs = [ML]
    for w_ in widths[:-1]:
        xs.append(xs[-1] + w_)
    for j, h in enumerate(cols):
        para(c, h, CELLH, xs[j], y, widths[j] - 6)
    y -= 12
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
    y -= 10
    rule(c, y, weight=1, color=INK)
    y = para(c, C.SIDE_NOTE, BODY, ML, y - 7, W)
    footer(c, n); check("side", y)

def page_apart(c, n):
    y = title(c, C.APART_TITLE)
    for i, (q, t) in enumerate(C.APART_ROWS):
        y = row(c, q, t, y, **first(i))
    y -= 14
    c.setFillColor(INK); c.setFont("Sans-Bold", 11); c.drawString(ML, y - 10, C.OTHER_TITLE)
    y = para(c, C.OTHER_INTRO, SMALLG, ML, y - 17, W) - 7
    for i, (l, t) in enumerate(C.OTHER_ROWS):
        y = row(c, l, t, y, **first(i))
    footer(c, n); check("apart+other", y)

URL = ParagraphStyle("url", fontName="Mono", fontSize=5.9, leading=8.2, textColor=GREY)

def page_end(c):
    """End page: sources at the top, colophon at the bottom. No page number."""
    y = title(c, C.END_TITLE)
    y = para(c, C.END_INTRO, BODY, ML, y, W) - SP_SECTION + 6
    for i, (name, url) in enumerate(C.END_SOURCES):
        rule(c, y, **first(i))
        y -= 4
        y = para(c, name, CELLB, ML, y, W) - 1
        p = Paragraph(url, URL); _, h = p.wrap(W, 100); p.drawOn(c, ML, y - h); y -= h + 3.5
    check("end", y)
    # colophon
    size, gap = 20, 6
    yb = MB + 64
    for i, e in enumerate(C.ENTRIES):
        avatar(c, e["mono"], ML + i * (size + gap), yb, size)
    c.setFillColor(INK); c.setFont("Sans-Bold", 7.6)
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
    for fn in (page_why, page_context, page_fit, page_legend):
        fn(c, n); c.showPage(); n += 1
    assert n == ENTRY_START, (n, ENTRY_START)
    for i, e in enumerate(C.ENTRIES):
        page_entry(c, e, i, n); c.showPage(); n += 1
    for fn in (page_tools_a, page_seq, page_tools_b, page_flow, page_side, page_apart):
        fn(c, n); c.showPage(); n += 1
    page_end(c); c.showPage(); n += 1
    c.save()
    return n - 1

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "agents-harnesses-skills-tools.pdf"
    pages = build(out)
    print(f"wrote {out}: {pages} pages")
    print("\n".join(PROBLEMS) if PROBLEMS else "no overflow")
    digest = hashlib.sha256(open(out, "rb").read()).hexdigest()
    print(f"sha256 {digest}")
    exp = os.path.join(HERE, "expected.sha256")
    if os.path.exists(exp):
        want = open(exp).read().split()[0]
        print("matches expected.sha256" if digest == want else f"DIFFERS from expected.sha256 ({want})")
