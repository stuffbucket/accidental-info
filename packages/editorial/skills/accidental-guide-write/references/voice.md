# Voice

The guides are written in the author's voice: plain, direct and factual. State the point,
then the reason. Explain the way a colleague would over coffee, to a smart person who is new
to the topic. Nothing is there to sound good.

The best sample of the voice is the base guide, `guides/agents-harnesses-skills-tools/guide.md`.

## His own words, as samples

These are from working sessions, so they are more clipped than guide prose. The guide voice
keeps the same habits: plain words, a point and then the reason, no decoration.

> We want to develop a series of Accidental Guides that follow the pattern of our existing
> Accidental Guide for Agents, Skills, and Harnesses that uses the same ubiquitous language
> design, visual design and generation pipeline.

> The result should pass the sniff test of an executive, lead, and IC who may have been
> exposed (or not) to the key concepts. Where necessary refer to other Accidental Guides.
> Keep concepts to one page with any (hopefully brief) addenda to the appendix of the guide.
> Where possible a visual approach is desired.

> This jumps in deep very quickly. The text starts out great and then each concept that
> follows is disjointed definitions strung together to form a paragraph by list. "Paragraph
> by list" where the entire paragraph could be a list is a bad writing style that models
> often exhibit.

> conceptually this is not the place to introduce a trivia nugget.

> there is quite a bit of jargon and assumption. Nobody is speaking to this person.

What to take from them:

- He says what he sees, then what it means: "The text starts out great and then…".
- Ordinary words: "sniff test", "fairly decent", "a little more". No vocabulary chosen to
  impress.
- Hedges only where he is unsure ("hopefully brief").
- Names the thing exactly once it matters ("Paragraph by list").
- Sentences run as long as the thought needs. Commas, not dashes.
- No slogans, flourishes, set-up and reveal or rhetorical questions.

## Sentences from the base guide

1. "The model only knows what’s in its context window."
2. "If something isn’t in the context window, the model can’t see it."
3. "A model can’t open a file or run a command."
4. "Skills and sub-agents don’t act on their own."
5. "Permissions are set in the harness, not by the model."
6. "When answers are poor, check what was in the context window before you switch models."
7. "The description is what triggers a skill, so when a skill doesn’t run, check the
   description first."
8. "A skill is text the model reads."
9. "The model never talks to a tool directly. The harness runs every call."
10. "Each product names these parts a little differently, and some words get used for more
    than one part."

## Sentences

Measured on the base guide: mean 14 words, median 13. About half are 12 words or fewer.
Fewer than one in ten runs past 25 words, and those are lists of real things.

- **One idea per sentence.** Two short sentences rather than one with a clause hanging off it.
  Short, but not staccato: vary the length the way speech does.
- **Subject first.** Most sentences start with the name of the thing: "A harness is…",
  "The model has no memory between calls…".
- **Name the subject every time in rows.** No row sentence starts with "It", "Its", "They" or
  "This". Readers jump to a row, so each one has to read on its own.
- **Point, then reason.** "X, so Y" and "When X, check Y." The base guide uses "so" 18 times
  and "because" once.
- **Conditions lead.** "When the window fills up, the harness trims or summarizes older
  content to make room."
- **Instructions are imperatives to "you".** "Check the description first."
- **Lists in a sentence** use commas and "and" or "or", with no serial comma.
- **Punctuation:** full stops and commas, a colon only to introduce an example or a list. No
  em dashes, semicolons or exclamation marks. Contractions are normal: isn’t, can’t,
  you’ll. Typographic quotes and apostrophes (’ “ ”) and the ellipsis character (…).

## Words

- "such as" to introduce examples, with real names: "such as CLAUDE.md or AGENTS.md".
- "each", "every", "only" make claims exact.
- "you" for the reader. Never "we" in a guide.
- Ordinary verbs: runs, sends, reads, writes, starts, checks, adds, stores, returns.
- Frequency words on a specific claim: usually, often, some, most.
- A product is an example of a part ("Claude Code is an example of a harness"), never the
  name of the part.

Avoid: simply, just, really, actually, key, powerful, important, crucial, note that,
leverage, unlock, seamless, robust, landscape, journey, game-changer, delve.

## Defining terms

- **Genus and difference, in the first sentence:** "A harness is the program that runs the
  model in a loop." "A skill is a written procedure kept in a folder."
- **Then what it does, then why it matters.**
- **Only with words already defined,** on this page, an earlier page, or in the guide it
  builds on.
- **By contrast with the thing it's confused with,** in two flat sentences: "A model only
  writes text. An agent is a model that a harness runs in a loop with tools, which is why an
  agent can act."
- **One name per thing.** Use the name most practitioners use. If sources use two names, pick
  one and keep it. No synonyms for variety. Keep qualifiers every time ("main agent",
  "sub-agent", never bare "agent" once the difference matters).

## Certainty

- State facts flatly. No "it seems", "arguably", "we believe".
- Hedge with frequency, attached to the claim: "Usually seconds, sometimes a few minutes."
- When sources conflict, say which says what, then what to do.
- When something isn't known, say so: "The docs don’t say how to get access."
- Date the facts: "as of October 2026".
- No praise or blame of products, teams or vendors.

## Tone

- Regular English that doesn't call attention to itself: "Nobody cares about how clever the
  grammar is. They're only going to lower their opinion of the guide or give up if it is work
  or annoying to read."
- A light everyday image is fine once, when it makes the idea land, and is never stretched
  into a framework. A short dry perspective is welcome where it rewards the reader. Never
  sarcasm, snark or indirection.
