# Plan: An Accidental Guide to… From Judgment to Action

Slug `judgment-to-action`. Builder copied from `packages/template/`. Target about 1,100 printed words and 9 pages. Facts only from `sources.md`.

## The reader

The reader understands that a model can label or score a case, but is tempted to treat the top answer or a high score as an action. They need a small operating design that keeps business decisions inspectable and handles uncertain cases without pretending uncertainty is gone. Reading Decision Models first helps but is not required.

## The question

How does a judgment become an action?

## The answer, in order

1. A model judgment and an application action are separate outputs owned by different parts of the system.
2. Policy combines model judgments with facts from ordinary systems.
3. Thresholds create branches only after being tested on representative labeled cases.
4. A review path gives selected cases an owned operating outcome.
5. Saved labeled cases make model, question, threshold and policy changes testable.

## Key concepts

| No. | Part | Key | Family | Meaning |
|---|---|---|---|---|
| 01 | Policy | Po | Dm | Visible rules that map facts and judgments to outcomes. |
| 02 | Threshold | Td | Dm | A chosen score boundary between two paths. |
| 03 | Review path | Rp | Dm | The outcome for a case software should not settle alone. |
| 04 | Labeled case | Lc | Wr | A saved example with an expected judgment. |

Plain words without tiles: model, state, judgment question, probability, account fact, error cost and monitoring. Decision Models owns the model-side terms.

Checked against `packages/editorial/registry.json`: all four concepts are owned here and all codes are unique.

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover and concept map | 45 |
| 2 | `{#why}` | Separates a refund judgment from the operating decision | 170 |
| 3 | `{#fit}` | Assigns model, ordinary-system, code and person responsibilities | 150 |
| 4–7 | `{#entry}` × 4 | One page per key concept | 4 × 130 |
| 8 | `{#habits}` | Pre-ship evidence and operating checklist | 160 |
| 9 | `{#sources}` | Four checked public sources | 90 |
| | | Total | about 1,135 |

## Entries

Field marks vary where needed but always give a short answer and one detail sentence.

| Entry | Identify by | Confused with |
|---|---|---|
| Policy | Rules mapping facts and judgments to outcomes | Judgment question |
| Threshold | A score boundary chosen for one path | Probability |
| Review path | A queue or pause owned by people | Error log |
| Labeled case | Reproducible request plus expected answer | Demonstration |

## Cross-references

- Builds on An Accidental Guide to: Decision Models for state, questions, answers and probability.
- Leaves provider catalogs, model benchmarks and runtime parity details to companion references and evaluations.

## Builder changes

- Map `Po`, `Td`, `Rp` and `Lc` to their registry families.
- Map singular and plural concept names in `NAME2MONO`.
- Use `From` / `Judgment to` / `Action` cover lines.
- Keep the generic text-first fit page because the responsibility table is the useful visual.
- Include `{#habits}` after the four entries and before sources.

## Open questions

- There is no universal safe threshold. The guide requires representative cases and outcome-specific error costs rather than suggesting a default.
- Review is an operating path with capacity and ownership, not a vague fallback.
- A provider benchmark and application evidence support different claims. The checklist names the application evidence needed before automation.
