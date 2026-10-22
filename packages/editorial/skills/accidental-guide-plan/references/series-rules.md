# Series rules

The rules for what goes into an Accidental Guide and how the guides fit together. They come
from the author's review of the first guides. Quotes are his.

## What the guides are for

Most of what's written about AI coding agents is long, comes from someone selling a product,
and uses the same word for different things. Each Accidental Guide answers one question,
uses one name for each thing, keeps that name across the series, and gives the reader a
pointer to the next guide.

The reader is someone with a question and "maybe a passing or perhaps begrudging level of
interest in the topic". Write for an executive, a lead and an engineer at once: the guide
should pass "the sniff test of an executive, lead, and IC who may have been exposed (or not)
to the key concepts."

"Giving them a reason to pick up another guide to read is success. Turning them off or
confusing them is not."

## One question, five minutes

- One plain question per guide, asked the way a reader would ask it: "What is a software
  factory?" Not "what a software factory is".
- "The total time for someone to read through any particular guide from front to back is
  5 minutes or less." That's about 1,100 printed words, tables, diagram labels and sources
  included, counted from the built PDF. Cut detail, not clarity.
- Title short and balanced: "The title is a bit wordy can we get that more into balance."
  Six words or fewer.

## Key concepts

- **Five or fewer.** "Six concepts is quite a lot... If five concepts will do just as well or
  better than six then consider reducing." Four is fine.
- **Each key has a page and a filled tile.** A key is a real thing the reader will meet: a
  file, a program, a setting, a step. A scale, a debate or a history is a plain page, not a
  key. Test: a key has an owner, something starts it or uses it, and it has a place in the
  overview diagram.
- **Each concept is a key in exactly one guide.** Other guides use its name in plain text,
  with no tile, and point to the guide that owns it.
- **No blank boxes.** "Concepts with a blank box ... tell us that we probably have something
  in the guide at the wrong level of detail." Anything that isn't one of the guide's parts is
  plain text in a diagram, as "You" is in the base guide's diagram. Never draw an outlined
  tile, and never add a legend that says something "isn't one of the parts". More than three
  things that want a box means something belongs in another guide.
- **No jargon labels in diagrams**, such as a stage name only one team uses.

## Build up one idea at a time

- Start from what the reader already has. The base guide,
  An Accidental Guide to: Agents, Harnesses, Skills, and Tools, defines model, harness,
  agent, skill, tool, MCP server, session and context window. A turn is one pass of the
  harness loop. A session is the turns from start to finish. Bigger ideas (a factory, a
  plugin, a team process) build on sessions.
- "This jumps in deep very quickly." The first three pages show whether the concepts are
  settled. If page 2 needs five new words to make sense, the guide starts too deep.
- Stay with one subject: "we start out with a person and then switch to a team. Stick with a
  person."

## Scope

- One guide, one idea. Don't bolt on side concepts. If a topic keeps coming up and needs its
  own explanation, it's another guide, and more guides are fine.
- Say plainly which group the guide is about. Don't claim what "most teams" do: "most teams
  don't do any of those things and many people will say that when they work with a team
  that their experience has often been that one person does most of the heavy lifting.
  Those aren't teams. We're talking about teams."
- The base guide is fixed and well reviewed. Never contradict it, don't repeat it, and point
  to it for the basics.
- Shared words keep the meaning the owning guide gives them. A later guide's terms page lists
  only the borrowed words it uses and names the guide they come from. It doesn't redefine them.

## Cross-references

- In body text, the colon form: "An Accidental Guide to: Agents, Harnesses, Skills, and Tools".
- The "…" form ("An Accidental Guide to…") appears only on the cover, as the kicker.
- Inside a guide, point to a thing by its name. Page numbers typed in the text go stale; if
  you use one, check it against the built PDF.

## Form models stay out of the text

The pacing of the guides follows a pocket field guide or a travel guide: short entries laid
out the same way, so they can be compared. That shapes structure only. "There is no
conceptual overlap between birds, species, and software factories. The birding guide was one
example of structure and pacing, not a literal framework to incorporate into the writing
explicitly." No birds, species, sightings, field guides, travel or video words in the text,
and no sentence that explains the guide by analogy to its form. The existing labels
(Identify by, Field marks, Confused with) stay as labels and are never explained.

## Public material only

- Facts come only from public, official documentation and a project's own published
  material.
- No non-public company material of any kind: internal product, team, project, tool or metric
  names, internal URLs, or anything marked confidential. "don't name check non-public
  [company] information or direct quotes from people... just drop the reference and keep the
  idea the quote is trying to convey."
- A guide that ever held internal material isn't published until it's clean.

## Versions

Every guide carries a semver `version:` in its front matter. A first draft is 0.1.0. Each
round of edits bumps it, and the published, reviewed guide is 1.0.0.
