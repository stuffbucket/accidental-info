# The guide template

A Word document to write your own Accidental Guide in, built with the same layout as the
guides. Its text says what goes where: the title and subtitle, the opening page, how the
parts fit, up to six parts with their field marks and "Confused with" note, and the sources.

`pnpm build` writes:

| File | What it is |
|---|---|
| `dist/accidental-guide-template.docx` | The template. The site offers it for download. |
| `dist/accidental-guide-template.pdf` | The same pages as a PDF, for checking the layout. |

The template isn't a guide. It isn't listed on the site or in the README, and it has no
release.

## How it's built

The folder was copied from `guides/lights-off-software-factories/` and is built the same
way, by `packages/pipeline/guide.py`. Then `rename.py` gives the files their download names
and removes `dist/guide.json`, which only the site's list of guides reads.

| File | What it's for |
|---|---|
| `guide.md` | The template's text. Edit this to change it. |
| `content.py` | Reads `guide.md` into the names both builders use. |
| `build_guide.py` | The PDF layout. The parts are named "Part one" to "Part six", with the tiles P1 to P6. "How do the parts fit together?" is text only. |
| `build_docx.py` | The Word layout, from the PDF's visual rules. |
| `rename.py` | Renames the built files. |
| `fonts/` | The guides' fonts and their licenses. |
| `expected.sha256` | SHA-256 of the built PDF. Update it when the text changes. |

The Markdown follows the format in `guides/lights-off-software-factories/README.md`: front
matter, then `{#why}`, `{#fit}`, up to six `{#entry num=01 mono=P1}` sections and
`{#sources}`.

## License

The template's text is under CC BY 4.0 (`LICENSE-TEXT` at the repository root), and its code
under the MIT License (`LICENSE`). TeX Gyre Heros is under the GUST Font License and
Liberation Mono under the GNU GPL v2 with its font exception, in `fonts/licenses/`.
