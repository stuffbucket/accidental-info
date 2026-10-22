# Hosting Thanksgiving: format leakage

A cold read of `drafts/hosting-thanksgiving/guide.md`, version 0.3.0, and the built PDF, by
a reader who has never seen an Accidental Guide. Every page was rendered and read (seven
page images). The PDF text was compared with `guide.md` to find text that only the
builders print.

Line numbers are `guide.md` lines. "PDF p. N" marks text only the build prints. Each finding
counts once, even when it covers several lines. "Low" marks a finding a reader would likely
get past.

First pass: `lint_guide.py` was not run. This review was limited to the guide, the page
images, the PDF text and the review references. No classifier pass.

Kinds: SN self-narration, UV unnamed voices, PV presenter voice, BF borrowed framing, TR
trivia, JG jargon, TT terms-table commentary, MP mannered prose.

## Status of the last scan

No earlier scan was supplied.

## Findings

The body has no "this guide", no unnamed voices, no hooks and no history. Most of the
leakage is in the labels the builder prints on every entry, and in a few lines that read
like slogans.

| Line | Text | Kind | Rewrite |
|---|---|---|---|
| PDF pp. 4–6 | "Field marks", "Identify by", "Confused with", "So what" (printed on every entry) | BF | Bird-guide labels, plus a presenter's "so what". A cold reader doesn't know what a field mark is, and "Identify by" makes no sense for thawing or helpers. In `build_guide.py`, allow per-guide labels and use "In short" for "Field marks", "Look for" for "Identify by", "Why it matters" for "So what" and "Not the same as" for "Confused with". |
| 142–144 | "Confused with: Cooks" / "Cooks make food. Helpers can also set the table, wash up or watch the clock." | BF | A contrast written to fill the slot. No one confuses helpers with cooks. Line 142: "## Confused with: Potluck". Line 144: "At a potluck, guests choose what to bring. Helpers get the dish or job you choose." |
| 17 | "Most of the dinner forgives a late start or ten extra minutes." | MP | "A late start or ten extra minutes won’t spoil most other dishes." |
| 18 | "The turkey is the one dish with firm numbers: how big, how long to thaw, how long to roast and how hot inside." | MP | Colon reveal with a four-part list. "The turkey has firm numbers for its size, thawing time, roasting time and inside temperature." |
| 99–100 | "Plan around the turkey" / "Two dishes, one oven" | MP | Slogan and drama fragment. Line 99: "Turkey first, then other dishes". Line 100: "Two oven dishes at once" |
| 113 | "so the thermometer decides when the turkey is done" | MP | Personification. "Roasting times are estimates, so go by the thermometer. Check deep in the thigh, the wing and the thickest part of the breast." |
| 25 | "Thermometer / A food thermometer, which tells you when the turkey is safe." | TT | Defines the term with itself. "A probe that reads the temperature deep inside the turkey." |
| 104–105 | "A roasting timetable gives the turkey’s hours by weight at 325 °F." | JG | Names a table the reader never sees. Give the hours instead (check sources): "At 325 °F, a turkey of 8 to 12 pounds takes 2¾ to 3 hours, and 12 to 14 pounds 3 to 3¾. An oven plan fits other dishes around those hours." |
| 84 | "A fresh turkey has never been chilled below 26 °F" | JG | A labelling threshold the reader can’t use (Low). "A fresh turkey has never been frozen, so it needs no thawing. Buy it only one or two days before cooking." |
| 39, 93 | "take the turkey out to rest"; "while the turkey rests" | JG | "Rest" is a cook’s word with no length given (Low). Line 39: "Thursday, from 3 p.m. / Check the thermometer. At 165 °F, take the turkey out to rest until 4 p.m. Bake the stuffing, then the rolls." |
| 4, PDF p. 1 and p. 7 | "A pocket-sized guide to getting Thanksgiving dinner on the table, for 26 November 2026." | SN | Describes the document, not the topic (Low; may be the series subtitle pattern, so the author decides). "Getting Thanksgiving dinner on the table on 26 November 2026." |
| PDF p. 7 | "Written and reviewed by a person. AI does the grunt work. Set in TeX Gyre Heros. Leave a star: accidental.info/star" | SN | Colophon about how the document was made, printed by the builder (Low). In the builder’s colophon, delete "Set in TeX Gyre Heros." and leave the rest to the series. |

## Counts

| Kind | Count |
|---|---|
| SN | 2 |
| UV | 0 |
| PV | 0 |
| BF | 2 |
| TR | 0 |
| JG | 3 |
| TT | 1 |
| MP | 4 |
| Total | 12 |

The body rewrites here match the reader panel’s rewrites for the same lines, so the two
reports give one edit per line. Together they save words (see the reader panel’s word
budget).
