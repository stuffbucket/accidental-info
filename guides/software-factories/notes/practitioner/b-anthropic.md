# Anthropic engineering posts — notes

Collected 2026-10-21. Raw text of each post saved under `b-raw/<name>/page.txt`. Quotes are verbatim from the fetched pages.

---

## 1. Building effective agents

- URL: https://www.anthropic.com/engineering/building-effective-agents
- Date: Dec 19, 2024 (page now carries a note that "Much of the tooling landscape described in this post has changed since December 2024")
- Authors: Erik S. and Barry Zhang
- Raw: `b-raw/anthropic-building-agents/page.txt`

### Verbatim

Definition of agentic systems, workflows, agents:

> "Agent" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as agentic systems, but draw an important architectural distinction between workflows and agents:
>
> - Workflows are systems where LLMs and tools are orchestrated through predefined code paths.
> - Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

Rule: start simple.

> When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense.

> When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale.

On frameworks:

> However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice.

> We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error.

Named building block and patterns (each has a diagram in the post):

> The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory.

> Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate” in the diagram below) on any intermediate steps to ensure that the process is still on track.

> Routing classifies an input and directs it to a specialized followup task.

> LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations:
> - Sectioning: Breaking a task into independent subtasks run in parallel.
> - Voting: Running the same task multiple times to get diverse outputs.

> In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.

> In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.

> When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value.

Agent definition and loop:

> Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop.

> During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it’s also common to include stopping conditions (such as a maximum number of iterations) to maintain control.

Failure mode / warning:

> The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails.

Three principles:

> When implementing agents, we try to follow three core principles:
> - Maintain simplicity in your agent's design.
> - Prioritize transparency by explicitly showing the agent’s planning steps.
> - Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing.

> To repeat: you should consider adding complexity only when it demonstrably improves outcomes.

### What this source says

Anthropic separates "workflows" (fixed code paths that call LLMs) from "agents" (the LLM decides its own steps and tool use). Both are "agentic systems". It names one building block (the augmented LLM) and five workflow patterns: prompt chaining, routing, parallelization (sectioning, voting), orchestrator-workers, evaluator-optimizer. An agent is "LLMs using tools based on environmental feedback in a loop". The main rule is to use the simplest thing that works and add complexity only when measurement shows it helps. Coins "agent-computer interface (ACI)" as the tool surface to design carefully.

---

## 2. Effective context engineering for AI agents

- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Date: Sep 29, 2025
- Authors: Anthropic Applied AI team (Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield, and others)
- Raw: `b-raw/anthropic-context-eng/page.txt`

### Verbatim

Definition:

> At Anthropic, we view context engineering as the natural progression of prompt engineering. Prompt engineering refers to methods for writing and organizing LLM instructions for optimal outcomes (see our docs for an overview and useful prompt engineering strategies). Context engineering refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts.

Context rot / attention budget:

> Studies on needle-in-a-haystack style benchmarking have uncovered the concept of context rot: as the number of tokens in the context window increases, the model’s ability to accurately recall information from that context decreases.

> Context, therefore, must be treated as a finite resource with diminishing marginal returns. Like humans, who have limited working memory capacity, LLMs have an “attention budget” that they draw on when parsing large volumes of context.

Guiding principle:

> Given that LLMs are constrained by a finite attention budget, good context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome.

Right altitude:

> The right altitude is the Goldilocks zone between two common failure modes. At one extreme, we see engineers hardcoding complex, brittle logic in their prompts to elicit exact agentic behavior. This approach creates fragility and increases maintenance complexity over time. At the other extreme, engineers sometimes provide vague, high-level guidance that fails to give the LLM concrete signals for desired outputs or falsely assumes shared context.

Just-in-time context and progressive disclosure:

> Rather than pre-processing all relevant data up front, agents built with the “just in time” approach maintain lightweight identifiers (file paths, stored queries, web links, etc.) and use these references to dynamically load data into context at runtime using tools.

> Letting agents navigate and retrieve data autonomously also enables progressive disclosure—in other words, allows agents to incrementally discover relevant context through exploration.

> Claude Code is an agent that employs this hybrid model: CLAUDE.md files are naively dropped into context up front, while primitives like glob and grep allow it to navigate its environment and retrieve files just-in-time, effectively bypassing the issues of stale indexing and complex syntax trees.

Long-horizon techniques:

> To enable agents to work effectively across extended time horizons, we've developed a few techniques that address these context pollution constraints directly: compaction, structured note-taking, and multi-agent architectures.

> Compaction is the practice of taking a conversation nearing the context window limit, summarizing its contents, and reinitiating a new context window with the summary.

> Structured note-taking, or agentic memory, is a technique where the agent regularly writes notes persisted to memory outside of the context window. These notes get pulled back into the context window at later times.

> Rather than one agent attempting to maintain state across an entire project, specialized sub-agents can handle focused tasks with clean context windows. The main agent coordinates with a high-level plan while subagents perform deep technical work or use tools to find relevant information. Each subagent might explore extensively, using tens of thousands of tokens or more, but returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens).

> We're already seeing that smarter models require less prescriptive engineering, allowing agents to operate with more autonomy.

### What this source says

Context engineering is the wider job of choosing every token the model sees, not only the prompt. Because accuracy falls as context grows ("context rot"), context is a budget. Aim for the smallest high-signal set. Pitch instructions at the "right altitude": neither brittle hard-coded logic nor vague guidance. Let agents fetch context "just in time" by reference (paths, queries) so they disclose it to themselves progressively. For long tasks use compaction, structured notes kept outside the window, and sub-agents that return short summaries.

Note: "context rot" is attributed in the post to needle-in-a-haystack studies, not coined by Anthropic.

---

## 3. Effective harnesses for long-running agents

- URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Date: Nov 26, 2025
- Author: Justin Young
- Raw: `b-raw/anthropic-harnesses/page.txt`

### Verbatim

Problem statement:

> The core challenge of long-running agents is that they must work in discrete sessions, and each new session begins with no memory of what came before. Imagine a software project staffed by engineers working in shifts, where each new engineer arrives with no memory of what happened on the previous shift.

Harness definition (of the SDK):

> The Claude Agent SDK is a powerful, general-purpose agent harness adept at coding, as well as other tasks that require the model to use tools to gather context, plan, and execute.

> However, compaction isn’t sufficient.

Failure modes:

> First, the agent tended to try to do too much at once—essentially to attempt to one-shot the app. Often, this led to the model running out of context in the middle of its implementation, leaving the next session to start with a feature half-implemented and undocumented.

> A second failure mode would often occur later in a project. After some features had already been built, a later agent instance would look around, see that progress had been made, and declare the job done.

> One final major failure mode that we observed was Claude’s tendency to mark a feature as complete without proper testing.

Two-agent pattern:

> - Initializer agent: The very first agent session uses a specialized prompt that asks the model to set up the initial environment: an init.sh script, a claude-progress.txt file that keeps a log of what agents have done, and an initial git commit that shows what files were added.
> - Coding agent: Every subsequent session asks the model to make incremental progress, then leave structured updates.

Footnote:

> We refer to these as separate agents in this context only because they have different initial user prompts. The system prompt, set of tools, and overall agent harness was otherwise identical.

Clean state:

> By “clean state” we mean the kind of code that would be appropriate for merging to a main branch: there are no major bugs, the code is orderly and well-documented, and in general, a developer could easily begin work on a new feature without first having to clean up an unrelated mess.

Feature list as spec:

> we prompted the initializer agent to write a comprehensive file of feature requirements expanding on the user’s initial prompt. In the claude.ai clone example, this meant over 200 features ... These features were all initially marked as “failing” so that later coding agents would have a clear outline of what full functionality looked like.

> We prompt coding agents to edit this file only by changing the status of a passes field, and we use strongly-worded instructions like “It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality.” After some experimentation, we landed on using JSON for this, as the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files.

Incremental progress:

> the next iteration of the coding agent was then asked to work on only one feature at a time. This incremental approach turned out to be critical to addressing the agent’s tendency to do too much at once.

Verification:

> Claude mostly did well at verifying features end-to-end once explicitly prompted to use browser automation tools and do all testing as a human user would.

Session start routine:

> - Run pwd to see the directory you’re working in. You’ll only be able to edit files in this directory.
> - Read the git logs and progress files to get up to speed on what was recently worked on.
> - Read the features list file and choose the highest-priority feature that’s not yet done to work on.

Failure-mode table (rows, verbatim problem column):

> Claude declares victory on the entire project too early.
> Claude leaves the environment in a state with bugs or undocumented progress.
> Claude marks features as done prematurely.
> Claude has to spend time figuring out how to run the app.

Open question:

> it’s still unclear whether a single, general-purpose coding agent performs best across contexts, or if better performance can be achieved through a multi-agent architecture.

### What this source says

Long tasks span many context windows, and each new session starts blank. Compaction alone did not fix this. The harness: an initializer agent writes `init.sh`, a progress file, a JSON feature list (all "failing"), and a first commit; every later coding agent reads progress and git log, runs a smoke test, picks one feature, implements it, verifies it end-to-end as a user would (browser automation), commits, and updates progress. Named failure modes: one-shotting, declaring victory early, marking features done without testing, leaving a dirty state. "Initializer" and "coding" agent differ only in their first prompt.

---

## 4. Harness design for long-running application development

- URL: https://www.anthropic.com/engineering/harness-design-long-running-apps
- Date: Mar 24, 2026
- Author: Prithvi Rajasekaran (Labs team)
- Raw: `b-raw/anthropic-harness-design/page.txt`

### Verbatim

Lineage, citing Ralph:

> In an earlier experiment, we used an initializer agent to decompose a product spec into a task list, and a coding agent that implemented the tasks one feature at a time before handing off artifacts to carry context across sessions. The broader developer community has converged on similar insights, with approaches like the "Ralph Wiggum" method using hooks or scripts to keep agents in continuous iteration cycles.

Context anxiety and context resets (named failure mode):

> Some models also exhibit "context anxiety," in which they begin wrapping up work prematurely as they approach what they believe is their context limit. Context resets—clearing the context window entirely and starting a fresh agent, combined with a structured handoff that carries the previous agent's state and the next steps—addresses both these issues.

> This differs from compaction, where earlier parts of the conversation are summarized in place so the same agent can keep going on a shortened history. While compaction preserves continuity, it doesn't give the agent a clean slate, which means context anxiety can still persist.

Self-evaluation failure mode:

> When asked to evaluate work they've produced, agents tend to respond by confidently praising the work—even when, to a human observer, the quality is obviously mediocre.

> Separating the agent doing the work from the agent judging it proves to be a strong lever to address this issue. ... But tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work, and once that external feedback exists, the generator has something concrete to iterate against.

GAN-inspired generator/evaluator:

> Taking inspiration from Generative Adversarial Networks (GANs), I designed a multi-agent structure with a generator and evaluator agent.

Grading criteria for design (four): "Design quality", "Originality", "Craft", "Functionality". Example:

> Originality: Is there evidence of custom decisions, or is this template layouts, library defaults, and AI-generated patterns? ... Unmodified stock components—or telltale signs of AI generation like purple gradients over white cards—fail here.

> I calibrated the evaluator using few-shot examples with detailed score breakdowns.

Three-agent architecture (Planner / Generator / Evaluator):

> Planner: Our previous long-running harness required the user to provide a detailed spec upfront. I wanted to automate that step, so I created a planner agent that took a simple 1-4 sentence prompt and expanded it into a full product spec. I prompted it to be ambitious about scope and to stay focused on product context and high level technical design rather than detailed technical implementation. This emphasis was due to the concern that if the planner tried to specify granular technical details upfront and got something wrong, the errors in the spec would cascade into the downstream implementation.

> Generator: ... instructing the generator to work in sprints, picking up one feature at a time from the spec.

> Evaluator: Applications from earlier harnesses often looked impressive but still had real bugs when you actually tried to use them. To catch these, the evaluator used the Playwright MCP to click through the running application the way a user would, testing UI features, API endpoints, and database states. ... Each criterion had a hard threshold, and if any one fell below it, the sprint failed and the generator got detailed feedback on what went wrong.

Sprint contract (named pattern):

> Before each sprint, the generator and evaluator negotiated a sprint contract: agreeing on what "done" looked like for that chunk of work before any code was written.

> Communication was handled via files: one agent would write a file, another agent would read it and respond either within that file or with a new file that the previous agent would read in turn.

Principle on harness components going stale:

> every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing, both because they may be incorrect, and because they can quickly go stale as models improve.

> I moved to a more methodical approach, removing one component at a time and reviewing what impact it had on the final result.

On when the evaluator is worth it:

> The practical implication is that the evaluator is not a fixed yes-or-no decision. It is worth the cost when the task sits beyond what the current model does reliably solo.

> Without the planner, the generator under-scoped: given the raw prompt, it would start building without first speccing its work, and end up creating a less feature-rich application than the planner did.

Outlook:

> In some cases, that will mean the scaffold surrounding the model matters less over time, and developers can wait for the next model and see certain problems solve themselves. On the other hand, the better the models get, the more space there is to develop harnesses that can achieve complex tasks beyond what the model can do at baseline.

### What this source says

Two failure modes persist on long tasks: losing coherence as context fills (including "context anxiety", where a model wraps up early near its believed limit), and lenient self-evaluation. Fixes: context resets with a handoff file (instead of only compaction), and a separate, tuned-to-be-skeptical evaluator agent. The full-stack harness has three roles (planner, generator, evaluator); generator and evaluator agree a "sprint contract" for what done means before coding, and talk via files. Every harness part is an assumption about what the model can't do; remove parts one at a time as models improve. With Opus 4.6 the sprint construct was dropped and the evaluator moved to one pass at the end; the planner stayed.

---

## 5. Building a C compiler with a team of parallel Claudes

- URL: https://www.anthropic.com/engineering/building-c-compiler
- Date: Feb 5, 2026
- Author: Nicholas Carlini (Safeguards team)
- Raw: `b-raw/anthropic-c-compiler/page.txt`

### Verbatim

Term "agent teams":

> I've been experimenting with a new approach to supervising language models that we’re calling "agent teams."
>
> With agent teams, multiple Claude instances work in parallel on a shared codebase without active human intervention.

Measured claim with method:

> To stress test it, I tasked 16 agents with writing a Rust-based C compiler, from scratch, capable of compiling the Linux kernel. Over nearly 2,000 Claude Code sessions and $20,000 in API costs, the agent team produced a 100,000-line compiler that can build Linux 6.9 on x86, ARM, and RISC-V.

The loop (Ralph-style):

> To elicit sustained, autonomous progress, I built a harness that sticks Claude in a simple loop (if you’ve seen Ralph-loop, this should look familiar). When it finishes one task, it immediately picks up the next. (Run this in a container, not your actual machine).

```
while true; do
 COMMIT=$(git rev-parse --short=6 HEAD)
 LOGFILE="agent_logs/agent_${COMMIT}.log"
 claude --dangerously-skip-permissions \
 -p "$(cat AGENT_PROMPT.md)" \
 --model claude-opus-X-Y &> "$LOGFILE"
done
```

Coordination via git locks:

> Claude takes a "lock" on a task by writing a text file to current_tasks/ ... If two agents try to claim the same task, git's synchronization forces the second agent to pick a different one.

> I haven’t yet implemented any other method for communication between agents, nor do I enforce any process for managing high-level goals. I don’t use an orchestration agent.

Where effort goes:

> The scaffolding runs Claude in a loop, but that loop is only useful if Claude can tell how to make progress. Most of my effort went into designing the environment around Claude—the tests, the environment, the feedback—so that it could orient itself without me.

Rules:

> Claude will work autonomously to solve whatever problem I give it. So it’s important that the task verifier is nearly perfect, otherwise Claude will solve the wrong problem.

> I had to constantly remind myself that I was writing this test harness for Claude and not for myself, which meant rethinking many of my assumptions about how tests should communicate results.

Named LLM limitations to design around:

> - Context window pollution: The test harness should not print thousands of useless bytes. At most, it should print a few lines of output and log all important information to a file so Claude can find it when needed.
> - Time blindness: Claude can't tell time and, left alone, will happily spend hours running tests instead of making progress.

Parallelism failure and fix (oracle):

> Every agent would hit the same bug, fix that bug, and then overwrite each other's changes. Having 16 agents running didn't help because each was stuck solving the same task.
>
> The fix was to use GCC as an online known-good compiler oracle to compare against.

Roles:

> LLM-written code frequently re-implements existing functionality, so I tasked one agent with coalescing any duplicate code it found. I put another in charge of improving the performance of the compiler itself, and a third I made responsible for outputting efficient compiled code. I asked another agent to critique the design of the project from the perspective of a Rust developer ... and another to work on documentation.

Limits and warning:

> The resulting compiler has nearly reached the limits of Opus’s abilities. ... New features and bugfixes frequently broke existing functionality.

> For autonomous systems, it is easy to see tests pass and assume the job is done, when this is rarely the case. I used to work in penetration testing, exploiting vulnerabilities in products produced by large companies, and the thought of programmers deploying software they’ve never personally verified is a real concern.

### What this source says

A fleet of 16 Claude agents in Docker containers, each in an infinite bash loop, shared a bare git repo and claimed tasks with lock files. No orchestrator. The author's effort went into the verifier (tests, CI, a GCC oracle) and making test output agent-readable (short output, grep-able ERROR lines, a `--fast` deterministic sample). Parallelism only helped when work could be split into independent failing tests; one big task (Linux kernel) needed an oracle to split it. Specialist agents handled dedup, performance, design critique, docs. He reports the cost and the code-quality limits and warns that passing tests is not proof.

---

## 6. Best practices for Claude Code

- URL (now): https://code.claude.com/docs/en/best-practices (redirected from https://www.anthropic.com/engineering/claude-code-best-practices; original blog post Apr 2025)
- Date: fetched 2026-10-21 (living document)
- Raw: `b-raw/anthropic-cc-best/page.txt`

### Verbatim

> Most best practices are based on one constraint: Claude’s context window fills up fast, and performance degrades as it fills.

Verification first:

> Give Claude a check it can run: tests, a build, a screenshot to compare. It’s the difference between a session you watch and one you walk away from.

> Claude stops when the work looks done. Without a check it can run, “looks done” is the only signal available, and you become the verification loop: every mistake waits for you to notice it.

Four gate strengths:

> - In one prompt: ask Claude to run the check and iterate in the same message, as in the table above.
> - Across a session: set the check as a /goal condition. A separate evaluator re-checks it after every turn and Claude keeps working until the goal resolves.
> - As a deterministic gate: a Stop hook runs your check as a script and blocks the turn from ending until it passes.
> - By a second opinion: a verification subagent or a dynamic workflow that checks its own findings has a fresh model try to refute the result, so the agent doing the work isn’t the one grading it.

> Have Claude show evidence rather than asserting success: the test output, the command it ran and what it returned, or a screenshot of the result.

Workflow phases: "Explore", "Plan", "Implement", "Commit".

> If you could describe the diff in one sentence, skip the plan.

Interview:

> For larger features, have Claude interview you first. Start with a minimal prompt and ask Claude to interview you using the AskUserQuestion tool.

Writer/Reviewer pattern and adversarial review:

> Before treating a task as done, have a subagent review the diff in a fresh context and report gaps.

> A reviewer running in a fresh subagent context sees only the diff and the criteria you give it, not the reasoning that produced the change, so it evaluates the result on its own terms.

Fan out:

> Loop through tasks calling claude -p for each. Use --allowedTools to pre-approve tools for batch operations.

Named failure patterns:

> - The kitchen sink session. ...
> - Correcting over and over. ... Fix: After two failed corrections, /clear and write a better initial prompt incorporating what you learned.
> - The over-specified CLAUDE.md. If your CLAUDE.md is too long, Claude ignores half of it because important rules get lost in the noise. Fix: Ruthlessly prune. If Claude already does something correctly without the instruction, delete it or convert it to a hook.
> - The trust-then-verify gap. Claude produces a plausible-looking implementation that doesn’t handle edge cases. Fix: Always provide verification (tests, scripts, screenshots). If you can’t verify it, don’t ship it.
> - The infinite exploration. ...

### What this source says

Two constraints drive the advice: context fills fast and degrades, and the agent stops when work "looks done". So: give a runnable check and decide how hard it gates (prompt, `/goal`, Stop hook, independent verifier); ask for evidence; explore → plan → implement → commit for non-trivial work; let the agent interview you for large features; use a separate reviewer context; fan out with `claude -p` loops or worktrees. Five named anti-patterns.
