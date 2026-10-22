# Ordering Wine for the Table: format leakage

A cold read of `drafts/ordering-wine/guide.md`, version 0.2.0, and the built PDF, by a reader
who has never seen an Accidental Guide. All seven pages were rendered and read. The PDF text
was compared with `guide.md` to find text that only the builders print.

Line numbers are `guide.md` lines. “PDF p. N” marks text only the build prints. Each finding
counts once, even when it covers several lines. “Low” marks a finding a reader would likely
get past.

First pass: `lint_guide.py` was not run, because this review was limited to the listed files.
No classifier pass was run. Every finding below comes from reading.

The fixed series labels (Identify by, What, So what, Field marks, Confused with) and the “A
pocket-sized guide to…” subtitle are left out on purpose.

Kinds: SN self-narration, UV unnamed voices, PV presenter voice, BF borrowed framing, TR
trivia, JG jargon, TT terms-table commentary, MP mannered prose.

## Status of the last scan

No earlier scan was provided.

## Findings

| Line | Text | Kind | Rewrite |
|---|---|---|---|
| 17 to 18 | “Five terms cover most of the job. Once you know what they mean, you can order without pretending to know more than you do.” | SN | Delete. The sentence counts the guide’s own table and sets it up with a reassurance. Line 14 already says the reader needn’t know every name. |
| 25 | “Price \| The price band you set before reading any names.” | TT | “\| Price \| What the restaurant charges for a bottle or glass. \|” The row gives an instruction instead of a meaning, and line 110 defines Price differently. |
| 39, 142 | “Nod when the wine is sound” and “whether the wine is sound” | JG | Line 39: “Nod when the wine isn’t faulty, and the server will pour it.” Line 142: “The taste is for faults.” |
| 130 | “Corked wine smells musty, like wet cardboard.” | JG | “One fault, corked wine, smells musty, like wet cardboard.” A new reader takes “corked” to mean the bottle has a cork. |
| 98, 103 | “A drying feel is tannin” and “which comes from tannin, not sugar” | JG (low) | Line 98: “A drying feel in the mouth”. Lines 102 to 103: “A dry wine isn’t sweet. A wine can also feel drying in your mouth, which has nothing to do with sugar.” |
| 71 | “A few names cover a lot.” | MP | “Ask for light or full.” A slogan that leads the So what row without telling the reader what to do. |
| 130, 131, 142 | “the small pour that checks the wine isn’t faulty”, “The taste checks the bottle, not your choice.”, “The taste tells you whether the wine is sound.” | MP | Line 130: “A taste is a small pour used to check for faults.” Line 131: delete the first sentence. Line 142: “The taste is for faults.” The pour is personified three times, and line 131 is a “not X” flourish. |
| 62 | “Wines by the glass are sold one glass at a time.” | MP (low) | Delete. Line 63: “Wines by the glass suit a table whose dishes need different wines.” The sentence restates its own name. |
| PDF p. 7 | “Written and reviewed by a person. AI does the grunt work. Set in TeX Gyre Heros. Leave a star: accidental.info/star” | SN (low) | In `build_guide.py`, keep only “Set in TeX Gyre Heros.” in the colophon, or keep the colophon as it is if it is a series-wide decision. The other lines describe how the guide was made and ask for a star, which has nothing to do with ordering wine. |

Read and kept:

- Line 156, “These public sources were checked in October 2026.” This mentions the sources,
  but it is the as-of date that the sources page needs.
- Line 122, “has a reputation as the worst deal.” This is close to an unnamed voice. The
  belief is the subject of the study that follows, so the phrase stays.
- Builder text on PDF pages 1 to 7: the tile page numbers, “Version 0.2.0” on the cover, the
  “Tip.” label, and the full stops added to the Field marks answers. None is self-narration.
- No borrowed framing beyond the exempt labels. No trivia. Neither the study’s authors nor
  the working-paper number appear in the body.

## Counts

| Kind | Count |
|---|---|
| SN | 2 |
| UV | 0 |
| PV | 0 |
| BF | 0 |
| TR | 0 |
| JG | 3 |
| TT | 1 |
| MP | 3 |
| Total | 9 |
