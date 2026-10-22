# <Title>: format leakage

A cold read of `<guide folder>/guide.md`, version <x.y.z>, and the built PDF, by a reader
who has never seen an Accidental Guide. Every page was rendered and read. The PDF text was
compared with `guide.md` to find text that only the builders print.

Line numbers are `guide.md` lines. "PDF p. N" marks text only the build prints. Each finding
counts once, even when it covers several lines. "Low" marks a finding a reader would likely
get past.

First pass: `lint_guide.py` (<n> errors, <n> warnings). <Classifier pass, if run: what it
found and what it missed.>

Kinds: SN self-narration, UV unnamed voices, PV presenter voice, BF borrowed framing, TR
trivia, JG jargon, TT terms-table commentary, MP mannered prose.

## Status of the last scan

<If there was one: which findings are gone and which remain, by line.>

## Findings

| Line | Text | Kind | Rewrite |
|---|---|---|---|
| <n> | "<exact text>" | SN | "<replacement>" or "Delete." |
| PDF p. <n> | "<text the builder prints>" | JG | <change in build_guide.py> |

## Counts

| Kind | Count |
|---|---|
| SN | <n> |
| UV | <n> |
| PV | <n> |
| BF | <n> |
| TR | <n> |
| JG | <n> |
| TT | <n> |
| MP | <n> |
| Total | <n> |
