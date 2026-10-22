# Plan: An Accidental Guide to… The Caro-Kann for Black

Slug `chess-caro-kann`. Builder copied from `drafts/chess-last-move/` with `new_guide.py`,
then given the same board changes as chess-scholars-mate (boards drawn with
`packages/chess/chessdiagram.py`, a board in each entry and in a back section). Target about
1,100 printed words, 9 pages. Facts only from `sources.md`. Made 22 October 2026.

Writer: gpt-5.6-sol-fast through `run_writer.sh` (the `copilot` CLI at `~/.local/bin/copilot`).

## The reader

Someone who knows how the pieces move, plays casual games, and wants one dependable answer
when White opens 1.e4. Has perhaps read An Accidental Guide to: The First Move in Chess. No
theory, and no wish to memorize long lines. Brian's aim: "We aren't trying to get them to
memorize anything; the goal is to give them enough to 'see' the board and want to learn
more."

## The question

What do I play as Black against 1.e4, and what do I do next?

## The answer, in order

1. The Caro-Kann is 1.e4 c6 2.d4 d5: c6 prepares d5, which challenges White's e4 pawn. It is
   known for being solid. It answers 1.e4 only; against 1.d4 a simple start is 1…d5.
2. What Black sets up: one board after 2…d5. The bishop on c8 has an open road to f5.
3. The light bishop: the plan. Get it out (f5 or g4) before …e6, then …e6, develop, castle.
   Unlike the French (1.e4 e6), where …e6 shuts the bishop in.
4. Advance (3.e5): 3…Bf5, then …e6 and …c5.
5. Exchange (3.exd5): 3…cxd5, then knights out; Bd3 stops …Bf5, so the bishop goes to g4.
6. Main line (3.Nc3 or 3.Nd2 dxe4 4.Nxe4): 4…Bf5; White chases the bishop with Ng3 and
   h4–h5; answer h4 with …h6.
7. Which traps should you avoid? Smothered mate (5.Qe2 Ngf6?? 6.Nd6#), the h-pawn against
   the bishop in the main line, h4 and g4 in the Advance.

## Key concepts

Four. Each has a page, a filled tile and one meaning. One colour per part.

| No. | Part | Key | Colour | Meaning (draft) |
|---|---|---|---|---|
| 01 | The light bishop | Lb | figjam (Wr family) | Black’s bishop on c8, which goes out to f5 or g4 before …e6 |
| 02 | Advance | Av | warning (Ru family) | White pushes 3.e5 |
| 03 | Exchange | Ex | success (Ck family) | White swaps pawns with 3.exd5 |
| 04 | Main line | Ml | brand (Nu family) | 3.Nc3 or 3.Nd2, dxe4 4.Nxe4 Bf5 |

Codes checked with `list_concepts.py` and `packages/editorial/registry.md` on 22 October
2026: Lb, Av, Ex and Ml are used by no other guide, by no reserved registry code, and by
neither of the other two new chess guides (Scholar’s Mate: Fs, Qn, Gu, Te; problem positions:
Pn, Fk, Bk, Hg, Ks).

Plain words, no tile: development, castling, center (keys in An Accidental Guide to: The
First Move in Chess), checkmate (The Last Move in Chess), the French Defense, the Panov Attack.

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover, four tiles | 50 |
| 2 | `{#why}` What is the Caro-Kann? | Three short paragraphs, terms on a grey block | 170 |
| 3 | `{#fit}` What does Black set up? | One large board, one paragraph | 110 |
| 4–7 | `{#entry}` × 4 | One board each, then the rows | 4 × 120 |
| 8 | `{#habits}` Which traps should you avoid? | Intro, Trap / Avoid it table, one board, closing sentence | 140 |
| 9 | `{#sources}` Sources | Six sources | 90 |
| | | Total | about 1,040 (each board adds 16 printed rank and file labels) |

## Boards

Every board is from Black’s side (`view black`). Every placement was generated from the
moves with python-chess 1.11.2 (scratch venv in /tmp, not the repo's .venv) on 22 October
2026; the smothered-mate board reports checkmate.

| Where | Moves | Placement | Tints and arrows |
|---|---|---|---|
| fit | 1.e4 c6 2.d4 d5 | rnbqkbnr/pp2pppp/2p5/3p4/3PP3/8/PPP2PPP/RNBQKBNR | c8 (Lb); c8→f5, d5→e4 |
| The light bishop | … 3.e5 Bf5 4.Nf3 e6 | rn1qkbnr/pp3ppp/2p1p3/3pPb2/3P4/5N2/PPP2PPP/RNBQKB1R | f5 |
| Advance | … 3.e5 | rnbqkbnr/pp2pppp/2p5/3pP3/3P4/8/PPP2PPP/RNBQKBNR | e5 (Av); c8→f5 |
| Exchange | … 3.exd5 cxd5 4.Bd3 Nc6 5.c3 Nf6 6.Bf4 Bg4 | r2qkb1r/pp2pppp/2n2n2/3p4/3P1Bb1/2PB4/PP3PPP/RN1QK1NR | g4 (Ex) |
| Main line | … 3.Nc3 dxe4 4.Nxe4 Bf5 (3.Nd2 gives the same placement) | rn1qkbnr/pp2pppp/2p5/5b2/3PN3/8/PPP2PPP/R1BQKBNR | f5 (Ml); f5→e4 |
| Traps | … 4.Nxe4 Nd7 5.Qe2 Ngf6 6.Nd6# | r1bqkb1r/pp1npppp/2pN1n2/8/3P4/8/PPP1QPPP/R1B1KBNR | d6 (Ml) |

Also played through: 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7 8.h5 Bh7 9.Bd3 Bxd3 10.Qxd3; 4…Nd7 5.Qe2
Ndf6 (safe); 3.e5 Bf5 4.h4 e6 5.g4 Be4 6.f3 Bg6 7.h5 (the bishop has no safe square); 4.h4
h5 5.Bd3 Bxd3 6.Qxd3 e6.

## Entries

Field mark labels, the same on every entry: White plays, You play.

| Entry | Identify by | Confused with |
|---|---|---|
| The light bishop | Black’s bishop on c8, with d7 empty after …d5 | The French Defense |
| Advance | White’s e-pawn pushed to e5, next to your d5 pawn | Exchange |
| Exchange | Pawns swapped on d5, the c-file half open | The Panov Attack (4.c4) |
| Main line | White’s knight takes on e4 | 3.Nd2 (the same position after 4.Nxe4) |

## Cross-references

- Points to: An Accidental Guide to: The First Move in Chess (notation, 1…d5 against 1.d4).
- Not mentioned: An Accidental Guide to: Stopping Scholar’s Mate, which is about 1.e4 e5
  lines that the Caro-Kann avoids.

## Builder changes (done by hand, not the writer)

- Same as chess-scholars-mate: `content.boards()`, entry boards, `blocks()` boards, kit drawing.
- `PART_FAMILY`, `NAME2MONO`, `COVER_LINES` ("The Caro-Kann", "for Black"), `BACK_LABW`.
- `build_docx.py`: not touched (Brian refreshes it later).

## Open questions

- No source ties Qb3 to an attack on b7 in the Caro-Kann, so that trap is left out.
- Wikipedia names 4.g4 as the Bayonet; the 4.Nc3 e6 5.g4 line is the Van der Wiel. Neither is
  named in the guide.

## Rounds (22 October 2026)

| Round | Brief | By | Result |
|---|---|---|---|
| 1 | WRITE-1.md | gpt-5.6-sol-fast via run_writer.sh | First draft, 1,136 printed words |
| Review | review-1.md | one cold subagent (fidelity, reader, leakage) | Boards all correct; "a square behind h7" and "5.Ng3 Bg6" as White's reply wrong; trap 1 started from an untaught 4…Nd7; e7 pawn on the mate board unexplained; notation unexplained |
| 2 | EDITS-2.md | gpt-5.6-sol-fast | Fixes applied, version 0.2.0; then trims by the editor (closing line of the traps page, Main line and Advance rows, two captions), version 0.2.1: 1,101 printed words, 5.0 minutes |

Left open: Wikipedia gives 7.Qb3 as White's next move in the Exchange line shown, and no
source read gives Black's answer, so the guide doesn't mention it.
