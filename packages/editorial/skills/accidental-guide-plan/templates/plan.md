# Plan: An Accidental Guide to… <Title>

Slug `<slug>`. Builder copied from `guides/<model-guide>/`. Target about 1,100 printed words,
<N> pages. Facts only from `sources.md`.

## The reader

<Who they are, what they already know, which guide they have probably read, and what
confuses them about this topic. Two to four sentences.>

## The question

<One line, asked the way the reader would ask it.>

## The answer, in order

<The ideas the guide builds, one per line, in the order a newcomer needs them. Start from
what the reader already knows (turn, session) and end at the guide's own idea.>

1. <...>
2. <...>
3. <...>

## Key concepts

Five or fewer. Each has a page, a filled tile and one meaning.

| No. | Part | Key | Colour | Meaning (draft) |
|---|---|---|---|---|
| 01 | <Name> | <Xx> | <token> | <one sentence> |
| 02 | | | | |
| 03 | | | | |
| 04 | | | | |

Plain words, no tile: <things this guide mentions that are other guides' keys or aren't parts,
and the guide each one comes from>.

Checked with `list_concepts.py`: no key here is a key in another guide, and no tile key
means something else elsewhere.

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover | 50 |
| 2 | `{#why}` What is <X>? | <paragraphs, then the terms table> | 170 |
| 3 | `{#fit}` How do the parts fit together? | <the diagram: nodes, arrows, labels> | 120 |
| 4–7 | `{#entry}` × <n> | <one per key> | 4 × 120 |
| 8 | `{#<id>}` <title> | <table page> | 150 |
| 9 | `{#sources}` Sources | <n> sources, checked <Month Year> | 90 |
| | | Total | about 1,100 |

## Entries

Field mark labels, the same on every entry: <Owned by, Cannot>.

| Entry | Identify by | Confused with |
|---|---|---|
| <Name> | <where the reader meets it> | <the thing it's mistaken for> |

## Cross-references

- Builds on: An Accidental Guide to: <Title> (<which words it borrows>).
- Points to: An Accidental Guide to: <Title> (<for what>).

## Builder changes

- `guide.md`: start from the plan skill's `templates/guide.md`, with these sections.
- `content.py`: the voice comment at the top; any new section ids.
- `build_guide.py`: `PART_TOKEN`, `NAME2MONO` (plurals too), `COVER_LINES`, `MONO_RE` if the
  topic has new literals (such as `.json` or `.toml`), the `FIT_*` labels and `page_fit()`,
  page order.
- `build_docx.py`: page order, and the diagram box if the diagram moved.

## Open questions

<Anything the sources don't settle, and what the guide will say about it.>
