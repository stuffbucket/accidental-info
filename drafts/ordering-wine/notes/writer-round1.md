# Writing instructions, round 1: An Accidental Guide to… Ordering Wine for the Table

You are writing one file: `drafts/ordering-wine/guide.md` (from your working directory it
is `./guide.md`). It holds PLACEHOLDER text that shows the shape the builders expect.
Replace every PLACEHOLDER with finished text. Don't touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

## Read first, in this order

1. `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`: the author's feedback. Binding.
2. `packages/editorial/skills/accidental-guide-write/references/voice.md`: his voice. Binding.
3. `packages/editorial/skills/accidental-guide-write/references/banned-patterns.md`: what never goes in. Binding.
4. `drafts/hosting-thanksgiving/guide.md`: a finished guide in the same series and layout.
   Match its register, row lengths and density. Don't copy its topic.
5. `drafts/ordering-wine/notes/plan.md`: the page plan. Follow it.
6. `drafts/ordering-wine/notes/sources.md`: every fact you may use. Use no fact that isn't
   there.

The AI-topic rules in those files (harness, agent, base guide) don't apply here. Everything
about voice, sentences, rows and banned patterns does.

## Who it's for

Someone at a restaurant dinner who has just been handed the wine list, because they're
hosting, paying or nearest the server. They drink wine but can't name many grapes, don't
know what "dry" promises, have heard the second-cheapest bottle is a trap, and dread the
moment the server pours them a taste while everyone watches. The author wants a calm,
plain read with a light, dry, warm touch at most: one line of understatement in the whole
guide is plenty, and it must also say something useful. No jokes with a set-up, no
exclamation marks, no snark, no wine-snob vocabulary.

## The question, and the answer in order

How do I order wine for the table?

1. You need less than you think: a price, a rough idea of what you like, and a question for
   the server.
2. How ordering goes, step by step (the `{#fit}` table).
3. Wine list: the restaurant's menu of wines and prices. Start with the numbers.
4. Grape: the variety a wine is made from. A few names, by body (how heavy and rich it
   tastes): Pinot Noir is a light red, Merlot sits in the middle, Cabernet Sauvignon is a
   full red, Chardonnay is often a full white because of oak, and Riesling is often a
   little sweet (off-dry).
5. Dry: not sweet. In a dry wine all the sugar you could taste has turned to alcohol.
   Off-dry means a bit of sugar is left.
6. Price: restaurants mark wine up by anywhere from 50 to 400 percent. The second-cheapest
   bottle has a reputation as the worst deal on the list, but one study of 235 London wine
   lists found its markup was lower than the next four bottles'. Give the server a price
   band.
7. Taste: the small pour is to check the wine isn't faulty, not to decide if you like it.
   Corked wine smells musty, like wet cardboard. Check the label before it's opened.

## Length

About 950 words in guide.md, sources included, which prints as about 1,050. Rough budget:
why 140, fit 140, each entry 90, common questions 110. Cut detail, not clarity. Short, but
not staccato.

## What goes where

Front matter: replace PLACEHOLDER in `subtitle` so it reads "A pocket-sized guide to <four
to eight words>." Change nothing else.

`{#why}`: paragraph 1 (about 45 words) answers the question and stands alone (the website
shows it by itself). Paragraph 2 (about 30 words) leads into the five terms. Terms table:
one plain defining sentence per term, under 14 words.

`{#fit}`: one or two sentences, then the steps table. Keep the Step labels exactly. Each
What-to-do cell is one or two short sentences:

- Pick a price: decide what you'll spend per bottle before you read any names.
- Open the list: find that price, and look at whites, reds or sparkling as you like.
- Ask the server: say what you're eating, what you like and don't, and your price band.
  You can point to a price on the list. (Decanter: "a price band to work within".)
- Check the label: the producer, the wine and the year (vintage) match what you ordered.
- Taste: a small pour for the host. Smell it and sip it, to check it isn't faulty.
- Pour for the table: nod, and the server pours for everyone.

The callout: a practical tip, such as a bottle pours about five glasses (750 ml, 5-ounce
glasses), so count about one bottle for every five glasses you expect. One or two
sentences.

Entries: Identify by, What, So what, then two field marks (Rule of thumb, Watch for) as
short answers of three to six words with no full stop, then Confused with in two flat
sentences. About 90 words each. Keep entries short: two entries share each page.

- What: the first sentence is a definition that reads alone in bold ("Dry means …",
  "A wine list is …"). Then what it does.
- So what: the first sentence says why it matters, readable alone in bold.
- No sentence in a row starts with "It", "Its", "They" or "This".

Confused with:
- Wine list / Wines by the glass: some wines are sold by the glass as well as the bottle.
  By the glass suits a table whose dishes need different wines (Decanter).
- Grape / Region: some wines are listed by the place they come from, such as Chablis or
  Rioja, instead of by grape. Ask the server which grape and style a place name means.
- Dry / Dry mouthfeel: a dry wine is one that isn't sweet. A wine can also feel drying in
  your mouth, which is about tannin, not sugar.
- Price / Second-cheapest bottle: the reputation, and what the study found (London, 235
  wine lists, lower markup than the next four bottles). Keep it to two sentences.
- Taste / Liking it: the taste checks for faults. If you don't like a sound wine, you can
  ask kindly for another, but the restaurant doesn't have to replace it. Keep it fair and
  plain.

`{#apart}` Common questions, one or two sentences each, from `sources.md`:

- How many bottles? A 750 ml bottle pours about five 5-ounce glasses.
- Glass or bottle? By the glass helps when the table's dishes are very different. For a
  large table, order a few bottles.
- Do I smell the cork? No need. Little can be told from it, and the presentation of the cork
  is mostly for show.
- What if I don’t like it? The taste is for faults. If it smells musty, mouldy or flat, ask
  for another bottle. If it's sound and you don't like it, you can ask, kindly.

Leave `{#sources}` exactly as it is.

## How to write it

- Regular English, normal word order, "you" for the reader.
- Build one idea at a time. No paragraph by list. Lists go in tables.
- No names of people. No quotes. Publishers' names (Decanter, Wine Spectator) stay on the
  sources page only. Say "one study of 235 London restaurants" without naming its authors.
- Grape and place names (Pinot Noir, Chablis) are fine and needed.
- Write money as "50 to 400 percent". No currency amounts.
- Typographic apostrophes and quotes (’ “ ”). No em dashes, semicolons, exclamation marks,
  "&", slashes in words, backticks or emphasis.
- Never write about the guide itself: no "this guide", "below", "this page".

## Keep the shape

Keep the front matter keys, every heading and its `{#id ...}`, the number of paragraphs in
each section, table header rows, first-column labels, the `> ` grey-block markers, the
`> [!TIP]` callout and the field mark labels. Don't add or remove sections or rows.

When you're done, reply with one line: done.
