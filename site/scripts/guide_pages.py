"""Turn each guide's guide.md into a Starlight page, and stage the guides' files for the site.

Run from anywhere after the guides are built (`pnpm build` does both), with the repo's
virtualenv:

    .venv/bin/python site/scripts/guide_pages.py

It reads each built guide's dist/guide.json under guides/ (finished) and drafts/ (still being
written), and its guide.md (parsed with that guide's own content.py, so the site reads the text
the same way the PDF does). It writes:

    site/public/guides.json                    every guide's guide.json, with its status
    site/public/guides/<id>.pdf, <id>.docx     copies of the built files
    site/public/guides/<id>/cover.png          the PDF's first page
    site/public/guides/<id>/diagram-<n>.png    the diagram on PDF page n, cropped to the figure
    site/src/content/docs/guides/<id>.md       a finished guide as a Starlight doc page
    site/src/content/docs/drafts/<id>.md       a draft, the same way, marked as a draft

Each run deletes those outputs first, so the result depends only on the inputs.

Diagrams can't be written in Markdown, so each fenced ```diagram block, and the overview
diagram that build_guide.py draws on the "fit" page, becomes an image cropped from the PDF
page it's drawn on. The page is found by its title in the PDF's text and checked against the
diagram's own labels; the crop leaves out the page's title, paragraphs, tables and footer,
which the site prints as text. Other fenced blocks (```skill) are written as code blocks.
'> ' blocks are written as ordinary text, and '> [!TIP]' style callouts as Starlight asides.
"""
import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GUIDES = ROOT / "guides"
DRAFTS = ROOT / "drafts"
PUBLIC = ROOT / "site" / "public"
CONTENT = ROOT / "site" / "src" / "content" / "docs"
DOCS = CONTENT / "guides"
DRAFT_DOCS = CONTENT / "drafts"
BASE = "/accidentalguide"
SCALE = 2

ORDER = ["accidental-intelligence", "agents-harnesses-skills-tools", "specs-and-reviews",
         "software-factories", "lights-off-software-factories"]
XREF = "An Accidental Guide to: "
# Callout labels from content.py's ALERTS (> [!TIP], > [!NOTE], > [!WARNING]) -> Starlight asides.
# Fenced blocks other than ```diagram are printed as text; this names their code language.
CODE_LANGS = {"skill": "md"}
ASIDES = {"Tip": "tip", "Note": "note", "Watch out": "caution", "Warning": "caution"}


# ---------------------------------------------------------------- loading
def load_content(guide_id, folder=None):
    """Import the guide's content.py and return the module (it parses guide.md on import)."""
    path = (folder or GUIDES / guide_id) / "content.py"
    spec = importlib.util.spec_from_file_location(f"guide_pages_{guide_id.replace('-', '_')}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sidebar_order(guides):
    """Map each guide id to its sidebar position: the fixed order first, then the rest A-Z."""
    ids = [g["id"] for g in guides]
    ordered = [i for i in ORDER if i in ids] + sorted(i for i in ids if i not in ORDER)
    return {gid: n for n, gid in enumerate(ordered, 1)}


# ---------------------------------------------------------------- text
def heading_text(title):
    """A guide.md heading as plain text: '<br/>' becomes a space."""
    return re.sub(r"\s+", " ", re.sub(r"<br\s*/?>", " ", title)).strip()


def escape(text):
    """Escape the few characters Markdown would read as markup. The guides' text uses none
    of them today; this keeps a stray one from breaking the page."""
    return re.sub(r"([\\`*<>\[\]])", r"\\\1", text)


def link_xrefs(text, published, self_id=None):
    """Turn 'An Accidental Guide to: <Title>' into a link when that guide is published.
    `published` maps title -> id. The words stay the same."""
    titles = sorted((t for t, i in published.items() if i != self_id), key=len, reverse=True)
    if not titles:
        return text
    pattern = re.compile(re.escape(XREF) + "(" + "|".join(map(re.escape, titles)) + r")(?![\w-])")
    return pattern.sub(lambda m: f"[{m.group(0)}]({BASE}/guides/{published[m.group(1)]}/)", text)


def inline(text, published, self_id):
    return link_xrefs(escape(text), published, self_id)


def is_web_address(address):
    return bool(address) and " " not in address and "." in address


def address_link(address):
    if not is_web_address(address):
        return escape(address)
    url = address if re.match(r"https?://", address) else "https://" + address
    return f"[{escape(address)}]({url})"


def table(header, rows, cell):
    """A GitHub-flavored Markdown table. `cell(col, text)` renders one body cell."""
    def line(cells):
        return "| " + " | ".join(c if c else " " for c in cells) + " |"
    out = [line([escape(h) for h in header]), "|" + "---|" * len(header)]
    for r in rows:
        r = list(r) + [""] * (len(header) - len(r))
        out.append(line([cell(i, c) for i, c in enumerate(r)]))
    return "\n".join(out)


# ---------------------------------------------------------------- page conversion
def section_heading(section):
    title = heading_text(section.title)
    if section.id == "entry" and section.attrs.get("num"):
        return f"## {section.attrs['num']} {title}"
    return f"## {title}"


def image(section, guide_id, page):
    return f"![{heading_text(section.title)}]({BASE}/guides/{guide_id}/diagram-{page}.png)"


def fence_langs(text):
    """The info string of each fenced block in guide.md, in order ('diagram', 'skill', ...).
    content.py keeps every fenced block as ("diagram", lines) without it."""
    langs, inside = [], False
    for line in text.splitlines():
        if line.startswith("```"):
            if not inside:
                langs.append(line[3:].strip())
            inside = not inside
    return langs


def render_body(sections, guide_id, published, diagram_pages, fit_page=None, fences=None):
    """The guide's sections as Markdown.

    Fenced blocks are numbered (section index, index within the section). diagram_pages maps
    a ```diagram block to the PDF page it's drawn on. fences maps any other fenced block to its
    info string; it's written out as a code block. fit_page, if given, is the page of the
    overview diagram drawn on the {#fit} page."""
    fences = fences or {}
    out = []
    for si, s in enumerate(sections):
        out.append(section_heading(s))
        diagrams = iter(range(len(s.blocks)))

        def emit(block):
            kind = block[0]
            if kind == "p":
                out.append(inline(block[1], published, guide_id))
            elif kind == "h2":
                out.append("### " + inline(heading_text(block[1]), published, guide_id))
            elif kind == "table":
                header, rows = block[1], block[2]
                if s.id == "sources" and header and header[-1].strip().lower() == "address":
                    last = len(header) - 1
                    cell = lambda i, c, last=last: address_link(c) if i == last else inline(c, published, guide_id)
                else:
                    cell = lambda i, c: inline(c, published, guide_id)
                out.append(table(header, rows, cell))
            elif kind == "diagram":
                key = (si, next(diagrams))
                if key in fences:
                    lang = CODE_LANGS.get(fences[key], fences[key] or "text")
                    out.append(f"```{lang}\n" + "\n".join(block[1]) + "\n```")
                else:
                    out.append(image(s, guide_id, diagram_pages[key]))
            elif kind == "grey":
                # A '>' block: the PDF sets it on grey. On the site it's ordinary text.
                for inner in block[1]:
                    emit(inner)
            elif kind == "callout":
                out.append(f":::{ASIDES.get(block[1], 'note')}\n{inline(block[2], published, guide_id)}\n:::")
            else:
                raise SystemExit(f"{guide_id}: section {heading_text(s.title)!r} has a {kind!r} block "
                                 "that guide_pages.py doesn't know how to write")

        for block in s.blocks:
            emit(block)
        if s.id == "fit" and fit_page:
            out.append(image(s, guide_id, fit_page))
    return "\n\n".join(out) + "\n"


def yaml_str(text):
    return json.dumps(text, ensure_ascii=False)


def render_page(guide, sections, order, published, diagram_pages, fit_page=None, fences=None):
    gid = guide["id"]
    head = [
        "---",
        f"title: {yaml_str(guide['title'])}",
        f"description: {yaml_str(guide['subtitle'])}",
        "sidebar:",
        f"  order: {order}",
        "---",
        "",
        "",
    ]
    links = [f"[PDF]({BASE}/guides/{guide['pdf']})"]
    if guide.get("docx"):
        links.append(f"[Word]({BASE}/guides/{guide['docx']})")
    draft = "Draft · " if guide.get("status") == "draft" else ""
    top = [f"{draft}Version {guide['version']} · {guide['pages']} pages · " + " · ".join(links)]
    # The blurb is the guide's first paragraph. Print it on its own only when the text
    # doesn't already open with it.
    blocks = [x for b in sections[0].blocks for x in (b[1] if b[0] == "grey" else [b])] if sections else []
    first = next((b[1] for b in blocks if b[0] == "p"), None)
    if guide.get("blurb") and guide["blurb"] != first:
        top.append(inline(guide["blurb"], published, gid))
    body = render_body(sections, gid, published, diagram_pages, fit_page, fences)
    return "\n".join(head) + "\n\n".join(top) + "\n\n" + body


# ---------------------------------------------------------------- PDF pages
def normalize(text):
    return re.sub(r"\s+", " ", text.replace("­", "")).strip()


def page_texts(pdf):
    return [normalize(pdf[i].get_textpage().get_text_range()) for i in range(len(pdf))]


def diagram_labels(lines):
    """Words from a diagram block that the PDF prints: message labels and the names of parts,
    bands, notes and guides."""
    labels = []
    for line in lines:
        kind, _, rest = line.partition(" ")
        if kind == "msg":
            labels.append(rest.split(": ", 1)[1])
        elif kind == "part":
            labels.append(rest.split("|")[0])
        elif kind in ("band",):
            labels.append(rest)
        elif kind == "note":
            labels.append(rest.split(": ", 1)[1])
        elif kind == "row":
            labels += rest.split("|")
        elif kind == "next":
            labels += rest.split(" -> ")
    return [normalize(l) for l in labels if l.strip()]


def find_page(texts, title, labels=(), window=120):
    """The 1-based number of the one page whose heading is `title` (it appears in the first
    `window` characters of the page's text, after any tile key). Every label must be on it."""
    want = normalize(heading_text(title))
    hits = [i for i, t in enumerate(texts) if i > 0 and want in t[:window]]
    if len(hits) != 1:
        raise SystemExit(f"expected one PDF page titled {want!r}, found pages {[h + 1 for h in hits]}")
    text = texts[hits[0]]
    missing = [l for l in labels if l not in text]
    if missing:
        raise SystemExit(f"page {hits[0] + 1} titled {want!r} is missing diagram labels {missing}")
    return hits[0] + 1


def render_png(pdf, page_number, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    pdf[page_number - 1].render(scale=SCALE).to_pil().save(path, optimize=True)


def section_strings(section):
    """The text of a section that the site prints as text: its title, paragraphs, callouts,
    subheads and table rows (cells joined by spaces, as the PDF's text reads)."""
    out = [heading_text(section.title)]

    def walk(blocks):
        for b in blocks:
            if b[0] in ("p", "h2"):
                out.append(b[1])
            elif b[0] == "callout":
                out.append(b[2])
            elif b[0] == "table":
                for row in [b[1], *b[2]]:
                    out.append(" ".join(c for c in row if c))
            elif b[0] == "grey":
                walk(b[1])
    walk(section.blocks)
    return [normalize(t) for t in out if normalize(t)]


def text_rows(page, strings, height):
    """Pixel rows (at SCALE) covered by any of `strings` where they appear whole on the page."""
    tp = page.get_textpage()
    raw = tp.get_text_range()
    norm, index = [], []
    for i, ch in enumerate(raw):
        if ch.isspace() or ch == "\u00ad":
            if norm and norm[-1] != " " and ch != "\u00ad":
                norm.append(" ")
                index.append(i)
        else:
            norm.append(ch)
            index.append(i)
    norm = "".join(norm)
    rows = set()
    for text in strings:
        start = norm.find(text)
        while start != -1:
            for k in range(start, start + len(text)):
                i = index[k]
                if raw[i].isspace():
                    continue
                left, bottom, right, top = tp.get_charbox(i)
                y0 = max(0, int((height - top) * SCALE))
                y1 = min(int(height * SCALE), int((height - bottom) * SCALE) + 1)
                rows.update(range(y0, y1))
            start = norm.find(text, start + len(text))
    return rows


def content_blocks(img):
    """Runs of pixel rows that have anything drawn on them: [(top, bottom)], bottom exclusive."""
    from PIL import ImageOps
    ink = ImageOps.invert(img.convert("L")).point(lambda v: 255 if v > 12 else 0)
    profile = [ink.crop((0, y, img.width, y + 1)).getbbox() is not None for y in range(img.height)]
    blocks, top = [], None
    for y, on in enumerate(profile + [False]):
        if on and top is None:
            top = y
        elif not on and top is not None:
            blocks.append((top, y))
            top = None
    return blocks, ink


def render_diagram(pdf, page_number, section, path, margin=24):
    """Render one PDF page and crop it to the diagram: drop the section's own text (title,
    paragraphs, tables), which the site prints as text, and the page footer. The diagram is the
    tallest run of drawn rows that holds none of that text."""
    page = pdf[page_number - 1]
    _w, h = page.get_size()
    img = page.render(scale=SCALE).to_pil().convert("RGB")
    covered = text_rows(page, section_strings(section), h)
    blocks, ink = content_blocks(img)
    footer_line = img.height * 0.93
    kinds = []
    for top, bottom in blocks:
        if top >= footer_line:
            kinds.append("footer")
        elif any(y in covered for y in range(top, bottom)):
            kinds.append("text")
        else:
            kinds.append("figure")
    runs, run = [], []
    for block, kind in zip(blocks, kinds):
        if kind == "figure":
            run.append(block)
        elif run:
            runs.append(run)
            run = []
    if run:
        runs.append(run)
    if not runs:
        raise SystemExit(f"page {page_number}: no diagram found outside the text")
    run = max(runs, key=lambda r: r[-1][1] - r[0][0])
    # A thin full-width rule at either end separates the diagram from the text; leave it out.
    def is_rule(b):
        box = ink.crop((0, b[0], img.width, b[1])).getbbox()
        return b[1] - b[0] <= 6 and box and box[2] - box[0] > img.width * 0.5
    while len(run) > 1 and is_rule(run[-1]):
        run = run[:-1]
    while len(run) > 1 and is_rule(run[0]):
        run = run[1:]
    top, bottom = run[0][0], run[-1][1]
    i0, i1 = blocks.index(run[0]), blocks.index(run[-1])
    above = blocks[i0 - 1][1] if i0 > 0 else 0
    below = blocks[i1 + 1][0] if i1 + 1 < len(blocks) else img.height
    box = ink.crop((0, top, img.width, bottom)).getbbox()
    left, right = box[0], box[2]
    crop = (max(0, left - margin), max(above, top - margin, (above + top) // 2),
            min(img.width, right + margin), min(below, bottom + margin, (bottom + below + 1) // 2))
    path.parent.mkdir(parents=True, exist_ok=True)
    img.crop(crop).save(path, optimize=True)
    return crop


# ---------------------------------------------------------------- main
def built_guides():
    """Each built guide's guide.json, with the folder it came from."""
    guides = []
    for folder in sorted(f for d in (GUIDES, DRAFTS) if d.is_dir() for f in d.iterdir()):
        if not (folder / "guide.md").exists():
            continue
        built = folder / "dist" / "guide.json"
        if not built.exists():
            sys.exit(f"{built} not found: build the guides first (pnpm build)")
        guides.append((json.loads(built.read_text(encoding="utf-8")), folder))
    return guides


def clean():
    for p in (PUBLIC / "guides", DOCS, DRAFT_DOCS):
        if p.exists():
            shutil.rmtree(p)
    (PUBLIC / "guides.json").unlink(missing_ok=True)


def main():
    import pypdfium2

    found = built_guides()
    guides = [g for g, _ in found]
    # Cross references link only to finished guides.
    published = {g["title"]: g["id"] for g in guides if g.get("status") != "draft"}
    order = sidebar_order(guides)

    clean()
    (PUBLIC / "guides").mkdir(parents=True)
    DOCS.mkdir(parents=True)
    DRAFT_DOCS.mkdir(parents=True)
    (PUBLIC / "guides.json").write_text(json.dumps(guides, indent=2, ensure_ascii=False) + "\n",
                                        encoding="utf-8")

    for g, folder in found:
        gid = g["id"]
        dist = folder / "dist"
        out_dir = PUBLIC / "guides" / gid
        for name in (g["pdf"], g.get("docx")):
            if name:
                shutil.copyfile(dist / name, PUBLIC / "guides" / name)
        content = load_content(gid, folder)
        sections = content.SECTIONS
        pdf = pypdfium2.PdfDocument(str(dist / g["pdf"]))
        try:
            render_png(pdf, 1, out_dir / "cover.png")
            texts = page_texts(pdf)
            diagram_pages, fences = {}, {}
            langs = iter(fence_langs((folder / "guide.md").read_text(encoding="utf-8")))
            for si, s in enumerate(sections):
                for di, block in enumerate(b for b in s.blocks if b[0] == "diagram"):
                    lang = next(langs)
                    if lang == "diagram":
                        diagram_pages[(si, di)] = find_page(texts, s.title, diagram_labels(block[1]))
                    else:
                        fences[(si, di)] = lang
            fit_page = None
            fit = next((s for s in sections if s.id == "fit"), None)
            if fit and "def page_fit" in (folder / "build_guide.py").read_text(encoding="utf-8"):
                fit_page = find_page(texts, fit.title)
            figures = {n: sections[si] for (si, _di), n in diagram_pages.items()}
            if fit_page:
                figures[fit_page] = fit
            for n, section in sorted(figures.items()):
                render_diagram(pdf, n, section, out_dir / f"diagram-{n}.png")
        finally:
            pdf.close()
        page = render_page(g, sections, order[gid], published, diagram_pages, fit_page, fences)
        docs = DRAFT_DOCS if g.get("status") == "draft" else DOCS
        (docs / f"{gid}.md").write_text(page, encoding="utf-8")
        shown = ", ".join(str(n) for n in sorted(set(diagram_pages.values()) | ({fit_page} - {None})))
        print(f"{gid}: {len(sections)} sections, diagram pages: {shown or 'none'}")
    print(f"wrote {CONTENT.relative_to(ROOT)}/ and {(PUBLIC / 'guides').relative_to(ROOT)}/ for {len(guides)} guides")


if __name__ == "__main__":
    main()
