# Edits, round 2: The First Move in Chess

Apply these edits in place to `drafts/chess-first-move/guide.md` (your working directory's
`./guide.md`). Line numbers are from the file as it is now (version 0.1.0, the round-1
draft). Replace each listed line with the new text, keeping the table row structure: label
cells stay as they are unless the edit gives a new label. Change nothing else. Don't touch
any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md` and
`packages/editorial/skills/accidental-guide-write/references/voice.md` first (paths from the
repository root, `../..` from your working directory). Every rule there applies to any text
you write or shorten.

## Why

The cold reviews (notes/review-readers.md, review-fidelity.md, review-leakage.md) found no
chess errors, but square names appear before the board page explains them, x and # are never
explained, the board is described only from White's side, "lines" means two things, "Nf3 and
Nc6" doesn't say whose moves they are, and a few claims go past the sources (knights before
bishops, "strongest piece", the touch-the-rook rule, "before doing anything else"). The guide
is 1,047 printed words, so additions must be paid for with cuts. Every replacement below is
word for word: use it as given.

## Front matter

1. Line 8: `version: 0.2.0`

## What should your first move be? (lines 11 to 27)

2. Lines 13–15 (the first paragraph, three lines): replace with these three lines:
   White moves first, then the players take turns. Start with a pawn in the middle of the
   board, bring out your knights and bishops, then castle to put your king somewhere safer.
   You don’t need to memorize a string of moves.
3. Lines 17–19 (the second paragraph, three lines): replace with these three lines:
   The first few moves have two jobs: get your pieces into the game quickly and get your king
   safe. When you’re learning, a few principles help more than memorized sequences of moves,
   because they work against whatever the other player does.
4. Line 21: `Center, development and castling cover most of what you need at the start.`
5. Line 25: `> | Center | The four squares in the middle of the board. |`
6. Line 27: `> | Castling | One move of your king and a rook together. |`

## How do you read the board? (lines 29 to 42)

7. Lines 36–38 (the first paragraph, three lines): replace with these four lines:
   Each square has a letter and a number. From White’s side, the columns, called files, run
   from a to h, left to right. The rows, called ranks, run from 1 to 8, going away from White.
   Black sees the board the other way round. Set it down so each player has a light square in
   the near right corner.
8. Lines 40–42 (the second paragraph, three lines): replace with these four lines:
   Pieces use K for king, Q for queen, R for rook, B for bishop and N for knight. A pawn move
   is written as the square it lands on. Moves are numbered with White first, so 1.e4 e5 means
   White’s pawn goes to e4, then Black’s pawn goes to e5. Black’s move alone is 1…e5. An x
   means a capture, and # means checkmate.

## Center (lines 44 to 63)

9. Line 50: `| So what | A center pawn move frees your queen and a bishop to move. The center usually opens first, because center pawns often capture each other. |`
10. Line 57: `> | Aim | A pawn in the middle |`

## Development (lines 65 to 84)

11. Line 69: `| Identify by | Knights and bishops leaving their starting squares. |`
12. Line 78: `> | Aim | Knights and bishops out |`
13. Lines 83–84 (the paragraph, two lines): replace with these two lines:
   Bring your queen out after your knights and bishops. An early queen can be chased by
   knights and bishops that your opponent wanted to develop anyway.

## Castling (lines 86 to 107)

14. Line 91: `| What | Castling is one move of the king and a rook, written 0-0 on the king’s side or 0-0-0 on the queen’s side. The king moves two squares toward the rook, then the rook lands on the square the king crossed. |`
15. Lines 104–107 (the paragraph, four lines): replace with these four lines:
   An ordinary king move goes one square. To castle, neither the king nor that rook may have
   moved, and no piece can stand between them. The king can’t castle out of check, and it can’t
   cross or land on a square an enemy piece attacks. Move the king first, then the rook.

## What do you play, as White or Black? (lines 109 to 127)

16. Line 109: `# What do you play,<br/>as White or Black? {#shown}`
17. Line 111: `Pick the row for your color and the move just played.`
18. Line 115: `> | 1.e4 | As White. The e-pawn moves two squares and frees the queen and a bishop to move. |`
19. Line 116: `> | 1.d4 | As White. The same idea with the d-pawn. |`
20. Line 117: `> | 1…e5 | As Black, after 1.e4. The e-pawn moves two squares, blocks White’s e-pawn and frees the queen and a bishop to move. |`
21. Line 118: `> | 1…d5 | As Black, after 1.d4. The same idea with the d-pawn. |`
22. Line 119: `> | 2.Nf3 Nc6 | White’s knight goes to f3 and Black’s knight goes to c6. Bishops come next. Each move brings one piece into the game. |`
23. Line 120: `> | 0-0 | Castle on the king’s side once the knight and bishop between king and rook have moved. |`
24. Lines 124–125 (the last two lines of the warning): replace with these two lines:
   > The game 1.e4 e5 2.Bc4 Bc5 3.Qh5 Nf6 4.Qxf7# ends in checkmate. As Black, when White’s
   > queen and bishop both aim at f7, defend f7 on your next move. Here, 3…Qe7 does it.
25. Line 127: `Then keep bringing out pieces you haven’t moved yet.`

## Check before you finish

- Every line not named above is unchanged, including the diagram block and the sources.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) and the ellipsis character (…) everywhere.

When you're done, reply with one line: done.
