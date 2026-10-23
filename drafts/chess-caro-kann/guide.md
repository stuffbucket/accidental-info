---
title: The Caro-Kann for Black
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to a solid answer to 1.e4 that you can play as Black.
running_footer: The Caro-Kann for Black
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: friend@accidental.info · October 2026
collection: Games
collection_mark: diamond
number: 05
version: 0.3.0
---

# What is<br/>the Caro-Kann? {#why}

The Caro-Kann is a chess opening for Black that begins 1.e4 c6, usually followed by 2.d4
d5. The c-pawn move prepares …d5, which challenges White’s pawn on e4. The Caro-Kann is
known for being solid.

The Caro-Kann answers 1.e4 only. Against 1.d4, a simple start is 1…d5, as in An Accidental
Guide to: The First Move in Chess, which also explains the notation. An x is a capture, #
is checkmate and … marks a move by Black. Every board is seen from Black’s side, with the
a-file on your right.

You need four terms for the plan.

> | Term | Meaning |
> |---|---|
> | The light bishop | Black’s bishop that starts on c8 and moves on the light squares. |
> | Advance | White pushes the e-pawn to e5. |
> | Exchange | White swaps the e-pawn for your pawn on d5. |
> | Main line | White defends e4 with a knight, you take the pawn, and the knight takes back. |

# What does Black<br/>set up? {#fit}

```diagram
view black
board After 1.e4 c6 2.d4 d5 | rnbqkbnr/pp2pppp/2p5/3p4/3PP3/8/PPP2PPP/RNBQKBNR | The pawn on d5 challenges e4, and the bishop on c8 has an open road to f5.
mark Lb c8
arrow Lb c8 f5
arrow Ml d5 e4
```

White has three main choices on move 3. White can push the e-pawn to e5 in the Advance,
swap it on d5 in the Exchange, or defend it with a knight in the Main line, and you take
on e4. In each line, the light bishop comes out before …e6, then you bring
out your other pieces and castle.

# The light bishop {#entry num=01 mono=Lb}

```diagram
view black
board After 3.e5 Bf5 4.Nf3 e6 | rn1qkbnr/pp3ppp/2p1p3/3pPb2/3P4/5N2/PPP2PPP/RNBQKB1R | The bishop reached f5 before …e6, so the pawns on c6, d5 and e6 don’t block it.
mark Lb f5
```

| Field | Text |
|---|---|
| Identify by | Your bishop from c8 on f5 or g4, outside the pawns on c6, d5 and e6. |
| What | The light bishop is Black’s bishop that starts on c8. Bring it to f5 or g4 before you play …e6. |
| So what | A pawn on e6 would shut the bishop in. Once the bishop is out, play …e6, bring out your knights and castle. |

## Field marks

> | Field | Short answer |
> |---|---|
> | White plays | Any third move |
> | You play | Bishop out, then …e6 |

## Confused with: The French Defense

The Caro-Kann begins 1.e4 c6, which leaves the bishop’s road open. The French Defense begins
1.e4 e6, where the pawn can block the bishop on c8.

# Advance {#entry num=02 mono=Av}

```diagram
view black
board After 3.e5 | rnbqkbnr/pp2pppp/2p5/3pP3/3P4/8/PPP2PPP/RNBQKBNR | White’s pawn has reached e5. Move the bishop from c8 to f5 before playing …e6.
mark Av e5
arrow Av c8 f5
```

| Field | Text |
|---|---|
| Identify by | White’s e-pawn on e5, next to your pawn on d5. |
| What | The Advance is White pushing the e-pawn to e5, which gains space. |
| So what | The bishop comes out with 3…Bf5, before …e6 can block it. After …e6, your bishop on f8 supports …c5, which attacks White’s pawn on d4. |

## Field marks

> | Field | Short answer |
> |---|---|
> | White plays | 3.e5 |
> | You play | 3…Bf5, then …e6 and …c5 |

## Confused with: Exchange

The Advance moves White’s e-pawn forward to e5. The Exchange uses that pawn to capture on
d5 instead.

# Exchange {#entry num=03 mono=Ex}

```diagram
view black
board After 3.exd5 cxd5 4.Bd3 Nc6 5.c3 Nf6 6.Bf4 Bg4 | r2qkb1r/pp2pppp/2n2n2/3p4/3P1Bb1/2PB4/PP3PPP/RN1QK1NR | White’s bishop on d3 stops …Bf5, so your light bishop goes to g4 instead.
mark Ex g4
```

| Field | Text |
|---|---|
| Identify by | White’s e-pawn gone and your c-pawn on d5. |
| What | The Exchange is White swapping pawns with 3.exd5. Take back with 3…cxd5. |
| So what | Taking with the c-pawn frees c6 for your knight. If White plays 4.Bd3 to stop …Bf5, put the light bishop on g4 instead. |

## Field marks

> | Field | Short answer |
> |---|---|
> | White plays | 3.exd5 |
> | You play | 3…cxd5, then …Nc6 and …Nf6 |

## Confused with: The Panov Attack

The Exchange goes on quietly with 4.Bd3. The Panov Attack starts with 4.c4
instead, and White’s c-pawn then attacks your pawn on d5.

# Main line {#entry num=04 mono=Ml}

```diagram
view black
board After 3.Nc3 dxe4 4.Nxe4 Bf5 | rn1qkbnr/pp2pppp/2p5/5b2/3PN3/8/PPP2PPP/R1BQKBNR | Your bishop comes out to f5 and attacks the knight that took back on e4.
mark Ml f5
arrow Ml f5 e4
```

| Field | Text |
|---|---|
| Identify by | White’s knight on e4 after the pawns are exchanged. |
| What | The Main line is White defending e4 with a knight. After 3.Nc3 dxe4 4.Nxe4, play 4…Bf5. |
| So what | The bishop comes out and attacks the knight. After 5.Ng3 Bg6, White often pushes h4. Answer with …h6, so the bishop can drop back to h7. |

## Field marks

> | Field | Short answer |
> |---|---|
> | White plays | 3.Nc3 or 3.Nd2 |
> | You play | 3…dxe4, then 4…Bf5 |

## Confused with: 3.Nd2

Both 3.Nc3 and 3.Nd2 defend e4. After 3…dxe4 4.Nxe4 they usually reach the same
position.

# Which traps<br/>should you avoid? {#habits}

Three traps catch a natural-looking move.

> | Trap | Avoid it |
> |---|---|
> | 5.Qe2 and 6.Nd6 | If you play 4…Nd7 instead of 4…Bf5, meet 5.Qe2 with 5…Ndf6. After 5…Ngf6, 6.Nd6 is checkmate. |
> | h4 and h5 | In the Main line, play …h6 when White plays h4 against your bishop on g6. The bishop can then retreat to h7. |
> | h4 and g4 | In the Advance, answer 4.h4 with 4…h5. After 4…e6, White traps the bishop with 5.g4 Be4 6.f3 Bg6 7.h5. |

```diagram
view black
board After 4…Nd7 5.Qe2 Ngf6 6.Nd6# | r1bqkb1r/pp1npppp/2pN1n2/8/3P4/8/PPP1QPPP/R1B1KBNR | Checkmate. Your own pieces box in the king, and taking with the e7 pawn would open the e-file to White’s queen.
mark Ml d6
```

# Sources {#sources}

These public sources were checked on 22 October 2026.

| Source | Date | Address |
|---|---|---|
| Wikipedia, Caro–Kann Defence | October 2026 | en.wikipedia.org/wiki/Caro–Kann_Defence |
| Chess.com, Caro-Kann Defense | October 2026 | chess.com/openings/caro-kann-defense |
| Wikibooks, Chess Opening Theory: 1.e4 c6 and its pages | October 2026 | en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...c6 |
| Wikipedia, French Defence | October 2026 | en.wikipedia.org/wiki/French_Defence |
| Wikipedia, Smothered mate | October 2026 | en.wikipedia.org/wiki/Smothered_mate |
| Wikipedia, Closed Game | October 2026 | en.wikipedia.org/wiki/Closed_Game |
