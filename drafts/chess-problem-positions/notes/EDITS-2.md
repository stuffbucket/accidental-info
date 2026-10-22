# Edits, round 2: Getting Out of Trouble in Chess

Apply these edits in place to `drafts/chess-problem-positions/guide.md` (your working
directory's `./guide.md`). Line numbers are from the file as it is now (version 0.1.0, after
round 1). Replace each listed line or line range with the new text, keeping the table row
structure: label cells stay as they are unless the edit gives a new label. Change nothing
else. Don't touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md` and
`packages/editorial/skills/accidental-guide-write/references/voice.md` first. Every rule there
applies to any text you write or shorten.

## Why

The printed guide is 1,312 words and must come down to about 1,100, so the habits page goes
(its four habits repeat the Next time field marks) and two sources go. A cold review
(notes/review-1.md) found a wrong way out on the hanging-piece board (a pawn attacks the
knight, so defending it isn't enough), a vague reason knights fork well, captions that don't
match their boards, terms used before they're explained (notation, back rank, developing
move, absolute pin) and "Break the line" where the sources say block.

## Front matter

1. Line 8: `version: 0.2.0`

## Whole cuts (delete exactly these lines)

2. Lines 166 to 178: the whole `{#habits}` section, from its heading to the blank line after
   "Look at the whole board once more, then make your move."
3. Line 185: the FIDE, Laws of Chess row.
4. Line 190: the Wikipedia, Castling row.

## {#why} (lines 11 to 29)

5. Line 11: # What are the<br/>five problems? {#why}
6. Lines 13 to 15, replace all three lines with:
   Five problems turn up often in casual games. Each has a usual way out, and a habit that
   helps you avoid it next time.
7. Lines 17 to 19, replace all three lines with:
   Moves are written in algebraic notation, explained in An Accidental Guide to: The First
   Move in Chess. In 4…Bd7, the dots mark a move by Black. An x marks a capture and + marks
   check. Each board is drawn from the side in trouble, Black for the pin and White for the
   others.
8. Line 21: Look for these five problems.
9. Line 27: > | Back-rank mate | A rook or queen mates a king shut in behind its own pawns. |
10. Line 29: > | King in the center | A king that hasn’t castled when lines toward it open. |

## Pin (lines 42 to 56)

11. Line 43: | What | A pin stops a piece moving without exposing a more valuable piece behind it. The knight on c6 is pinned to the king, so moving it is against the rules. |
12. Line 44: | So what | Block the line with 4…Bd7, putting the bishop between the knight and the king. In other positions you can also move the king, or capture or chase away the pinning piece. |
13. Line 50: > | Way out | Block the line |
14. Lines 55 to 56, replace both lines with:
   The pin on the board is absolute, because the king is behind the knight. In a relative
   pin another piece is behind, so the pinned piece may move, but the piece behind can then
   be captured.

## Fork (lines 62 to 79)

15. Line 62, change only the caption after the last `|` to:
   The knight on c2 checks the king and attacks the rook on a1.
16. Line 71: | What | A fork is one piece attacking two or more pieces at once. Knights fork well because no piece a knight attacks can capture it, except another knight. |
17. Line 72: | So what | Capture the forking piece if you can, here with Qxc2. If you can’t, answer the check and expect to lose the rook. |

## Back-rank mate (lines 89 to 110)

18. Line 89, change only the caption after the last `|` to:
   Black threatens Re1. The pawns on f2, g2 and h2 block the king, and the rook would also cover f1 and h1.
19. Line 96: | Identify by | Your king on its back rank behind its own pawns, with an enemy rook or queen able to reach that rank. |
20. Line 97: | What | A back-rank mate is checkmate by a rook or queen along the back rank, the row where the king started. The king can’t escape because its own pawns block the squares in front of it. |
21. Line 98: | So what | Make an escape square with h3, so the king can step to h2. You can also keep a rook or queen guarding the back rank. |
22. Lines 109 to 110, replace both lines with:
   Castling usually moves your king somewhere safer. The pawns that shelter a castled king
   can also trap it on the back rank.

## Hanging piece (lines 116 to 137)

23. Line 116, change only the caption after the last `|` to:
   White to move. The pawn on d6 attacks the knight on e5, and no white piece protects the knight.
24. Line 124: | What | A hanging piece is unprotected and can be captured. The knight on e5 is hanging, because nothing defends it. |
25. Line 125: | So what | Move the piece to a safe square or defend it. Here, move the knight back with 4.Nf3, because a pawn attacks it. |
26. Line 131: > | Way out | Move it or defend it |
27. Line 132: > | Next time | Check what is unprotected |
28. Lines 136 to 137, replace both lines with:
   En prise covers any piece that can be taken at a loss. That includes a piece with too few
   defenders, or one attacked by a cheaper piece.

## King in the center (lines 143 to 164)

29. Line 143: change the board label (the text between `board ` and the first `|`) to
   `After 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4+` and the caption after
   the last `|` to:
   White to move. The bishop on b4 checks the king on e1 before White has castled.
30. Line 150: | Identify by | Your king still on e1 or e8, with open lines toward it. |
31. Line 151: | What | A king in the center is a king that hasn’t castled when the lines toward it open. Here the c-pawn and d-pawn have gone, so the bishop on b4 reaches e1. |
32. Line 152: | So what | Block the check with 7.Bd2 or 7.Nc3, which also bring a piece into play, then castle. |
33. Lines 163 to 164, replace both lines with:
   You can’t castle while in check. You also can’t castle across or onto a square an enemy
   piece attacks.

## Check before you finish

- Every line not named above is unchanged.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
