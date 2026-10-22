"""Build the pocket guide as a Word document.

Run from anywhere:  python3 build_docx.py GUIDE.pdf [output.docx]

The text comes from content.py (which reads guide.md), the same as the PDF. The visual
rules come from build_guide.py, so the two outputs share them: the part colours, which
words are set in mono, and which part of a row is the bold short answer. The two
diagrams are drawn once, by the PDF build, and placed here as images rendered from
GUIDE.pdf, which must be the PDF built from the same text.

The document uses the PDF's page size and margins, starts each PDF page on a new page,
and embeds the PDF's fonts. Output is deterministic: the same input gives the same bytes.
"""
import io
import os
import re
import sys
import uuid
import zipfile
from datetime import datetime

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_ROW_HEIGHT_RULE, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING, WD_TAB_ALIGNMENT
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.opc.packuri import PackURI
from docx.opc.part import Part
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor
import pypdfium2 as pdfium

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_guide as G  # the PDF's layout constants and visual rules
import content as C

SANS = "TeX Gyre Heros"
MONO = "Liberation Mono"


def hexof(color):
    """A ReportLab colour as RRGGBB."""
    return color.hexval()[2:].upper()


INK, GREY, HAIR = hexof(G.INK), hexof(G.GREY), hexof(G.HAIR)


# ---------- text ----------
def rich(par, text, size, color=INK, bold=False, italic=False):
    """Add text to a paragraph: <b>…</b> spans in bold, and the words the PDF sets in mono
    (MONO_RE) in Liberation Mono at 90% size."""
    for i, chunk in enumerate(re.split(r"</?b>", text)):
        if not chunk:
            continue
        pos = 0
        for m in G.MONO_RE.finditer(chunk):
            _run(par, chunk[pos:m.start()], size, color, bold or i % 2 == 1, italic)
            _run(par, m.group(1), size * 0.9, color, bold or i % 2 == 1, italic, MONO)
            pos = m.end()
        _run(par, chunk[pos:], size, color, bold or i % 2 == 1, italic)
    return par


def _run(par, text, size, color, bold, italic, font=SANS):
    if not text:
        return None
    r = par.add_run(text)
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = RGBColor.from_string(color)
    if font != SANS:
        r.font.name = font
    return r


def para(container, text="", size=7.6, color=INK, bold=False, space_after=4, leading=None, italic=False):
    par = container.add_paragraph()
    pf = par.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(space_after)
    pf.line_spacing = Pt(leading or size * 1.37)
    rich(par, text, size, color, bold, italic)
    return par


def heading(doc, text, level=1, size=17, space_after=8):
    """A page title or subhead, as a Word heading so it shows in the navigation pane.
    '<br/>' in a title is a line break, as in the PDF."""
    par = doc.add_heading(level=level)
    pf = par.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(space_after)
    pf.line_spacing = Pt(size * 1.12)
    pf.keep_with_next = True
    for i, line in enumerate(text.split("<br/>")):
        if i:
            par.add_run().add_break(WD_BREAK.LINE)
        _run(par, line, size, INK, True, False)
    return par


def label(container, text, space_after=3):
    """The small grey label that names a group of rows, such as 'Field marks'."""
    return para(container, text, 6.8, GREY, bold=True, space_after=space_after)


# ---------- tiles ----------
TILE_DPI = 600
_tiles = {}


def tile_png(key, size, number=None):
    """A part's tile as a PNG: drawn by the PDF build's avatar() on a canvas the size of
    the tile, then rendered, so every tile in the Word document is the PDF's tile."""
    if (key, size, number) not in _tiles:
        buf = io.BytesIO()
        c = G.canvas.Canvas(buf, pagesize=(size, size), invariant=1)
        G.avatar(c, key, 0, 0, size, number=number)
        c.save()
        pdf = pdfium.PdfDocument(buf.getvalue())
        img = pdf[0].render(scale=TILE_DPI / 72).to_pil()
        pdf.close()
        out = io.BytesIO()
        img.save(out, format="PNG", optimize=True)
        _tiles[(key, size, number)] = out.getvalue()
    return io.BytesIO(_tiles[(key, size, number)])


def badge(par, key, size=9, gap=True):
    """A small tile inline with text, as the PDF's tag() draws it: lowered to sit on the
    text, and the line allowed to grow to fit it rather than clip it."""
    r = par.add_run()
    r.add_picture(tile_png(key, size), width=Pt(size))
    pos = OxmlElement("w:position")
    pos.set(qn("w:val"), str(-round(size * 0.5)))  # half-points: down by a quarter of the tile
    r._r.get_or_add_rPr().append(pos)
    par.paragraph_format.line_spacing_rule = WD_LINE_SPACING.AT_LEAST
    if gap:
        _run(par, "\u2002", 6, INK, False, False)


def tagged(par, name, size, color=INK, bold=True, tile=9):
    """A part name with its tile in front, if it has one, as the PDF's tag() does."""
    key = G.NAME2MONO.get(name)
    if key:  # a name that isn't one of the parts has no tile
        badge(par, key, tile)
    rich(par, name, size, color, bold)


# ---------- tables ----------
def _border(tc_pr, edge, size_pt, color):
    borders = tc_pr.find(qn("w:tcBorders"))
    if borders is None:
        borders = OxmlElement("w:tcBorders")
        tc_pr.append(borders)
    el = OxmlElement(f"w:{edge}")
    el.set(qn("w:val"), "single" if size_pt else "nil")
    el.set(qn("w:sz"), str(int(round(size_pt * 8))))
    el.set(qn("w:space"), "0")
    el.set(qn("w:color"), color)
    borders.append(el)


def _no_borders(table):
    tbl_pr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "nil")
        borders.append(el)
    tbl_pr.append(borders)


def widths(table, ws):
    """Set column widths on the grid, the table and each cell, so every reader agrees."""
    for j, w in enumerate(ws):
        table.columns[j].width = Pt(w)
        for cell in table.columns[j].cells:
            cell.width = Pt(w)
    tbl_w = table._tbl.tblPr.find(qn("w:tblW"))
    if tbl_w is None:
        tbl_w = OxmlElement("w:tblW")
        table._tbl.tblPr.append(tbl_w)
    tbl_w.set(qn("w:w"), str(int(sum(ws) * 20)))
    tbl_w.set(qn("w:type"), "dxa")
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    table._tbl.tblPr.append(layout)


def _margins(table, top=3.5, bottom=3, left=0, right=4):
    mar = OxmlElement("w:tblCellMar")
    for edge, v in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:w"), str(int(v * 20)))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    table._tbl.tblPr.append(mar)


def grid(doc, col_widths, rows, header=None, size=6.6, pad=(3.5, 3)):
    """A table laid out like the PDF's: no vertical lines, a heavy rule above the first
    row and hairlines between rows, and an optional grey bold header. Each row is a list
    of cell writers, functions that fill one cell's paragraph."""
    table = doc.add_table(rows=0, cols=len(col_widths))
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    _no_borders(table)
    _margins(table, top=pad[0], bottom=pad[1])
    if header:
        cells = table.add_row().cells
        for j, h in enumerate(header):
            p = cells[j].paragraphs[0]
            rich(p, h, size, GREY, bold=True)
    for i, row in enumerate(rows):
        cells = table.add_row().cells
        for j, write in enumerate(row):
            _border(cells[j]._tc.get_or_add_tcPr(), "top", 1 if i == 0 else 0.3, INK if i == 0 else HAIR)
            p = cells[j].paragraphs[0]
            p.paragraph_format.line_spacing = Pt(size * 1.30)  # the PDF's cell leading
            write(p)
    widths(table, col_widths)
    para(doc, "", 2, space_after=2)  # Word needs a paragraph between tables; keep it small
    return table


def text_cell(text, size=7.0, color=INK, bold=False):
    return lambda p: rich(p, text, size, color, bold)


def tag_cell(name, size=6.6, bold=True):
    return lambda p: tagged(p, name, size, INK, bold)


def rows_table(doc, items, size=7.0, label_w=G.LABW + G.GAP):
    """Label and text rows, like the PDF's row(): bold label on the left."""
    rest = G.W - label_w
    grid(doc, [label_w, rest], [[text_cell(l, 6.8, bold=True), text_cell(t, size)] for l, t in items])


def short_detail(short, detail):
    return G.short_detail(short, detail)


# ---------- tiles and titles ----------
def tile_cell(cell, key, size, number=None, align=WD_ALIGN_PARAGRAPH.RIGHT):
    """A part's large tile in a table cell, as the image the PDF build draws."""
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    p.add_run().add_picture(tile_png(key, size, number), width=Pt(size))


def titled(doc, text, key, size=17, number=None, tile=G.TILE):
    """A page title with the part's tile in the top-right corner, as the PDF's tile_title()."""
    table = doc.add_table(rows=1, cols=2)
    table.autofit = False
    _no_borders(table)
    _margins(table, top=0, bottom=0, left=0, right=0)
    left, right = table.rows[0].cells
    widths(table, [G.W - tile, tile])
    p = left.paragraphs[0]
    p.style = doc.styles["Heading 1"]
    p.paragraph_format.line_spacing = Pt(size * 1.12)
    for i, line in enumerate(text.split("<br/>")):
        if i:
            p.add_run().add_break(WD_BREAK.LINE)
        _run(p, line, size, INK, True, False)
    tile_cell(right, key, tile, number)
    para(doc, "", 6, space_after=6)
    return table


# ---------- bookmarks and page references ----------
_bookmark_id = [0]


def bookmark(par, name):
    _bookmark_id[0] += 1
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), str(_bookmark_id[0]))
    start.set(qn("w:name"), name)
    end = OxmlElement("w:bookmarkEnd")
    end.set(qn("w:id"), str(_bookmark_id[0]))
    par._p.insert(0, start)
    par._p.append(end)


def field(par, instr, cached, size, color=GREY, bold=False):
    """A Word field, such as PAGE or PAGEREF, showing `cached` until Word updates it."""
    def fld(kind):
        r = par.add_run()
        el = OxmlElement("w:fldChar")
        el.set(qn("w:fldCharType"), kind)
        r._r.append(el)
    fld("begin")
    r = par.add_run()
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = f" {instr} "
    r._r.append(it)
    fld("separate")
    _run(par, cached, size, color, bold, False)
    fld("end")


def entry_ref(i):
    return f"entry_{C.ENTRIES[i]['num']}"


# ---------- diagrams ----------
def diagram(doc, pdf, page_no, box):
    """Place one region of a page of the built PDF as an image. box is (x0, y0, x1, y1)
    in PDF points, origin bottom-left."""
    x0, y0, x1, y1 = box
    page = pdf[page_no - 1]
    bitmap = page.render(scale=300 / 72, crop=(x0, y0, G.PW - x1, G.PH - y1))
    buf = io.BytesIO()
    bitmap.to_pil().save(buf, format="PNG", optimize=True)
    buf.seek(0)
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    p.add_run().add_picture(buf, width=Pt(x1 - x0))


def fit_box():
    """The diagram on 'How the parts fit', from the PDF's own fit_layout()."""
    top, _rows, bottom = G.fit_layout()
    return (G.ML - 2, bottom - 2, G.PW - G.MR + 2, top + 2)


def map_box():
    """The map and its key, from the PDF's own map_layout()."""
    top, bottom, _grid, _key = G.map_layout()
    return (G.ML - 2, bottom - 4, G.PW - G.MR + 2, top + 2)


def seq_box():
    """The diagram on 'One work item through a factory', as G.page_seq() lays it out."""
    p = G.Paragraph(C.SEQ_TITLE, G.TITLE_ST)
    _, h = p.wrap(G.W - G.TILE - 12, 200)
    y = min(G.PH - G.MT - G.TILE, G.PH - G.MT - h) - G.SP_TILE
    p = G.Paragraph(G.mono(C.SEQ_INTRO, G.BODY.fontSize), G.BODY)
    _, h = p.wrap(G.W, 1000)
    head = y - h - G.SP_SECTION
    top = head - 12 - 20
    step_h = {"msg": 14.5, "note": 9.5, "band": 14.5}
    bottom = top - 6 - sum(step_h[s[0]] for s in C.SEQ_STEPS) + 4
    return (G.ML - 2, bottom - 14, G.PW - G.MR + 2, head + 2)  # includes the arrow key


# ---------- pages ----------
def page_cover(doc):
    para(doc, C.KICKER, 9, bold=True, space_after=6)
    # The PDF sets the title on the lines in COVER_LINES.
    lines = list(G.COVER_LINES)
    t = doc.add_paragraph(style="Title")
    t.paragraph_format.line_spacing = Pt(29)
    t.paragraph_format.space_after = Pt(8)
    for i, line in enumerate(lines):
        if i:
            t.add_run().add_break(WD_BREAK.LINE)
        _run(t, line, 27, INK, True, False)
    # The PDF puts the grid of tiles at a fixed height near the bottom of the page.
    para(doc, C.SUBTITLE, 8.6, space_after=cover_gap(lines), leading=11.8)
    size = 38
    cols = G.COVER_COLS
    table = doc.add_table(rows=2, cols=cols)
    table.autofit = False
    _no_borders(table)
    _margins(table, top=0, bottom=0, left=0, right=0)
    widths(table, [G.W / cols] * cols)
    for row in table.rows:
        row.height = Pt(80)
        row.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY
    for i, e in enumerate(C.ENTRIES):
        cell = table.rows[i // cols].cells[i % cols]
        tile_cell(cell, e["mono"], size, e["num"], align=WD_ALIGN_PARAGRAPH.LEFT)
        p = cell.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        rich(p, e["name"], 7.6, bold=True)
        p = cell.add_paragraph()
        rich(p, "page ", 6.6, GREY)
        field(p, f"PAGEREF {entry_ref(i)} \\h", str(G.ENTRY_START + i), 6.6)


def cover_gap(lines):
    """Space between the subtitle and the tile grid, from the PDF's page_cover() layout:
    the grid's top is at y=214."""
    st = G.ParagraphStyle("t", fontName="Sans-Bold", fontSize=27, leading=29)
    _, th = G.Paragraph("<br/>".join(lines), st).wrap(G.W, 1000)
    _, sh = G.Paragraph(G.mono(C.SUBTITLE, G.LEAD.fontSize), G.LEAD).wrap(G.W * 0.8, 1000)
    subtitle_bottom = G.PH - G.MT - 22 - th - 8 - sh
    return max(0, subtitle_bottom - 214)


def page_why(doc):
    heading(doc, C.WHY_TITLE)
    for t in C.WHY_INTRO:
        para(doc, t, 7.6, space_after=5)
    if C.WHY_ROWS:
        grid(doc, [G.LABW + G.GAP, G.TW], [
            [text_cell(term, 6.8, bold=True), text_cell(meaning, 7.0)] for term, meaning in C.WHY_ROWS
        ], header=list(C.WHY_HEAD))


def table_page(doc, title, intro, cols, rows, widths, note, size=6.6):
    """A plain concept page: title, paragraphs, a table with a header, and a closing note."""
    heading(doc, title)
    for t in intro:
        para(doc, t, 7.6, space_after=6)
    grid(doc, widths, [[tag_cell(r[0], size)] + [text_cell(v, size) for v in r[1:]] for r in rows],
         header=cols, size=size)
    para(doc, note, 7.0)


def page_meaning(doc):
    table_page(doc, C.MEAN_TITLE, C.MEAN_INTRO, C.MEAN_COLS, C.MEAN_ROWS, G.MEAN_WIDTHS, C.MEAN_NOTE)


def page_table(doc, sid):
    t = C.TABLE_PAGES[sid]
    cell = G.TABLE_CELL.get(sid)
    table_page(doc, t["title"], t["intro"], t["cols"], t["rows"], G.TABLE_WIDTHS[sid], t["note"],
               cell.fontSize if cell else 6.6)


def page_fit(doc, pdf):
    heading(doc, C.FIT_TITLE)
    diagram(doc, pdf, 2 + G.FRONT_IDS.index("fit"), fit_box())
    for t in C.FIT_BODY:
        para(doc, t, 7.6, space_after=5)


def page_map(doc, pdf):
    heading(doc, C.MAP_TITLE)
    para(doc, C.MAP_INTRO, 7.6, space_after=6)
    diagram(doc, pdf, 2 + G.FRONT_IDS.index("map"), map_box())
    para(doc, C.MAP_NOTE, 7.0)


def page_entry(doc, i, e):
    table = titled(doc, e["name"], e["mono"], size=24, number=e["num"])
    bookmark(table.rows[0].cells[0].paragraphs[0], entry_ref(i))
    grid(doc, [G.LABW + G.GAP, G.TW], ([
        [text_cell("Identify by", 6.8, bold=True), text_cell(e["identify"], 7.0)]] if e["identify"] else []) + [
        [text_cell("What", 6.8, bold=True), text_cell(G.bold_first(e["what"]), 7.6)],
        [text_cell("So what", 6.8, bold=True), text_cell(G.bold_first(e["sowhat"]), 7.6)],
    ])
    label(doc, e["names_head"])
    grid(doc, G.NAMES_WIDTHS, [[text_cell(a, 6.6, bold=True), text_cell(b, 6.6), text_cell(c, 6.6)]
                               for a, b, c in e["names"]], header=list(e["names_cols"]))
    other, test = e["confused"]
    grid(doc, [G.LABW + G.GAP, G.TW], [[
        text_cell("Confused with", 6.8, bold=True),
        lambda p: (tagged(p, other, 7.0), p.add_run().add_break(), rich(p, test, 7.0)),
    ]])


def page_seq(doc, pdf):
    titled(doc, C.SEQ_TITLE, G.SEQ_TILE)
    para(doc, C.SEQ_INTRO, 7.6, space_after=8)
    back = [x for x in ("seq",) if x in G.HAVE]
    diagram(doc, pdf, G.ENTRY_START + len(C.ENTRIES) + back.index("seq"), seq_box())
    para(doc, C.SEQ_NOTE, 7.0)


def page_flow(doc):
    heading(doc, C.FLOW_TITLE)
    para(doc, C.FLOW_INTRO, 7.6, space_after=10)

    def parts_cell(parts):
        def write(p):
            for k, name in enumerate(parts):
                if k:
                    p.add_run().add_break()
                tagged(p, name, 6.6, bold=False)
        return write

    xs = G.FLOW_X + (G.PW - G.MR,)
    grid(doc, [xs[i + 1] - xs[i] for i in range(5)],
         [[text_cell(str(i + 1), 6.6, GREY, True), tag_cell(who), text_cell(what, 6.6),
           parts_cell(parts), text_cell(added, 6.6, GREY)]
          for i, (who, what, parts, added) in enumerate(C.FLOW_STEPS)],
         header=C.FLOW_COLS, pad=(2.5, 2))  # the densest table; Word's padding is looser than the PDF's
    para(doc, C.FLOW_NOTE, 7.0, space_after=10)
    heading(doc, C.FLOW_CMP_HEAD, level=2, size=11, space_after=4)
    grid(doc, G.FLOW_CMP_WIDTHS, [[text_cell(a, 6.6, bold=True), text_cell(b, 6.6), text_cell(c, 6.6)]
                                  for a, b, c in C.FLOW_CMP], header=C.FLOW_CMP_COLS)
    para(doc, C.FLOW_CMP_NOTE, 7.0)


def page_side(doc):
    heading(doc, C.SIDE_TITLE)
    w0 = 62
    rest = (G.W - w0) / 3
    grid(doc, [w0, rest, rest, rest],
         [[tag_cell(r[0])] + [text_cell(v, 6.6) for v in r[1:]] for r in C.SIDE_ROWS],
         header=C.SIDE_COLS)
    rest2 = (G.W - w0) / 2
    grid(doc, [w0, rest2, rest2],
         [[tag_cell(r[0])] + [text_cell(v, 6.6) for v in r[1:]] for r in C.SIDE_ROWS2],
         header=C.SIDE_COLS2)
    para(doc, C.SIDE_NOTE, 7.6)


def page_apart(doc):
    heading(doc, C.APART_TITLE)
    heading(doc, C.APART_HEAD, level=2, size=11, space_after=3)
    rows_table(doc, C.APART_ROWS)
    heading(doc, C.OTHER_TITLE, level=2, size=11, space_after=3)
    rows_table(doc, C.OTHER_ROWS)


def page_end(doc):
    heading(doc, C.END_TITLE)
    para(doc, C.END_INTRO, 7.6, space_after=8)

    def source(p, n, d, a):
        rich(p, n, 6.6, bold=True)
        p.add_run().add_break()
        _run(p, f"{d} · ", 6.2, GREY, False, False)
        _run(p, a, 6.2 if " " in a else 5.9, GREY, False, False, SANS if " " in a else MONO)

    grid(doc, [G.W], [[lambda p, n=n, d=d, a=a: source(p, n, d, a)] for n, d, a in C.END_SOURCES],
         pad=(2.5, 2))
    para(doc, "", 7.6, space_after=24)
    p = para(doc, "", 7.6, space_after=6)
    for k, e in enumerate(C.ENTRIES):
        badge(p, e["mono"], 20, gap=False)
        if k < len(C.ENTRIES) - 1:
            _run(p, "\u2009", 6, INK, False, False)
    para(doc, C.KICKER, 6.4, GREY, space_after=1)
    para(doc, C.TITLE, 7.6, bold=True, space_after=1)
    para(doc, C.SUBTITLE, 6.4, GREY, space_after=1)
    para(doc, "Set in TeX Gyre Heros. Built with python-docx.", 6.4, GREY, space_after=0)


# ---------- document setup ----------
def setup(doc):
    s = doc.sections[0]
    s.page_width, s.page_height = Pt(G.PW), Pt(G.PH)
    s.left_margin, s.right_margin = Pt(G.ML), Pt(G.MR)
    s.top_margin, s.bottom_margin = Pt(G.MT), Pt(G.MB)
    s.footer_distance = Pt(G.MB - 22)
    s.header_distance = Pt(12)
    for name in ("Normal", "Title", "Heading 1", "Heading 2"):
        st = doc.styles[name]
        st.font.name = SANS
        st.font.color.rgb = RGBColor.from_string(INK)
        rpr = st.element.get_or_add_rPr()
        fonts = rpr.find(qn("w:rFonts"))
        for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            fonts.set(qn(attr), SANS)
        for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
            fonts.attrib.pop(qn(attr), None)
    doc.styles["Normal"].font.size = Pt(7.6)
    doc.styles["Normal"].paragraph_format.space_after = Pt(0)
    for name in ("Title", "Heading 1", "Heading 2"):
        st = doc.styles[name]
        # Bold is a toggle in Word: bold in both the style and the run can cancel out. The
        # runs set it, so the styles don't.
        st.font.bold = None
        st.paragraph_format.space_before = Pt(0)
        pbdr = st.element.get_or_add_pPr().find(qn("w:pBdr"))
        if pbdr is not None:  # the template's Title has a rule under it; the guide doesn't
            pbdr.getparent().remove(pbdr)


def running_footer(section):
    f = section.footer
    f.is_linked_to_previous = False
    p = f.paragraphs[0]
    p.paragraph_format.tab_stops.add_tab_stop(Pt(G.W), alignment=WD_TAB_ALIGNMENT.RIGHT)
    _run(p, C.RUNNING_FOOTER, 6, GREY, False, False)
    _run(p, "\t", 6, GREY, False, False)
    field(p, "PAGE", "2", 6)


def start_numbering(section, start):
    """Number the section's pages from `start`. pgNumType has a fixed place in sectPr."""
    num = OxmlElement("w:pgNumType")
    num.set(qn("w:start"), str(start))
    after = ("cols", "formProt", "vAlign", "noEndnote", "titlePg", "textDirection", "bidi",
             "rtlGutter", "docGrid", "printerSettings", "sectPrChange")
    sect = section._sectPr
    for child in sect:
        if child.tag in [qn(f"w:{a}") for a in after]:
            child.addprevious(num)
            return
    sect.append(num)


def ruled_footer(section, text):
    """The cover's and end page's footer: a heavy rule, then grey text, as the PDF has."""
    f = section.footer
    f.is_linked_to_previous = False
    p = f.paragraphs[0]
    bdr = OxmlElement("w:pBdr")
    top = OxmlElement("w:top")
    for k, v in (("w:val", "single"), ("w:sz", "8"), ("w:space", "4"), ("w:color", INK)):
        top.set(qn(k), v)
    bdr.append(top)
    p._p.get_or_add_pPr().append(bdr)
    _run(p, text, 6.4, GREY, False, False)


def new_page(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def build(pdf_path, out):
    doc = Document()
    setup(doc)
    pdf = pdfium.PdfDocument(pdf_path)

    page_cover(doc)
    ruled_footer(doc.sections[0], f"{C.COVER_FOOTER} · Version {C.VERSION}")
    body = doc.add_section(WD_SECTION.NEW_PAGE)
    running_footer(body)
    start_numbering(body, 2)

    # Pilot: only the pages whose section is in guide.md, as build_guide.py does.
    front = {"why": page_why, "meaning": page_meaning, "fit": lambda d: page_fit(d, pdf),
             "map": lambda d: page_map(d, pdf)}
    pages = [front[x] for x in G.FRONT_IDS]
    pages += [lambda d, i=i, e=e: page_entry(d, i, e) for i, e in enumerate(C.ENTRIES)]
    back = (("seq", lambda d: page_seq(d, pdf)), ("levels", lambda d: page_table(d, "levels")),
            ("shown", lambda d: page_table(d, "shown")), ("who", lambda d: page_table(d, "who")),
            ("flow", page_flow), ("side", page_side),
            ("apart", page_apart))
    pages += [fn for sid, fn in back if sid in G.HAVE]
    for k, fn in enumerate(pages):
        if k:
            new_page(doc)
        fn(doc)
    end = doc.add_section(WD_SECTION.NEW_PAGE)
    ruled_footer(end, C.EDITION)
    page_end(doc)

    props = doc.core_properties
    props.title, props.subject, props.author = C.TITLE, C.SUBTITLE, "bstucker"
    props.last_modified_by, props.revision = "bstucker", 1
    # Fixed dates, like the PDF's invariant mode.
    props.created = props.modified = props.last_printed = datetime(1999, 12, 31)
    props.comments = props.keywords = props.category = ""

    drop_thumbnail(doc)
    embed_fonts(doc)
    buf = io.BytesIO()
    doc.save(buf)
    write_fixed(buf.getvalue(), out)
    pdf.close()
    return 2 + len(pages)


def drop_thumbnail(doc):
    """python-docx's template carries a stock thumbnail image; the guide has none."""
    rels = doc.part.package.rels
    for rid, rel in list(rels.items()):
        if rel.reltype == RT.THUMBNAIL:
            del rels[rid]


# ---------- embedded fonts ----------
FONTS = [  # (family, style element, file)
    (SANS, "embedRegular", "heros-regular.ttf"),
    (SANS, "embedBold", "heros-bold.ttf"),
    (SANS, "embedItalic", "heros-italic.ttf"),
    (MONO, "embedRegular", "LiberationMono-Regular.ttf"),
]


def obfuscate(data, key):
    """ECMA-376 font obfuscation: XOR the first 32 bytes with the key GUID's bytes, read
    from the end of its hex digits."""
    hexkey = key.strip("{}").replace("-", "")
    k = bytes(int(hexkey[30 - 2 * i:32 - 2 * i], 16) for i in range(16))
    head = bytes(b ^ k[i % 16] for i, b in enumerate(data[:32]))
    return head + data[32:]


def embed_fonts(doc):
    """Embed the PDF's fonts so Word shows the document in them. The keys are derived from
    the font names, so they are the same on every build."""
    package = doc.part.package
    table_part = next(p for p in package.iter_parts() if p.partname == "/word/fontTable.xml")
    from lxml import etree
    root = etree.fromstring(table_part.blob)
    w = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    r = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    for n, (family, element, filename) in enumerate(FONTS, 1):
        key = "{" + str(uuid.uuid5(uuid.NAMESPACE_URL, f"accidental-guides/{filename}")).upper() + "}"
        with open(os.path.join(G.FONT_DIR, filename), "rb") as f:
            blob = obfuscate(f.read(), key)
        part = Part(PackURI(f"/word/fonts/font{n}.odttf"),
                    "application/vnd.openxmlformats-officedocument.obfuscatedFont", blob, package)
        rid = table_part.relate_to(part, RT.FONT)
        font = root.find(f"{{{w}}}font[@{{{w}}}name='{family}']")
        if font is None:
            font = etree.SubElement(root, f"{{{w}}}font", {f"{{{w}}}name": family})
        etree.SubElement(font, f"{{{w}}}{element}", {f"{{{r}}}id": rid, f"{{{w}}}fontKey": key})
    table_part._blob = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

    settings = doc.settings.element
    before = ["writeProtection", "view", "zoom", "removePersonalInformation", "removeDateAndTime",
              "doNotDisplayPageBoundaries", "displayBackgroundShape", "printPostScriptOverText",
              "printFractionalCharacterWidth", "printFormsData"]
    index = 0
    for i, child in enumerate(settings):
        if etree.QName(child).localname in before:
            index = i + 1
    settings.insert(index, OxmlElement("w:embedTrueTypeFonts"))
    # The template declares Word 2010; declare the current format so Word doesn't open the
    # document in Compatibility Mode.
    for cs in settings.iter(qn("w:compatSetting")):
        if cs.get(qn("w:name")) == "compatibilityMode":
            cs.set(qn("w:val"), "15")


def write_fixed(data, out):
    """Rewrite the .docx zip with fixed entry times, so the same input gives the same bytes."""
    src = zipfile.ZipFile(io.BytesIO(data))
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as dst:
        for info in src.infolist():
            fixed = zipfile.ZipInfo(info.filename, date_time=(1999, 12, 31, 0, 0, 0))
            fixed.compress_type = zipfile.ZIP_DEFLATED
            fixed.external_attr = 0o644 << 16
            dst.writestr(fixed, src.read(info.filename))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: build_docx.py GUIDE.pdf [output.docx]")
    pdf_path = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "plugins-and-marketplaces.docx"
    pages = build(pdf_path, out)
    print(f"wrote {out}: {pages} pages")
