# The guide's text, read from guide.md.
#
# guide.md is the source: edit it to change the text. This file parses it (with the
# standard library only) into the names that build_guide.py and build_docx.py use, so
# the layout code doesn't change when the text does. See README.md for the format.
#
# Voice: Brian's. Plain-spoken and direct, the way a colleague explains something over
# coffee, to a reader who may never have run a project. Contractions are fine. State the
# point, then the reason, and build one idea on the last. No taglines, slogans, rhetorical
# questions, "not X but Y", em-dash asides, rhythm triplets or stage direction ("this page",
# "below"). Rows must read on their own: no sentence starts with "it", "its", "they" or
# "this". Each field row leads with a short bold answer. Each term keeps one meaning. No
# quotes and no names of people in the body; public sources go on the sources page only. No
# text about the guide itself: no "this guide", page numbers or descriptions of the layout.
#
# One name per part: wine list, grape, dry, price, taste. These are the ordinary words of
# choosing a bottle in a restaurant, for someone who has just been handed the list. The
# person who brings the wine is "the server" (a sommelier, where there is one). Facts come
# from the public sources on the sources page and nowhere else. No names of people.

import re
from pathlib import Path

SOURCE = Path(__file__).with_name("guide.md")

HEADING = re.compile(r"^# (.*?) \{#([\w-]+)((?: [\w-]+=\S+?)*)\}$")
# A '>' block that starts with one of these is a callout with that label. Any other '>' block
# is a grey block.
ALERTS = {"[!TIP]": "Tip", "[!NOTE]": "Note", "[!WARNING]": "Watch out"}


class Section:
    """One '#' section of guide.md: its title, id, attributes and blocks in order.
    A block is ("p", text), ("h2", text), ("table", header, rows), ("diagram", lines),
    ("grey", blocks) for the paragraphs and tables in a '>' block, or ("callout", label, text)."""

    def __init__(self, title, sid, attrs):
        self.title, self.id, self.attrs, self.blocks = title, sid, attrs, []

    def all(self, kind):
        """Blocks of one kind, including those inside grey blocks."""
        flat = [x for b in self.blocks for x in (b[1] if b[0] == "grey" else [b])]
        return [b for b in flat if b[0] == kind]

    def grey_tables(self):
        return [(x[1], x[2]) for b in self.blocks if b[0] == "grey" for x in b[1] if x[0] == "table"]

    def paras(self):
        return [b[1] for b in self.all("p")]

    def tables(self):
        return [(b[1], b[2]) for b in self.all("table")]

    def heads(self):
        return [b[1] for b in self.all("h2")]


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse(text):
    """Return the front matter as a dict and the sections in order."""
    lines = text.splitlines()
    meta = {}
    i = 0
    if lines and lines[0] == "---":
        i = 1
        while lines[i] != "---":
            key, _, value = lines[i].partition(":")
            meta[key.strip()] = value.strip()
            i += 1
        i += 1
    sections = []
    para, table, fence = [], None, None
    quote = None  # inside a '>' block: [callout label or None, its blocks]

    def into():
        return quote[1] if quote else sections[-1].blocks

    def flush():
        nonlocal para, table
        if para:
            into().append(("p", " ".join(para)))
            para = []
        if table:
            into().append(("table", table[0], table[1:]))
            table = None

    def close_quote():
        nonlocal quote
        flush()
        label, blocks = quote
        quote = None
        if label:  # a callout is one paragraph
            sections[-1].blocks.append(("callout", label, " ".join(b[1] for b in blocks)))
        else:
            sections[-1].blocks.append(("grey", blocks))

    for line in lines[i:]:
        if fence is not None:
            if line.startswith("```"):
                sections[-1].blocks.append(("diagram", fence))
                fence = None
            else:
                fence.append(line)
            continue
        if line.startswith(">"):
            line = line[1:].removeprefix(" ")
            if quote is None:
                flush()
                quote = [ALERTS.get(line.strip()), []]
                if quote[0]:
                    continue
        elif quote is not None:
            close_quote()
        m = HEADING.match(line)
        if m:
            flush()
            attrs = dict(a.split("=", 1) for a in m.group(3).split())
            sections.append(Section(m.group(1), m.group(2), attrs))
        elif line.startswith("## "):
            flush()
            sections[-1].blocks.append(("h2", line[3:].strip()))
        elif line.startswith("```"):
            flush()
            fence = []
        elif line.startswith("|"):
            if para:
                flush()
            cells = _cells(line)
            if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                continue
            if table is None:
                table = []
            table.append(cells)
        elif not line.strip():
            flush()
        else:
            if table:
                flush()
            para.append(line.strip())
    if quote is not None:
        close_quote()
    flush()
    return meta, sections


META, SECTIONS = parse(SOURCE.read_text(encoding="utf-8"))


def section(sid):
    return next(s for s in SECTIONS if s.id == sid)


def rows(table):
    return [tuple(r) for r in table[1]]


# ---------------------------------------------------------------- cover and footers
TITLE = META["title"]
SUBTITLE = META["subtitle"]
KICKER = META["kicker"]
RUNNING_FOOTER = META["running_footer"]
EDITION = META["edition"]
COVER_FOOTER = META["cover_footer"]
# The cover's band: the collection the guide is in, the collection's mark and the guide's
# number in it. pnpm sync writes them from site/src/data/collections.json.
COLLECTION = META.get("collection", "")
COLLECTION_MARK = META.get("collection_mark", "")
NUMBER = META.get("number", "")
if not COLLECTION or COLLECTION_MARK not in ("square", "triangle", "circle", "diamond") \
        or not re.fullmatch(r"\d\d", NUMBER):
    raise SystemExit(f"{SOURCE}: front matter needs collection:, collection_mark: (square, "
                     "triangle, circle or diamond) and number: (two digits); pnpm sync writes them "
                     "for a guide listed in site/src/data/collections.json")
VERSION = META.get("version", "")
if not re.fullmatch(r"\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?(\+[0-9A-Za-z.-]+)?", VERSION):
    raise SystemExit(f"{SOURCE}: front matter needs version: as semver, such as 1.0.0 (got {VERSION!r})")

# ---------------------------------------------------------------- terms page
_s = section("why")
WHY_TITLE = _s.title
# The page is drawn block by block: paragraphs, the terms table, grey blocks and callouts.
WHY_BLOCKS = _s.blocks
# The summary the site shows for this guide. Not printed in the PDF.
BLURB = _s.paras()[0]

# ---------------------------------------------------------------- what people mean
if any(s.id == "meaning" for s in SECTIONS):
    _s = section("meaning")
    MEAN_TITLE = _s.title
    MEAN_INTRO = _s.paras()[:-1]
    _t = _s.tables()[0]
    MEAN_COLS = _t[0]
    MEAN_ROWS = rows(_t)
    MEAN_NOTE = _s.paras()[-1]

# ---------------------------------------------------------------- overview
# A page of blocks (paragraphs, a grey block, a callout), with no diagram drawn in code.
if any(s.id == "fit" for s in SECTIONS):
    _s = section("fit")
    FIT_TITLE = _s.title
    FIT_BLOCKS = _s.blocks

# ---------------------------------------------------------------- entries
ENTRIES = []
for _s in (s for s in SECTIONS if s.id == "entry"):
    _fields, _marks = _s.tables()
    _f = dict(_fields[1])
    ENTRIES.append(dict(
        num=_s.attrs["num"], mono=_s.attrs["mono"], name=_s.title,
        identify=_f["Identify by"], what=_f["What"], sowhat=_f["So what"],
        # A field marks table may leave out the Detail column.
        marks=[tuple(r) + ("",) * (3 - len(r)) for r in _marks[1]],
        marks_grey=_marks in _s.grey_tables(),
        confused=(_s.heads()[1].removeprefix("Confused with:").strip(), _s.paras()[0]),
    ))

# ---------------------------------------------------------------- unattended, closed loop, dark
if any(s.id == "modes" for s in SECTIONS):
    _s = section("modes")
    MODES_TITLE = _s.title
    MODES_INTRO = _s.paras()[:-1]
    _t = _s.tables()[0]
    MODES_COLS = _t[0]
    MODES_ROWS = rows(_t)
    MODES_NOTE = _s.paras()[-1]

# ---------------------------------------------------------------- an optional sequence diagram
SEQ_PARTS, SEQ_STEPS = [], []
_s = next((s for s in SECTIONS if s.id == "seq"), None)
if _s is not None:
    SEQ_TITLE = _s.title
    SEQ_INTRO, SEQ_NOTE = _s.paras()
# The diagram block: "part Label | Key | caption", then one step per line:
# "msg A -> B: label" (a request), "msg A --> B: label" (a result, drawn dashed),
# "band Label" and "note N: text". A and B count parts from 0.
for _line in (_s.all("diagram")[0][1] if _s is not None else []):
    _kind, _, _rest = _line.partition(" ")
    if _kind == "part":
        _p = [x.strip() for x in _rest.split("|")]
        SEQ_PARTS.append((_p[0], _p[1], _p[2] if len(_p) > 2 else ""))
    elif _kind == "msg":
        _m = re.fullmatch(r"(\d+) (-->|->) (\d+): (.*)", _rest)
        SEQ_STEPS.append(("msg", int(_m.group(1)), int(_m.group(3)), _m.group(4), _m.group(2) == "-->"))
    elif _kind == "band":
        SEQ_STEPS.append(("band", _rest))
    elif _kind == "note":
        _n, _, _text = _rest.partition(": ")
        SEQ_STEPS.append(("note", int(_n), _text))

# ---------------------------------------------------------------- two scales of level
if any(s.id == "levels" for s in SECTIONS):
    _s = section("levels")
    LEVELS_TITLE = _s.title
    LEVELS_INTRO, LEVELS_STAGES, LEVELS_NOTE = _s.paras()
    LEVELS_HEAD_A, LEVELS_HEAD_B = _s.heads()
    (LEVELS_COLS_A, _a), (LEVELS_COLS_B, _b) = _s.tables()
    LEVELS_ROWS_A = [tuple(r) for r in _a]
    LEVELS_ROWS_B = [tuple(r) for r in _b]

# ---------------------------------------------------------------- flow
if any(s.id == "flow" for s in SECTIONS):
    _s = section("flow")
    FLOW_TITLE = _s.title
    FLOW_INTRO, FLOW_NOTE, FLOW_CMP_NOTE = _s.paras()
    FLOW_CMP_HEAD = _s.heads()[0]
    _t = _s.tables()[1]
    FLOW_CMP_COLS = _t[0]
    FLOW_CMP = rows(_t)
    _t = _s.tables()[0]
    FLOW_COLS = _t[0]
    # The first column numbers the steps for the reader; the PDF numbers them itself.
    FLOW_STEPS = [(who, what, [p.strip() for p in parts.split(",") if p.strip()], added)
                  for _num, who, what, parts, added in _t[1]]

# ---------------------------------------------------------------- side by side
if any(s.id == "side" for s in SECTIONS):
    _s = section("side")
    SIDE_TITLE = _s.title
    (SIDE_COLS, _r1), (SIDE_COLS2, _r2) = _s.tables()
    SIDE_ROWS = [tuple(r) for r in _r1]
    SIDE_ROWS2 = [tuple(r) for r in _r2]
    SIDE_NOTE = _s.paras()[0]

# ---------------------------------------------------------------- internal names
if any(s.id == "names" for s in SECTIONS):
    _s = section("names")
    NAMES_TITLE = _s.title
    _t = _s.tables()[0]
    NAMES_COLS = _t[0]
    NAMES_ROWS = rows(_t)

# ---------------------------------------------------------------- apart + other
# Each is a title and its blocks, drawn after the entries, sharing a page when they fit.
if any(s.id == "apart" for s in SECTIONS):
    _s = section("apart")
    APART_TITLE = _s.title
    APART_BLOCKS = _s.blocks

if any(s.id == "other" for s in SECTIONS):
    _s = section("other")
    OTHER_TITLE = _s.title
    OTHER_BLOCKS = _s.blocks

# ---------------------------------------------------------------- end page
_s = section("sources")
END_TITLE = _s.title
END_INTRO = _s.paras()[0]
END_SOURCES = rows(_s.tables()[0])
