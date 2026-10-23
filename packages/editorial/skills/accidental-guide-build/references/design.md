# Design

What an Accidental Guide looks like, so you can tell from a page image whether the build is
right. The model is `guides/agents-harnesses-skills-tools/`; the newer layout elements are in
`guides/specs-and-reviews/`.

## The book

A pocket guide, 4.5 × 7.5 in, about 8 to 10 pages, one idea per page or per block. White
pages in black and grey, with colour only to mark the key concepts. No photos, icons or
illustrations: the only pictures are the part tiles and the diagrams.

## Every page

- Title top left, 17 pt bold, wrapping short of the corner tile if there is one.
- Running footer below the bottom margin: the short name on the left, the page number on the
  right, 6 pt grey. The cover and end page have a heavy rule and a date or edition line.

## Pages

| Page | What you should see |
|---|---|
| Cover | A black band 150 pt deep across the top, edge to edge: the kicker in small white bold, the collection's name in grey, the guide's number and the collection's mark on the right, and the title in white at 27 pt on two or three lines, set on the band's foot. Below it the subtitle, the six families in a row under a thin rule (filled where the guide has parts in that family), one row per key concept with its tile in its family's column and its name and page beside it, the tagline, a heavy rule and the date and version at the foot |
| Terms page | Two or three short paragraphs, then the terms as rows (on a grey block in newer builders) |
| Overview | The diagram: part tiles as nodes with a bold name and grey caption, arrows with grey labels, plain text for things that aren't parts. One short paragraph |
| Entry | Corner tile (the part's colour, its key and number), thumb tab on the right edge stepped down by entry number, the name, Identify by, What and So what with the first sentence bold, the field marks, Confused with |
| Table page | Title, an intro sentence, a table with grey column headers, a closing sentence |
| Sources | A sentence on when the facts were checked, each source as a bold name over a grey mono address, then the colophon with the tiles, title and edition |

## Rows and rules

Most content is rows: a label in a 62 pt left column and text in the rest. A heavy rule opens
a group. Older builders put a hairline under every row; newer ones use space instead, which
reads with fewer breaks.

## Type

TeX Gyre Heros (a Helvetica clone) for everything, Liberation Mono at 90% for literals. Body
7.6 pt, rows and notes 7.0, table cells 6.6. Bold for titles, labels and short answers only.
Italic only in sequence diagram notes.

## Colour

Three greys for text and rules: ink `#111111`, grey `#5f5f5f`, hairline `#bdbdbd`. Six part
colours from one swatch: blue `#0D99FF`, green `#14AE5C`, purple `#9747FF`, yellow `#FFCD29`,
pink `#E83FBF`, red-orange `#F24822`. A tile is the base colour with a darker band; text on a
tile is white, except on yellow, where it's ink. Colour means one thing: which part this is.

## The ubiquitous language

1. The terms page comes first and gives each key concept one plain meaning.
2. Each part is defined once, on its entry, in the first sentence of What.
3. Part names get a tile wherever they label something (a row, a step, a Confused with),
   by rule from `NAME2MONO`. In running prose they are plain words.
4. Literals are set in mono by rule. Concept words never are.

## Looking at the pages

Render every page (`build_one.sh` does it at 60 dpi) and look at each one. The overflow check
doesn't catch:

- text running past the right edge, usually a long mono string in a narrow column;
- diagram labels that collide or run over a line;
- a title running under the corner tile (force a break with `<br/>`);
- a part name with no tile because its spelling isn't in `NAME2MONO`;
- an ordinary word set in mono because it has a slash or a dot;
- a page that is half empty after a full one, which reads as a break;
- a cover title split badly (`COVER_LINES`).
