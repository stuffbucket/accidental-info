# Page kinds and the word budget

A guide is 4.5 × 7.5 inches, about 8 to 10 pages. One section of `guide.md` is one page, or
one block on a packed page. Nothing flows from one page to the next: if a section doesn't
fit, cut words.

## The pages

| Page | Section id | What it holds | Words |
|---|---|---|---|
| Cover | front matter | Kicker, title on two or three lines, subtitle, one tile per key concept with its page | about 50 |
| What is X? | `why` | Two or three short paragraphs that answer the question, then a Term / Meaning table with one row per key concept | 150 to 180 |
| How do the parts fit together? | `fit` | The overview diagram, drawn in code, then one short paragraph | about 120, labels included |
| One entry per key concept | `entry` (one per key) | Identify by, What, So what; two or three field marks; Confused with | about 90 to 130 each |
| A table page | an id the builder reads, such as `shown` | One intro sentence, a two- or three-column table, one closing sentence | about 150 |
| Sequence diagram (optional) | `seq` | A fenced `diagram` block that follows one piece of work through the parts | about 100 |
| Easy to mix up (optional) | `apart` | Pairs that get confused, each as a question and a one- or two-sentence answer | about 80 |
| Sources | `sources` | One sentence on when the facts were checked, then Source / Date / Address | about 90 |

With four or five entries that comes to about 1,100 words.

## Entries

Every entry in a guide has the same rows in the same order, so a reader can compare them.

- **Identify by:** where the reader meets it: a file name, a setting, a screen.
- **What:** the definition in the first sentence, genus and difference ("A harness is the
  program that runs the model in a loop."), then what it does. The first sentence prints
  in bold and has to read on its own.
- **So what:** why the difference matters to the reader.
- **Field marks:** two or three rows, the same labels on every entry, such as Owned by,
  Started by, Runs on, Can, Cannot. Each row is a short answer (no full stop; the builder
  adds it and sets it in bold) and one sentence of detail.
- **Confused with:** the one thing it's most often mistaken for, and two flat sentences that
  tell them apart.

## Visuals

- A diagram or a table wherever it says more than a paragraph would.
- The overview diagram shows the guide's own parts as tiles and the few things they connect
  to as plain text. Its labels live in `build_guide.py`.
- A sequence diagram follows one real piece of work, step by step. Solid arrows are requests,
  dashed arrows are results.
- Colour marks which part is which, and nothing else. No icons, photos or decoration.

## Layout elements (newer builders)

Builders copied from `guides/specs-and-reviews/` also have:

| Element | Markdown | Use it for |
|---|---|---|
| Grey block | lines that start with `> ` | The one table or passage on a page to read first. One per page. |
| Callout | a `> ` block whose first line is `> [!TIP]`, `> [!NOTE]` or `> [!WARNING]` | One practical tip or warning the reader can act on. At most one per page, never a definition. |
| Packed pages | none; the builder does it | Entries and back matter go down the page one after another, so two short entries share a page. |

Check the README in the guide folder you copy: it says which of these its builder supports.

## Colour

Each guide's `build_guide.py` maps each key's two-letter tile key to one of six colours in
`PART_TOKEN`. Most guides use the series rule written above `PART_TOKEN`: the entry number
sets the colour (01 blue, 02 green, 03 purple, 04 yellow, 05 pink, 06 red-orange). The
catalog guide uses colour families instead (things that run, things you write down, things
that check, things an agent uses, decisions people make, numbers and claims). Use the rule
in the builder you copy, and don't reuse a two-letter key that means something else in
another guide (`list_concepts.py` shows the clashes).
