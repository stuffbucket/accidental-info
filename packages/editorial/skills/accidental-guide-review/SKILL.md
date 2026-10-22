---
name: accidental-guide-review
description: Review a draft Accidental Guide before the next round of edits or before publishing it. Runs four cold reviews (a reader panel of exec, lead and engineer, fidelity against the sources, a format-leakage scan for self-narration and borrowed framing, and series consistency) and turns their findings into a line-numbered edit list. Use when a draft builds and needs checking, when the author asks whether a guide is ready, or before moving a guide from drafts/ to guides/.
metadata:
  series: Accidental Guides
  version: "1.0"
---

# Review an Accidental Guide

A guide is reviewed by readers who start cold. Each review runs as its own subagent (or
person) with only the files that review lists, so it reads what the guide says, not what it
meant to say. Findings come back with line numbers and rewrites, and become the next edit
list for the `accidental-guide-write` skill.

[references/review-method.md](references/review-method.md) describes each review: who the
reviewer is, what it gets, what it looks for and how it reports.
[references/checklist.md](references/checklist.md) is the page-by-page yes-or-no list.

## Steps

1. **Build first.** The guide must build with "no overflow", and the page images must be
   fresh (`accidental-guide-build`, `build_one.sh`). Note the version and commit.
2. **Lint.** Run `python3 packages/editorial/skills/accidental-guide-write/scripts/lint_guide.py
   <guide>`, which reads your deny list (see `accidental-guide-write`). Fix the errors yourself or put them in the edit list. The reviewers
   then spend their time on what the lint can't see.
3. **Run the four reviews**, in parallel, each with a fresh context and only its inputs:

   | Review | Gets | Template |
   |---|---|---|
   | Reader panel | PDF page images and text, `guide.md` | [templates/readers.md](templates/readers.md) |
   | Fidelity | `guide.md`, `sources.md` | [templates/fidelity.md](templates/fidelity.md) |
   | Format leakage | `guide.md`, page images; nothing about the series | [templates/format-leakage.md](templates/format-leakage.md) |
   | Series consistency | this guide, the guides it names, the base guide, `list_concepts.py` output | [templates/series-consistency.md](templates/series-consistency.md) |

   Use the reviewer prompt at the end of the method reference. Save each report as
   `<notes>/review-<kind>.md` (add `-2` and so on for later passes).
4. **Sort the findings.** Drop any that contradict the author's rules or the base guide.
   Where reviews disagree, the author's feedback decides, then the sources.
5. **Write one edit list** with the write skill's `templates/edit-list.md`: line numbers from
   the current file, grouped by section, replacement text word for word where you have it.
   Run the writer, then lint, build and commit.
6. **Re-check.** Re-run only the reviews that found serious problems, against the new
   build. Before publishing, an optional final cold read reports blockers only.

## Ready to publish when

- The fidelity review has no Wrong, Unsourced or Non-public findings left.
- The format-leakage scan has nothing left above "low".
- The reader panel's top fixes are done, and each reader would finish the guide.
- No concept is a key in two guides, and cross-references use the colon form.
- The lint passes with the deny list, and the guide reads in five minutes.

Then publish with `accidental-guide-build`.
