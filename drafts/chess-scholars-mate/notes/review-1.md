# Review 1: fidelity, reader panel, format leakage

Boards: all five match their move captions square by square from Black’s side, and the arrows are correct. Board 2 is mate. On board 5, c2 is undefended. The L17 cross-reference was not checked.

## Findings, most serious first

1. **L162, L140 (Overreach, reader risk).** “5.Nc3 Nd4 | Attack the queen…” and “White’s queen retreats to d1”. Wikibooks marks 5.Nc3 as a mistake (“if White doesn’t defend d4, instead playing 5. Nc3?”), and Qd1 is the best reply, not the only one. Readers will try …Nd4 after any fifth move.
   L162: “| 5.Nc3 Nd4 | If White leaves d4 undefended, attack the queen and threaten Nxc2, which forks the king and rook. |”
   L140: “White’s best answer is Qd1, and you continue with …Bg7 and castling.”

2. **L112 (reader risk, sourced).** “Play 4…Nf6 to block that line, then prepare …Bg7 and castling.” Wikibooks says the f6 knight is pinned (Qxf7# if it moves). The guide never warns of this.
   Rewrite: “Play 4…Nf6 to block that line, then …Bg7 and castling. Keep the knight on f6 while the queen aims at f7.”

3. **L163 (Wrong).** “so Qh5 is no longer possible.” Qh5 stays legal. The knight on f6 just takes the queen there.
   Rewrite: “Bring out your king’s knight before the queen reaches h5, so Qh5 loses the queen to Nxh5.”

4. **L26, L83 (Unsourced).** “usually to h5 or f3” and “on h5 or f3”. No source has Qf3 on move 2 or 3, or says “usually”.
   L26: “White’s queen brought out on move 2 or 3, often to h5.”
   L83: “White’s queen out on move 2 or 3, often on h5.”

5. **L84 (Overreach, Naming).** “brought out before the other pieces, often in the Wayward Queen Attack or Danvers Opening.” In the 2.Bc4 order the bishop comes first. Both names belong to one opening, and “or” makes them sound like two.
   Rewrite: “The early queen is White’s queen brought out before most other pieces, as in 2.Qh5, the Wayward Queen Attack. From h5, the queen attacks e5 and f7.”

6. **L49 (Overreach, reader).** “The bishop guards her, so your king has no way out.” The bishop only stops the king taking. The reader also doesn’t learn until page 6 that 3…Nf6 was the mistake.
   Rewrite: “3…Nf6 doesn’t guard f7, so the queen takes there. Your king can’t take her because the bishop guards her, and every other square is blocked or attacked.”

7. **L123, L138, L147, L140 (reader, undefined terms).** “develops”, “Develop” and “forking” are never explained. The guide says “bring out” elsewhere.
   L123: “The move 3…Nf6 brings out a knight and attacks the queen. The move loses here because it doesn’t block either line, so 4.Qxf7# follows.”
   L138: “A move that brings out a piece and attacks the queen.”
   L147: “Bring out a piece with a threat”
   L140, first sentence: “The move 5…Nd4 attacks the queen and threatens Nxc2, a fork that attacks White’s king and rook at once.”

8. **L130 (reader).** “also threatens the pawn on c2.” The arrow ends on a pawn, and the caption never mentions the fork.
   Rewrite: “The knight on d4 attacks the queen on f3 and threatens Nxc2, which would attack the king on e1 and the rook on a1.”

9. **L64, L118 (reader).** “Queen and bishop on f7” and “Both attackers on f7” read as if the pieces stand on f7.
   L64: “Queen and bishop aimed at f7”
   L118: “Queen and bishop both aimed at f7”

10. **L18–19 (reader).** “Your pieces are nearest you” assumes the reader plays Black, which the guide never says.
    Rewrite: “You play Black, and every board is shown from your side, with the a-file on your right.”

11. **L40 (reader).** “White threatens Qxf7#, and the game ends if the queen takes the pawn.” This is the first “x” and “#”, and a casual reader may not know either.
    Rewrite: “White threatens Qxf7#, the queen taking on f7 with checkmate.”

12. **L155 (SN, reader).** “Use the row that matches White’s move order and the last move played.” This talks about the table, and “move order” is unclear because the 2.Bc4 row comes last.
    Rewrite: “Find White’s last move, then play the reply beside it.”

## Format leakage and mannered prose

13. **L21 (SN).** “Four parts explain what to watch and what to play.” Describes the guide. Cut it.

14. **L17 (SN, minor).** “Moves here use algebraic notation, which is explained in…”
    Rewrite: “Moves are written in algebraic notation, explained in An Accidental Guide to: The First Move in Chess.”

15. **L151 (MP, filler).** “The clock doesn’t change how many tempi a move gains.” Adds nothing, and “tempi” is unexplained. Cut it.

16. **L60, L87, L114, L144 (BF).** “Field marks” is bird-guide vocabulary. It looks like a series label, so raise it at series level.

Otherwise clean: no rhetorical questions, em dashes, unnamed voices or rows starting with It, Its, They or This. L165 ends on a fact.

## Sentences that can be cut

| Line | Text | Words saved |
|---|---|---|
| 21 | “Four parts explain what to watch and what to play.” | 10 |
| 42 | “First, see where the queen’s line and bishop’s line meet.” The arrows already show this. | 10 |
| 151 | “The clock doesn’t change how many tempi a move gains.” | 10 |
| 18–19 | Finding 10 rewrite, in place of two sentences | 5 |

About 35 words, enough for the overrun plus findings 1 and 2.
