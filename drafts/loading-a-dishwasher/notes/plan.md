# Plan: An Accidental Guide to… Loading a Dishwasher

Slug `loading-a-dishwasher`. Builder copied from `guides/specs-and-reviews/` with
`new_guide.py` (grey blocks, callouts, packed entries). Target about 1,000 to 1,100 printed
words, 7 pages. Facts only from `sources.md`.

## The reader

Someone who shares a kitchen with a person who loads the dishwasher differently, and who has
been told, more than once, that they're doing it wrong. They want to know what actually gets
dishes clean, from the people who make the machines and the detergent, so the argument can be
settled or at least held on better ground. No other guide is needed.

## The question

Is there a right way to load a dishwasher?

## The answer, in order

1. Mostly yes: the makers agree on more than households do. Water sprays up from arms under
   each rack, so anything facing the spray gets clean and anything blocking it doesn't.
2. Scrape, don't rinse: detergents are made to work on food soil, and pre-rinsing wastes
   water (as sourced).
3. Where things go: the rack map.
4. Each part: bottom rack, top rack, cutlery basket, spray arm, detergent.
5. The usual arguments, answered from the sources, including where the makers disagree
   (cutlery up or down), with "follow your own manual" as the tie-breaker.

## Key concepts

Five. Each has an entry and a filled tile. Colours use the registry's six families by kind of
thing, matched by analogy.

| No. | Part | Key | Family | Colour | Meaning (draft) |
|---|---|---|---|---|---|
| 01 | Bottom rack | Bo | Dm decisions people make | pink | Where plates, pots and large items go |
| 02 | Top rack | Tc | Dm decisions people make | pink | Where cups, glasses, small bowls and plastics go |
| 03 | Cutlery basket | Cb | Dm decisions people make | pink | Where knives, forks and spoons stand |
| 04 | Spray arm | Ar | Ru things that run | yellow | The turning arm that sprays water up into a rack |
| 05 | Detergent | Dg | Us things it uses | red-orange | What goes in the dispenser and does the cleaning |

The three places you choose where things go share the "decisions" colour. `Tr` and `Tp` are
taken in the registry. Top rack was `Ta` until version 0.5.1; the parallel draft
`ordering-wine` uses `Ta`, so Top rack moved to `Tc`.

Plain words, no tile: filter, rinse aid, third rack, dispenser, cycle.

Checked with `list_concepts.py` and `registry.md` on 22 October 2026: none of Bo, Tc, Cb, Ar,
Dg is used by another guide or reserved in the registry.

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover, five tiles | 40 |
| 2 | `{#why}` Is there a right way to load a dishwasher? | Two short paragraphs, terms on a grey block | 170 |
| 3 | `{#fit}` Where does everything go? | The rack map (drawn in code, labels in `FIT_*`), one paragraph, one tip callout | 150 |
| 4–6 | `{#entry}` × 5, packed | Identify by, What, So what; field marks Job, Watch for, Cannot; Confused with | 5 × 110 |
| 6 | `{#apart}` The usual arguments | Question / Answer grey block, four or five rows, closing sentence | 140 |
| 7 | `{#sources}` Sources | About 8 sources | 100 |
| | | Total | about 1,100 |

## The rack map

A front view of the tub with the door folded down. Top rack: cups and glasses upside down,
leaning in. Upper spray arm under it. Bottom rack: a pan face down at the side, plates facing
the middle, the cutlery basket at the side. Lower spray arm under it. Door: the detergent
dispenser. Each part's tile, name and a two-line grey caption at the left. Captions:
"cups, glasses and small bowls, / open side down, not touching"; "nothing hanging down, / so
they spin freely"; "plates face the middle, / pots and pans face down"; "mix the pieces, /
knives point down"; "in the dispenser, with / its lid free to open". Each caption must be
supported by `sources.md`; change the `FIT_*` strings if it isn't.

## Entries

Field mark labels, the same on every entry: Job, Watch for, Cannot.

| Entry | Identify by | Confused with |
|---|---|---|
| Bottom rack | The lower, bigger rack | Top rack |
| Top rack | The upper rack, often height-adjustable | Third rack |
| Cutlery basket | The basket in the bottom rack or on the door | Third rack |
| Spray arm | The arm under each rack | Filter |
| Detergent | Pods, tablets, powder or gel in the door dispenser | Rinse aid |

## Cross-references

None. Household guide.

## Builder changes

- `content.py`: voice comment; `fit`, `seq` and `apart` optional (shared patch).
- `build_guide.py`: `PART_FAMILY`, `NAME2MONO`; `fit_diagram()` draws the rack map and
  `page_fit()` prints it, then the blocks; `wide_widths()` for three-column tables.
- `build_docx.py`: `fit_box()` crops the rack map from the PDF by running `fit_diagram()`.
- `README.md`: the Markdown section.

## Writer

Round 1 and later edit rounds by gpt-5.6-sol-fast through `run_writer.sh` (see
`writer-round1.md` and `EDITS-*.md`).

## Open questions

- Cutlery up or down: makers differ. The guide says what each says and to follow your manual.

## Rounds (22 October 2026)

The writer CLI worked: every round was applied by gpt-5.6-sol-fast through `run_writer.sh`
(with `COPILOT=~/.local/bin/copilot`), editing `guide.md` in place. One one-word cut ("loading"
in the closing line of the arguments page) and the `Ta` to `Tc` tile change were made by hand.

| Round | Brief | What it did | Version |
|---|---|---|---|
| 1 | `writer-round1.md` | First draft from the placeholder shape | 0.1.0 |
| 2 | `EDITS-2.md` | Opening line, Confused with pairs, hot-tap argument, fewer sources | 0.2.0 |
| 3 | `EDITS-3.md` | Cuts toward 1,100 words | 0.3.0 |
| 4 | `EDITS-4.md` | Entries short enough to pack two to a page | 0.4.0 |
| 5 | `EDITS-5.md` | Fixes from `review-fidelity.md` (most makers on knives, hedges, silverware basket, GE page) | 0.5.0 |
| – | by hand | Top rack tile `Ta` to `Tc` (clash with ordering-wine) | 0.5.1 |

Result: 7 pages, 1,100 printed words (5.0 minutes), 8 sources, lint clean, no overflow.
