# Matt Pocock — notes

Collected 2026-10-21. Sources: AI Hero (https://www.aihero.dev), his skills repo (https://github.com/mattpocock/skills), and his AI Coding Dictionary (https://www.aihero.dev/ai-coding-dictionary, repo https://github.com/mattpocock/dictionary-of-ai-coding). Raw: `b-raw/pocock-*`. AI Hero pages fetched via a reader proxy (r.jina.ai); "Published Time" values below come from the page metadata.

Pocock sells courses and a newsletter on AI Hero. Course/newsletter promotion is excluded below.

---

## 1. 11 Tips For AI Coding With Ralph Wiggum

- URL: https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum
- Date: 2026-01-08
- Raw: `b-raw/pocock-ralph-tips/page.txt`
- Credits Ralph to Geoffrey Huntley (links https://ghuntley.com/ralph/) and the progress-file and `passes` JSON ideas to Anthropic's long-running-agents post.

### Verbatim

Definition:

> But there's a new approach called Ralph Wiggum. Ralph runs your AI coding CLI in a loop, letting it work autonomously on a list of tasks. You define what needs to be done. Ralph figures out how - and keeps going until it's finished. In other words, it's long-running, autonomous, and unsupervised AFK coding.

His staging of AI coding phases:

> **Vibe coding** is where you let the AI write code without really checking it.
> **Planning** is where you ask the AI to plan before it codes.
> **Multi-phase plans** break large features into phases, each handled in a separate context window.
> **Ralph** simplifies everything. Instead of writing a new prompt for each phase, you run the same prompt in a loop

The loop prompt (from his `ralph.sh`; shell line-continuation backslashes removed):

> 1. Decide which task to work on next. This should be the one YOU decide has the highest priority, - not necessarily the first in the list.
> 2. Check any feedback loops, such as types and tests.
> 3. Append your progress to the progress.txt file.
> 4. Make a git commit of that feature.
> ONLY WORK ON A SINGLE FEATURE.
> If, while implementing the feature, you notice that all work is complete, output <promise>COMPLETE</promise>.

Key claim:

> The key improvement here is that **the agent chooses the task, not you**.

Two modes (table):

> **HITL** (human-in-the-loop) | Run once, watch, intervene | Learning, prompt refinement
> **AFK** (away from keyboard) | Run in a loop with max iterations | Bulk work, low-risk tasks

> For AFK Ralph, always cap your iterations. Infinite loops are dangerous with stochastic systems. I typically use 5-10 iterations for small tasks, or 30-50 for larger ones.

> The progression is simple:
> 1. Start with HITL to learn and refine
> 2. Go AFK once you trust your prompt
> 3. Review the commits when you return

Scope:

> Before you let Ralph run, you need to define what "done" looks like. This is a shift from planning to requirements gathering. Instead of specifying each step, you describe the desired end state and let the agent figure out how to get there.

Failure-mode anecdote (shortcut / premature victory):

> After three iterations, Ralph reported: "Done with all user-facing commands." But it had skipped the internal ones entirely. It decided they weren't user-facing and marked them to be ignored by coverage.

Feedback loops:

> Ralph's success depends on feedback loops. The more loops you give it, the higher quality code it produces.

> The best setup blocks commits unless everything passes. Ralph can't declare victory if the tests are red.

> Every tip in this article works for human developers too. Feedback loops, small steps, explicit scope - these aren't AI-specific techniques. They're just good engineering. Ralph makes them non-negotiable.

Small steps:

> The rate at which you can get feedback is your speed limit. Never outrun your headlights.

> context windows are limited, and LLMs get worse as they fill up. This is called context rot - the longer you go, the stupider the output.

Risk ordering:

> Use HITL Ralph for early architectural decisions - the code from these tasks stays forever, and any shortcuts here will cascade through the entire project.
>
> Save AFK Ralph for when the foundation is solid.

"The repo wins":

> Your instructions compete with your codebase. When Ralph explores your repo, it sees two sources of truth: what you told it to do and what you actually did. One is a few lines of instruction. The other is thousands of lines of evidence.

> Agents amplify what they see. Poor code leads to poorer code. Low-quality tests produce unreliable feedback loops.

> This is software entropy - the tendency of codebases to deteriorate over time. Ralph accelerates this.

Sandboxing:

> For HITL Ralph, sandboxes are optional - you're watching. For AFK Ralph, especially overnight loops, they're essential insurance against runaway agents.

His own usage (measured, personal):

> I'm on the Anthropic 5x Max plan at around £90/month. I've run AFK Ralph a few times, but most of my usage is HITL.

On his "Test Coverage Loop":

> I used this to take AI Hero CLI from 16% to 100% coverage.

Named alternative loops: "Test Coverage Loop", "Duplication Loop", "Linting Loop", "Entropy Loop".

> Any task that can be described as "look at repo, improve something, report findings" fits the Ralph pattern.

### What this source says

Ralph = the same prompt run in a capped loop over a PRD/task list; each iteration the agent picks the highest-priority task, implements one feature, runs feedback loops, appends to `progress.txt`, commits, and emits a completion marker when the list is done. Start HITL (one iteration, watched), go AFK (capped, sandboxed) once the prompt is trusted. Define "done" precisely or the agent will take shortcuts. Do risky/architectural work HITL first. Existing code outweighs instructions, so clean the repo first. Variants: coverage, duplication, lint, entropy loops.

---

## 2. Getting Started With Ralph / Getting Started (workshop)

- URLs: https://www.aihero.dev/getting-started-with-ralph (2026-01-08); https://www.aihero.dev/getting-started-m2c6l (2026-02-02)
- Raw: `b-raw/pocock-ralph-getting-started/`, `b-raw/pocock-getting-started/`

### Verbatim

> Ralph is a technique for running AI coding agents in a loop. You run the same prompt repeatedly. The AI picks its own tasks from a PRD. It commits after each feature. You come back later to working code.

> Ralph is a technique for running AI coding agents in a loop. You give it a PRD. It picks tasks, implements them, and commits. You come back to working code.

---

## 3. Skills repo — "Skills For Real Engineers"

- URL: https://github.com/mattpocock/skills (created 2026-02-03; README fetched 2026-10-21)
- Raw: `b-raw/pocock-skills-repo/` (current files) and `b-raw/pocock-skills-repo/early-2026-02-10/` (early versions from commits b81729c6ad, 2026-02-10, and 78649baa3e, 2026-02-25)

### Verbatim (README, current)

> My agent skills that I use every day to do real engineering - not vibe coding.

> Developing real applications is hard. Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve.

> These skills are designed to be small, easy to adapt, and composable.

Four named failure modes (headings, verbatim): "#1: The Agent Didn't Do What I Want", "#2: The Agent Is Way Too Verbose", "#3: The Code Doesn't Work", "#4: We Built A Ball Of Mud".

> **The Problem**. The most common failure mode in software development is misalignment.

> There is a communication gap between you and the agent. The fix for this is a **grilling session** - getting the agent to ask you detailed questions about what you're building.

> These are my most popular skills. They help you align with the agent before you get started, and think deeply about the change you're making. Use them _every_ time you want to make a change.

On shared language (borrowing DDD's ubiquitous language):

> **The Fix** for this is a shared language. It's a document that helps agents decode the jargon used in the project.

On feedback/TDD:

> For automated tests, a red-green-refactor loop is critical. This is where the agent writes a failing test first, then fixes the test. This helps give the agent a consistent level of feedback that results in far better code.

On entropy:

> Because agents can radically speed up coding, they also accelerate software entropy. Codebases get more complex at an unprecedented rate.
>
> **The Fix** for this is a radical new approach to AI-powered development: caring about the design of the code.

Skill split:

> **User-invoked** skills are reachable only when you type them (e.g. `/grill-me`); their job is to orchestrate. **Model-invoked** skills can be invoked by you _or_ reached for automatically by the agent when the task fits; they hold the reusable discipline.

Pipeline skills (current names; one-line descriptions verbatim):

> **to-spec**: Turn the current conversation into a spec and publish it to the issue tracker.
> **to-tickets**: Break any plan, spec, or conversation into a set of tracer-bullet tickets, each declaring its blocking edges
> **implement**: Build the work described by a spec or set of tickets, driving `/tdd` at pre-agreed seams and closing out with `/code-review` before committing.
> **implement-spec**: Implement a whole spec on one integration branch. Works the tickets as a task graph, running implementer subagents across the ready frontier for maximum concurrency, then closes out with `/code-review`.
> **retro**: Suggest improvements to the coding agent's environment (navigation, automated checks, coding standards, steering files, tooling) after a session, most severe first.
> **code-review**: Two-axis review of the diff since a fixed point: **Standards** ... and **Spec** ..., run as parallel sub-agents so neither pollutes the other.

### Original "grill me" (2026-02-25 version, entire skill body)

> Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.

### Current "grilling" skill (excerpts)

> Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

> Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled

> Finding _facts_ is your job, never the user's. ... The _decisions_ are the user's: put each to them and wait.

> The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed.

### Original PRD → issues pipeline (Feb 2026)

`write-a-prd` (2026-02-10) steps, verbatim excerpts:

> 4. Interview the user about the implementation. Be extremely detailed and thorough.
> 5. Hammer out the exact scope of the implementation. Work out what you plan to build and what you DON'T plan to build as part of this PRD.
> 6. Sketch out the major modules you will need to build or modify to complete the implementation. Actively look for opportunities to extract deep modules that can be tested in isolation.

> 7. ... The PRD should be submitted as a GitHub issue.

PRD template sections: "Problem Statement", "Solution", "User Stories", "'Polishing' Requirements", "Implementation Decisions" (and more).

`prd-to-issues` (2026-02-25):

> Break a PRD into independently-grabbable GitHub issues using vertical slices (tracer bullets).

> Slices may be 'HITL' or 'AFK'. HITL slices require human interaction, such as an architectural decision or a design review. AFK slices can be implemented and merged without human interaction. Prefer AFK over HITL where possible.

> - Each slice delivers a narrow but COMPLETE path through every layer (schema, API, UI, tests)
> - A completed slice is demoable or verifiable on its own
> - Prefer many thin slices over few thick ones

### Current `to-tickets` (successor to prd-to-issues)

> - Each slice is sized to fit in a single fresh context window

> Apply the `ready-for-agent` triage label unless instructed otherwise; the tickets are agent-grabbable by construction.

> **Wide refactors are the exception to vertical slicing.** ... sequence it as **expand–contract**.

### Current `tdd` skill (excerpts)

> TDD is the red → green loop.

> **Test only at pre-agreed seams.** Before writing any test, write down the seams under test and confirm them with the user.

Anti-patterns named: "Implementation-coupled", "Tautological", "Horizontal slicing".

> **Refactoring is not part of the loop.** It belongs to the review stage (see the `code-review` skill), not the red → green implementation cycle.

### What this source says

Pocock's pipeline: grill (agent interviews you down the design tree until no decision is assumed) → spec/PRD published to the issue tracker → tickets as tracer-bullet vertical slices with blocking edges, each sized to one fresh context window and labelled `ready-for-agent` (earlier: marked HITL or AFK) → implement with TDD at agreed seams → two-axis code review in sub-agents → retro that improves the agent's environment. He positions this as small composable skills against process-owning frameworks (GSD, BMAD, Spec-Kit). Names have changed over 2026 (write-a-prd → to-spec; prd-to-issues → to-tickets); the TDD skill now moves refactoring out of the loop into review.

---

## 4. AI Coding Dictionary (selected entries)

- Index: https://www.aihero.dev/ai-coding-dictionary ; repo https://github.com/mattpocock/dictionary-of-ai-coding (created 2026-05-01)
- Entry dates from repo commit history: AFK first committed 2026-05-01; "Software factory" and "Dark factory" first committed 2026-09-24.

### Software factory — https://www.aihero.dev/ai-coding-dictionary/software-factory (2026-09-24)

> A system of work where agent sessions are started by triggers — an issue being created, a schedule, a CI failure, another session finishing — rather than by a human, so more work runs AFK and human attention is spent on the human-in-the-loop decisions that remain.

> Without a factory, every session starts because someone started it. ... A factory takes the human out of starting sessions, and not necessarily out of anything else.

> A factory doesn't have to cover the whole software process. One cron job that runs one kind of session and opens one reviewable PR is a factory. Starting that small is useful: a narrow loop produces small, similar PRs, and reviewing them shows how far the loop can be trusted before it's widened.

> Humans can sit anywhere in a factory — writing and labelling the issues that trigger sessions, approving a plan before implementation starts, doing human review before merge. Deciding which of those decisions stay human is the main design question.

Trigger table rows (verbatim trigger names): "Issue created or labelled", "Schedule (cron)", "CI failure or monitoring alert", "Another session finishing".

### Dark factory — https://www.aihero.dev/ai-coding-dictionary/dark-factory (2026-09-24)

> A codebase, or part of one, where a software factory writes the code and no human reads it. There is no human review. Humans can still write the issues that start the work. But nobody reads the code that comes out. The name comes from "lights-out" factories, which make things with no people on the floor.

> A dark factory is vibe coding for an area of code, not for one change.

> The problem shows when something breaks. You do not know what changed, because nobody read the changes.

> _Avoid:_ calling a codebase "dark" only because its factory runs with nobody watching. If agent sessions run AFK and a human reviews their PRs, that is a software factory. It is not a dark factory.

### AFK — https://www.aihero.dev/ai-coding-dictionary/afk

> Away from keyboard. A working pattern where the user kicks off a session and leaves the agent to run unattended.

> The characteristic failure is coming back to hours of finished, confident work built on a wrong call made in the first ten minutes. The work isn't sloppy — it's coherent, just coherent about the wrong thing.

> Since you can't give input during the run, give it before and after instead.

> AFK doesn't remove human review; it defers all of it to the end, which is why what arrives at the end has to be worth reviewing.

> _Avoid:_ "background agent" — centers the machine ("running in the background") rather than the human pattern ("user has walked away").

### Human-in-the-loop — https://www.aihero.dev/ai-coding-dictionary/human-in-the-loop

> A working pattern where one or more humans pair with the agent during a session — reviewing, redirecting, or collaborating in real time. The human is present and engaged, not just gating individual actions.

> The judgement call is essentially: how expensive is a wrong turn, and how late would you catch it?

### Harness — https://www.aihero.dev/ai-coding-dictionary/harness

> Everything around the model that turns it into an agent: tools, system prompt, context-window management, permissions, hooks.

> The agent loop — model proposes, harness executes, repeat — is run by the harness.

### Agent (index one-liner)

> A model harnessed with tools, a system prompt, and a context window, that takes turns with a user. The model in motion.

### Spec — https://www.aihero.dev/ai-coding-dictionary/spec

> A handoff artifact describing a multi-session piece of work — what's being built, not how each session does its share. Mutates as work progresses. Made of tickets.

> The style matters less than the role: for the agent, each of these is the same thing — the durable statement of intent it reads at the start of every session.

### Grilling — https://www.aihero.dev/ai-coding-dictionary/grilling

> A technique for developing a design concept with an agent: the agent interviews the user Socratically, one decision at a time, proposing a recommended answer for each.

> The technique exists because agents fill gaps silently.

### Smart zone — https://www.aihero.dev/ai-coding-dictionary/smart-zone

> Early in a session the agent is in a "smart zone" — sharp, focused, recall is good. As the session grows it drifts into a "dumb zone": sloppier, forgetful, more mistakes

> On frontier models, the dumb zone commonly begins around 125K-150K tokens — though this is debated.

(Entry does not say who coined "smart zone"/"dumb zone".)

### AX — https://www.aihero.dev/ai-coding-dictionary/ax

> Agent experience — how well the environment is set up for an agent to do good work in a codebase. The agent-facing counterpart to DX.

Three dimensions: "Automated checks", "Architecture", "Free context".

> Humans tolerate tribal knowledge, slow CI, and "ask Sarah about the billing module"; agents can't.

### Vibe coding (index one-liner)

> A working pattern where the user accepts the agent's code without human review. The diff is treated as opaque.

### What this source says

Pocock's dictionary gives the most explicit definition of "software factory" in this source set: sessions started by triggers rather than people. A factory removes humans from starting work, not necessarily from review; "dark factory" is the case where nobody reads the output. AFK, HITL, spec, ticket, grilling, AX, smart/dumb zone are defined as a connected vocabulary.
