# The First Move in Chess: fidelity review

Checked `drafts/chess-first-move/guide.md`, version 0.1.0, against
`drafts/chess-first-move/notes/sources.md`. The raw pages behind it were not available. The
hype notes were not read. Sources fetched 22 October 2026.

Every move, square and position in the text and the board diagram was also checked against
the rules quoted in `sources.md` (FIDE Laws 1.2, 2.1, 2.4, 3.2 to 3.8, 4.4.1 and Appendix C).

| Verdict | Count |
|---|---|
| Wrong | 0 |
| Overreach | 2 |
| Unsourced | 5 |
| Naming | 2 |
| Non-public | 0 |
| Stale | 0 |

Each verdict section runs from most to least serious.

## Moves, squares and the board diagram

No move, square or position is wrong.

| Line | Item | Check |
|---|---|---|
| 32 | FEN `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR` | The standard starting position. White on ranks 1 and 2, Black on 7 and 8 (C.6) |
| 32 | Rendered board (PDF p. 3) | h1 is light, a1 is dark (2.1). Files a to h left to right, ranks 1 to 8 bottom to top (C.5, C.6). Queens on d1 and d8, kings on e1 and e8 |
| 33 | Tinted d4, d5, e4, e5 | Matches the center in both the FIDE curriculum and US Chess |
| PDF p. 3 | Key: "K king, Q queen, R rook, B bishop, N knight" | Matches C.2. "White’s pieces are light, Black’s are dark" matches 1.2 |
| 41 to 42 | 1.e4 e5, pawn move by square only | C.4, C.8 and the sample game in C |
| 49 | King or queen pawn two squares into the center | e2-e4 and d2-d4 land on center squares (3.7.2) |
| 90 to 91 | King two squares, rook to the square crossed, 0-0 and 0-0-0 | 3.8.2, C.13 |
| 104 to 106 | King and rook unmoved, nothing between, no check, no attacked square crossed or landed on | 3.8.2.1, 3.8.2.2 |
| 115 to 118 | 1.e4, 1.d4, 1…e5, 1…d5 open lines for the queen and a bishop | Correct from 3.2, 3.4 and 3.5. The e-pawn frees Qd1-h5 and Bf1, the d-pawn frees the d-file for the queen and Bc1, and the same for Black |
| 119 | Nf3, Nc6 | Legal second moves after any of the four first moves (3.6) |
| 120 | 0-0 after clearing the squares between king and rook | 3.8.2.2 (4) |
| 123 | f7 defended only by Black’s king at the start | Curriculum, lesson 18 |
| 124 | 1.e4 e5 2.Bc4 Bc5 3.Qh5 Nf6 4.Qxf7# | Matches the US Chess sample game. Checked: Qh5-f7 runs through an empty g6, Bc4 guards f7 through empty d5 and e6, and the king has no flight square (d8 and d7 are occupied, e7 and f8 are covered by the queen) |

## Overreach

### O1. Knights before bishops (lines 78 and 119, Development and page 7)

**Guide:** "| Aim | Knights, then bishops |" (line 78) and "Develop knights, then bishops." (line 119)

**Source** (FIDE, Curriculum: Chess for Refugees,
https://www.fide.com/docs/presentations/Curriculum%20Chess%20for%20Refugees.pdf): "1. First develop the pawns in the center, then knights and bishops." US Chess,
https://new.uschess.org/sites/default/files/media/documents/11th-edition-guide-to-scholastic-chess-6-29-21.pdf: "F. Develop knights and bishops quickly."

**Verdict:** overreach. Both sources put knights and bishops together. Neither gives an order
between them.

**Corrected:** line 78: "> | Aim | Knights and bishops out |". Line 119: "> | 2.Nf3 Nc6 | White’s knight goes to f3 and Black’s knight goes to c6. Each move brings one piece into the game. |"

### O2. Defending f7 "before doing anything else" (line 125, warning)

**Guide:** "As Black, when a queen and bishop point at f7, defend it, for example with your queen,
before doing anything else."

**Source** (FIDE Curriculum, lesson 18): "The f7-pawn is considered weak because it is
defended only by the king"

**Verdict:** overreach. The source says why f7 is weak, not that defending it comes before
every other move. Capturing the attacking queen, for one, comes first. The queen defence is
not in the sources, but 3…Qe7 follows from 3.4 (the queen moves along a diagonal to e7, then
guards f7 on the rank and e5 on the file).

**Corrected:** from "As Black" in line 124: "As Black, when White’s queen and bishop both aim at f7, defend f7 on your next move. In this game, 3…Qe7 defends f7 and the e5 pawn."

## Unsourced

### U1. Touching the rook first (lines 106 to 107, Castling)

**Guide:** "Touch the king first, since touching the rook first may require you to move the
rook."

**Verdict:** unsourced. `sources.md` quotes only 4.4.1 (touching king and rook commits you
to castling). The rook-first case is Article 4.4.2, which isn’t quoted. The rule is also a
touch-move rule the guide never introduces. Either add 4.4.2 and 4.3.1 to `sources.md`, or
replace the sentence with one that 3.8.2 already supports.

**Corrected:** "Move the king first, then the rook."

### U2. "The queen is your strongest piece" (line 83, Development)

**Guide:** "The queen is your strongest piece, but bring it out later."

**Verdict:** unsourced. No source in `sources.md` ranks the pieces. The curriculum says only
that the queen "might be attacked by developing pieces of opponent". Either find a public
source and add it, or cut the claim.

**Corrected:** "Bring your queen out after your knights and bishops."

### U3. "reach both sides of the board" (line 50, Center)

**Guide:** "A center pawn helps your pieces reach both sides of the board."

**Verdict:** unsourced. Neither source says this, and it doesn’t follow from the move rules
as stated. What does follow from 3.2, 3.4 and 3.5 is that a center pawn move frees the queen
and a bishop. The second sentence is sourced (curriculum lesson 12: "the center pawns often
get exchanged").

**Corrected:** "| So what | A center pawn move frees your queen and a bishop to move. The center usually opens first, because center pawns often capture each other. |"

### U4. "An ordinary king move goes one square" (line 104, Castling)

**Guide:** "An ordinary king move goes one square."

**Verdict:** unsourced. The fact is right, but `sources.md` quotes no king-move rule (Laws
3.8.1). Add the 3.8.1 excerpt to `sources.md`. The text can stay.

**Corrected:** no change to the text.

### U5. The "1…" convention for a Black move (line 42, How do you read the board?)

**Guide:** "Black’s move alone is 1…e5."

**Verdict:** unsourced. Appendix C as quoted in `sources.md` doesn’t show how a Black move is
written on its own. The convention is standard. Add an excerpt that shows it, or keep the
text and accept the gap.

**Corrected:** no change to the text.

## Naming

### N1. "Lines" in two senses (lines 18 and 115 to 118)

**Guide:** "Opening lines matter less when you’re learning" (line 18) and "opens lines for the
queen and a bishop" (lines 115 to 118)

**Source** (FIDE Curriculum): "Concrete opening variations are overrated for beginners."

**Verdict:** naming. The source calls memorized sequences "variations". The guide calls them
"lines", then uses "lines" for the paths a piece moves along.

**Corrected:** lines 18 to 19, from "Opening lines": "When you’re learning, a few principles help more than memorized sequences of moves. You can use the principles against whatever the other player does." Line 115: "> | 1.e4 | As White. The e-pawn moves two squares and frees the queen and a bishop to move. |" (the same change in lines 116 to 118).

### N2. "Starting row" for rank (line 69, Development)

**Guide:** "Knights and bishops leaving their starting row."

**Source** (FIDE Laws 2.4, https://handbook.fide.com/chapter/E012023): "The eight horizontal
rows of squares are called ‘ranks’."

**Verdict:** naming. Page 3 defines ranks. Line 69 switches to "row".

**Corrected:** "| Identify by | Knights and bishops leaving their starting squares. |"

## Non-public

None.

## Stale

None. The Laws are dated January 2023, and `sources.md` records that the handbook shows no
later edition as of 22 October 2026. The sources page (line 131) gives the check date.

## Sources page

- Listed but not used: none. The Laws support the board and notation, the curriculum supports
  the principles and f7, and US Chess supports the center squares and the sample game.
- Used but not listed: none, but `sources.md` needs excerpts for Laws 3.8.1 (U4) and 4.4.2
  (U1) if those sentences stay.
- The table (lines 133 to 137) matches `sources.md` in titles, dates and addresses. The
  curriculum address drops "www.", which is harmless. In the PDF the US Chess address breaks
  mid-word ("…11th-edition-gui" / "de-to-scholastic…"), which is a layout issue, not a
  fidelity one.
