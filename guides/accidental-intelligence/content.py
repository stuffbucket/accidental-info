# The guide's text, read from guide.md.
#
# guide.md is the source: edit it to change the text. This file parses it (with the
# standard library only) into the names that build_guide.py and build_docx.py use, so
# the layout code doesn't change when the text does. See README.md for the format.
#
# Voice: see packages/editorial/skills/accidental-guide-write/references/voice.md. Plain-spoken and
# direct. Sentences run as long as the thought needs, without going staccato.
# Contractions are fine. State the point, then the reason. No taglines, slogans, rhetorical
# questions, embedded questions, vague stand-ins such as "around", "not X but Y", em-dash asides,
# rhythm triplets or stage direction ("this page", "below"). Rows must read on their own: no
# sentence starts with "it", "its", "they" or "this". Each field row leads with a short bold
# answer. Each term keeps one meaning. Do not name-check public or private sources in the body.
# No text about the guide itself: no "this guide", page numbers or descriptions of the layout.
#
# The catalog of the series. It has no parts of its own: its tiles are the six color families,
# and the parts it shows belong to the other guides, with those guides' names and keys. In
# tables and on the cards a guide is named by its short title ("Software Factories"); in a
# paragraph, by its title in colon form ("An Accidental Guide to: Software Factories"). Keep
# the versions and the map in step with the other guides' guide.md files.

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

# ---------------------------------------------------------------- the guides
_s = section("why")
WHY_TITLE = _s.title
WHY_INTRO = _s.paras()
_t = _s.tables()[0]
WHY_COLS = _t[0]
WHY_ROWS = rows(_t)
# The summary the site shows for this guide. Not printed in the PDF.
BLURB = WHY_INTRO[0]
GUIDES = [r[0] for r in WHY_ROWS]
DRAFTS = {r[0] for r in WHY_ROWS if "draft" in r[2]}

# ---------------------------------------------------------------- where to start
_s = section("start")
START_TITLE = _s.title
START_NOTE = _s.paras()[0]
_t = _s.tables()[0]
START_COLS = _t[0]
START_ROWS = rows(_t)
# The diagram block: "row A | B | C" puts guides in the columns of one row (an empty cell
# leaves the column empty), and "next A -> B" draws an arrow from guide A to guide B.
START_GRID, START_NEXT = [], []
for _line in _s.all("diagram")[0][1]:
    _kind, _, _rest = _line.partition(" ")
    if _kind == "row":
        START_GRID.append([x.strip() for x in _rest.split("|")])
    elif _kind == "next":
        _a, _, _b = _rest.partition(" -> ")
        START_NEXT.append((_a.strip(), _b.strip()))
for _a, _b in START_NEXT:
    assert _a in GUIDES and _b in GUIDES, (_a, _b)
for _r in START_ROWS:
    assert _r[0] in GUIDES, _r

# ---------------------------------------------------------------- the color families
_s = section("colours")
COL_TITLE = _s.title
COL_INTRO = _s.paras()[:-1]
COL_NOTE = _s.paras()[-1]
FAMILIES = [dict(key=k, name=n, holds=h) for k, n, h in rows(_s.tables()[0])]

# ---------------------------------------------------------------- the map
_s = section("map")
MAP_TITLE = _s.title
MAP_INTRO, MAP_NOTE = _s.paras()
# One row per part: the guide it belongs to, its name, its two-letter key and its family's key.
PARTS = [dict(guide=g, name=n, key=k, family=f) for g, n, k, f in rows(_s.tables()[0])]
for _p in PARTS:
    assert _p["guide"] in GUIDES, _p
    assert _p["family"] in {f["key"] for f in FAMILIES}, _p

# ---------------------------------------------------------------- the guide cards
# Each {#cards} section is one page: a title, then for each guide a "## Guide" subhead and a
# Field | Text table.
CARD_PAGES = []
for _s in (s for s in SECTIONS if s.id == "cards"):
    _cards, _name = [], None
    for _b in _s.blocks:
        if _b[0] == "h2":
            _name = _b[1]
        elif _b[0] == "table":
            assert _name in GUIDES, _name
            _cards.append(dict(name=_name, rows=[tuple(r) for r in _b[2]]))
    CARD_PAGES.append(dict(title=_s.title, cards=_cards))
assert sorted(c["name"] for p in CARD_PAGES for c in p["cards"]) == sorted(GUIDES)

# ---------------------------------------------------------------- end page
_s = section("end")
END_TITLE = _s.title
END_INTRO = _s.paras()
