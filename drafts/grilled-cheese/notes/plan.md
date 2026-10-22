# Plan: An Accidental Guide to… Grilled Cheese

Slug `grilled-cheese`. Builder copied with `new_guide.py` from `drafts/hosting-thanksgiving/`,
which is `guides/specs-and-reviews/` with a blocks-only overview page and no mono
literals (see that guide's plan). Target about 900 to 1,100 printed words, 6 or 7 pages.
Facts only from `sources.md`.

## The reader

Someone who has been asked to make lunch, or a hungry adult who keeps burning the bread
while the cheese stays cold. They can use a frying pan. They've probably heard a strong
opinion about mayonnaise and don't know whom to believe.

## The question

How do I make a good grilled cheese?

## The answer, in order

1. Four things: bread, cheese, butter and heat. The trick is melting the cheese before the
   bread burns.
2. The method, step by step: medium-low heat, butter melted in the pan, sandwich in,
   golden, flip with more butter, golden again.
3. Bread: sliced white is the usual, sturdy breads work, airy ones leak.
4. Cheese: a melting cheese (American, sharp cheddar, Swiss). Shredded melts faster. Hard
   and aged cheeses stay on the cheese board.
5. Butter: about a tablespoon per sandwich, half in the pan for each side. Many recipes
   butter the bread instead, and that works too.
6. Heat: medium-low, 3 to 5 minutes a side, until golden. Too hot browns the bread before
   the cheese melts.
7. The arguments: bread or pan, butter or mayonnaise, lid or no lid, pressing.

## Key concepts

Four. Colours follow the registry's families by kind of thing.

| No. | Part | Key | Colour | Meaning (draft) |
|---|---|---|---|---|
| 01 | Bread | Br | red-orange (Us, things you use) | The two slices that toast golden on the outside. |
| 02 | Cheese | Cs | red-orange (Us) | A cheese that melts, in the middle. |
| 03 | Butter | Bu | red-orange (Us) | The fat that browns the bread, melted in the pan. |
| 04 | Heat | He | pink (Dm, decisions people make) | How high you set the burner: medium-low. |

Three tiles share a colour because bread, cheese and butter are the same kind of thing.
Heat is a setting you choose, like the registry's Settings and Permissions.

Codes checked against `registry.md` and `list_concepts.py`: `Br`, `Cs`, `Bu`, `He` are
unused. Cheese can't be `Ch` (Check owns it).

Plain words, no tile: pan, mayonnaise, lid, panini press.

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover | 45 |
| 2 | `{#why}` What makes a good grilled cheese? | Two short paragraphs, terms in a grey block | 140 |
| 3 | `{#fit}` How does it come together? | One sentence, a grey Step / What to do table, a callout | 150 |
| 4–5 | `{#entry}` × 4 | Two to a page | 4 × 100 |
| 6 | `{#apart}` What’s worth arguing about? | Grey Question / Answer table: bread or pan, butter or mayonnaise, lid, pressing | 120 |
| 7 | `{#sources}` Sources | Four sources | 70 |
| | | Total | about 930 |

No diagram: the steps table is the visual.

## Entries

Field mark labels, the same on every entry: Rule of thumb, Watch for.

| Entry | Identify by | Confused with |
|---|---|---|
| Bread | Two slices from a sliced loaf | Panini (a press cooks both sides at once) |
| Cheese | Slices or a handful of shredded cheese | Hard cheese (Parmesan, Manchego) |
| Butter | A pat melting in the pan | Mayonnaise (spread on the bread, higher smoke point) |
| Heat | The burner knob, a little below the middle | Lid (traps heat, may steam the bread) |

## Tone

The arguments are meant to be fun, so one dry line is welcome on the arguments page or the
first page. State the method plainly, give the butter-the-bread and mayonnaise camps their
due, and don't pick fights.

## Builder changes

- `build_guide.py`: `PART_FAMILY`, `NAME2MONO`, `COVER_LINES` ("Grilled", "Cheese"),
  `SEQ_TILE` (unused). Everything else as in hosting-thanksgiving.
- `content.py`: the voice comment.

## The writer

`gpt-5.6-sol-fast` through `run_writer.sh`: `writer-round1.md`, then `EDITS-2.md` and on.
