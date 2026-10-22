# Plan: An Accidental Guide to… Stopping Scholar’s Mate

Slug `chess-scholars-mate`. Builder copied from `drafts/chess-last-move/` with `new_guide.py`,
then changed by hand to draw every board with the chess diagram kit (`packages/chess/`), with
boards in entries as well as on `{#fit}`. Target about 1,100 printed words, 9 pages. Facts only
from `sources.md`. Made 22 October 2026.

Writer: gpt-5.6-sol-fast through `run_writer.sh` (the `copilot` CLI at `~/.local/bin/copilot`).

## The reader

Someone who knows how the pieces move and plays casual games, online or at a club, and keeps
losing in four moves to the same queen-and-bishop trick, or is nervous it will happen. No
theory. Has perhaps read An Accidental Guide to: The First Move in Chess, which shows the
mate once in a warning box. Brian's aim: "We aren't trying to get them to memorize anything;
the goal is to give them enough to 'see' the board and want to learn more."

## The question

How do I stop Scholar’s Mate, and make it backfire?

## The answer, in order

1. Scholar’s Mate is a queen and bishop aiming at f7, the one square next to Black’s king that
   only the king defends. It can be stopped easily, and once it’s stopped the attacker is
   usually worse off.
2. What it looks like: one board, from Black’s side, with both lines into f7.
3. The f7 square: the target; the mate when you miss it (3…Nf6?? 4.Qxf7#).
4. The early queen: 2.Qh5 (the Wayward Queen) or Qf3. It attacks e5 and f7. 2…Nc6.
5. Guarding f7: 3…g6 (blocks and attacks the queen) or 3…Qe7. Not 3…Nf6 while the queen is on
   h5 and the bishop on c4. 4.Qf3 Nf6 is right, because the knight now blocks the f-file.
6. Tempo: develop with a threat to the queen. 5.Nc3 Nd4 attacks the queen and c2.
7. A short reply table for the usual move orders.

## Key concepts

Four. Each has a page, a filled tile and one meaning. Colours are one per part, from the six
families, chosen so the board tints read apart: red-orange for the target, yellow for the
attacker's queen, green for the guard, pink for the move you choose.

| No. | Part | Key | Colour | Meaning (draft) |
|---|---|---|---|---|
| 01 | The f7 square | Fs | danger (Us family) | The pawn square next to Black’s king that only the king defends at the start |
| 02 | The early queen | Qn | warning (Ru family) | White’s queen brought out on move 2 or 3, to h5 or f3 |
| 03 | Guarding f7 | Gu | success (Ck family) | A move that defends f7 or blocks the line to it: …g6, …Qe7, …Nf6 when the queen is on f3 |
| 04 | Tempo | Te | assistive (Dm family) | A move gained by developing a piece with a threat, so the queen must move again |

Codes checked with `list_concepts.py` and `packages/editorial/registry.md` on 22 October
2026: Fs, Qn, Gu and Te are used by no other guide, by no reserved code in the registry, and
by neither of the other two new chess guides (Caro-Kann: Lb, Av, Ex, Ml; problem positions:
Pn, Fk, Bk, Hg, Ks).

Plain words, no tile: check, checkmate (keys in An Accidental Guide to: The Last Move in
Chess), development (a key in An Accidental Guide to: The First Move in Chess), algebraic
notation (explained in The First Move in Chess; one pointer here).

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover, four tiles | 50 |
| 2 | `{#why}` What is Scholar’s Mate? | Three short paragraphs; terms on a grey block; notation pointer | 170 |
| 3 | `{#fit}` What does the attack look like? | One large board from Black’s side; one paragraph | 120 |
| 4–7 | `{#entry}` × 4 | One board each, then the rows | 4 × 130 |
| 8 | `{#shown}` What do you play against it? | Intro, Move / Why table, closing sentence | 130 |
| 9 | `{#sources}` Sources | Six sources | 90 |
| | | Total | about 1,080 (each board adds 16 printed rank and file labels) |

## Boards

Every board is from Black’s side (`view black`). Each FEN placement and move sequence was
played out with python-chess 1.11.2 (a scratch venv in /tmp, not the repo's .venv) on 22
October 2026; the mate board reports checkmate, the others are legal positions with the side
to move as the caption implies.

| Where | Position | Moves | Tints and arrows |
|---|---|---|---|
| fit | r1bqkbnr/pppp1ppp/2n5/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR | 1.e4 e5 2.Qh5 Nc6 3.Bc4 | f7 (Fs); h5→f7, c4→f7 |
| The f7 square | r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR | … 3…Nf6?? 4.Qxf7# (checkmate) | f7; c4→f7 |
| The early queen | rnbqkbnr/pppp1ppp/8/4p2Q/4P3/8/PPPP1PPP/RNB1KBNR | 1.e4 e5 2.Qh5 | h5 (Qn); h5→e5, h5→f7 |
| Guarding f7 | r1bqkbnr/pppp1p1p/2n3p1/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR | … 3.Bc4 g6 | g6 (Gu); g6→h5 |
| Tempo | r1bqkb1r/pppp1p1p/5np1/4p3/2BnP3/2N2Q2/PPPP1PPP/R1B1K1NR | … 3…g6 4.Qf3 Nf6 5.Nc3 Nd4 | d4 (Te); d4→f3, d4→c2 |

## Entries

Field mark labels, the same on every entry: Watch for, Your answer.

| Entry | Identify by | Confused with |
|---|---|---|
| The f7 square | Queen and bishop both aimed at f7 | f2 (White’s matching weak square) |
| The early queen | White’s queen out on move 2 or 3, on h5 or f3 | A strong attack |
| Guarding f7 | A move that blocks or defends the line into f7 | 3…Nf6 (natural, but loses to Qxf7#) |
| Tempo | A developing move that attacks the queen | Time on the clock |

## Cross-references

- Points to: An Accidental Guide to: The First Move in Chess (notation, development).
- Points to: An Accidental Guide to: The Last Move in Chess (checkmate).

## Builder changes (done by hand, not the writer)

- `content.py`: `boards()` parses every ```diagram block (board, mark, arrow, view); entries
  get `boards`; `ALL_BOARDS`.
- `build_guide.py`: boards drawn with `packages/chess/chessdiagram.py` (`draw_board`, Black's
  side); a small board under each entry's name with its label and caption beside it;
  `blocks()` draws a ```diagram block in a back section; the piece key is gone (the kit draws
  real piece shapes). `PART_FAMILY`, `NAME2MONO`, `COVER_LINES`, `BACK_LABW`.
- `build_docx.py`: not touched (copied from chess-last-move; Brian refreshes it later). The
  Word document has the `{#fit}` board but not the entry boards yet.

## Open questions

- No source gives one sentence on when …Nf6 is safe; the guide shows the two cases (loses with
  the queen on h5 and bishop on c4; right after 4.Qf3, when the knight blocks the f-file).
- Sources range from "equal" to "Black slightly better" after the queen is chased. The guide
  says the attack gains nothing and the attacker often ends up worse, not that Black wins.

## Rounds (22 October 2026)

| Round | Brief | By | Result |
|---|---|---|---|
| 1 | WRITE-1.md | gpt-5.6-sol-fast via run_writer.sh | First draft, 1,115 printed words |
| Review | review-1.md | one cold subagent (fidelity, reader, leakage) | Boards all correct; "Qh5 no longer possible" wrong; …Nd4 overstated; "h5 or f3" unsourced; develop, fork, tempi unexplained |
| 2 | EDITS-2.md | gpt-5.6-sol-fast | Fixes applied, version 0.2.0; then three trims by the editor (shown table, Tempo So what): 1,098 printed words, 5.0 minutes |
