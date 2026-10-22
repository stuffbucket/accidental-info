# The Last Move in Chess: reader panel

Reviewed: `drafts/chess-last-move/guide.md`, version 0.1.0, and its 9-page PDF built
22 October 2026. Each page was read as three readers with no access to the sources:

- **Casual.** An adult who knows how the pieces move and plays at home or online. Wants to know whether the game is over and who won.
- **Club.** A club player who checks that nothing is wrong or misleading under FIDE or US Chess rules.
- **Teen.** A teenager about to play a first rated tournament game, with a clock and a scoresheet.

The voice pass checks the guide against the review skill’s `checklist.md`. `lint_guide.py`
was not run, because this review was limited to the listed files.

## Top fixes

Most serious first.

**1. The stalemate advice is wrong.**
Page 3, lines 43 to 44: “When you’re winning, make sure the other king still has a legal move unless you have checkmate.” The Club reader stops. Stalemate needs the whole side to have no legal move, not only the king. The Casual reader learns the commonest beginner mistake from this sentence.
Rewrite lines 43 to 44: “When you’re winning, make sure your opponent still has a legal move, unless your move is checkmate.”

**2. Repetition and fifty moves read as automatic.**
Page 2, lines 14 to 15: “A draw can come from … a repeated position, fifty moves without a pawn move or capture”. Page 6, line 109: “the same position appearing again”. Line 110: “the rules can end the game because of … repetition, fifty moves each”. The Teen will expect the game to stop by itself, or will claim after the second repetition. The Club reader knows both need a claim, and line 15 drops “each”.
Rewrite lines 14 to 16: “A draw comes from agreement, stalemate or one of a few other rules.”
Rewrite line 109: “A draw offer after a move, or the same position for the third time.”
Rewrite line 110: “A draw is a game that ends without a winner. A draw comes from agreement, stalemate, a position where nobody can checkmate, or a claim after repetition or fifty moves each without a pawn move or capture.”

**3. Time is missing.**
Page 2, line 13: “You win by checkmate, or when the other player resigns.” The Teen’s game has a clock, and running out of time is a common way to lose a rated game. The Club reader reads this as a complete list and sees the gap. The fix needs FIDE Article 6 added to `sources.md`.
Rewrite line 13: “A chess game ends in a win or a draw. You win by checkmate, or when the other player resigns. In a game with clocks, a player who runs out of time usually loses.”

**4. The draw offer leaves out the clock.**
Page 8, line 153: “Make one offer after your move.” The Teen needs the order: move, offer, then press the clock.
Rewrite line 153: “Make your move, offer the draw, then press your clock. The offer stands until your opponent accepts it, says no or touches a piece to move.”

**5. “Check” said aloud isn’t something to wait for.**
Page 4, line 50: “Check” said aloud, or a + written after the move. In a rated game the opponent may say nothing. The Teen could miss a check while waiting to hear it.
Rewrite line 50: “A piece attacking a king, or a + written after the move.”

**6. FIDE-only rules are stated as universal.**
Page 7, line 131: “If the other player couldn’t possibly checkmate from the position, the result is a draw instead.” Page 6, line 111: “five times makes the draw automatic.” The Club reader checking US Chess rules asks whose rule this is.
Rewrite line 131: “The other player wins when you resign. Under FIDE rules, if the other player couldn’t possibly checkmate, the result is a draw instead.”
Rewrite line 111: “A draw gives each player half a point. The same position three times lets the player to move claim a draw. Under FIDE rules, five times ends the game in a draw.”

**7. The checkmate board doesn’t say why the king can’t take the queen.**
Page 3, line 35: “The king on h8 is in check and has no legal move.” The Casual reader’s first thought is Kxg7. Nothing on the page says the White king guards g7. On the right board, the caption doesn’t say why Black has no move.
Rewrite line 35 caption: “Black to move. The queen gives check, and the white king guards the queen.”
Rewrite line 37 caption: “Black to move. The king isn’t in check, and every square next to it is attacked.”

**8. Adjusting is only allowed on your turn.**
Page 8, line 152: “Say “I adjust” before straightening a piece on its square”. The Teen may adjust on the opponent’s time.
Rewrite line 152: “On your turn, say “I adjust” before straightening a piece, so your opponent knows you aren’t moving it.”

**9. “Safe” and “not in check” are used for the same thing.**
Lines 28, 83 and 90 say “safe”. Lines 37, 42 and 91 say “isn’t in check”. The Casual reader can take “safe” to mean “not threatened”, which is a different idea.
Rewrite line 28: “The player to move has no legal move, but that player’s king isn’t in check.”
Rewrite line 83: “Checkmate requires the king to be in check. In stalemate, the king isn’t in check, but its player has no legal move.”
Rewrite line 90: “Your turn, your king not in check and no legal move available.”

**10. “Touch-move” appears once, undefined.**
Page 8, line 158: “agree before you start if you won’t use touch-move.” The row on line 151 never uses the word.
Rewrite line 158: “In a casual game, agree before you start whether a touched piece must move.”

**11. The clock row guesses at a reason.**
Page 7, lines 142 to 143: “The player may be stopping the clocks to ask for help with a claim.” The Casual reader has no clock, and the Teen doesn’t know who gives “help”.
Rewrite lines 142 to 143: “Stopping both clocks doesn’t necessarily mean a player has resigned. Ask before you treat the game as over.”

## Cuts for the word budget

These cost the reader least. The table saves about 125 printed words. The other fixes above
add about 15 back, so the net saving is about 110. Fix 3 adds 13 more, so make it only if
the budget allows.

| Where | Cut or rewrite | Words saved |
|---|---|---|
| Lines 14 to 16 | As in fix 2. The list stays on the Draw page, and line 22 below covers check. | 19 |
| Lines 41 to 44 | “Black has no legal move on either board. The left board is checkmate, so White wins. The right board is stalemate, so the game is a draw. When you’re winning, make sure your opponent still has a legal move, unless your move is checkmate.” The captions in fix 7 give the reasons. | 18 |
| Line 71 | Keep only “Checkmate is check with no legal way out.” The three ways out are on line 52, on the same page. | 18 |
| Line 51 | Keep only “Check means the king is attacked by an enemy piece.” Line 58 says the game goes on. | 10 |
| Line 130 | “Resigning means giving up the game.” Line 19 already says the game ends at once. | 10 |
| Diagram key | “K king, Q queen. White’s pieces are light, Black’s are dark.” Only kings and queens are drawn. | 9 |
| Lines 142 to 143 | As in fix 11. | 6 |
| Line 110 | As in fix 2. | 6 |
| Line 18 | “A win scores one point, a draw half a point each and a loss none.” | 6 |
| Line 91 | Cut “The game ends at once.” | 5 |
| Lines 19 to 20 | “The game ends as soon as checkmate, stalemate or a resignation happens, so nobody captures the king.” | 4 |
| Line 147 | “A few habits prevent confusion at the end of a game.” | 4 |
| Line 154 | “Say “I resign” or tip over your king, so the result is clear.” | 4 |
| Line 156 | “Set up the pieces again after the game.” | 4 |
| Line 155 | “A handshake shows respect. Say the result as well.” | 2 |

If the table shape may change, the “Say “I adjust” first” row (line 152) is the least
end-of-game row and saves 22 more.

## Page by page

| Page | Reader | Stops at | Why |
|---|---|---|---|
| 2 | Teen | “You win by checkmate, or when the other player resigns.” (13) | No word about the clock (fix 3). |
| 2 | Club | “a repeated position, fifty moves” (14 to 15) | Both need a claim, and the fifty moves are by each player (fix 2). |
| 2 | Casual | “These five terms tell you whether the game continues and how it ends.” (22) | Talks about the table, not the game (voice pass). |
| 3 | Casual | “The king on h8 is in check and has no legal move.” (35) | Why can’t the king take the queen? (fix 7) |
| 3 | Club | “the other king still has a legal move” (43) | Wrong rule (fix 1). |
| 3 | Casual | Blue square on h8, both boards (PDF only) | The key doesn’t say what blue means. The captions name h8, so it’s minor. Add “The blue square is the king to move.” to the key, or drop the mark lines 36 and 38. |
| 4 | Teen | “Check” said aloud (50) | Fix 5. |
| 4 | Casual | “The mating move” (79) | “Mating” is never defined. Rewrite: “The checkmating move”. |
| 5 | Casual | “your king safe” (90) | Fix 9. |
| 6 | Teen | “the same position appearing again” (109) | Fix 2. |
| 6 | Club | “five times makes the draw automatic” (111) | FIDE only (fix 6). |
| 7 | Club | “the result is a draw instead” (131) | FIDE only (fix 6). |
| 7 | Casual | “to ask for help with a claim” (143) | Fix 11. |
| 8 | Teen | “Make one offer after your move.” (153) | Fix 4. |
| 8 | Casual | “touch-move” (158) | Fix 10. |

Pages 1 and 9: no stops. The cover page numbers match the entries.

## Voice pass

No row sentence starts with “It”, “Its”, “They” or “This”. No em dashes, semicolons or
straight apostrophes were found.

| Line | Text | Rule | Rewrite |
|---|---|---|---|
| 22 | “These five terms tell you whether the game continues and how it ends.” | Nothing about the guide itself | “Check is the only one of these that doesn’t end the game.” |
| 15 to 16 | “Check is a warning, not the end.” | “Not X but Y” flourish, and “warning” is used nowhere else | Delete. Line 22, rewritten, says it plainly. |
| 130 | “Resigning means ending the game by conceding it.” | Defined with a synonym | “Resigning means giving up the game.” |
| 122 to 123 | “so say what you mean.” | Ends on a phrase, not the action | “so say the result in words.” |

## Verdict

All three readers would finish the guide. It is short, and the checkmate and stalemate
boards are right. The Casual reader would leave with a wrong stalemate rule (line 43) unless
fix 1 is made. The Teen would leave without the clock, which shapes a first rated game more
than any other rule here (fixes 3 and 4). The Club reader would accept the guide once the
claim rules and the FIDE-only rules say what they are.
