# Writing instructions, round 1: An Accidental Guide to… Stopping Scholar’s Mate

You are writing one file: `drafts/chess-scholars-mate/guide.md` (from your working directory
it is `./guide.md`). It holds PLACEHOLDER text that shows the shape the builders expect.
Replace every PLACEHOLDER with finished text. Don't touch any other file.

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
5. `drafts/chess-scholars-mate/notes/plan.md`: the page plan. Follow it.
6. `drafts/chess-scholars-mate/notes/sources.md`: every fact you may use. Use no fact that
   isn't there. Restate in your own plain words.

## Who it's for

Someone who knows how the pieces move and plays casual games, and keeps losing in four moves
to the same queen-and-bishop trick, or worries about it. No theory. The author's aim for the
chess guides: "We aren't trying to get them to memorize anything; the goal is to give them
enough to 'see' the board and want to learn more." So point the reader at the boards: what to
look at, which piece, which square. The series' spirit is warm, a little self-deprecating and
dry: at most one light, dry touch per page, never jokey. The voice rules win over any wish to
be funny.

## The question, and the answer in order

How do you stop Scholar’s Mate, and make it backfire?

1. `{#why}` (about 160 words with the table). Paragraph 1 is the summary the website shows
   and must stand alone (about 50 words): Scholar’s Mate is a quick checkmate where White’s
   queen and bishop both aim at f7 and the queen takes there. It is easy to stop, and once
   stopped the attacker has usually wasted moves. Paragraph 2 (about 45 words): moves are
   written in algebraic notation, explained in An Accidental Guide to: The First Move in
   Chess; every board is drawn from Black’s side, so your pieces are nearest you and the
   a-file is on your right. Paragraph 3: one sentence into the four terms. Terms table: one
   short sentence each.
2. `{#fit}`: the board caption (about 20 words) says what to see: the two arrows meet on f7.
   One paragraph (about 70 words): Black to move; the threat is Qxf7#; f7 is defended only
   by the king; so the first job is to see the two lines meet, and the next move must guard
   f7.
3. Entries (about 110 words each, plus a board caption of about 20 words). Each board is
   drawn above the rows; its caption says what to look at on the board. Rows: Identify by
   (what you see on the board); What (first sentence is the definition, genus and
   difference, and prints bold up to the first ". "); So what (first sentence prints bold
   too); two field marks, Watch for and Your answer, each a short answer of two to seven
   words with no full stop; Confused with, two flat sentences.
   - The f7 square: board is the mate after 3…Nf6 4.Qxf7#. The king can’t take the queen
     because the bishop on c4 guards it. f7 is defended only by the king at the start.
     Confused with f2: White’s matching weak square, also defended only by the king.
   - The early queen: board is 1.e4 e5 2.Qh5, which has the names Wayward Queen Attack and
     Danvers Opening. The queen attacks e5 and f7, but the first real threat is Qxe5+. Answer
     2…Nc6, which defends e5 and brings out a knight. Confused with a strong attack: sources
     say the queen comes out early and gets chased, and the attacker gains nothing.
   - Guarding f7: board after 3…g6. The pawn blocks the queen’s line to f7 and attacks the
     queen. 3…Qe7 also guards f7. After 4.Qf3 the queen aims at f7 again, and 4…Nf6 blocks
     the f-file. Confused with 3…Nf6: the natural developing move, which attacks the queen
     but leaves f7 to Qxf7#.
   - Tempo: board after 4.Qf3 Nf6 5.Nc3 Nd4. A tempo is one move’s worth of time. A move
     that develops a piece and attacks the queen gains one, because the queen has to move
     again. Nd4 attacks the queen and c2, where the knight could fork king and rook; the
     queen goes back to d1 and Black follows with …Bg7 and castling. Confused with time on
     the clock: a tempo is a move, not minutes.
4. `{#shown}` What do you play against it? One intro sentence (the usual move orders, and the
   reply that fits each). Then one sentence per row of the Move / Why table (keep the Move
   cells exactly as they are). Closing sentence: then keep developing and castle, and the
   early queen has cost White time. Mention that 3…Qe7 is the other safe reply to 3.Bc4 in
   the Why for that row.

## Length

Five minutes front to back: about 850 words in guide.md, tables and sources included, because
the five boards add printed rank and file labels. Stay under each budget above. Cut detail,
not clarity.

## How to write it

- Regular English, normal word order, "you" for the reader, who plays Black.
- Build one idea at a time. Short sentences, but not staccato.
- No paragraph by list: if it's a list, it's in a table already.
- Each part has one name: The f7 square, The early queen, Guarding f7, Tempo. Use them.
- Write moves exactly as the sources do, with the typographic ellipsis for Black’s moves
  (3…g6). Use no ?? or ! marks in the text.
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
