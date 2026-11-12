# Plan: An Accidental Guide to… Decision Models

Slug `decision-models`. Builder copied from `packages/template/`. Target about 1,100 printed words and 9 pages. Facts only from `sources.md`.

## The reader

The reader has messages, records or images that people sort quickly, but does not think of that work as classification. Terms such as model, probability and confidence make the task sound more technical than it is. The reader needs to recognize the shape of the job before choosing a product or writing code.

## The question

What does a decision model do?

## The answer, in order

1. People already make quick, bounded judgments from supplied information.
2. An application gives a decision model state, one narrow judgment question and allowed answers.
3. The model returns structured answers and numbers rather than owning the next action.
4. Forced choices and probabilities require explicit handling and testing.
5. Code applies policy after the judgment.

## Key concepts

| No. | Part | Key | Family | Meaning |
|---|---|---|---|---|
| 01 | Decision model | Dj | Ru | A model that judges supplied answers against supplied information. |
| 02 | State | Si | Wr | The information available for one judgment. |
| 03 | Judgment question | Jq | Wr | One narrow thing the model is asked to judge. |
| 04 | Allowed answers | Al | Wr | The answers the application permits. |
| 05 | Probability | Pb | Nu | A number describing how strongly an answer fits under the provider's interface. |

Plain words without tiles: code, policy, threshold, review path and confidence. The companion guide, An Accidental Guide to: From Judgment to Action, owns policy, threshold and review path.

Checked against `packages/editorial/registry.json`: all five concepts are owned here and all codes are unique.

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover and concept map | 45 |
| 2 | `{#why}` | Starts with familiar message sorting, then defines the model contract | 170 |
| 3 | `{#fit}` | Follows one message through state, question, answers, result and code | 150 |
| 4–8 | `{#entry}` × 5 | One page per key concept | 5 × 125 |
| 9 | `{#sources}` | Four checked public sources | 90 |
| | | Total | about 1,080 |

## Entries

Field marks vary where needed but always give a short answer and one detail sentence.

| Entry | Identify by | Confused with |
|---|---|---|
| Decision model | A bounded structured interface | Chatbot |
| State | Information sent with one request | Memory |
| Judgment question | One observable judgment | Instruction |
| Allowed answers | Fixed options or a scale | Generated reply |
| Probability | A number attached to an answer | Certainty |

## Cross-references

- Builds on no required earlier guide; it is the entry point to the Models group.
- Points to An Accidental Guide to: From Judgment to Action for policy, thresholds, review and evidence.

## Builder changes

- Map `Dj`, `Si`, `Jq`, `Al` and `Pb` to their registry families.
- Map singular and plural concept names in `NAME2MONO`.
- Use `Decision` / `Models` cover lines.
- Keep the generic text-first fit page. The table shows the real contract more clearly than a decorative diagram.
- Build the five entries in source order; no sequence or additional back-matter page.

## Open questions

- Providers define probability and confidence differently. The guide says to use the provider's definition and does not equate the terms.
- Some products support images and box answers. The guide mentions that capability without making it part of the common contract.
- The example scores are invented and are labeled as such. They teach result shape rather than model performance.
