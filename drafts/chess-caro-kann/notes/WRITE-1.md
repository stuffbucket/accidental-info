# Writing instructions, round 1: An Accidental Guide to… The Caro-Kann for Black

You are writing one file: `drafts/chess-caro-kann/guide.md` (from your working directory it
is `./guide.md`). It holds PLACEHOLDER text that shows the shape the builders expect. Replace
every PLACEHOLDER with finished text. Don't touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

## Read first, in this order

Paths are from the repository root (`../..` from your working directory).

1. `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`: the
   author's feedback. Binding.
2. `packages/editorial/skills/accidental-guide-write/references/voice.md`: his voice. Binding.
3. `packages/editorial/skills/accidental-guide-write/references/banned-patterns.md`: what
   never goes in.
4. `drafts/chess-last-move/guide.md` and `drafts/chess-first-move/guide.md`: two finished chess
   guides in the same layout. Copy their length and register, not their topic. Don't
   contradict them. The First Move in Chess explains algebraic notation; point to it.
5. `drafts/chess-caro-kann/notes/plan.md`: the page plan. Follow it.
6. `drafts/chess-caro-kann/notes/sources.md`: every fact you may use. Use no fact that isn't
   there. Restate in your own plain words.

## Who it's for

Someone who knows how the pieces move, plays casual games, and wants one dependable answer
when White opens 1.e4. No theory, no long lines to memorize. The author's aim for the chess
guides: "We aren't trying to get them to memorize anything; the goal is to give them enough
to 'see' the board and want to learn more." So point the reader at the boards: what to look
at, which piece, which square. The series' spirit is warm, a little self-deprecating and dry:
at most one light, dry touch per page, never jokey. The voice rules win.

## The question, and the answer in order

What do you play as Black against 1.e4, and what do you do next?

1. `{#why}` (about 160 words with the table). Paragraph 1 is the summary the website shows
   and must stand alone (about 50 words): the Caro-Kann is 1.e4 c6 2.d4 d5. The c-pawn move
   prepares …d5, which challenges White’s pawn on e4. It is known for being solid, and you can
   play it with a short plan instead of long lines. Paragraph 2 (about 50 words): it answers
   1.e4 only. Against 1.d4, a simple start is 1…d5, as in An Accidental Guide to: The First
   Move in Chess, which also explains the notation. Every board is drawn from Black’s side, so
   your pieces are nearest you and the a-file is on your right. Paragraph 3: one sentence into
   the four terms. Terms table: one short sentence each.
2. `{#fit}`: board caption (about 20 words): the d5 pawn challenges e4, and the bishop on c8
   now has an open road to f5. One paragraph (about 70 words): White has three main choices
   at move 3: push the pawn to e5 (Advance), swap on d5 (Exchange), or defend e4 with a knight,
   after which you take on e4 (Main line). In each one, the same plan works: bishop out, then
   …e6, then develop and castle.
3. Entries (about 105 words each, plus a board caption of about 20 words). The board is drawn
   above the rows; its caption says what to look at. Rows: Identify by (what you see on the
   board); What (first sentence is the definition, genus and difference, and prints bold up
   to the first ". "); So what (first sentence prints bold too); two field marks, White plays
   and You play, each a short answer of two to seven words with no full stop (the Advance,
   Exchange and Main line field marks are already filled in; keep them, and fill the light
   bishop's two); Confused with, two flat sentences.
   - The light bishop: board after 3.e5 Bf5 4.Nf3 e6, the bishop outside the pawns on c6, d5
     and e6. The plan: bring the bishop out to f5 or g4 before you play …e6, because …e6
     would shut it in. Then …e6, knights out, castle. Field marks: White plays: any third
     move; You play: bishop out, then …e6. Confused with The French Defense: 1.e4 e6, where
     the e6 pawn can block the bishop on c8.
   - Advance: board after 3.e5, with the arrow showing 3…Bf5. White pushes past your d5 pawn
     and takes space. Play 3…Bf5 at once, then …e6. With the e6 pawn in place, your other
     bishop supports …c5, which hits White’s pawn chain at d4. Confused with Exchange: in the
     Advance, White pushes the e-pawn forward; in the Exchange, White swaps it on d5.
   - Exchange: board after 3.exd5 cxd5 4.Bd3 Nc6 5.c3 Nf6 6.Bf4 Bg4. You take back with the
     c-pawn, which frees c6 for your knight. White’s Bd3 stops …Bf5, so the bishop goes to g4
     instead. Confused with The Panov Attack: after 3.exd5 cxd5, 4.c4 is a different line with
     its own name, and it isn’t covered here.
   - Main line: board after 3.Nc3 dxe4 4.Nxe4 Bf5. White defends e4 with a knight, you take
     the pawn, and the bishop comes out attacking the knight. White often chases the bishop
     with 5.Ng3 Bg6 and then h4. Answer h4 with …h6, so the bishop has a square to drop back
     to. Confused with 3.Nd2: after 3…dxe4 4.Nxe4, 3.Nd2 gives the same position.
4. `{#habits}` Which traps should you avoid? One intro sentence. One or two sentences per row
   of the Trap / Avoid it table (keep the Trap cells as they are):
   - 5.Qe2 and 6.Nd6: after 4…Nd7 instead of 4…Bf5, White’s 5.Qe2 sets a trap. 5…Ngf6 lets
     6.Nd6 give checkmate, because every square around your king is blocked by your own
     pieces. 5…Ndf6 is safe.
   - h4 and h5: in the Main line, when White plays h4 with your bishop on g6, play …h6.
   - h4 and g4: in the Advance, after 3…Bf5 4.h4, play 4…h5. If you play 4…e6 first, White
     traps the bishop with 5.g4 Be4 6.f3 Bg6 7.h5.
   Board caption (about 20 words): the knight on d6 gives check, and the king can’t move
   because its own pieces fill every square. Closing sentence: when White’s pawns run at your
   bishop, give it a square to retreat to.

## Length

Five minutes front to back: about 850 words in guide.md, tables and sources included, because
the six boards add printed rank and file labels. Stay under each budget above. Cut detail,
not clarity.

## How to write it

- Regular English, normal word order, "you" for the reader, who plays Black.
- Build one idea at a time. Short sentences, but not staccato.
- No paragraph by list: if it's a list, it's in a table already.
- Each part has one name: The light bishop, Advance, Exchange, Main line. Use them.
  American spelling (defense, center), but "Caro-Kann" with a hyphen.
- Write moves as the sources do, with the typographic ellipsis for Black’s moves (3…Bf5).
  Use no ?? or ! marks.
- No quotes and no names of people. Don't mention Wikipedia or any source in the body.
- Cross-references in the colon form: "An Accidental Guide to: The First Move in Chess".
- Typographic apostrophes (’) and quotes. No em dashes, semicolons, backticks or emphasis.
- No sentence in a table row starts with "It", "Its", "They" or "This".

## Keep the shape

Keep the front matter, every heading and its `{#id ...}`, the ```diagram blocks except the
caption text after the last `|` on each `board` line (replace those PLACEHOLDERs), the number
of paragraphs in each section, table header rows, first-column labels and the field mark
labels. Don't add or remove sections. Don't touch the Sources section.

When you're done, reply with one line: done.
