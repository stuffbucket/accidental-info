# Source for Plugins, Connectors, and Marketplaces

This folder contains everything needed to build An Accidental Guide to… Plugins, Connectors,
and Marketplaces as a PDF, exactly, and as a Word document. It was copied from
`lights-off-software-factories/` and adds one diagram type, the map. The builds don't read
any font or file from outside this folder, apart from the Python packages pinned in
`../../requirements.txt`.

The text is in `guide.md`. Edit it to change the guide; see "The Markdown" below.

## Rebuild

`pnpm build` in `packages/accidental-guides` builds this guide and the others into
`dist/`. To build this one by hand, with the packages from `../../requirements.txt`
installed:

```sh
python3 build_guide.py                                        # the PDF
python3 build_docx.py plugins-and-marketplaces.pdf       # the .docx, from that PDF
```

The script writes `plugins-and-marketplaces.pdf` to the current directory. You can
also pass an output path: `python3 build_guide.py /path/to/out.pdf`. When it finishes, the
script prints the page count, any page where content runs past the bottom margin, the
file's SHA-256, and whether that hash matches `expected.sha256`.

With the versions in `../../requirements.txt`, the rebuilt file is byte-identical to the shipped
PDF. The script uses ReportLab's invariant mode, which fixes the creation date
(31 Dec 1999) and document ID so they don't change between runs. With other versions of
ReportLab, the pages usually look the same, but the bytes, and so the hash, may differ.

`expected.sha256` holds the PDF's hash, and is how a change to the layout or the
build is checked against it. When you change the text on purpose, update
`expected.sha256` with the new hash.

`build_docx.py` writes the Word document. It uses the PDF's page size, margins and
pages, and embeds the PDF's fonts. Its visual rules come from `build_guide.py`: the part
colours, which words are set in mono, and which part of a row is the bold short
answer. The diagram is drawn only by `build_guide.py`; the Word document places
an image of it rendered from the built PDF. Like the PDF, the `.docx` is deterministic:
the same text gives the same bytes.

## What's here

| File | What it's for |
|---|---|
| `guide.md` | Every word in the guide: titles, entries, tables, sources and footers. Edit this to change the text. |
| `content.py` | Reads `guide.md` into the names both builders use, such as `WHY_ROWS`, `MAP_LINES`, `MAP_STATIONS`, `ENTRIES`, `TABLE_PAGES` and `END_SOURCES`, and `BLURB`, the paragraph the site shows. |
| `build_guide.py` | The PDF: page layout, colors, tiles, the map and the margin check. |
| `build_docx.py` | The Word document: layout in Word's terms, the map as an image from the PDF, and the embedded fonts. |
| `fonts/texgyreheros-{regular,bold,italic}.otf` | TeX Gyre Heros 2.004, the body typeface, as originally distributed (OpenType with CFF outlines). |
| `fonts/heros-{regular,bold,italic}.ttf` | The same three fonts converted to TrueType outlines. ReportLab can only embed TrueType, so these are the files the PDF actually uses. |
| `fonts/LiberationMono-Regular.ttf` | Liberation Mono 1.07.4, used for file names, paths and commands. |
| `fonts/licenses/` | License and readme files for both typefaces. |
| `expected.sha256` | SHA-256 of the published PDF, for checking a rebuild. Update it when the text changes. |

## The Markdown

`guide.md` starts with front matter (title, kicker, subtitle, running footer, edition,
cover footer). After that, each `#` heading starts one part of the guide and ends with
an id that says which part it is: `{#why}`, `{#map}`, five `{#entry}` sections,
`{#who}` and `{#sources}`. Each entry is one line on the map, and is
`# Name {#entry num=01 mono=Tl}`. The order of sections in the file doesn't set the
order of pages; the builders do.

Within a section:

- Paragraphs are separated by blank lines, and a paragraph can be wrapped over several
  lines.
- `##` headings are the subheads. In an entry, the first `##` heading names the table of names
  on that line (columns: name, what it is) and `## Confused with: Tools`
  names the entry it's confused with, followed by a paragraph.
- Tables are pipe tables. Where the PDF prints a column header row, such as the tables on
  the levels and shown pages, the table's header row is what's printed. Tables the PDF
  prints without a header still need one in Markdown; those header rows (`Question`,
  `Field`, `Term`, `Source`) are only labels for whoever edits the file.
- The product page `{#who}` has one or more intro paragraphs, one table with a column per
  product, and exactly one closing paragraph after the table.
- The sources table has three columns: the source, its date, and its address (no
  `https://`), which is set in mono.
- Each entry's name gets its tile wherever it labels a row. Any other name is plain text with
  no tile.
- The map page `{#map}` has one paragraph, a fenced block with the map's data, and one
  paragraph under the map. The block has three kinds of line:

  ```
  line Tl | Adds tools | MCP server, Extension
  station MCP server | 0 2 | r | Claude Code, Codex
  also MCP server | Connector | Claude apps
  ```

  `line` is the entry's key, the line's name, and its stations in order. `station` is a
  name, its place on the grid (column and row, counted from the top left; halves are fine),
  which side its label goes on (`r`, `l`, `a` above or `b` below), and a grey caption.
  `also` gives another name for the same thing and where that name is used. A station on
  two lines, or with an `also`, is drawn as an interchange. The grid's width is the text
  block; each row is 34 pt. The line is drawn along the grid first, then at 45 degrees into
  the next station, so place stations to get the bends you want. `build_docx.py` finds the
  map on the page through `map_layout()`, so the two can't drift apart. The overflow check
  doesn't see labels that collide or run over a line: look at the page.

Write the text plainly: no backticks or emphasis. The builders set file names, paths
and commands in mono, and bold each row's short answer, by rule.

## About the converted fonts

If the `heros-*.ttf` files are missing, `build_guide.py` regenerates them from the `.otf`
files with fontTools, which is not in `../../requirements.txt` and has to be installed
for that. fontTools writes the current time into each converted font, and
that timestamp ends up in the PDF, so a PDF built from regenerated fonts will look the
same but won't match `expected.sha256`. Keep the shipped `.ttf` files if you need an
exact match.

## Licenses

TeX Gyre Heros is distributed under the GUST Font License (`fonts/licenses/GUST-FONT-LICENSE.txt`).
Liberation Mono 1.07.4 is distributed under the Liberation Fonts license, which is GPL v2
with a font exception (`fonts/licenses/fonts-liberation-debian-copyright.txt`). Both allow
the fonts to be redistributed with this source and embedded in the PDF and the Word document.
