# Brief for a new Accidental Guide

Work from the repository root. The process skills are in `packages/editorial/skills/` (read
each SKILL.md you use, and use their scripts). The new guide goes in `drafts/<slug>/`.

## What the author wants

In his words: "remember no mannered prose and the writing is clear, easy to follow, doesn't put a
lot of burden on the reader and makes no assumptions that they have a lot of depth in a topic nor
are they an expert. These are 5 minute reads, tops."

- **Five minutes or less, front to back:** about 1,100 printed words including tables (check
  with the build skill's `reading_time.py <slug>`). Cut detail, not clarity.
- **Key concepts:** five or fewer, each with a page and a filled tile. Don't draw blank-box
  "not one of the parts" concepts, and don't add legends that say so. No jargon labels in diagrams.
- **Visual first:** a diagram or a table wherever it says more than a paragraph.
- **Writing rules:** the Voice section of `CONTRIBUTING.md` and the write skill's
  `references/author-feedback.md`, `references/voice.md` and `references/banned-patterns.md`
  are binding. Write in regular English that builds one idea at a time, as if to a smart
  colleague who is new to this. Avoid all of:
  - paragraph-by-list
  - stiff "A person can"
  - self-narration ("this guide"), hooks, trivia, sarcasm or snark
  - borrowed framing (no birds, field guides or travel)
  - mannered prose
  - quotes or name-checks of people
  - non-public company material
- **Cross-references:** in body prose, use the colon form: "An Accidental Guide to: Agents,
  Harnesses, Skills, and Tools". The "…" form appears only on the cover.
- **The base guide:** `guides/agents-harnesses-skills-tools/guide.md` is well reviewed and
  fixed. Never contradict it, don't repeat it, and point to it for the basics (agent,
  harness, skill, tool, session, context window).
- **The registry:** `packages/editorial/registry.md` gives each concept one tile code, one
  colour family and one owning guide. A new key concept gets a code no other concept uses.
- **Facts:** come only from public, official documentation and the project's own published
  material, fetched now. Save notes with URLs and short verbatim excerpts in a `sources.md`
  in your notes folder (outside `drafts/` and `guides/`). List the sources in a short
  appendix (title, publisher, URL, date checked). Where products differ or change often, say
  "as of <Month Year>".
- **Front matter:** `version: 0.1.0`, `kicker: An Accidental Guide to…`, a short, balanced
  title, and the public imprint: `edition: oops@accidental.info · CC BY 4.0 · <Month Year>`
  and `cover_footer: friend@accidental.info · <Month Year>`.

## How to build it

1. **Set up the folder:**
   `python3 packages/editorial/skills/accidental-guide-build/scripts/new_guide.py lights-off-software-factories <slug> --title "<Title>"`,
   then `pnpm sync`. Use `specs-and-reviews` as the source instead for grey blocks,
   callouts, packed pages or a sequence diagram. Read the build skill's
   `references/pipeline.md` first. Don't change other guides' folders.
2. **Plan:** write the page plan to `plan.md` in your notes folder, from the plan skill's
   template.
3. **Write:** put the instructions in a file (the write skill's `templates/writer-round1.md`)
   and write the draft from it, or apply it with the optional writer,
   `packages/editorial/skills/accidental-guide-write/scripts/run_writer.sh <slug> <notes>/WRITE-1.md --add-dir .`.
   - Always include this line: "No mannered prose: the writing must not call attention to
     itself. Make no assumption that the reader is an expert."
   - Later rounds are targeted edit lists with line numbers, applied in place. Never
     regenerate the guide.
   - Do the folder setup and any builder code yourself.
   - If an AI model drafts or edits the text, follow the disclosure rule in CONTRIBUTING.md.
4. **Build:** `packages/editorial/skills/accidental-guide-build/scripts/build_one.sh <slug>`
   must print "no overflow". It also builds the Word document, renders every page and counts
   the words. `pnpm turbo run build --filter=@accidentalguide/<slug>` runs the same checks.
5. **Check:** look at every page image. Read each page as a newcomer and fix what fails. Run
   the write skill's `lint_guide.py <slug>` and fix every error.
6. **Hash:** `build_one.sh <slug> --update-hash` writes `expected.sha256` and confirms it
   matches.
7. **Commit** after each round, only your own paths:
   `git add drafts/<slug> && git commit -m "<plain message>"`.
   - Retry if git reports `index.lock`. Never use `git stash`.
   - Don't edit the guide tables in `README.md` by hand; `pnpm sync` writes them.
8. **Rounds:** up to three.

Reply in under 120 words: title, slug, key concepts, page count, printed word count, and page 2's
first paragraph verbatim.
