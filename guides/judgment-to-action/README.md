# Source for From Judgment to Action

This folder contains everything needed to build An Accidental Guide to… From Judgment to Action as a PDF and Word document. The text is in `guide.md`.

## Rebuild

From the repository root:

```sh
pnpm turbo run build --filter=@accidentalguide/judgment-to-action
```

The build writes `dist/judgment-to-action.pdf`, `dist/judgment-to-action.docx` and `dist/guide.json`. The site reads `guide.json` and lists the guide as a draft.

To run the builders directly from this folder, with the pipeline dependencies installed:

```sh
python3 build_guide.py
python3 build_docx.py judgment-to-action.pdf
```

`build_guide.py` reports the page count, overflow status and PDF hash. `expected.sha256` records the accepted PDF after the first reviewed build.

## Files

| File | What it is for |
|---|---|
| `guide.md` | Titles, entries, tables, sources and public metadata. |
| `content.py` | Parses `guide.md` for both builders. |
| `build_guide.py` | PDF layout, concept tiles and margin checks. |
| `build_docx.py` | Word layout using the PDF builder's visual rules. |
| `fonts/` | Embedded typefaces and their licenses. |
| `expected.sha256` | Accepted PDF hash, created after visual review. |

The Markdown has `{#why}` and `{#fit}` opening pages, four `{#entry}` sections, a `{#habits}` checklist and `{#sources}`. Every page before the checklist has a figure, and all of them follow the same support message. The entry tiles are `Po`, `Td`, `Rp` and `Lc`; their ownership and color families come from `packages/editorial/registry.json`.

## Figures

Each figure is a fenced `diagram` block in `guide.md`, one item per line, with `|` between fields. `build_guide.py` draws it in vector form with the guide's fonts and family colours, and `build_docx.py` places the same drawing in the Word document. The figure code is the same in `guides/decision-models` and `guides/judgment-to-action`; keep the two copies identical.

| First line holds | Figure |
|---|---|
| `message`, `ask`, `answer` | A message, then questions with their answers as score bars |
| `group`, `step` | Groups of steps, each a part beside its value in the example |
| `input`, `output` | What goes into a decision model and what comes out |
| `message`, `missing` | What was sent and what was left out |
| `side` | Questions in columns, each with its scores |
| `shape` | Answer shapes as chips; `*` marks a picked answer and `>` an ordered level |
| `case` | Two sets of scores side by side |
| `message`, `scores`, `facts`, `rules`, `checks`, `check`, `results`, `else` | One message followed down two columns, one per action: the model’s answers, account facts, the rule, the checks and the action |
| `head`, `label`, `band`, `row`, `cut` | Messages sorted by score into one band per action, with thresholds between the bands; a row with a fourth field is a boxed mistake |
| `yes`, `no`, `try` | For each cut-off, the saved messages it would refund automatically |
| `ruleset` | Two versions of the rules side by side |
| `record`, `field` | One saved record as a card |

## License

The guide text is under CC BY 4.0 (`LICENSE-TEXT` at the repository root), and its code is under the MIT License (`LICENSE`). Font licenses are in `fonts/licenses/`.
