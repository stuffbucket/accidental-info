# Writing instructions, round 1: An Accidental Guide to… The First Move in Chess

You are writing one file: `drafts/chess-first-move/guide.md` (from your working directory it
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
4. `guides/specs-and-reviews/guide.md`: a finished guide with the same layout. Copy its
   length and register, not its topic.
5. `drafts/chess-first-move/notes/plan.md`: the page plan. Follow it.
6. `drafts/chess-first-move/notes/sources.md`: every fact you may use. Use no fact that isn't
   there. Restate in your own plain words.

## Who it's for

Someone who has just sat down at a chessboard, as White or as Black, and knows roughly how
the pieces move. They may be playing a child, a friend or a colleague, and would quite like
not to lose in four moves. Notation looks like code to them. The series' spirit is warm,
a little self-deprecating and dry: at most one light, dry touch per page, never jokey. The
voice rules win over any wish to be funny.

## The question, and the answer in order

What should my first move be?

1. White moves first, then the players take turns. The first few moves have two jobs: get
   your pieces out quickly and get your king safe. Three ideas cover most of it: the center,
   development and castling. You don't need to memorise opening lines.
2. How do you read the board? The board diagram is drawn from the diagram block (don't
   change it). Two paragraphs explain notation once: squares are named by file letter (a to h,
   left to right from White's side) and rank number (1 to 8, from White's side); pieces are
   K, Q, R, B, N (N for knight); a pawn move is just the square; moves are numbered, White's
   then Black's, so 1.e4 e5 means White's pawn to e4, then Black's pawn to e5. When Black's
   move is written alone, it takes three dots: 1…e5. Use the ellipsis character (…).
3. Center, Development, Castling: one entry each.
4. What should you play first? A Move / Why table, a warning callout, a closing sentence.

## Section by section

- Front matter: keep it as it is.
- `{#why}` (about 160 words in all). Paragraph 1 is the blurb the website shows, so it must
  stand alone (about 50 words). Paragraph 2 (about 45 words): what the first few moves are
  for, with the principle that opening lines matter less to a beginner than a few principles.
  Paragraph 3: one sentence that leads into the three terms. Terms table: one short sentence
  each.
- `{#fit}`: two paragraphs, about 45 words each, as described above.
- Each entry (about 110 words): Identify by (where you see it on the board); What (first
  sentence is the definition, genus and difference; it prints bold up to the first ". ");
  So what (first sentence prints bold too); three field marks (When, Aim, Mistake), each a
  short answer of two to six words with no full stop; Confused with, two flat sentences.
  - Center: d4, d5, e4 and e5. Put a center pawn out first. The center opens up first, so
    pieces there reach both sides. Confused with Pawn moves: one or two center pawn moves
    help, but too many early pawn moves leave your pieces at home.
  - Development: moving knights and bishops off the back rank so they take part; each piece
    once if you can; your opponent is doing the same; a lead in development means more of
    your pieces are in the game. Confused with Bringing out the queen: the queen is your
    strongest piece, but out early it gets chased by pieces your opponent is developing
    anyway, so bring it out later.
  - Castling: the king moves two squares toward a rook and the rook lands on the square the
    king crossed, all as one move, written 0-0 or 0-0-0. Do it early: the king gets safe and a
    rook comes toward the middle. Rules: neither piece may have moved; no piece between them;
    the king may not be in check or cross or land on an attacked square. Confused with Moving
    the king: an ordinary king move is one square; touching the king first is the safe way to
    castle (if you touch a rook first, you may have to move the rook).
- `{#shown}` What should you play first? One intro sentence. Six table rows, Move then Why:
  1.e4 (as White); 1.d4 (as White); 1…e5 (as Black, after 1.e4); 1…d5 (as Black, after
  1.d4); Nf3 and Nc6 (then knights, then bishops); 0-0 (then castle). Put the side in the
  Why text ("As White." "As Black, after 1.e4."). The Move cell holds only the move. Each
  Why is one or two sentences that say which principle the move follows and what it opens up
  (a center pawn two squares forward frees lines for the queen and a bishop). No claims about
  which move is most popular or best.
  Warning callout (about 50 words): the four-move checkmate beginners fall for: White's
  queen and bishop both aim at f7, which only Black's king defends. The game 1.e4 e5 2.Bc4
  Bc5 3.Qh5 Nf6 4.Qxf7# ends in checkmate; as Black, when the queen and a bishop both point
  at f7, defend it (for example with your queen) before anything else. Closing sentence: the
  last fact or an action, no kicker.
- `{#sources}`: don't change it.

## Length

Five minutes front to back, and shorter is fine: about 850 words in guide.md, tables and
sources included. Stay under the word budget for each section. Cut detail, not clarity.

## How to write it

- Regular English, normal word order, "you" for the reader.
- Build one idea at a time. Each paragraph answers the reader's next question.
- No paragraph by list: if it's a list, it goes in a table. Otherwise write connected
  sentences. Short, but not staccato.
- Every term is defined before or where it's first used.
- One name per part, used every time: center, development, castling. American spelling
  (center, memorize).
- No quotes and no names of people. No trivia or history, no named openings (no "Italian",
  "Sicilian").
- The form of the guide (entries, field marks) is structure only. Don't explain it or use its
  vocabulary in the text. No travel, birds or field-guide words. Don't describe the guide.

## Format rules the parser needs

- Typographic quotes and apostrophes (’ “ ”) and the ellipsis character (…). No Markdown
  emphasis, no backticks, no list lines, no "&", no "<" except `<br/>` in a `#` title. No
  "e.g." or "i.e.".
- No slashes in ordinary words.
- A Short answer cell must not end with a full stop.
- No sentence in a table row starts with "It", "Its", "They" or "This".
- No em dashes, no semicolons, no exclamation marks.

## Keep the shape

Keep the front matter keys, every heading and its `{#id ...}`, the number of paragraphs in
each section, table header rows, first-column labels in the terms and field-mark tables, the
diagram block, the callout's first line and the sources section. Don't add or remove sections,
paragraphs or table rows.

When you're done, reply with one line: done.
