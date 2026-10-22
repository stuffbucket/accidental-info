# Disagreements and warnings between practitioners (set A)

Each item quotes both sides from primary sources. Talk quotes come from auto-transcripts. Dates matter: several authors changed position during 2025-2026, and those reversals are listed too.

---

## 1. Should humans read or review the code?

**No (StrongDM, Feb 2026):**
> - Code must not be written by humans
> - Code must not be reviewed by humans
(https://factory.strongdm.ai/)

> Code was treated analogously to an ML model snapshot: opaque weights whose correctness is inferred exclusively from externally observable behavior.
(https://factory.strongdm.ai/techniques)

**No, and not by line (Huntley, Oct 2026):**
> If humans eyeballing code were sufficient engineering to stop bugs, we'd never have had any defects. It didn't work at human speed. It sure as heck isn't going to work at a thousand times human speed.

> I don't trust the generation, and I don't read the code line by line, but I'm still aware of what's going on by driving queries through an agent
(https://ghuntley.com/agency/)

**Not yet, but soon no (Yegge, Aug 2026):**
> CTOs keep asking me if code review is really dead. The answer: Not Yet. But it will be by next year.
> Upshot: in the short term, yes, keep reviewing agent code.
(https://yegge.ai/essays/the-shape-of-things-to-come/)

Yegge on his own projects (Mar 2026): "the last 25% or so of pull requests need human review. ... there's still a thing called taste that current models can't be trusted with." (https://steve-yegge.medium.com/vibe-maintainer-a2273a841040). Yet of Gas Town itself (Jan 2026): "It's also 100% vibe coded. I've never seen the code, and I never care to".

**Yes, read it (Horthy, from Mar 2026, a reversal of Aug 2025):**
> So, the new advice, uh don't read the plans. Please, read the code.
> I was wrong. ... We tried not reading the code for like 6 months. Uh it did not end well. We had to rip out and replace large parts of that system.
(https://www.youtube.com/watch?v=YwZR6tc7qYg, auto-transcript)

> I'm going to posit something potentially controversial: the lights off factory does not work.
> 4. Read the dang code
(https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md)

Asked directly about StrongDM's "never have a human read either side" (Mar 2026 Q&A): "Um I do not endorse that. Let's put it that way." (auto-transcript)

**Horthy's earlier position (Aug 2025), which he later reversed:**
> I had to learn to let go of reading every line of PR code. I still read the tests pretty carefully, but the specs became our source of truth
(ace-fca.md)

**Willison's position (Feb 2026), skeptical but curious:**
> How could that possibly be a sensible strategy when we all know how prone LLMs are to making inhuman mistakes?
(https://simonwillison.net/2026/Feb/7/software-factory/)

Willison earlier counted code review among practices agents reward (Oct 2025): "A culture of code review. This one explains itself." (https://simonwillison.net/2025/Oct/7/vibe-engineering/)

---

## 2. Can a factory keep a codebase maintainable?

**Horthy: no, the models can't (Jul 2026):**
> models have a shortcoming. They can't maintain and improve codebase quality over time -- not without a decent amount of human steering.
> there is no penalty for eroding codebase maintainability
> Of course, more review agents and more tokens do help -- they raise the floor, catching the dumb stuff. But they don't move the ceiling
(wsff.md)

**Huntley: maintainability by humans is the wrong frame (Jul 2025):**
> When I hear that argument, I question "by whom"? By humans? Why are humans the frame for maintainability? Aren't we in the post-AI phase where you can just run loops to resolve/adapt when needed?
> any problem created by AI can be resolved through a different series of prompts
(https://ghuntley.com/ralph/)

Huntley later (Oct 2026) adds architectural enforcement rather than review: "I'm doing the same thing with pre-commit hooks, generating scripts that deterministically inspect the generated code. ... It's architectural enforcement, same as it ever was." (https://ghuntley.com/agency/)

**Shapiro: take on more debt, pay later with cheaper AI hours (Dec 2025):**
> You should be willing to take on more technical debt than you ever would have before⁴. Ship the prototype⁵⁶. Skip the elegant abstraction. You are borrowing expensive human hours today, and you will get to pay them back with cheap AI hours tomorrow.
(https://www.danshapiro.com/blog/2025/12/this-is-a-time-of-technical-deflation/)

Horthy's data point against this: "it feels like an agent-built codebase starts to struggle after maybe **three to six months**" and, from his own team, "my cofounder spent **two whole weeks** in VS Code (not even cursor) plumbing out all the patterns by hand." (wsff.md)

---

## 3. One loop or many agents?

**Huntley: a monolithic single loop; multi-agent is "a red hot mess" (Jul 2025, repeated Jan 2026):**
> Consider microservices and all the complexities that come with them. Now, consider what microservices would look like if the microservices (agents) themselves are non-deterministic—a red hot mess.
> Ralph is monolithic. Ralph works autonomously in a single repository as a single process that performs one task per loop.
(https://ghuntley.com/ralph/ ; repeated at https://ghuntley.com/loop/ with "I hope that folks will come back down from orbit")

> Everyone right now is going through their zany period
(https://ghuntley.com/loop/)

Huntley in Oct 2026: "People ask why I don't have supervision trees, swarms, and an orchestrator. I've built that. ... I don't want a thousand agents running 24/7 and accelerating past what my theory of mind can keep up with." (https://ghuntley.com/agency/)

**Yegge: orchestrated swarms of 20-30, and he rejects monoliths (Jan 2026, Apr 2026):**
> I've tamed them to where you can use 20–30 at once, productively, on a sustained basis.
(Gas Town)

> Claude Code and some other agents are trying to turn themselves into dark factories ... But so far, they're all trying to do it with a product lens, no platform to speak of — a monolith. ... safe to say I'm not a fan.
(https://steve-yegge.medium.com/gas-town-from-clown-show-to-v1-0-c239d9a407ec)

> You should almost never deploy a single-agent pack for a real business process. The reality is that any agent can go temporarily insane, at any time, and make a bad call.
(https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607)

(Huntley's "monolith" means a single loop/process. Yegge's "monolith" means a single-vendor product. Both use the word against the other's preferred shape.)

**Horthy on Gas Town (Mar 2026):**
> this is why I'm a little mid on agent swarms and the whole gas town thing because you still need to be able to ensure quality, and like going 10 times faster doesn't matter if you're going to throw it all away in 6 months. So, shoot for 2 to 3x.
(auto-transcript, https://www.youtube.com/watch?v=YwZR6tc7qYg)

**Huntley on factories as a corporate project (Oct 2026):**
> If companies think they're going to build a swarm or a software factory, how will they afford that talent when they're competing directly with the labs for talent? It'll be "I've heard about Kubernetes, let's do a Kubernetes project" that fails all over again.
(https://ghuntley.com/agency/)

**Yegge's own report that Gas Town failed (Aug 2026):**
> Gas Town was intended to be reusable, but I only ever wound up using it to build itself. Gas Town fell apart at the seams with Opus 4.7.
(https://yegge.ai/essays/the-shape-of-things-to-come/)
His successor (Wheelhouse) is still multi-agent ("40+ agents around the clock").

---

## 4. Throughput versus completeness

**Yegge accepts lost and duplicated work (Jan 2026):**
> Work in Gas Town can be chaotic and sloppy, which is how it got its name. Some bugs get fixed 2 or 3 times, and someone has to pick the winner. Other fixes get lost. Designs go missing and need to be redone. It doesn't matter, because you are churning forward relentlessly on huge, huge piles of work
(Gas Town)

**Horthy: no slop (2025-2026):**
> If you're writing production code that is used by users and you're going to get paged at 3:00 a.m. if it's broken, uh no slop. This is the year, 2026, no more slop.
(auto-transcript, Mar 2026)

> It is possible you are too busy trying to move 10-100x faster and trying to convince yourself code quality doesn't matter any more, when you could embrace the constraints and move 2-3x faster, safely.
(wsff.md)

---

## 5. Natural-language control flow versus code control flow

**StrongDM's Attractor: LLM-evaluated edges (Feb 2026):**
> Edges between nodes are expressed in natural language and evaluated by the LLM.
(https://factory.strongdm.ai/products/attractor)

**Horthy: use real control flow (Apr 2025; Mar 2026):**
> Factor 8: Own your control flow
(12-factor agents)
> The lesson is don't use prompts for control flow if you can use control flow for control flow. Like the if statement is really, really powerful and LLMs are really good at classifying things.
(auto-transcript, Mar 2026)

**Yegge: workflows as agent-followed molecules (Jan 2026):**
> Because AIs are really good at following TODO lists and acceptance criteria, they are reliable at following molecules.
(Gas Town)
Yegge also admits GUPP is unreliable: "Claude Code is so miserably polite that GUPP doesn't always work in practice." He adds deterministic nudges and heartbeats from cron (Aug 2026: "crons watch, models act").

---

## 6. AGENTS.md, skills, and prompt tuning versus deterministic checks

**Huntley: skill packs are astrology; use hooks (Oct 2026):**
> I swear it's astrology for software engineers. Horoscopes. Just because it's there doesn't mean it works, but it reads well and makes you feel good.
> you should probably delete your skills and your AGENTS.md every couple of months.
(https://ghuntley.com/agency/)

**HumanLayer: customise AGENTS.md first (Mar 2026):**
> Before touching any other harness configuration points, it's usually worth customizing your CLAUDE.md / AGENTS.md files.
(https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents)

**Hashimoto: AGENTS.md lines, each from a bad behaviour, "almost completely resolved them all" (Feb 2026):**
(https://mitchellh.com/writing/my-ai-adoption-journey)

**Yegge: skills are a band-aid that will age out (Aug 2026):**
> The problem with public Skills is that they enter the training data for new models and become irrelevant over time. However, I'll concede that they can be a good band-aid for today's models.
(https://yegge.ai/essays/the-shape-of-things-to-come/)

**Horthy: also warns about markdown proliferation (Nov 2025):**
> Watch out for tools that just spew out a bunch of markdown files just to make you feel good.
(auto-transcript)

---

## 7. Reusable harnesses / frameworks

**Yegge (Aug 2026):**
> I have given up on building reusable harnesses. Indeed I believe harnesses will all soon be bespoke, and the people trying to sell you one will all soon be bebroke.

**Horthy/HumanLayer is building one (Jul 2026):**
> We're building towards two ideas: "building blocks for your software factory" and "better verifiers for software maintainability"
(wsff.md); HumanLayer: "The future of software factories must be open and composable" (resources page).

**Huntley: harnesses are fungible (Oct 2026):**
> Codex, OpenCode, T3 Code, Pi: they're all fungible. What matters is how you get your tokens, and getting them cheaply.

---

## 8. Ralph: what it is for

**Huntley: greenfield only (Jul 2025):**
> "There's no way in heck would I use Ralph in an existing code base"

**Horthy runs Ralph-style loops on an existing codebase, nightly and small (Jan 2026):**
> for existing codebases, make the change set manageable - we have since set up any ralph-ish desired state loops to once ONCE on a cron overnight, and merge small iterations over time.

**Horthy on the Anthropic plugin's reading of Ralph (Jan 2026):**
> it misses the key point of ralph which is not "run forever" but in "carve off small bits of work into independent context windows".

**Horthy on exploratory work:**
> if you are iterating/exploring, you probably don't want ralph in the first place
(https://www.humanlayer.dev/blog/brief-history-of-ralph)

Huntley, by contrast, calls Ralph "GENERIC and can be used for ALL TASKS" (https://ghuntley.com/loop/).

---

## 9. Model choice

**Huntley: pick one and lock in (Oct 2026):**
> Pick a model that works and lock in. Don't change every week.

**Horthy agrees (Nov 2025):** "Pick one tool and get some reps. I recommend against minmaxing across cloud and codeex and all these different tools." (auto-transcript)

**StrongDM and Yegge route roles to different models.** StrongDM's Weather Report assigns a model per role and plans by "consensus(opus-5.5, gpt-5.6-sol)". Yegge: "Every implementation bead goes through this lifecycle: Fable design, Opus implementation, Fable review."

---

## 10. Spec-driven development

**Horthy (Nov 2025):** "specri development is broken. Not the idea, but the phrase." (auto-transcript). (Mar 2026), on treating code like assembly: "I do not endorse that."

**StrongDM:** the spec ("seed") plus holdout scenarios is the whole input. "Spec + Test Suite = Complete Intent".

**Shapiro (Level 5):** "a black box that turns specs into software."

**Huntley:** specs plus a type-strong language are the core of Ralph. But his own failure was a bad spec: "my specification for the lexer defined a keyword twice for two opposing scenarios, which resulted in a lot of time wasted."

**Horthy's own Ralph spec failure (Jan 2026):** "I didn't really read the specs, and I didn't read the code. The output sucked. I went back to read the specs and they were way off base."

---

## 11. Who coined what (attribution disputes)

- Context engineering: HumanLayer says "We introduced the term". Willison's June 2025 account credits Tobi Lutke and Karpathy and does not mention HumanLayer.
- Harness engineering: HumanLayer says "coined by Viv". Hashimoto used it on Feb 5, 2026, before Viv's Feb 17 post. Horthy himself used it in Nov 2025.
- Lights-off factory: Horthy says "Dan Shapiro coined this term". Shapiro's text says "Dark Factory".
