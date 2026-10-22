# Plan: An Accidental Guide to… Smoke Detectors That Chirp

Slug `chirping-smoke-detector`. Builder copied from `guides/specs-and-reviews/` with
`new_guide.py` (grey blocks, callouts, packed entries). Target about 1,000 to 1,100 printed
words, 7 pages. Facts only from `sources.md`.

## The reader

Someone at home, often at night, with a high single chirp coming from somewhere in the house
every half minute or so. They don't know which alarm it is, whether it's an emergency, or how
to make it stop without breaking anything. They have read no other Accidental Guide, and none
is needed: this is the first household guide, so it builds on nothing in the series and borrows
no series words.

## The question

Which smoke alarm is chirping, and how do I make it stop?

## The answer, in order

1. A single short chirp every 30 to 60 seconds is the alarm asking for attention, not a fire.
   A loud repeating pattern is the alarm sound: get out.
2. The usual cause is a low battery. The other common one is the alarm reaching its end of
   life, about 10 years after it was made.
3. Chirps often start in the small hours because batteries give less power when the house
   cools at night.
4. Finding it: wait for a chirp, look for the alarm whose light is blinking differently,
   narrow it down room by room. Interconnected alarms all sound for smoke, but only the one
   with the problem chirps.
5. The fix: a new battery (or a new alarm, if it's past its date or has a sealed battery),
   then press test. The hush button buys time; it doesn't fix anything.
6. Never take an alarm down and leave it down.

## Key concepts

Five. Each has an entry and a filled tile. Colours use the registry's six families by kind of
thing (these are household things, so the families are matched by analogy).

| No. | Part | Key | Family | Colour | Meaning (draft) |
|---|---|---|---|---|---|
| 01 | Chirp | Cr | Ck things that check | green | The short single beep an alarm gives when its own check finds a problem |
| 02 | Indicator light | Ld | Ck things that check | green | The small light on the alarm whose blinking shows which alarm and what's wrong |
| 03 | Battery | Ba | Us things it uses | red-orange | What powers the alarm, or backs up a hardwired one |
| 04 | Hush button | Hu | Dm decisions people make | pink | The button you press to quiet the alarm for a short time |
| 05 | Manufacture date | Md | Nu numbers | blue | The date on the back that tells you when to replace the whole alarm |

Plain words, no tile: smoke alarm (the device), interconnected alarms, hardwired, breaker,
alarm sound, test button.

Checked with `list_concepts.py` and `registry.md` on 22 October 2026: none of Cr, Ld, Ba, Hu,
Md is used by another guide or reserved in the registry.

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover, five tiles | 40 |
| 2 | `{#why}` Why is my smoke alarm chirping? | Two short paragraphs, then the terms on a grey block | 170 |
| 3 | `{#fit}` Which one is it? | One paragraph, a grey Step / What to do block of four steps, one warning callout | 160 |
| 4–6 | `{#entry}` × 5, packed two to a page | Identify by, What, So what; field marks Found on, Fixed by, Cannot; Confused with | 5 × 110 |
| 6 | `{#apart}` What does the sound mean? | Three-column grey table Sound / Means / Do this; one closing sentence | 110 |
| 7 | `{#sources}` Sources | About 8 sources | 100 |
| | | Total | about 1,100 |

No drawn diagram: the step table and the sound table say more than a picture would.

## Entries

Field mark labels, the same on every entry: Found on, Fixed by, Cannot.

| Entry | Identify by | Confused with |
|---|---|---|
| Chirp | One short high beep, about every 30 to 60 seconds | Alarm sound |
| Indicator light | A small light on the cover, often red or green | Power light |
| Battery | 9-volt or AA behind a door or under the cover | Sealed battery |
| Hush button | Often the same button as test | Test button |
| Manufacture date | Printed on the back | Battery |

## Cross-references

None. This is a household guide; it builds on no other guide in the series.

## Builder changes

- `content.py`: voice comment; `fit`, `seq` and `apart` optional (shared patch).
- `build_guide.py`: `PART_FAMILY` and `NAME2MONO` for the five parts; `page_fit()` prints the
  title and blocks (no drawn diagram); tables of three or more columns in a section print with
  their header (`wide_widths()`); no sequence page.
- `build_docx.py`: the same table rule; `page_fit()` without a diagram.
- `README.md`: the Markdown section.

## Writer

Round 1 and later edit rounds by gpt-5.6-sol-fast through `run_writer.sh` (see
`writer-round1.md` and `EDITS-*.md`).

## Open questions

- Chirp intervals and end-of-life patterns vary by maker and model. The guide gives the range
  the sources give and says to check the alarm's label or manual.

## Rounds (22 October 2026)

The writer CLI worked: every round was applied by gpt-5.6-sol-fast through `run_writer.sh`
(with `COPILOT=~/.local/bin/copilot`), editing `guide.md` in place.

| Round | Brief | What it did | Version |
|---|---|---|---|
| 1 | `writer-round1.md` | First draft from the placeholder shape | 0.1.0 |
| 2 | `EDITS-2.md` | Tone, night-time claim, standby blink, reset, hush | 0.2.0 |
| 3 | `EDITS-3.md` | Cut to about 60 words of row text per entry | 0.3.0 |
| 4 | `EDITS-4.md` | Small cuts to reach 1,100 words | 0.4.0 |
| 5 | `EDITS-5.md` | Battery entry one line shorter so entries pack two to a page | 0.5.0 |
| 6 | `EDITS-6.md` | Fixes from `review-fidelity.md` (CO action, breaker first, hedges, LED, Silence) | 0.6.0 |

Result: 7 pages, 1,100 printed words (5.0 minutes), 8 sources, lint clean, no overflow.
Deviations from the page plan: the sound table carries the reset steps; the
"smoke detector" naming sentence was cut for length.
