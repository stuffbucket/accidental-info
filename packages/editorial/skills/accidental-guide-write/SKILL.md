---
name: accidental-guide-write
description: Write or revise the text of an Accidental Guide in the author's voice, with a written brief for the first draft and targeted edit lists for each later round, optionally applied by an outside writer model. Use when a planned guide needs its first draft, when a review or the author asks for changes to a guide's guide.md, or when checking a draft for mannered prose, self-narration, borrowed framing, quotes or internal names.
metadata:
  series: Accidental Guides
  version: "1.0"
compatibility: Needs bash and python3. The optional writer script needs the GitHub Copilot CLI (copilot).
---

# Write an Accidental Guide

The first draft follows a written brief. Later rounds are edit lists with line numbers,
applied in place. Never regenerate a whole guide: a fresh draft loses every fix the earlier
rounds made. Commit after each round.

You can write the words yourself, or have an outside writer model apply the brief or the
edit list with `scripts/run_writer.sh`. The writer is optional and you don't need it to
contribute. If an AI model drafts or edits text you contribute, follow the disclosure rule
in CONTRIBUTING.md.

Before you write a brief, read these. Give them to the writer too.

- [references/author-feedback.md](references/author-feedback.md): the author's feedback in
  his words. Binding.
- [references/voice.md](references/voice.md): his voice, with samples and measurements.
- [references/banned-patterns.md](references/banned-patterns.md): what never goes in, and the
  text rules the builders need.

The plan and sources come from the `accidental-guide-plan` skill. Building and checking the
PDF is the `accidental-guide-build` skill.

## Round 1: the first draft

1. Commit the guide folder with its placeholder `guide.md`, so the draft is one clean diff.
2. Copy [templates/writer-round1.md](templates/writer-round1.md) into the notes folder as
   `WRITE-1.md` and fill it in: the files to read, the reader, the question, the answer in
   order, the word budget. Paths in it are relative to the repository root, so `<skills>`
   is `packages/editorial/skills`.
3. Write the draft from the brief, or run the optional writer:
   `packages/editorial/skills/accidental-guide-write/scripts/run_writer.sh <slug> <notes>/WRITE-1.md --add-dir .`
   from the repository root. The default model is `gpt-5.6-sol-fast`; pass `--model` or set `WRITER_MODEL` for
   another. The script puts "No mannered prose: the writing must not call attention to
   itself" in every prompt and prints the diff of `guide.md`. If it lists other changed
   files, restore them.
4. Lint: `python3 packages/editorial/skills/accidental-guide-write/scripts/lint_guide.py <slug>`.
   Fix every error. Read every warning and decide.
5. Build and read the pages (see `accidental-guide-build`). Check "no overflow" and the word
   count.
6. Bump the version, update `expected.sha256`, commit: "<Title>: first draft, version
   0.1.0". Name the model in the commit if one wrote the draft.

## Later rounds: edit lists

1. Collect what to fix: the lint, the build, the page images, the reviews
   (`accidental-guide-review`) and anything the author said. Quote the author's words in the
   list when they apply.
2. Write the edits with [templates/edit-list.md](templates/edit-list.md) as `EDITS-<n>.md`.
   For each edit give the line number from the file as it is now and, wherever you can, the
   full replacement text. Where you can't, say what to change, the word count and a short
   example of the register. Group the edits by section.
3. Apply the edit list yourself, or run the writer with it, as in round 1.
4. Check the diff: every changed line is one the list named. Revert anything else.
5. Lint, build, read the pages, bump the version, update the hash and commit after each round,
   so rounds don't drift.

Small fixes (a word, a typo, one row) you can make in place without an edit list. When a
writer model drafted the guide, give it anything that needs new sentences, so the voice
stays the same across the guide.

Three rounds is usually enough. If a fourth round is still changing concepts, go back to the
plan.

## What the brief always says

- "No mannered prose: the writing must not call attention to itself. Make no assumption that
  the reader is an expert."
- Edit in place. Keep the shape (headings, ids, paragraph counts, table labels). Change only
  what is named.
- Five minutes or less front to back, about 1,100 printed words. Five or fewer key
  concepts. Shorten by dropping detail, not by
  packing the same detail into denser sentences.
- No quotes or names of people. No non-public material. Facts only from `sources.md`.
- The form of the guide is structure only. Its vocabulary stays out of the text.

## Scripts

| Script | What it does |
|---|---|
| `scripts/run_writer.sh GUIDE INSTRUCTIONS.md [--model M] [--add-dir D] [--timeout S] [--dry-run]` | Optional. Runs the writer model from the guide folder with the instructions file, then shows the diff of `guide.md` and any other file it touched |
| `scripts/lint_guide.py GUIDE [--deny FILE] [--no-deny] [--strict] [--skip CODES] [--list]` | Reports banned patterns with line numbers: Markdown the builders print literally, em dashes and semicolons, self-narration, unnamed voices, mannered markers, embedded questions, pronoun-led rows, borrowed framing, cross-reference form, quotes and name-checks, and names from your deny list. Exits 1 on errors |

The lint can't judge flow, tone or whether a paragraph builds on the last one. Read the
pages as a newcomer would.

## The deny list

The deny list holds non-public names that must never be printed, one per line. It lives
outside every repository and is never committed. The lint reads
`~/.config/accidental-guides/denylist.txt` by default. To keep it elsewhere, set
`ACCIDENTAL_GUIDE_DENYLIST` to its path (several paths separated by colons), or pass
`--deny FILE`. When no deny list is found, the lint says internal names weren't checked.
[templates/denylist.example.txt](templates/denylist.example.txt) shows the format, with
made-up entries.
