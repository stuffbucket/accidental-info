# Writing instructions, round 1: An Accidental Guide to… Your First D&D Game

You are writing one file: `drafts/first-dnd-game/guide.md` (from your working directory it is
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
5. `drafts/first-dnd-game/notes/plan.md`: the page plan. Follow it.
6. `drafts/first-dnd-game/notes/sources.md`: every fact you may use. Use no fact that isn't
   there. Restate rules in your own plain words. Never copy sentences from the sources.

## Who it's for

A friend has invited them to play Dungeons & Dragons, maybe this weekend. They have never
played and are a little nervous about looking silly or slowing the table down. They don't
know what the odd dice are for, what to look at on the sheet someone handed them, or what
they're allowed to do when it's their turn. The series' spirit is warm, a little
self-deprecating and dry, in the way of a friend who has been there: at most one light,
dry touch per page, never jokey, never snark. The voice rules win over any wish to be funny.

## The question, and the answer in order

What happens at a D&D game, and what do I do?

1. D&D is a story told together. One player, the Dungeon Master (DM), describes the world and
   plays everyone else in it. Each other player plays one character and says what that
   character tries to do. When the result is uncertain, the DM asks for a roll. The DM isn't
   your opponent.
2. One roll, start to finish: the sequence diagram (already written, don't change it) shows
   the loop. The intro says what it follows. The closing note says the numbers are an
   example, that 15 is a medium target, and that you don't need to know the target number.
3. Dungeon Master, Character sheet, Dice, Your turn: one entry each.
4. How do you play well? Six habits, each with why it helps.

## Section by section

- Front matter: keep it as it is.
- `{#why}` (about 170 words in all). Paragraph 1 is the blurb the website shows, so it must
  stand alone: what D&D is, who does what, and that dice settle what's uncertain (about 50
  words). Paragraph 2: what you need to know for a first game is small. You don't need the
  rules; the DM tells you what to roll, and your character sheet has your numbers (about 45
  words). Paragraph 3: one sentence that leads into the four terms. Terms table: one short
  sentence each.
- `{#seq}`: intro (one or two sentences, about 25 words: the diagram follows one moment, such
  as trying to sneak past a guard). Closing note (one or two sentences, about 35 words).
  Don't touch the diagram block.
- Each entry (about 110 words): Identify by (where you see it at the table); What (first
  sentence is the definition, genus and difference, and prints bold up to the first ". ");
  So what (first sentence prints bold too); three field marks (Who, When, Cannot), each a
  short answer of two to six words with no full stop; Confused with, two flat sentences.
  - Dungeon Master: mention once that the rules' reference document calls the role the Game
    Master. Confused with Opponent: the DM plays the monsters but isn't against you (sourced).
  - Character sheet: printed, in an app or on plain paper. Name the few numbers a newcomer
    uses: ability modifiers, Armor Class, Hit Points, Speed, attack bonus. Confused with
    Rulebook: you're not expected to know every rule; know roughly what your character can
    do.
  - Dice: d4, d6, d8, d10, d12, d20; the d20 decides success or failure; the others mostly
    roll damage; how to read "1d8 + 2" (give your own small example in the same form as the
    source's "3d8 + 5"). Confused with Natural 20: a natural 20 on an attack roll always hits;
    the rules make that exception for attack rolls.
  - Your turn: in a fight, turns go in Initiative order; on your turn you can move up to your
    Speed and take one action, such as Attack, Dash, Help or Hide; talking briefly is free;
    if you can't decide, the Dodge action is a safe choice. Confused with Bonus Action: you
    get one only when a feature, spell or ability on your sheet says so.
- `{#apart}` How do you play well? One intro sentence. Six rows: Habit (a short imperative,
  three to seven words) and Why it helps (one sentence). Take them from source 5 and the
  Basic Rules: know roughly what your character can do; bring dice, a pencil and paper; plan
  your turn while others take theirs; listen first, talk second, and give everyone a chance
  to shine; say what your character does and let the DM tell you what to roll; choose actions
  the whole table enjoys. Closing sentence: the last fact or an action, such as asking the DM
  when you're unsure. No kicker.
- `{#sources}`: don't change it.

## Length

Five minutes front to back: about 950 words in guide.md, tables and sources included, which
prints as about 1,050. Stay under the word budget for each section. Cut detail, not clarity.

## How to write it

- Regular English, normal word order, "you" for the reader.
- Build one idea at a time. Each paragraph answers the reader's next question.
- No paragraph by list: if it's a list, it goes in a table. Otherwise write connected
  sentences. Short, but not staccato.
- Every term is defined before or where it's first used. Say "Dungeon Master (DM)" the first
  time in the body, then "DM".
- Each part has one name, used every time: Dungeon Master, character sheet, dice, your turn.
  Rules terms keep the rules' capitals: Armor Class, Hit Points, Speed, Initiative, Bonus
  Action, D20 Test (only if you use it).
- No quotes and no names of people. No trivia, history, or edition talk beyond "as of October
  2026" once if needed.
- The form of the guide (entries, field marks) is structure only. Don't explain it or use its
  vocabulary in the text. No travel, birds or field-guide words.
- The words "game", "story", "table" are fine. Don't describe the guide or its pages.

## Format rules the parser needs

- Typographic quotes and apostrophes (’ “ ”). No Markdown emphasis, no backticks, no list
  lines, no "&" except inside "D&D" and "Dungeons & Dragons", no "<" except `<br/>` in a `#`
  title. No "e.g." or "i.e.".
- No slashes in ordinary words ("and/or").
- A Short answer cell must not end with a full stop.
- No sentence in a table row starts with "It", "Its", "They" or "This".
- No em dashes, no semicolons, no exclamation marks.

## Keep the shape

Keep the front matter keys, every heading and its `{#id ...}`, the number of paragraphs in
each section, table header rows, first-column labels in the terms and field-mark tables, the
diagram block and the sources section. Don't add or remove sections or paragraphs.

When you're done, reply with one line: done.
