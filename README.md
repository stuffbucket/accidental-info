# Accidental Guides

Short guides to how the AI systems we work with are put together. Read them at
**https://stuffbucket.github.io/accidentalguide/**.

Each guide is a folder under `guides/` with its text in Markdown, its layouts and its
fonts. `python build.py` (after installing `requirements.txt`) or `pnpm build` builds every
guide into `dist/`:

- `dist/<guide>.pdf` and `dist/<guide>.docx`, one of each per guide;
- `dist/guides.json`, each guide's title, subtitle, edition, version, page count, blurb and files.

`python build_site.py` then writes the site to `_site/`: an `index.html` that lists the
guides from `guides.json`, with the PDFs, Word documents, a cover image of each guide and
the fonts. `pnpm site` does both steps. The Pages workflow in `.github/workflows/pages.yml`
runs the same build on every push to `main` and deploys `_site/` to GitHub Pages. It fails
if a guide's PDF differs from its `expected.sha256`.

`pnpm build` makes its own virtual environment in `.venv/` and installs the packages
pinned with hashes in `requirements.txt`. To do it by hand:

```sh
python3 -m venv .venv
.venv/bin/pip install --require-hashes -r requirements.txt
.venv/bin/python build.py
.venv/bin/python build_site.py
```

The build fails if a page has content past its bottom margin.

## Guides

| Folder | Guide |
| --- | --- |
| `guides/accidental-intelligence` | An Accidental Guide to… Accidental Intelligence (the catalog of the others) |
| `guides/agents-harnesses-skills-tools` | An Accidental Guide to… Agents, Harnesses, Skills, and Tools |
| `guides/lights-off-software-factories` | An Accidental Guide to… Lights-Off Software Factories |
| `guides/software-factories` | An Accidental Guide to… Software Factories |
| `guides/specs-and-reviews` | An Accidental Guide to… Specs and Reviews |

## Editing a guide

Change the text in the guide's `guide.md`, then build. Each guide's README describes
its Markdown.

Each `guide.md` has a `version:` in its front matter, in semver (such as `1.0.0`), which
the cover and `guides.json` show; bump it when the guide's text changes. The build fails
if a guide has no valid version.

## Text, layout and visuals

- **The Markdown holds the words**, and the data a diagram is drawn from, such as the
  steps of a sequence diagram. It has no layout in it.
- **Each output has its own layout:** `build_guide.py` for the PDF and `build_docx.py`
  for the Word document.
- **Visual rules are defined once,** in `build_guide.py`, and `build_docx.py` imports
  them: the part colours, which words are set in mono, and which part of a row is bold.
- **Diagrams are drawn once,** by the PDF build. The Word document places images of them
  rendered from the built PDF, so the two never disagree.
- **The PDF is the oracle.** Its build is deterministic and its hash is in
  `expected.sha256`, so a change to the text pipeline or a builder that alters the PDF
  shows up as a different hash.

## Adding a guide

Add a folder under `guides/` with:

- the guide's text, and a `content.py` that defines `TITLE`, `KICKER`, `SUBTITLE`,
  `EDITION`, `VERSION` and `BLURB` (the paragraph the site shows) along with the rest of it;
- `build_guide.py`, which takes the output path as its argument and prints
  `wrote <path>: <n> pages`, then `no overflow` when every page fits;
- optionally `build_docx.py`, which takes the built PDF and the output path.

## Changing package versions

Edit `requirements.in`, then regenerate `requirements.txt` with
`pip-compile --generate-hashes --strip-extras requirements.in`. A guide's PDF is
byte-identical to its `expected.sha256` only with the versions it was built with.

## License

The code and the guides' text are under the MIT License in `LICENSE`. The fonts in each
guide's `fonts/` folder keep their own licenses, in `fonts/licenses/`: TeX Gyre Heros under
the GUST Font License and Liberation Mono under the GNU GPL v2 with its font exception.
