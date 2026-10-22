# Writing instructions, round 1: An Accidental Guide to… The Last Move in Chess

You are writing one file: `drafts/chess-last-move/guide.md` (from your working directory it is
`./guide.md`). It holds PLACEHOLDER text that shows the shape the builders expect. Replace
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
5. `drafts/chess-last-move/notes/plan.md`: the page plan. Follow it.
6. `drafts/chess-last-move/notes/sources.md`: every fact you may use. Use no fact that isn't
   there. Restate in your own plain words.

## Who it's for

Someone in a casual game, or their first club game, who isn't sure whether the game is over.
Did they win? Is it a draw? Can they just shake hands and go? They know how the pieces move.
The series' spirit is warm, a little self-deprecating and dry: at most one light, dry touch
per page, never jokey. The voice rules win over any wish to be funny.

## The question, and the answer in order

How does a chess game end?

1. A game ends in a win or a draw. You win by checkmate, or when the other player resigns.
   A draw comes from stalemate, agreement, repeating a position, fifty moves without a pawn
   move or capture, or a position where nobody can checkmate. Check is the warning on the way.
   Points: a win is 1, a draw is a half each, a loss is 0.
2. Checkmate or stalemate? The two boards are drawn from the diagram block (don't change it):
   the same three pieces, with the queen one square apart. One paragraph (about 60 words)
   says what to see: in both, Black has no legal move; on the left Black is in check, so it's
   checkmate and White wins; on the right Black isn't in check, so it's stalemate and a draw.
   When you're winning, leave the other king a move.
3. Check, Checkmate, Stalemate, Draw, Resigning: one entry each.
4. How do you finish politely? A Habit / Why table and a closing sentence.

## Section by section

- Front matter: keep it as it is.
- `{#why}` (about 160 words in all). Paragraph 1 is the blurb the website shows, so it must
  stand alone (about 50 words). Paragraph 2 (about 45 words): the score (1, a half, 0) and
  that a game ends the moment checkmate, stalemate or a resignation happens. Paragraph 3: one
  sentence leading into the five terms. Terms table: one short sentence each.
- `{#fit}`: one paragraph, as above.
- Each entry (about 95 words): Identify by (what you see or hear at the board); What (first
  sentence is the definition, genus and difference; it prints bold up to the first ". ");
  So what (first sentence prints bold too); two field marks (Result, Decided by), each a
  short answer of two to six words with no full stop; Confused with, two flat sentences.
  - Check: the king is attacked by an enemy piece. You must get out of it at once, in one of
    three ways: move the king, block the line, or capture the attacker. You may never make a
    move that leaves your own king in check. Written + after a move. Result: the game goes on.
    Confused with Checkmate.
  - Checkmate: check with no legal way out. The game ends at once and the player who gave it
    wins. Written #. Confused with Stalemate.
  - Stalemate: the player to move has no legal move and isn't in check. A draw, and the game
    ends at once. Confused with Any draw: not every draw is a stalemate (US Chess says so
    plainly).
  - Draw: a game nobody wins. Ways: agreement (offer once, after making your move; the offer
    stands until the other player accepts, says no, or touches a piece to move), the same
    position three times (a claim) or five times (automatic), fifty moves each with no pawn
    move and no capture, or a dead position where nobody can checkmate. Confused with A
    handshake: a handshake on its own can be read as a draw by one player and a resignation
    by the other, so say the words.
  - Resigning: ending the game by conceding it. Say "I resign" or tip over your king. The game
    ends at once, and the other player wins (unless they couldn't possibly checkmate, which
    makes it a draw). Confused with Stopping the clock: stopping both clocks isn't the same
    as resigning, because the player may be calling for help with a claim.
- `{#habits}` How do you finish politely? One intro sentence. Six rows, Habit (a short
  imperative, three to seven words) then Why (one sentence): touch only the piece you mean to
  move (touch-move: touch your own piece and you must move it; touch your opponent's and you
  must take it, if you can); say "I adjust" before you straighten a piece; offer a draw once,
  right after your move; resign out loud or by tipping your king; shake hands before and
  after the game; put the pieces back on their starting squares. Closing sentence: the last
  fact or an action, no kicker. (Touch-move and "I adjust" come from FIDE's Basic Rules of
  Play; friends may agree to relax them in a casual game, but say only what the sources say.)
- `{#sources}`: don't change it.

## Length

Five minutes front to back: about 950 words in guide.md, tables and sources included. Stay
under the word budget for each section. Cut detail, not clarity.

## How to write it

- Regular English, normal word order, "you" for the reader.
- Build one idea at a time. Each paragraph answers the reader's next question.
- No paragraph by list: if it's a list, it goes in a table. Otherwise write connected
  sentences. Short, but not staccato.
- Every term is defined before or where it's first used.
- One name per part, used every time: check, checkmate, stalemate, draw, resigning.
- No quotes of people. Short phrases players say ("I resign", "I adjust") are fine in
  typographic quotes. No names of people, no trivia or history, no famous games.
- The form of the guide (entries, field marks) is structure only. Don't explain it or use its
  vocabulary in the text. No travel, birds or field-guide words. Don't describe the guide.

## Format rules the parser needs

- Typographic quotes and apostrophes (’ “ ”). No Markdown emphasis, no backticks, no list
  lines, no "&", no "<" except `<br/>` in a `#` title. No "e.g." or "i.e.".
- No slashes in ordinary words.
- A Short answer cell must not end with a full stop.
- No sentence in a table row starts with "It", "Its", "They" or "This".
- No em dashes, no semicolons, no exclamation marks.

## Keep the shape

Keep the front matter keys, every heading and its `{#id ...}`, the number of paragraphs in
each section, table header rows, first-column labels in the terms and field-mark tables, the
diagram block and the sources section. Don't add or remove sections, paragraphs or table rows.

When you're done, reply with one line: done.
