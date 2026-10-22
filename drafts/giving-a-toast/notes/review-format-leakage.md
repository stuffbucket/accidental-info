# Giving a Toast: format leakage

A cold read of `drafts/giving-a-toast/guide.md`, version 0.2.0, and the built 7-page PDF, by
a reader who has never seen an Accidental Guide. Every page image was read. The PDF text
(`guide.txt`) was compared with `guide.md` to find text that only the builders print.

Line numbers are `guide.md` lines. "PDF p. N" marks text only the build prints. Each finding
counts once, even when it covers several lines. "Low" marks a finding a reader would likely
get past.

First pass: `lint_guide.py` was not run, because this review was limited to the listed
files. No classifier pass. Every finding below comes from reading.

Not reported, as fixed series conventions: the labels “Identify by”, “What”, “So what”,
“Field marks” and “Confused with”, and the “A pocket-sized guide to…” subtitle. “Sam” is a
deliberate placeholder.

Kinds: SN self-narration, UV unnamed voices, PV presenter voice, BF borrowed framing, TR
trivia, JG jargon, TT terms-table commentary, MP mannered prose.

## Status of the last scan

No earlier scan was supplied.

## Findings

The guide is mostly clean. It never says “this guide”, has no unnamed voices or trivia, and
the only borrowed framing is in the fixed series labels.

| Line | Text | Kind | Rewrite |
|---|---|---|---|
| 17–18 | "The opening tells the room who you are. The story gives them one reason to celebrate, and the last line brings everyone in." | MP | "Tie what you say to the occasion. At a wedding, lean toward sentiment. For a retirement, lean toward nostalgia." |
| 42–43 | "You’ll hear where a sentence is too long before the room does." | MP | "Use only words you’d use in everyday life." |
| 29–30 | "A toast then follows six small steps, from getting the room’s attention to taking a sip." | SN, low | "Toast once drinks are served, usually at the start of the meal or just before dessert." |
| 130 | "Off-limits. The spotlight belongs on the person you’re toasting." | MP, low | "Stories that might embarrass the person are off-limits. A toast celebrates them." |
| 131 | "A toast isn’t the time to overshare." | MP, low | "Pick something simple that a mixed room can share." |
| 25 | "Length \| Two to three minutes from start to finish." | TT, low | "Length \| How long you speak, from first word to raised glass." |
| PDF p. 7 | "Written and reviewed by a person. AI does the grunt work. Set in TeX Gyre Heros. Leave a star: accidental.info/star" | SN, low | Builder colophon about how the guide was made. If it is a series convention, keep it. Otherwise cut it in `build_guide.py` or keep only the contact line. |

Notes on each:

- Lines 17 to 18 are a rhythm triplet that restates line 13 with a flourish (“brings
  everyone in”). The rewrite replaces it with sourced advice the guide lacks.
- Line 43 ends the tip on a kicker that pictures the room judging the speaker.
- Lines 29 to 30 count and preview the table below (“six small steps, from … to …”), which
  is set-up rather than content. The rewrite keeps the timing, which is what the reader
  needs.
- Line 130 opens on a one-word fragment. The spotlight reason belongs to length in the
  sources, not to embarrassment.
- Line 131 is a slogan that restates the row label instead of giving a reason.
- Line 25 is a rule, not a meaning, in a terms table whose other rows define parts. The
  rule is already on lines 14 and 117.
- Line 145, "These public sources were checked in October 2026.", talks about the sources but
  sits on the Sources page and dates them. Kept, not counted.
- PDF p. 1 and p. 7 print the tile for Last line as “Ll”, which reads as “LI” in this font.
  This is a legibility point, not leakage, and is not counted.

## Counts

| Kind | Count |
|---|---|
| SN | 2 |
| UV | 0 |
| PV | 0 |
| BF | 0 |
| TR | 0 |
| JG | 0 |
| TT | 1 |
| MP | 4 |
| Total | 7 |
