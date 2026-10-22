---
name: accidental-guide-build
description: Set up, build, check and release an Accidental Guide with its PDF and Word pipeline. Use when making a new guide folder, after any change to a guide's guide.md or builders, to render and check the pages, count printed words for the five-minute target, update expected.sha256, bump the semver version, commit a round, or move a guide from drafts/ to guides/ to publish it.
metadata:
  series: Accidental Guides
  version: "1.0"
compatibility: Needs bash, python3 with the repository's .venv (made by the pipeline package's build from packages/pipeline/requirements.txt), and poppler (pdftoppm, pdftotext, pdfinfo).
---

# Build and release an Accidental Guide

Each guide is a folder with its text (`guide.md`), a parser (`content.py`), two builders
(`build_guide.py` for the PDF, `build_docx.py` for Word), its fonts and the PDF's expected
hash. The PDF build is deterministic, so the hash shows any change.

- [references/pipeline.md](references/pipeline.md): the folders, what the pipeline does, what
  to change in a new guide, the overflow rule, the hash and the gotchas.
- [references/guide-md-format.md](references/guide-md-format.md): the Markdown the parsers
  read.
- [references/design.md](references/design.md): what the pages should look like, and what to
  look for on them.

Run every command from the repository root. `GUIDE` is the guide folder (`drafts/<slug>` or
`guides/<slug>`); the scripts also take the bare slug and look in `drafts/` and then
`guides/`. `SCRIPTS` is `packages/editorial/skills/accidental-guide-build/scripts`.

## Set up a new guide

1. Install the tools once: `mise install`, `pnpm install`, then
   `pnpm turbo run build --filter=@accidentalguide/pipeline` to make `.venv/`.
2. Copy a guide that builds into `drafts/`:
   `python3 SCRIPTS/new_guide.py lights-off-software-factories <slug> --title "<Title>" [--guide-md <placeholder guide.md>]`.
   Use `specs-and-reviews` as the source instead if the plan needs grey blocks, callouts,
   packed pages or a sequence diagram. The script sets the public imprint in the front
   matter (`edition: oops@accidental.info · CC BY 4.0 · <Month Year>` and
   `cover_footer: hi@accidental.info · <Month Year>`) and the author "Accidental Guides" in
   the builders.
3. Run `pnpm sync` to add the folder to the workspace. It writes the guide's
   `package.json` and the lists of guides in `README.md` and `site/package.json`.
4. Make the builder changes the script lists (tiles, names, mono pattern, diagram labels,
   page order). See "Making a new guide folder" in the pipeline reference.
5. Build with `--update-hash` to write the first `expected.sha256`.

## Build and check, every round

1. `SCRIPTS/build_one.sh GUIDE [--out DIR] [--pages-dir DIR]`. It builds the PDF into
   `GUIDE/dist/`, fails on overflow, builds the `.docx`, warns if their page counts differ,
   renders every page to PNG, and prints the word count per page and the reading time.
   `pnpm turbo run build --filter=@accidentalguide/<slug>` runs the same build checks and
   also writes `dist/guide.json` for the site.
2. Look at every page image as a newcomer. The overflow check is vertical only (see the design
   reference for what it misses).
3. Reading time: `python3 SCRIPTS/reading_time.py GUIDE`. Each guide is a five-minute read
   or less: about 1,100 printed words, five minutes at 220 words a minute. It exits 1 above
   1,250. Cut whole rows and sections first, then repeated explanations.
4. Lint the text with `accidental-guide-write`'s `scripts/lint_guide.py GUIDE`. It reads your
   deny list (see that skill).
5. If the text changed on purpose, bump the version and update the hash:
   `python3 SCRIPTS/bump_version.py GUIDE minor` (patch for small fixes, minor for a round,
   major when it's published as reviewed), then `SCRIPTS/build_one.sh GUIDE --update-hash`.
   The summary must say `matches expected.sha256`.
6. Commit after each round, only your own paths:
   `git add GUIDE && git commit -m "<Title>: <what changed>, version <x.y.z>"`.
   If git reports `index.lock`, wait and retry. Don't use `git stash` when other people or
   agents share the checkout. `__pycache__/` and `dist/` are ignored; don't commit page
   images.

If only a builder changed, the hash must not change. If it does, the change altered the PDF.

## Publish

A guide is written in `drafts/<slug>/` and published by moving it to `guides/<slug>/`. The
site shows a guide in `drafts/` as a draft and one in `guides/` as published.

1. The guide has been through the reviews in `accidental-guide-review`, and their findings are
   fixed or answered.
2. The lint passes with your deny list: no internal names, nothing marked confidential, no
   quotes or names of people in the body.
3. Every source on the Sources page is public and was checked this month.
4. `git mv drafts/<slug> guides/<slug>`, then `pnpm sync`, which moves the guide's row from
   the drafts list to the guides list in `README.md`. Bump to `1.0.0` (or the next major)
   and update the hash.
5. Run `pnpm turbo run build test` from the root and confirm every guide still builds and
   matches its `expected.sha256`.
6. Commit: "Publish <Title>, version 1.0.0". On the next push to `main`, the Pages workflow
   makes the release `<slug>-v1.0.0`.

## Scripts

| Script | What it does |
|---|---|
| `scripts/new_guide.py SOURCE NEW --title T [--guide-md FILE] [--month "Month Year"]` | Copies a guide folder to `drafts/<slug>`, sets the title, version and public imprint, and lists what to change by hand |
| `scripts/build_one.sh GUIDE [--out DIR] [--update-hash] [--pages-dir DIR] [--dpi N]` | PDF, overflow check, `.docx`, page-count check, page images, word count, hash status. Set `PYTHON` to use another interpreter |
| `scripts/reading_time.py GUIDE [--wpm N] [--target N] [--max N] [--quiet]` | Printed words per page and in total, and minutes to read, from the built PDF |
| `scripts/bump_version.py GUIDE patch\|minor\|major\|--show` | Bumps the semver `version:` in the front matter |
