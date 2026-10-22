# The guide's text, read from guide.md.
#
# guide.md is the source: edit it to change the text. This file parses it (with the
# standard library only) into the names that build_guide.py and build_docx.py use, so
# the layout code doesn't change when the text does. See README.md for the format.
#
# Voice: Brian's. Plain-spoken and direct, the way a colleague explains something over
# coffee. Contractions are fine. State the point, then the reason. No taglines, slogans,
# rhetorical questions, "not X but Y", em-dash asides, rhythm triplets or stage direction
# ("this page", "below"). Rows must read on their own: no sentence starts with "it", "its",
# "they" or "this". Each term keeps one meaning. No quotes and no names of people in the
# body; public sources go on the sources page only. No text about the guide itself: no
# "this guide", page numbers or descriptions of the layout.
#
# The reader has An Accidental Guide to: Agents, Harnesses, Skills, and Tools, which defines
# agent, harness, skill, tool, MCP server, session and context window. Those words keep that
# guide's meanings and are never redefined here. This guide sorts the names for things you
# add to a coding agent or AI app into five kinds, one line each on the map: tools,
# instructions, hooks, packages and marketplaces. Product facts are as of October 2026.

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
# The table is optional: without one the page is paragraphs only.
_t = (_s.tables() or [(("", ""), [])])[0]
WHY_HEAD = tuple(_t[0])
WHY_ROWS = [tuple(r) for r in _t[1]]
# The summary the site shows for this guide. Not printed in the PDF.
BLURB = WHY_INTRO[0]

# ---------------------------------------------------------------- the map
# {#map}: a title, one paragraph, the map's data in a fenced block, and one note under it.
#   line Key | Name | Station, Station, ...     a line, in the colour of the entry with that key
#   station Name | col row | side [| caption]    where a station sits on the grid, which side of
#                                               it its name goes on, and an optional grey note
#   also Name | Other name | where              another name for the same station's thing, and
#                                               where that name is used
# A station on more than one line, or with another name, is an interchange.
_s = section("map")
MAP_TITLE = _s.title
MAP_INTRO, MAP_NOTE = _s.paras()
MAP_LINES, MAP_STATIONS, MAP_ALSO = [], {}, {}
for _line in _s.all("diagram")[0][1]:
    if not _line.strip():
        continue
    _kind, _, _rest = _line.strip().partition(" ")
    _f = [x.strip() for x in _rest.split("|")]
    if _kind == "line":
        MAP_LINES.append((_f[0], _f[1], [x.strip() for x in _f[2].split(",")]))
    elif _kind == "station":
        _col, _row = (float(v) for v in _f[1].split())
        MAP_STATIONS[_f[0]] = dict(col=_col, row=_row, side=_f[2], caption=_f[3] if len(_f) > 3 else "")
    elif _kind == "also":
        MAP_ALSO.setdefault(_f[0], []).append((_f[1], _f[2] if len(_f) > 2 else ""))
    else:
        raise SystemExit(f"{SOURCE}: unknown map line: {_line!r}")
for _key, _name, _stops in MAP_LINES:
    for _stop in _stops:
        if _stop not in MAP_STATIONS:
            raise SystemExit(f"{SOURCE}: line {_name!r} stops at {_stop!r}, which has no station line")

# ---------------------------------------------------------------- entries
ENTRIES = []
for _s in (s for s in SECTIONS if s.id == "entry"):
    _fields, _names = _s.tables()
    _f = dict(_fields[1])
    ENTRIES.append(dict(
        num=_s.attrs["num"], mono=_s.attrs["mono"], name=_s.title,
        identify=_f.get("Identify by"), what=_f["What"], sowhat=_f["So what"],
        # The names on this entry's line of the map: a subhead, then a table with a header row.
        names_head=_s.heads()[0], names_cols=tuple(_names[0]), names=rows(_names),
        confused=(_s.heads()[1].removeprefix("Confused with:").strip(), _s.paras()[0]),
    ))

# ---------------------------------------------------------------- table pages
# A plain page: a title, one or more paragraphs, a table with a header row, and one closing
# paragraph under the table. Used by {#who}.
TABLE_PAGES = {}
for _s in (s for s in SECTIONS if s.id in ("levels", "shown", "who")):
    _t = _s.tables()[0]
    TABLE_PAGES[_s.id] = dict(title=_s.title, intro=_s.paras()[:-1], cols=_t[0], rows=rows(_t),
                              note=_s.paras()[-1])

# ---------------------------------------------------------------- apart + other
# Optional: the builders print this page only when guide.md has an {#apart} section.
if any(s.id == "apart" for s in SECTIONS):
    _s = section("apart")
    APART_TITLE = _s.title
    APART_HEAD = _s.heads()[0]
    APART_ROWS = rows(_s.tables()[0])

    _s = section("other")
    OTHER_TITLE = _s.title
    OTHER_ROWS = rows(_s.tables()[0])

# ---------------------------------------------------------------- end page
_s = section("sources")
END_TITLE = _s.title
END_INTRO = _s.paras()[0]
END_SOURCES = rows(_s.tables()[0])
