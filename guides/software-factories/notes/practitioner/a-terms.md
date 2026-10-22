# Glossary of terms of art (practitioner set A)

Each entry gives the coiner or earliest primary user found, the date, the definition in the originator's own words, and the URL. "Coined" means the author claims it or is credited by the others. Where coinage is disputed, the evidence is listed. Talk quotes come from auto-transcripts; check them against the video before citing.

---

## Part 1: words the practitioners use differently

### "agent"

| Author | Definition (verbatim) | Source |
|---|---|---|
| Simon Willison (18 Sep 2025) | "An LLM agent runs tools in a loop to achieve a goal." | https://simonwillison.net/2025/Sep/18/agents/ |
| Geoffrey Huntley (24 Aug 2025) | "300 lines of code running in a loop with LLM tokens. You just keep throwing tokens at the loop, and then you've got yourself an agent." | https://ghuntley.com/agent/ |
| Dex Horthy (Apr 2025) | "Agents, at least the good ones, don't follow the "here's your prompt, here's a bag of tools, loop until you hit the goal" pattern. Rather, they are comprised of mostly just software." | https://github.com/humanlayer/12-factor-agents |
| Steve Yegge (1 Jan 2026) | "In Gas Town, an agent is not a session. Sessions are ephemeral" / "In Gas Town, an agent is a Bead, an identity with a singleton global address." | https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04 |
| Vivek Trivedy (10 Mar 2026) | "Agent = Model + Harness." / "A raw model is not an agent. But it becomes one when a harness gives it things like state, tool execution, feedback loops, and enforceable constraints." | https://www.vtrivedy.com/posts/the-anatomy-of-an-agent-harness |
| Solomon Hykes (quoted by Willison, 30 Sep 2025) | "An AI agent is an LLM wrecking its environment in a loop." | https://simonwillison.net/2025/Sep/30/designing-agentic-loops/ |

Differences: Willison and Huntley define an agent as a mechanism (tools in a loop). Horthy's 12-factor sense is about agent *products* and says good ones are mostly deterministic code. Yegge separates the agent (a persistent identity stored in git) from the session (disposable). Horthy credits Willison: "An agent is just tools in a loop" (No Vibes Allowed, auto-transcript).

### "harness"

| Author | Meaning | Source |
|---|---|---|
| Huntley (24 Aug 2025) | The coding-agent product around the model: "the harness (Cursor, Windsurf, Claude Code, Amp) also needs to allocate some additional memory". "The harness prompt is where your tool registrations go." | https://ghuntley.com/agent/ |
| Willison (18 Sep 2025) | What runs the tools: "the LLM is given the ability to request actions to be executed by its harness" | https://simonwillison.net/2025/Sep/18/agents/ |
| HumanLayer / Kyle Mistele (12 Mar 2026) | The agent's configuration surface: "We call this the coding agent's harness, and we think of it as the agent's runtime, or as its peripherals: what does the model use to interact with its environment?" | https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents |
| Vivek Trivedy (10 Mar 2026) | Everything except the model: "A harness is every piece of code, configuration, and execution logic that isn't the model itself." | https://www.vtrivedy.com/posts/the-anatomy-of-an-agent-harness |
| StrongDM (Feb 2026) | The *validation* harness: "Your validation harness must be end-to-end, as close to the real environment as possible: customers, integrations, economics." | https://factory.strongdm.ai/principles |
| Yegge (Aug 2026) | His own orchestrator: "Wheelhouse, my orchestrator/harness for Wyvern". "I believe harnesses will all soon be bespoke". | https://yegge.ai/essays/the-shape-of-things-to-come/ |
| Horthy (Jul 2026) | One component of a factory: "The harness is only one part of a software factory." | https://www.humanlayer.com/blog/humanlayer-resources |

Differences: For Huntley and Willison the harness is the agent runtime. For HumanLayer it is the configurable surface of that runtime (AGENTS.md, skills, MCP, hooks, subagents). For Trivedy it is everything that is not the model. For StrongDM it is the verification apparatus. For Yegge it is the whole multi-agent orchestrator, and he says it must be bespoke.

### "harness engineering" (coinage disputed)

- Horthy, Nov 2025 (auto-transcript): "if you really want a hypy word, you can call this harness harness engineering, which is part of context engineering, and it's how you integrate with the integration points on codeex, claude, cursor, whatever." https://www.youtube.com/watch?v=rmvDxxNubIg
- Mitchell Hashimoto, February 5, 2026: "I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this "harness engineering." It is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again." https://mitchellh.com/writing/my-ai-adoption-journey
- Vivek Trivedy, 17 Feb, 2026: "Harness Engineering is about systems, you're building tooling around the model to optimize goals like task performance, token efficiency, latency, etc." https://www.vtrivedy.com/posts/improving-deep-agents-with-harness-engineering
- OpenAI "Harness engineering" (Ryan Lopopolo), Feb 2026, https://openai.com/index/harness-engineering/ (not fetched; blocked).
- HumanLayer's attribution (12 Mar 2026): "Harness engineering, coined by Viv, describes the practice of leveraging these configuration points to customize and improve your coding agent's output quality and reliability." and "We view harness engineering as a subset of context engineering."
- Horthy's later use, in the WSFF subtitle (Jul 2026): "or: harness engineering is not enough".

Note: Hashimoto's definition is the same practice as Huntley's July 2025 "signs" (tuning Ralph after each observed failure).

### "software factory"

| Author | Definition (verbatim) | Source |
|---|---|---|
| NATO 1968 (per Horthy) | "the term traces all the way back to a NATO conference in 1968 -- the same one that gave us "software engineering."" | https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md |
| Huntley (17 Jan 2026) | "I'm going for a level 9 where autonomous loops evolve products and optimise automatically for revenue generation. Evolutionary software - also known as a software factory." | https://ghuntley.com/loop/ |
| Huntley (2 Oct 2026) | "the idea of a software factory, something that optimizes a whole business function" | https://ghuntley.com/readable/ |
| StrongDM / McCarthy (6 Feb 2026) | "We built a Software Factory: non-interactive development where specs + scenarios drive agents that write code, run harnesses, and converge without human review." | https://factory.strongdm.ai/ |
| Yegge (1 Jan 2026) | "Gas Town is an industrialized coding factory manned by superintelligent robot chimps" | https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04 |
| Yegge (24 Apr 2026) | "That's why we think of deployed orchestration as being fundamentally made of multi-agent teams: factories." | https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607 |
| Horthy (22 Jul 2026) | Pre-AI 2022 factory = tracker → build → PR review → ship → monitor → user feedback loops. "The agentic factory looks mostly like swapping "someone builds the thing" → "an agent builds the thing"" | wsff.md (above) |

Differences: Horthy uses the word for any software delivery system, including human teams. StrongDM means one with no human writing or review. Huntley means a system that changes the product itself and optimises business outcomes. Yegge means a multi-agent orchestrator, and later extends it to business processes.

### "dark factory" / "lights-off factory"

| Author | Definition (verbatim) | Source |
|---|---|---|
| Dan Shapiro (23 Jan 2026), coiner for software | "At level 5, it's not really a car any more. ... It's a black box that turns specs into software." / "It's dark, because it's a place where humans are neither needed nor welcome." | https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/ |
| Willison (7 Feb 2026) | "what Dan Shapiro called the Dark Factory level of AI adoption, where no human even looks at the code the coding agents are producing" | https://simonwillison.net/2026/Feb/7/software-factory/ |
| Yegge (24 Apr 2026) | "A dark factory is any system in which coding agents are set up to work autonomously without humans watching. The name is frankly a little bit misleading. It just means background work. ... Observability is a choice in dark factory design." | https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607 |
| Horthy (22 Jul 2026) | "lights-off software factory": "[Dan Shapiro coined this term] ... -- where we no longer read the code." | wsff.md |

Differences: Shapiro's and Willison's dark factory has no human reading the code. Yegge's has no human *watching* it in real time, and the lights can be turned up. He calls Gas City a "Light Factory" and still reviews pull requests himself. Horthy attributes "lights-off" to Shapiro, but Shapiro's post says "Dark Factory", not "lights-off".

### "loop"

| Author | Meaning (verbatim) | Source |
|---|---|---|
| Huntley (14 Jul 2025) | "Ralph is a technique. In its purest form, Ralph is a Bash loop." | https://ghuntley.com/ralph/ |
| Huntley (17 Jan 2026) | "Ralph is an orchestrator pattern where you allocate the array with the required backing specifications and then give it a goal then looping the goal." | https://ghuntley.com/loop/ |
| Willison (30 Sep 2025) | "A critical new skill to develop is designing agentic loops." | https://simonwillison.net/2025/Sep/30/designing-agentic-loops/ |
| Horthy (Jul 2026) | Skeptical: "A lot has been said about loop engineering, and the prevailing wisdom is that we should probably write more loops." | wsff.md |
| Yegge (Aug 2026) | "Gas Town wasn't really a "loop" in the sense that I thought Boris might be suggesting. It was more like a chariot, with you driving." | https://yegge.ai/essays/the-shape-of-things-to-come/ |
| StrongDM (Feb 2026) | "Seed → Validation harness → Feedback loop. Tokens are the fuel." | https://factory.strongdm.ai/principles |

Differences: Huntley's loop is the outer re-invocation of the agent with fresh context. Willison's "agentic loop" is the inner tool loop plus its environment. StrongDM's loop is validation feedback until the holdout scenarios pass. "Loop engineering" (Huntley, with Josh Wulf, Oct 2026: "Josh Wulf and I talked loop engineering"; also HumanLayer's Kyle Mistele, "Loops Engineering from First Principles", Jul 2026) is used as a discipline name by 2026.

### "spec" / "spec-driven development"

| Author | Meaning (verbatim) | Source |
|---|---|---|
| Huntley (14 Jul 2025) | "Specs are formed through a conversation with the agent at the beginning phase of a project. ... issue a prompt to write the specifications out, one per file, in the specifications folder." | https://ghuntley.com/ralph/ |
| Horthy (Aug 2025), citing Sean Grove | "Sean proposes that in the AI future, the specs will become the real code." | ace-fca.md |
| Horthy (Nov 2025, auto-transcript) | "No, specri development is broken. Not the idea, but the phrase. it's not well defined." | https://www.youtube.com/watch?v=rmvDxxNubIg |
| StrongDM (Feb 2026) | "Every piece of software needs an initial seed. Historically, you might have called this a PRD or a spec. Today, this could equally be a few sentences, a screenshot, or an existing codebase." / "Spec + Test Suite = Complete Intent" / "An existing application constitutes an executable specification." | https://factory.strongdm.ai/principles ; /techniques/shift-work |
| Shapiro (Jan 2026) | Level 4: "You write a spec. You argue with it about the spec." Level 5: "a black box that turns specs into software." | Shapiro levels post |

### "context engineering" (coinage disputed)

- Horthy, 12-Factor Agents, April 2025: "Everything is context engineering. LLMs are stateless functions that turn inputs into outputs. To get the best outputs, you need to give them the best inputs." https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md
- HumanLayer's claim (Sep 2026): "We introduced the term context engineering to describe what strong production AI builders were already doing" https://www.humanlayer.com/blog/humanlayer-resources ; Horthy (Mar 2026 talk, auto-transcript): "I wrote this paper called 12 factor agents, which was uh allegedly the first time anyone was like talking a lot about context engineering."
- Willison, 27 June 2025, credits its spread to Tobi Lutke and Andrej Karpathy and does not mention HumanLayer: "The term context engineering has recently started to gain traction as a better alternative to prompt engineering." Lutke: "the art of providing all the context for the task to be plausibly solvable by the LLM." Karpathy: "context engineering is the delicate art and science of filling the context window with just the right information for the next step." https://simonwillison.net/2025/Jun/27/context-engineering/
- Huntley calls Ralph context engineering: "ralph is about getting the most out how the underlying models work through context engineering and that pattern is GENERIC" https://ghuntley.com/loop/

---

## Part 2: terms with a single clear originator

| Term | Coiner, date | Definition (verbatim) | URL |
|---|---|---|---|
| Ralph / Ralph Wiggum technique | Geoffrey Huntley, 14 Jul 2025 (Horthy saw him present it June 19th 2025) | "Ralph is a technique. In its purest form, Ralph is a Bash loop." `while :; do cat PROMPT.md \| claude-code ; done` | https://ghuntley.com/ralph/ |
| back pressure | Huntley, 14 Jul 2025 (used); Moss, Jan 17 2026 (essay) | Huntley: "Anything can be wired in as back pressure to reject invalid code generation." Moss: "Projects that are able to setup structure around the agent itself, to provide it with automated feedback on quality and correctness, have been able to push them to work on longer horizon tasks." | https://ghuntley.com/ralph/ ; https://banay.me/dont-waste-your-backpressure/ |
| signs (tuning Ralph) | Huntley, 14 Jul 2025 | "one then tunes Ralph by adding a sign next to the slide saying "SLIDE DOWN, DON'T JUMP, LOOK AROUND," and Ralph is more likely to look and see the sign." | https://ghuntley.com/ralph/ |
| one item per loop | Huntley, 14 Jul 2025 | "One item per loop. I need to repeat myself here—one item per loop." | https://ghuntley.com/ralph/ |
| forward mode / reverse mode (clean rooming) | Huntley, 17 Jan 2026 | "ralph isn't just about forwards (building autonomously) or reverse mode (clean rooming)" | https://ghuntley.com/loop/ |
| overbaking | Huntley (reported by Horthy, 6 Jan 2026) | "If you leave ralph running too long, you end up with all sorts of bizarre emergent behavior, like post-quantum cryptography support." | https://www.humanlayer.dev/blog/brief-history-of-ralph |
| real vs advertised context window | Huntley, 13 Apr 2025 | "Claude 3.7's advertised context window is 200k, but I've noticed that the quality of output clips at the 147k-152k mark." | https://ghuntley.com/subagents/ |
| whiteboard defence | Huntley, 13 Oct 2026 | "For any code I work on, I want a whiteboard defence. If someone asks how it works, I should be able to draw the system-level design and defend it." | https://ghuntley.com/agency/ |
| explainable (not readable) software | Huntley, 2 Oct 2026 | "Software doesn't need to be readable by a human. It needs to be explainable to a human." | https://ghuntley.com/readable/ |
| intentional compaction | Dex Horthy, Aug 2025 | "Whether you're on track or not, as your context starts to fill up, you probably want to pause your work and start over with a fresh context window." | ace-fca.md |
| frequent intentional compaction | Horthy, Aug 2025 | "designing your ENTIRE WORKFLOW around context management, and keeping utilization in the 40%-60% range" | https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md |
| Research / Plan / Implement (RPI) | Horthy / HumanLayer, Aug 2025 | Research: "Understand the codebase, the files relevant to the issue, and how information flows". Plan: "Outline the exact steps ... being super precise about the testing / verification steps in each phase." Implement: "Step through the plan, phase by phase." | ace-fca.md |
| QRSPI ("crispy") | Horthy, Mar 2026 (talk) | "now it's questions, research, design, structure, plan, work tree, implement, PR" ... "we're calling this crispy." | https://www.youtube.com/watch?v=YwZR6tc7qYg |
| dumb zone / smart zone | Horthy, Nov 2025 (talk) | "Around the 40% line is where you're going to start to see some diminishing returns depending on your task." Dec 2025: "stay in the ~75k token "smart zone" for claude models" | https://www.youtube.com/watch?v=rmvDxxNubIg ; https://www.humanlayer.dev/blog/context-efficient-backpressure |
| instruction budget | Horthy (crediting cofounder Kyle), Mar 2026 | "you have an instruction budget" ... "frontier LLMs could only follow about 150 to 200 instructions with like good consistency" | https://www.youtube.com/watch?v=YwZR6tc7qYg |
| "don't use prompts for control flow" | Horthy, Mar 2026 | "The lesson is don't use prompts for control flow if you can use control flow for control flow." | same |
| mental alignment | Blake Smith (via Horthy, Aug 2025) | "the most important part of code review is mental alignment - keeping members of the team on the page as to how the code is changing and why." | ace-fca.md |
| "do not outsource the thinking" | Jake Nations, Netflix (credited by Horthy) | Horthy: "AI cannot replace thinking. It can only amplify the thinking you have done or the lack of thinking you have done." | No Vibes Allowed talk; https://www.arthropod.software/p/vibe-coding-our-way-to-disaster |
| horizontal plans / vertical slices | Horthy (vertical slices = "tracer bullets", credited to Matt Pocock and Shape Up), Jul 2026 | "Models love what I call "horizontal plans" - doing things in stack-order" | wsff.md |
| program design (as a phase) | Horthy, Jul 2026 | "we go a level down from architecture into the **shape of code**: the types, the method signatures, the program layout, and the call stacks." | wsff.md |
| maintainability has no fast oracle | Horthy, Jul 2026 | "maintainability has no fast oracle, so we can't reward for it during RL" | wsff.md |
| Five Levels (0–5) | Dan Shapiro, 23 Jan 2026 | Level 0 "your parents' Volvo"; Level 1 "lanekeeping and cruise control"; Level 2 "Autopilot on the highway"; Level 3 "a Waymo with a safety driver ... You are… a manager"; Level 4 "a robotaxi ... you're a PM"; Level 5 dark factory. | Shapiro levels post |
| technical deflation | Shapiro, 17 Dec 2025 | "AI is driving down the cost of writing code. Economists have a word for what happens when stuff keeps getting cheaper: deflation." | https://www.danshapiro.com/blog/2025/12/this-is-a-time-of-technical-deflation/ |
| six waves; agent clusters; agent fleets | Steve Yegge, 22 Mar 2025 | "traditional (2022), completions-based (2023), chat-based (2024), coding agents (2025 H1), agent clusters (2025 H2), and agent fleets (2026)"; "agent fleets" are "what happens when we get AI supervisors for the leaf nodes" | https://sourcegraph.com/blog/revenge-of-the-junior-developer |
| 8 stages (of developer AI adoption) | Yegge, 1 Jan 2026 | Stage 1 "Zero or Near-Zero AI" … Stage 8 "Building your own orchestrator." | Gas Town post |
| Beads | Yegge, 13 Oct 2025 | "Beads is a git-backed issue tracker that gives coding agents the memory they don't have." | https://yegge.ai/essays/introducing-beads-a-coding-agent-memory-system/ |
| Gas Town | Yegge, 1 Jan 2026 | "Gas Town is a new take on the IDE for 2026. Gas Town helps you with the tedium of running lots of Claude Code instances." | Gas Town post |
| Gas Town roles: Overseer, Mayor, Polecats, Refinery, Witness, Deacon, Dogs, Crew | Yegge, 1 Jan 2026 | e.g. "Refinery: ... the engineer agent responsible for intelligently merging all changes, one at a time, to main." (see a-yegge.md for all) | Gas Town post |
| GUPP | Yegge, 1 Jan 2026 | "GUPP states, simply: If there is work on your hook, YOU MUST RUN IT." | Gas Town post |
| MEOW / molecules | Yegge, 1 Jan 2026 | "Molecular Expression of Work (MEOW)"; "molecules are workflows, chained with Beads." | Gas Town post |
| NDI (Nondeterministic Idempotence) | Yegge, 1 Jan 2026 | "even though the path is fully nondeterministic, the outcome — the workflow you wanted to run — eventually finishes, "guaranteed", as long as you keep throwing agents at it." | Gas Town post |
| Light Factory; shepherds | Yegge, 24 Apr 2026 | "I have begun to think of Gas City as a Light Factory… or at least, a very well-lit dark one!"; "devs will become shepherds, tending flocks of agents" | https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607 |
| Land Rush / Thunderdome | Yegge, Aug 2026 | "whenever the MQ hits 100, we abandon the bisection and just smash it all in with a megabatch. And then we do swarm diagnosis (not bisection) to fix it." | https://yegge.ai/essays/the-shape-of-things-to-come/ |
| Wish Factory | Yegge (name) / Guy Podjarny (idea), Aug 2026 | "an agent you can throw onto a GitHub repo. It doesn't accept PRs, only GHIs. It then implements them for you." | same |
| "crons watch, models act" | Yegge, Aug 2026 | "I have about 45 launchd/systemd units ... that wake an agent when something needs judgment. The rule is: crons watch, models act." | same |
| discernment horizon | Yegge, 19 Jun 2026 | "set not by the hardest problem you can pose, but by the hardest answer you can judge." | https://steve-yegge.medium.com/the-flat-curve-society-36c8b01eb33b |
| non-interactive development / grown software | StrongDM, 6 Feb 2026 | "the first glimmer of what we now refer to internally as non-interactive development or grown software." | https://factory.strongdm.ai/ |
| compounding correctness | StrongDM, 6 Feb 2026 | "long-horizon agentic coding workflows began to compound correctness rather than error." | https://factory.strongdm.ai/ |
| scenario (repurposed) | StrongDM, 6 Feb 2026 (Willison traces it to Cem Kaner's scenario testing, 2003) | "an end-to-end "user story", often stored outside the codebase (similar to a "holdout" set in model training), which could be intuitively understood and flexibly validated by an LLM." | https://factory.strongdm.ai/ |
| satisfaction | StrongDM, 6 Feb 2026 | "of all the observed trajectories through all the scenarios, what fraction of them likely satisfy the user?" | https://factory.strongdm.ai/ |
| Digital Twin Universe (DTU) | StrongDM (Jay Taylor created it, per Willison), Feb 2026 | "behavioral clones of the third-party services our software depends on." | https://factory.strongdm.ai/techniques/dtu |
| gene transfusion | StrongDM, Feb 2026 | "Move working patterns between codebases by pointing agents at concrete exemplars." | https://factory.strongdm.ai/techniques |
| shift work | StrongDM, Feb 2026 | "Separate interactive work from fully specified work." | https://factory.strongdm.ai/techniques |
| semport | StrongDM, Feb 2026 | "Semantically-aware automated ports, one time or ongoing." | https://factory.strongdm.ai/techniques |
| pyramid summaries | StrongDM, Feb 2026 | "Reversible summarization at multiple zoom levels." | https://factory.strongdm.ai/techniques |
| deliberate naivete | StrongDM, Feb 2026 | "finding and removing the habits, conventions, and constraints of Software 1.0." | https://factory.strongdm.ai/ |
| lethal trifecta | Simon Willison, 16 Jun 2025 | "Access to your private data ... Exposure to untrusted content ... The ability to externally communicate" | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ |
| designing agentic loops | Willison, 30 Sep 2025 | "The art of using them well is to carefully design the tools and loop for them to use." | https://simonwillison.net/2025/Sep/30/designing-agentic-loops/ |
| vibe engineering | Willison, 7 Oct 2025 (superseded) | "seasoned professionals accelerate their work with LLMs while staying proudly and confidently accountable for the software they produce" | https://simonwillison.net/2025/Oct/7/vibe-engineering/ |
| agentic engineering | Willison's definition, 23 Feb 2026 (he says the term was "coming out on top"; not his coinage) | "building software using coding agents ... where the defining feature is that they can both generate and execute code" | https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/ |
| vibe coding | Andrej Karpathy, Feb 2025 (credited by Yegge and Willison) | Willison: "coding where you pay no attention to the code at all". Yegge (different): "vibe coding just means letting the AI do the work." | Willison Feb 2026; Yegge Mar 2025 |
