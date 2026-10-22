# Edits, round 2: Stopping Scholar’s Mate

Apply these edits in place to `drafts/chess-scholars-mate/guide.md` (your working directory's
`./guide.md`). Line numbers are from the file as it is now (version 0.1.0, after round 1).
Replace each listed line or line range with the new text, keeping the table row structure:
label cells stay as they are unless the edit gives a new label. Change nothing else. Don't
touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md` and
`packages/editorial/skills/accidental-guide-write/references/voice.md` first. Every rule there
applies to any text you write or shorten.

## Why

A cold review (notes/review-1.md) found one wrong claim (Qh5 is still legal after 2…Nf6; it
just loses the queen), two overreaches (…Nd4 works because d4 is undefended; "h5 or f3" on
move 2 or 3 isn't in the sources), undefined words (develop, fork, tempi), field marks that
read as if the pieces stand on f7, and two sentences that talk about the guide itself. The
printed guide is 1,115 words and must come down to about 1,100.

## Front matter

1. Line 8: `version: 0.2.0`

## {#why} (lines 13 to 28)

2. Lines 17 to 19, replace all three lines with:
   Moves are written in algebraic notation, explained in An Accidental Guide to: The First
   Move in Chess. You play Black, and every board is shown from your side, with the a-file on
   your right.
3. Line 21: delete the line, and the blank line after it, so the table follows the paragraph
   ending "on your right."
4. Line 26: > | The early queen | White’s queen brought out in the first few moves, often to h5. |

## {#fit} (lines 40 to 43)

5. Lines 40 to 43, replace all four lines with:
   Black is to move. White threatens Qxf7#, the queen taking on f7 with checkmate. Your king
   is the only piece defending f7, and it can’t take the queen there because the bishop on c4
   guards her. Your next move must guard f7 or block one of those lines.

## The f7 square (lines 49 to 69)

6. Line 49, change only the caption after the last `|` to:
   3…Nf6 doesn’t guard f7, so the queen takes there. The bishop stops your king taking her, and every other square is blocked.
7. Line 64: > | Watch for | Queen and bishop aimed at f7 |

## The early queen (lines 83 to 85)

8. Line 83: | Identify by | White’s queen out in the first few moves, often on h5. |
9. Line 84: | What | The early queen is White’s queen brought out before most other pieces, as in 2.Qh5, the Wayward Queen Attack. From h5, the queen attacks e5 and f7. |

## Guarding f7 (lines 112 to 124)

10. Line 112: | So what | White can aim at f7 again with 4.Qf3. Play 4…Nf6 to block that line, then …Bg7 and castling. Keep the knight on f6 while the queen aims at f7. |
11. Line 118: > | Watch for | Queen and bishop both aimed at f7 |
12. Lines 123 to 124, replace both lines with:
   The move 3…Nf6 brings out a knight and attacks the queen. The move loses here because it
   blocks neither line, so 4.Qxf7# follows.

## Tempo (lines 130 to 151)

13. Line 130, change only the caption after the last `|` to:
   The knight on d4 attacks the queen on f3 and threatens Nxc2, which would attack the king on e1 and the rook on a1.
14. Line 138: | Identify by | A move that brings out a piece and attacks the queen. |
15. Line 139: | What | A tempo is one move’s worth of time. A move that attacks a piece and makes it move again gains a tempo. |
16. Line 140: | So what | With d4 undefended, 5…Nd4 attacks the queen and threatens Nxc2, which would attack White’s king and rook at once. White’s best answer is Qd1, and you continue with …Bg7 and castling. |
17. Line 147: > | Your answer | Bring out a piece with a threat |
18. Line 151: A tempo counts moves, not minutes.

## {#shown} (lines 155 to 163)

19. Line 155: Find White’s last move, then play the reply beside it.
20. Line 162: > | 5.Nc3 Nd4 | If White leaves d4 undefended, attack the queen and threaten Nxc2, which would attack the king and rook at once. |
21. Line 163: > | 2.Bc4 Nf6 | Bring out your king’s knight before the queen reaches h5, so Qh5 loses the queen to Nxh5. |

## Check before you finish

- Every line not named above is unchanged.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
