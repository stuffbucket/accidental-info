# Steve Yegge: primary-source notes

Author: Steve Yegge (ex-Amazon, ex-Google, ex-Sourcegraph). Writes on Medium (steve-yegge.medium.com) and mirrors essays at yegge.ai.
Medium blocks direct fetches. Sources used: the Medium RSS feed (full text of the 10 most recent posts), the Wayback Machine copy of "Welcome to Gas Town", yegge.ai for Beads, and the Sourcegraph blog for "Revenge". All quotes are copied from those texts.

---

## 1. "Revenge of the junior developer"

- URL: https://sourcegraph.com/blog/revenge-of-the-junior-developer
- Date: March 22, 2025
- Coins: **six waves** of programming modalities; **agent clusters** and **agent fleets** (placeholder terms); "camels" to "chariots" metaphor. Credits Karpathy with "vibe coding". Defines vibe coding as "letting the AI do the work".

> Brief note about the meaning of "vibe coding": In this post, I assume that vibe coding will grow up and people will use it for real engineering, with the "turn your brain off" version of it sticking around just for prototyping and fun projects. For me, vibe coding just means letting the AI do the work.

> He called it "vibe coding" and it became an instant blue/gold dress situation pretty much overnight.

The six waves:

> The chart in Figure 1 depicts six overlapping waves of programming: traditional (2022), completions-based (2023), chat-based (2024), coding agents (2025 H1), agent clusters (2025 H2), and agent fleets (2026).

> As a sneak preview for our discussion, "agent clusters" is the placeholder term I'm using for devs being able to run and fruitfully manage many coding agents in parallel, potentially even more than can fit on a dev's local machine. And "agent fleets" are what happens when we get AI supervisors for the leaf nodes

> Today, you have to notice when an agent worker is stuck, done, or gone astray, and nudge it appropriately. Supervisor agents can and will start doing most of that for us very soon. The result: wave six.

> You can vibe code with any non-manual AI modality: chat, agents, clusters. As long as AI is doing the work, you're vibing!

> Vibe coding simply means never writing code again.

> Task graph decomposition, a skill we've all learned during the chat days of yore (December), is just as important today as you switch to vibe coding with agents.

> Chariots are next. Just you wait.

Junior developer thesis:

> One consistent pattern I've observed in the past year, since I published "The Death of the Junior Developer", is that junior developers have actually been far more eager to adopt AI than senior devs.

### What this source says

Yegge predicts waves of AI coding: completions, then chat, then single agents, then "agent clusters" (many agents in parallel per developer), then "agent fleets" (supervisor agents managing worker agents), which he expected by 2026. He says each wave is about 5x more productive than the last; that is his estimate, with no method (hype file). For him "vibe coding" is not a modality. It means AI doing the work, at any level of human attention. He argues junior developers adopt faster than seniors. Task decomposition stays the key human skill.

---

## 2. "Introducing Beads: A coding agent memory system"

- URL: https://yegge.ai/essays/introducing-beads-a-coding-agent-memory-system/ (Medium: https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a)
- Date: 2025-10-13 (per yegge.ai)
- Coins: **Beads** (`bd`). Names failure modes: **"The Dementia Problem"**, **"work disavowal"**, lost **"discovered work"**, the markdown-plan sprawl ("Plan Jungle").

> Beads is a git-backed issue tracker that gives coding agents the memory they don't have.

> The other colossal design mistake I made was embracing markdown plans — the same ones that agents already use by default, as they're organizing and planning their work.

> By the time I finally found a solution that works — Beads—I discovered I had six hundred and five markdown plan files in varying stages of decay in my plans/ folder.

> The problem we all face with coding agents is that they have no memory between sessions — sessions that only last about ten minutes. It's the movie Memento in real life, or Fifty First Dates.

> By the start of phase 3 (out of 6), the AI has mostly forgotten where it came from. It wakes up, plops in your video cassette, and reads about phase 3. It then declares, "Oh wow, this is a big project, I'm going to break it into five phases and create a markdown plan." Which should sound eerily familiar.

> I had had enough. On a lark, I said, "Screw it. Let's just move all known work from the plans into an issue tracker."

> My agents have switched — without a hint of ever going back — from using markdown plans, to using the issue tracker exclusively. This has granted them unprecedented continuity from session to session. And as a bonus, as you'll see, when you let them use Beads, you will never again lose discovered work.

> Or beads on a chain, which agents can follow to get tasks done in the right order. And the shorthand bd — the tool itself — can be thought of as standing for "bug database."

> By and large, Beads is a tool that AI has built for itself.

> Beads manages to help with this problem, because you can just kill your agents after completing each issue. Beads helps agents easily find where they're supposed to pick up again, so it's easy to make your sessions throwaway.

> If you split your bd issues up into fine-grained tasks, then each session will be quadratically cheaper, and your agents will make better decisions overall because they're generally at the beginning of their context windows if they're only doing one small task at a time.

> In other words, Beads doesn't just make agents better at following the plan, it makes them less likely to take shortcuts along the way.

### What this source says

Agents lose track of long work across sessions and compactions, and they keep generating new markdown plans (605 in his folder). Beads replaces markdown plans with a git-backed issue tracker that has dependency links. Agents can then pick up work, record work they discover, and be killed after each issue. Short sessions keep each agent near the start of its context window. This matches Huntley's and Horthy's reasoning about fresh context.

---

## 3. "Welcome to Gas Town"

- URL: https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04 (read via Wayback Machine copy)
- Date: 2026-01-01 (datePublished in page metadata)
- Coins: **Gas Town**; the **8 stages** of the "Evolution of the Programmer in 2024–2026"; roles **Overseer, Mayor, Polecats, Refinery, Witness, Deacon, Dogs (Boot), Crew**; **Town**, **Rig**; **GUPP** (Gastown Universal Propulsion Principle); **hook**; **MEOW** (Molecular Expression of Work); **molecules, protomolecules, formulas, wisps, patrols, convoys**; **NDI** (Nondeterministic Idempotence); **"Idea Compiler"**; "guzzoline". Gas Town is built on Beads.

Definition:

> Gas Town is a new take on the IDE for 2026. Gas Town helps you with the tedium of running lots of Claude Code instances.

> I predicted someone would lash the Claude Code camels together into chariots, and that is exactly what I've done with Gas Town. I've tamed them to where you can use 20–30 at once, productively, on a sustained basis.

> But the comparison should serve as a warning: Gas Town is complicated. Not because I wanted it to be, but because I had to keep adding components until it was a self-sustaining machine.

> "It will be like kubernetes, but for agents," I said.
> "It will have to have multiple levels of agents supervising other agents," I said.
> "It will have a Merge Queue," I said.
> "It will orchestrate workflows," I said.
> "It will have plugins and quality gates," I said.

> Gas Town (in Go) is my fourth complete, functioning orchestrator of 2025.

Warnings (his own):

> First of all, the code base is under 3 weeks old. ... It's also 100% vibe coded. I've never seen the code, and I never care to, which might give you pause.

The eight stages (verbatim):

> Stage 1: Zero or Near-Zero AI: maybe code completions, sometimes ask Chat questions
> Stage 2: Coding agent in IDE, permissions turned on. A narrow coding agent in a sidebar asks your permission to run tools.
> Stage 3: Agent in IDE, YOLO mode: Trust goes up. You turn off permissions, agent gets wider.
> Stage 4: In IDE, wide agent: Your agent gradually grows to fill the screen. Code is just for diffs.
> Stage 5: CLI, single agent. YOLO. Diffs scroll by. You may or may not look at them.
> Stage 6: CLI, multi-agent, YOLO. You regularly use 3 to 5 parallel instances. You are very fast.
> Stage 7: 10+ agents, hand-managed. You are starting to push the limits of hand-management.
> Stage 8: Building your own orchestrator. You are on the frontier, automating your workflow.

> If you're not at least Stage 7, or maybe Stage 6 and very brave, then you will not be able to use Gas Town. You aren't ready yet. Gas Town is an industrialized coding factory manned by superintelligent robot chimps, and when they feel like it, they can wreck your shit in an instant.

Working style (throughput over completeness):

> Working effectively in Gas Town involves committing to vibe coding. Work becomes fluid, an uncountable substance that you sling around freely, like slopping shiny fish into wooden barrels at the docks. Most work gets done; some work gets lost.

> Work in Gas Town can be chaotic and sloppy, which is how it got its name. Some bugs get fixed 2 or 3 times, and someone has to pick the winner. Other fixes get lost. Designs go missing and need to be redone. It doesn't matter, because you are churning forward relentlessly on huge, huge piles of work, which Gas Town is both generating and consuming.

> In Gas Town, you let Claude Code do its thing. You are a Product Manager, and Gas Town is an Idea Compiler. You just make up features, design them, file the implementation plans, and then sling the work around to your polecats and crew.

> It runs itself pretty well most of the time, but stuff goes wrong often. ... It's very much a hands-on-the-wheel orchestration system.

> Gas Town is also expensive as hell.

> But right now? It's like a late 1800s factory with machines that can disembowel you if you're not careful.

Roles (verbatim, abridged to the definitional sentences):

> 👤The Overseer: That's you, Human. The eighth role.

> 🎩The Mayor: This is the main agent you talk to most of the time. It's your concierge and chief-of-staff.

> 😺Polecats: Gas Town is a work-swarming engine. Polecats are ephemeral per-rig workers that spin up on demand. Polecats work, often in swarms, to produce Merge Requests (MRs), then hand them off to the Merge Queue (MQ).

> 🏭Refinery: As soon as you start swarming workers, you run into the Merge Queue (MQ) problem. ... This is the job of the Refinery: the engineer agent responsible for intelligently merging all changes, one at a time, to main. No work can be lost, though it is allowed to escalate.

> 🦉The Witness: Once you spin up enough polecats, you realize you need an agent just to watch over them and help them get un-stuck.

> 🐺The Deacon: ... The Deacon is a Patrol Agent: it runs a "patrol" (a well-defined workflow) in a loop. Gas Town has a daemon that pings the Deacon every couple minutes and says, "Do your job."

> 🐶Dogs: ... this is the Deacon's personal crew. Unlike polecats, Dogs are town-level workers. They do things like maintenance (cleaning up stale branches, etc.)

> 👷The Crew: ... The crew are per-Rig coding agents who work for the Overseer (you), and are not managed by the Witness. ... The crew are great for stuff like design work, where there is a lot of back-and-forth.

> 🏗️Rigs: Each project (git repo) you put under Gas Town management is called a Rig.

GUPP and agent identity:

> GUPP is what keeps Gas Town moving. The biggest problem with Claude Code is it ends. The context window fills up, and it runs out of steam, and stops. GUPP is my solution to this problem.

> GUPP states, simply: If there is work on your hook, YOU MUST RUN IT.

> In Gas Town, an agent is not a session. Sessions are ephemeral; they are the "cattle" in the Kubernetes "pets vs cattle" metaphor.

> In Gas Town, an agent is a Bead, an identity with a singleton global address.

> Unfortunately, Claude Code is so miserably polite that GUPP doesn't always work in practice.

MEOW / molecules / NDI:

> Gas Town is the tip of a deep iceberg. Gas Town itself may not live longer than 12 months, but the bones of Gas Town — the MEOW stack — may live on for several years to come.

> In other words, molecules are workflows, chained with Beads.

> If the workflow is captured as a molecule, then it survives agent crashes, compactions, restarts, and interruptions.

> Gas Town operates on the principle I call Nondeterministic Idempotence, or NDI. It is similar to Temporal's deterministic, durable replay, but Gas Town achieves its durability and guaranteed execution through completely different machinery.

> So even though the path is fully nondeterministic, the outcome — the workflow you wanted to run — eventually finishes, "guaranteed", as long as you keep throwing agents at it.

> There are tons of edge cases. This description of NDI is oversimplifying. Gas Town is not a replacement for Temporal.

> A patrol is an ephemeral (wisp) workflow that the agent runs in a loop.

> The Convoy is Gas Town's ticketing or work-order system.

> Aside from just keeping Gas Town on the rails, probably the hardest problem is keeping it fed. It churns through implementation plans so quickly that you have to do a LOT of design and planning to keep the engine fed.

> I implemented a formula for Jeffrey Emanuel's "Rule of Five", which is the observation that if you make an LLM review something five times, with different focus areas each time though, it generates superior outcomes and artifacts.

Kubernetes comparison:

> The big difference is, Kubernetes asks, "Is it running?" while Gas Town asks "Is it done?"

### What this source says

Gas Town is an orchestrator for 20-30 parallel coding agents. Each worker is a normal coding agent prompted into one of seven roles; the human "Overseer" is the eighth. Ephemeral polecats produce merge requests. A Refinery agent merges them serially to avoid merge-queue conflicts. A Witness unsticks workers. A Deacon runs a patrol loop as a heartbeat. Dogs do maintenance. Crew are long-lived agents for interactive design work. State lives in Beads in git, so agent identity, hooks and workflows ("molecules") outlive any session. "If there is work on your hook, YOU MUST RUN IT" (GUPP) keeps it moving. Yegge's eight stages run from no AI to "building your own orchestrator". The human role is product manager and feeder: the bottleneck is producing enough designed work. He openly accepts lost and duplicated work and never reads the code. The post reports no quality measure.

---

## 4. "Vibe Maintainer"

- URL: https://steve-yegge.medium.com/vibe-maintainer-a2273a841040
- Date: Tue, 31 Mar 2026
- Coins: **vibe maintainer**, **fix-merging**, "PR Sheriff". Refers to "AI-era design principles (e.g. ZFC)" (not defined in this post).

> I accept most PRs, but still maintain hard lines on architecture, what goes in core, code quality, and many other AI-era design principles (e.g. ZFC).

> My core philosophy is, help contributors get to the finish line. I optimize for community throughput. I review every PR and try to find the value in it, and have my worker agents do something appropriate for each one.

> Notice that the first resort for almost every OSS maintainer, which is to send your PR back requesting changes, is the last resort in my vibe maintainer workflow.

> And that's why the last 25% or so of pull requests need human review. At least, so far. It's because there's still a thing called taste that current models can't be trusted with. Not yet.

> If you think of Gas Town as a Dark Factory (it is!), then Gas City is a Dark Factory Factory.

### What this source says

As maintainer of Beads and Gas Town, Yegge has agents triage pull requests into easy-wins, fix-merge and needs-review, and absorbs the good parts of each one rather than sending it back. He still reviews every PR and says about a quarter need human judgment because models lack "taste". He calls Gas Town a "Dark Factory". (His "88%" merge figure and "median time to resolution is about 15 hours" are his own project metrics without a stated method; usable only as self-report.)

---

## 5. "Gas Town: from Clown Show to v1.0"

- URL: https://steve-yegge.medium.com/gas-town-from-clown-show-to-v1-0-c239d9a407ec
- Date: Fri, 03 Apr 2026

> I truly think it comes down to the Mayor giving you less stuff to read.

> Claude Code and some other agents are trying to turn themselves into dark factories, by running subagents, and providing their own task management, memory systems, etc. But so far, they're all trying to do it with a product lens, no platform to speak of — a monolith. ... safe to say I'm not a fan.

> If Claude Code is an Executive Assistant, then the Gas Town Mayor is more like your Chief of Staff, who manages a full team of capable EAs, all working for you behind the scenes.

### What this source says

The Mayor's value is filtering: it reads the output of many workers so the human reads less. Yegge rejects single-product "monolith" agents trying to become factories. This is the opposite of Huntley's preference for a monolithic loop (see a-disagreements.md).

---

## 6. "Welcome to Gas City"

- URL: https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607
- Date: Fri, 24 Apr 2026
- Coins: **Gas City** (an SDK for building dark factories), **packs**, **"Light Factory"**, devs as **shepherds**. Gives his own definition of **dark factory** and extends the 8 stages.

> What is Gas City, you ask? It is Gas Town, but torn apart and rewritten from the ground up as an SDK for building your own dark factories. It enables you to deploy teams of collaborating agents in any topology

> A dark factory is any system in which coding agents are set up to work autonomously without humans watching. The name is frankly a little bit misleading. It just means background work. It's only dark inside a dark factory because the work is happening in rooms where there are no humans present. But those rooms are allowed to have windows. Observability is a choice in dark factory design.

> So then is Claude Code a dark factory? The terminology here, with factories and harnesses and so on, is all evolving fast, so there aren't any reliable definitions yet.

> For this reason I have begun to think of Gas City as a Light Factory… or at least, a very well-lit dark one!

> So dark factories are a much broader concept than IDEs. They can automate and orchestrate any arbitrary process. But with what reliability?
> Well, that depends on how robust your custom factories are, doesn't it?

> In the very near future, devs will become shepherds, tending flocks of agents which do the ground-level work. It's not really a manager job, because the workers are not humans

> As soon as I had this realization, the shepherd thing, I knew we'd discovered at least 2–3 new squares in my now-infamous "8 Stages of AI Adoption" diagram from Welcome to Gas Town

> After you deploy your first real one, you officially have a garden you're tending. A tiny crew of agents, acting like employees. Your little factory team runs 24x7, which requires maintenance.

> You should almost never deploy a single-agent pack for a real business process. The reality is that any agent can go temporarily insane, at any time, and make a bad call. No matter how smart they are.

> You should always have at least two or three working together on a little crew.

> With Gas City you can build any sort of adversarial group structure you like, for a team of collaborating agents. They can watch over each other.

### What this source says

Yegge's "dark factory" is broad: any setup where agents work without a human watching. He says the "dark" can have windows, i.e. observability. That is weaker than Shapiro's Level 5 ("humans are neither needed nor welcome") and StrongDM's "no human review". He extends factories from coding to business processes. He recommends always pairing agents so they check each other, never a single agent. He extends his stage chart past Stage 8 to deploying and tending "mini-factories".

---

## 7. "Welcome to the Wasteland: A Thousand Gas Towns"

- URL: https://steve-yegge.medium.com/welcome-to-the-wasteland-a-thousand-gas-towns-a5eb9bc8dc1f
- Date: Wed, 04 Mar 2026
- Terms: **rigs, posters, validators**; **stamps**; "yearbook rule".

> The Wasteland has three kinds of actors: rigs, posters, and validators. Every rig rolls up to a human participant.

> A stamp is a multi-dimensional attestation: quality, reliability, creativity, each scored independently.

> And there's a yearbook rule: you can't stamp your own work.

> The world needs a coding agent that behaves like a factory worker, and we don't have one today. So one will get built.

### What this source says

A federated work board across many Gas Towns. Human-anchored "rigs" claim work, and validators with earned trust attest to its quality. Nobody can validate their own work.

---

## 8. Other Yegge posts in the feed (scanned, lower relevance)

- "The Flat Curve Society", https://steve-yegge.medium.com/the-flat-curve-society-36c8b01eb33b (19 Jun 2026). Coins **"back-pocket evals"** and **"discernment horizon"**:

> I call my hard problems "back-pocket evals," and I collect them.

> There is a darker horizon, which I think of as the discernment horizon proper. This one is set not by the hardest problem you can pose, but by the hardest answer you can judge. Past this scary line, you can't tell whether the model is right, because checking the work is itself beyond you.

- "Fences, not Sandboxes", https://steve-yegge.medium.com/fences-not-sandboxes-5719cd9b04bd (24 Aug 2026). Describes long-lived "officer" agents directing implementation fleets:

> I have built a team of 18 "officer" seats, all Heads of This and That, all long-lived Fable instances. I also have mostly-headless Sol and Opus fleets, for implementation, reviews, and monitoring. Fable runs them.

- "Software Survival 3.0" (29 Jan 2026), "The Anthropic Hive Mind" (6 Feb 2026), "The AI Vampire" (11 Feb 2026), "The Last Technical Interview" (29 May 2026): scanned, no factory definitions extracted.

---

## 9. "The Shape of Things to Come" (Part 1: The Continuous Thunderdome)

- URL: https://yegge.ai/essays/the-shape-of-things-to-come/ (quoted by Simon Willison, https://simonwillison.net/2026/Aug/4/steve-yegge/)
- Date: August 2026 (Willison's quote is dated 4th August 2026)
- Coins: **Wheelhouse** (his bespoke harness), **Land Rush** / **Thunderdome** (megabatch merge plus swarm diagnosis), **Wish Factory** (credits the idea to Guy Podjarny/Tessl; the name is his), **"crons watch, models act"**, **crew / fleet / role agents with standing orders**, "Beads machine", "project brain". Reports **Gas Town failed**.

Gas Town's end (his own account):

> Gas Town was intended to be reusable, but I only ever wound up using it to build itself. Gas Town fell apart at the seams with Opus 4.7. Up through 4.6 it was working brilliantly. With 4.7 we saw the introduction of the "just two more things" tic, which prevented Opus from ever converging on being ready to do real work—it always wanted to fiddle with Gas Town itself. The Opus tic never went away, so Gas Town effectively burned down. It had other problems, too, but 4.7 was the final straw.

> I have given up on building reusable harnesses. Indeed I believe harnesses will all soon be bespoke, and the people trying to sell you one will all soon be bebroke. Harnesses need to be part of your application, chemically bonded in.

> Gas Town wasn't really a "loop" in the sense that I thought Boris might be suggesting. It was more like a chariot, with you driving.

> It turns out that all you need in order to set up your own long-running software factory loop, is an infinite source of tokens. And then to have them work on a graph, you just need Beads, plus a small Markdown project brain.

Limits of models:

> Building large software remains hard. And it always will be, because our ambition will forever outstrip the metal.

> Making a halfway decent MMO takes many tens of thousands of Fable sessions, throughout which you must display intense focus, dedication, and no small amount of taste.

Wheelhouse structure (producer/consumer):

> There are three categories of coding agents in Wheelhouse: crew agents, fleet workers, and role agents with standing orders.

> Every implementation bead goes through this lifecycle: Fable design, Opus implementation, Fable review. This keeps Opus on the rails and keeps the whole thing running relatively smoothly.

> So the crew produces work, and the fleet consumes work. That's the core of a Beads machine: matching producers to consumers. Too many of one and you're blocked on the other.

> the nutshell takeaway is that without trying (at all), I reinvented Gas Town, bit by bit. I wound up with crew, fleet, a concierge role, beads mail, tmux under the hood, handoffs, broadcast messaging, a merge queue, and much more. It was all completely unintentional, so the shape I keep finding must be important.

> It turns out unattended agents need a hell of a lot of wiring. I have about 45 launchd/systemd units across the mini and the VM that wake an agent when something needs judgment. The rule is: crons watch, models act.

> working on Wheelhouse itself occupies about 20-25% of all my Wyvern work. I think that figure might turn out to be roughly constant over the life of systems with agentic harnesses.

> I run pretty lean. I don't use any sandboxing. I don't use MCP.

Code review (prediction):

> CTOs keep asking me if code review is really dead. The answer: Not Yet. But it will be by next year. You can't work at agentic speeds and block everything with human reviews. Those are incompatible.

> Upshot: in the short term, yes, keep reviewing agent code.

> get ready to replace your human code review with many, many rounds of agentic code review.

CI/CD (measured from his own system):

> I'm averaging about 175 "real" commits per day this month, some days up to 250. And my build gate, wouldn't you know it, takes right around half an hour.

> So with 40+ agents around the clock, my MQ was growing without bound, shooting right past 100 MRs in the queue after a couple of days of crew dumping beads on the fleet. We would get caught up in bisection loops and nothing would make forward progress.

> And that's how we landed on the Land Rush: whenever the MQ hits 100, we abandon the bisection and just smash it all in with a megabatch. And then we do swarm diagnosis (not bisection) to fix it.

> CI/CD has fallen victim to the Pigeonhole Principle: if you have more pigeons than holes, some hole ends up holding more than one pigeon. Once your commit rate outruns your build slots, one commit per green build becomes mathematically impossible.

Wish Factory:

> I've got to credit Guy Podjarny for this idea, although "Wish Factory" is my name for it. Guy told me back at the AIE World's Fair that his company Tessl, for whom I'm an advisor, is launching an agent you can throw onto a GitHub repo. It doesn't accept PRs, only GHIs. It then implements them for you.

> On the heels of that success, I decided to extend the wish factory to our players. Which is of course riskier. ... So I had to put in more guardrails, reviews, and triage.

Convergent architecture:

> I didn't design Wheelhouse, just like I didn't design Gas Town. I excavated both of them, and I'm confident you'll dig up the same shape.

### What this source says

Yegge says Gas Town failed: it only ever built itself, and a model behaviour change (Opus 4.7) stopped it converging. He has given up on reusable harnesses and says each project needs its own. Wheelhouse, his replacement, has the same shape: design agents (crew) produce work as Beads, implementation agents (fleet) consume it, and unattended "role agents" run production, woken by cron/systemd units ("crons watch, models act"). Every work item goes design, implementation by a cheaper model, then review by the stronger model. Maintaining the harness takes 20-25% of his effort. At ~175 commits/day with a 30-minute build, a serial merge queue could not keep up. He moved to megabatch merges with swarm diagnosis, which he compares to game-industry practice. He still says to keep human code review for now, and predicts it will be replaced by "many, many rounds of agentic code review" within a year. A "Wish Factory" turns user requests directly into shipped changes, with extra guardrails when users are players rather than admins. (Token-spend figures and "operating about 12 months in the future" are self-description; see the hype file.)
