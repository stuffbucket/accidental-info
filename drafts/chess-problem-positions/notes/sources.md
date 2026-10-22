# Sources for An Accidental Guide to… Getting Out of Trouble in Chess

All fetched 22 October 2026 with curl (Wikipedia as raw wikitext through `action=raw`,
Chess.com and FIDE as HTML, tags stripped). Raw files were kept outside the repository, in
`/tmp/ppsrc/`. Excerpts are verbatim and short. Public material only: FIDE (the
international chess federation), Wikipedia articles (with the sources they cite noted) and
Chess.com's public Chess Terms pages. Nothing internal.

How Wikipedia was read: the raw wikitext, so excerpts below drop link and template markup
(`[[...]]`, `{{chessgloss|...}}`) but keep the words. The page date is the last revision
timestamp from the Wikipedia API on 22 October 2026.

## 1. Pin

Wikipedia, "Pin (chess)". <https://en.wikipedia.org/wiki/Pin_(chess)>
Page date: last revised 27 May 2026. Cites Hooper and Whyld, The Oxford Companion to Chess
(1996), p. 308.

- Definition: "a pin is a tactic in which a defending piece cannot move out of an attacking
  piece's line of attack without exposing a more valuable defending piece."
- Who pins: "Only a piece that can move any number of squares along a horizontal, vertical,
  or diagonal line (i.e. a bishop, rook, or queen) can pin. Any piece can be pinned except
  the king."
- Absolute pin: "An absolute pin is one where the piece shielded by the pinned piece is the
  king. In this case it is illegal to move the pinned piece out of the line of attack, as
  that would place one's king in check"
- Relative pin: "Moving such a pinned piece is legal but may not be prudent, as the shielded
  piece would then be vulnerable to capture"
- Ways out ("Unpinning" section): "Breaking a pin is called unpinning. This can be done in a
  number of ways: the piece creating the pin can be captured or chased away; another unit
  can be moved to block the line of the pin; the unit to which a piece is pinned can be
  moved; or, a relatively pinned piece can move despite the pin"

Chess.com, "Pin" (Chess Terms). <https://www.chess.com/terms/pin-chess>
Page date: none given.

- Absolute pin: "It happens when a piece is covering an attack on the king . Since it is
  illegal to make a move that would put your king in check , the pinned piece literally
  cannot move."
- Relative pin: "although moving the pinned piece is not illegal, it is not desirable."
- Ways out: "The first one is by capturing the piece that is pinning your forces. Another
  way of unpinning your piece is by blocking the attack with another piece of yours. You can
  also free yourself from a pin by moving the threatened piece from behind your pinned
  piece. Finally, you can neutralize a pin by creating an even stronger pin"

FIDE, Laws of Chess (from 1 January 2023). <https://handbook.fide.com/chapter/E012023>

- Why an absolute pin can't move, 3.9.2: "No piece can be moved that will either expose the
  king of the same colour to check or leave that king in check."
- 3.9.1: "The king is said to be 'in check' if it is attacked by one or more of the
  opponent's pieces, even if such pieces are constrained from moving to the square occupied
  by the king because they would then leave or place their own king in check."

## 2. Fork

Wikipedia, "Fork (chess)". <https://en.wikipedia.org/wiki/Fork_(chess)>
Page date: last revised 8 July 2026. Cites Lichess practice "The Fork", Chess.com "Fork in
Chess" and Hooper and Whyld (1996), p. 143.

- Definition: "a fork is a tactic in which a piece attacks multiple enemy pieces
  simultaneously. The attacker usually aims to capture one of the forked pieces. The
  defender often cannot counter every threat."
- Forcing: "A fork is most effective when it is forcing, such as when the king is put in
  check."
- Knight fork: "a fork by a knight is a knight fork."
- Why knights: "knights are particularly effective as the forking piece because they cannot
  be captured by the non-knight pieces they attack, and as a minor piece they are less
  valuable than rooks and queens."
- Royal fork: "A fork of the king and queen, the highest material-gaining fork possible, is
  sometimes called a royal fork."
- Lead diagram caption: "The white knight forks Black's king and rook."

Chess.com, "Fork" (Chess Terms). <https://www.chess.com/terms/fork-chess>
Page date: none given.

- Definition: "A fork is a basic chess tactic that consists of a single piece attacking two
  or more pieces at the same time."
- Knights: "Although every piece can deliver a fork, the most striking forks come from a
  knight. Because of the unique way it moves, a forking knight cannot be captured by the
  pieces it is threatening."
- King forks: "The deadliest forks are the ones that are forcing. Usually, those forks
  involve an attack on the enemy king" and the caption "The king is in check so it must
  move. The rook cannot be saved."
- Not stated (either source): a list of what the forked side should do. Capturing the
  forking piece follows from the three ways out of check (section 6) when the fork is a
  check. Prevention is not stated directly; the hanging-piece advice (section 4, "look at
  the square where you are going to place your piece and make sure it is safe") is the
  nearest.

## 3. Back-rank mate

Wikipedia, "Back-rank checkmate". <https://en.wikipedia.org/wiki/Back-rank_checkmate>
Page date: last revised 27 May 2026. Cites Burgess (2009), p. 16.

- Definition: "a back-rank checkmate (also known as a corridor mate) is a checkmate
  delivered by a rook or queen along the opponent's back rank (that is, the row closest to
  them) in which the mated king is unable to move up the board because the king is blocked
  by friendly pieces (usually pawns) on the second rank."
- Beginners: "Beginners are more likely to succumb to back-rank checkmate, as they are more
  likely to miss threats in general."
- Guarding: "Back-rank mates are often guarded against by a friendly rook or queen
  protecting the back rank."
- Luft: "Back-rank threats can be guarded against more permanently by moving one of the
  pawns in front of the king to give the king a flight square (or luft)." Example: "1...g6,
  giving the king a square on g7 to which it can safely move."
- Caution: "It is often not a good idea to play such pawn moves unless there is a pressing
  need to do so, as they can not only represent a loss of time, but may also allow enemy
  penetration around the squares weakened by the pawn advance."

Wikipedia, "Glossary of chess", entry "luft".
<https://en.wikipedia.org/wiki/Glossary_of_chess> Page date: last revised 17 October 2026.
Cites Seirawan and Silman (1994), p. 243.

- "Space made for a castled king to give it a flight square to prevent a back-rank mate.
  Usually luft is made by moving a pawn on the second rank in front of the king."

Chess.com, "Back-Rank Mate" (Chess Terms). <https://www.chess.com/terms/back-rank-mate-chess>
Page date: none given.

- Definition: "a back-rank mate is a checkmating pattern that happens when a player delivers
  checkmate by attacking the back rank of their opponent (first rank for White, eighth rank
  for Black). For this checkmate to be possible, the squares in front of the king must be
  blocked by its own pieces."
- Why it comes up: "Since castling is usually the best way to keep the king safe, the pawn
  structure that allows for this kind of mate often appears on the board. Castling protects
  the king but also allows for the exploitation of the back-rank weakness."
- Not stated here: luft by name (Wikipedia covers it).

## 4. Hanging piece

Chess.com, "Hanging Piece" (Chess Terms). <https://www.chess.com/terms/hanging-piece-chess>
Page date: none given.

- Definition: "A hanging piece is a piece that is unprotected and can be captured. In other
  words, a hanging piece is undefended or "loose" and is attacked."
- En prise: "A piece that can be captured is also known as being "en prise" (a synonym for
  being exposed to capture)."
- Habit: "A simple step to start practicing is to look at the square where you are going to
  place your piece and make sure it is safe"
- Recognising: "Recognizing hanging pieces can be as simple as identifying a piece and
  looking to see if it is protected."
- Example: "Black has just played 3...Nd4. ... White's bishop on b5 is both unprotected and
  attacked!"
- Both sides: "So you can try to avoid hanging pieces, and also so you can recognize your
  opponent's hanging pieces (to attack them)!"

Wikipedia, "Glossary of chess", entries "hanging" and "en prise".
<https://en.wikipedia.org/wiki/Glossary_of_chess>

- hanging (cites Silman 1999, p. 434): "Unprotected and exposed to capture. A hanging piece
  may also be said to be en prise."
- en prise: "describes a piece or pawn exposed to a material-winning capture by the
  opponent. This is either a hanging piece, an undefended pawn, a piece attacked by a less
  valuable attacker, or a piece or pawn defended insufficiently."
- loose piece: "A piece vulnerable to opponent attacks because it is undefended and cannot
  easily be withdrawn or supported."

Counting attackers and defenders: Chess.com's "En Prise" page
(<https://www.chess.com/terms/en-prise>) was served only in German on 22 October 2026. It
says (translated): identifying an en prise piece "can be as simple as comparing how many
attackers and defenders a piece has", with a knight on c6 "attacked three times but defended
only once". Use the glossary's "defended insufficiently" in the guide; don't cite the German
page.

## 5. King in the centre and castling

Wikipedia, "Castling". <https://en.wikipedia.org/wiki/Castling>
Page date: last revised 6 July 2026.

- Why castle: "Castling is generally an important goal in the opening: it moves the king to
  safety away from the center files of the board, and it moves the rook to a more active
  position"
- Rule summary: "A player may not castle out of, through, or into check."
- Caption: "Black cannot castle on either side because the black king is in check by the
  white bishop."
- Exception: "In positions where the opponent cannot organize an attack against a
  centralized king, castling may be unnecessary or even detrimental."

Chess.com, "Castling" (Chess Terms). <https://www.chess.com/terms/castling-chess>
Page date: none given.

- "you cannot castle out of, through, or into check!"
- "Castling gets your king out of the center and protected by pawns . Castling also lets
  your rook into the game."
- "By removing your king from the center, you avoid a lot of quick checkmates!"

FIDE, Laws of Chess, castling. <https://handbook.fide.com/chapter/E012023>

- 3.8.2.1: "The right to castle has been lost: 1) If the king has already moved, or 2) With a
  rook that has already moved."
- 3.8.2.2: "Castling is prevented temporarily: 3) If the square on which the king stands,
  or the square which it must cross, or the square which it is to occupy, is attacked by one
  or more of the opponent's pieces, or 4) If there is any piece between the king and the rook
  with which castling is to be effected."

Wikipedia, "Giuoco Piano". <https://en.wikipedia.org/wiki/Giuoco_Piano>
Page date: last revised 14 September 2026. Cites Van der Sterren, Fundamental Chess Openings
(2009).

- The line: "the old main line 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4+" (after 1.e4 e5 2.Nf3 Nc6
  3.Bc4 Bc5, the Giuoco Piano's moves in the article's lead).
- Replies: "After 5.d4 exd4 6.cxd4 Bb4+ is the standard continuation ... White can then play
  7.Nc3, 7.Bd2, 7.Nbd2, or 7.Kf1!?, which avoids pinning a piece to the king at the cost of
  losing castling rights."
- "After 6.cxd4, the bishop check on b4 is rather inconvenient for White. There are four
  ways to counter it."
- "7.Bd2 is White's most popular move. A possible continuation is 7...Bxd2+ 8.Nbxd2 d5"
- Gambit line: "7.Nc3 Nxe4 8.0-0" (Greco's gambit line).
- The opening's moves, from the article's infobox: "moves = 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5".
  Verify the position with python-chess before drawing it.

## 6. Getting out of check

Chess.com, "Check" (Chess Terms). <https://www.chess.com/terms/check-chess>
Page date: none given.

- "The three ways to get out of check are to move out of check, block the check, or capture
  the piece putting you in check."
- "If you are in check and cannot get out of check, then checkmate has occurred and the game
  is over!"

FIDE 3.9.2 (above) is the rule behind it. FIDE doesn't list the three ways in those words.

## Not found or not used

- Lichess practice pages (the-fork, the-pin) returned HTTP 403 to a plain fetch; not read,
  so not cited.
- No source read gives a step-by-step "what to do when forked" list. The guide can say:
  check whether you can capture the forking piece; if the king is in check you must answer
  the check first (Chess.com Check, FIDE 3.9.2); then save the more valuable piece.

## Board lines (added by the editor, 22 October 2026)

Wikipedia, "Ruy Lopez", section "Steinitz Defence: 3...d6".
<https://en.wikipedia.org/wiki/Ruy_Lopez> (raw wikitext fetched 22 October 2026)

- The line on the Pin board: "White's most direct approach is 4.d4 immediately challenging
  Black's pawn on e5" ... "Following 4.d4, Black proceeds with 4...Bd7 which breaks the pin
  but also defends against White's threat of winning a pawn with 5.Bxc6 and 6.dxe5."

Wikipedia, "Petrov's Defence".
<https://en.wikipedia.org/wiki/Petrov%27s_Defence> (raw wikitext fetched 22 October 2026)

- The line on the Hanging piece board: "After 3.Nxe5, the standard reply for Black is 3...d6
  (3...Nxe4?! is usually considered an error). After 4.Nf3 Nxe4, White's main options are
  5.d4 ... and 5.Nc3".

Every board position was played out or set up with python-chess 1.11.2 (a scratch venv in
/tmp, not the repo's .venv) on 22 October 2026:

| Board | Placement | Checked |
|---|---|---|
| Pin | r1bqkbnr/ppp2ppp/2np4/1B2p3/3PP3/5N2/PPP2PPP/RNBQK2R (after 1.e4 e5 2.Nf3 Nc6 3.Bb5 d6 4.d4) | Black to move; the knight on c6 is pinned and has no legal move; after 4…Bd7 it is no longer pinned |
| Fork | 4k3/pp3ppp/8/8/8/8/PPn2PPP/R2QK2R, White to move | Legal; White in check; legal moves Ke2, Kd2, Kf1, Qxc2 |
| Back-rank mate | 4r1k1/pp3ppp/8/8/8/Q7/PP3PPP/6K1, White to move | Legal; if Black moved now, Re1 would be checkmate; after 1.h3, 1.g3 or 1.Kf1 Black has no mate in one |
| Hanging piece | rnbqkb1r/ppp2ppp/3p1n2/4N3/4P3/8/PPPP1PPP/RNBQKB1R (after 1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6) | White to move; the knight on e5 is attacked by the pawn on d6 and defended by nothing |
| King in the center | r1bqk2r/pppp1ppp/2n2n2/8/1bBPP3/5N2/PP3PPP/RNBQK2R (after the Giuoco Piano line to 6…Bb4+) | White in check; legal moves Ke2, Kf1, Nfd2, Qd2, Bd2, Nc3, Nbd2; castling isn't among them |

## For the sources page

| Source | Date | Address |
|---|---|---|
| FIDE, Laws of Chess | January 2023 | handbook.fide.com/chapter/E012023 |
| Wikipedia, Pin (chess) | May 2026 | en.wikipedia.org/wiki/Pin_(chess) |
| Wikipedia, Fork (chess) | July 2026 | en.wikipedia.org/wiki/Fork_(chess) |
| Wikipedia, Back-rank checkmate | May 2026 | en.wikipedia.org/wiki/Back-rank_checkmate |
| Wikipedia, Glossary of chess | October 2026 | en.wikipedia.org/wiki/Glossary_of_chess |
| Wikipedia, Castling | July 2026 | en.wikipedia.org/wiki/Castling |
| Wikipedia, Giuoco Piano | September 2026 | en.wikipedia.org/wiki/Giuoco_Piano |
| Wikipedia, Ruy Lopez | October 2026 | en.wikipedia.org/wiki/Ruy_Lopez |
| Wikipedia, Petrov’s Defence | October 2026 | en.wikipedia.org/wiki/Petrov%27s_Defence |
| Chess.com, Chess Terms: Pin, Fork, Back-Rank Mate, Hanging Piece, Check, Castling | October 2026 | chess.com/terms |
