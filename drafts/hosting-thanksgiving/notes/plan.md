# Plan: An Accidental Guide to… Hosting Thanksgiving

Slug `hosting-thanksgiving`. Builder copied from `guides/specs-and-reviews/` with
`new_guide.py`, then changed (see "Builder changes"). Target about 1,100 printed words,
about 8 pages. Facts only from `sources.md`. Time-sensitive: US Thanksgiving is Thursday
26 November 2026.

## The reader

Someone who has just agreed, or been told, that Thanksgiving is at their place this year.
They have cooked dinners but never a whole turkey for a crowd. They haven't read any other
Accidental Guide and don't need to: nothing here builds on the AI guides. What worries
them: buying the wrong size bird, finding it still frozen on Thursday morning, a raw or
dry turkey, and everything needing the oven at once.

## The question

How do I get Thanksgiving dinner on the table?

## The answer, in order

1. Most of the dinner forgives mistakes. The turkey is the one dish with hard numbers:
   how big, how long to thaw, how long to roast, how hot inside.
2. Count back from dinner: buy, thaw, plan the oven, roast, check, rest.
3. Turkey size: about 1 pound per person (more for leftovers).
4. Thawing: in the fridge, a day for every 4 to 5 pounds. Start days early.
5. Oven plan: the turkey takes the oven for hours. Bake the rest ahead or while it rests.
6. Thermometer: 165 °F (74 °C) in the thigh, wing and breast. The time is a guess; the
   thermometer decides.
7. Helpers: hand out whole dishes and jobs. Keep hot food hot and put food away within
   two hours.

## Key concepts

Five, each with a page and a filled tile. Colours follow the registry's families by kind of
thing.

| No. | Part | Key | Colour | Meaning (draft) |
|---|---|---|---|---|
| 01 | Turkey size | Tu | blue (Nu, numbers and claims) | How many pounds of turkey to buy for your guests. |
| 02 | Thawing | Th | yellow (Ru, things that run) | Getting a frozen turkey ready to cook, safely, over days. |
| 03 | Oven plan | Ov | purple (Wr, things you write down) | A written schedule of what goes in the oven when. |
| 04 | Thermometer | Tm | green (Ck, things that check) | The food thermometer that tells you when the turkey is safe. |
| 05 | Helpers | Hp | pink (Dm, decisions people make) | The guests and household you give dishes and jobs to. |

Plain words, no tile: pop-up timer, stuffing, sides, leftovers, the two-hour rule, roasting
timetable.

Checked with `list_concepts.py` and `registry.md`: no key here is a key in another guide.
`Tu`, `Th`, `Ov`, `Tm` and `Hp` aren't used by any concept or family. (`Tk` is Token and
`Tp` is Transport; `Tm` is distinct from both.)

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover | 50 |
| 2 | `{#why}` What does hosting Thanksgiving take? | Two short paragraphs, then the terms in a grey block | 160 |
| 3 | `{#fit}` How does the week fit together? | One sentence, then a grey block countdown table (When / What to do), one callout | 150 |
| 4–6 | `{#entry}` × 5 | One per key, packed two to a page where they fit | 5 × 105 |
| 7 | `{#apart}` Common questions | Grey Question / Answer table: frozen, stuffing, washing, sitting out, leftovers | 140 |
| 8 | `{#sources}` Sources | Six sources, read October 2026 | 90 |
| | | Total | about 1,100 |

The countdown table is the guide's one visual: a timeline counted back from dinner on
Thursday 26 November 2026, with a worked example (16-pound turkey, dinner at 4 p.m.). A
diagram drawn in code would say the same thing with more work, so there's none.

## Entries

Field mark labels, the same on every entry, in a grey grid: Rule of thumb, Watch for. (When was dropped in EDITS-3 because it repeated the countdown.)

| Entry | Identify by | Confused with |
|---|---|---|
| Turkey size | The weight on the label | Leftovers (plan more if you want them) |
| Thawing | A frozen turkey and a date on the calendar | Fresh turkey (never frozen, buy one or two days before) |
| Oven plan | A list of dishes with times and temperatures | Roasting timetable (the turkey's hours only) |
| Thermometer | A food thermometer with a probe | Pop-up timer |
| Helpers | Guests who ask what to bring | Potluck (changed from Cooks in EDITS-4) |

## Cross-references

None. This guide stands alone; it is outside the AI series and borrows no words from it.

## Builder changes (done by hand, not by the writer)

- `content.py`: voice comment; `{#fit}`, `{#seq}` and `{#apart}` are optional, and `{#fit}`
  is a plain page of blocks.
- `build_guide.py`: `PART_FAMILY` (Tu Nu, Th Ru, Ov Wr, Tm Ck, Hp Dm), `NAME2MONO`,
  `COVER_LINES` ("Hosting", "Thanksgiving"), `MONO_RE` matches nothing (no file names in a
  cooking guide, and "°F" or "a.m." must never come out in mono), `page_fit()` draws the
  section's blocks with no diagram, `SEQ_TILE` set to `Ov` (unused).
- `build_docx.py`: `page_fit()` without the diagram image; `fit_box()` removed.

## The writer

Round 1 and the edit rounds run through `run_writer.sh` with `gpt-5.6-sol-fast` (the
Copilot CLI answered a test prompt on 22 October 2026). Briefs: `writer-round1.md`,
`EDITS-2.md` and on.

## Tone

The reader is anxious. Warm, calm and dry, with at most one light line of understatement
(the turkey is the only dish that can really go wrong). Voice rules win: short plain
sentences, no jokes that need a set-up, no exclamation marks.

## Open questions

- The FSIS and FoodSafety.gov pages were read from Internet Archive copies (September and
  October 2026) because the live sites refuse automated fetches. A person should confirm
  the live pages before publishing.
- Food Network and FSIS disagree on resting time and on pounds per person. See
  `sources.md`.
