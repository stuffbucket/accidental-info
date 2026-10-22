# Birgitta Böckeler / martinfowler.com — notes

Collected 2026-10-21. Raw text under `b-raw/fowler-*/page.txt`. The "Exploring Generative AI" series index is https://martinfowler.com/articles/exploring-gen-ai.html (memos by Böckeler and Thoughtworks colleagues; one piece by Kief Morris included here because it defines "on the loop").

---

## 1. Harness engineering for coding agent users

- URL: https://martinfowler.com/articles/harness-engineering.html
- Date: 02 April 2026 (supersedes her memo "Harness Engineering - first thoughts", 17 February 2026, whose URL https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html now redirects here)
- Author: Birgitta Böckeler (Thoughtworks)
- Raw: `b-raw/fowler-harness/page.txt`

### Verbatim

Definition and scoping:

> The term harness has emerged as a shorthand to mean everything in an AI agent except the model itself - Agent = Model + Harness. That is a very wide definition, and therefore worth narrowing down for common categories of agents. I want to take the liberty here of defining its meaning in the bounded context of using a coding agent. In coding agents, part of the harness is already built in (e.g. via the system prompt, or the chosen code retrieval mechanism, or even a sophisticated orchestration system). But coding agents also provide us, their users, with many features to build an outer harness specifically for our use case and system.

> It has been pointed out to me that wrapping harnesses around harnesses doesn't make sense: “Have you ever tried to put a harness on the inside of a dog?” So this somewhat stretches the metaphor

Goals of the outer harness:

> A well-built outer harness serves two goals: it increases the probability that the agent gets it right in the first place, and it provides a feedback loop that self-corrects as many issues as possible before they even reach human eyes. Ultimately it should reduce the review toil and increase the system quality, all with the added benefit of fewer wasted tokens along the way.

Guides and sensors:

> - Guides (feedforward controls) - anticipate the agent's behaviour and aim to steer it before it acts. Guides increase the probability that the agent creates good results in the first attempt
> - Sensors (feedback controls) - observe after the agent acts and help it self-correct. Particularly powerful when they produce signals that are optimised for LLM consumption, e.g. custom linter messages that include instructions for the self-correction - a positive kind of prompt injection.

> Separately, you get either an agent that keeps repeating the same mistakes (feedback-only) or an agent that encodes rules but never finds out whether they worked (feed-forward-only).

Computational vs inferential:

> - Computational - deterministic and fast, run by the CPU. Tests, linters, type checkers, structural analysis. Run in milliseconds to seconds; results are reliable.
> - Inferential - Semantic analysis, AI code review, “LLM as judge”. Typically run by a GPU or NPU. Slower and more expensive; results are more non-deterministic.

Relation to context engineering:

> Context engineering provides us with the means to make guides and sensors available to the agent. Engineering a user harness for a coding agent is a specific form of context engineering.

Steering loop (human role):

> The human's job in this is to steer the agent by iterating on the harness. Whenever an issue happens multiple times, the feedforward and feedback controls should be improved to make the issue less probable to occur in the future, or even prevent it.

Timing ("keep quality left"):

> You want to have checks as far left in the path to production as possible, since the earlier you find issues, the cheaper they are to fix. Feedback sensors, including the new inferential ones, need to be distributed across the lifecycle accordingly.

Cybernetic framing:

> The agent harness acts like a cybernetic governor, combining feed-forward and feedback to regulate the codebase towards its desired state.

Three regulation categories: "Maintainability harness", "Architecture fitness harness", "Behaviour harness".

> Computational sensors catch the structural stuff reliably: duplicate code, cyclomatic complexity, missing test coverage, architectural drift, style violations.

> Neither catches reliably some of the higher-impact problems: Misdiagnosis of issues, overengineering and unnecessary features, misunderstood instructions. They'll sometimes catch them, but not reliably enough to reduce supervision. Correctness is outside any sensor's remit if the human didn't clearly specify what they wanted in the first place.

> This groups guides and sensors that define and check the architecture characteristics of the application. Basically: Fitness Functions.

Behaviour harness (open problem):

> This is the elephant in the room - how do we guide and sense if the application functionally behaves the way we need it to? At the moment, I see most people who give high autonomy to their coding agents do this:
> - Feed-forward: A functional specification (of varying levels of detail, from a short prompt to multi-file descriptions)
> - Feed-back: Check if the AI-generated test suite is green, has reasonably high coverage, some might even monitor its quality with mutation testing. Then combine that with manual testing.
>
> This approach puts a lot of faith into the AI-generated tests, that's not good enough yet.

Harnessability:

> Not every codebase is equally amenable to harnessing. A codebase written in a strongly typed language naturally has type-checking as a sensor; clearly definable module boundaries afford architectural constraint rules

> Legacy teams, especially with applications that have accrued a lot of technical debt, face the harder problem: the harness is most needed where it is hardest to build.

Ambient affordances (term credited to Ned Letcher):

> My colleague Ned Letcher uses the term “ambient affordances” for the properties of the agent environment that make it more harnessable: “structural properties of the environment itself that make it legible, navigable, and tractable to agents operating within it.”

Harness templates:

> These might evolve into harness templates in the future: a bundle of guides and sensors that leash a coding agent to the structure, conventions and tech stack of a topology.

Ashby's Law:

> The law says that a regulator must have at least as much variety as the system it governs, and it can only regulate what it has a model of. An LLM-based coding agent can produce almost anything, but committing to a topology narrows that space, making a comprehensive harness more achievable. Defining topologies is a variety-reduction move.

Role of the human:

> As human developers we bring our skills and experience as an implicit harness to every codebase.

> A coding agent has none of this: no social accountability, no aesthetic disgust at a 300-line function, no intuition that “we don't do it that way here,” and no organisational memory.

> Harnesses are an attempt to externalise and make explicit what human developer experience brings to the table, but it can only go so far. ... A good harness should not necessarily aim to fully eliminate human input, but to direct it to where our input is most important.

Open questions:

> If sensors never fire, is that a sign of high quality or inadequate detection mechanisms? We need a way to evaluate harness coverage and quality similar to what code coverage and mutation testing do for tests.

> Building this outer harness is emerging as an ongoing engineering practice, not a one-time configuration.

### What this source says

"Harness" = everything in an agent except the model. Böckeler narrows it to the "outer harness" a coding-agent user builds. It is made of guides (feedforward) and sensors (feedback), each either computational (deterministic tools) or inferential (LLM judgment). The human steers by improving the harness whenever an issue recurs (the "steering loop"). Put checks as early as cost allows. Three things a harness regulates: maintainability (easiest, existing tools), architecture fitness (fitness functions), behaviour (unsolved; AI-written tests are not trusted enough). Some codebases are more "harnessable" (types, module boundaries). Proposes "harness templates" per service topology, justified by Ashby's Law. A harness directs human input, it does not remove it.

---

## 2. Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl

- URL: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- Date: 15 October 2025
- Raw: `b-raw/fowler-sdd-tools/page.txt`

### Verbatim

> Here’s what I can gather from how I have seen it used so far: Spec-driven development means writing a “spec” before writing code with AI (“documentation first”). The spec becomes the source of truth for the human and the AI.

Three levels (her taxonomy):

> - Spec-first: A well thought-out spec is written first, and then used in the AI-assisted development workflow for the task at hand.
> - Spec-anchored: The spec is kept even after the task is complete, to continue using it for evolution and maintenance of the respective feature.
> - Spec-as-source: The spec is the main source file over time, and only the spec is edited by the human, the human never touches the code.

Her definition of spec:

> A spec is a structured, behavior-oriented artifact - or a set of related artifacts - written in natural language that expresses software functionality and serves as guidance to AI coding agents.

Memory bank vs spec:

> There is a useful difference to be made I think between specs and the more general context documents for a codebase. That general context are things like rules files, or high level descriptions of the product and the codebase. Some tools call this context a memory bank

Tool workflows (verbatim labels): Kiro "Requirements → Design → Tasks"; spec-kit "Constitution → 𝄆 Specify → Plan → Tasks 𝄇".

Warnings:

> When I asked Kiro to fix a small bug ... it quickly became clear that the workflow was like using a sledgehammer to crack a nut. The requirements document turned this small bug into 4 “user stories” with a total of 16 acceptance criteria

> To be honest, I’d rather review code than all these markdown files.

> Even with all of these files and templates and prompts and workflows and checklists, I frequently saw the agent ultimately not follow all the instructions.

> The past has shown that the best way for us to stay in control of what we’re building are small, iterative steps, so I’m very skeptical that lots of up-front spec design is a good idea, especially when it’s overly verbose.

> I wonder if spec-as-source, and even spec-anchoring, might end up with the downsides of both MDD and LLMs: Inflexibility and non-determinism.

> But the term “spec-driven development” isn’t very well defined yet, and it’s already semantically diffused. I’ve even recently heard people use “spec” basically as a synonym for “detailed prompt”.

Closing, on the German word "Verschlimmbesserung":

> Are we making something worse in the attempt of making it better?

### What this source says

SDD means writing a spec before code; it comes in three strengths (spec-first, spec-anchored, spec-as-source). A spec is a natural-language, behaviour-oriented artifact for agents; distinct from the always-loaded "memory bank". She found the tools' fixed workflows too heavy for small changes, the markdown tedious to review, and agents still ignored instructions. She compares spec-as-source to model-driven development and warns it may combine MDD's inflexibility with LLM non-determinism.

---

## 3. Context Engineering for Coding Agents

- URL: https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
- Date: 05 February 2026
- Raw: `b-raw/fowler-context-eng/page.txt`

### Verbatim

> My colleague Bharani Subramaniam’s simple definition is: “Context engineering is curating what the model sees so that you get a better result.”

Who decides to load context:

> LLM: Allowing the LLM to decide when to load context is a prerequisite for running agents in an unsupervised way. But there always remains some uncertainty (dare I say non-determinism) if the LLM will actually load the context when we would expect it to. Example: Skills
> Human: A human invocation of context gives us control, but reduces the level of automation overall. Example: Slash commands
> Agent software: Some context features are triggered by the agent software itself, at deterministic points in time. Example: Claude Code hooks

> Beware: Illusion of control
> In spite of the name, ultimately this is not really engineering… Once the agent gets all these instructions and guidance, execution still depends on how well the LLM interprets them! ... But as long as LLMs are involved, we can never be certain of anything, we still need to think in probabilities and choose the right level of human oversight for the job.

### What this source says

Defines context engineering (quoting Bharani Subramaniam) and classifies Claude Code context features by who triggers loading: the LLM (skills), the human (slash commands), or the agent software (hooks). Warns that context engineering gives probability, not control.

---

## 4. TDD inside the agent loop - theater or actual value?

- URL: https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html
- Date: 10 August 2026 (from series index)
- Raw: `b-raw/fowler-tdd-agent-loop/page.txt`

### Verbatim

Three ways to use TDD with AI:

> - Human writes the tests: A human defines the test scenarios in some form, be it in natural language, in BDD style, or directly in code. Then AI writes the implementation to make those tests pass ...
> - Review checkpoint for the human: AI writes a failing test, human looks at it to review that the test is testing the wanted behavior, then AI writes the implementation
> - Fully inside the agentic loop: Prompt an agent to write failing tests first, one by one, and then write the implementation and check that the previously failing test is green.

Result (small informal eval, 5 batches, Opus-judged, mutation scores):

> TLDR; Based on Opus's judgment of the quality of the outcomes, there was no clearly discernable difference based on TDD workflow versus no TDD workflow. On the contrary, more than once Opus ranked the non-TDD workflow solutions slightly higher in design and test quality. There was also no meaningful difference in mutation scores across the solutions.

Hypothesis:

> The TDD instructions actively work against such an up front design step. The design in those runs emerged from the sum of many locally-minimal decisions and was rarely revisited, so it tended to land on whatever shape the first test happened to lock in. Behaviour the agent didn't think to write a test for didn't get implemented at all.

Ivett Ördög, quoted:

> The way AI agents were trained is that they have seen completed functions and descriptions of those functions. The number of actual step-by-step TDD examples they have seen is a tiny part of the training data.

Costs: "At least 3x the tokens".

> TDD is a process that doesn't seem to “come natural” to models. It's like an uphill battle against the training data

Conclusions:

> I think at this point there is generally more and more evidence that being overly specific about how we want a model to do something is not a sustainable approach. Instead, we should find as many ways as we can to monitor the outcomes and give feedback.

> I personally have stopped telling my coding agents to write tests first, let alone do TDD (which I never did, to be honest), until I see evals or other strong arguments that convince me otherwise.

> I monitor and improve regression quality with the help of mutation testing, instead of giving elaborate TDD instructions and hoping for the best.

> Whatever ends up giving us trust and confidence in our software in the future - I think the role of TDD as we've known it is significantly smaller than pre-GenAI.

Mentions "Approved Scenarios" (Ivett Ördög) as a semi-manual testing approach with frozen expectations.

### What this source says

A small, self-described informal experiment found no benefit from prompting an agent to do TDD inside its own loop; non-TDD runs designed up front and ranked slightly better; TDD cost ~3x tokens. She now prefers outcome checks (regression tests, mutation testing, approved scenarios) over prescribing process.

---

## 5. Humans and Agents in Software Engineering Loops (Kief Morris)

- URL: https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html
- Date: 04 March 2026
- Author: Kief Morris (Thoughtworks)
- Raw: `b-raw/fowler-loops-morris/page.txt`

### Verbatim

> The right place for us humans is to build and manage the working loop rather than either leaving the agents to it or micromanaging what they produce. Let’s call this “on the loop.”

> As software creators we build an outcome by turning our ideas into working software and iterating as we learn and evolve our ideas. This is the “why loop”.

> The process of building the software is the “how loop.”

> Plenty of people have discovered the joy of letting humans stick to the why loop, and leaving the how loop for the agents to deal with. This is the common definition of “vibe coding”.

> When people talk about “humans in the loop”, they often mean humans as a gatekeeper within the innermost loop where code is generated, such as manually inspecting each line of code created by an LLM.

> The challenge when we insist on being too closely involved in the process is that we become a bottleneck. Agents can generate code faster than humans can manually inspect it.

> The collection of specifications, quality checks, and workflow guidance that control different levels of loops inside the how loop is the agent’s harness. The emerging practice of building and maintaining these harnesses, Harness Engineering, is how humans work on the loop.

> The “in the loop” way is to fix the artefact, whether by directly editing it, or by telling the agent to make the correction we want. The “on the loop” way is to change the harness that produced the artefact so it produces the results we want.

> Something like the on the loop concept has also been described as the “middle loop,” including by participants of The Future of Software Development Retreat.

Section "The agentic flywheel":

> The next level is humans directing agents to manage and improve the harness rather than doing it by hand.

> In practice, a cleanly-designed, well-structured codebase has externally important benefits over a messy codebase. When LLMs can more quickly understand and modify the code they work faster and spiral less.

Footnote on Ralph:

> These days “ralph loop” is often used colloquially to mean just firing up a bunch of agents and leaving them to keep looping until (hopefully) they finish their task. But as originally described the operator plays an important role in steering agents as they ralph.

### What this source says

Three human positions: outside the loop (vibe coding), in the loop (gatekeeping every line, becomes a bottleneck), on the loop (build and improve the harness that runs the how loop). Fix the harness, not the artefact. Next step is the "agentic flywheel": agents propose harness improvements, with scored auto-approval as trust grows. Internal quality still matters because agents work faster and "spiral less" in clean code.

---

## 6. I still care about the code

- URL: https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html
- Date: 09 July 2025
- Raw: `b-raw/fowler-care-code/page.txt`

### Verbatim

> LLMs are NOT compilers, interpreters, transpilers or assemblers of natural language, they are inferrers.

> And once we manage to wrap them in enough scaffolding to make them predictable, we risk stripping away the very thing that makes them valuable in the first place.

> Because of the non-deterministic nature of these inferrers, using Generative AI in the software context is constant risk assessment.

Three factors: "Impact of something going wrong", "Probability of something going wrong", "Detectability".

> Hallucinations are the core feature of LLMs. We just call it “hallucinations” when they do something we don’t want, and “intelligence” in the cases where it’s useful to us.

> If you were on call for the application you’re working on, at which point would you be ok with deploying a 1,000 or 5,000 LOC change set?

> For me personally, the minimum I want to still care about and be on top of is the test code.

### What this source says

Rejects the "code is like assembly now" view. Using AI is ongoing risk assessment by impact, probability, and detectability. Where impact is high and detectability low, read the code; at minimum, own the tests.

---

## 7. LLMs bring new nature of abstraction (Martin Fowler)

- URL: https://martinfowler.com/articles/2025-nature-abstraction.html
- Date: 24 June 2025
- Raw: `b-raw/fowler-nature-abstraction/page.txt`

### Verbatim

> I think the appearance of LLMs will change software development to a similar degree as the change from assembler to the first high-level programming languages.

> Large Language Models introduce a non-deterministic abstraction, so I can't just store my prompts in git and know that I'll get the same behavior each time. As my colleague Birgitta put it, we're not just moving up the abstraction levels, we're moving sideways into non-determinism at the same time.

> Thus far I've not had the opportunity to do more than dabble with the best Gen-AI tools

### What this source says

Fowler (by his own account a light user at the time) calls LLMs a change on the scale of assembler to high-level languages, but non-deterministic; prompts in git do not reproduce behaviour.

---

## Other series items seen (not read in full)

- "Are Harnesses Worth the Cost?" — Naresh Jain, 13 October 2026 (series index)
- "An Accidental Blackboard" — Giles Edwards-Alexander, 02 September 2026: https://martinfowler.com/articles/exploring-gen-ai/an-accidental-blackboard.html (raw saved: `b-raw/fowler-blackboard/`)
- "Sensors for coding agents" follow-up — https://martinfowler.com/articles/sensors-for-coding-agents.html (raw saved: `b-raw/fowler-sensors/`)
- "The role of developer skills in agentic coding" — 25 March 2025 (failure-mode catalogue; raw saved: `b-raw/fowler-dev-skills/`)
- "To vibe or not to vibe" — 23 September 2025 (raw saved: `b-raw/fowler-vibe/`)
