# The guide's text, read from guide.md.
#
# guide.md is the source: edit it to change the text. This file parses it (with the
# standard library only) into the names that build_guide.py and build_docx.py use, so
# the layout code doesn't change when the text does. See README.md for the format.
#
# Voice: Brian's. Plain-spoken, direct, full sentences of moderate length, contractions are fine.
# State the point, then the reason. No taglines, slogans, idioms or mannered prose.
# Rows must read on their own: no sentence starts with "it", "its", "they" or "this"; name the
# subject instead. Each field row leads with a short bold answer.
# Use the generally accepted name for each part. Marketing terms and terms that apply to more
# than one concept are not used. "Agent" always carries a qualifier: main agent, sub-agent or
# agent definition.

import re
from pathlib import Path

SOURCE = Path(__file__).with_name("guide.md")

HEADING = re.compile(r"^# (.*?) \{#([\w-]+)((?: [\w-]+=\S+?)*)\}$")


class Section:
    """One '#' section of guide.md: its title, id, attributes and blocks in order.
    A block is ("p", text), ("h2", text), ("table", header, rows) or ("diagram", lines)."""

    def __init__(self, title, sid, attrs):
        self.title, self.id, self.attrs, self.blocks = title, sid, attrs, []

    def all(self, kind):
        return [b for b in self.blocks if b[0] == kind]

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

    def flush():
        nonlocal para, table
        if para:
            sections[-1].blocks.append(("p", " ".join(para)))
            para = []
        if table:
            sections[-1].blocks.append(("table", table[0], table[1:]))
            table = None

    for line in lines[i:]:
        if fence is not None:
            if line.startswith("```"):
                sections[-1].blocks.append(("diagram", fence))
                fence = None
            else:
                fence.append(line)
            continue
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
VERSION = META.get("version", "")
if not re.fullmatch(r"\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?(\+[0-9A-Za-z.-]+)?", VERSION):
    raise SystemExit(f"{SOURCE}: front matter needs version: as semver, such as 1.0.0 (got {VERSION!r})")

# ---------------------------------------------------------------- terms page
_s = section("why")
WHY_TITLE = _s.title
WHY_INTRO = _s.paras()
_t = _s.tables()[0]
WHY_HEAD = (_t[0][0], _t[0][1])
WHY_ROWS = rows(_t)
# The summary the site shows for this guide. Not printed in the PDF.
BLURB = WHY_INTRO[0]

# ---------------------------------------------------------------- model and context window
_s = section("context")
CTX_TITLE = _s.title
CTX_INTRO = _s.paras()[:-1]
CTX_HEAD = _s.heads()[0]
_t = _s.tables()[0]
CTX_COLS = _t[0]
CTX_ROWS = rows(_t)
CTX_NOTE = _s.paras()[-1]

# ---------------------------------------------------------------- overview
_s = section("fit")
FIT_TITLE = _s.title
FIT_BODY = _s.paras()

# ---------------------------------------------------------------- legend
_s = section("legend")
LEGEND_TITLE = _s.title
LEGEND_INTRO = _s.paras()[0]
LEGEND_ROWS = rows(_s.tables()[0])

# ---------------------------------------------------------------- entries
ENTRIES = []
for _s in (s for s in SECTIONS if s.id == "entry"):
    _fields, _marks = _s.tables()
    _f = dict(_fields[1])
    ENTRIES.append(dict(
        num=_s.attrs["num"], mono=_s.attrs["mono"], name=_s.title,
        identify=_f["Identify by"], what=_f["What"], sowhat=_f["So what"],
        marks=rows(_marks),
        confused=(_s.heads()[1].removeprefix("Confused with:").strip(), _s.paras()[0]),
    ))

# ---------------------------------------------------------------- tool section
_s = section("tools")
TOOLS_TITLE = _s.title
TOOLS_INTRO = _s.paras()[0]
TOOLS_CALL_HEAD, TOOLS_KINDS_HEAD = _s.heads()
TOOLS_CALL = _s.paras()[1:]
_t = _s.tables()[0]
TOOLS_KINDS_COLS = _t[0]
TOOLS_KINDS = rows(_t)

_s = section("seq")
SEQ_TITLE = _s.title
SEQ_INTRO, SEQ_NOTE = _s.paras()
# The diagram block: "part Label | Key | caption", then one step per line:
# "msg A -> B: label" (a request), "msg A --> B: label" (a result, drawn dashed),
# "band Label" and "note N: text". A and B count parts from 0.
SEQ_PARTS, SEQ_STEPS = [], []
for _line in _s.all("diagram")[0][1]:
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

_s = section("tools-follow")
TOOLS_FOLLOWS_HEAD = _s.title
TOOLS_CTX_LABEL, TOOLS_USE_LABEL = _s.heads()
_ctx, _use = _s.tables()
TOOLS_CTX = rows(_ctx)
TOOLS_USE = rows(_use)

# ---------------------------------------------------------------- flow
_s = section("flow")
FLOW_TITLE = _s.title
FLOW_INTRO, FLOW_NOTE = _s.paras()
_t = _s.tables()[0]
FLOW_COLS = _t[0]
# The first column numbers the steps for the reader; the PDF numbers them itself.
FLOW_STEPS = [(who, what, [p.strip() for p in parts.split(",") if p.strip()], added)
              for _num, who, what, parts, added in _t[1]]

# ---------------------------------------------------------------- side by side
_s = section("side")
SIDE_TITLE = _s.title
(SIDE_COLS, _r1), (SIDE_COLS2, _r2) = _s.tables()
SIDE_ROWS = [tuple(r) for r in _r1]
SIDE_ROWS2 = [tuple(r) for r in _r2]
SIDE_NOTE = _s.paras()[0]

# ---------------------------------------------------------------- apart + other
_s = section("apart")
APART_TITLE = _s.title
APART_ROWS = rows(_s.tables()[0])

_s = section("other")
OTHER_TITLE = _s.title
OTHER_INTRO = _s.paras()[0]
OTHER_ROWS = rows(_s.tables()[0])

# ---------------------------------------------------------------- end page
_s = section("sources")
END_TITLE = _s.title
END_INTRO = _s.paras()[0]
END_SOURCES = rows(_s.tables()[0])
