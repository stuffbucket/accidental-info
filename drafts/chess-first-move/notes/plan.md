# Plan: An Accidental Guide to… The First Move in Chess

Slug `chess-first-move`. Builder copied from `drafts/context-windows/` (grey blocks,
callouts, packed pages, optional back sections). Target about 900 to 1,100 printed words,
7 pages. Facts only from `sources.md`. Made 22 October 2026.

Writer: gpt-5.6-sol-fast through `run_writer.sh` (the `copilot` CLI answered a test prompt on
22 October 2026).

## The reader

Someone who has sat down at a chessboard, as White or as Black, knows roughly how the pieces
move, and doesn't know what to do first. They may be playing a child, a friend or a
colleague, and would like not to lose in four moves. They have read no other Accidental
Guide. Chess notation looks like code to them.

## The question

What should my first move be?

## The answer, in order

1. White moves first. The opening has two jobs: bring your pieces out quickly and get your
   king safe. Three ideas do most of it: the center, development, castling.
2. How to read the board and the moves (one board diagram, notation explained once).
3. Center: the four middle squares, d4, d5, e4, e5. Put a pawn there first.
4. Development: knights and bishops out, each moved once; the queen later.
5. Castling: king two squares toward a rook, the rook jumps over; do it early.
6. What to play: 1.e4 or 1.d4 as White; 1…e5 or 1…d5 as Black; then knights, bishops,
   castle. One warning: the four-move checkmate on f7 (Scholar's Mate).

## Key concepts

Three. Each has a page, a filled tile and one meaning. Colours reuse the registry's six
families by kind of thing: the center is a place you use (Us, red-orange); development and
castling are moves you make, one after another (Ru, yellow).

| No. | Part | Key | Colour | Meaning (draft) |
|---|---|---|---|---|
| 01 | Center | Ce | danger (red-orange, Us family) | The four middle squares, d4, d5, e4 and e5 |
| 02 | Development | Dv | warning (yellow, Ru family) | Moving knights and bishops off the back rank so they can join the game |
| 03 | Castling | Ca | warning (yellow, Ru family) | One move of king and rook that tucks the king in the corner |

None of Ce, Dv, Ca is in the registry. Proposed registry additions: these three, owner
chess-first-move. Spelling "center", as in US Chess and the series' American spelling.

Plain words, no tile: opening, notation, file, rank, piece, pawn, check, checkmate (the last
two belong to An Accidental Guide to: The Last Move in Chess, written alongside).

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover, three tiles | 45 |
| 2 | `{#why}` What should your first move be? | Three short paragraphs, terms on a grey block | 160 |
| 3 | `{#fit}` How do you read the board? | Board diagram (starting position, center tinted), key, notation in two short paragraphs | 140 |
| 4–5 | `{#entry}` × 3, packed | Center, Development, Castling | 3 × 115 |
| 6 | `{#shown}` What should you play first? | Intro, grey Move / Why table, callout on Scholar's Mate, closing sentence | 190 |
| 7 | `{#sources}` Sources | Three sources | 70 |
| | | Total | about 950 |

## Entries

Field mark labels, the same on every entry: When, Aim, Mistake.

| Entry | Identify by | Confused with |
|---|---|---|
| Center | The four middle squares, tinted on the board diagram | Pawn moves |
| Development | Knights and bishops leaving the back rank | Bringing out the queen |
| Castling | King two squares sideways, rook on the other side of it | Moving the king |

## Builder changes (done by hand)

- `content.py`: `FIT_BOARDS` parsed from a `diagram` block in `{#fit}` ("board Label | FEN
  placement | caption", "mark Key squares…"); voice comment.
- `build_guide.py`: `PART_FAMILY`, `NAME2MONO`, `COVER_LINES` ("The First Move", "in
  Chess"), a new `page_fit()` that draws one or two boards with tinted squares, rank and file
  labels, and a key (`FIT_KEY`), and `fit_layout()` for the Word document's crop.
  Pieces are discs with their FIDE letter (K, Q, R, B, N); pawns are small plain discs.
- `build_docx.py`: unchanged (it crops the PDF's board through `fit_layout()`).

## Open questions

- No source says which first move is most common. The guide presents 1.e4 and 1.d4 as two
  moves that follow the principles, without claiming popularity.

## Rounds (22 October 2026)

| Round | Brief | By | Result |
|---|---|---|---|
| 1 | writer-round1.md | gpt-5.6-sol-fast via run_writer.sh | First draft, 1,047 printed words |
| Review | review-readers.md, review-fidelity.md, review-leakage.md | cold subagent reviews | No chess errors; square names before the board page, x and # unexplained, board orientation, overreach on knights-before-bishops and "strongest piece" |
| 2 | EDITS-2.md | gpt-5.6-sol-fast | Fixes applied; one filler word ("just") trimmed by the editor: 1,058 words, 4.8 minutes |

Builder fixes during the rounds: the fit page's title breaks with `<br/>` (`plain_title`),
`FIT_KEY` names only the pieces on the boards, `bold_first()` bolds a one-sentence row whole.
