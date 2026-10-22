---
name: accidental-guide-plan
description: Scope, research and plan a new Accidental Guide, or re-scope an existing one. Use when someone asks for a new guide, when a guide's key concepts or page list need to change, or before any writing starts. Produces the guide's question, its five or fewer key concepts, a sources file of public facts, a page plan and a starting guide folder.
metadata:
  series: Accidental Guides
  version: "1.0"
---

# Plan an Accidental Guide

An Accidental Guide answers one plain question for someone who is new to the topic, in five
minutes or less. Planning decides the question, the few concepts that answer it, the facts
behind them and the pages. Writing comes after, in the `accidental-guide-write` skill.

Read [references/series-rules.md](references/series-rules.md) before you start. It has the
author's rules for scope, concepts and cross-references.

## Steps

1. **Pick the question.** Write it the way a reader would ask it: "What is a software
   factory?", "What is MCP for?". One question per guide. Name the reader: what they already
   know, which guide they have probably read, and what confuses them.

2. **Check the series.** Run `python3 scripts/list_concepts.py` to see every guide's key
   concepts, in `guides/` and `drafts/`. Each concept is owned by exactly one guide;
   `packages/editorial/registry.md` lists the owner, tile code and colour family of each.
   If a concept you need is another guide's key, use it as a plain word and point to that
   guide. Read the base guide, `guides/agents-harnesses-skills-tools/guide.md`. Never
   contradict it, don't repeat it, and point to it for the basics.

3. **Pick the key concepts.** Five or fewer, each a real thing the reader will meet, each
   with a page and a tile. Build up from what the reader knows: turn, then session, then the
   bigger idea. If the overview diagram needs boxes for things that aren't keys, the guide is
   at the wrong level of detail. If a side topic keeps coming up, it's another guide.

4. **Research.** Follow [references/research.md](references/research.md). Save the notes to
   `sources.md` in the guide's notes folder, using
   [templates/sources.md](templates/sources.md). Public, official sources only, fetched now,
   with URLs and short verbatim excerpts.

5. **Write the plan.** Copy [templates/plan.md](templates/plan.md) into the notes folder and
   fill it in: reader, questions in order, key concepts with tile keys, page list with a
   word budget, visuals, cross-references and builder changes.
   [references/page-kinds.md](references/page-kinds.md) lists the pages a guide can have and
   how many words each one takes.

6. **Set up the folder.** Copy a guide that builds with `new_guide.py` from the
   `accidental-guide-build` skill:
   `python3 packages/editorial/skills/accidental-guide-build/scripts/new_guide.py <model-guide> <slug> --title "<Title>" --guide-md <notes>/guide.md`,
   from the repository root. It makes `drafts/<slug>/` with the public imprint; then run
   `pnpm sync` to add it to the workspace.
   Start `guide.md` from [templates/guide.md](templates/guide.md), with the plan's sections
   and PLACEHOLDER text, so the writer fills a shape the builders already read. The template
   matches the `lights-off-software-factories` builder and uses its tile keys (Sn, Dt, Sa,
   Cl) so it builds as it is. Change the keys, names and number of entries in `guide.md`
   and the builder together: tiles (`PART_TOKEN`, `NAME2MONO`), cover lines, diagram labels
   and page order. Do the builder work yourself, not the writer. Then build it once.

7. **Commit** the guide folder (and the notes, if you keep them in the repository). Then
   hand off to `accidental-guide-write`.

## Where things go

| What | Where |
|---|---|
| Notes: plan, sources, writer briefs, edit lists, reviews | A notes folder outside `guides/` and `drafts/`, such as `notes/<slug>/`. Notes needn't be committed |
| The guide while it's written | `drafts/<slug>/` |
| The guide once it's published | `guides/<slug>/` |

The slug is lowercase words joined by hyphens. It becomes the PDF and Word file names.

## Done when

- The question fits on one line, and the title is short and balanced (six words or fewer).
- There are five or fewer key concepts, none of them another guide's key.
- Every fact the plan needs is in `sources.md` with a public URL.
- The word budget adds up to about 1,100 printed words.
- The draft folder builds with placeholder text and prints "no overflow".
