# Source for Ordering Wine for the Table

This folder contains everything needed to build An Accidental Guide to… Ordering Wine for the Table as a PDF,
exactly, and as a Word document. It was copied from `drafts/hosting-thanksgiving/` with `new_guide.py`, which was copied from `guides/specs-and-reviews/`. The builds don't read
any font or file from outside this folder, apart from the Python packages pinned in
`packages/pipeline/requirements.txt`.

The text is in `guide.md`. Edit it to change the guide; see "The Markdown" below.

## Rebuild

`pnpm turbo run build --filter=@accidentalguide/ordering-wine` at the repository root builds this guide
into its `dist/`, and `pnpm build` builds every guide. To build this one by hand, with the packages from `packages/pipeline/requirements.txt`
installed:

```sh
python3 build_guide.py                                        # the PDF
python3 build_docx.py ordering-wine.pdf                   # the .docx, from that PDF
```

The script writes `ordering-wine.pdf` to the current directory. You can
also pass an output path: `python3 build_guide.py /path/to/out.pdf`. When it finishes, the
script prints the page count, any page where content runs past the bottom margin, the
file's SHA-256, and whether that hash matches `expected.sha256`.

With the versions in `packages/pipeline/requirements.txt`, the rebuilt file is byte-identical to the shipped
PDF. The script uses ReportLab's invariant mode, which fixes the creation date
(31 Dec 1999) and document ID so they don't change between runs. With other versions of
ReportLab, the pages usually look the same, but the bytes, and so the hash, may differ.

`expected.sha256` holds the PDF's hash, and is how a change to the layout or the
build is checked against it. When you change the text on purpose, update
`expected.sha256` with the new hash.

`build_docx.py` writes the Word document. It uses the PDF's page size, margins and
pages, and embeds the PDF's fonts. Its visual rules come from `build_guide.py`: the part
colours, which words are set in mono, and which part of a row is the bold short
answer. The guide has no diagrams: its overview page is a table. Like the PDF, the `.docx` is deterministic:
the same text gives the same bytes.

## What's here

| File | What it's for |
|---|---|
| `guide.md` | Every word in the guide: titles, entries, tables, sources and footers. Edit this to change the text. |
| `content.py` | Reads `guide.md` into the names both builders use, such as `WHY_BLOCKS`, `FIT_BLOCKS`, `ENTRIES`, `APART_BLOCKS` and `END_SOURCES`, and `BLURB`, the paragraph the site shows. |
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
with an id that says which part it is: `{#why}`, `{#fit}`, five `{#entry}` sections,
`{#apart}` and `{#sources}`. The builders also read `{#seq}` (a sequence diagram) and `{#other}` if
they're present. Each of the five entries is
`# Name {#entry num=01 mono=Wn}`. The order of sections in the file doesn't set the order
of pages; the builders do.

The entries, then `{#apart}` and `{#other}`, go down the page one after another, and a new
page starts only when the next one doesn't fit, so two short entries share a page. The cover
and the Word document take the page numbers from the same packing (`PAGES` in
`build_guide.py`).

Within a section:

- Paragraphs are separated by blank lines, and a paragraph can be wrapped over several
  lines.
- `##` headings are the subheads. In an entry, `## Field marks` comes before its table and
  `## Confused with: Wines by the glass` names the thing it's confused with, followed by a paragraph.
- Tables are pipe tables. The header rows (`Term`, `Question`, `Field`, `Source`) are only
  labels for whoever edits the file. A two-column table is printed as rows, label on the left,
  with a heavy rule over the first row and no rules between rows.
- A block of lines that start with `> ` is a grey block: its paragraphs and tables are printed
  on a light grey background, with no rules. Use it for the one table or passage on a page that
  the reader should look at first.
- A `> ` block whose first line is `> [!TIP]`, `> [!NOTE]` or `> [!WARNING]` is a callout:
  one paragraph in an outlined box, led by "Tip.", "Note." or "Watch out." in bold. Use at most
  one on a page, for one practical tip or warning.
- In an entry, a field marks table in a grey block is printed as a grid of three columns, each
  label over its short answer. Its Detail column can be left out.
- The sources table has three columns: the source, its date, and its address. An address
  with a space in it names a site that isn't on the web and is set in the body face; any
  other address is a web address and is set in mono.
- An optional sequence diagram (`{#seq}`) is a fenced `diagram` block, written as in
  `guides/specs-and-reviews/README.md`. This guide doesn't use one.
- Names in `NAME2MONO` in `build_guide.py` get a tile wherever they label a row. The five
  parts get their colour. Any other name is plain text with no tile.
- The overview page (`{#fit}`) is drawn block by block like the terms page: paragraphs, one
  grey block and a callout. Nothing on it is drawn in code.
- Nothing is set in mono: `MONO_RE` in `build_guide.py` matches nothing, because a cooking,
  wine or speaking guide has no file names or commands, and "°F" or "a.m." must stay in
  the body face.

Write the text plainly: no backticks or emphasis. The builders bold each row's short
answer by rule.

## About the converted fonts

If the `heros-*.ttf` files are missing, `build_guide.py` regenerates them from the `.otf`
files with fontTools, which is not in `packages/pipeline/requirements.txt` and has to be installed
for that. fontTools writes the current time into each converted font, and
that timestamp ends up in the PDF, so a PDF built from regenerated fonts will look the
same but won't match `expected.sha256`. Keep the shipped `.ttf` files if you need an
exact match.

## Licenses

TeX Gyre Heros is distributed under the GUST Font License (`fonts/licenses/GUST-FONT-LICENSE.txt`).
Liberation Mono 1.07.4 is distributed under the Liberation Fonts license, which is GPL v2
with a font exception (`fonts/licenses/fonts-liberation-debian-copyright.txt`). Both allow
the fonts to be redistributed with this source and embedded in the PDF and the Word document.
