---
title: The First Move in Chess
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to what to play first, as White or as Black.
running_footer: The First Move in Chess
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: friend@accidental.info · October 2026
collection: Games
collection_mark: diamond
number: 02
version: 0.4.0
---

# What should your<br/>first move be? {#why}

White moves first, then the players take turns. Start with a pawn in the middle of the
board, bring out your knights and bishops, then castle to put your king somewhere safer.
You don’t need to memorize a string of moves.

The first few moves have two jobs: get your pieces into the game quickly and get your king
safe. When you’re learning, a few principles help more than memorized sequences of moves,
because they work against whatever the other player does.

Center, development and castling cover most of what you need at the start.

> | Term | Meaning |
> |---|---|
> | Center | The four squares in the middle of the board. |
> | Development | Moving knights and bishops out so they can take part. |
> | Castling | One move of your king and a rook together. |

# How do you<br/>read the board? {#fit}

```diagram
board From White’s side | rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR | White moves first. The four tinted squares are the center. | white
mark Ce d4 d5 e4 e5
board From Black’s side | rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR | The same position. Files run h to a, and rank 8 is nearest. | black
mark Ce d4 d5 e4 e5
```

Each square has a letter and a number. From White’s side, the columns, called files, run
from a to h, left to right. The rows, called ranks, run from 1 to 8, going away from White.
Set it down so each player has a light square in the near right corner.

Pieces use K for king, Q for queen, R for rook, B for bishop and N for knight. A pawn move
is written as the square it lands on. Moves are numbered with White first, so 1.e4 e5 means
White’s pawn goes to e4, then Black’s pawn goes to e5. Black’s move alone is 1…e5. An x
means a capture, and # means checkmate.

# Center {#entry num=01 mono=Ce}

| Field | Text |
|---|---|
| Identify by | The four middle squares, d4, d5, e4 and e5. |
| What | The center is the four squares in the middle of the board. Start by moving the pawn in front of your king or queen two squares into it. |
| So what | A center pawn move frees your queen and a bishop to move. The center usually opens first, because center pawns often capture each other. |

## Field marks

> | Field | Short answer |
> |---|---|
> | When | On your first move |
> | Aim | A pawn in the middle |
> | Mistake | Too many pawn moves |

## Confused with: Pawn moves

One or two center pawn moves help your pieces get out. Too many early pawn moves leave your
knights and bishops at home.

# Development {#entry num=02 mono=Dv}

| Field | Text |
|---|---|
| Identify by | Knights and bishops leaving their starting squares. |
| What | Development is moving your knights and bishops out so they can take part. Try to move each piece once before moving it again. |
| So what | A lead in development gives you more pieces in the game than your opponent. Your opponent is trying to bring pieces out too. |

## Field marks

> | Field | Short answer |
> |---|---|
> | When | After a center pawn |
> | Aim | Knights and bishops out |
> | Mistake | Moving one piece twice |

## Confused with: Bringing out the queen

Bring your queen out after your knights and bishops. An early queen can be chased by
knights and bishops that your opponent wanted to develop anyway.

# Castling {#entry num=03 mono=Ca}

| Field | Text |
|---|---|
| Identify by | The king moves two squares and a rook moves past it. |
| What | Castling is one move of the king and a rook, written 0-0 on the king’s side or 0-0-0 on the queen’s side. The king moves two squares toward the rook, then the rook lands on the square the king crossed. |
| So what | Castling moves your king away from the center and brings a rook toward it. Castle early, after moving the pieces between your king and rook. |

## Field marks

> | Field | Short answer |
> |---|---|
> | When | Early in the game |
> | Aim | A safer king |
> | Mistake | Waiting too long |

## Confused with: Moving the king

An ordinary king move goes one square. To castle, neither the king nor that rook may have
moved, and no piece can stand between them. The king can’t castle out of check, and it can’t
cross or land on a square an enemy piece attacks. Move the king first, then the rook.

# What do you play,<br/>as White or Black? {#shown}

Pick the row for your color and the last move played.

> | Move | Why |
> |---|---|
> | 1.e4 | As White. The e-pawn moves two squares and frees the queen and a bishop to move. |
> | 1.d4 | As White. The same idea with the d-pawn. |
> | 1…e5 | As Black, after 1.e4. The e-pawn moves two squares, blocks White’s e-pawn and frees the queen and a bishop to move. |
> | 1…d5 | As Black, after 1.d4. The same idea with the d-pawn. |
> | 2.Nf3 Nc6 | White’s knight goes to f3 and Black’s knight goes to c6. Bishops come next. Each move brings one piece into the game. |
> | 0-0 | Castle on the king’s side once the knight and bishop between king and rook have moved. |

> [!WARNING]
> White’s queen and bishop can both attack f7, which only Black’s king defends at the start.
> The game 1.e4 e5 2.Bc4 Bc5 3.Qh5 Nf6 4.Qxf7# ends in checkmate. As Black, when White’s
> queen and bishop both aim at f7, defend f7 on your next move. Here, 3…Qe7 does it.

Then keep bringing out pieces you haven’t moved yet.

# Openings for White {#openings side=white}

Each board shows the position after both players have made four moves.

```diagram
column Standard lines
line Ruy Lopez | 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 | The bishop attacks e5’s defender.
line Italian Game | 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 | The bishop aims at f7 as c3 prepares d4.
line Queen’s Gambit Declined | 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 | Black keeps the pawn on d5.
column Lines to avoid
line Wayward Queen Attack | 1.e4 e5 2.Qh5 Nc6 3.Bc4 g6 4.Qf3 Nf6 | The early queen is chased, losing time.
line Grob’s Attack | 1.g4 d5 2.Bg2 Bxg4 3.c4 d4 4.Bxb7 Nd7 | White’s king side is loose after g4.
line Halloween Gambit | 1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Nxe5 Nxe5 | White gives a knight for one pawn.
```

# Openings for Black {#openings side=black}

Each board shows four moves by each player, drawn from Black’s side.

```diagram
column Standard lines
line Sicilian Defense | 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 | Black’s c-pawn takes White’s d-pawn.
line Caro-Kann Defense | 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 | The bishop moves before e6 blocks it.
line King’s Indian Defense | 1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 | Black lets White build a pawn center.
column Lines to avoid
line Damiano Defense | 1.e4 e5 2.Nf3 f6 3.Nxe5 fxe5 4.Qh5+ Ke7 | The f-pawn move exposes Black’s king.
line Latvian Gambit | 1.e4 e5 2.Nf3 f5 3.Nxe5 Qf6 4.d4 d6 | The f-pawn move weakens Black’s king.
line Englund Gambit | 1.d4 e5 2.dxe5 Nc6 3.Nf3 Qe7 4.Bf4 Qb4+ | Black gives a pawn to set a queen trap.
```

# Sources {#sources}

These public sources were checked on 22 October 2026.

| Source | Date | Address |
|---|---|---|
| FIDE, Laws of Chess | January 2023 | handbook.fide.com/chapter/E012023 |
| FIDE, Curriculum: Chess for Refugees | October 2023 | fide.com/docs/presentations/Curriculum%20Chess%20for%20Refugees.pdf |
| US Chess, Guide to Scholastic Chess, 11th edition | June 2021 | new.uschess.org/sites/default/files/media/documents/11th-edition-guide-to-scholastic-chess-6-29-21.pdf |
| Wikipedia, List of ECO codes and each opening’s article | October 2026 | en.wikipedia.org/wiki/List_of_ECO_codes |
| Lichess, opening explorer | October 2026 | lichess.org/opening |
