# Sources for An Accidental Guide to… Stopping Scholar’s Mate

All fetched 22 October 2026 (raw copies kept outside the repo while writing, in
/tmp/sm-src/). Excerpts are verbatim and short. Wikipedia and Wikibooks pages were read as
raw wikitext (action=raw); Chess.com pages as HTML, text extracted. Every move sequence
below was replayed with python-chess 1.11.2 (scratch venv, not the repo's .venv): all are
legal, and both Scholar’s mate orders end in checkmate.

## 1. What Scholar’s mate is

Wikipedia, "Scholar's mate". <https://en.wikipedia.org/wiki/Scholar%27s_mate>
Page date: none given (live article, read 22 October 2026). Cites Hooper and Whyld, The
Oxford Companion to Chess (1996), pp. 358–359, and Kállai, Basic Chess Openings (1997), p. 7
(books, not read; the guide relies only on the article text).

- The moves: "In chess, scholar's mate is the checkmate achieved by the following moves, or
  similar: 1. e4 e5 2. Qh5 Nc6 3. Bc4 Nf6?? 4. Qxf7#"
- Other orders, same idea: "The same mating pattern may be reached by various move orders.
  For example, White might play 2.Bc4. In all variations, the basic idea is the same: the
  queen and bishop combine in a simple mating attack, occurring on f7 for White or on f2 for
  Black."
- Easy to stop, and the attacker ends up worse: "It is used almost exclusively by
  beginners. Defending against it is very simple, and if it is parried, the attacker's
  position usually worsens."
- Common among beginners: "games ending in scholar's mate are quite common among
  beginners. It is not difficult to parry, however."
- f7 and f2 are weak: "the basic idea underlying it—that f7 and f2, squares defended only by
  the kings, are weak and therefore good targets for early attack"
- Not stated: who the "scholar" was in a way the guide needs (history is trivia, left out).

Chess.com, "Scholar's Mate - The 4 Move Checkmate" (Chess Terms).
<https://www.chess.com/terms/scholars-mate-chess>
Page date: none shown in the extracted text.

- Bishop and queen on f7: "It ends the game after only four moves by attacking the weak
  f-pawn with a bishop and a queen. The f7-pawn is considered weak because it is solely
  defended by the king"
- The Bc4-first order: "It occurs after 1.e4 e5 2.Bc4 (targeting f7) Nc6 3.Qh5 (adding
  another attacker to the f7-pawn) Nf6?? 4.Qxf7#."
- Easy to defend, can backfire: "it is easy to defend against and can lead to a worse
  position if it fails."
- The early queen can be chased: "If White is not careful, Black can exploit the fact that
  the white queen is vulnerable to gain a lead in development."

## 2. The Wayward Queen (2.Qh5)

Wikipedia, "Danvers Opening". <https://en.wikipedia.org/wiki/Danvers_Opening>
Page date: none given.

- The moves and the name: "The Danvers Opening is an unorthodox chess opening characterized
  by the moves: 1. e4 e5 2. Qh5". Also known as "Wayward Queen Attack" (among other names:
  Kentucky Opening, Queen's Attack, Patzer Opening, Parham Attack).
- Why it's dubious: "The Danvers Opening violates a conventional opening principle by
  developing the queen too early, subjecting it to attack and loss of tempo."
- The usual reply: "forcing Black (unless they want to sacrifice a pawn) to first defend the
  e-pawn (usually with 2...Nc6), then 3.Bc4 forces Black to make some compromise to defend
  against the mate threat; 3...g6 commits Black to fianchettoing the king's bishop, 3...Qe7
  blocks the bishop, and 3...Qf6 occupies the knight's best square."
- Played hoping for Scholar’s mate: "2.Qh5 is frequently played with the hope of delivering
  the Scholar's Mate, e.g. 2.Qh5 Nc6 3.Bc4 Nf6?? 4.Qxf7#. Black can easily avoid this"
- Bad replies: "Black's worst possible response to 2.Qh5 is 2...Ke7?? 3.Qxe5#." "Also
  losing is 2...g6?? 3.Qxe5+, winning a rook and pawn. The most frequently played move is
  2...Nc6"
- The main line and its verdict: "Black defends the e-pawn and prepares to meet 3.Bc4 with
  3...Qe7 or 3...g6. The latter move is more common and after 4.Qf3 Nf6 5.Ne2 the main
  position is reached. White is not worse, but also has no advantage." Then "5...Bg7" is
  "one of the most popular" plans.

Wikipedia, "Scholar's mate", section "After 2.Qh5" (same URL as above).

- What 2.Qh5 threatens: "White does not threaten Qxf7# yet, but does threaten Qxe5+. The
  cleanest way to defend against this is 2...Nc6, developing a knight and protecting the
  pawn. (2...d6 is also good.) After 3.Bc4, Black can stop the mate with 3...g6; White can
  threaten mate again with 4.Qf3, but this can be stopped with 4...Nf6. Black can later
  fianchetto the f8-bishop (...Bg7)."
- Diagram caption: "After 1.e4 e5 2.Qh5 Nc6 3.Bc4 g6 4.Qf3 Nf6, Black has successfully
  defended against the scholar's mate."

Wikibooks, "Chess Opening Theory/1. e4/1...e5/2. Qh5".
<https://en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...e5/2._Qh5>

- Attacks e5 and f7: "2. Qh5 both attacks the pawn on e5 and puts pressure on f7. The f7
  square is the weakest point in Black's position at the start of the game, because it is
  the only square guarded only by Black's king."
- No mate threat yet: "As f7 is attacked once (by White's queen) and defended once (by
  Black's king), there is no immediate threat of Qxf7+. However, there is a threat of
  Qxe5+."
- 2...Nc6: "2...Nc6 is the best move. Black defends against Qxe5+, while also getting to
  develop a piece to its most active square."
- The defence step by step: "3. Bc4 (bringing a second attacker to f7, so now White really
  is threatening Qxf7#) g6 (cuts off White's queen's vision of f7, and gains time by forcing
  the queen to move again) 4. Qf3 (threatens Qxf7# again) Nf6 (blocks White's queen's
  vision of f7). The immediate threats parried, Black is ready to play ...Bg7 and ...O-O."
- Black gains time: "So long as Black doesn't fall into White's traps, they will be able to
  develop easily and play useful moves that gain time on White's queen."
- 2...Qf6 is not recommended: "violating opening principles yourself is no way to punish
  your opponent's violations of the same."
- 2...g6??: "Black attacks the queen and leaves their e-pawn undefended, but moving the
  g-pawn exposed Black's rook on h8: 3. Qxe5+ Be7 (or 3...Qe7) 4. Qxh8"

## 3. The defences: ...g6, ...Qe7, ...Nf6 at the right moment

Chess.com, "Scholar's Mate" (same URL as section 1), "How To Defend Against The Scholar's
Mate", from the position after 1.e4 e5 2.Bc4 Nc6 3.Qh5:

- ...g6: "The move g6 is the most sensible response to the threat of a Scholar's Mate. It
  frees up the g7-square for Black to fianchetto their bishop" … "it wins a tempo because
  it threatens the white queen, forcing White to move their lady away from danger."
- ...Qe7: "Another option to defend against this attack is to move your queen to the
  e7-square. This move protects the f7-pawn, develops the queen, and adds another defender
  to the e5-pawn. This move comes with two drawbacks: it blocks the dark-squared bishop and
  brings out the queen too early."
- ...Qf6: "it creates difficulties for one of your minor pieces to develop and exposes your
  queen, so it is not the most recommended response."

Wikibooks, "Chess Opening Theory/1. e4/1...e5/2. Qh5/2...Nc6/3. Bc4".
<https://en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...e5/2._Qh5/2...Nc6/3._Bc4>

- "The two decent replies are 3...g6 and 3...Qe7."
- The trap: "At the lower level many players may be tempted to play 3…Nf6?? attacking
  White’s queen. However, Black leaves f7 undefended, and White can play the move they were
  intending to play when 2. Qh5 was played: 4. Qxf7#"
- Theory table rows (1.e4 e5 2.Qh5 Nc6): "3.Bc4 g6 4.Qf3 Nf6 5.Ne2 Bg7 6.Nbc3 d6 =/+" and
  "3.Bc4 g6 4.Qf3 Nf6 5.Qb3 Nd4 =/+" (=/+ means Black is equal or slightly better).

Wikibooks, "…/3. Bc4/3...Nf6". 
<https://en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...e5/2._Qh5/2...Nc6/3._Bc4/3...Nf6>

- "The next move will be 4.Qxf7# (standing for mate). The one natural developing move leads
  to mate - and that is why black has to always be careful for Scholar's mate."

Wikibooks, "…/3. Bc4/3...g6".
<https://en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...e5/2._Qh5/2...Nc6/3._Bc4/3...g6>

- "Black counterattacks the White queen, and blocks 4. Qxf7#. White then moves the queen to
  safety on f3 and attacks f7 from a different angle."

Wikibooks, "…/3...g6/4. Qf3".
<https://en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...e5/2._Qh5/2...Nc6/3._Bc4/3...g6/4._Qf3>

- Nf6 at the right moment, and the wrong ones: "White renews the threat of (delayed)
  Scholar's mate 5.Qxf7# if Black does not prevent this, for example, if 4...Nd4?? to
  attack the queen, or 4...Bg7?? or 4...d6??. Black’s options are to play 4...Nf6, which
  successfully blocks the checkmate threat"

Wikibooks, "…/4. Qf3/4...Nf6".
<https://en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...e5/2._Qh5/2...Nc6/3._Bc4/3...g6/4._Qf3/4...Nf6>

- "Black blocks the attack from the queen. Although the black knight is "pinned" to the pawn
  (If it were to move, white would play Qxf7#), Black has been handed the moves ...Bg7 and
  ...O-O on a platter."
- "if White doesn't defend d4, instead playing 5. Nc3?, (which is also a common response
  between low rating players) Black has 5...Nd4! 6. Qd1 Bg7."

## 4. Punishing the early queen: tempo

Wikibooks, "…/4...Nf6/5. Nc3/5...Nd4".
<https://en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...e5/2._Qh5/2...Nc6/3._Bc4/3...g6/4._Qf3/4...Nf6/5._Nc3/5...Nd4>

- "Black threatens to fork White’s pieces while simultaneously putting pressure on the
  queen, thereby forcing it to retreat to its original square, resulting in a tempo gain."
- "Qd1 retreats the queen back to the square, saving white from being forked. This move is
  the best move to play in this position." "Everything else loses the rook to 6...Nxc2! and
  7...Nxa1."

Wikipedia, "Tempo (chess)". <https://en.wikipedia.org/wiki/Tempo_(chess)>

- Definition: "a tempo … is a "turn" or single move". "when a player forces their opponent
  to make moves not according to their initial plan, one is said to "gain tempi" because the
  opponent is wasting moves. A move that gains a tempo is often called "a move with tempo"."
- Attacking a piece: "A move that comes "with a tempo on a piece" is a move that gains a
  tempo by attacking that piece." Example: "after 1.e4 d5 2.exd5 Qxd5, White's 3.Nc3 comes
  "with a tempo on the queen": the knight attacks Black's queen, forcing it to move again"

Chess.com, "Tempo In Chess" (Chess Terms). <https://www.chess.com/terms/tempo-chess>

- "it is a way to identify each turn a player spends to move a piece."
- "When you successfully move your piece to a good square and force your opponent to stop
  their original plan to defend against your newly created threat, you have gained a
  tempo."
- "White develops their pieces and attacks the queen at the same time, gaining many tempi."

## 5. The 2.Bc4 order and ...Qe7 there

Wikipedia, "Scholar's mate", section "After 2.Bc4" (same URL as section 1).

- "The most popular response to 2.Bc4 is 2...Nf6, the Berlin Defense, which immediately
  renders the scholar's mate non-viable."
- "In the continuation 2...Bc5 (the Classical Defense) 3.Qh5, Black can defend against both
  scholar's mate and the threatened 4.Qxe5+ with 3...Qe7, intending to gain a tempo later
  with 4...Nf6."

Note: 2...Nf6 against 2.Bc4 is "the right moment" for ...Nf6: before the queen reaches h5,
the knight stops Qh5 coming at all (the knight covers h5). After 3.Qh5 is already on the
board with the bishop on c4, ...Nf6 is the losing move. The guide can say the timing rule
from these two excerpts; no source states it as one sentence.

## Where sources disagree

- ...Qe7 versus ...g6: Chess.com calls ...g6 "the most sensible response" and lists ...Qe7
  with two drawbacks. Wikibooks calls both "decent". Wikipedia says ...g6 "is more common".
  The guide can offer ...g6 first and ...Qe7 as the other safe choice.
- 2.Qh5's verdict: Wikipedia says after 5.Ne2 "White is not worse, but also has no
  advantage"; Wikibooks' table marks the lines =/+ (Black equal or slightly better). Wikipedia
  (Scholar's mate) says the attacker's "position usually worsens" once it's parried. The guide
  should say the attacker gains nothing and often ends up worse, not that Black is winning.

## Not found

- No Lichess learn or practice page covers Scholar’s mate (lichess.org/practice fetched; its
  topics are checkmate patterns and endgames). Not used.
- No source gives 5.Qb3 Nd4 in prose; only the Wikibooks theory table (=/+). Prefer
  5.Nc3? Nd4! 6.Qd1, which has prose.
- FIDE Laws not needed.

## For the sources page

| Source | Date | Address |
|---|---|---|
| Wikipedia, Scholar’s mate | October 2026 | en.wikipedia.org/wiki/Scholar%27s_mate |
| Wikipedia, Danvers Opening | October 2026 | en.wikipedia.org/wiki/Danvers_Opening |
| Wikipedia, Tempo (chess) | October 2026 | en.wikipedia.org/wiki/Tempo_(chess) |
| Wikibooks, Chess Opening Theory, 1.e4 e5 2.Qh5 | October 2026 | en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...e5/2._Qh5 |
| Chess.com, Scholar’s Mate | October 2026 | chess.com/terms/scholars-mate-chess |
| Chess.com, Tempo | October 2026 | chess.com/terms/tempo-chess |
