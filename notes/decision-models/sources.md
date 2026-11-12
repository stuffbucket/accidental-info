# Sources for An Accidental Guide to… Decision Models

All fetched 12 November 2026. Excerpts are verbatim and short. Public, official documentation and the projects' own published material only.

## 1. Jev's request and result

TypeSafe, "Introduction". <https://docs.typesafe.ai/introduction.md>
Page date: none given.

- Request and result: "Send state and typed questions; get structured answers your code can use directly."
- State forms: "text, JSON, or images."
- Output forms: "typed values and probability distributions that your code can branch on, sort by, and route with."
- Mixed questions: "Any mix of question types can go in a single request."
- Bounded result: "No text generation, no parsing."
- Not stated: One portable definition of probability or confidence across providers.

## 2. Narrow judgment questions and code ownership

TypeSafe, "TypeSafe AI skill". <https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md>
Page date: none given.

- Human test: "could a smart person, shown only this state and this question, answer quickly by intuition?"
- Atomic questions: "Each question tends to work best when it asks for one judgment that a person could make at a glance."
- Separation: "Integrations tend to work best when Jev makes the judgments and code decides what to do with them."
- Null case: "Pair either one with a Noul in the same request that asks whether anything fits"
- Testing: "Start with a few representative cases, plus hard ones"

## 3. Open model task shapes

Fastino, "GLiNER2.5-Decide" model card. <https://huggingface.co/fastino/GLiNER2.5-Decide>
Page date: none given; linked paper published 24 July 2025.

- Scope: "The 340M English classification model in the GLiNER2.5 family."
- License: "License: Apache 2.0."
- Single-label result: "Single-label tasks return one string."
- Multi-label result: "Multi-label tasks return every label above the threshold."
- Predicate result: "Yes or no is the whole answer"
- Not stated consistently: Page metadata reports 0.5B parameters while the description and details report 340M. The guide does not state a size.

## 4. Local classification

GLiNER Runner, "README". <https://github.com/stuffbucket/gliner-runner>
Page date: none given.

- Local behavior: "GLiNER Runner sorts text into labels you choose. It runs on your own computer, and your text never leaves it."
- Bounded labels: "You give it some text and a list of labels. It picks the label that fits best and says how confident it is."
- Multi-label and null behavior: "The second run adds `--multi`, which lets a text have several labels, or none."

## Where sources disagree

- TypeSafe documents typed probabilities and a distinct confidence value for some questions. GLiNER Runner labels its output confidence. The guide treats the meaning as interface-specific and tells the reader to check the provider's definition.
- Fastino's model card gives two parameter counts. Size is not needed to answer the guide's question, so the guide omits it.

## For the sources page

| Source | Date | Address |
|---|---|---|
| TypeSafe, Introduction to Jev | November 2026 | docs.typesafe.ai/introduction.md |
| TypeSafe, Jev agent skill | November 2026 | github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md |
| Fastino, GLiNER2.5-Decide model card | November 2026 | huggingface.co/fastino/GLiNER2.5-Decide |
| GLiNER Runner, project documentation | November 2026 | github.com/stuffbucket/gliner-runner |
