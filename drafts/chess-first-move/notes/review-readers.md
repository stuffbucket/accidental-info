# The First Move in Chess: reader panel

Reviewed: `drafts/chess-first-move/guide.md`, version 0.1.0, and its 8-page PDF in
`dist/chess-first-move.pdf`. Each page was read as three readers with no access to the
sources:

- **Novice.** An adult who knows how the pieces move and has never studied chess. Wants to
  know what to play on move one.
- **Club player.** Checks that nothing is wrong or misleading.
- **Parent.** About to play their child. Has to set up the board, play sensibly and explain
  the moves.

The voice pass checks the guide against the review skill’s `checklist.md`.

## Top ten fixes

Most serious first.

**1. Squares are named before the reader can read them.**
Page 2, line 25: "The four middle squares, d4, d5, e4 and e5." The novice and the parent
meet d4 on page 2. Letters and numbers are only explained on page 3.
Rewrite line 25: "> | Center | The four squares in the middle of the board. |"

**2. The one full game uses symbols nobody has explained.**
Page 7, line 124: "The game 1.e4 e5 2.Bc4 Bc5 3.Qh5 Nf6 4.Qxf7# ends in checkmate." Page 3
explains piece letters and move numbers but not x or #. The novice and the parent stop at
"Qxf7#".
Rewrite line 42: "White’s pawn moves to e4, then Black’s pawn moves to e5. Black’s move alone is 1…e5. An x means a capture and # means checkmate."

**3. The board is described only from White’s side, and nothing says how to set it down.**
Page 3, lines 36 to 38: "From White’s side, the vertical columns, called files, run from a
to h going left to right." The parent playing Black sees h on the left. A board turned the
wrong way is the usual first mistake at a home table, and the guide never says which way
round it goes.
Rewrite line 38, replacing "The tinted squares are d4, d5, e4 and e5." with: "The tinted squares are d4, d5, e4 and e5. Black sees the board from the other side, so h is on Black’s left. Place the board so each player has a light square in the near right corner."

**4. "Nf3 and Nc6" doesn’t say whose moves they are.**
Page 7, line 119: "| Nf3 and Nc6 | Develop knights, then bishops. Each move brings one piece
into the game. |" The novice reads both as their own moves. The row has no move number,
unlike every row above it.
Rewrite line 119: "> | 2.Nf3 Nc6 | White’s knight goes to f3 and Black’s knight goes to c6. Each move brings one piece into the game. |"

**5. "Lines" means two different things.**
Line 18: "Opening lines matter less when you’re learning than a few principles you can use
against whatever the other player does." Lines 115 to 118: "opens lines for the queen and a
bishop". On page 2 a line is a memorized sequence of moves. On page 7 it is a path a piece
can move along. The novice knows neither meaning.
Rewrite lines 18 to 19, from "Opening lines" to the end of the paragraph: "When you’re learning, a few principles help more than memorized sequences of moves. You can use the principles against whatever the other player does."
Rewrite line 115: "> | 1.e4 | As White. The e-pawn moves two squares and frees the queen and a bishop to move. |" (and the same change in lines 116 to 118).

**6. The castling rules end on a touch rule that is never introduced.**
Page 6, lines 105 to 107: "The king can’t be in check or cross or land on an attacked square.
Touch the king first, since touching the rook first may require you to move the rook." The
parent playing at home doesn’t know that touching a piece can commit you to moving it. The
club player agrees the rule is real but it needs the touch-move rule behind it. "Be in check
or cross or land on" also takes two readings.
Rewrite lines 105 to 107, from "The king can’t": "The king can’t castle out of check. The king also can’t cross or land on a square an enemy piece attacks. Move the king first, then the rook."

**7. The Scholar’s Mate advice is too absolute and too vague.**
Page 7, lines 124 to 125: "As Black, when a queen and bishop point at f7, defend it, for
example with your queen, before doing anything else." The club player objects to "before
doing anything else" (if you can capture the queen, you do that). The novice doesn’t know
which queen move defends f7. In this game White’s queen also attacks e5, so the defence has
to cover both.
Rewrite, from "As Black": "As Black, when White’s queen and bishop both aim at f7, defend f7 on your next move. In this game, 3…Qe7 defends f7 and the e5 pawn."

**8. "Knights, then bishops" is stated as a rule.**
Page 5, line 78: "| Aim | Knights, then bishops |", and line 119. The club player notes that
bishops often come out before knights, especially after 1.d4. The point is to get both out.
Rewrite line 78: "> | Aim | Knights and bishops out |"

**9. 0-0 and 0-0-0 are never told apart.**
Page 6, line 91: "written 0-0 or 0-0-0". Page 7 then recommends "0-0" with no side named. The
novice can’t tell which castling that is.
Rewrite line 91: "| What | Castling is one move of the king and a rook, written 0-0 on the king’s side or 0-0-0 on the queen’s side. The king moves two squares toward the rook, then the rook lands on the square the king crossed. |"

**10. Two pages carry almost the same title.**
Line 11: "What should your<br/>first move be?" Line 109: "What should you<br/>play first?" The
parent flipping back can’t tell the two apart. Page 2 is about what the first moves do.
Rewrite line 11: "# What do the<br/>first moves do? {#why}"

## Page by page

### Page 1: cover

| Reader | Stops at | Why |
|---|---|---|
| Novice | | Reads through |
| Club player | | Nothing wrong |
| Parent | | Reads through |

Rewrite: none.

### Page 2: What should your first move be?

| Reader | Stops at | Why |
|---|---|---|
| Novice | "d4, d5, e4 and e5" (line 25) | Notation comes a page later (fix 1) |
| Club player | "Opening lines" (line 18) | Fine for a club player, but it clashes with "opens lines" on page 7 (fix 5) |
| Parent | "Three ideas cover most of what you need at the start." (line 21) | Reads on, but it repeats line 13’s three steps |

Rewrite: fixes 1, 5 and 10.

### Page 3: How do you read the board?

| Reader | Stops at | Why |
|---|---|---|
| Novice | "small disc pawn" (PDF key line) | Reads as a kind of pawn. The key also repeats line 40 |
| Club player | | Board, colours, tints and corner square are all correct |
| Parent | "From White’s side" (line 36) | Playing Black, or setting the board up (fix 3) |

Rewrite of the key line (printed by the builder): "Letters mark the pieces: K king, Q queen, R rook, B bishop, N knight. A small disc is a pawn. White’s pieces are light and Black’s are dark."
Then on line 40, replace "Pieces use K for king, Q for queen, R for rook, B for bishop and N for knight." with "Written moves use the same letters, with N for knight because K is the king."

### Page 4: Center

| Reader | Stops at | Why |
|---|---|---|
| Novice | "as its pawns are exchanged" (line 50) | "Exchanged" isn’t defined, and nothing says why an open center matters |
| Club player | "helps your pieces reach both sides of the board" (line 50) | Vague. Page 7 gives the real reason, which is that the queen and a bishop can move |
| Parent | | Reads through |

Rewrite line 50: "| So what | A center pawn move frees your queen and a bishop to move. The center usually opens first, because center pawns often capture each other. |"

### Page 5: Development

| Reader | Stops at | Why |
|---|---|---|
| Novice | "A lead in development gives you more pieces in the game than your opponent." (line 71) | Circular. It says what a lead is, not why it matters |
| Club player | "Moving one piece twice" (line 79) | Sometimes you have to, when the piece is attacked |
| Parent | "Knights, then bishops" (line 78) | Will teach it to the child as a rule (fix 8) |

Rewrite line 71: "| So what | Your opponent is bringing pieces out too, so develop quickly. A lead in development means you have more pieces in the game than your opponent. |"
Rewrite line 79: "> | Mistake | Moving one piece twice for no reason |"

### Page 6: Castling

| Reader | Stops at | Why |
|---|---|---|
| Novice | "0-0 or 0-0-0" (line 91) | No side named (fix 9) |
| Club player | "touching the rook first may require you to move the rook" (line 106) | True under touch-move, which is never mentioned (fix 6) |
| Parent | "can’t be in check or cross or land on" (line 105) | Has to read it twice (fix 6) |

Rewrite: fixes 6 and 9.

### Page 7: What should you play first?

| Reader | Stops at | Why |
|---|---|---|
| Novice | "4.Qxf7#" (line 124) | x and # undefined (fix 2) |
| Club player | "before doing anything else" (line 125) | Too absolute (fix 7) |
| Parent | "develop your other pieces" (line 111) | "Other pieces" includes the queen, which page 5 says to hold back |

Rewrite line 111: "Choose a center pawn, develop your knights and bishops and castle."

### Page 8: Sources

| Reader | Stops at | Why |
|---|---|---|
| Novice | | Reads through |
| Club player | | Sources are the right ones |
| Parent | | Reads through |

Rewrite: none.

## Voice pass

| Line | Text | Rule | Rewrite |
|---|---|---|---|
| 27 | "One move that moves your king and a rook." | Plain words (repeats "move") | "One move of your king and a rook together." |
| 69 | "Knights and bishops leaving their starting row." | One name per thing (ranks are defined on page 3) | "Knights and bishops leaving their starting squares." |
| 117 | "The e-pawn answers White in the middle" | Vague stand-in | "> \| 1…e5 \| As Black, after 1.e4. The e-pawn moves two squares, blocks White’s e-pawn and frees the queen and a bishop to move. \|" |
| 118 | "The d-pawn answers White in the middle" | Vague stand-in | "> \| 1…d5 \| As Black, after 1.d4. The d-pawn moves two squares, blocks White’s d-pawn and frees the queen and a bishop to move. \|" |

No row sentence starts with It, Its, They or This. No em dashes, semicolons, exclamation marks
or straight apostrophes.

## Verdict

All three readers would finish the guide. It takes five minutes, and the main advice (a center
pawn, then knights and bishops, then castle) is clear on pages 2 and 7. The novice and the
parent stall on notation used before it’s explained (page 2) or never explained (x and # on
page 7), and the parent gets no help setting up the board. The club player finds nothing
wrong in the moves or the diagram, only advice stated more firmly than it should be.
