# Design direction for the Accidental Guides

Written on 22 October 2026. The survey is from every guide in
`packages/accidental-guides/dist/`, rendered at 50 dpi (`pdftoppm -r 50 -png`). The
prototype is `guides/specs-and-reviews/`. Agents, Harnesses, Skills, and Tools and Software
Factories were not changed.

## What the breaks are

The author: "There are an awful lot of breaks in the later pages." On the pages, that means
these things.

1. **A rule under every row.** Each entry page has ten rules: a heavy rule over Identify by,
   hairlines under What and So what, a heavy rule and five hairlines through the field marks,
   and a heavy rule over Confused with. The back pages do the same: "Terms that are easy to mix
   up", "Related terms", "Names at Microsoft" and Sources put every row under its own line.
   Claims page 17 has 20 sources under 20 rules. The eye stops at every line, and every row
   looks as important as the one before.
2. **One treatment for everything.** Definitions, field marks, reference rows, sources and
   closing notes are all label-and-text rows under the same rules. Nothing on a page says
   which part to read first.
3. **Many short sections.** The back matter is three to five pages, each a title, a subhead,
   a table and a note under a heavy rule. "More terms" is split again into "Easy to mix up"
   and "Related terms". Running a Software Factory has "Names at Microsoft", "Terms that are
   easy to mix up" and "Related terms" as separate blocks.
4. **Half-empty pages.** Measured from the last line of text to the bottom margin: Claims
   pages 15 and 16 are 53% and 68% empty, Running page 15 is 69% and page 17 is 44%, Harness
   Engineering pages 13 and 14 are 43% and 59%, Lights-Off page 8 is 43%, and Specs pages 9 and
   10 are about a quarter empty. A short page after a full one reads as a break too.
5. **Tables split up.** Claims runs its sources over two pages ("Sources, continued"). The
   side-by-side pages split one comparison into two tables with two header rows (Agents page
   16, Software Factories page 10, Claims page 14, Running page 15).
6. **Walls of text up front.** The terms pages run four to six paragraphs before the table.
   The Specs terms page has 303 words, the most of any page in that guide.
7. **Length.** The guides run 2,100 to 4,550 words over 11 to 18 pages, which is 10 to 20
   minutes of reading. Five minutes is about 1,100 words.

## The design language

Keep the page size, type, greys, part colours, tiles, thumb tabs and footers. Colour still
means one thing, which part this is. Add these five things, each drawn by the builder from
plain Markdown, so writers still don't mark up layout.

| Element | What it looks like | Markdown | Where to use it |
|---|---|---|---|
| Grey block | A light grey panel (`#ebebeb`) behind a table or passage. The panel reaches 7 pt into the side margins, so the text keeps its left edge. No rules inside. | Lines that start with `> ` | The one thing on a page to read first: the terms table, an entry's field marks, "Easy to mix up", a short worked example. One per page, or one per entry on a shared page. |
| Callout | An outlined box (0.8 pt ink), its text led by a bold label: "Tip.", "Watch out." or "Note." | A `> ` block whose first line is `> [!TIP]`, `> [!WARNING]` or `> [!NOTE]` (GitHub's alert syntax) | One practical tip or warning that a reader can act on. At most one per page, and never a definition. |
| Fewer rules | A heavy rule opens a group of rows. There are no hairlines between rows; the space between them does that job. | None, it's the default | Every table and list of rows. Diagrams keep their own lines. |
| Field marks at a glance | In an entry, the field marks sit on a grey block as a grid of three columns, each label over its short answer. | The field marks table inside `> `, with the Detail column left out | Every entry. Every entry keeps the same rows, so entries can still be compared. |
| Packed pages | Entries and the term sections go down the page one after another. A new page starts only when the next one doesn't fit, so two short entries share a page and "Easy to mix up" follows the last entry. | None, it's a builder rule | Entries and back matter. The cover, the overview and the sequence diagram keep their own pages. |

What the elements replace:

- The "Field marks" label and six ruled rows become one grey grid.
- A closing note under a heavy rule becomes either plain text or, if it is advice, a callout.
- "More terms" with two subheads becomes "Easy to mix up" on a grey block, after the entries.
- A paragraph of advice in the body ("When review keeps sending the same work back…")
  becomes a callout.

How long a guide is, by page:

| Page | Words |
|---|---|
| Cover | about 50 |
| What it's about, with the terms on a grey block | 150 to 180 |
| How the parts fit, with one callout | about 120 |
| Each entry | about 90, two to a page |
| Easy to mix up | about 80 |
| The sequence diagram | about 100 |
| Sources and colophon | about 90 |

That comes to about 1,100 words, as `pdftotext` counts them, on about 8 pages.

What it costs:

- An entry keeps three field marks instead of six, and only the short answer. The same three
  rows on every entry keep them comparable.
- The entry tile is 34 pt instead of 46, so two entries fit on a page. The thumb tabs still
  step down the edge by entry number, but no longer line up with one entry per page.
- "One idea per page" becomes "one idea per block". A page can hold two entries.

## Should every guide show all six colours?

No. Give each colour one meaning across the series, as in the six families in `colors.md`,
and show only the families a guide actually has parts in. On the cover, add a small strip of
the six family colours in their fixed order, with the families this guide covers filled and
named, and the others left as empty outlines.

The reason is that colour should only ever mean something. A colour with no part behind it
would be decoration, and it would suggest a part the guide doesn't have. With one meaning
everywhere, a reader who knows one guide can read the colours in the next one, and the strip
on the cover shows at a glance where this guide sits among the others. Specs and Reviews, for
example, would show three families: things you write down (Spec, Work item, Tracker),
decisions people make (Acceptance criteria) and things that check (Review).

The prototype keeps the current colours. The family change is a separate step for every guide
at once, as `colors.md` describes.

## The prototype

Specs and Reviews, `packages/accidental-guides/guides/specs-and-reviews/`:

- `content.py` reads `> ` blocks as grey blocks and `> [!TIP]` blocks as callouts.
- `build_guide.py` adds `on_grey()`, `callout()`, `blocks()` (paragraphs, two-column tables,
  grey blocks and callouts in order), `marks_grid()`, and `pack()`, which puts the entries and
  term sections on pages. `rule()` skips a rule of weight 0, and `first()` gives only the first
  row a rule.
- `build_docx.py` does the same in Word: shaded cells for a grey block, a boxed one-cell table
  for a callout, and the same pages as `pack()`.
- `README.md` in the guide folder describes the new Markdown.

The text was cut to the budget above with gpt-5.6-sol-fast in four editing passes, and the guide is now version
0.3.0.

| | Before (0.2.0) | After (0.3.0) |
|---|---|---|
| Pages | 11 | 8 |
| Words (`pdftotext … \| wc -w`) | 2,092 | 1,094 |
| Rules on an entry page | 10 | 2 per entry |
| Entry pages | 5, one entry each | 3: two entries, two entries, and Review with "Easy to mix up" |
| Back matter | "More terms" with two subheads on its own page | "Easy to mix up" on a grey block after Review; "Related terms" cut |
| Field marks per entry | 6, with detail | 3 (Owned by, Kept in, Cannot), short answers only |

The five parts and their entries are all still there. What was cut: the detail column of the
field marks and three of the six rows, "Related terms", the "Spec or plan?" row, the pointer to
the Software Factories guide on the first page, and about half the words in every paragraph.

Still to check: the Word document builds with 8 pages and the same grey blocks, callout and
packing, but it was not opened in Word here.
