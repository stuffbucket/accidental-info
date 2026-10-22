# Plan: An Accidental Guide to… Is My Houseplant Dying?

Slug `is-my-houseplant-dying`. Builder copied from `guides/specs-and-reviews/` with
`new_guide.py` (grey blocks, callouts, packed entries). Target about 1,000 to 1,100 printed
words, 6 or 7 pages. Facts only from `sources.md`.

## The reader

Someone with one houseplant that looks unwell: drooping, yellowing or dropping leaves. Maybe a
gift, maybe one they've had for years. They have no gardening background and their first
instinct is to water it. No other guide is needed.

## The question

Is my houseplant dying?

## The answer, in order

1. Probably not yet. Most houseplant trouble comes from light and water, and both can be
   fixed.
2. A drooping plant can be thirsty or drowning. The signs overlap, so check the soil first.
3. Thirsty or drowning: the sign-by-sign table.
4. The parts that decide it: light, watering, the pot (drainage), the roots.
5. Is it actually dead? Checks on stems and roots, and what to do if part of it is alive.

## Key concepts

Four. Each has an entry and a filled tile. Colours use the registry's six families by kind of
thing, matched by analogy.

| No. | Part | Key | Family | Colour | Meaning (draft) |
|---|---|---|---|---|---|
| 01 | Light | Lt | Us things it uses | red-orange | What the plant uses to make its food |
| 02 | Watering | Wa | Dm decisions people make | pink | When and how much you water |
| 03 | Pot | Pt | Us things it uses | red-orange | The container, and whether water can drain out |
| 04 | Roots | Rt | Ck things that check | green | Where you check whether the plant is healthy, drowning or dead |

Plain words, no tile: soil, leaves, stems, saucer, decorative pot (cachepot), root rot,
thirsty, drowning.

Checked with `list_concepts.py` and `registry.md` on 22 October 2026: none of Lt, Wa, Pt, Rt
is used by another guide or reserved in the registry.

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover, four tiles | 40 |
| 2 | `{#why}` Is my houseplant dying? | Two short paragraphs, terms on a grey block | 160 |
| 3 | `{#fit}` Thirsty or drowning? | One paragraph; a three-column grey table Sign / Thirsty / Drowning; one tip | 170 |
| 4–5 | `{#entry}` × 4, packed | Identify by, What, So what; field marks Check by, Healthy, Trouble; Confused with | 4 × 115 |
| 6 | `{#apart}` Is it actually dead? | Intro sentence, three-column grey table Check / Still alive / Dead, closing sentence | 130 |
| 7 | `{#sources}` Sources | About 8 sources | 100 |
| | | Total | about 1,050 |

No drawn diagram: the thirsty-or-drowning table is the picture.

## Entries

Field mark labels, the same on every entry: Check by, Healthy, Trouble.

| Entry | Identify by | Confused with |
|---|---|---|
| Light | Which window, and how far from it | Heat |
| Watering | How often you water and how wet the soil stays | Misting |
| Pot | Holes in the bottom, a saucer or a decorative outer pot | Decorative pot |
| Roots | What you see when you slide the plant out of its pot | Soil |

## Cross-references

None. Household guide.

## Builder changes

- `content.py`: voice comment; `fit`, `seq` and `apart` optional (shared patch).
- `build_guide.py`: `PART_FAMILY`, `NAME2MONO`; `page_fit()` prints the title and blocks;
  `wide_widths()` for three-column tables.
- `build_docx.py`: the same table rule; `page_fit()` without a diagram.
- `README.md`: the Markdown section.

## Writer

Round 1 and later edit rounds by gpt-5.6-sol-fast through `run_writer.sh` (see
`writer-round1.md` and `EDITS-*.md`).

## Open questions

- Watering frequency depends on the plant, the light and the season. The guide gives the
  check (feel the soil) rather than a schedule.

## Rounds (22 October 2026)

The writer CLI worked: every round was applied by gpt-5.6-sol-fast through `run_writer.sh`
(with `COPILOT=~/.local/bin/copilot`), editing `guide.md` in place.

| Round | Brief | What it did | Version |
|---|---|---|---|
| 1 | `writer-round1.md` | First draft from the placeholder shape | 0.1.0 |
| 2 | `EDITS-2.md` | Shorter entries, new table rows, "Is it dead yet?" title, lint fixes | 0.2.0 |
| 3 | `EDITS-3.md` | Short answers that don't wrap, so entries pack two to a page | 0.3.0 |
| 4 | `EDITS-4.md` | Fixes from `review-fidelity.md` (hedges, sour smell is the soil's, good and bad signs, Missouri source) | 0.4.0 |

Then by hand: the serial comma came out of the subtitle (0.4.1).

Result: 7 pages, 1,005 printed words (4.6 minutes), 10 sources, lint clean, no overflow.
The `{#apart}` title became "Is it dead yet?" because the lint bans "actually".
