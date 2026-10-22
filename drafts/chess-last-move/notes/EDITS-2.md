# Edits, round 2: The Last Move in Chess

Apply these edits in place to `drafts/chess-last-move/guide.md` (your working directory's
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

The cold reviews (notes/review-readers.md, review-fidelity.md, review-leakage.md) found one
wrong piece of advice (stalemate is about the whole side having no move, not the king), a
repetition rule that reads as automatic, FIDE-only rules stated as universal, two unsourced
lines, and "safe" used as a second name for "not in check". The printed guide is 1,216 words
and must come down under 1,100, so this round also cuts repeats. Every replacement below is
word for word: use it as given.

## Front matter

1. Line 8: `version: 0.2.0`

## How does a chess game end? (lines 11 to 30)

2. Lines 13–16 (the first paragraph, four lines): replace with these three lines:
   A chess game ends in a win or a draw. You win by checkmate, or when the other player
   resigns. With a clock, a player who runs out of time usually loses. A draw comes from
   agreement, stalemate or one of a few other rules.
3. Lines 18–20 (the second paragraph, three lines): replace with these two lines:
   A win scores one point, a draw half a point each and a loss nothing. The game ends as soon
   as checkmate, stalemate or a resignation happens, so nobody ever captures a king.
4. Line 22: `Check is the only one of these five that doesn’t end the game.`
5. Line 28: `> | Stalemate | The player to move has no legal move, but that player’s king isn’t in check. |`

## Checkmate or stalemate? (lines 32 to 44)

6. Line 35: `board Checkmate | 7k/6Q1/6K1/8/8/8/8/8 | Black to move. The queen gives check, and the white king guards the queen.`
7. Line 37: `board Stalemate | 7k/5Q2/6K1/8/8/8/8/8 | Black to move. The king isn’t in check, but every square next to it is attacked.`
8. Lines 41–44 (the paragraph, four lines): replace with these three lines:
   Black has no legal move on either board. The left board is checkmate, so White wins. The
   right board is stalemate, so the game is a draw. When you’re winning, make sure your
   opponent still has a legal move, unless your move is checkmate.

## Check (lines 46 to 64)

9. Line 50: `| Identify by | A piece attacking a king, or a + written after the move. |`
10. Line 51: `| What | Check means the king is attacked by an enemy piece. The game goes on. |`

## Checkmate (lines 66 to 84)

11. Line 71: `| What | Checkmate is check with no legal way out. None of the three ways out of check works. |`
12. Line 79: `> | Decided by | The checkmating move |`
13. Lines 83–84 (the paragraph, two lines): replace with these two lines:
   Checkmate requires the king to be in check. In stalemate, the king isn’t in check, but its
   player has no legal move.

## Stalemate (lines 86 to 103)

14. Line 90: `| Identify by | Your turn, your king not in check and no legal move available. |`
15. Line 91: `| What | Stalemate is a position where the player to move has no legal move and isn’t in check. |`
16. Line 92: `| So what | Stalemate makes the game a draw, however many pieces the other side has. A player who was losing still gets half a point. |`

## Draw (lines 105 to 123)

17. Line 109: `| Identify by | A draw offer after a move, or the same position for the third time. |`
18. Line 110: `| What | A draw is a game that ends without a winner. A draw comes from agreement, stalemate, a position where nobody can checkmate, or a claim after repetition or fifty moves each without a pawn move or capture. |`
19. Line 111: `| So what | A draw gives each player half a point. The same position three times lets the player to move claim a draw. Under FIDE rules, five times ends the game in a draw. |`
20. Lines 122–123 (the paragraph, two lines): replace with these two lines:
   A handshake alone doesn’t state the result. One player may take it as a draw and the other
   as a resignation, so say the result in words.

## Resigning (lines 125 to 143)

21. Line 130: `| What | Resigning means giving up the game. The game ends as soon as you resign. |`
22. Line 131: `| So what | The other player wins when you resign. Under FIDE rules, if the other player couldn’t possibly checkmate, the result is a draw instead. |`
23. Lines 142–143 (the paragraph, two lines): replace with these two lines:
   Stopping both clocks doesn’t necessarily mean a player has resigned. Ask before you treat
   the game as over.

## How do you finish politely? (lines 145 to 158)

24. Line 147: `A few habits prevent confusion at the end of a game.`
25. Line 152: `> | Say “I adjust” first | On your turn, say it before you straighten a piece, so your opponent knows you aren’t moving it. |`
26. Line 153: `> | Offer a draw after moving | Make your move, offer the draw, then press your clock if you have one. The offer stands until your opponent accepts it, says no or touches a piece to move. |`
27. Line 154: `> | Resign clearly | Say “I resign” or tip over your king, so the result is clear. |`
28. Line 158: `After the handshake, share your thoughts about the game, whatever the result.`

## Check before you finish

- Every line not named above is unchanged, including the sources.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
