# Source for Claude Code

This folder contains everything needed to build An Accidental Guide to… Claude Code as a
PDF, exactly, and as a Word document. It was copied from `lights-off-software-factories/`.
The builds don't read any font or file from outside this folder, apart from the Python packages pinned in `../../requirements.txt`.

The text is in `guide.md`. Edit it to change the guide; see "The Markdown" below.

## Rebuild

`pnpm build` in `packages/accidental-guides` builds this guide and the others into
`dist/`. To build this one by hand, with the packages from `../../requirements.txt`
installed:

```sh
python3 build_guide.py                                        # the PDF
python3 build_docx.py claude-code.pdf       # the .docx, from that PDF
```

The script writes `claude-code.pdf` to the current directory. You can
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
answer. This guide has no diagram pages. Like the PDF, the `.docx` is deterministic:
the same text gives the same bytes.

## What's here

| File | What it's for |
|---|---|
| `guide.md` | Every word in the guide: titles, entries, tables, sources and footers. Edit this to change the text. |
| `content.py` | Reads `guide.md` into the names both builders use, such as `WHY_BLOCKS`, `ENTRIES`, `WHERE_GROUPS`, `TABLE_PAGES` and `END_SOURCES`, and `BLURB`, the paragraph the site shows. |
| `build_guide.py` | The PDF: page layout, colors, tiles and the margin check. |
| `build_docx.py` | The Word document: layout in Word's terms and the embedded fonts. |
| `fonts/texgyreheros-{regular,bold,italic}.otf` | TeX Gyre Heros 2.004, the body typeface, as originally distributed (OpenType with CFF outlines). |
| `fonts/heros-{regular,bold,italic}.ttf` | The same three fonts converted to TrueType outlines. ReportLab can only embed TrueType, so these are the files the PDF actually uses. |
| `fonts/LiberationMono-Regular.ttf` | Liberation Mono 1.07.4, used for file names, paths and commands. |
| `fonts/licenses/` | License and readme files for both typefaces. |
| `expected.sha256` | SHA-256 of the published PDF, for checking a rebuild. Update it when the text changes. |

## The Markdown

`guide.md` starts with front matter (title, kicker, subtitle, running footer, edition,
cover footer, version). After that, each `#` heading starts one page and ends with an id
that says which page it is: `{#why}`, five `{#entry}` sections, `{#where}`, `{#scopes}`,
`{#elsewhere}` and `{#sources}`. Each entry is `# Name {#entry num=01 mono=In}`. The order
of sections in the file doesn't set the order of pages; the builders do.

The entries, then `{#where}`, `{#scopes}` and `{#elsewhere}`, go down the page one after
another, and a new page starts only when the next one doesn't fit, so two short entries share
a page. The cover and the Word document take the page numbers from the same packing (`PAGES`
in `build_guide.py`).

Within a section:

- Paragraphs are separated by blank lines, and a paragraph can be wrapped over several
  lines.
- `##` headings are the subheads. In an entry, `## Field marks` comes before its table and
  `## Confused with: Agent` names the part it's confused with, followed by a paragraph.
- Tables are pipe tables. Where the PDF prints a column header row, such as the tables on
  the scopes and elsewhere pages, the table's header row is what's printed. Tables the PDF
  prints without a header still need one in Markdown; those header rows (`Question`,
  `Field`, `Term`, `Source`) are only labels for whoever edits the file.
- The where section has one or more paragraphs, then one table per scope, then any closing
  paragraphs or a callout. Each table's first header cell is the scope's label, which is
  printed; the second header cell is only a label for editors.
- The scopes and elsewhere sections each have one or more intro paragraphs, one table, and
  any closing paragraphs or a callout after the table.
- A block of lines that start with `> ` is a grey block: its paragraphs and tables are printed
  on a light grey background, with no rules. The terms table on the first page is one.
- A `> ` block whose first line is `> [!TIP]`, `> [!NOTE]` or `> [!WARNING]` is a callout:
  one paragraph in an outlined box, led by "Tip.", "Note." or "Watch out." in bold. Use at most
  one on a page, for one practical tip or warning.
- In an entry, a field marks table in a grey block is printed as a grid of three columns, each
  label over its short answer. Its Detail column can be left out.
- A two-column table is printed as rows, label on the left, with a heavy rule over the first
  row and no rules between rows.
- The sources table has three columns: the source, its date, and its address (no
  `https://`), which is set in mono.
- Names in `NAME2MONO` in `build_guide.py` get a tile wherever they label a row. The five
  things get their colour. Any other name, such as Hooks or Permission rules, is plain text
  with no tile.

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
