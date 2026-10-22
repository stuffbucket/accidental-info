# Source for Accidental Intelligence

This folder contains everything needed to build An Accidental Guide to… Accidental
Intelligence, the catalog of the Accidental Guides, as a PDF, exactly, and as a Word
document. It was copied from `software-factories/` and keeps that guide's fonts, page size,
type and helpers. The builds don't read any font or file from outside this folder, apart
from the Python packages pinned in `../../requirements.txt`.

The text is in `guide.md`. Edit it to change the guide; see "The Markdown" below. The
catalog doesn't read the other guides: when a guide changes its title, version or parts,
change its rows here by hand.

## Rebuild

`pnpm build` in `packages/accidental-guides` builds this guide and the others into
`dist/`. To build this one by hand, with the packages from `../../requirements.txt`
installed:

```sh
python3 build_guide.py                                        # the PDF
python3 build_docx.py accidental-intelligence.pdf             # the .docx, from that PDF
```

The script writes `accidental-intelligence.pdf` to the current directory. You can also pass
an output path: `python3 build_guide.py /path/to/out.pdf`. When it finishes, the script
prints the page count, any page where content runs past the bottom margin, the file's
SHA-256, and whether that hash matches `expected.sha256`.

With the versions in `../../requirements.txt`, the rebuilt file is byte-identical to the
shipped PDF. The script uses ReportLab's invariant mode, which fixes the creation date
(31 Dec 1999) and document ID so they don't change between runs. When you change the text
on purpose, update `expected.sha256` with the new hash.

`build_docx.py` writes the Word document. It uses the PDF's page size, margins and pages,
and embeds the PDF's fonts. Its colors and mono rule come from `build_guide.py`. The two
drawings, the reading order and the map of parts, are drawn only by `build_guide.py`; the
Word document places images of them cropped from the built PDF, using `start_layout()` and
`map_layout()`.

## What's here

| File | What it's for |
|---|---|
| `guide.md` | Every word in the guide, the reading order, and the list of every part with its guide, key and family. Edit this to change the text. |
| `content.py` | Reads `guide.md` into the names both builders use, such as `WHY_ROWS`, `START_GRID`, `FAMILIES`, `PARTS` and `CARD_PAGES`, and `BLURB`, the paragraph the site shows. |
| `build_guide.py` | The PDF: page layout, the family colors, tiles, the two drawings and the margin check. |
| `build_docx.py` | The Word document: layout in Word's terms, the drawings as images from the PDF, and the embedded fonts. |
| `fonts/` | TeX Gyre Heros and Liberation Mono, copied byte for byte from `software-factories/`, with their licenses. See that folder's README for how the `.ttf` files were made. |
| `expected.sha256` | SHA-256 of the published PDF, for checking a rebuild. Update it when the text changes. |

## The pages

| Page | Section | What it shows |
|---|---|---|
| 1 | front matter | Cover, with the six family tiles |
| 2 | `{#why}` | The guides, the question each answers, and each version |
| 3 | `{#start}` | The reading order, drawn, and who each guide is for |
| 4 | `{#colours}` | The six color families and the parts in each |
| 5 | `{#map}` | Every guide's parts as tiles, in family colors |
| 6–7 | `{#cards}` × 2 | One card per guide: its parts and what to read next |
| 8 | `{#end}` | Versions, and the colophon |

## The Markdown

`guide.md` starts with front matter (title, kicker, subtitle, running footer, edition,
cover footer, version). After that, each `#` heading ends with an id.

- `{#why}`: paragraphs, then a table of Guide, Answers, Version. The Guide column is each
  guide's short title, and every other section names guides exactly as written here. A
  version containing "draft" marks the guide as a draft: a dashed box in the reading order,
  "draft" on the map and the card.
- `{#start}`: one paragraph (the note under the drawing), a fenced `diagram` block, and a
  table of Guide and who it's for. In the block, `row A | B | C` puts guides in the three
  columns of one row, with an empty cell for an empty column, and `next A -> B` draws an
  arrow from A to B. Arrows between rows go down, across and down; an arrow within a row
  goes across.
- `{#colours}`: paragraphs, a table of Key, Family and What it holds, and a closing
  paragraph printed as the note. The key is the family tile's two letters. Each key's color
  is in `FAMILY_TOKEN` in `build_guide.py`.
- `{#map}`: two paragraphs (the intro and the note), then one table row per part: Guide,
  Part, Key, Family. A part's tile takes its family's color. A key used in two guides must
  have the same family in both, or the build stops.
- `{#cards}`: each one is a page. A `## Guide` subhead, then a Field and Text table, for
  each guide on that page. The Parts row comes from the map, and the version from `{#why}`.
  Every guide in `{#why}` must have exactly one card.
- `{#end}`: paragraphs above the colophon.

Write the text plainly: no backticks or emphasis. Name a guide by its short title in a table
or a card, and as "An Accidental Guide to: Software Factories" in a paragraph.

## Licenses

TeX Gyre Heros is distributed under the GUST Font License (`fonts/licenses/GUST-FONT-LICENSE.txt`).
Liberation Mono 1.07.4 is distributed under the Liberation Fonts license, which is GPL v2
with a font exception (`fonts/licenses/fonts-liberation-debian-copyright.txt`). Both allow
the fonts to be redistributed with this source and embedded in the PDF and the Word document.
