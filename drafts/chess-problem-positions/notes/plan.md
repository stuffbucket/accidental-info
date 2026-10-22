# Plan: An Accidental Guide to… Getting Out of Trouble in Chess

Slug `chess-problem-positions`. Builder copied from `drafts/chess-last-move/` with
`new_guide.py`, then given the same board changes as chess-scholars-mate (boards drawn with
`packages/chess/chessdiagram.py`, a board in each entry). No `{#fit}` page: `content.py` now
allows it to be missing, and the entries follow the terms page. Target about 1,100 printed
words, 9 pages. Facts only from `sources.md`. Made 22 October 2026.

Writer: gpt-5.6-sol-fast through `run_writer.sh` (the `copilot` CLI at `~/.local/bin/copilot`).

## The reader

Someone who knows how the pieces move and plays casual games, and keeps losing pieces or
games to the same few problems without being able to name them. No theory. Has perhaps read
An Accidental Guide to: The First Move in Chess and An Accidental Guide to: The Last Move in
Chess. Brian's aim: "We aren't trying to get them to memorize anything; the goal is to give
them enough to 'see' the board and want to learn more."

## The question

What are the common problem positions, and how do I get out of each one?

## The answer, in order

1. Five problems come up again and again; each has one clear way out, and one habit that
   stops it happening next time.
2. Pin: a piece that can’t move without exposing a more valuable piece behind it. Pinned to
   the king, it can’t move at all. Way out: block the line (4…Bd7), move the piece behind, or
   chase the pinning piece.
3. Fork: one piece attacking two at once; knights do it best. Way out: capture the forking
   piece if you can (here Qxc2); if the king is in check, answer the check first, then save
   what you can.
4. Back-rank mate: the castled king shut in by its own pawns, mated by a rook or queen on the
   back rank. Way out: give the king a square (h3), or keep a rook or queen guarding the back
   rank.
5. Hanging piece: unprotected and attacked. Way out: move it or defend it. Before each move,
   check the square you put a piece on is safe.
6. King in the center: no castling, center opening, a check. You can’t castle out of check.
   Way out: block with a piece that develops (Bd2 or Nc3), then castle.
7. What do you check before each move? A short table of habits.

## Key concepts

Five. Each has a page, a filled tile and one meaning. One colour per part, so board tints
read apart.

| No. | Part | Key | Colour | Meaning (draft) |
|---|---|---|---|---|
| 01 | Pin | Pn | figjam (Wr family) | A piece that can’t move without exposing a more valuable piece behind it |
| 02 | Fork | Fk | danger (Us family) | One piece attacking two or more enemy pieces at once |
| 03 | Back-rank mate | Bk | warning (Ru family) | Checkmate on the back rank, the king shut in by its own pawns |
| 04 | Hanging piece | Hg | success (Ck family) | A piece that is unprotected and can be captured |
| 05 | King in the center | Ks | assistive (Dm family) | A king that hasn’t castled when the center opens |

Codes checked with `list_concepts.py` and `packages/editorial/registry.md` on 22 October
2026: Pn, Fk, Bk, Hg and Ks are used by no other guide, by no reserved registry code, and by
neither of the other two new chess guides (Scholar’s Mate: Fs, Qn, Gu, Te; Caro-Kann: Lb, Av,
Ex, Ml).

Plain words, no tile: check and checkmate (keys in An Accidental Guide to: The Last Move in
Chess), castling and development (keys in An Accidental Guide to: The First Move in Chess),
notation (explained in The First Move in Chess).

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover, five tiles | 50 |
| 2 | `{#why}` What does trouble look like? | Three short paragraphs; terms on a grey block | 170 |
| 3–7 | `{#entry}` × 5 | One board each, then the rows | 5 × 120 |
| 8 | `{#habits}` What do you check before each move? | Intro, Check / Why table, closing sentence | 110 |
| 9 | `{#sources}` Sources | Ten sources | 120 |
| | | Total | about 1,050 (each board adds 16 printed rank and file labels) |

## Boards

Each board is from the side in trouble: Black for the pin, White for the rest. Every
position was checked with python-chess 1.11.2 (scratch venv in /tmp); the results are in
`sources.md`, "Board lines".

| Entry | Position | How it arises | Tints and arrows |
|---|---|---|---|
| Pin | r1bqkbnr/ppp2ppp/2np4/1B2p3/3PP3/5N2/PPP2PPP/RNBQK2R | 1.e4 e5 2.Nf3 Nc6 3.Bb5 d6 4.d4 (Ruy Lopez, Steinitz Defence), Black to move | c6; b5→e8 |
| Fork | 4k3/pp3ppp/8/8/8/8/PPn2PPP/R2QK2R | A set-up position, White to move and in check | c2; c2→e1, c2→a1 |
| Back-rank mate | 4r1k1/pp3ppp/8/8/8/Q7/PP3PPP/6K1 | A set-up position, White to move; Black threatens Re1# | e1; e8→e1 |
| Hanging piece | rnbqkb1r/ppp2ppp/3p1n2/4N3/4P3/8/PPPP1PPP/RNBQKB1R | 1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 (Petrov’s Defence), White to move | e5; d6→e5 |
| King in the center | r1bqk2r/pppp1ppp/2n2n2/8/1bBPP3/5N2/PP3PPP/RNBQK2R | Giuoco Piano: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4+ | e1; b4→e1 |

## Entries

Field mark labels, the same on every entry: Way out, Next time.

| Entry | Identify by | Confused with |
|---|---|---|
| Pin | A bishop, rook or queen lined up through your piece to a bigger one | Relative pin |
| Fork | One piece, often a knight, attacking two of yours | Pin |
| Back-rank mate | Castled king behind three unmoved pawns, enemy rook or queen on an open file | A safe castled king |
| Hanging piece | A piece with nothing defending it, and something attacking it | En prise |
| King in the center | King still on e1 or e8 with the center files opening | Castling out of check |

## Cross-references

- Points to: An Accidental Guide to: The First Move in Chess (notation, castling).
- Points to: An Accidental Guide to: The Last Move in Chess (check, checkmate).

## Builder changes (done by hand, not the writer)

- Same as chess-scholars-mate: `content.boards()`, entry boards, `blocks()` boards, kit drawing.
- `content.py`: `{#fit}` optional.
- `PART_FAMILY`, `NAME2MONO`, `COVER_LINES` ("Getting Out of", "Trouble in Chess"), `BACK_LABW`.
- `build_docx.py`: not touched (Brian refreshes it later).

## Open questions

- No source gives a step-by-step "what to do when forked". The guide says: answer the check,
  capture the forking piece if you can, otherwise save the more valuable piece. The first two
  follow from the three ways out of check (Chess.com, FIDE 3.9.2).
- Counting attackers against defenders is only on a Chess.com page that came back in German;
  not used.

## Rounds (22 October 2026)

| Round | Brief | By | Result |
|---|---|---|---|
| 1 | WRITE-1.md | gpt-5.6-sol-fast via run_writer.sh | First draft, 1,312 printed words, 9 pages with a `{#habits}` page |
| Review | review-1.md | one cold subagent (fidelity, reader, leakage) | Boards all correct; "move or defend it" wrong for a knight a pawn attacks; vague reason knights fork well; captions not matching boards; notation, back rank, absolute pin undefined |
| 2 | EDITS-2.md | gpt-5.6-sol-fast | Fixes applied; `{#habits}` page cut (it repeated the Next time field marks); FIDE and Wikipedia Castling dropped from the sources page (Chess.com covers both facts); version 0.2.0 |
| 2b | none | the editor | Sentence trims across the entries, version 0.2.1: 1,099 printed words, 5.0 minutes, 8 pages |
