# Writing instructions, round 1: An Accidental Guide to… Getting Out of Trouble in Chess

You are writing one file: `drafts/chess-problem-positions/guide.md` (from your working
directory it is `./guide.md`). It holds PLACEHOLDER text that shows the shape the builders
expect. Replace every PLACEHOLDER with finished text. Don't touch any other file.

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
5. `drafts/chess-problem-positions/notes/plan.md`: the page plan. Follow it.
6. `drafts/chess-problem-positions/notes/sources.md`: every fact you may use. Use no fact that
   isn't there. Restate in your own plain words.

## Who it's for

Someone who knows how the pieces move and plays casual games, and keeps losing pieces or
games to the same few problems without a name for them. No theory. The author's aim for the
chess guides: "We aren't trying to get them to memorize anything; the goal is to give them
enough to 'see' the board and want to learn more." So point the reader at the boards: what
to look at, which piece, which square. The series' spirit is warm, a little self-deprecating
and dry: at most one light, dry touch per page, never jokey. The voice rules win.

## The question, and the answer in order

What are the common problem positions, and how do you get out of each one?

1. `{#why}` (about 160 words with the table). Paragraph 1 is the summary the website shows
   and must stand alone (about 50 words): five problems come up again and again in casual
   games; each has a clear way out, and a habit that stops it next time. Paragraph 2 (about
   45 words): moves are written in algebraic notation, explained in An Accidental Guide to:
   The First Move in Chess; each board is drawn from the side in trouble, so the pieces you
   need to save are nearest you (Black for the pin, White for the rest). Paragraph 3: one
   sentence into the five terms. Terms table: one short sentence each.
2. Entries (about 105 words each, plus a board caption of about 20 words). The board is drawn
   above the rows; its caption says what to look at. Rows: Identify by (what you see on the
   board); What (first sentence is the definition, genus and difference, and prints bold up
   to the first ". "); So what (the way out, first sentence prints bold too); two field
   marks, Way out and Next time, each a short answer of two to seven words with no full
   stop; Confused with, two flat sentences.
   - Pin: board after 1.e4 e5 2.Nf3 Nc6 3.Bb5 d6 4.d4, Black to move. The bishop on b5 lines
     up through the knight on c6 to the king on e8. Pinned to the king, the knight can’t move
     at all, because no move may expose your own king to check. Way out: put a piece in the
     line, here 4…Bd7, which breaks the pin. Other ways: move the piece behind, or capture or
     chase the pinning piece. Only a bishop, rook or queen can pin. Confused with Relative
     pin: when the piece behind isn’t the king, the pinned piece may move, but you lose
     what’s behind it.
   - Fork: board is White to move and in check from a knight on c2, which also attacks the
     rook on a1. A fork is one piece attacking two or more at once. Knights fork well because
     the pieces they attack can’t capture them back the same way. When the fork comes with
     check, you must answer the check first. Way out: capture the forking piece if you can,
     here Qxc2. If you can’t, the king must move and the other piece is usually lost. Next
     time: look at the squares an enemy knight can reach next move. Confused with Pin: a fork
     attacks two pieces at once, a pin stops one piece from moving.
   - Back-rank mate: board is White to move. Black threatens Re1, which would be checkmate
     because the pawns on f2, g2 and h2 block the king. White is a queen for a rook ahead and
     would still lose. Way out: make a square for the king by moving a pawn in front of it, here
     h3 (often called luft), or keep a rook or queen guarding the back rank. Confused with A
     safe castled king: castling protects the king but leaves the back rank as a weakness.
   - Hanging piece: board after 1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6, White to move. The knight on e5
     is attacked by the pawn on d6 and nothing defends it. A hanging piece is unprotected
     and can be captured. Way out: move it to a safe square or defend it, here 4.Nf3. Next
     time: before each move, look at the square you put a piece on and check it is safe.
     Confused with En prise: en prise covers any piece that can be taken at a loss, including
     one defended too little or attacked by a cheaper piece.
   - King in the center: board in the Giuoco Piano after 6.cxd4 Bb4+, White in check with the
     king on e1. Castling gets the king away from the center files, and a king left in the
     center is open to quick attacks. You can’t castle out of check, so White blocks with a
     piece that develops, 7.Bd2 or 7.Nc3, and castles next. Next time: castle early.
     Confused with Castling out of check: castling isn’t allowed while in check, or through or
     into check.
3. `{#habits}` What do you check before each move? One intro sentence. Four rows: Check (a
   short imperative, three to seven words) then Why (one sentence). Rows: look at the square
   you’re moving to; look where enemy knights can jump next; give your castled king a square;
   castle early. Closing sentence: one plain line that sends the reader back to the board.

## Length

Five minutes front to back: about 850 words in guide.md, tables and sources included, because
the five boards add printed rank and file labels. Stay under each budget above. Cut detail,
not clarity.

## How to write it

- Regular English, normal word order, "you" for the player in trouble.
- Build one idea at a time. Short sentences, but not staccato.
- No paragraph by list: if it's a list, it's in a table already.
- Each part has one name: Pin, Fork, Back-rank mate, Hanging piece, King in the center. Use
  them. American spelling (center).
- Write moves as the sources do, with the typographic ellipsis for Black’s moves (4…Bd7). Use
  no ?? or ! marks.
- No quotes and no names of people or openings' namesakes. Don't mention Wikipedia or any
  source in the body.
- Cross-references in the colon form: "An Accidental Guide to: The First Move in Chess".
- Typographic apostrophes (’) and quotes. No em dashes, semicolons, backticks or emphasis.
- No sentence in a table row starts with "It", "Its", "They" or "This".

## Keep the shape

Keep the front matter, every heading and its `{#id ...}`, the ```diagram blocks except the
caption text after the last `|` on each `board` line (replace those PLACEHOLDERs), the number
of paragraphs in each section, table header rows, first-column labels and the field mark
labels. In `{#habits}`, replace the PLACEHOLDER first-column cells with the short imperatives.
Don't add or remove sections. Don't touch the Sources section.

When you're done, reply with one line: done.
