# Grilled Cheese: format leakage

A cold read of `drafts/grilled-cheese/guide.md`, version 0.2.0, and the built PDF, by a
reader who has never seen an Accidental Guide. All seven pages were rendered and read. The
PDF text was compared with `guide.md` to find text that only the builders print.

Line numbers are `guide.md` lines. "PDF p. N" marks text only the build prints. Each finding
counts once, even when it covers several lines. "Low" marks a finding a reader would likely
get past.

First pass: `lint_guide.py` not run. The brief limited this review to the listed files. No
classifier pass.

Kinds: SN self-narration, UV unnamed voices, PV presenter voice, BF borrowed framing, TR
trivia, JG jargon, TT terms-table commentary, MP mannered prose.

Not reported, per the brief: the series labels "Identify by", "What", "So what", "Field
marks" and "Confused with".

## Status of the last scan

No earlier scan was provided.

## Findings

| Line | Text | Kind | Rewrite |
|---|---|---|---|
| 17 to 18 | "Strong opinions about each are available, but lunch only needs all four working together." | PV, low | "The job comes down to bread, cheese, butter and heat. All four have to work together." A teaser for the arguments page, with lunch doing the needing. The fun fits better on page 6. |
| 131 | "Butter gives the usual buttery result." | MP, low | "Butter soaks into the bread and tastes of butter." A circular answer that sounds like a point. |
| 27 | "How does it<br/>come together?" | MP, low | "How do you<br/>cook one?" A stock phrase, and "it" has nothing to refer to in a heading. |
| PDF p. 1, 5, 7 | "Cs" tile for Cheese (from line 65, mono=Cs) | JG, low | Change to mono=Ch if the tile list allows it. Next to "Br" and "He", "Cs" reads as the chemical symbol for caesium, not cheese. |

## Seen and not counted

- Line 4 and PDF p. 1, 7: "A pocket-sized guide to crisp bread and melted cheese." The
  subtitle calls the document a guide. Expected on a cover.
- Line 137: "These public sources were checked in October 2026." On the sources page,
  where a reader expects it.
- PDF p. 7: "Written and reviewed by a person. AI does the grunt work. Set in TeX Gyre
  Heros." and "Leave a star: accidental.info/star". A back-cover colophon about the making.
  Expected there, so not counted.
- PDF p. 3: "Tip." The builder’s label for the callout at lines 41 to 43. Reads naturally.
- PDF p. 4 to 6: the builder adds full stops to the short answers. No leakage.

The body has no "this guide", "this page", "below", "here’s", unnamed voices, trivia or
travel or bird vocabulary outside the fixed labels. The terms table at lines 20 to 25 is
plain definitions, and all four terms are used.

## Counts

| Kind | Count |
|---|---|
| SN | 0 |
| UV | 0 |
| PV | 1 |
| BF | 0 |
| TR | 0 |
| JG | 1 |
| TT | 0 |
| MP | 2 |
| Total | 4 |
