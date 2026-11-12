# Sources for An Accidental Guide to… From Judgment to Action

All fetched 12 November 2026. Excerpts are verbatim and short. Public, official documentation and the projects' own published material only.

## 1. Judgment and policy separation

TypeSafe, "TypeSafe AI skill". <https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md>
Page date: none given.

- Separation: "Integrations tend to work best when Jev makes the judgments and code decides what to do with them."
- Visible policy: "write the decision itself in code, where it's visible and testable"
- Atomic work: "Break complex judgments or decisions into their parts, and combine the answers in code"
- Representative testing: "Start with a few representative cases, plus hard ones"

## 2. Scores as inputs to code

TypeSafe, "Introduction". <https://docs.typesafe.ai/introduction.md>
Page date: none given.

- Code can use results directly: "typed values and probability distributions that your code can branch on, sort by, and route with."
- Policy formulas belong outside prompts: "Combine the scores with your own formula"
- Policy can change in code: "a coefficient in your code rather than rewriting a prompt."

## 3. The model-policy boundary

Decision Models for Humans, "The mental model". <https://github.com/stuffbucket/decision-models-for-humans/blob/main/docs/mental-model.md>
Page date: none given.

- Model contract: "A decision model makes bounded judgments over information supplied by an application."
- Policy boundary: "What should the company do? The answer depends on policy that belongs in code."
- Change isolation: "This exposes missing cases and lets the organization change policy without retraining or rewording the model questions."
- Null behavior: "A pick-one question always has a winner, even when no option fits."
- Threshold practice: "collect representative labeled cases" and "give the middle region an explicit outcome, usually review"

## 4. What evidence supports

Decision Models for Humans, "Evidence". <https://github.com/stuffbucket/decision-models-for-humans/blob/main/docs/evidence.md>
Page date: none given.

- Application evidence: "representative application data, human labeling guidance, error costs, thresholds, review capacity, drift monitoring and a fallback path."
- Limit of generic evidence: "No generic benchmark can settle this claim."
- Demonstration limit: "A polished demonstration can make a model understandable. It cannot establish that the model is good enough for a job."
- Change control: "Keep the exact payload and rerun held-out cases after a change."
- Threshold basis: "Thresholds should follow the cost of errors."

## Where sources disagree

- The sources use probability, score and confidence for provider-specific outputs. The guide calls the model result a judgment and tells readers to preserve the provider's definition.
- No source offers a universal threshold. The guide explicitly rejects copied defaults and ties each threshold to labeled cases, one policy path and its error costs.

## For the sources page

| Source | Date | Address |
|---|---|---|
| TypeSafe, Jev agent skill | November 2026 | github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md |
| TypeSafe, Introduction to Jev | November 2026 | docs.typesafe.ai/introduction.md |
| Decision Models for Humans, Mental model | November 2026 | github.com/stuffbucket/decision-models-for-humans/blob/main/docs/mental-model.md |
| Decision Models for Humans, Evidence | November 2026 | github.com/stuffbucket/decision-models-for-humans/blob/main/docs/evidence.md |
