# Edits, round 2: The Caro-Kann for Black

Apply these edits in place to `drafts/chess-caro-kann/guide.md` (your working directory's
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

A cold review (notes/review-1.md) found two wrong lines (…h6 gives the bishop h7, not "a
square behind h7", and "White often replies 5.Ng3 Bg6" gives Black's move to White), a trap
that starts from a move the guide never teaches (4…Nd7), a mate board where the pawn on e7
seems able to take the knight, "past your pawn" where the board shows the pawn beside d5,
claims with no source (the same plan works everywhere, a short plan instead of long lines),
notation and "develop" used without a word of explanation, and a sentence that talks about
the guide ("isn't covered here"). The printed guide is 1,136 words and must come down to
about 1,100.

## Front matter

1. Line 8: `version: 0.2.0`

## {#why} (lines 13 to 28)

2. Lines 13 to 15, replace all three lines with:
   The Caro-Kann is a chess opening for Black that begins 1.e4 c6, usually followed by 2.d4
   d5. The c-pawn move prepares …d5, which challenges White’s pawn on e4. The Caro-Kann is
   known for being solid.
3. Lines 17 to 19, replace all three lines with:
   The Caro-Kann answers 1.e4 only. Against 1.d4, a simple start is 1…d5, as in An Accidental
   Guide to: The First Move in Chess, which also explains the notation. An x is a capture, #
   is checkmate and … marks a move by Black. Every board is seen from Black’s side, with the
   a-file on your right.
4. Line 25: > | The light bishop | Black’s bishop that starts on c8 and moves on the light squares. |
5. Line 28: > | Main line | White defends e4 with a knight, you take the pawn, and the knight takes back. |

## {#fit} (lines 40 to 43)

6. Lines 40 to 43, replace all four lines with:
   White has three main choices on move 3. White can push the e-pawn to e5 in the Advance,
   swap it on d5 in the Exchange, or defend it with a knight in the Main line, where you take
   the pawn on e4 anyway. In each line, the light bishop comes out before …e6, then you bring
   out your other pieces and castle.

## The light bishop (lines 49 to 57)

7. Line 49, change only the caption after the last `|` to:
   The bishop reached f5 before …e6, so the pawns on c6, d5 and e6 don’t block it.
8. Line 55: | Identify by | Black’s bishop from c8 on f5 or g4, in front of the pawns on c6, d5 and e6. |
9. Line 57: | So what | A pawn on e6 would shut the bishop in. With the bishop out, play …e6, bring out your knights and castle. |

## Advance (lines 83 to 84)

10. Line 83: | What | The Advance is White pushing the e-pawn to e5 with 3.e5. The pawn takes more space and closes the center. |
11. Line 84: | So what | The bishop comes out with 3…Bf5, before …e6 can block it. After …e6, your bishop on f8 supports …c5, which attacks White’s pawn on d4. |

## Exchange (lines 110 to 122)

12. Line 110: | So what | The c-pawn leaves c6 open for your knight. When White plays 4.Bd3 to stop …Bf5, bring out your knights and put the light bishop on g4 instead. |
13. Lines 121 to 122, replace both lines with:
   The Exchange goes on quietly when White plays 4.Bd3. The Panov Attack starts with 4.c4
   instead, and White’s c-pawn then attacks your pawn on d5.

## Main line (lines 136 to 149)

14. Line 136: | What | The Main line is White defending e4 with a knight. After 3.Nc3 dxe4 4.Nxe4, play 4…Bf5. |
15. Line 137: | So what | The bishop comes out and attacks the knight on e4. White often replies 5.Ng3, the bishop drops back to g6, and White pushes h4. Answer h4 with …h6, so the bishop can drop back to h7. |
16. Lines 148 to 149, replace both lines with:
   Both 3.Nc3 and 3.Nd2 defend e4. After 3…dxe4 4.Nxe4 they usually reach the same
   position.

## {#habits} (lines 153 to 167)

17. Line 153: Three early traps catch a natural-looking move.
18. Line 157: > | 5.Qe2 and 6.Nd6 | If you play 4…Nd7 instead of 4…Bf5, meet 5.Qe2 with 5…Ndf6. After 5…Ngf6, 6.Nd6 is checkmate. |
19. Line 163, change only the caption after the last `|` to:
   The knight on d6 gives checkmate. Your own pieces box in the king, and the pawn on e7 can’t take the knight, because that would open the e-file to White’s queen on e2.
20. Line 167: When White pushes the h-pawn toward your bishop, answer with your own h-pawn: …h6 in the Main line and …h5 in the Advance.

## Check before you finish

- Every line not named above is unchanged.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
