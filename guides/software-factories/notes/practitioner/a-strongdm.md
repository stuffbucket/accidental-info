# StrongDM software factory (Justin McCarthy et al.): primary-source notes

Site: https://factory.strongdm.ai/ (StrongDM AI team: Justin McCarthy, co-founder and CTO; Jay Taylor; Navan Chauhan. Team founded July 14th, 2025.)
All quotes copied from pages fetched 2026-10-21. The site is a set of short pages: Story, Principles, Techniques (with subpages), Products, Weather Report.

---

## 1. "Software Factories And The Agentic Moment" (Story page)

- URL: https://factory.strongdm.ai/
- Date: February 6th, 2026, Justin McCarthy
- Coins (internal terms, per the page): **non-interactive development**, **grown software**, **scenario** (repurposed), **satisfaction**, **Digital Twin Universe (DTU)**, **"deliberate naivete"**, **"unlocks"**. The rules "Code must not be written by humans" / "Code must not be reviewed by humans" are stated here.

Definition:

> We built a Software Factory: non-interactive development where specs + scenarios drive agents that write code, run harnesses, and converge without human review.

Rules (kōan, rule, practical forms):

> - Why am I doing this? (implied: the model should be doing this instead)

> In rule form:
> - Code must not be written by humans
> - Code must not be reviewed by humans

> Finally, in practical form:
> - If you haven't spent at least $1,000 on tokens today per human engineer, your software factory has room for improvement

Compounding correctness (the claimed catalyst):

> The catalyst was a transition observed in late 2024: with the second revision of Claude 3.5 (October 2024), long-horizon agentic coding workflows began to compound correctness rather than error.

> Prior to this model improvement, iterative application of LLMs to coding tasks would accumulate errors of all imaginable varieties (misunderstandings, hallucinations, syntax, DRY violations, library incompatibility, etc). The app or product would decay and ultimately "collapse": death by a thousand cuts, etc.

> Together with YOLO mode, the updated model from Anthropic provided the first glimmer of what we now refer to internally as non-interactive development or grown software.

Charter:

> Initially it was just a hunch. An experiment. How far could we get, without writing any code by hand?
> Not very far! At least: not very far, until we added tests. However, the agent, obsessed with the immediate task, soon began to take shortcuts: return true is a great way to pass narrowly written tests, but probably won't generalize to the software you want.
> Tests were not enough.

Scenarios and satisfaction:

> One recurring theme of the agentic moment: we need new language. For example, the word "test" has proven insufficient and ambiguous. A test, stored in the codebase, can be lazily rewritten to match the code. The code could be rewritten to trivially pass the test.

> We repurposed the word scenario to represent an end-to-end "user story", often stored outside the codebase (similar to a "holdout" set in model training), which could be intuitively understood and flexibly validated by an LLM.

> Because much of the software we grow itself has an agentic component, we transitioned from boolean definitions of success ("the test suite is green") to a probabilistic and empirical one. We use the term satisfaction to quantify this validation: of all the observed trajectories through all the scenarios, what fraction of them likely satisfy the user?

Limits of tests (named failure modes):

> 1. Tests are too rigid - we were coding with agents, but we're also building with LLMs and agent loops as design primitives; evaluating success often required LLM-as-judge
> 2. Tests can be reward hacked - we needed validation that was less vulnerable to the model cheating

Digital Twin Universe:

> The Digital Twin Universe is our answer: behavioral clones of the third-party services our software depends on. We built twins of Okta, Jira, Slack, Google Docs, Google Drive, and Google Sheets, replicating their APIs, edge cases, and observable behaviors.

> With the DTU, we can validate at volumes and rates far exceeding production limits. We can test failure modes that would be dangerous or impossible against live services. We can run thousands of scenarios per hour without hitting rate limits, triggering abuse detection, or accumulating API costs.

Economics / mindset:

> Creating a high fidelity clone of a significant SaaS application was always possible, but never economically feasible.

> Those of us building software factories must practice a deliberate naivete: finding and removing the habits, conventions, and constraints of Software 1.0.

Credits others (footnotes):

> ¹ We are not alone in these convictions. See also: Luke PM's "The Software Factory", Sam Schillace's "I Have Seen the Compounding Teams", and Dan Shapiro's "Five Levels from Spicy Autocomplete to the Software Factory".
> ² Others are building factories too: Devin, 8090, Factory, Superconductor, and Jesse Vincent's Superpowers.

### What this source says

StrongDM's factory has no human writing or reviewing code. Specs ("seeds") and end-to-end scenarios drive agents until the output converges. The scenarios are kept outside the codebase, like a model-training holdout set, so the agent cannot rewrite them to pass. Success is measured as "satisfaction", the fraction of observed trajectories through the scenarios that likely satisfy the user, not as a green test suite. Scenarios run against a Digital Twin Universe of cloned third-party SaaS APIs, at volume and without rate limits. They say the approach became possible when models began to "compound correctness rather than error" (Claude 3.5 rev 2, Oct 2024). The page reports no outcome data: no defect rates, satisfaction numbers, or shipped-product results. (The "$1,000 on tokens per human engineer per day" rule is a slogan with no stated basis; see the hype file.)

---

## 2. Principles

- URL: https://factory.strongdm.ai/principles
- Date: undated (published with the site, Feb 2026)

> Seed → Validation harness → Feedback loop. Tokens are the fuel.

> Every piece of software needs an initial seed. Historically, you might have called this a PRD or a spec. Today, this could equally be a few sentences, a screenshot, or an existing codebase.

> Your validation harness must be end-to-end, as close to the real environment as possible: customers, integrations, economics.

> A sample of the output, fed back into the inputs. This closed loop allows your system to self-correct and compound correctness.

> The loop runs until the holdout scenarios pass (and stay passing)

> The theory of Validation and Feedback is easy to understand. The practice requires creative, frontier engineering. For every obstacle, ask: how can we convert this problem into a representation the model can understand?

(The page lists these inputs, rendered as tags: Use traces; Screen capture; Conversation transcripts; Incident replays; Adversarial use; Agentic simulation; Just-in-time surveys; Customer interviews; Price elasticity testing.)

### What this source says

For StrongDM, "harness" means the *validation* harness: end-to-end checks as close to the real environment as possible. This differs from HumanLayer's and Huntley's use of "harness" for the coding-agent runtime.

---

## 3. Techniques

- URL: https://factory.strongdm.ai/techniques (+ subpages)
- Named techniques: **Digital Twin Universe (DTU)**, **Gene Transfusion**, **The Filesystem**, **Shift Work**, **Semport**, **Pyramid Summaries**.

> Digital Twin Universe (DTU)
> Clone the externally observable behaviors of critical third-party dependencies. Validate at volumes and rates far exceeding production limits, with deterministic, replayable test conditions.

> Gene Transfusion
> Move working patterns between codebases by pointing agents at concrete exemplars. A solution paired with a good reference can be reproduced in new contexts.

> The Filesystem
> Models can navigate repositories quickly and adjust their own context by reading and writing files. Directories, indexes, and on-disk state become a practical memory substrate.

> Shift Work
> Separate interactive work from fully specified work. When intent is complete (specs, tests, existing apps), an agent can run end-to-end without back-and-forth.

> Semport
> Semantically-aware automated ports, one time or ongoing. Move code between languages or frameworks while preserving intent.

> Pyramid Summaries
> Reversible summarization at multiple zoom levels. Compress context without losing the ability to expand back to full detail.

The validation constraint:

> Given zero hand-written code and zero traditional review, we required a system that could:
> - Grow from cascades of natural-language specifications
> - Be validated automatically without semantic inspection of source

> Code was treated analogously to an ML model snapshot: opaque weights whose correctness is inferred exclusively from externally observable behavior. Internal structure is treated as opaque.

DTU subpage (https://factory.strongdm.ai/techniques/dtu):

> The key insight is to replicate behavior at the boundary. We build test doubles from API contracts and observed edge cases, then validate them against the live dependency until we stop finding behavioral differences.

Shift Work subpage (https://factory.strongdm.ai/techniques/shift-work):

> We distinguish between interactive and non-interactive system growth.

> Interactive
> The familiar cadence: generate, clarify, generate, approve, correct.

> Non-Interactive
> Tasks that are already fully specified.

> Spec + Test Suite = Complete Intent

> An existing application constitutes an executable specification.

> A plausible Instagram clone can be described in a few sentences of functional intent. The technical difficulty of a global, image-oriented social network lies primarily outside the functional specification: scalability, performance, availability, security, efficiency, and related properties.

Gene Transfusion subpage (https://factory.strongdm.ai/techniques/gene-transfusion):

> Gene transfusion functions as a mechanism for structure reuse without shared authorship or manual refactoring.

> Identifying Caddy's Let's Encrypt integration as a reference and using it as the basis for synthesizing native Let's Encrypt support in another module.

### What this source says

The factory treats code as opaque, like ML weights, and judges it only by external behaviour. Work is split into interactive (human and agent shaping intent together) and non-interactive (intent already complete, such as an RFC with a test suite or an existing app to port). Only non-interactive work runs unattended. StrongDM says non-functional properties (scale, security, performance) lie outside the functional spec. That is the hard part of their own Instagram example.

---

## 4. Products: Attractor

- URL: https://factory.strongdm.ai/products/attractor
- Also listed: CXDB ("Self-hosted context store for AI agents"), StrongDM ID.

> Attractor is our implementation of a non-interactive coding agent.

> It composes models, prompts, and tools into a graph-structured pipeline. It is designed to operate end-to-end once the work is fully specified.

> Attractor is structured as a graph of nodes, forming a generative SDLC.

> Each node corresponds to a phase of work and is governed by a core prompt (e.g. "implement the functionality", "identify the bottleneck").

> Edges between nodes are expressed in natural language and evaluated by the LLM.

> Execution consists of traversing this graph until convergence or termination conditions are met.

### What this source says

The factory's coding agent is a graph of phases. Each phase has a prompt, and the LLM decides which natural-language edge to take. This is the opposite of HumanLayer's "use control flow for control flow" (see a-disagreements.md).

---

## 5. Weather Report

- URL: https://factory.strongdm.ai/weather-report
- Dates: log entries February 6th, 2026 through September 28th, 2026

> What models we're running today, how they're configured, and what role each one plays in the factory.

> Consensus operator refers to an LLM merge of the points from independent plans.

Roles in the factory (table "Use" column, Sep 28, 2026): CS/Math Hard Problems; Image comprehension; Frontend Aesthetics; Frontend Architecture; Architectural Critique; Sprint Planning (consensus of two models); Devops Tasks; QA Orchestration; Security review; Bulk classification; Bulk MapReduce; UX Ideation; Copy / Writing; Agentic dialogues; Voice (interactive).

> gpt-5.3-codex remains our default implementation model — we've evaluated alternatives but haven't found a reason to switch.

(Log entry dated April 20th, 2026.)

### What this source says

The factory uses different models for different roles: implementation, architectural critique, security review, planning by consensus of two models, QA orchestration. The page is the only running record of the factory and contains model choices, not outcomes. Horthy notes in July 2026 that he could not find "definitive data/findings from StrongDM on how that whole dark factory went" (a-horthy.md section 7).
