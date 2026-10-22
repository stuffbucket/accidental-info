# The Last Move in Chess: fidelity review

Checked `drafts/chess-last-move/guide.md`, version 0.1.0, against
`drafts/chess-last-move/notes/sources.md`. The raw pages were not kept in the repository, so
the excerpts in `sources.md` are the evidence. No other notes were read. Sources fetched
22 October 2026.

| Verdict | Count |
|---|---|
| Wrong | 2 |
| Overreach | 5 |
| Unsourced | 3 |
| Naming | 2 |
| Non-public | 0 |
| Stale | 0 |

Each verdict section runs from most to least serious.

## The two boards

Both positions are correct. The rendered boards on PDF p. 3 match the FEN in guide.md lines
35 and 37, the square colours are right (a1 dark, h1 light) and both kings are on legal,
non-adjacent squares.

| Board | Pieces | Check? | Black king’s squares | Result |
|---|---|---|---|---|
| Left, `7k/6Q1/6K1/8/8/8/8/8` | Black king h8, White queen g7, White king g6. The other 61 squares are empty. | Yes. The queen on g7 attacks h8 on the diagonal (FIDE 3.9.1). | g8 and h7 are attacked by the queen (h7 also by the king). Taking on g7 is illegal because the White king guards g7 (3.9.2). No other Black piece can capture or block. | Checkmate (1.4, 5.1.1) |
| Right, `7k/5Q2/6K1/8/8/8/8/8` | Black king h8, White queen f7, White king g6. The other 61 squares are empty. | No. The queen on f7 is a knight’s jump from h8, and the king on g6 doesn’t reach h8. | g8 is attacked by the queen on the diagonal. g7 and h7 are attacked by the queen along rank 7 and by the king. Black has no other piece. | Stalemate (5.2.1) |

The captions (lines 35 and 37) are accurate. The key line printed under the boards is
accurate on colours, but it lists the rook, bishop, knight and pawn, which neither board
shows. Suggested key: “K king, Q queen. White’s pieces are light, Black’s are dark.”

## Wrong

### W1. Stalemate is about the player, not the king (lines 43 to 44, p. 3)

**Guide:** “When you’re winning, make sure the other king still has a legal move unless you have checkmate.”

**Source** (FIDE Laws 5.2.1, https://handbook.fide.com/chapter/E012023): “The game is drawn when the player to move has no legal move and his/her king is not in check.”

**Verdict:** wrong. A king with no legal move isn’t stalemate while any other piece of that player can move. The advice teaches the commonest beginner mistake about stalemate.

**Corrected:** “When you’re winning, make sure your opponent still has a legal move, unless your move is checkmate.”

### W2. A position appearing again doesn’t draw (line 109, Draw)

**Guide:** “A draw offer after a move, or the same position appearing again.”

**Source** (FIDE Laws 9.2): “The game is drawn, upon a correct claim by a player having the move, when the same position for at least the third time”

**Verdict:** wrong. A second occurrence gives nothing. The third allows a claim.

**Corrected:** “A draw offer after a move, or the same position for the third time.”

## Overreach

### O1. Repetition and fifty moves don’t end the game on their own (lines 14 to 15 and 110)

**Guide:** “A draw can come from stalemate, agreement, a repeated position, fifty moves without a pawn move or capture, or a position where nobody can checkmate.” and “the rules can end the game because of stalemate, repetition, fifty moves each without a pawn move or capture, or a position where nobody can checkmate.”

**Source** (FIDE Laws 9.2 and 9.3.2 need “a correct claim”. 9.6.1 and 9.6.2 draw without a claim only at “at least five times” or “at least 75 moves … by each player”)

**Verdict:** overreach. Stalemate and a dead position end the game. Three repetitions and fifty moves only let a player claim. Line 15 also drops “each”, which line 110 and 9.3.2 (“by each player”) keep.

**Corrected line 14 to 16:** “A draw comes from agreement, stalemate or one of a few other rules.” (The list stays on the Draw page.)

**Corrected line 110:** “A draw is a game that ends without a winner. A draw comes from agreement, stalemate, a position where nobody can checkmate, or a claim after repetition or fifty moves each without a pawn move or capture.”

### O2. The resignation exception is FIDE’s (line 131, Resigning)

**Guide:** “If the other player couldn’t possibly checkmate from the position, the result is a draw instead.”

**Source** (FIDE Laws 5.1.2): “unless the position is such that the opponent cannot checkmate the player's king by any possible series of legal moves. In this case the result of the game is a draw.” US Chess 13B, as quoted: “The player whose opponent resigns wins the game.”

**Verdict:** overreach. Only the FIDE text gives the exception. The US Chess excerpt states no exception, so the guide should say whose rule it is.

**Corrected:** “The other player wins when you resign. Under FIDE rules, if the other player couldn’t possibly checkmate, the result is a draw instead.”

### O3. Five repetitions and “offer once” (line 111, Draw)

**Guide:** “The same position three times allows a claim, while five times makes the draw automatic. Offer a draw once, after making your move.”

**Source** (FIDE Laws 9.2, 9.6.1, and 11.5: “It is forbidden to distract or annoy the opponent … unreasonable offers of a draw”)

**Verdict:** overreach. The five-times rule is quoted only from FIDE. No source says “once”. FIDE forbids unreasonable offers. The claim belongs to the player whose turn it is. The offer advice repeats line 153, so cut it here.

**Corrected:** “A draw gives each player half a point. The same position three times lets the player to move claim a draw. Under FIDE rules, five times ends the game in a draw.”

### O4. Draw offer leaves out the clock (line 153, habits)

**Guide:** “Make one offer after your move.”

**Source** (FIDE Laws 9.1.2.1): “shall do so after having made a move on the chessboard and before pressing his/her clock.”

**Verdict:** overreach by omission. The rule has two halves, and a first rated game has a clock.

**Corrected:** “Make your move, offer the draw, then press your clock. The offer stands until your opponent accepts it, says no or touches a piece to move.”

### O5. Adjusting is only on your turn (line 152, habits)

**Guide:** “Say “I adjust” before straightening a piece on its square, so your opponent knows you aren’t moving it.”

**Source** (FIDE Laws 4.2.1): “Only the player having the move may adjust one or more pieces on their squares”

**Verdict:** overreach by omission. The row reads as if you may adjust at any time.

**Corrected:** “On your turn, say “I adjust” before straightening a piece, so your opponent knows you aren’t moving it.”

## Unsourced

### U1. Saying “check” aloud (line 50, Check)

**Guide:** “Check” said aloud, or a + written after the move.

**Verdict:** unsourced. No source says players announce check. Appendix C supports only the +. A new tournament player may wait for a word that never comes. Cut the spoken part, or add a source that covers it.

**Corrected:** “A piece attacking a king, or a + written after the move.”

### U2. Why a player stops the clocks (lines 142 to 143, Resigning)

**Guide:** “The player may be stopping the clocks to ask for help with a claim.”

**Verdict:** unsourced. The US Chess excerpt says only that stopping both clocks “does not necessarily indicate a resignation”. A source would need to cover pausing the clocks to call an arbiter (FIDE Article 6, which `sources.md` doesn’t quote). Cut it.

**Corrected:** “Stopping both clocks doesn’t necessarily mean a player has resigned. Ask before you treat the game as over.”

### U3. Skipping touch-move in casual games (line 158, habits)

**Guide:** “In a casual game, agree before you start if you won’t use touch-move.”

**Verdict:** unsourced, low. The only source on it, the US Chess scholastic guide, says to play touch-move “from the beginning”. As advice it can stay, but it needs plain words (see N2).

**Corrected:** “In a casual game, agree before you start whether a touched piece must move.”

## Naming

### N1. “Safe” for “not in check” (lines 28, 83 and 90)

**Guide:** “but the king is safe” (28), “the king is safe but its player has no legal move” (83), “your king safe” (90)

**Source** (FIDE 5.2.1 and US Chess 14A both say “not in check”)

**Verdict:** naming. The guide says “isn’t in check” on lines 37, 42 and 91, so it uses two names for one condition. A king that isn’t in check can still be in danger.

**Corrected:** line 28 “The player to move has no legal move, but that player’s king isn’t in check.” Line 83 “In stalemate, the king isn’t in check, but its player has no legal move.” Line 90 “Your turn, your king not in check and no legal move available.”

### N2. Terms used once without a definition (lines 79 and 158)

**Guide:** “The mating move” (79), “touch-move” (158)

**Verdict:** naming. Neither word appears elsewhere. The touch rule is called “Touch only the intended piece” on line 151.

**Corrected:** line 79 “The checkmating move”. Line 158 as in U3.

## Sources page

- Listed but not used: none. All four sources support at least one line. FIDE Laws supports the rules, US Chess Official Rules the handshake, clock and stalemate notes, the FIDE curriculum the blocking, handshake and pieces-back lines, and the US Chess scholastic guide touch-move and the draw offer.
- Used but not listed: none today. If the editor adds time losses (see the reader panel), add FIDE Laws Article 6 to `sources.md`. It is the same listed source, so the table doesn’t change.
- The table on lines 164 to 169 matches `sources.md` in titles, dates and addresses. On PDF p. 9, two long addresses break mid-word (“us-chess-rule / -book”, “11th-edition-gui / de-to”), so someone typing one in could get it wrong. That is a build issue, not a text one.
