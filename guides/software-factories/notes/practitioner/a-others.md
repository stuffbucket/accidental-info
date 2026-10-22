# Other practitioners cited as term origins

These authors are included only because the main sources (HumanLayer, Huntley) cite them as the origin of a term. Each is quoted from their own page.

---

## Moss: "Don't waste your back pressure"

- URL: https://banay.me/dont-waste-your-backpressure/
- Date: Sat, Jan 17, 2026
- Cited by Huntley (https://ghuntley.com/pressure/, 17 Jan 2026) as the write-up of their conversation. Huntley had used "back pressure" for agent loops since July 2025 (https://ghuntley.com/ralph/). Full quotes are in a-huntley.md section 3.

---

## Mitchell Hashimoto: "My AI Adoption Journey"

- URL: https://mitchellh.com/writing/my-ai-adoption-journey
- Date: February 5, 2026
- Cited by HumanLayer (Kyle Mistele, "Skill Issue", Mar 12, 2026) for the definition of **harness engineering**. Hashimoto does not claim to have coined it.

> Step 5: Engineer the Harness

> At risk of stating the obvious: agents are much more efficient when they produce the right result the first time, or at worst produce a result that requires minimal touch-ups. The most sure-fire way to achieve this is to give the agent fast, high quality tools to automatically tell it when it is wrong.

> I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this "harness engineering." It is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again. I don't need to invent any new terms here; if another one exists, I'll jump on the bandwagon.

> 1. Better implicit prompting (AGENTS.md). For simple things, like the agent repeatedly running the wrong commands or finding the wrong APIs, update the AGENTS.md (or equivalent). ... Each line in that file is based on a bad agent behavior, and it almost completely resolved them all.
> 2. Actual, programmed tools. For example, scripts to take screenshots, run filtered tests, etc etc.

> I'm not [yet?] running multiple agents, and currently don't really want to.

### What this source says

Hashimoto's "harness engineering" is the same practice as Huntley's "signs" in Ralph: each observed agent mistake becomes a permanent fix, either an AGENTS.md line or a tool that tells the agent when it is wrong.

---

## Vivek Trivedy (LangChain): harness engineering posts

- "Improving Deep Agents with Harness Engineering", https://www.vtrivedy.com/posts/improving-deep-agents-with-harness-engineering, 17 Feb, 2026
- "The Anatomy of an Agent Harness", https://www.vtrivedy.com/posts/the-anatomy-of-an-agent-harness, 10 Mar, 2026 (also on the LangChain blog)
- HumanLayer says "Harness engineering, coined by Viv". His posts here are dated after Hashimoto's Feb 5, 2026 use. Horthy also said "you can call this harness harness engineering" in his Nov 2025 talk (auto-transcript). The coinage is unresolved.

> TLDR: Agent = Model + Harness. Harness engineering is how we build systems around models to turn them into work engines. The model contains the intelligence and the harness makes that intelligence useful.

> If you're not the model, you're the harness.

> A harness is every piece of code, configuration, and execution logic that isn't the model itself. A raw model is not an agent. But it becomes one when a harness gives it things like state, tool execution, feedback loops, and enforceable constraints.

> The goal of a harness is to mold the inherently spiky intelligence of a model for tasks we care about. Harness Engineering is about systems, you're building tooling around the model to optimize goals like task performance, token efficiency, latency, etc. Design decisions include the system prompt, tool choice, and execution flow.

> Part of harness engineering is building a good delivery mechanism for context engineering.

Measured claim (primary, with method named):

> TLDR: Our coding agent went from Top 30 to Top 5 on Terminal Bench 2.0. We only changed the harness. Here's our approach to harness engineering (teaser: self-verification & tracing help a lot).

---

## Not fetched (cited by the main sources as origins; follow-up needed)

- Sean Grove (OpenAI), "Specs are the new code" talk, AI Engineer World's Fair 2025. Horthy cites it as the origin of the spec-as-source idea.
- OpenAI, "Harness engineering" (Ryan Lopopolo), https://openai.com/index/harness-engineering/, Feb 2026. The fetch was blocked. Horthy and HumanLayer cite it. HumanLayer reads it as "configuring everything outside of the agent's runtime ... more focused on back-pressure and verification".
- Luke PM, "The Software Factory", https://lukepm.com/blog/the-software-factory/ (cited by StrongDM).
- Jake Nations (Netflix), "do not outsource the thinking", https://www.arthropod.software/p/vibe-coding-our-way-to-disaster (cited by Horthy).
- Martin Fowler, "semantic diffusion" (2006), cited by Horthy.
- Cem Kaner, "scenario testing" (2003), cited by Willison as the origin of StrongDM's "scenario".
