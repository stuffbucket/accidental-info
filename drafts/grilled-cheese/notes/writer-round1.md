# Writing instructions, round 1: An Accidental Guide to… Grilled Cheese

You are writing one file: `drafts/grilled-cheese/guide.md` (from your working directory it
is `./guide.md`). It holds PLACEHOLDER text that shows the shape the builders expect.
Replace every PLACEHOLDER with finished text. Don't touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

## Read first, in this order

1. `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`: the author's feedback. Binding.
2. `packages/editorial/skills/accidental-guide-write/references/voice.md`: his voice. Binding.
3. `packages/editorial/skills/accidental-guide-write/references/banned-patterns.md`: what never goes in. Binding.
4. `drafts/hosting-thanksgiving/guide.md`: a finished guide in the same series and layout,
   on a cooking topic. Match its register, row lengths and density. Don't copy its topic.
5. `drafts/grilled-cheese/notes/plan.md`: the page plan. Follow it.
6. `drafts/grilled-cheese/notes/sources.md`: every fact you may use. Use no fact that isn't
   there.

The AI-topic rules in those files (harness, agent, base guide) don't apply here. Everything
about voice, sentences, rows and banned patterns does.

## Who it's for

Someone who has been asked to make lunch, or keeps burning the bread while the cheese stays
cold. They can use a frying pan. They've heard strong opinions about mayonnaise and don't
know whom to believe. The author wants this one to be a little fun: grilled cheese starts
arguments, and that's fine. State the method plainly, give the other camps their due in a
sentence each, and let one dry line of understatement through (on the first page or the
arguments page, not both). No jokes with a set-up, no exclamation marks, no snark.

## The method to state plainly

Butter the pan, not the bread, and keep the heat low so the bread doesn't burn before the
cheese melts. Concretely, per sandwich: a skillet over medium-low heat; melt about half a
tablespoon of butter and swirl it round the pan; lay the sandwich in; cook without pressing
until the bottom is golden, about 3 to 5 minutes; lift it, melt the rest of the butter (about
half a tablespoon), lay it back down on its other side; cook about 3 to 4 minutes, until
golden and the cheese has melted. Those numbers are all in `sources.md` (1 tablespoon of fat
per sandwich, medium-low, 3 to 4 or about 5 minutes, no pressing, butter melted in the
skillet and more after the flip).

Be fair: plenty of recipes spread butter on the outside of the bread instead, and that works
too. Say so plainly once, on the Butter entry or in the arguments, not in every row.

## The question, and the answer in order

How do I make a good grilled cheese?

1. Four things: bread, cheese, butter and heat. The whole job is melting the cheese before
   the bread burns.
2. The method, step by step (the countdown-style table on `{#fit}`).
3. Bread: sliced white bread is the usual choice; sourdough, rye or brioche also work; airy
   bread such as focaccia lets cheese seep through and burn.
4. Cheese: a melting cheese such as American, sharp cheddar or Swiss. Shredded melts faster
   than sliced. Save Parmesan and Manchego for a cheese board.
5. Butter: about 1 tablespoon per sandwich, half in the pan for each side. The bread soaks
   it up from the pan.
6. Heat: medium-low, 3 to 5 minutes a side, until golden. Too high browns the bread before
   the cheese melts.
7. The arguments: butter on the bread or in the pan; butter or mayonnaise (mayonnaise has a
   higher smoke point than butter, so it browns without burning); lid or no lid (a lid
   traps heat and melts the cheese faster, and it can also steam the bread soggy); pressing
   (don't).

## Length

About 850 words in guide.md, sources included, which prints as about 950. Rough budget: why
130, fit 140, each entry 95, arguments 120. Cut detail, not clarity. Short, but not
staccato.

## What goes where

Front matter: replace PLACEHOLDER in `subtitle` so it reads "A pocket-sized guide to <four
to eight words>." Change nothing else.

`{#why}`: paragraph 1 (about 45 words) answers the question and stands alone (the website
shows it by itself). Paragraph 2 (about 30 words) leads into the four terms. Terms table:
one plain defining sentence per term, under 14 words.

`{#fit}`: one or two sentences, then the steps table. Keep the Step labels exactly. Each
What-to-do cell is one or two short sentences. The callout: one practical tip the reader can
act on (for example, shredded cheese melts faster than sliced, so all of it melts before the
bread finishes toasting).

Entries: Identify by, What, So what, then two field marks (Rule of thumb, Watch for) as
short answers of four to eight words with no full stop, then Confused with in two flat
sentences. About 95 words each.

- What: the first sentence is a definition that reads alone in bold ("Butter is …"). Then
  what it does.
- So what: the first sentence says why it matters, readable alone in bold.
- No sentence in a row starts with "It", "Its", "They" or "This".

Confused with:
- Bread / Panini: a panini press closes on the sandwich and cooks both sides at once. A
  grilled cheese cooks one side at a time in an open pan.
- Cheese / Hard cheese: Parmesan and Manchego are hard, aged cheeses kept for a cheese board.
  A melting cheese such as American or cheddar goes in the sandwich.
- Butter / Mayonnaise: mayonnaise is spread on the outside of the bread. It has a higher smoke
  point than butter, so it browns without burning.
- Heat / Lid: a lid traps heat to melt the cheese faster. It can also steam the bread soft.

`{#apart}`: one sentence of lead-in, then four answers of one or two sentences each, fair to
every side, from `sources.md`. Leave `{#sources}` exactly as it is.

## How to write it

- Regular English, normal word order, "you" for the reader.
- Build one idea at a time. No paragraph by list. Lists go in tables.
- No names of people, chefs, restaurants or brands in the body. No quotes.
- Typographic apostrophes and quotes (’ “ ”). No em dashes, semicolons, exclamation marks,
  "&", slashes in words, backticks or emphasis.
- Never write about the guide itself: no "this guide", "below", "this page".

## Keep the shape

Keep the front matter keys, every heading and its `{#id ...}`, the number of paragraphs in
each section, table header rows, first-column labels, the `> ` grey-block markers, the
`> [!TIP]` callout and the field mark labels. Don't add or remove sections or rows.

When you're done, reply with one line: done.
