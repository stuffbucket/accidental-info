# Edits, round 3: The First Move in Chess

Apply these edits in place to `drafts/chess-first-move/guide.md` (your working directory's
`./guide.md`). Line numbers are from the file as it is now (version 0.2.0 plus the new board
lines and two new reference sections). Change only the lines named. Don't touch any other
file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`,
`packages/editorial/skills/accidental-guide-write/references/voice.md` and
`packages/editorial/skills/accidental-guide-write/references/banned-patterns.md` first (paths
from the repository root, `../..` from your working directory). Facts only from
`notes/sources.md` (section 4 is new and covers the openings).

## Why

The author asked for better boards: the starting position from White's side and from
Black's side, side by side, and two reference pages after the guide, one for White and one
for Black, each with six boards after four moves: three sound lines and three tempting lines
that opening theory considers poor. The boards and moves are in place. The words around them
are a first draft and need your pass. The reference pages are reference: keep their text
minimal. Each board's caption has room for exactly one line of text.

## Rules for the diagram lines

Lines inside the fenced ```diagram blocks are data. In a `board` line the fields are
separated by ` | `, and you may change only the third field (the caption). In a `line` line,
change only the third field (the idea). In a `column` line, everything after `column ` is the
label. Never change a name, a FEN, the moves, `mark` lines, `white`/`black`, or the fences.

## How do you read the board? (lines 29 to 46)

1. Line 32, caption of the White board: keep it as it is: "White moves first. The four tinted
   squares are the center."
2. Line 34, caption of the Black board. It now repeats the paragraph at lines 40 to 41.
   Replace with a caption that says what changes from Black's side: the files run from h to
   a and rank 8 is nearest. Up to 14 words. Register:
   > The same position from Black’s side. Files run h to a, and rank 8 is nearest.
3. Lines 38 to 41: the boards now show both sides, so the paragraph can say less about
   Black's view. Keep the first two sentences (files a to h, ranks 1 to 8). Replace "Black
   sees the board the other way round." with nothing or with a shorter pointer, and keep the
   light-square sentence. Don't grow the paragraph.

## Openings for White (lines 132 to 145)

4. Line 134: one sentence, up to 12 words, that says each board is the position after each
   player has made four moves. Keep it plain. The current text is close.
5. Lines 137 and 141, the column labels. Plain words, no personification if you can avoid it,
   up to 5 words each, the same pair on both pages. The first column holds sound, standard
   lines; the second holds tempting lines that the sources call weak, dubious or refuted. For
   example "Sound" and "Tempting but weak", or "Standard lines" and "Lines to avoid". Pick one
   pair and use it on both pages (lines 137, 141, 152, 156).
6. Lines 138 to 140 and 142 to 144: the idea of each line, in one short sentence of at most
   40 characters including spaces and the final full stop (it must fit on one printed line).
   Say what the moves do on the board, in words a beginner can follow, from sources.md
   section 4. No names of people, no ECO codes, no popularity claims. For the three weak lines,
   say what goes wrong for the side that plays them. The current drafts:
   - Ruy Lopez: the bishop attacks the knight that defends e5.
   - Italian Game: the bishop aims at f7, and c3 prepares d4.
   - Queen's Gambit Declined: Black keeps the pawn on d5 instead of taking on c4.
   - Wayward Queen Attack: the queen comes out early and gets chased, losing time.
   - Grob's Attack: 1.g4 loosens White's king side, and after 2...Bxg4 White has lost the pawn.
     (In this line White then wins b7, but sources call 1.g4 one of the worst first moves.)
   - Halloween Gambit: White gives a knight for one pawn.

## Openings for Black (lines 147 to 160)

7. Line 149: as edit 4, adding that the boards are drawn from Black's side. Up to 14 words.
8. Lines 153 to 155 and 157 to 159: as edit 6. The facts:
   - Sicilian: Black's c-pawn takes White's d-pawn.
   - Caro-Kann: Black's light-squared bishop comes out before e6 would block it in.
   - King's Indian: Black lets White build a pawn center, to attack it later.
   - Damiano: 2...f6 blocks the knight's square and, after 3...fxe5, the king is attacked
     (4.Qh5+ Ke7). The current "loses a pawn" is wrong: replace it.
   - Latvian: an early f-pawn move that sources call dubious; it weakens Black's king.
   - Englund: Black gives a pawn for a queen check that sets up Qxb2, a trap. Sources call the
     gambit weak.

## Sources (lines 162 to 170)

9. After line 170, add two rows, exactly:
   | Wikipedia, List of ECO codes and each opening’s article | October 2026 | en.wikipedia.org/wiki/List_of_ECO_codes |
   | Lichess, opening explorer | October 2026 | lichess.org/opening |

## Check before you finish

- Every line not named above is unchanged, and every ```diagram line keeps its fields.
- Every idea is 40 characters or fewer.
- No sentence starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
