# Plan: An Accidental Guide to… Your First D&D Game

Slug `first-dnd-game`. Builder copied from `guides/specs-and-reviews/` (grey blocks, callouts,
packed pages, the sequence diagram). Target about 1,000 to 1,100 printed words, 8 pages.
Facts only from `sources.md`. Made 22 October 2026.

Writer: gpt-5.6-sol-fast through `run_writer.sh` (the `copilot` CLI answered a test prompt on
22 October 2026, so the writer is used for round 1 and the edit rounds).

## The reader

A friend has invited them to a D&D game, maybe this weekend. They have never played, may
have seen it on TV, and are a little anxious about looking silly or slowing everyone down.
They have read no other Accidental Guide, and this guide shares no concepts with the others.
They need to know what happens at the table, what the funny dice are for, what to look at on
the character sheet, what they can do when it's their turn, and how to be a welcome new
player.

## The question

What happens at a D&D game, and what do I do?

## The answer, in order

1. D&D is a story told together: one Dungeon Master describes the world, everyone else plays
   one character and says what that character does, and dice decide when the result is
   uncertain. The DM isn't your opponent.
2. One roll, start to finish (sequence diagram): the DM describes, you say what your
   character does, the DM asks for a roll, you roll a d20, add the modifier from your sheet,
   say the total, the DM compares it with a target number and narrates.
3. Dungeon Master: who runs the game and decides what to roll.
4. Character sheet: where your numbers are, and the four or five you need.
5. Dice: the d20 for success or failure, the others mostly for damage; how "1d8 + 2" reads.
6. Your turn: in a fight, one move and one action, talking is free.
7. How do you play well? A table of habits, from the publisher's own advice.

## Key concepts

Four. Each has a page, a filled tile and one meaning. Colours reuse the registry's six
families by kind of thing (the registry's families are for software; the closest kind is
used): the DM decides results (Decisions people make, pink); the character sheet is written
down (purple); dice are something you use (red-orange); a turn is something that runs, one
after another (yellow).

| No. | Part | Key | Colour | Meaning (draft) |
|---|---|---|---|---|
| 01 | Dungeon Master | Gm | assistive (pink, Dm family) | The player who runs the game: describes the world, plays everyone else, asks for rolls |
| 02 | Character sheet | Cs | figjam (purple, Wr family) | The page or app that holds your character's numbers and abilities |
| 03 | Dice | Di | danger (red-orange, Us family) | The d4 to d20; the d20 decides success, the others mostly damage |
| 04 | Your turn | Tn | warning (yellow, Ru family) | In a fight: move up to your Speed and take one action |

Codes: `Dm` is a family code, so the Dungeon Master tile is `Gm`, after the rules' other
name for the role (Game Master), which the entry mentions. None of Gm, Cs, Di, Tn is in the
registry or in `list_concepts.py` output. Proposed registry additions: these four, owner
first-dnd-game.

Plain words, no tile: player, character, D20 Test, modifier, Difficulty Class (DC), Armor
Class, Hit Points, action, Speed.

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover, four tiles | 50 |
| 2 | `{#why}` What happens at a D&D game? | Three short paragraphs, then the terms on a grey block | 170 |
| 3 | `{#seq}` One roll, start to finish | Sequence diagram: You, DM, sheet, dice; one ability check | 110 |
| 4–6 | `{#entry}` × 4, packed | Dungeon Master, Character sheet, Dice, Your turn | 4 × 110 |
| 7 | `{#apart}` How do you play well? | Intro sentence, grey Habit / Why table, closing sentence | 150 |
| 8 | `{#sources}` Sources | Five sources, checked 22 October 2026, trademark line | 110 |
| | | Total | about 1,050 |

The sequence page sits right after the terms page (builder change), so the newcomer sees the
whole loop before the parts.

## Entries

Field mark labels, the same on every entry: Who, When, Cannot.

| Entry | Identify by | Confused with |
|---|---|---|
| Dungeon Master | The player at the head of the table who describes the scene | Opponent |
| Character sheet | The printed or app page with your character's name and numbers | Rulebook |
| Dice | The bag of seven-ish odd-shaped dice; d4, d6, d8, d10, d12, d20 | Natural 20 |
| Your turn | In a fight, when the DM calls your name in Initiative order | Bonus Action |

## Cross-references

None. No other guide covers games.

## Builder changes (done by hand, not by the writer)

- `content.py`: `{#fit}` made optional; voice comment for this guide.
- `build_guide.py`: `PART_FAMILY`, `NAME2MONO`, `COVER_LINES` ("Your First", "D&D Game"),
  `SEQ_TILE = "Di"`, the sequence page moved to the front (`FRONT_IDS`), and an `esc()` so
  "D&D" prints (ReportLab reads `&D` as an entity).
- `build_docx.py`: the sequence page's PDF page number and the page order follow
  `FRONT_IDS`.
- The lint flags each "D&D" as Markdown the builder prints literally (MD). The builder
  escapes it, so those MD hits are expected; every other MD hit is a real error.

## Open questions

- Trademark: one line in the sources intro. The SRD's own attribution statement isn't added,
  because the guide restates short facts in its own words and copies no SRD text. Flag for
  the author.
- 2014 and 2024 rules: the guide uses the 2024 Basic Rules and SRD 5.2.1 and says "as of
  October 2026" once.

## Rounds (22 October 2026)

| Round | Brief | By | Result |
|---|---|---|---|
| 1 | writer-round1.md | gpt-5.6-sol-fast via run_writer.sh | First draft, 1,121 printed words |
| Review | review-readers.md, review-fidelity.md, review-leakage.md | cold subagent reviews | Two wrong facts, undefined terms, one overreach, a title printing its markup |
| 2 | EDITS-2.md | gpt-5.6-sol-fast | Fixes applied, 1,192 words |
| 3 | EDITS-3.md | gpt-5.6-sol-fast | Cuts, 1,116 words |
| 4 | EDITS-4.md | gpt-5.6-sol-fast | Cuts, then two one-word trims by the editor: 1,099 words, 5.0 minutes |

Builder fixes during the rounds: `plain_title()` takes a `y` so a back section's title can
break with `<br/>`; `bold_first()` bolds a one-sentence row whole; `COVER_COLS` (two per row
for four parts); an undated source shows no leading dot (PDF and Word).

Entries don't share pages (each is a little over half a page), so the guide is 9 pages.
