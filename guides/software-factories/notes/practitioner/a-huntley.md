# Geoffrey Huntley: primary-source notes

Author: Geoffrey Huntley (ghuntley.com). Independent; later at Antithesis (verification) per the Oct 2026 post.
All quotes copied from the pages as fetched 2026-10-21. Some of his posts are subscriber-only past the intro (noted where so).

---

## 1. "Ralph Wiggum as a 'software engineer'"

- URL: https://ghuntley.com/ralph/
- Date: 14 Jul 2025
- Coins: **Ralph** (the Ralph Wiggum technique / Ralph loop). Uses **back pressure** in this post (July 2025) for automated rejection of bad generation. Also uses "specs", "stdlib", "fix_plan.md", "AGENT.md", "signs".

### Definition

> If you've seen my socials lately, you might have seen me talking about Ralph and wondering what Ralph is. Ralph is a technique. In its purest form, Ralph is a Bash loop.

>     while :; do cat PROMPT.md | claude-code ; done

> Ralph can replace the majority of outsourcing at most companies for greenfield projects. It has defects, but these are identifiable and resolvable through various styles of prompts.

> That's the beauty of Ralph - the technique is deterministically bad in an undeterministic world.

> Ralph can be done with any tool that does not cap tool calls and usage.

### Tuning by "signs" (the playground metaphor)

> It begins with no playground, and Ralph is given instructions to construct one.
> Ralph is very good at making playgrounds, but he comes home bruised because he fell off the slide, so one then tunes Ralph by adding a sign next to the slide saying "SLIDE DOWN, DON'T JUMP, LOOK AROUND," and Ralph is more likely to look and see the sign.

> Eventually all Ralph thinks about is the signs so that's when you get a new Ralph that doesn't feel defective like Ralph, at all.

> There seems to be an obsession in the programming community with the perfect prompt. There is no such thing as a perfect prompt.

> When CURSED is being built, I'm sitting there watching the stream, looking for patterns of bad behaviour—opportunities to tune Ralph.

### Against multi-agent (at that time)

> While I was in SFO, everyone seemed to be trying to crack on multi-agent, agent-to-agent communication and multiplexing. At this stage, it's not needed. Consider microservices and all the complexities that come with them. Now, consider what microservices would look like if the microservices (agents) themselves are non-deterministic—a red hot mess.

> What's the opposite of microservices? A monolithic application. A single operating system process that scales vertically. Ralph is monolithic. Ralph works autonomously in a single repository as a single process that performs one task per loop.

### One item per loop; context window budget

> To get good outcomes with Ralph, you need to ask Ralph to do one thing per loop. Only one thing. Now, this might seem wild, but you also need to trust Ralph to decide what's the most important thing to implement. This is full hands-off vibe coding that will test the bounds of what you consider "responsible engineering".

> There's a few things in the above prompt which I'll expand upon shortly but the other key thing is deterministically allocate the stack the same way every loop.

> The items that you want to allocate to the stack every loop are your plan ("@fix_plan.md") and your specifications.

> One item per loop. I need to repeat myself here—one item per loop. You may relax this restriction as the project progresses, but if it starts going off the rails, then you need to narrow it down to just one item.

> The name of the game is that you only have approximately 170k of context window to work with. So it's essential to use as little of it as possible. The more you use the context window, the worse the outcomes you'll get. Yes, this is wasteful because you're effectively burning the allocation of the specifications every loop and not reusing the allocation.

### Specs

> Specs are formed through a conversation with the agent at the beginning phase of a project. Instead of asking the agent to implement the project, what you want to do is have a long conversation with the LLM about your requirements for what you're about to implement. Once your agent has a decent understanding of the task to be done, it's at that point that you issue a prompt to write the specifications out, one per file, in the specifications folder.

### Subagents; primary context as scheduler

> Ralph requires a mindset of not allocating to the primary context window. Instead, what you should do is spawn subagents. Your primary context window should operate as a scheduler, scheduling other subagents to perform expensive allocation-type work, such as summarising whether your test suite worked.

> If you were to fan out to a couple of hundred subagents and then tell those subagents to run the build and test of an application, what you'll get is bad form back pressure. Thus, the instruction above is that only a single subagent should be used for validation, but Ralph can use as many subagents as he likes for searching the file system and for writing files.

### Failure modes named

> A common failure scenario for Ralph is when the LLM runs ripgrep and comes to the incorrect conclusion that the code has not been implemented. This failure scenario is easily resolved by erecting a sign for Ralph, instructing Ralph not to make assumptions.

> If you wake up to find that Ralph is doing multiple implementations, then you need to tune this step. This nondeterminism is the Achilles' heel of Ralph.

> Claude has the inherent bias to do minimal and placeholder implementations.

> Do not be dismayed if, in the early days, Ralph ignores this sign and does placeholder implementations. The models have been trained to chase their reward function, and the reward function is compiling code. You can always run more Ralphs to identify placeholders and minimal implementations and transform that into a to-do list for future Ralph loops.

> Yep, it's true, you'll wake up to a broken codebase that doesn't compile from time to time, and you'll have situations where Ralph can't fix it himself. This is where you need to put your brain on. You need to make a judgment call. Is it easier to do a git reset --hard and to kick Ralph back off again? Or do you need to come up with another series of prompts to be able to rescue Ralph?

### Phase one: generate / phase two: backpressure

> Generating code is now cheap, and the code that Ralph generates is within your complete control through your technical standard library and your specifications.

> If Ralph is generating the wrong code or using the wrong technical patterns, then you should update your standard library to steer it to use the correct patterns.
> If Ralph is building the wrong thing completely, then your specifications may be incorrect.

> This is where you need to have your engineering hat on. As code generation is easy now, what is hard is ensuring that Ralph has generated the right thing. Specific programming languages have inbuilt back pressure through their type system.

> It's the speed of the wheel turning that matters, balanced against the axis of correctness.

> In the diagram above, it just shows the words "test and build", but this is where you put your engineering hat on. Anything can be wired in as back pressure to reject invalid code generation. That could be security scanners, it could be static analysers, it could be anything. But the key collective sum is that the wheel has got to turn fast.

> If you're using a dynamically typed language, I must stress the importance of wiring in a static analyser/type checker when Ralphing

### Notes for future loops

> it's crucial in that moment to ask Ralph to write out the meaning and the importance of the test explaining what it's trying to do.

> To me, I see it like leaving little notes for future iterations by the LLM, explaining why a test exists and its importance because future loops will not have the reasoning in their context window.

### TODO list, planning mode vs building mode

> You have to believe in eventual consistency and know that most issues can be resolved through more loops with Ralph, focusing on the areas where Ralph is making mistakes.

> The TODO list is what I'm watching like a hawk. And I throw it out often.

> Then when you've got your todo list you kick Ralph back off again with... instructions to switch from planning mode to building mode...

### Loop back; AGENT.md

> You want to program in ways where Ralph can loop himself back into the LLM for evaluation. This is incredibly important. Always look for opportunities to loop Ralph back on itself.

> The @AGENT.md is the heart of the loop. It instructs how Ralph should compile and run the project. If Ralph discovers a learning, permit him to self-improve

### Maintainability, limits, role of engineers

> When I hear that argument, I question "by whom"? By humans? Why are humans the frame for maintainability? Aren't we in the post-AI phase where you can just run loops to resolve/adapt when needed?

> What I'd like people to understand is that all these issues, created by Ralph, can be resolved by crafting a different series of prompts and running more loops with Ralph.

> Ralph has three states. Under baked, baked, or baked with unspecified latent behaviours (which are sometimes quite nice!)

> Having said all of that, engineers are still needed. There is no way this is possible without senior expertise guiding Ralph. Anyone claiming that engineers are no longer required and a tool can do 100% of the work without an engineer is peddling horseshit.

> "There's no way in heck would I use Ralph in an existing code base"

> This works best as a technique for bootstrapping Greenfield, with the expectation you'll get 90% done with it.

### What this source says

Ralph is a loop that feeds the same prompt file to a coding agent over and over. Each pass starts with a fresh context window and loads the same things: the specs and a plan file (`fix_plan.md`). The agent does one item per pass, runs tests, commits, and updates the plan and an `AGENT.md` file of build learnings. The operator watches the output and adds instructions ("signs") whenever a failure pattern shows up. Specs come from a long conversation with the agent and are written one per file. "Back pressure" (type systems, tests, static analysers, security scanners) rejects bad generation, and the loop should run fast. Huntley prefers one process per repository over multi-agent designs. He names these failure modes: wrongly deciding code is missing after a search, duplicate implementations, placeholder or minimal implementations, a broken build overnight, and specs that contradict each other. He says senior engineers are still required, the technique is for greenfield work, and it gets you about 90% of the way. (The "$50k contract for $297" item in the post is a reposted tweet with no method; it is in the hype file.)

---

## 2. "everything is a ralph loop"

- URL: https://ghuntley.com/loop/
- Date: 17 Jan 2026
- Uses **software factory** = "evolutionary software"; refers to "level 8" and "level 9" (in Yegge's numbering; Gas Town is "a full level 8"). Introduces **Loom** ("The Weaving Loom"). Names **forward mode** and **reverse mode (clean rooming)**.

> Standard software practices is to build it vertically brick by brick - like Jenga but these days I approach everything as a loop. You see ralph isn't just about forwards (building autonomously) or reverse mode (clean rooming) it's also a mind set that these computers can be indeed programmed.

> I'm there as an engineer just as I was in the brick by brick era but instead am programming the loop, automating my job function and removing the need to hire humans.

> Software is now clay on the pottery wheel and if something isn't right then i just throw it back on the wheel to address items that need resolving.

> Ralph is an orchestrator pattern where you allocate the array with the required backing specifications and then give it a goal then looping the goal.

> It's important to watch the loop as that is where your personal development and learning will come from. When you see a failure domain – put on your engineering hat and resolve the problem so it never happens again.

> In practice this means doing the loop manually via prompting or via automation with a pause that involves having to prcss CTRL+C to progress onto the next task. This is still ralphing as ralph is about getting the most out how the underlying models work through context engineering and that pattern is GENERIC and can be used for ALL TASKS.

> Loom is something that has been in my head for the last three years (and various prototypes were developed last year!) and it is essentially infrastructure for evolutionary software. Gas town focuses on spinning plates and orchestration - a full level 8.

> I'm going for a level 9 where autonomous loops evolve products and optimise automatically for revenue generation. Evolutionary software - also known as a software factory.

> Whilst software development/programming is now dead. We however deeply need software engineers with these skills who understand that LLMs are a new form of programmable computer.

> It's not that hard to build a coding agent. 300 lines of code running in a loop with LLM tokens. You just keep throwing tokens at the loop, and then you've got yourself an agent.

> Here in the tweet below I am putting loom under the mother of all ralph loops to automatically perform system verification.

### What this source says

Huntley widens Ralph from a coding technique into a general way of working. The engineer's job becomes programming the loop, watching it, and fixing each failure class so it does not happen again. He repeats his warning against multi-agent designs. He defines a "software factory" as "evolutionary software": autonomous loops that change a product and optimise it for revenue. He places this at a "level 9", one step past Gas Town's "level 8" in Yegge's numbering. Loom is his research system for it. (The claims "software development is dead - I killed it" and "cheaper than the wage of a burger flipper" are slogans; they are in the hype file.)

---

## 3. "don't waste your back pressure" (Huntley's pointer post) and Moss's original

- Huntley URL: https://ghuntley.com/pressure/ (17 Jan 2026; mostly subscriber-only)
- Original essay URL: https://banay.me/dont-waste-your-backpressure/ by **Moss** (Moss' blog), Sat, Jan 17, 2026
- Huntley used "back pressure" for agent loops in July 2025 (Ralph post). Moss's essay is the fullest definition. Huntley says Moss "translated" a conversation between them "into words".

Huntley:

> A simple convo between mates - well Moss translated it into words and i've been waiting for it to come out so I didn't front run him.

> Enjoy. This is what engineering now looks like in the post loom/gastown era or even when doing ralph loops.

> If you aren't capturing your back-pressure then you are failing as a software engineer.

Moss (definition):

> You might notice a pattern in the most successful applications of agents over the last year. Projects that are able to setup structure around the agent itself, to provide it with automated feedback on quality and correctness, have been able to push them to work on longer horizon tasks.

> This back pressure helps the agent identify mistakes as it progresses and models are now good enough that this feedback can keep them aligned to a task for much longer.

> This means you spend your back pressure (the time you spend giving feedback to agents) on typing a message telling the agent it missed an import. This scales poorly and limits you to working on simple problems.

> Languages with expressive type systems have been growing in popularity in part because of back pressure.

> I think that the payoff of investing into higher quality testing is growing massively, and an increasing part of engineering will involve designing and building back pressure in order to scale the rate at which contributions from agents can be accepted.

> In your projects you should think about how you can build back pressure into your workflow and once you have it, you can loop agents until they have stamped out all of the inconsistencies and issues for you. Without it, you're going to be stuck spending your time telling the agent about each mistake it makes yourself.

### What this source says

Back pressure is automated feedback on quality and correctness that the agent can read and act on: build output, type errors, tests, rendered UI from Playwright or DevTools, LSP lints, generated OpenAPI docs, proof assistants, fuzzing. Moss also uses the phrase for the human feedback budget itself ("the time you spend giving feedback to agents"). If a human has to spend that time on trivial mistakes, the work does not scale. Investing in tests and checks raises how much agent output can be accepted.

---

## 4. "how to build a coding agent: free workshop"

- URL: https://ghuntley.com/agent/
- Date: 24 Aug 2025
- Defines **agent** and **harness** as he uses them.

> 300 lines of code running in a loop with LLM tokens. You just keep throwing tokens at the loop, and then you've got yourself an agent.

> Cursor, Windsurf, Claude Code, GitHub Copilot, and Amp are just a small number of lines of code running in a loop of LLM tokens. I can't stress that enough. The model does all the heavy lifting here, folks. It's the model that does it all.

> The advertised context window for Sonnet is 200k. However, you don't get to use all of that because the model needs to allocate memory for the system-level prompt. Then the harness (Cursor, Windsurf, Claude Code, Amp) also needs to allocate some additional memory, which means you end up with approximately 176k tokens usable.

> The first primitive behind any coding agent is a read tool.

(Five primitives in order: read, list, bash, edit, search.)

> The fifth and final primitive behind any coding harness is a search tool. What if I were to tell you that there is no magic for indexing source code or any intelligence?

> The harness prompt is where your tool registrations go.

### What this source says

To Huntley, an "agent" is the inference loop plus tools. A "harness" is the product around the model (Cursor, Claude Code, Amp) that registers tools and takes up context. A coding agent needs five tools: read, list, bash, edit, search.

---

## 5. "I dream about AI subagents; they whisper to me while I'm asleep"

- URL: https://ghuntley.com/subagents/
- Date: 13 Apr 2025

> Claude 3.7's advertised context window is 200k, but I've noticed that the quality of output clips at the 147k-152k mark. Regardless of which agent is used, when clipping occurs, tool call to tool call invocation starts to fail

> The current generation of coding agents work via a tight evaluation loop of tool calls to tool calls that operate within a single context window (ie. RAM). However, the problem with this design is that when an LLM provides a bad outcome, the coding assistants/agents' death spiral and brute force on the main context window which consumes precious resources as it tries to figure out the next steps.

> What if an agent could spawn a new agent and clone the context window? If such a thing were possible, it would enable an agent to spawn a sub-agent. The main agent would pause, wait for the sub-agent to burn through its own context window (ie. SWAP), and then provide concrete next steps for the primary agent.

### What this source says

The context window works like RAM. He observed output quality degrading near 147k-152k of an advertised 200k ("real" vs "advertised" context window). He proposes subagents so the main context does not fall into a "death spiral". This is the earliest primary statement in this set of context degradation before the window is full. Horthy later calls this the "dumb zone".

---

## 6. "software doesn't need to be readable anymore. it needs to be explainable."

- URL: https://ghuntley.com/readable/
- Date: 02 Oct 2026 (write-up of AI21 YAAP podcast)

> Software doesn't need to be readable by a human. It needs to be explainable to a human.

> That's the shift. The artifact doesn't need to be optimized for a human to read cold. It needs to be something a model can explain to a human on demand.

> Types are a form of verification. They provide back pressure: compiler errors that the LLM picks up and fixes automatically, every loop.

> This is also why I can get away with cheaper models. Pick a language that does the verification for you, and you need less intelligence to stay on the rails.

> Porting is easy when the end result is easy to verify.

> Since January, I've been talking about Loom and the idea of a software factory, something that optimizes a whole business function. It's on GitHub, it's not really usable, and it's not intended to be; it's research.

> Software factories are very, very hard to do right now. For the last six months, my view has been that we need one of: better models, better programming languages, or a revival of some old computer science techniques like simulators.

> It's a distributed system, so I'm building it in Rust and building the simulator first, then driving the agent to validate everything through the simulator. That has kept the agent on the rails remarkably well.

### What this source says

Code should be explainable on demand by a model, not readable cold by a human. Type systems are back pressure, and strong types let cheaper models stay on track. By Oct 2026 Huntley says software factories are "very, very hard to do right now". He says they need better models, better languages, or simulators. Building the simulator first kept his agent on track.

---

## 7. "nobody should type code by hand anymore. here's what's left."

- URL: https://ghuntley.com/agency/
- Date: 13 Oct 2026 (write-up of four-part conversation with Josh Wulf, "Agentic Engineering" show)
- Terms: **loop engineering**, **filesystem-as-state**, **whiteboard defence**, **"Danger Systems in the loop"**, "vision and verification", "skill packs are astrology", "agency, not AGENTS.md" (Josh Wulf's phrase).

> Josh Wulf and I talked loop engineering for four episodes. The models stopped being the constraint a long time ago; what's left is vision, verification and agency. Delete your skill packs, put the whole system under test, and revisit everything that used to be hard.

> In February last year I discovered filesystem-as-state, the first of the loops: the idea of autonomously building things.

> Take an existing application, clean-room it into specifications, then rebuild the software from those specifications, much like the way AMD's CPUs came out of Intel's.

> So he figured out what the missing 20% was: completeness and verification, because the models would leave stubs and partial implementations. Do the 20% instead of the 100%, and you've got scale.

> If companies think they're going to build a swarm or a software factory, how will they afford that talent when they're competing directly with the labs for talent? It'll be "I've heard about Kubernetes, let's do a Kubernetes project" that fails all over again.

> If humans eyeballing code were sufficient engineering to stop bugs, we'd never have had any defects. It didn't work at human speed. It sure as heck isn't going to work at a thousand times human speed.

> When I develop software, I put the entire system under test, operating system included, with Nix, and the agent runs against that.

> LLMs can act as a judge and spot problems, but they can't tell you whether something will hold up in worst-case scenarios.

> Josh framed it well. Humans fit in at two points: the vision and the verification. The implementation in the middle has become a black box, whether that's a team of contractors you never see or silicon.

> For any code I work on, I want a whiteboard defence. If someone asks how it works, I should be able to draw the system-level design and defend it.

> I'm not advocating for complete YOLO. It's still engineering; the craft is just very different.

> If your codebase has bad architectural patterns, or is inconsistent, AI will copy and paste them everywhere. It's an amplifier.

> Many people spend their time tuning the agent itself: skill packs, AGENTS.md, MCPs. They're probabilistic. There's no guarantee they'll do anything.

> I swear it's astrology for software engineers. Horoscopes. Just because it's there doesn't mean it works, but it reads well and makes you feel good.

> Instead, I write a pre-commit hook that checks the git diff for direct calls to observability modules that bypass my diagnostics module. Boom: fail the commit, inject a prompt telling the agent to use the diagnostics library. All of a sudden it's ten out of ten. Josh called it Danger Systems in the loop.

> Here's something most people don't know: you should probably delete your skills and your AGENTS.md every couple of months. The models get better, so how do you know you're not de-tuning them? Unless you've invested in evals over all your traces (lab behavior, and a tiny minority of companies), you don't know whether you're going forward or backward.

> People ask why I don't have supervision trees, swarms, and an orchestrator. I've built that. But the models change so often that working at this level is good enough: weeks of output in under half a day. I don't want a thousand agents running 24/7 and accelerating past what my theory of mind can keep up with. I want to keep my whiteboard defense. Josh called it going fast by going slow.

> Keep in mind that I do a lot of greenfield and research work. My agents have sudo, and I push to main. I don't do pull requests anymore. They're gone. I've built my trust up to that point. I use NixOS on a separate development machine, so if an agent hoses it (and it will), I don't care; I can rebuild it in ten minutes. Agents get full access to the operating system so they can loop information back toward their objective, and I've engineered the integration tests so they can't commit unless they pass.

> Back pressure is what keeps the loop honest.

> That's why I'm in the verification space: you need a good verification platform as back pressure.

> If you have an oracle, porting is a loop.

### What this source says

By late 2026 Huntley says the scarce inputs are vision, verification and agency, not model capability. He says human PR review does not scale to agent volume. He would replace it with ownership: whole-system tests (Nix, deterministic simulation and fault injection at Antithesis, property-based tests) and deterministic checks in pre-commit hooks. He calls skill packs and AGENTS.md tuning unverified ("astrology"). He suggests deleting them every few months unless you have evals over your traces. He chooses not to run swarms or an orchestrator, so that he can keep a "whiteboard defence" of the system. He also warns that companies trying to build a "swarm or a software factory" will fail for lack of talent. ("500,000 unique views", the "$450 million" figure, the "15 million sandboxes" anecdote, and "Cloning three or four companies to write a conference talk is not unhinged. That's the baseline now." are unsupported claims; see the hype file.)

---

## 8. Other Huntley posts checked (lower relevance)

- "autoregressive queens of failure", https://ghuntley.com/gutter/, 22 Apr 2025: autoregressive failure (the model compounding its own bad output).
- "too many model context protocol servers and LLM allocations on the dance floor", https://ghuntley.com/allocations/, 23 Aug 2025: "Less is more in the context window."
- "the eighteen-month recap: AI Engineer, Singapore, May 2026", https://ghuntley.com/eighteen-month-recap/, 27 Sep 2026. Quote:

> It's been roughly a year and a half since I published the technique of allocating memory in a particular way. If you wrap the tool calls around another loop, it's just a loop. But there's a lot of science in the context engineering needed to actually achieve these outcomes

> It's really sad, because LLMs and AI are literally just a while loop, and Ralph is a while loop on a while loop.
