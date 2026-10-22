# Simon Willison: primary-source notes

Author: Simon Willison (simonwillison.net). He documents others' work closely and coins or defines terms himself. All quotes are from his blog as fetched 2026-10-21.

---

## 1. "The lethal trifecta for AI agents: private data, untrusted content, and external communication"

- URL: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Date: 16th June 2025
- Coins: **lethal trifecta**.
- Relevance to factories: unattended agents with shell, network and secrets meet all three conditions. StrongDM's DTU and Huntley's separate NixOS machine are partial answers. Yegge runs with "no sandboxing".

> The lethal trifecta of capabilities is:
> - Access to your private data—one of the most common purposes of tools in the first place!
> - Exposure to untrusted content—any mechanism by which text (or images) controlled by a malicious attacker could become available to your LLM
> - The ability to externally communicate in a way that could be used to steal your data (I often call this "exfiltration" but I'm not confident that term is widely understood.)

> If your agent combines these three features, an attacker can easily trick it into accessing your private data and sending it to that attacker.

> LLMs are unable to reliably distinguish the importance of instructions based on where they came from. Everything eventually gets glued together into a sequence of tokens and fed to the model.

### What this source says

Any agent that has private data, untrusted input and an outbound channel can be steered by prompt injection into leaking data. The fix is to remove one of the three.

---

## 2. "Context engineering"

- URL: https://simonwillison.net/2025/Jun/27/context-engineering/
- Date: 27th June 2025
- Records the June 2025 spread of **context engineering** via Tobi Lutke and Andrej Karpathy. He does not mention HumanLayer's April 2025 use. This conflicts with HumanLayer's claim to have coined it (see a-terms.md).

> The term context engineering has recently started to gain traction as a better alternative to prompt engineering. I like it. I think this one may have sticking power.

Quoting Tobi Lutke:

> I really like the term "context engineering" over prompt engineering.
> It describes the core skill better: the art of providing all the context for the task to be plausibly solvable by the LLM.

Quoting Andrej Karpathy:

> +1 for "context engineering" over "prompt engineering".

> context engineering is the delicate art and science of filling the context window with just the right information for the next step.

> It turns out that inferred definitions are the ones that stick. I think the inferred definition of "context engineering" is likely to be much closer to the intended meaning.

---

## 3. "I ran Claude in a loop for three months, and it created a genz programming language called cursed" (link post)

- URL: https://simonwillison.net/2025/Sep/9/cursed/
- Date: 9th September 2025
- Documents the outcome of Huntley's Ralph loop (the CURSED language).

> Geoffrey Huntley vibe-coded an entirely new programming language using Claude

> This is a substantial project. The repository currently has 1,198 commits. It has both an interpreter mode and a compiler mode, and can compile programs to native binaries (via LLVM) for macOS, Linux and Windows.

> The first version was written in C, then Geoffrey had Claude port it to Rust and then Zig.

Huntley's cost, as quoted by Willison:

> Technically it costs about 5k usd to build your own compiler now because cursed was implemented first in c, then rust, now zig. So yeah, it's not one compiler it's three editions of it. For a total of $14k USD.

### What this source says

An independent check that the Ralph-built artifact exists and what it contains (commit count, modes, targets). The cost figure is Huntley's own.

---

## 4. "I think 'agent' may finally have a widely enough agreed upon definition to be useful jargon now"

- URL: https://simonwillison.net/2025/Sep/18/agents/
- Date: 18 September 2025
- Defines **agent** as "tools in a loop to achieve a goal". Horthy credits this ("thank you, Simon ... An agent is just tools in a loop").

> Moving forward, when I talk about agents I'm going to use this:
> An LLM agent runs tools in a loop to achieve a goal.

> The "tools in a loop" definition has been popular for a while—Anthropic in particular have settled on that one. This is the pattern baked into many LLM APIs as tools or function calls—the LLM is given the ability to request actions to be executed by its harness, and the outcome of those tools is fed back into the model so it can continue to reason through and solve the given problem.

> I debated whether to specify "... a goal set by a user". I decided that's not a necessary part of this definition: we already have sub-agent patterns where another LLM sets the goal

> So long as agents lack a commonly shared definition, using the term reduces rather than increases the clarity of a conversation.

Note: here "harness" means whatever executes the tool calls the LLM requests.

---

## 5. "Designing agentic loops"

- URL: https://simonwillison.net/2025/Sep/30/designing-agentic-loops/
- Date: 30th September 2025
- Coins (as a named skill): **designing agentic loops**. Uses **YOLO mode**. Quotes Solomon Hykes's definition.

> A critical new skill to develop is designing agentic loops.

> One way to think about coding agents is that they are brute force tools for finding solutions to coding problems. If you can reduce your problem to a clear goal and a set of tools that can iterate towards that goal a coding agent can often brute force its way to an effective solution.

> My preferred definition of an LLM agent is something that runs tools in a loop to achieve a goal. The art of using them well is to carefully design the tools and loop for them to use.

Quoting Solomon Hykes:

> An AI agent is an LLM wrecking its environment in a loop.

Three named risks of unattended YOLO mode:

> 1. Bad shell commands deleting or mangling things you care about.
> 2. Exfiltration attacks where something steals files or data visible to the agent—source code or secrets held in environment variables are particularly vulnerable here.
> 3. Attacks that use your machine as a proxy to attack another target—for DDoS or to disguise the source of other hacking attacks.

> If you want to run YOLO mode anyway, you have a few options:
> 1. Run your agent in a secure sandbox that restricts the files and secrets it can access and the network connections it can make.
> 2. Use someone else's computer. ...
> 3. Take a risk! ...
>
> Most people choose option 3.

### What this source says

Agent use is a design problem: choose a clear goal, the tools, and a safe environment so the agent can brute-force toward the goal. Running unattended (YOLO) is what makes agents effective and also what makes them dangerous. A sandbox is the reasonable default.

---

## 6. "Vibe engineering"

- URL: https://simonwillison.net/2025/Oct/7/vibe-engineering/
- Date: 7th October 2025 (updated 23rd February 2026)
- Coins: **vibe engineering**. Later replaced by **agentic engineering** (his update says "coming out on top").

> I feel like vibe coding is pretty well established now as covering the fast, loose and irresponsible way of building software with AI—entirely prompt-driven, and with no attention paid to how the code actually works. This leaves us with a terminology gap: what should we call the other end of the spectrum, where seasoned professionals accelerate their work with LLMs while staying proudly and confidently accountable for the software they produce?
>
> I propose we call this vibe engineering, with my tongue only partially in my cheek.

> Update 23rd February 2026: It looks like the term "Agentic Engineering" is coming out on top for this now.

> It's also become clear to me that LLMs actively reward existing top tier software engineering practices:

(The list he gives: automated testing; planning in advance; comprehensive documentation; good version control habits; effective automation; a culture of code review; "a very weird form of management"; really good manual QA; strong research skills; ability to ship to a preview environment; an instinct for what can be outsourced; an updated sense of estimation.)

> Without tests? Your agent might claim something works without having actually tested it at all, plus any new change could break an unrelated feature without you realizing it. Test-first development is particularly effective with agents that can iterate in a loop.

> You're not just responsible for writing the code—you're researching approaches, deciding on high-level architecture, writing specifications, defining success criteria, designing agentic loops, planning QA, managing a growing army of weird digital interns who will absolutely cheat if you give them a chance, and spending so much time on code review.

> AI tools amplify existing expertise. The more skills and experience you have as a software engineer the faster and better the results you can get from working with LLMs and coding agents.

### What this source says

Willison separates accountable professional work with agents from "vibe coding" (Karpathy's original sense: not looking at the code). He lists ordinary senior-engineering practices that agents reward. Code review is among them in this October 2025 post.

---

## 7. "Writing about Agentic Engineering Patterns"

- URL: https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/
- Date: 23rd February 2026
- Defines **agentic engineering**.

> I'm using Agentic Engineering to refer to building software using coding agents—tools like Claude Code and OpenAI Codex, where the defining feature is that they can both generate and execute code—allowing them to test that code and iterate on it independently of turn-by-turn guidance from their human supervisor.

> I think of vibe coding using its original definition of coding where you pay no attention to the code at all, which today is often associated with non-programmers using LLMs to write code.

> Agentic Engineering represents the other end of the scale: professional software engineers using coding agents to improve and accelerate their work by amplifying their existing expertise.

First chapters named: "Writing code is cheap now" and "Red/green TDD".

> Writing code is cheap now talks about the central challenge of agentic engineering: the cost to churn out initial working code has dropped to almost nothing, how does that impact our existing intuitions about how we work, both individually and as a team?

---

## 8. "The Five Levels: from Spicy Autocomplete to the Dark Factory" (link post on Shapiro)

- URL: https://simonwillison.net/2026/Jan/28/the-five-levels/
- Date: 28th January 2026
- Willison's paraphrased numbering of Shapiro's levels is useful because it names a role at each level. These are Willison's words, not Shapiro's:

> 0. Spicy autocomplete, aka original GitHub Copilot or copying and pasting snippets from ChatGPT.
> 1. The coding intern, writing unimportant snippets and boilerplate with full human review.
> 2. The junior developer, pair programming with the model but still reviewing every line.
> 3. The developer. Most code is generated by AI, and you take on the role of full-time code reviewer.
> 4. The engineering team. You're more of an engineering manager or product/program/project manager. You collaborate on specs and plans, the agents do the work.
> 5. The dark software factory, like a factory run by robots where the lights are out because robots don't need to see.

His first-hand observation of an (at the time unnamed) Level-5 team:

> - Nobody reviews AI-produced code, ever. They don't even look at it.
> - The goal of the system is to prove that the system works. A huge amount of the coding agent work goes into testing and tooling and simulating related systems and running demos.
> - The role of the humans is to design that system - to find new patterns that can help the agents work more effectively and demonstrate that the software they are building is robust and effective.

> Some of them had 20+ years of experience as software developers working on systems with high reliability requirements, so they were not approaching this from a naive perspective.

> Update 7th February 2026: The demo was by StrongDM's AI team

---

## 9. "How StrongDM's AI team build serious software without even looking at the code"

- URL: https://simonwillison.net/2026/Feb/7/software-factory/
- Date: 7th February 2026
- Links Shapiro's "Dark Factory" to StrongDM. Ties StrongDM's "scenario" to **Scenario testing (Cem Kaner, 2003)**. Records Jay Taylor's DTU method. Raises cost concerns.

> Last week I hinted at a demo I had seen from a team implementing what Dan Shapiro called the Dark Factory level of AI adoption, where no human even looks at the code the coding agents are producing.

> I think the most interesting of these, without a doubt, is "Code must not be reviewed by humans". How could that possibly be a sensible strategy when we all know how prone LLMs are to making inhuman mistakes?

> I've seen many developers recently acknowledge the November 2025 inflection point, where Claude Opus 4.5 and GPT 5.2 appeared to turn the corner on how reliably a coding agent could follow instructions and take on complex coding tasks.

> This feels like the most consequential question in software development right now: how can you prove that software you are producing works if both the implementation and the tests are being written for you by coding agents?

> StrongDM's answer was inspired by Scenario testing (Cem Kaner, 2003).

> That idea of treating scenarios as holdout sets—used to evaluate the software but not stored where the coding agents can see them—is fascinating. It imitates aggressive testing by an external QA team—an expensive but highly effective way of ensuring quality in traditional software.

> security software is the last thing you would expect to be built using unreviewed LLM code!

> As I understood it the trick was effectively to dump the full public API documentation of one of those services into their agent harness and have it build an imitation of that API, as a self-contained Go binary.

Jay Taylor (DTU creator), quoted from Hacker News:

> Use the top popular publicly available reference SDK client libraries as compatibility targets, with the goal always being 100% compatibility.

On Attractor's release:

> Except the repo itself contains no code at all—just three markdown files describing the spec for the software in meticulous detail, and a note in the README that you should feed those specs into your coding agent of choice!

On roles:

> It felt like a glimpse of one potential future of software development, where software engineers move from building the code to building and then semi-monitoring the systems that build the code. The Dark Factory.

On cost:

> If these patterns really do add $20,000/month per engineer to your budget they're far less interesting to me. At that point this becomes more of a business model exercise: can you create a profitable enough line of products that you can afford the enormous overhead of developing software in this way?

> I'm particularly invested in the question of what it takes to have agents prove that their code works without needing to review every line of code they produce.

### What this source says

Willison saw StrongDM's demo in October 2025. He calls verification without review "the most consequential question in software development right now". He describes scenarios as hidden holdout sets that imitate an external QA team, and the DTU as API clones built by agents from public docs and SDKs. He questions the $1,000/day token spend. He describes the engineer's role as building and "semi-monitoring the systems that build the code".

---

## 10. Lenny's Podcast appearance (write-up)

- URL: https://simonwillison.net/2026/Apr/2/lennys-podcast/
- Date: April 2026
- Gives his own account of the dark factory's two rules and his view that the bottleneck has moved to testing.

> 12:49 The reason it's called the dark factory is there's this idea in factory automation that if your factory is so automated that you don't need any people there, you can turn the lights off.

> So there's this policy that nobody writes any code: you cannot type code into a computer. And honestly, six months ago, I thought that was crazy. And today, probably 95% of the code that I produce, I didn't type myself.

> The next rule though, is nobody reads the code. And this is the thing which StrongDM started doing last year.

Section heading: "The bottleneck has moved to testing"

> Anyone who's done any product work knows that your initial ideas are always wrong. What matters is proving them, and testing them.

---

## 11. "Codex CLI 0.128.0 adds /goal" (link post)

- URL: https://simonwillison.net/2026/Apr/30/codex-goals/
- Date: 30th April 2026

> The latest version of OpenAI's Codex CLI coding agent adds their own version of the Ralph loop: you can now set a /goal and Codex will keep on looping until it evaluates that the goal has been completed... or the configured token budget has been exhausted.

### What this source says

By April 2026 vendors were building the Ralph loop into their coding agents.

---

## 12. Quotes of Yegge and Huntley (Aug and Oct 2026)

- https://simonwillison.net/2026/Aug/4/steve-yegge/ (4th August 2026) quotes Yegge's report that "Gas Town fell apart at the seams with Opus 4.7" (full text in a-yegge.md section 9).
- https://simonwillison.net/2026/Oct/13/geoffrey-huntley/ (13th October 2026) quotes Huntley's pre-commit-hook-over-AGENTS.md passage (full text in a-huntley.md section 7).

## 13. "2026 in LLMs so far" (talk write-up)

- URL: https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/
- Date: 27 Sep 2026

> Dan Shapiro called this approach the Dark Factory, after the idea that if your factory is sufficiently automated you can turn the lights out, because you don't even need to see what's going on.

> What I found interesting about StrongDM is that they were living six months ahead of the rest of us, and they'd been exploring what it means to build software, not read the code, but still be confident that the software is of high quality. What can you do with these agents to help verify their work?

> This continued to be a huge topic for much of this year. Many of the sessions at this event have been about code review and how you can get away with this.
