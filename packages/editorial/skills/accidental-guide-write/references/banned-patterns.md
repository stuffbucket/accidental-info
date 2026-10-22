# Banned patterns

Mannered prose draws attention to itself instead of to the point. None of it goes in a
guide. `scripts/lint_guide.py` finds most of the markers below by pattern; the rest only a
reader finds, so read the pages too.

## Mannered prose

| Pattern | Example | Write instead |
|---|---|---|
| Paragraph by list | Four definitions strung together as one paragraph | A table, or connected sentences that build one idea at a time |
| Stiff generic subject | "A person can…", "One may…", "A team that…" | "You can…", or name who does it |
| Embedded question | "…explains what a software factory is." | Ask it plainly: "What is a software factory?" |
| Vague stand-in | "the steps around the agent session", "behind", "on top of" | Name the real thing |
| Slogan or tagline | "The context is the product." | The fact |
| Rhetorical question | "So why won’t your skill run?" | The answer: "When a skill doesn’t run, check the description first." Plain questions are fine as titles and in question-and-answer tables. |
| "Not X but Y" flourish | "It’s not a tool, it’s a system." | Say what it is. A plain correction of a common misreading is fine once: "Permissions are set in the harness, not by the model." |
| Triplets for rhythm | "Fast, cheap and everywhere." | List what matters, however many there are |
| Em-dash aside | "The harness — not the model — decides." | Two sentences, or a comma |
| Colon reveal | "The result: chaos." | "As a result, …" |
| Drama fragments | "Then it broke. Silently." | "It failed without an error." |
| Kicker ending | A page that ends on an aphorism | End on the last fact or the action |
| Throat-clearing | "It’s worth noting that…", "At its core" | Delete |
| Filler and inflated words | simply, just, really, actually, leverage, unlock, seamless, robust, crucial, journey, delve | The ordinary word, or nothing |
| Stacked metaphors | "A well-oiled machine humming along the line" | No metaphor. One light everyday image, once, if it explains something |
| Personification | "The model wants…" | "The model writes a tool call." |
| Synonyms for variety | "the loop", "the runtime" for the harness | The defined term, every time |
| Pronoun-led rows | "It runs on each call." | "The harness runs on each call." |
| Sarcasm or snark | Any | A dry, light touch at most |

## Self-narration and format leakage

The guide never talks about itself, its sources or its layout, and never borrows the voice of
a video, a presenter or a travel guide.

| Kind | Examples | Fix |
|---|---|---|
| Self-narration | "this guide", "this page", "the series", "the table below", "as noted above", "here’s", "let’s" | Start with the content. One sentence on how to read a figure is fine ("Solid arrows are requests and dashed arrows are results.") |
| Unnamed voices | "speakers mean", "people say", "some argue" | Say what the thing is |
| Hooks and teasers | Teaser titles, set-up and reveal, "they say X, we say Y" | Plain titles that name the concept |
| Borrowed framing | birds, species, sightings, field guide, in the wild, travel, episodes | Leave the form model out of the words |
| Trivia and history | Who coined a term, a 1968 paper | Cut it |
| Process narration | "We set out to…", "Our research found…", "None found in the sources read" | The finding, as a fact about the topic |
| Jargon | A team's stage names, an acronym with no gloss | Plain words, or define it where it first appears |

## People, quotes and claims

- No direct quotes and no names of people in the body. Keep the idea, drop the quote and the
  name. Sources go on the last page.
- No claims about what "most teams" or "most people" do.
- No praise or blame of a product, vendor or team.
- No non-public company names or details. Keep a local deny list of the names you must never
  print, outside the repository, in `~/.config/accidental-guides/denylist.txt` or the path
  in `ACCIDENTAL_GUIDE_DENYLIST`. The lint reads it (see `templates/denylist.example.txt`).

## Text rules for guide.md

The builders print what isn't one of these constructs literally, so:

- No backticks and no emphasis. Bold and mono are applied by rule.
- No list lines. A line starting `- ` prints as part of a paragraph. Use a table.
- No `&` directly before letters (ReportLab reads `R&D` as an entity). Write "and".
- No `<` except `<br/>` in a `#` title.
- No slashes in ordinary words ("and/or", "CI/CD"): anything shaped like a path is set in mono.
- No "e.g. " in the first sentence of What or So what. The builder bolds up to the first
  ". ".
- A Short answer cell doesn't end with a full stop. The builder adds one.
- Typographic quotes and apostrophes (’ “ ”) and the ellipsis character (…).
- Keep the shape: section ids, the number of paragraphs in each section, table header rows
  and first-column labels. `content.py` takes text by position, so an extra paragraph moves
  text into the wrong slot or stops the build.
