# Dex Horthy / HumanLayer: primary-source notes

Author: Dex (Dexter) Horthy, founder of HumanLayer. Some HumanLayer posts are by his cofounder Kyle Mistele; those are marked.
Talk quotes come from auto-generated YouTube transcripts (via usetranscribe.io). They may contain transcription errors and should be checked against the video before publishing. Written sources are quoted exactly.

---

## 1. 12-Factor Agents

- URL: https://github.com/humanlayer/12-factor-agents (README; blog copy at https://www.humanlayer.dev/blog/12-factor-agents)
- Date: April 2025 (blog dated April 3, 2025; HumanLayer's resources page lists the GitHub essay as Apr 15, 2025). Talk at AI Engineer World's Fair, June 2025: https://www.youtube.com/watch?v=8kMaTybvDUw
- Scope: building LLM *applications*, not coding agents. It is the source of HumanLayer's "context engineering" vocabulary.

The 12 factors (names exactly as listed):

> - Factor 1: Natural Language to Tool Calls
> - Factor 2: Own your prompts
> - Factor 3: Own your context window
> - Factor 4: Tools are just structured outputs
> - Factor 5: Unify execution state and business state
> - Factor 6: Launch/Pause/Resume with simple APIs
> - Factor 7: Contact humans with tool calls
> - Factor 8: Own your control flow
> - Factor 9: Compact Errors into Context Window
> - Factor 10: Small, Focused Agents
> - Factor 11: Trigger from anywhere, meet users where they are
> - Factor 12: Make your agent a stateless reducer

> **I've been surprised to find** that most of the products out there billing themselves as "AI Agents" are not all that agentic. A lot of them are mostly deterministic code, with LLM steps sprinkled in at just the right points to make the experience truly magical.

> Agents, at least the good ones, don't follow the ["here's your prompt, here's a bag of tools, loop until you hit the goal"](https://www.anthropic.com/engineering/building-effective-agents#agents) pattern. Rather, they are comprised of mostly just software.

Agent loop as defined in the README:

> Let's dive one step deeper - with agents you've got this loop consisting of 3 steps:
>
> 1. LLM determines the next step in the workflow, outputting structured json ("tool calling")
> 2. Deterministic code executes the tool call
> 3. The result is appended to the context window
> 4. Repeat until the next step is determined to be "done"

The failure journey he describes:

> 4. Get to 70-80% quality bar
> 5. Realize that 80% isn't good enough for most customer-facing features
> 6. Realize that getting past 80% requires reverse-engineering the framework, prompts, flow, etc.
> 7. Start over from scratch

Factor 3 (https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md):

> #### At any given point, your input to an LLM in an agent is "here's what's happened so far, what's the next step"

> Everything is context engineering. [LLMs are stateless functions](https://thedataexchange.media/baml-revolution-in-ai-engineering/) that turn inputs into outputs. To get the best outputs, you need to give them the best inputs.

### What this source says

Reliable LLM software is mostly ordinary deterministic code with model calls at chosen points. The builder should own the prompts, context window, control flow and state rather than handing them to a framework. HumanLayer later claims this document introduced the term "context engineering" (see section 6 and a-terms.md for the contested origin).

---

## 2. "Getting AI to Work in Complex Codebases" / Advanced Context Engineering for Coding Agents (ACE-FCA)

- URL: https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md (blog copy: https://www.humanlayer.dev/blog/advanced-context-engineering, dated August 29, 2025)
- Talk: Y Combinator, August 20, 2025 ("Advanced Context Engineering for Agents", https://hlyr.dev/ace)
- Coins: **frequent intentional compaction**, **intentional compaction**. Names the **research, plan, implement** workflow. Uses **mental alignment** (credits Blake Smith's framing of code review).

> We use a family of techniques I call "frequent intentional compaction" - deliberately structuring how you feed context to the AI throughout the development process.

> I am now fully convinced that AI for coding is not just for toys and prototypes, but rather a deeply technical engineering craft.

Origins credited: Sean Grove's "Specs are the new code" and Yegor Denisov-Blanch's Stanford study (both AI Engineer 2025).

> Sean proposes that in the AI future, the specs will become the real code.

> Our approach was to adopt something like sean's spec-driven development.
> It was uncomfortable at first. I had to learn to let go of reading every line of PR code. I still read the tests pretty carefully, but the specs became our source of truth for what was being built and why.

> The transformation took about 8 weeks. It was incredibly uncomfortable for everyone involved, not least of all for me.

### Intentional compaction

> You have probably done something I've come to call "intentional compaction". Whether you're on track or not, as your context starts to fill up, you probably want to pause your work and start over with a fresh context window.

> What eats up context?
> - Searching for files
> - Understanding code flow
> - Applying edits
> - Test/build logs
> - Huge JSON blobs from tools
>
> All of these can flood the context window. Compaction is simply distilling them into structured artifacts.

### Why context

> At any given point, a turn in an agent like claude code is a stateless function call. Context window in, next step out.

> That is, the contents of your context window are the ONLY lever you have to affect the quality of your output.

> You should optimize your context window for:
> 1. Correctness
> 2. Completeness
> 3. Size
> 4. Trajectory
>
> Put another way, the worst things that can happen to your context window, in order, are:
> 1. Incorrect Information
> 2. Missing Information
> 3. Too much Noise

On Ralph:

> Geoff describes ralph as a "hilariously dumb" solution to the context window problem. I'm not entirely sure that it is dumb.

### Subagents

> Subagents are not about playing house and anthropomorphizing roles. Subagents are about context control.

### Frequent intentional compaction / RPI

> Essentially, this means designing your ENTIRE WORKFLOW around context management, and keeping utilization in the 40%-60% range (depends on complexity of the problem ).

> **Research** Understand the codebase, the files relevant to the issue, and how information flows, and perhaps potential causes of a problem.

> **Plan** Outline the exact steps we'll take to fix the issue, and the files we'll need to edit and how, being super precise about the testing / verification steps in each phase.

> **Implement** Step through the plan, phase by phase. For complex work, I'll often compact the current status back into the original plan file after each implementation phase is verified.

### Human leverage (the error-amplification diagram)

> A bad line of code is… a bad line of code. But a bad line of a plan could lead to hundreds of bad lines of code. And a bad line of research, a misunderstanding of how the codebase works or where certain functionality is located, could land you with thousands of bad lines of code.

> So you want to focus human effort and attention on the HIGHEST LEVERAGE parts of the pipeline.

> When you review the research and the plans, you get more leverage than you do when you review the code.

> You have to engage with your task when you're doing this or it WILL NOT WORK.

> There's a certain type of person who is always looking for the one magic prompt that will solve all their problems. It doesn't exist.

### Mental alignment

> I prefer Blake Smith's framing in Code Review Essentials for Software Teams, where he says the most important part of code review is mental alignment - keeping members of the team on the page as to how the code is changing and why.

> A guaranteed side effect of everyone shipping way more code is that a much larger proportion of your codebase is going to be unfamiliar to any given engineer at any point in time.

> I can't read 2000 lines of golang daily. But I can read 200 lines of a well-written implementation plan.

### Reported results and limits

These are measured, with method described, so they count as primary:

> I decided to test our techniques on BAML, a 300k LOC Rust codebase ... Within an hour or so, I had a PR fixing a bug which was approved by the maintainer the next morning.

> the two of us spent 7 hours (3 hours on research/plans, 4 hours on implementation) and shipped 35k LOC to add cancellation and wasm support to BAML. The cancelation PR just got merged last week. The WASM one is still open

> A few weeks back, @blakesmith and I sat down for 7 hours and tried to remove hadoop dependencies from parquet java ... it did not go well. The tl;dr is that the research steps didn't go deep enough through the dependency tree

> I think the other learning here is that you probably need at least one person who is an expert in the codebase

> (oh, and yeah, our team of three is averaging about $12k on opus per month)

### What this source says

Agents fail in large brownfield codebases mostly because of what ends up in their context window. Horthy's answer is to split work into research, plan and implement. Each phase writes a compact markdown artifact. Context use is kept at 40-60%. Subagents do searching so the parent context stays clean. Human review moves to the research and the plan, where one error spreads into many lines of code. In this August 2025 version he had stopped reading every line of code and treated specs and plans as the source of truth. He reversed this in 2026 (sections 5 and 6). He reports one failure: the parquet-java Hadoop removal.

---

## 3. "No Vibes Allowed: Solving Hard Problems in Complex Codebases" (talk)

- URL: https://www.youtube.com/watch?v=rmvDxxNubIg (AI Engineer Code Summit, Nov 2025; HumanLayer lists YouTube date Dec 2, 2025). Transcript used: https://www.usetranscribe.io/yt/rmvDxxNubIg/ai-in-software (auto-transcribed)
- Coins: **the dumb zone** (and "smart zone"). Repeats **"do not outsource the thinking"** (credits Jake Nations of Netflix). Applies Fowler's **semantic diffusion** to "spec-driven development".

Dumb zone (auto-transcript):

> This leads to a concept I'm in a very very academic concept called the dumb zone. So, you have your context window. You have 168,000 tokens roughly. Some are reserved for output and compaction. This varies by model. but we'll use cloud code as an example here. Around the 40% line is where you're going to start to see some diminishing returns depending on your task. if you have too many MCPs in your coding agent, you are doing all your work in the dumb zone and you're never going to get good results.

Trajectory (auto-transcript):

> So, the next most likely conver token in this conversation is I better do something wrong so the human can yell at me again. So, mind be mindful of your trajectory.

Subagents (auto-transcript):

> if you have a front-end sub aent and a backend sub aent and a QA sub aent and a data data scientist sub aent please stop. Sub aents are not for anthropomorphizing roles. They are for controlling context.

Thinking (auto-transcript):

> do not outsource the thinking. AI cannot replace thinking. It can only amplify the thinking you have done or the lack of thinking you have done.

Spec-driven development and semantic diffusion (auto-transcript):

> So people ask, so Dex, this is specri development, right? No, specri development is broken. Not the idea, but the phrase. it's not well defined.

> there will never be a year of agents because of semantic diffusion.

> Martin Fowler said this in 2006. We come up with a good term with a good definition and then everybody gets excited and everybody starts meaning it to mean a hundred things to a 100 different people and it becomes useless. We had an agent is a person, an agent is a micros service. An agent is a chatbot. An agent is a workflow. And thank you, Simon. We're back to the beginning. An agent is just tools in a loop.

> people say Spectrum Dev is writing a better prompt, a product requirements document.

> Sometimes it's using like verifiable feedback loops and back pressure. Maybe it is treating the code like assembly like Sean taught us. but a lot of people is just using a bunch of markdown files while you're coding.

Research and planning as compression (auto-transcript):

> We are compressing truth. planning is leverage. Planning is about compression of intent.

> as your plans get longer, reliability goes up, readability goes down. There's a sweet spot for you and your team and your codebase.

> Watch out for tools that just spew out a bunch of markdown files just to make you feel good.

Harness engineering (auto-transcript):

> if you really want a hypy word, you can call this harness harness engineering, which is part of context engineering, and it's how you integrate with the integration points on codeex, claude, cursor, whatever.

Org rift (auto-transcript):

> staff engineers don't adopt AI because it doesn't make them that much faster. And then junior mid-levels engineers use a lot because it fills in skill gaps and then it also produces some slop. And then the senior engineers hate it more and more every week because they're cleaning up slop that was shipped by cursor the week before.

### What this source says

In the "dumb zone", performance drops as context fills. The guideline is beyond about 40% of usable context, depending on the task. RPI ("research, plan, implement") is a way to stay in the "smart zone". Horthy says not to treat the acronym as the point: "The important part is compaction and context engineering". "Spec-driven development" has lost a stable meaning. He calls harness engineering a part of context engineering.

---

## 4. "A Brief History of Ralph"

- URL: https://www.humanlayer.dev/blog/brief-history-of-ralph
- Date: January 6, 2026
- Credits **Ralph** to Huntley. Records Huntley's term **"overbaking"**.

> The Ralph Wiggum Technique, created by Geoff Huntley, went viral in the final weeks of 2025.

> Geoff talks about the "overbaking" phenomenon. If you leave ralph running too long, you end up with all sorts of bizarre emergent behavior, like post-quantum cryptography support.

> Ralph is also a great example of using declarative specifications over imperative instructions.

His own failed experiment:

> I wrote a half-pager on what I wanted, I had ralph write the specs from that, and I had another ralph build the implementation from the specs.
> I didn't really read the specs, and I didn't read the code.
> The output sucked. I went back to read the specs and they were way off base.

> Lessons:
> - if the specs are bad, the results will be meh
> - if you don't actually know your desired end state workflows and how you will test it, you probably won't know what to do when its done
> - if you are iterating/exploring, you probably don't want ralph in the first place

Refactor experiment (React standards doc, 6-hour loop, PR closed due to merge conflicts):

> Lesson - code is cheap - the easier alternative to "merge/rebase" is just to re-run the ralph loop on the fresh code with the same prompt and re-open a PR.

> Lesson - for existing codebases, make the change set manageable - we have since set up any ralph-ish desired state loops to once ONCE on a cron overnight, and merge small iterations over time. Waking up to one small refactor every morning is better than both a) waking up to none and b) waking up to 50.

On the Anthropic plugin:

> Beyond that, it misses the key point of ralph which is not "run forever" but in "carve off small bits of work into independent context windows".

> Perhaps the point is not the 5-line bash loop. Perhaps the point is dumb things can work surprisingly well, so what could we expect from a smart version of the thing?

> You should mess with this stuff. It's not exactly the future, but its an imporant slice through a bunch of important concepts that will make you a better Agentic Coder and a better AI Engineer.

### What this source says

A dated history (June 2025 to Jan 2026) of how Ralph spread. Horthy reads Ralph as context isolation, not as running forever. For existing codebases he runs a "desired state loop" once a night on a cron and merges small changes. He found bad specs gave bad output.

---

## 5. "Context-Efficient Backpressure for Coding Agents"

- URL: https://www.humanlayer.dev/blog/context-efficient-backpressure
- Date: December 9, 2025

> Here's a pattern we use constantly at HumanLayer: swallow all test/build/lint output and replace it with a single ✓ if the stage passes.

> You should try hard to stay in the ~75k token "smart zone" for claude models - every line of PASS src/utils/helper.test.ts is waste.

> Rather than letting the model decide what to truncate, we like to take control of output deterministically.

### What this source says

Back pressure costs context. Wrap test, build and lint commands so that a pass prints one line and only failures print their full output.

---

## 6. "Everything We Got Wrong About Research-Plan-Implement" (talk)

- URL: https://www.youtube.com/watch?v=YwZR6tc7qYg (MLOps.community; HumanLayer dates it Mar 24, 2026 / "talk 3/26"). Transcript: https://www.usetranscribe.io/yt/YwZR6tc7qYg (auto-transcribed)
- Coins: **QRSPI ("crispy")**. Uses **instruction budget** (credits cofounder Kyle). "Don't use prompts for control flow". **Horizontal plans** vs vertical. Reverses the "don't read the code" advice.

> One thing that's very relevant if you've been on Twitter today is uh I don't think it's okay to not read the code. Uh, I also don't think you should read really long plan files.

> We did get a couple things right. Uh, there is no magic prompt. Uh, do not outsource the thinking. You the engineer are an important part of this process, and seek leverage.

> And I found myself in workshops full of enterprise engineers saying, "Well, guys, guys, guys, guys, yeah, here's the software, but don't forget to say the magic words." It was um quite frankly, it was embarrassing.

> If you built a tool that requires hours and hours of training and reps to get like good results from, go fix the tool.

> one of the big takeaways I'll give you today is like you have an instruction budget.

> So, the new advice, uh don't read the plans. Please, read the code.

> I was wrong. I am humble enough to admit when I was wrong. Uh this is actually a very big conversation right now. Please, please read the code. We tried not reading the code for like 6 months. Uh it did not end well. We had to rip out and replace large parts of that system.

> this is why I'm a little mid on agent swarms and the whole gas town thing because you still need to be able to ensure quality, and like going 10 times faster doesn't matter if you're going to throw it all away in 6 months. So, shoot for 2 to 3x.

> Um basically we just hide the ticket from the context window that's doing research, and we do it deterministically.

> So we split it across several prompts. And so like before it was research, plan, implement, now it's questions, research, design, structure, plan, work tree, implement, PR.

> And before it was 85 instructions, now they're all less than 40

> The lesson is don't use prompts for control flow if you can use control flow for control flow.

> So if design is like, "Where are we going?" the structure outline is, "How do we get there?"

> So, if the plan is the implementation, the outline is the C header files.

> we cannot get models to stop writing horizontal plans.

> Uh that didn't make a very good acronym though, so we just picked the ones we liked and uh we're calling this crispy.

On StrongDM (Q&A):

> Um I do not endorse that. Let's put it that way.

Context (auto-transcript): the question was "Curious your thoughts on like the software factory. I think it's like strong DM that's saying the opposite, which is like never have a human read either side of it". Horthy's answer, just before the line above: "I used to cite Shawn Grose's talk where he was like it's just the spec. Just write the document that explains the desired behavior and you treat the code like it's assembly and you never read it anymore."

On the dumb zone after six months (Q&A):

> if you were have been using AI coding agents for 6 to 9 months and you use them for 60 hours a week like the dumb zone is not a useful concept to you. I will regularly go up to 60. I will regularly like aggressively keep it below 30.

> shoot to keep it under 40 and if you get up to 60 like think about wrapping it up

> we don't use the built-in compaction because everything that matters is going into static assets.

HumanLayer docs define the workflow in written form (https://docs.humanlayer.com/reference/skills-workflows):

> RPI            Questions, research, design discussion, structure outline, implementation, PR

### What this source says

RPI failed in rollout because it relied on users saying "magic words", and one large prompt (85 instructions) blew the model's instruction budget. QRSPI splits the work into smaller prompts joined by real control flow. Research runs blind to the ticket so it stays factual. The design discussion (~200 lines) and the structure outline (the "C header file") are the short, high-leverage documents humans review. Horthy now says to read the code, not long plans, and to aim for 2-3x speed rather than 10x.

---

## 7. "Why Software Factories Fail" (essay) / AI Engineer World's Fair 2026 keynote

- URL: https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md
- Date: Jul 22, 2026 (essay); keynote Jul 23, 2026 (https://www.youtube.com/watch?v=Ib5GBkD555M). Also published as X articles "The Harness Is Not Enough" / "Turning the Lights Back On" (Jul 24-25, 2026).
- Subtitle: "or: harness engineering is not enough"
- Terms: **lights-off software factory** (attributes coinage to Dan Shapiro), **agentic software factory**, **2022 software factory**, **loop engineering**, **horizontal plans / vertical slices (tracer bullets)**, **program design**. Traces "software factory" to the **1968 NATO conference**.

> [StrongDM wrote about their lights-off software factory](https://factory.strongdm.ai) where no human reads code and no human writes code.

> The narrative goes something like this:
> 1. You are the bottleneck.
> 2. The models are good enough.
> 3. Code is free.
> 4. Just ship more stuff.

> I've been building and studying software factories my whole career, but I only learned this recently: the term traces all the way back to a [NATO conference in 1968](http://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1968.PDF) -- the same one that gave us "software engineering."

2022 software factory (definition):

> - **People decide what to build** -- engineers, PMs, leadership driving the vision
> - **It goes in a tracker** -- Linear, Jira, whatever: a state machine of what needs to happen
> - **Someone grabs a ticket and builds it** -- probably does some manual/automated testing while they're at it
> - **Pull request** -- automated checks, a human reviews the code, maybe someone pulls it down to test
> - **Anything wrong? Loop back** to "someone builds the thing"
> - **Ship to prod** -- and it makes contact with users
> - **Add monitoring** -- there's an entire industry built around paging an engineer at 3am when something breaks
> - **Users complain** -- ask for things, find bugs, file feature requests → back to the team to add to the tracker

> And on and on. We haven't even hit AI yet, and there are already several loops in this picture.

Agentic software factory:

> The agentic factory looks mostly like swapping **"someone builds the thing" → "an agent builds the thing"** -- there's some stuff here like orchestration, a harness, a sandbox, a model, computer use, etc.

> - Building drops from hours or days to minutes or hours.
> - Review still takes hours or days. A human still has to read the code and test the change. So review is now the bottleneck.

> At which point the job is two questions: how much can you stuff into the queue, and how fast can you review and test what comes out?

Lights-off software factory:

> [Dan Shapiro coined this term](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/) and [Simon Willison wrote about StrongDM's implementation of it](https://simonwillison.net/2026/Feb/7/software-factory/) -- where we no longer read the code.

> So you drop it, and you put the effort somewhere else:
> - Invest in testing and letting the agent test its own work
> - Invest in sandboxes and orchestration
> - Invest in automated review
> - Invest in monitoring
> - Invest in rollout
> - Invest in collecting feedback signals from users

> I'm going to posit something potentially controversial: the lights off factory does not work.

What they tried (primary, with what they did):

> In July 2025 we went full lights-off. Just read the specs and the tickets, background agents for all the small/medium stuff, the whole thing.

> You find at least one issue gnarly enough that the agent can't solve it -- even with your most advanced prompting and workflows.

> By the ~third time in november, we decided it would be easier to rewrite from scratch, and my cofounder spent **two whole weeks** in VS Code (not even cursor) plumbing out all the patterns by hand.

Failure mode named:

> models have a shortcoming. They can't maintain and improve codebase quality over time -- not without a decent amount of human steering.

> When I say maintainability, I mean the specific thing where it becomes really, really hard to change one part of the codebase without breaking another part. This is [Martin Fowler's shotgun surgery](https://refactoring.guru/smells/shotgun-surgery).

> I hear the word **brownfield** a lot to talk about this split. Historically that meant some ten-year-old Java thing, but at the pace we can ship now, it feels like an agent-built codebase starts to struggle after maybe **three to six months**

> THERE ARE NO GOOD BENCHMARKS for a model's ability to maintain codebase quality

> How the model got to a correct answer doesn't matter. If the tests pass, we win, but there is **no penalty** for eroding codebase maintainability.

> Tests give you feedback in seconds, but the cost function of bad architecture is measured in weeks, months, maybe even years

> if a model could reliably tell good code from bad, it might have written the good version to begin with, but maintainability has no fast oracle, so we can't reward for it during RL

> Of course, more review agents and more tokens do help -- they raise the floor, catching the dumb stuff.
> But they don't move the ceiling, because the ceiling is whatever we managed to teach the model in RL, and good design is the thing we still don't know how to teach it.

Turning the lights back on (four phases):

> - Product Requirements
> - System Architecture
> - Program Design
> - Vertical Slices

> If you wanna save time during review, you pick the person who would review the PR, and run through the product/tech specs with them before you get to the coding part

> After architecture we do this thing that I think is criminally underemphasized in agentic coding: **program design**.

> Models love what I call "horizontal plans" - doing things in stack-order

> - ~40% of tasks get oneshot or oneshot w/ 1-2 rounds of light feedback

> You don't have too many PRs. You have too many bad PRs.

> It is possible you are too busy trying to move 10-100x faster and trying to convince yourself code quality doesn't matter any more, when you could embrace the constraints and move 2-3x faster, safely.

> 1. Learn the constraints well, develop intuition by working with models a lot
> 2. Optimize systems within the arena of these constraints
> 3. Seek leverage
> 4. Read the dang code

Footnote on who discovered the loop:

> The loop, as an AI technique, was more or less discovered by an [alleged goat farmer](https://ghuntley.com/ralph/) on a remote island off the coast of Australia.

### What this source says

A "software factory" is old: the term goes back to 1968, and a 2022 team with a tracker, PRs, monitoring and user feedback already ran several loops. The agentic factory replaces the builder with an agent, which makes review the bottleneck. The "lights-off" factory removes human review and invests in tests, sandboxes, automated review, monitoring and rollout instead. Horthy says this does not work. HumanLayer ran it from July 2025, hit problems the agent could not fix in code nobody had read, and by November rewrote by hand. His cause is that RL rewards passing tests and never penalises damage to maintainability, and there is no fast oracle for maintainability. Harness engineering and review agents raise the floor but not the ceiling. His fix is to put human judgment back in front of the work: product review, system architecture, program design (types, signatures, call-stack trees, file-tree diffs), then vertical slices reviewed as they land. He aims for 2-3x speed. (Revenue figures for Claude Code and the Faros AI percentages are reported second-hand. Horthy calls the Faros report "more of a correlation signal than a verifiable smoking gun". Do not cite them as findings.)

---

## 8. "Skill Issue: Harness Engineering for Coding Agents" (by Kyle Mistele, HumanLayer)

- URL: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents
- Date: March 12, 2026
- Records coinage claims for **harness engineering** (Viv, i.e. Vivek Trivedy) and **context engineering** (Dex, 12-factor agents). Quotes Mitchell Hashimoto's definition.

> These are all technically separate concepts, but they are all part of the coding agent's configuration surface. We call this the coding agent's harness, and we think of it as the agent's runtime, or as its peripherals: what does the model use to interact with its environment?

> Harness engineering, coined by Viv, describes the practice of leveraging these configuration points to customize and improve your coding agent's output quality and reliability.

> As Mitchell Hashimoto put it, harness engineering
> > [...] is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again.

> We view harness engineering as a subset of context engineering. Coined by my cofounder Dex in 12-factor agents, context engineering is a superset of "prompt engineering" and a variety of other techniques for systematically improving AI agents' reliability.

> OpenAI recently wrote a blog post on the topic as well. ... it seems to indicate that they view harness engineering as configuring everything outside of the agent's runtime. It's more focused on back-pressure and verification mechanisms.

> Sub-agents are a popular but often misunderstood harness configuration point. We tried the "frontend engineer" sub-agent and "backend engineer" sub-agent and "data analyst" sub-agent thing. It doesn't work. What does work is using sub-agents for context control.

> The core insight is that your likelihood of successfully solving a problem with a coding agent is strongly correlated with the agent's ability to verify its own work.

### What this source says

To HumanLayer, the "harness" is the agent's configuration surface: AGENTS.md/CLAUDE.md, MCP servers, skills, subagents, hooks and back-pressure mechanisms. They treat harness engineering as a subset of context engineering. They say OpenAI uses the term more broadly, for everything outside the agent runtime with a focus on verification.

---

## 9. HumanLayer "All Resources" chronology

- URL: https://www.humanlayer.com/blog/humanlayer-resources (dated September 4, 2026, Dex)
- Useful for dates and HumanLayer's own description of its eras. Includes view counts and a product pitch (hype file).

> We introduced the term context engineering to describe what strong production AI builders were already doing: owning and shaping the full set of information available to a model at each step.

> After running a lights-off factory for five months and getting drowned in unmaintainable slop, we took a step back, reset, and revised our advice: read the code, seek leverage, and break skills into workflows.

> The harness is only one part of a software factory. We set out its failure modes: one-shot tests, token use, and task count do not measure whether code stays easy to change. We then described the building blocks teams need to build better factories: composable compute, development environments, harnesses, sessions, plans, artifacts, review, and human control.

Listed items not fetched (titles only, for follow-up): "The Software Factory Existential Risk" (X posts, Mar 6-10, 2026: "If teams replace code review with loops and stop reading code, one failure can leave nobody able to recover."), "Loops Engineering from First Principles" (Kyle Mistele, Jul 25, 2026), "AI That Works: Software Factory Design Patterns" (Aug 28, 2026), "State of the Software Factory - Sept 2026", SlopCodeBench reports (Jul 27, 2026).
