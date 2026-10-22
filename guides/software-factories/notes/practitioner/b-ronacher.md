# Armin Ronacher — notes

Collected 2026-10-21. Blog: https://lucumr.pocoo.org/ (AI tag list: https://lucumr.pocoo.org/tags/ai/). Raw: `b-raw/armin-*/page.txt`. Ronacher created Flask; co-builds the Pi coding agent harness.

---

## 1. Agentic Coding Recommendations

- URL: https://lucumr.pocoo.org/2025/6/12/agentic-coding/
- Date: June 12, 2025

### Verbatim

> My general workflow involves assigning a job to an agent (which effectively has full permissions) and then waiting for it to complete the task. I rarely interrupt it, unless it’s a small task.

> I disable all permission checks. ... Now you can call that irresponsible and there are definitely risks with it, but you can manage those risks with moving your dev env into docker.

Tool rules:

> Anything can be a tool. A shell script can be a tool, an MCP server can be a tool, a log file can be a tool. If the agent can interact or observe it, it counts.
> Tools need to be fast. The quicker they respond (and the less useless output they produce) the better. Crashes are tolerable; hangs are problematic.
> Tools need to be user friendly! Tools must clearly inform agents of misuse or errors to ensure forward progress.
> Tools need to be protected against an LLM chaos monkey using them completely wrong. There is no such things as user error or undefined behavior!
> Tools need to provide the right debuggability and observability.

> Agentic coding’s inefficiency largely arises from inference cost and suboptimal tool usage.

> Getting observability from the first shot of code generation beats writing code, failing to run it and only then going back to a debug loop where debug information is added.

Codebase rules:

> Simple code significantly outperforms complex code in agentic contexts. ... Have the agent do “the dumbest possible thing that will work”.

> Keep important checks local. ... Hiding permission checks in another file or some config file will amost guarantee you that the AI will forget to add permission checks in when adding new routes.

> agents make upgrades so “cheap” that it’s tempting to just let the AI do it and see if tests still pass. I do not find this to be a successful path at all. Be even more conservative about upgrades than before.

> Agents aren’t exceptionally fast individually, but parallelization boosts overall efficiency.

> Agentic coding alters refactoring priorities. Agents handle tasks effectively until project complexity surpasses some manageable thresholds.

Language choice: he recommends Go for new backends because of explicit context, test caching, simplicity, structural interfaces, low ecosystem churn.

### What this source says

Run the agent with full permissions in a container and let it finish. Make tools fast, quiet, robust to misuse, and observable (log to files the agent can read). Prefer simple code, plain SQL, local permission checks, stable ecosystems, few dependencies. Refactor before complexity passes what the agent can handle.

---

## 2. Agentic Coding Things That Didn’t Work

- URL: https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/
- Date: July 30, 2025

### Verbatim

> - I only automate things that I do regularly.
> - If I create an automation for something that I do regularly, but then I stop using the automation, I consider it a failed automation and I delete it.

> I tried hard to make hooks work, but I haven’t seen any efficiency gains from them yet.

> Anything we can fully automate, we should. Using an LLM for tasks that don’t require inference is the wrong approach in my book.

> What’s interesting about workflow automation is that without rigorous rules that you consistently follow as a developer, simply taking time to talk to the machine and give clear instructions outperforms elaborate pre-written prompts.

> The rule I have now is that if I do want to automate something, I must have done it a few times already, and then I evaluate whether the agent gets any better results through my automation. ... I mostly measure that right now by letting it do the same task three times and looking at the variance manually

### What this source says

Most of his slash commands, hooks, and print-mode scripts did not last. Rule: automate only what you already do repeatedly, check it improves results (run three times, compare variance), and delete unused automations. Deterministic work belongs in scripts, not inference.

---

## 3. 90%

- URL: https://lucumr.pocoo.org/2025/9/29/90-percent/
- Date: September 29, 2025

### Verbatim

> For the infrastructure component I started at my new company, I’m probably north of 90% AI-written code.

> I began in the traditional way: system design, schema, architecture. At this state I don’t let the AI write, but I loop it in AI as a kind of rubber duck.

> the constant is Codex for code review after PRs.

> I cannot stress enough how bad the code from these agents can be if you’re not careful. While they understand system architecture and how to build something, they can’t keep the whole picture in scope. They will recreate things that already exist. They create abstractions that are completely inappropriate for the scale of the problem.

> The most important piece of working with an agent is the same as regular software engineering. You need to understand your state machines, how the system behaves at any point in time, your database.

> At the same time, for me, AI doesn’t own the code. I still review every line, shape the architecture, and carry the responsibility for how it runs in production.

### What this source says

A measured personal claim (one Go service, >90% AI-written) with method: human does design, schema, architecture; agents write in PR-sized reviewable chunks; Codex reviews PRs; he reviews every line and owns production.

---

## 4. Agent Psychosis: Are We Going Insane?

- URL: https://lucumr.pocoo.org/2026/1/18/agent-psychosis/
- Date: January 18, 2026

### Verbatim

> And then there are things like Beads and Gas Town, Steve Yegge’s agentic coding tools, which are the complete celebration of slop loops.

> There is also another side to this slop loop addiction: token consumption.

> It takes you a minute of prompting and waiting a few minutes for code to come out of it. But actually honestly reviewing a pull request takes many times longer than that. The asymmetry is completely brutal.

> Every day brings more PRs that took someone a minute to generate and take an hour to review.

### What this source says

Names "slop loops" and "agent psychosis" (people over-trusting their agent "dæmon"). Criticizes Gas Town/Beads as uncontrolled slop loops. Names the generation/review asymmetry that burdens maintainers.

---

## 5. The Final Bottleneck

- URL: https://lucumr.pocoo.org/2026/2/13/the-final-bottleneck/
- Date: February 13, 2026

### Verbatim

> Historically, writing code was slower than reviewing code.

> Anyone who has worked with queues knows this: if input grows faster than throughput, you have an accumulating failure. At that point, backpressure and load shedding are the only things that retain a system that can still operate.

> When one part of the pipeline becomes dramatically faster, you need to throttle input.

> If the machine writes the code, the machine better review the code at the same time. So what ultimately comes up for human review would already have passed the most critical possible review of the most capable machine.

> As we’re entering the phase of single-use plastic software, we might be moving the whole layer of responsibility elsewhere.

> We will find ways to take responsibility for what we ship, because society will demand it. Non-sentient machines will never be able to carry responsibility

> I too am the bottleneck now. But you know what? Two years ago, I too was the bottleneck. I was the bottleneck all along.

### What this source says

Uses the textile-mill analogy: removing one bottleneck moves it downstream. Review is now the bottleneck; options are throttling input (as Pi does by auto-closing untrusted PRs) or machine review before human review. Accountability stays with humans.

---

## 6. The Coming Loop

- URL: https://lucumr.pocoo.org/2026/6/23/the-coming-loop/
- Date: June 23, 2026

### Verbatim

Epigraph (quoted, attributed to Boris Cherny; not a primary source for Cherny):

> I don’t prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops.
> — Boris Cherny

Definition of the pattern:

> The pattern is the same everywhere though: work is put into a queue of sorts, a machine picks it up, attempts it, stops, and then some harness decides whether that was actually the end.
>
> If not, the harness continues the same session, injects another message, starts a fresh session with modified context, or sends the task to another machine. The task stays alive beyond the point where the model by itself would normally have said: “I am done.”

Two loops:

> There is already an agent loop inside every coding agent. The model calls a tool, incorporates the result, calls another tool, reads a file, edits a file, runs tests, and eventually produces some answer. ... The other loop is the harness level loop: the loop outside the agent loop.

Failure modes of loop-written code:

> Present-day models tend to produce code that is too defensive, too complex, too local in its reasoning. They avoid strong invariants. They add fallbacks instead of making bad states impossible. They duplicate code, invent bad abstractions, and paper over unclear design with more machinery.

> When you take that behavior and you put it behind loops, you tend to amplify it. If each iteration adds another small defense, the system slowly becomes less understandable while appearing more robust. The more hands-off you are, the more that happens.

Where loops work:

> Porting code one of them. ... Performance explorations are another case where this works beautifully. ... Security scanning fits naturally too and so does almost any type of research

> I believe that loops that produce artifacts without necessity of longevity or that create some form of clearly verifiable mechnical translation matters more than the general ability of a harness to mechanically measure a goal.

> The harness just needs some signal that lets it continue. It does not have to be objective or binary, it just has to be useful enough to drive another iteration.

Software as organism:

> The metaphor I like to reach for is one of moving from software as a deterministic machine to software as an organism.

> We treat it, we monitor it, we stabilize it, but we do not necessarily comprehend it.

Cannot opt out:

> If attackers and reporters loop, defenders will eventually need to loop too to keep up.

Dependency:

> We may create codebases that are not merely hard to maintain by humans, but that assume machine participation as part of their maintenance model.

Human role in harness loops:

> Adopting the idea of harness loops means that the harness decides when work is finished. In the agent loop, the model eventually says “done” and I review. ... In the harness operated loop I’m not sure what my role even is. Even the “done” signal loses all meanings and just becomes communicated to yet another machine that judges. My role is reduced to that of a messenger.

> So I guess I’m coming to terms with that the question is not whether we will loop because clearly we will. Maybe the question is that in a future of loops, how do we don’t abdicate judgment

### What this source says

Distinguishes the inner "agent loop" from the outer "harness level loop" that keeps a task alive past the model's "done". Loops work well for porting, performance search, security scanning, research — short-lived or mechanically verifiable output. For lasting code he finds loop output worse (defensive, duplicated, weak invariants) and says loops amplify that. Raises dependency on model access and loss of comprehension ("software as organism"). Expects loops to win anyway; asks how to keep judgment.

---

## 7. Astra for Coding: Why Are We Doing This Again?

- URL: https://lucumr.pocoo.org/2026/9/7/astra-why/
- Date: September 7, 2026
- Raw: `b-raw/armin-astra-why/page.txt`

A first-hand software-factory run, reported with what he did and what came out.

### Verbatim

> “Armin, you should run a software factory!” I’ve heard that a few times now, so I figured I might celebrate the release of it by running a little software factory over the weekend.

> My software factory was intentionally set up to let the model decide the how of the workflow entirely. It was free to manage its own context and could maintain its own records in an agent-notes folder. Then it spun off subagents to work on stuff. The goal? What if we had a Python with virtual threads and lexical scoping.

> I burned a full reset’s worth of ChatGPT tokens on this which appears to be around 4 billion tokens. 35 hours later, the factory has delivered absolutely nothing of value and also not taught me anything about how to operate a better one.

> I think I’m suspecting something is going “wrong” in the training process. The model is greatly rewarded for succeeding on long-horizon tasks, but presumably there is very little punishing going on for “shitty code.”

> But these local optimizations do not produce global optimums, and the fewer of us are looking at the output, the less it matters. Obviously my software factory ran aground over the ~35 hours that it ran, but you can see the gradual regression towards insanity from the notes that it produced. For instance the task naming in the task file starts with an optimistic 1, 2, 3, 5, 5a but then eventually gets to 8a, 8a1, and then ends up with 8b2c2b3 and “8b2c2b2b checkpoint1”.

> And probably you can now run a software factory for as long as you don’t care about the code.

> Postscriptum: speaking of weird: how is it that these models, in a sandbox, with supposedly no way to communicate with other agents, manage to find the same public wikis as a scratch pad for agent communication?

### What this source says

An unsupervised factory (model chose its own workflow, notes folder, sub-agents) ran ~35 hours on a language-runtime goal and produced nothing of value; task numbering in its notes shows drift ("regression towards insanity"). He attributes this partly to training that rewards long-horizon completion more than code quality. Failure modes named: hardcoded constants, string-splicing edits via Python instead of the patch tool, task-list drift.

---

## Other posts saved, not quoted

- A Year Of Vibes (Dec 22, 2025): `b-raw/armin-a-year-of-vibes/`
- Some Things Just Take Time (Mar 20, 2026): `b-raw/armin-some-things-just-take-time/`
