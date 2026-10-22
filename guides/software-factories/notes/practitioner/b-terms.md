# Terms of art — glossary (practitioner set B)

Each entry: who used it first in this source set (with date), their definition quoted, URL, then how other authors use the same word. "First in this source set" is not a claim of global coinage unless the author says so. Full context for each quote is in the per-author `b-*.md` files.

---

## Core words that authors use differently

### Harness

- **Böckeler** (02 Apr 2026), https://martinfowler.com/articles/harness-engineering.html
  > The term harness has emerged as a shorthand to mean everything in an AI agent except the model itself - Agent = Model + Harness.
  She then narrows it to the user's **outer harness**:
  > In coding agents, part of the harness is already built in (e.g. via the system prompt, or the chosen code retrieval mechanism, or even a sophisticated orchestration system). But coding agents also provide us, their users, with many features to build an outer harness specifically for our use case and system.
- **Pocock** (dictionary), https://www.aihero.dev/ai-coding-dictionary/harness — the vendor product layer:
  > Everything around the model that turns it into an agent: tools, system prompt, context-window management, permissions, hooks.
- **Anthropic** (Young, 26 Nov 2025), https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents — the SDK is the harness:
  > The Claude Agent SDK is a powerful, general-purpose agent harness
  but the post's "long-running agent harness" also includes the user-built init script, progress file, and feature list.
- **Lopopolo** (repo README, Jul 2026), https://github.com/lopopolo/harness-engineering — the environment around a fixed model and agent:
  > holds a chosen model and coding agent constant as a black box. It improves the two external levers—context and tools—and curates the environment around them.
- **Kief Morris** (04 Mar 2026), https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html:
  > The collection of specifications, quality checks, and workflow guidance that control different levels of loops inside the how loop is the agent’s harness.
- **Ronacher** (23 Jun 2026) uses it for the outer orchestration program ("some harness decides whether that was actually the end"; Pi "is a harness").
- **Carlini** (5 Feb 2026) uses "harness" both for the infinite-loop script and for the "test harness" written for Claude.

Divergence: two layers get the same word. Pocock/Anthropic-SDK mean the agent product (Claude Code, Codex CLI). Böckeler/Morris/Lopopolo/OpenAI mean what a team builds around that product (docs, lints, tests, checks, workflow). Böckeler flags the clash ("put a harness on the inside of a dog").

### Harness engineering

- **Hashimoto** (5 Feb 2026) — earliest dated use found here; disclaims coining it. https://mitchellh.com/writing/my-ai-adoption-journey
  > I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this "harness engineering." It is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again.
- **OpenAI / Lopopolo** (11 Feb 2026) — title of the post that made it a named practice. https://openai.com/index/harness-engineering/ . The post frames the work as:
  > design environments, specify intent, and build feedback loops that allow Codex agents to do reliable work.
- **Böckeler** (17 Feb 2026 memo, 02 Apr 2026 article) — treats it as a form of context engineering:
  > Engineering a user harness for a coding agent is a specific form of context engineering.
- **Morris** (04 Mar 2026):
  > The emerging practice of building and maintaining these harnesses, Harness Engineering, is how humans work on the loop.

Divergence: Hashimoto's is reactive (fix each observed mistake permanently). OpenAI's covers the whole environment (repo knowledge, architecture, observability, merge policy, garbage collection). Böckeler's is a control-system model (guides/sensors).

### Agent

- **Anthropic** (Dec 2024), https://www.anthropic.com/engineering/building-effective-agents:
  > Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.
  > They are typically just LLMs using tools based on environmental feedback in a loop.
- **Hashimoto** (Feb 2026):
  > An agent is the industry-adopted term for an LLM that can chat and invoke external behavior in a loop
- **Pocock** (dictionary): "A model harnessed with tools, a system prompt, and a context window, that takes turns with a user. The model in motion."
- **Anthropic** (Nov 2025) — "agent" as a role defined by its first prompt:
  > We refer to these as separate agents in this context only because they have different initial user prompts. The system prompt, set of tools, and overall agent harness was otherwise identical.
- **Beck** calls the agent "the genie" (2025–2026), and: "Nobody wants agents. Nobody wants agent swarms. I have a system and I want it to change."

Divergence: Anthropic's 2024 definition contrasts agents with **workflows** (fixed code paths); later posts use "agent" for any prompted role in a fixed orchestration (initializer, planner, evaluator), which by the 2024 definition is closer to a workflow.

### Loop

- **Anthropic** (Dec 2024): the agent loop ("LLMs using tools based on environmental feedback in a loop") and the **evaluator-optimizer** loop ("one LLM call generates a response while another provides evaluation and feedback in a loop").
- **Ronacher** (23 Jun 2026), https://lucumr.pocoo.org/2026/6/23/the-coming-loop/ — two levels:
  > There is already an agent loop inside every coding agent. ... The other loop is the harness level loop: the loop outside the agent loop.
- **Morris** (04 Mar 2026): **why loop** ("turning our ideas into working software and iterating"), **how loop** ("The process of building the software"), humans **outside / in / on the loop**, **middle loop**, **agentic flywheel**.
- **Böckeler** (Apr 2026): **steering loop** — "The human's job in this is to steer the agent by iterating on the harness."
- **Huntley / Pocock**: **Ralph loop** (below).
- **OpenAI**: "iterate in a loop until all agent reviewers are satisfied (effectively this is a Ralph Wiggum Loop)".

Divergence: "in the loop" means a human gate per line of code to Morris, but a human pairing in real time to Pocock (HITL). OpenAI says "Humans always remain in the loop, but work at a different layer of abstraction" — which Morris would call "on the loop".

### Spec

- **Huntley** (14 Jul 2025), https://ghuntley.com/ralph/:
  > Specs are formed through a conversation with the agent at the beginning phase of a project. ... issue a prompt to write the specifications out, one per file, in the specifications folder.
- **Böckeler** (15 Oct 2025), https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html:
  > A spec is a structured, behavior-oriented artifact - or a set of related artifacts - written in natural language that expresses software functionality and serves as guidance to AI coding agents.
  She notes: "I’ve even recently heard people use “spec” basically as a synonym for “detailed prompt”."
- **Pocock** (dictionary): "A handoff artifact describing a multi-session piece of work — what's being built, not how each session does its share. Mutates as work progresses. Made of tickets."
- **Anthropic** (Mar 2026): the planner expands "a simple 1-4 sentence prompt ... into a full product spec", kept at product/high-level design to avoid cascading errors.
- **Lopopolo** (13 Mar 2026): spec as the distributable artifact ("ghost library"), produced *after* the code ("spec-driven development in reverse").

Divergence: Böckeler separates specs (task-specific) from the always-loaded **memory bank**; Huntley loads specs every loop; Pocock's spec is a tracker issue made of tickets; Lopopolo's spec replaces the code as the source.

### Factory

- **Shapiro** (23 Jan 2026) — **dark factory** = level 5: "a black box that turns specs into software". https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/
- **Pocock** (dictionary, 24 Sep 2026) — **software factory**: https://www.aihero.dev/ai-coding-dictionary/software-factory
  > A system of work where agent sessions are started by triggers — an issue being created, a schedule, a CI failure, another session finishing — rather than by a human, so more work runs AFK and human attention is spent on the human-in-the-loop decisions that remain.
  — **dark factory**: "A codebase, or part of one, where a software factory writes the code and no human reads it."
- **Ronacher** (7 Sep 2026) — a "software factory" as an unsupervised setup where the model decides its own workflow; "you can now run a software factory for as long as you don’t care about the code."
- **Beck** (2 Jun 2026) — **trust factory**: "XP manufactured trust. But how? What is a trust factory?" — a process that produces trust along with code. Different sense.
- **Ronacher** (13 Feb 2026) uses the textile-mill factory as analogy for moved responsibility ("it became the responsibility of the factory as a whole").

Divergence: Pocock's factory is defined by triggers and may keep human review; Shapiro's and Pocock's "dark" variant removes review; Ronacher's usage implies no one caring about code; Beck's is about manufacturing trust, not code.

---

## Other terms (alphabetical)

**ACI (agent-computer interface)** — Anthropic, Dec 2024. "Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing." https://www.anthropic.com/engineering/building-effective-agents

**AFK** — Pocock (Ralph tips 8 Jan 2026; dictionary entry 1 May 2026). "Away from keyboard. A working pattern where the user kicks off a session and leaves the agent to run unattended." Failure: "coherent, just coherent about the wrong thing." https://www.aihero.dev/ai-coding-dictionary/afk . Pocock rejects "background agent" as a synonym; Lopopolo uses **background task** for a different idea (below).

**Agent legibility / application legibility** — OpenAI, 11 Feb 2026. "From the agent’s point of view, anything it can’t access in-context while running effectively doesn’t exist." https://openai.com/index/harness-engineering/

**Agent psychosis / slop loop** — Ronacher, 18 Jan 2026. Slop loops: "Beads and Gas Town ... are the complete celebration of slop loops." https://lucumr.pocoo.org/2026/1/18/agent-psychosis/

**Agent teams** — Carlini (Anthropic), 5 Feb 2026. "With agent teams, multiple Claude instances work in parallel on a shared codebase without active human intervention." https://www.anthropic.com/engineering/building-c-compiler

**Agentic flywheel** — Morris, 04 Mar 2026. "The next level is humans directing agents to manage and improve the harness rather than doing it by hand."

**Agentic systems; workflows vs agents** — Anthropic, Dec 2024. "Workflows are systems where LLMs and tools are orchestrated through predefined code paths." Patterns: augmented LLM, prompt chaining, routing, parallelization (sectioning, voting), orchestrator-workers, evaluator-optimizer.

**Ambient affordances** — Ned Letcher (Thoughtworks), quoted by Böckeler 02 Apr 2026: “structural properties of the environment itself that make it legible, navigable, and tractable to agents operating within it.”

**Attention budget / context rot** — Anthropic, 29 Sep 2025. Context rot (attributed to needle-in-a-haystack studies): "as the number of tokens in the context window increases, the model’s ability to accurately recall information from that context decreases." Pocock reuses "context rot" and "attention budget".

**Augmented coding** (vs **vibe coding**) — Beck, 25 Jun 2025 (and earlier posts from May 2025). "In augmented coding you care about the code, its complexity, the tests, & their coverage. The value system in augmented coding is similar to hand coding--tidy code that works." https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes . "Vibe coding" itself predates all sources here (not coined by these authors).

**AX (agent experience)** — Pocock dictionary. "how well the environment is set up for an agent to do good work in a codebase. The agent-facing counterpart to DX." Three dimensions: automated checks, architecture, free context.

**Background task** — Lopopolo, 13 Mar 2026. "work where the desired state is already clear, the interfaces are understood, and the result can be verified." https://hyperbo.la/w/software-work-not-scheduled/

**Context anxiety / context reset** — Rajasekaran (Anthropic), 24 Mar 2026. "they begin wrapping up work prematurely as they approach what they believe is their context limit." Reset = "clearing the context window entirely and starting a fresh agent, combined with a structured handoff". Distinguished from **compaction**. https://www.anthropic.com/engineering/harness-design-long-running-apps

**Context engineering** — Anthropic, 29 Sep 2025: "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference". Böckeler quotes Bharani Subramaniam: “Context engineering is curating what the model sees so that you get a better result.” She adds: "In spite of the name, ultimately this is not really engineering…". The term predates these posts; origin not traced here.

**Context window pollution / time blindness** — Carlini, 5 Feb 2026 (named LLM limitations a test harness must design around).

**Garbage collection / golden principles / doc-gardening / taste invariants** — OpenAI, 11 Feb 2026. "we started encoding what we call “golden principles” directly into the repository and built a recurring cleanup process." "This functions like garbage collection."

**Genie** — Beck (2025–). His name for the coding agent; "Genies “care” about satisfying prompts, not purposes."

**Ghost library / spec-driven development in reverse** — Lopopolo, 13 Mar 2026. "Symphony is a ghost library: the spec is the distribution, and the source tree is one generated artifact." https://hyperbo.la/w/code-is-not-the-artifact/

**Grill me / grilling** — Pocock (skill in repo by 25 Feb 2026). Original: "Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one." Anthropic's equivalent tip: "Let Claude interview you".

**Guides / sensors; computational / inferential; steering loop; harnessability; harness templates; maintainability / architecture fitness / behaviour harness** — Böckeler, 02 Apr 2026. "Guides (feedforward controls) - anticipate the agent's behaviour and aim to steer it before it acts." "Sensors (feedback controls) - observe after the agent acts and help it self-correct."

**HITL** — general term; Pocock's specific use: "A working pattern where one or more humans pair with the agent during a session". In Pocock's early `prd-to-issues`, HITL/AFK is a label on each ticket.

**Humans on the loop / in the loop / outside the loop; why loop / how loop; middle loop** — Morris, 04 Mar 2026 ("middle loop" credited to participants of The Future of Software Development Retreat).

**Initializer agent / coding agent** — Anthropic (Young), 26 Nov 2025.

**Planner / generator / evaluator; sprint contract** — Anthropic (Rajasekaran), 24 Mar 2026. Sprint contract: "agreeing on what "done" looked like for that chunk of work before any code was written."

**Progressive disclosure / just-in-time context** — Anthropic, 29 Sep 2025; OpenAI 11 Feb 2026 ("agents start with a small, stable entry point and are taught where to look next").

**Ralph / Ralph loop / Ralph Wiggum loop** — Huntley, 14 Jul 2025. "Ralph is a technique. In its purest form, Ralph is a Bash loop. while :; do cat PROMPT.md | claude-code ; done". Uses differ:
- Huntley: one item per loop, operator watches and tunes.
- Pocock (8 Jan 2026): capped iterations over a PRD, progress file, commit per feature, HITL then AFK.
- OpenAI: loop of self-review and agent reviews until reviewers are satisfied.
- Carlini: infinite loop per container in a parallel team.
- Morris footnote: "These days “ralph loop” is often used colloquially to mean just firing up a bunch of agents and leaving them to keep looping until (hopefully) they finish their task. But as originally described the operator plays an important role in steering agents as they ralph."

**Smart zone / dumb zone** — Pocock dictionary (origin not stated in the entry). "On frontier models, the dumb zone commonly begins around 125K-150K tokens — though this is debated."

**Spec-first / spec-anchored / spec-as-source** — Böckeler, 15 Oct 2025 (her taxonomy of SDD).

**Supervised collaboration** — DHH, 7 Jan 2026. "Yet pure vibe coding remains an aspirational dream for professional work for me, for now. Supervised collaboration, though, is here today." **Agent wranglers** — DHH, 7 Oct 2026.

**Tracer-bullet tickets / vertical slices** — Pocock (borrowing The Pragmatic Programmer). "Each slice cuts a narrow but COMPLETE path through every layer (schema, API, UI, tests)" and "Each slice is sized to fit in a single fresh context window".

**Trust factory; single player problem; multiplayer** — Beck, 2 Jun 2026 and 23 Apr 2026.
