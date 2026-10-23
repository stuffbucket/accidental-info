---
title: Stopping Scholar’s Mate
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to spotting the four-move checkmate, and making it backfire.
running_footer: Stopping Scholar’s Mate
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: friend@accidental.info · October 2026
version: 0.2.0
---

# What is<br/>Scholar’s Mate? {#why}

Scholar’s Mate is a quick checkmate where White’s queen and bishop both aim at f7, then the
queen captures there. The attack is easy to stop once you see both pieces lining up. After
you stop it, White has usually wasted moves bringing the queen out early.

Moves are written in algebraic notation, explained in An Accidental Guide to: The First
Move in Chess. You play Black, and every board is shown from your side, with the a-file on
your right.

> | Term | Meaning |
> |---|---|
> | The f7 square | The pawn square beside Black’s king that only the king defends at the start. |
> | The early queen | White’s queen brought out in the first few moves, often to h5. |
> | Guarding f7 | A move that defends f7 or blocks an attacker’s line to it. |
> | Tempo | One move’s worth of time. |

# What does the<br/>attack look like? {#fit}

```diagram
view black
board After 1.e4 e5 2.Qh5 Nc6 3.Bc4 | r1bqkbnr/pppp1ppp/2n5/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR | The queen on h5 and bishop on c4 both aim at f7 beside your king.
mark Fs f7
arrow Fs h5 f7
arrow Fs c4 f7
```

Black is to move. White threatens Qxf7#, the queen taking on f7 with checkmate. Your king
is the only piece defending f7, and it can’t take the queen there because the bishop on c4
guards her. Your next move must guard f7 or block one of those lines.

# The f7 square {#entry num=01 mono=Fs}

```diagram
view black
board After 3…Nf6 4.Qxf7# | r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR | 3…Nf6 doesn’t guard f7, so the queen takes there. The bishop stops your king taking her, and every other square is blocked.
mark Fs f7
arrow Fs c4 f7
```

| Field | Text |
|---|---|
| Identify by | White’s queen and bishop both aimed at f7. |
| What | The f7 square is the pawn square beside your king that only your king defends at the start. The queen can take there with checkmate when the bishop guards her. |
| So what | Watch f7 as soon as White’s queen or bishop points toward it. If both pieces attack it, your next move must stop the mate. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Watch for | Queen and bishop aimed at f7 |
> | Your answer | Guard f7 now |

## Confused with: f2

The f2 square is White’s matching weak square. Only White’s king defends f2 at the start.

# The early queen {#entry num=02 mono=Qn}

```diagram
view black
board After 1.e4 e5 2.Qh5 | rnbqkbnr/pppp1ppp/8/4p2Q/4P3/8/PPPP1PPP/RNB1KBNR | The queen on h5 attacks your e5 pawn and looks along the diagonal toward f7.
mark Qn h5
arrow Qn h5 e5
arrow Qn h5 f7
```

| Field | Text |
|---|---|
| Identify by | White’s queen out in the first few moves, often on h5. |
| What | The early queen is White’s queen brought out before most other pieces, as in 2.Qh5, the Wayward Queen Attack. From h5, the queen attacks e5 and f7. |
| So what | The first threat after 2.Qh5 is Qxe5+, not checkmate on f7. Play 2…Nc6 to defend e5 while bringing out your knight. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Watch for | Queen on h5 |
> | Your answer | 2…Nc6 |

## Confused with: A strong attack

An early queen can look dangerous, but White gains nothing if you meet each threat. Your
knights and pawns can chase the queen while you bring pieces out.

# Guarding f7 {#entry num=03 mono=Gu}

```diagram
view black
board After 3…g6 | r1bqkbnr/pppp1p1p/2n3p1/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR | The pawn on g6 blocks the queen’s line to f7 and attacks the queen on h5.
mark Gu g6
arrow Gu g6 h5
```

| Field | Text |
|---|---|
| Identify by | A move that defends f7 or blocks an attacker’s line to it. |
| What | Guarding f7 means stopping the queen from taking there with checkmate. After 3.Bc4, 3…g6 blocks the queen’s line and makes her move. |
| So what | White can aim at f7 again with 4.Qf3. Play 4…Nf6 to block that line, then …Bg7 and castling. Keep the knight on f6 while the queen aims at f7. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Watch for | Queen and bishop both aimed at f7 |
> | Your answer | 3…g6 or 3…Qe7 |

## Confused with: 3…Nf6

The move 3…Nf6 brings out a knight and attacks the queen. The move loses here because it
blocks neither line, so 4.Qxf7# follows.

# Tempo {#entry num=04 mono=Te}

```diagram
view black
board After 4.Qf3 Nf6 5.Nc3 Nd4 | r1bqkb1r/pppp1p1p/5np1/4p3/2BnP3/2N2Q2/PPPP1PPP/R1B1K1NR | The knight on d4 attacks the queen on f3 and threatens Nxc2, which would attack the king on e1 and the rook on a1.
mark Te d4
arrow Te d4 f3
arrow Te d4 c2
```

| Field | Text |
|---|---|
| Identify by | A move that brings out a piece and attacks the queen. |
| What | A tempo is one move’s worth of time. A move that attacks a piece and makes it move again gains a tempo. |
| So what | With d4 undefended, 5…Nd4 attacks the queen and threatens Nxc2, hitting White’s king and rook at once. After Qd1, continue with …Bg7 and castling. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Watch for | A useful attack on the queen |
> | Your answer | Bring out a piece with a threat |

## Confused with: Time on the clock

A tempo counts moves, not minutes.

# What do you play<br/>against it? {#shown}

Find White’s last move, then play the reply beside it.

> | Move | Why |
> |---|---|
> | 2.Qh5 Nc6 | Defend e5 and bring out your queen’s knight. |
> | 3.Bc4 g6 | Block the queen’s line and attack her. 3…Qe7, which guards f7, is also safe. |
> | 4.Qf3 Nf6 | Block the queen’s new line to f7 and bring out your king’s knight. |
> | 5.Nc3 Nd4 | With d4 undefended, attack the queen and threaten Nxc2. |
> | 2.Bc4 Nf6 | Bring out your king’s knight before the queen reaches h5, so Qh5 loses the queen to Nxh5. |

Then keep bringing out your pieces and castle. White’s early queen moves have cost time.

# Sources {#sources}

These public sources were checked on 22 October 2026.

| Source | Date | Address |
|---|---|---|
| Wikipedia, Scholar’s mate | October 2026 | en.wikipedia.org/wiki/Scholar%27s_mate |
| Wikipedia, Danvers Opening | October 2026 | en.wikipedia.org/wiki/Danvers_Opening |
| Wikipedia, Tempo (chess) | October 2026 | en.wikipedia.org/wiki/Tempo_(chess) |
| Wikibooks, Chess Opening Theory, 1.e4 e5 2.Qh5 | October 2026 | en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...e5/2._Qh5 |
| Chess.com, Scholar’s Mate | October 2026 | chess.com/terms/scholars-mate-chess |
| Chess.com, Tempo | October 2026 | chess.com/terms/tempo-chess |
