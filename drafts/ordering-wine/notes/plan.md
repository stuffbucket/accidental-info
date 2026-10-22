# Plan: An Accidental Guide to… Ordering Wine for the Table

Slug `ordering-wine`. Builder copied with `new_guide.py` from `drafts/hosting-thanksgiving/`
(itself `guides/specs-and-reviews/` with a blocks-only overview page and no mono
literals). Target about 1,000 to 1,100 printed words, 7 or 8 pages. Facts only from
`sources.md`.

## The reader

Someone at a restaurant dinner who has just been handed the wine list, because they're
hosting, paying, or sitting nearest the server. They drink wine but don't know grape names,
can't tell what "dry" promises, have heard that the second-cheapest bottle is a trap, and
dread the moment the server pours them a taste while everyone watches.

## The question

How do I order wine for the table?

## The answer, in order

1. You don't need to know much: a price, a rough style and a willingness to ask.
2. How ordering goes, step by step: set a price, look at the list, tell the server what
   you're eating, what you like and your price band, check the label, taste for faults,
   pour for the table. A bottle pours about five glasses.
3. Wine list: the menu of wines, with prices by the bottle and often by the glass. You only
   need the numbers to start.
4. Grape: the variety on the label or list. A few names, by body: Pinot Noir light red,
   Merlot medium, Cabernet Sauvignon full red, Chardonnay often a full white, Riesling often
   off-dry.
5. Dry: not sweet. All perceptible sugar fermented to alcohol. Off-dry means a little left.
   A second, different sense is how a wine feels in your mouth.
6. Price: markups run 50 to 400 percent. The second-cheapest-bottle trap is a myth: in a
   study of 235 London wine lists its markup was below the next four bottles'. Give the
   server a price band.
7. Taste: the small pour is for faults, not liking. Corked wine smells musty, like wet
   cardboard. Check the label first.

## Key concepts

Five, each with a page and a filled tile. Colours follow the registry's families by kind of
thing.

| No. | Part | Key | Colour | Meaning (draft) |
|---|---|---|---|---|
| 01 | Wine list | Wn | purple (Wr, things you write down) | The restaurant's menu of wines and prices. |
| 02 | Grape | Gr | red-orange (Us, things you use) | The variety a wine is made from, often its name on the list. |
| 03 | Dry | Dy | blue (Nu, numbers and claims) | A claim about sugar: not sweet. |
| 04 | Price | Pr | pink (Dm, decisions people make) | The price band you pick before you read names. |
| 05 | Taste | Ta | green (Ck, things that check) | The small pour you check for faults. |

Codes checked against `registry.md` and `list_concepts.py`: `Wn`, `Gr`, `Dy`, `Pr`, `Ta`
are unused (`Tp` is Transport, `Pe` Permissions, `Pl` Plugin, `Wi` Work item). Wine list was `Wl` in the first draft, changed to `Wn` because `Wl` reads as "WI" in the typeface.

Plain words, no tile: server, sommelier, vintage, cork, by the glass, corked.

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover | 50 |
| 2 | `{#why}` How do you order wine for the table? | Two paragraphs, terms in a grey block | 150 |
| 3 | `{#fit}` How does ordering go? | One sentence, grey Step / What to do table, callout | 150 |
| 4–6 | `{#entry}` × 5 | Two to a page | 5 × 95 |
| 7 | `{#apart}` Common questions | How many bottles, glass or bottle, the cork, sending it back | 120 |
| 8 | `{#sources}` Sources | Nine sources | 130 |
| | | Total | about 1,075 |

No diagram: the steps table is the visual.

## Entries

Field mark labels, the same on every entry: Rule of thumb, Watch for.

| Entry | Identify by | Confused with |
|---|---|---|
| Wine list | A separate menu, or pages at the back | Wines by the glass |
| Grape | A name such as Pinot Noir before the producer or region | Region (a place name such as Chablis) |
| Dry | The word on a list or label, or what a server asks | Dry mouthfeel (tannin) |
| Price | The column of numbers | Second-cheapest bottle |
| Taste | The small pour the server gives the host | Liking it |

"Region" as Confused with for Grape: Decanter mentions Chablis and Rioja as wines people
ask for by name. The guide may say a list names some wines by place instead of grape,
which the Decanter article's examples (Chablis, Rioja, Muscadet, Condrieu) show. No
further claim about which grape a region uses (not in sources).

## Tone

Calm and a little dry. The taste ritual is the anxious moment, so the Taste entry should
leave the reader relieved. One light line at most.

## Builder changes

- `build_guide.py`: `PART_FAMILY`, `NAME2MONO`, `COVER_LINES` ("Ordering Wine", "for the
  Table"; set by hand, the script's split read badly), `SEQ_TILE` (unused).
- `content.py`: the voice comment.

## The writer

`gpt-5.6-sol-fast` through `run_writer.sh`: `writer-round1.md`, then `EDITS-2.md` and on.

## Open questions

- The second-cheapest study is a 2021 working paper on London restaurants in 2015. The
  guide says so briefly (London, one study) rather than claiming it for every country.
