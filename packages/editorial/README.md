# Editorial

How the guides are planned, written, built and reviewed. None of this is needed to suggest a
guide or fix a mistake; [CONTRIBUTING.md](../../CONTRIBUTING.md) covers that.

| Path | What it holds |
| --- | --- |
| `skills/accidental-guide-plan/` | Scoping a guide: its question, five or fewer key concepts, sources and page plan |
| `skills/accidental-guide-write/` | Writing and revising `guide.md`: the voice, the banned patterns, edit lists and the lint |
| `skills/accidental-guide-build/` | Making a draft folder, building and checking it, versions, and moving it to `guides/` |
| `skills/accidental-guide-review/` | Four cold reviews and the checklist before publishing |
| `registry.md`, `registry.json` | One tile code, colour family and owning guide for each key concept |
| `briefs/new-guide.md`, `briefs/final-pass.md` | Briefs for writing a new guide and for a last pass on one |

Each skill is a folder with a `SKILL.md`, and `.claude/skills/` links to them, so Claude
Code opens them in this repository. Other agents can read the same files. Run the scripts
from the repository root. They find guides in `drafts/` and `guides/` by slug:

```sh
python3 packages/editorial/skills/accidental-guide-write/scripts/lint_guide.py skills
python3 packages/editorial/skills/accidental-guide-plan/scripts/list_concepts.py
packages/editorial/skills/accidental-guide-build/scripts/build_one.sh skills
```

## The deny list

`lint_guide.py` checks a guide against a list of non-public names that must never be
printed. The list is kept outside every repository and is never committed. The lint reads
`~/.config/accidental-guides/denylist.txt`, or the paths in `ACCIDENTAL_GUIDE_DENYLIST`
(separated by colons) when that is set. `skills/accidental-guide-write/templates/denylist.example.txt`
shows the format.

## The writer

`skills/accidental-guide-write/scripts/run_writer.sh` has an outside model apply a brief or
an edit list to a guide. It's optional: you can write and edit a guide yourself. If an AI
model drafts or edits text you contribute, follow the disclosure rule in CONTRIBUTING.md.

`pnpm test` checks that the scripts compile.
