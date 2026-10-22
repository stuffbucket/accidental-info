# OpenAI / Ryan Lopopolo — notes

Collected 2026-10-21. Raw text under `b-raw/openai-harness/` and `b-raw/lopopolo-*/`.

---

## 1. Harness engineering: leveraging Codex in an agent-first world

- URL: https://openai.com/index/harness-engineering/
- Date: 2026-02-11 (date and author taken from Lopopolo's own source index, https://github.com/lopopolo/harness-engineering `sources/sources.json`, which lists it as "Canonical public statement of the practice". openai.com returned 403 to direct fetch; text retrieved through a reader proxy, byline not in the captured text.)
- Author: Ryan Lopopolo (OpenAI)
- Raw: `b-raw/openai-harness/page.txt`
- Note: the post's title is the origin of "harness engineering" as a named practice in this corpus. Böckeler (17 Feb 2026) writes that she wrote her memo "as the term first appeared" in response to this post.

### Verbatim

Setup (the constraint):

> Over the past five months, our team has been running an experiment: building and shipping an internal beta of a software product with **0 lines of manually-written code**.

> **Humans steer. Agents execute.**

> we needed to understand what changes when a software engineering team’s primary job is no longer to write code, but to design environments, specify intent, and build feedback loops that allow Codex agents to do reliable work.

> how to maximize our one truly scarce resource: human time and attention.

Measured claim (with what they did):

> Five months later, the repository contains on the order of a million lines of code across application logic, infrastructure, tooling, documentation, and internal developer utilities. Over that period, roughly 1,500 pull requests have been opened and merged with a small team of just three engineers driving Codex. This translates to an average throughput of 3.5 PRs per engineer per day, and surprisingly the throughput has _increased_ as the team has grown to now seven engineers.

(The "1/10th the time" estimate in the opening paragraph has no stated method; see hype file.)

Role of the engineer:

> Early progress was slower than we expected, not because Codex was incapable, but because the environment was underspecified.

> When something failed, the fix was almost never “try harder.” Because the only way to make progress was to get Codex to do the work, human engineers always stepped into the task and asked: “what capability is missing, and how do we make it both legible and enforceable for the agent?”

The loop (cites Ralph):

> To drive a PR to completion, we instruct Codex to review its own changes locally, request additional specific agent reviews both locally and in the cloud, respond to any human or agent given feedback, and iterate in a loop until all agent reviewers are satisfied (effectively this is a Ralph Wiggum Loop).

> Humans may review pull requests, but aren’t required to. Over time, we’ve pushed almost all review effort towards being handled agent-to-agent.

Application legibility:

> As code throughput increased, our bottleneck became human QA capacity.

> we made the app bootable per git worktree, so Codex could launch and drive one instance per change. We also wired the Chrome DevTools Protocol into the agent runtime

> Logs, metrics, and traces are exposed to Codex via a local observability stack that’s ephemeral for any given worktree.

Repository as system of record; AGENTS.md as map:

> **give Codex a map, not a 1,000-page instruction manual.**

> We tried the “one big AGENTS.md” approach. It failed in predictable ways:
> - **Context is a scarce resource.** ...
> - **Too much guidance becomes _non-guidance_.** When everything is “important,” nothing is. ...
> - **It rots instantly.** A monolithic manual turns into a graveyard of stale rules. ...
> - **It’s hard to verify.** ...

> So instead of treating AGENTS.md as the encyclopedia, we treat it as **the table of contents**.

> A short AGENTS.md (roughly 100 lines) is injected into context and serves primarily as a map, with pointers to deeper sources of truth elsewhere.

> Plans are treated as first-class artifacts. Ephemeral lightweight plans are used for small changes, while complex work is captured in execution plans with progress and decision logs that are checked into the repository.

> This enables **progressive disclosure**: agents start with a small, stable entry point and are taught where to look next, rather than being overwhelmed up front.

> A recurring “doc-gardening” agent scans for stale or obsolete documentation that does not reflect the real code behavior and opens fix-up pull requests.

Agent legibility:

> From the agent’s point of view, anything it can’t access in-context while running effectively doesn’t exist. Knowledge that lives in Google Docs, chat threads, or people’s heads are not accessible to the system.

> Technologies often described as “boring” tend to be easier for agents to model due to composability, api stability, and representation in the training set.

Enforcing architecture and taste:

> **By enforcing invariants, not micromanaging implementations, we let agents ship fast without undermining the foundation.**

> within each business domain (e.g. App Settings), code can only depend “forward” through a fixed set of layers (Types → Config → Repo → Service → Runtime → UI). Cross-cutting concerns (auth, connectors, telemetry, feature flags) enter through a single explicit interface: Providers. Anything else is disallowed and enforced mechanically.

> This is the kind of architecture you usually postpone until you have hundreds of engineers. With coding agents, it’s an early prerequisite: the constraints are what allows speed without decay or architectural drift.

> Because the lints are custom, we write the error messages to inject remediation instructions into agent context.

> In a human-first workflow, these rules might feel pedantic or constraining. With agents, they become multipliers: once encoded, they apply everywhere at once.

> enforce boundaries centrally, allow autonomy locally.

> The resulting code does not always match human stylistic preferences, and that’s okay. As long as the output is correct, maintainable, and legible to future agent runs, it meets the bar.

> When documentation falls short, we promote the rule into code

Merge philosophy:

> The repository operates with minimal blocking merge gates. Pull requests are short-lived. Test flakes are often addressed with follow-up runs rather than blocking progress indefinitely. In a system where agent throughput far exceeds human attention, corrections are cheap, and waiting is expensive.
>
> This would be irresponsible in a low-throughput environment. Here, it’s often the right tradeoff.

Human role:

> Humans always remain in the loop, but work at a different layer of abstraction than we used to. We prioritize work, translate user feedback into acceptance criteria, and validate outcomes. When the agent struggles, we treat it as a signal: identify what is missing—tools, guardrails, documentation—and feed it back into the repository, always by having Codex itself write the fix.

End-to-end autonomy (list, abridged items verbatim): "Validate the current state of the codebase", "Reproduce a reported bug", "Record a video demonstrating the failure", "Implement a fix", "Validate the fix by driving the application", "Record a second video demonstrating the resolution", "Open a pull request", "Respond to agent and human feedback", "Detect and remediate build failures", "Escalate to a human only when judgment is required", "Merge the change".

> This behavior depends heavily on the specific structure and tooling of this repository and should not be assumed to generalize without similar investment—at least, not yet.

Entropy and garbage collection (failure mode + named practice):

> Codex replicates patterns that already exist in the repository—even uneven or suboptimal ones. Over time, this inevitably leads to drift.

> Our team used to spend every Friday (20% of the week) cleaning up “AI slop.” Unsurprisingly, that didn’t scale.

> Instead, we started encoding what we call “golden principles” directly into the repository and built a recurring cleanup process.

> On a regular cadence, we have a set of background Codex tasks that scan for deviations, update quality grades, and open targeted refactoring pull requests. Most of these can be reviewed in under a minute and automerged.

> This functions like garbage collection. Technical debt is like a high-interest loan

> Human taste is captured once, then enforced continuously on every line of code.

Open questions:

> What we don’t yet know is how architectural coherence evolves over years in a fully agent-generated system.

> building software still demands discipline, but the discipline shows up more in the scaffolding rather than the code.

> **Our most difficult challenges now center on designing environments, feedback loops, and control systems** that help agents accomplish our goal: build and maintain complex, reliable software at scale.

### What this source says

An OpenAI team built an internal product with no hand-written code over five months (3 then 7 engineers, ~1,500 merged PRs). The engineers' job became building the environment: making the app, UI, logs, and metrics legible to the agent per worktree; keeping knowledge in the repo with a short AGENTS.md as a map to a `docs/` system of record; checked-in execution plans; strict layered architecture enforced by custom lints whose messages tell the agent how to fix; agent-to-agent review in a loop (they call it a Ralph Wiggum loop); few blocking merge gates; and recurring "garbage collection" agents enforcing "golden principles" against drift. When the agent fails, ask what capability is missing and add it. They say it may not generalize without similar investment and that long-run coherence is unknown.

---

## 2. Lopopolo's harness-engineering repo (README)

- URL: https://github.com/lopopolo/harness-engineering (README; repo created 2026-07-18; "Ryan Lopopolo’s anthology, field guide, and agent context bundle for harness engineering")
- Date: July 2026

### Verbatim

Definition (author's own, later and narrower than the OpenAI post):

> Harness engineering, the practice of improving agent output by shaping the environment around it, holds a chosen model and coding agent constant as a black box. It improves the two external levers—context and tools—and curates the environment around them. The worker should be able to recover intent, operate the real system, respect authority, prove the outcome, and leave the next run better equipped.

> A central purpose of that environment is to carry an organization's nonfunctional requirements: the quality attributes and constraints governing reliability, security, compatibility, maintainability, performance, operability, risk posture, and polish.

> Because work is an iterative game, a harness can make organizational judgment cumulative. Lessons from accepted work, corrections, failures, and user responses become context, boundaries, tools, examples, and checks that shape later trajectories.

> Harness engineering is the last-mile work of making it available to a capable worker as context and tools.

### What this source says

Lopopolo's later definition: hold the model and agent fixed; improve context and tools around it. The harness carries the organization's non-functional requirements and accumulates judgment from each run.

---

## 3. Stop Treating Code as the Artifact

- URL: https://hyperbo.la/w/code-is-not-the-artifact/
- Date: March 13, 2026 (updated July 17, 2026)
- Raw: `b-raw/lopopolo-code-not-artifact/page.txt`

### Verbatim

> Symphony is an issue-tracker-based agent orchestration system. It polls for work, creates an isolated workspace, runs a coding agent, and exposes enough status to operate many concurrent runs. The system is distributed first as a spec.

> Symphony is a ghost library: the spec is the distribution, and the source tree is one generated artifact.

Spec distillation loop:

> We gave the working system to Codex and asked it to write the spec. A disconnected agent was then given only that spec and asked to reimplement Symphony. Another agent compared the new implementation with the original and amended the spec where they diverged. We repeated that loop until the spec could reproduce the system with high fidelity.

> This is spec-driven development in reverse. Code is an extremely information-dense straw man for what the system could be. It is easier to build the concrete thing, engage with it as a team, and distill the accepted decisions into a spec than it is to anticipate every consequential decision up front.

> An agent-authored PR should carry the prompt that produced it because the diff only shows what was implemented.

> These constraints are also code, and all code in the repository is itself a prompt. A codebase with six competing patterns requires the model to spend attention rediscovering which one is canonical.

### What this source says

Coins "ghost library" (spec is the distribution) and describes "spec-driven development in reverse": build first, then have agents distill a spec and test it by reimplementation. PRs should carry their prompt. Code in the repo acts as a prompt for future agents, so one consistent pattern beats many.

---

## 4. Software Work Is No Longer Scheduled

- URL: https://hyperbo.la/w/software-work-not-scheduled/
- Date: March 13, 2026

### Verbatim

> I use background task for work where the desired state is already clear, the interfaces are understood, and the result can be verified.

> A background task needs enough context to identify the correct change, static guardrails to prevent obvious regressions, and an acceptance procedure that produces evidence for review.

> There is still software work that belongs on a roadmap. Building a product from zero, carrying a difficult interface refactor, or working in a part of the system where the interfaces themselves are unknown all require sustained human judgment. In these cases, producing code is incidental to deciding what should exist.

### What this source says

Defines "background task": clear desired state, known interfaces, verifiable result. Such work can go to agents asynchronously instead of competing for roadmap slots. Ambiguous work still needs human judgment.

---

## 5. The Production Function Changed

- URL: https://hyperbo.la/w/production-function-changed/
- Date: March 13, 2026

### Verbatim

> The higher the agent throughput, the more policy has to be executable. Repeating the same invariant in comments on every agent-authored PR does not scale. If it matters, it belongs in a verifier owned by the repo.

> The agent does not need to remember the rule up front; the verifier gives it the missing context exactly when it needs it.

> Review has to scale with implementation. At the end of a run, the agent should be treated like another member of the team: it needs to convince the reviewer to merge.

> The agent should attach those validation artifacts to the PR before asking for review.

> In these workflows, human implementation is no longer the constraint. The scarce work is choosing the invariant and deciding whether the proof is sufficient.

### What this source says

Agents make migrations to stricter lints cheap, so policy should become executable verifiers. Agent PRs carry their own proof (tests, logs, screenshots, video); the human decides on the invariant and whether the proof is enough.
