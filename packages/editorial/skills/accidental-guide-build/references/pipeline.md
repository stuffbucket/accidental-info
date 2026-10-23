# The pipeline

How a guide gets from `guide.md` to a PDF, a Word document and a listing on the site.

## Layout

The repository is a pnpm and Turborepo workspace. Every folder in `guides/` and `drafts/` is
a workspace package named `@accidentalguide/<slug>`.

```
<repository root>/
  guides/<slug>/          published guides
  drafts/<slug>/          guides being written, laid out the same way
  packages/pipeline/      guide.py builds one guide; workspace.py (pnpm sync) keeps the
                          package.json files and README lists in step; imprint.py; the
                          pinned requirements.txt
  packages/editorial/     these skills, the concept registry and the briefs
  site/                   the Astro and Starlight site, which lists every guide
  .venv/                  made by the pipeline package's build
```

Each guide folder holds everything it needs:

```
<slug>/
  guide.md            every word in the guide
  content.py          reads guide.md into named slots both builders use
  build_guide.py      the PDF: layout, colours, tiles, diagrams, margin check, hash check
  build_docx.py       the Word document; places images of the PDF's diagrams
  expected.sha256     the PDF's hash, one line: "<hash>  <slug>.pdf"
  README.md           what's here, how to rebuild, the Markdown this guide's builder reads
  fonts/              copied byte for byte, including heros-*.ttf and licenses/
  package.json        written by pnpm sync
  dist/               the build's output, not committed
```

Nothing is shared between guides except `packages/pipeline/` and `.venv/`, so a change to
one guide never changes another guide's bytes.

## What the pipeline does

`pnpm turbo run build --filter=@accidentalguide/<slug>` (or
`.venv/bin/python packages/pipeline/guide.py drafts/<slug>`) builds one guide. `pnpm build`
builds every guide and then the site. For one guide, `guide.py`:

1. runs `python build_guide.py dist/<slug>.pdf` from inside the folder, and fails unless it
   printed `no overflow`, or if the PDF differs from `expected.sha256`;
2. runs `python build_docx.py dist/<slug>.pdf dist/<slug>.docx` if the folder has one;
3. imports `content.py` and reads `TITLE`, `KICKER`, `SUBTITLE`, `EDITION`, `VERSION` and
   `BLURB` (the first paragraph of `{#why}`, which the site shows);
4. writes `dist/guide.json` with those, the page count from the PDF, and a status: "draft"
   for a folder in `drafts/`, "published" otherwise.

The site reads each guide's `guide.json`. CI runs `pnpm turbo run build test` on every pull
request. On every push to `main` the Pages workflow builds and deploys the site, and makes a
GitHub release for each guide version that doesn't have one yet.

`pnpm sync` runs `packages/pipeline/workspace.py`. Run it after you add, rename or move a
guide folder, or after you change `site/src/data/collections.json`: it writes the guide's
`package.json`, the site's list of guides, and the guides and drafts tables in `README.md`
from each `guide.md`'s front matter, and the cover's `collection`, `collection_mark` and
`number` into each `guide.md` from `collections.json`. `pnpm test` fails if they're out of
step, or if a guide isn't listed in `collections.json`.

## Making a new guide folder

Copy a guide that builds with `scripts/new_guide.py`. Pick the model by the pages you need:
`lights-off-software-factories` (why, fit, four entries, table pages, sources) or
`specs-and-reviews` (adds grey blocks, callouts, packed pages and a sequence diagram). The
script copies the folder, renames the slug in the builders and README, sets `COVER_LINES`
from the title, and sets the title, `version: 0.1.0` and the cover's collection and number in
`guide.md`. The copied builders
already put the end page's star link (`Leave a star: accidental.info/star`, linked to
https://accidental.info/star/) in the colophon and make the footer's address a `mailto:`
link, in the PDF and the Word document; leave them. Then change by hand:

| File | Change |
|---|---|
| `content.py` | The voice comment at the top (writers read it). Slots for any section added or dropped. Slots are taken by position, so a section's shape and its slots change together. |
| `build_guide.py` | `PART_FAMILY` (tile key to family, which sets the tile's colour and its column on the cover), `NAME2MONO` (every spelling of each part name that gets a tile, plurals included), `MONO_RE` (literals for this topic, such as `.json` or `.toml`), the `FIT_*` labels and `page_fit()`, the page order in `build()`. |
| `build_docx.py` | The page order, and `fit_box()` or `fit_layout()` if the overview diagram moved. If the PDF's diagram moves and these don't, the Word document places a wrongly cropped image and nothing fails. |
| `README.md` | The title, "copied from", and the Markdown section if the guide adds constructs. |

## The overflow rule

- Page: 4.5 × 7.5 in (324 × 540 pt). Margins 24 pt left and right, 28 pt top, 36 pt bottom.
- Each page function ends with `check(name, y)`. The build prints the problems or
  `no overflow`, and the pipeline fails without `no overflow`.
- The check is vertical only. It doesn't catch text past the right edge (a long mono string
  in a narrow column), colliding diagram labels or a title running under the corner tile.
  Look at the pages.
- If a page doesn't fit, cut words. Never shrink type or split a section across pages.

## The hash

The PDF build is deterministic: ReportLab's invariant mode fixes the dates and document id,
and the fonts are fixed files. `build_guide.py` prints `sha256 <hash>` and then
`matches expected.sha256` or `DIFFERS from expected.sha256 (<old>)`.

- New guide: build once and write the hash (`build_one.sh --update-hash`).
- Text changed on purpose: update `expected.sha256` in the same commit.
- Only a builder or the pipeline changed: the hash should not change. If it does, the change
  altered the PDF.
- Missing `heros-*.ttf` fonts get regenerated with a timestamp, and the PDF will never match.
  Keep the shipped files.

There is no hash for the `.docx`, but it is deterministic too.

## Gotchas

- **The PDF and the Word document can disagree on pages.** The site shows the PDF's page
  count. If the `.docx` has a different number of pages, its page order is wrong.
  `build_one.sh` warns.
- **Text lives in the builders too.** The cover title lines and the overview diagram's labels
  are in `build_guide.py`. Check them when the title or the parts change, and lint them by
  eye.
- **Part names must match `NAME2MONO` exactly** to get a tile, plurals included.
- **Two-letter keys can clash between guides.** Check with the plan skill's
  `list_concepts.py`.
- **Page numbers typed in the text** don't update. The cover and entry index compute theirs.
- **`__pycache__/` and `dist/`** appear in the guide folder after a build. Both are ignored
  by git.
- **A new folder isn't in the workspace** until you run `pnpm sync`.
