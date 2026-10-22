# Page checklist

Apply to one page at a time, against the page image and the page's section in `guide.md`.
Each item is yes or no.

## The page

- [ ] The page is about one concept, and its title names that concept.
- [ ] An entry has every row, in the same order as every other entry.
- [ ] The first sentence of What defines the part and reads correctly in bold on its own.
- [ ] Every Short answer reads on its own in bold and has no full stop in `guide.md`.
- [ ] The build printed `no overflow`, and the image shows nothing past the right edge, no
      colliding diagram labels and no title under the corner tile.
- [ ] Nothing was cut mid-thought to make it fit.

## Flow

- [ ] The page builds on what came before. Nothing assumes depth the reader doesn't have.
- [ ] Each paragraph answers the reader's next question, and one subject runs through it.
- [ ] No paragraph is a list in disguise.
- [ ] Questions are asked plainly ("What is X?"), never as "what X is".

## Terms

- [ ] Every term is defined before or where it's first used, here, earlier, or in the guide
      this one builds on.
- [ ] Each part has one name, used every time. No synonyms, no product name as a category.
- [ ] Part names that label rows, steps or Confused with match `NAME2MONO`, so they get their
      tile.
- [ ] Literals come out in mono, and no ordinary word does.

## Voice

- [ ] Sentences are short, one idea each, mostly under 20 words, but not staccato.
- [ ] No row sentence starts with "It", "Its", "They" or "This".
- [ ] Point first, then reason.
- [ ] No slogans, rhetorical questions, "not X but Y" flourishes, rhythm triplets, em dashes,
      colon reveals, drama fragments, kicker endings or personification.
- [ ] No throat-clearing, "let's", "simply", "just" or inflated words.
- [ ] At most one light image, only if it explains something.
- [ ] Uncertainty is stated as what the sources say, with a frequency word or a date.
- [ ] No praise or blame of a product, vendor or team. No claims about what most teams do.

## Nothing about the guide itself

- [ ] No "this guide", "this page", "below", "as noted above", "here's".
- [ ] No unnamed voices, hooks, trivia or borrowed framing.
- [ ] A sentence about a figure says only how to read it.

## Sources and names

- [ ] No quotes or names of people in the body.
- [ ] No non-public names or material.
- [ ] Every fact is in `sources.md`, and every source listed is used.
- [ ] Cross-references to other guides use the colon form and that guide's meanings.

## Markdown

- [ ] No backticks, emphasis, list lines, `&` before letters, or `<` except `<br/>` in a title.
- [ ] Typographic quotes and apostrophes.
- [ ] If the text changed, the version was bumped and `expected.sha256` holds the new hash.
