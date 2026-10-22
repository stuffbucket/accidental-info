# Plan: An Accidental Guide to… The Last Move in Chess

Slug `chess-last-move`. Builder copied from `drafts/context-windows/`, with the board diagram
from `chess-first-move` (same code). Target about 1,000 to 1,100 printed words, 8 pages.
Facts only from `sources.md`. Made 22 October 2026.

Writer: gpt-5.6-sol-fast through `run_writer.sh` (the `copilot` CLI answered a test prompt on
22 October 2026).

## The reader

Someone playing a casual game, or their first club game, who isn't sure whether the game is
over. Did they win? Is it a draw? Can they just shake hands? They know how the pieces move.
They have read no other Accidental Guide, perhaps An Accidental Guide to: The First Move in
Chess.

## The question

How does a chess game end?

## The answer, in order

1. A game ends in a win (checkmate, or the other player resigns) or a draw (stalemate,
   agreement, repetition, and a few others). Check is the warning before checkmate.
2. Checkmate or stalemate? Two boards side by side: same pieces, one square apart.
3. Check: the king is attacked; you must get out of it (move, block, capture).
4. Checkmate: check with no way out. A win, one point.
5. Stalemate: no legal move and not in check. A draw, not a win.
6. Draw: by agreement, by repeating a position, by fifty moves, or when nobody can mate.
7. Resigning: say "I resign" or tip over your king. A handshake alone is unclear.
8. How do you finish politely? Touch-move, "I adjust", draw offers, resigning clearly,
   handshake, putting the pieces back.

## Key concepts

Five. Each has a page, a filled tile and one meaning. Colours reuse the registry's six
families by kind of thing: check is a threat the other player must answer (Ck, green);
checkmate and stalemate are results with a score (Nu, blue); a draw by agreement and
resigning are decisions people make (Dm, pink).

| No. | Part | Key | Colour | Meaning (draft) |
|---|---|---|---|---|
| 01 | Check | Kc | success (green, Ck family) | Your king is attacked and you must deal with it now |
| 02 | Checkmate | Mt | brand (blue, Nu family) | Check with no way out; the game is won |
| 03 | Stalemate | Sm | brand (blue, Nu family) | No legal move and not in check; the game is drawn |
| 04 | Draw | Dw | assistive (pink, Dm family) | A game nobody wins: agreed, repeated, or with nothing left to mate with |
| 05 | Resigning | Rs | assistive (pink, Dm family) | Ending the game by conceding it |

Codes: `Ch` is Check in harness-engineering (a different meaning of the same word, an
automated check on code), so this guide's Check is `Kc` (king in check). Mt, Sm, Dw, Rs are
free. Proposed registry additions: these five, owner chess-last-move, with a note that
"Check" means two things across the series (chess and harness-engineering).

Plain words, no tile: touch-move, handshake, clock, arbiter (not used), notation.

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover, five tiles | 50 |
| 2 | `{#why}` How does a chess game end? | Three short paragraphs, terms on a grey block | 170 |
| 3 | `{#fit}` Checkmate or stalemate? | Two boards, key, one paragraph | 120 |
| 4–6 | `{#entry}` × 5, packed | Check, Checkmate, Stalemate, Draw, Resigning | 5 × 95 |
| 7 | `{#habits}` How do you finish politely? | Intro, grey Habit / Why table, closing sentence | 150 |
| 8 | `{#sources}` Sources | Four sources | 90 |
| | | Total | about 1,050 |

## Entries

Field mark labels, the same on every entry: Result, Decided by.

| Entry | Identify by | Confused with |
|---|---|---|
| Check | "Check" said aloud, or + after a move | Checkmate |
| Checkmate | The king in check, with no move that gets out | Stalemate |
| Stalemate | Your turn, king safe, no legal move | Any draw |
| Draw | An offer after a move, or the same position again and again | A handshake |
| Resigning | "I resign", or the king tipped over | Stopping the clock |

## Builder changes (done by hand)

- Same board code as chess-first-move: `FIT_BOARDS` in `content.py`, `page_fit()`,
  `fit_layout()`, `FIT_KEY` in `build_guide.py`.
- `PART_FAMILY`, `NAME2MONO`, `COVER_LINES` ("The Last Move", "in Chess"), `BACK_LABW`.

## Open questions

- The handshake: FIDE's teaching curriculum says players shake hands before and after a
  game; US Chess says a handshake on its own isn't a resignation. The guide says both.
- Casual games have no arbiter or clock. The guide keeps to rules that apply on any board
  (FIDE's Basic Rules of Play) and mentions the clock only where a source does.

## Rounds (22 October 2026)

| Round | Brief | By | Result |
|---|---|---|---|
| 1 | writer-round1.md | gpt-5.6-sol-fast via run_writer.sh | First draft, 1,216 printed words |
| Review | review-readers.md, review-fidelity.md, review-leakage.md | cold subagent reviews | Both boards correct; wrong stalemate advice ("leave the king a move"), repetition read as automatic, FIDE-only rules stated as universal, "safe" for "not in check" |
| 2 | EDITS-2.md | gpt-5.6-sol-fast | Fixes applied, time loss added (FIDE 6.9), 1,156 words |
| 3 | EDITS-3.md | gpt-5.6-sol-fast | Cuts, then four small trims by the editor: 1,097 words, 5.0 minutes |
