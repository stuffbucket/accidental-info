# Source for Claude Desktop

This folder contains everything needed to build An Accidental Guide to… Claude Desktop as a
PDF, exactly, and as a Word document. It was copied from
`lights-off-software-factories/`. The builds don't read any font or file from outside this folder, apart
from the Python packages pinned in `../../requirements.txt`.

The text is in `guide.md`. Edit it to change the guide; see "The Markdown" below.

## Rebuild

`pnpm build` in `packages/accidental-guides` builds this guide and the others into
`dist/`. To build this one by hand, with the packages from `../../requirements.txt`
installed:

```sh
python3 build_guide.py                                        # the PDF
python3 build_docx.py claude-desktop.pdf       # the .docx, from that PDF
```

The script writes `claude-desktop.pdf` to the current directory. You can
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
| `content.py` | Reads `guide.md` into the names both builders use, such as `WHY_ROWS`, `ENTRIES`, `TABLE_PAGES` and `END_SOURCES`, and `BLURB`, the paragraph the site shows. |
| `build_guide.py` | The PDF: page layout, colors, tiles and the margin check. |
| `build_docx.py` | The Word document: layout in Word's terms and the embedded fonts. |
| `fonts/texgyreheros-{regular,bold,italic}.otf` | TeX Gyre Heros 2.004, the body typeface, as originally distributed (OpenType with CFF outlines). |
| `fonts/heros-{regular,bold,italic}.ttf` | The same three fonts converted to TrueType outlines. ReportLab can only embed TrueType, so these are the files the PDF actually uses. |
| `fonts/LiberationMono-Regular.ttf` | Liberation Mono 1.07.4, used for file names, paths and commands. |
| `fonts/licenses/` | License and readme files for both typefaces. |
| `expected.sha256` | SHA-256 of the published PDF, for checking a rebuild. Update it when the text changes. |

## The Markdown

`guide.md` starts with front matter (title, kicker, subtitle, running footer, edition,
cover footer, version). After that, each `#` heading starts one part of the guide and ends
with an id that says which part it is: `{#why}`, five `{#entry}` sections, `{#where}`,
`{#account}`, `{#elsewhere}` and `{#sources}`. Each of the five entries is
`# Name {#entry num=01 mono=In}`. The order of sections in the file doesn't set the order of
pages; the builders do.

Within a section:

- Paragraphs are separated by blank lines, and a paragraph can be wrapped over several
  lines.
- `##` headings are the subheads. In an entry, `## Field marks` comes before its table and
  `## Confused with: Agent` names the part it's confused with, followed by a paragraph.
- Tables are pipe tables. Where the PDF prints a column header row, such as the tables on
  the where, account and elsewhere pages, the table's header row is what's printed. Tables the PDF
  prints without a header still need one in Markdown; those header rows (`Question`,
  `Field`, `Term`, `Source`) are only labels for whoever edits the file.
- The where, account and elsewhere pages each have intro paragraphs, one table, and
  exactly one closing paragraph after the table. A table cell may use `<br/>` for a line
  break, which both builders honour.
- The sources table has two columns: the source and its address (no `https://`), set in
  mono. An address with no slash is a Help Center article number and goes on the source's
  line; the date checked and the shared Help Center address are in the intro.
- Names in `NAME2MONO` in `build_guide.py` get a tile wherever they label a row. The five
  concepts get their colour. Any other name is plain text with no tile.
- Menu paths are written with " > " between steps (Settings > General). Paths on macOS and
  Windows, the registry key and the preference domain are set in mono by `MONO_RE`.

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
