# Disagreements and warnings (practitioner set B)

Where these authors disagree with each other, or warn against an approach. Quotes are verbatim; dates and URLs in `b-index.md`; context in per-author files.

---

## 1. Should the agent do TDD inside its own loop?

For:
- **Pocock** (skills README): "For automated tests, a red-green-refactor loop is critical. This is where the agent writes a failing test first, then fixes the test. This helps give the agent a consistent level of feedback that results in far better code."
- **Beck** (Jun 2025) used a system prompt: "Always follow the TDD cycle: Red → Green → Refactor".

Against:
- **Böckeler** (Aug 2026, small informal eval): "there was no clearly discernable difference based on TDD workflow versus no TDD workflow. On the contrary, more than once Opus ranked the non-TDD workflow solutions slightly higher in design and test quality." And: "I personally have stopped telling my coding agents to write tests first, let alone do TDD ... until I see evals or other strong arguments that convince me otherwise."
- Böckeler's hypothesis: "The TDD instructions actively work against such an up front design step."

Partial convergence: Pocock's current `tdd` skill drops refactoring from the loop ("**Refactoring is not part of the loop.** It belongs to the review stage"), which Beck's Tidy First prompt keeps inside the cycle.

---

## 2. One agent or many?

Warnings against multi-agent / swarms:
- **Huntley** (Jul 2025): "everyone seemed to be trying to crack on multi-agent, agent-to-agent communication and multiplexing. At this stage, it's not needed. ... consider what microservices would look like if the microservices (agents) themselves are non-deterministic—a red hot mess."
- **Beck** (Apr 2026): "Nobody wants agents. Nobody wants agent swarms." / "I’ve never been able to get two agents working on the same codebase at the same time without my head exploding." / "Multi-agent is a feature. Outcome-orientation is the thing the feature is supposed to deliver."
- **Hashimoto** (Feb 2026): "I'm not [yet?] running multiple agents, and currently don't really want to."
- **Anthropic** (Dec 2024): "we recommend finding the simplest solution possible, and only increasing complexity when needed."

For (with conditions):
- **Carlini** (Feb 2026): agent teams of 16 in parallel; but "Having 16 agents running didn't help because each was stuck solving the same task" until the work could be split with an oracle.
- **Rajasekaran** (Mar 2026): separate evaluator is worth it "when the task sits beyond what the current model does reliably solo".
- **Anthropic** (Nov 2025) leaves it open: "it’s still unclear whether a single, general-purpose coding agent performs best across contexts, or if better performance can be achieved through a multi-agent architecture."

---

## 3. Does a human need to read the code?

Humans need not review:
- **OpenAI** (Feb 2026): "Humans may review pull requests, but aren’t required to. Over time, we’ve pushed almost all review effort towards being handled agent-to-agent."
- **Lopopolo** (Mar 2026): "Once the PR carries its own proof, I do not need to watch the implementation happen." / "I am evaluating the invariant and the proof."

Humans must read / own it:
- **Böckeler** (Jul 2025): "So especially in cases with high impact and low detectability, I absolutely still care about the code." / "For me personally, the minimum I want to still care about and be on top of is the test code."
- **Ronacher** (Sep 2025): "I still review every line, shape the architecture, and carry the responsibility for how it runs in production." (Feb 2026): "Non-sentient machines will never be able to carry responsibility".
- **Ronacher** (Jun 2026): "Maybe the question is that in a future of loops, how do we don’t abdicate judgment".
- **Pocock** (dark factory entry): "The problem shows when something breaks. You do not know what changed, because nobody read the changes." and "AFK doesn't remove human review; it defers all of it to the end".
- **Carlini** (Feb 2026): "the thought of programmers deploying software they’ve never personally verified is a real concern."
- **DHH** (Jul 2025): "You cannot give someone pointers if you don’t know how to do it. ... You have to be a doer first."

---

## 4. Agent-written tests as the behaviour check

- **Böckeler** (Apr 2026): "This approach puts a lot of faith into the AI-generated tests, that's not good enough yet."
- **Carlini**: "it’s important that the task verifier is nearly perfect, otherwise Claude will solve the wrong problem." / "it is easy to see tests pass and assume the job is done, when this is rarely the case."
- **Beck** (May 2025) on test cheating: "I’ve seen truly pernicious behavior like deleting assertions from tests, deleting whole tests, & faking large swathes of implementation."
- **Anthropic** (Nov 2025) defends against it with JSON and wording: "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality."

---

## 5. How much spec up front?

- **Böckeler** (Oct 2025): "The past has shown that the best way for us to stay in control of what we’re building are small, iterative steps, so I’m very skeptical that lots of up-front spec design is a good idea, especially when it’s overly verbose." / "To be honest, I’d rather review code than all these markdown files."
- **Rajasekaran** (Mar 2026): keep the planner high-level because "if the planner tried to specify granular technical details upfront and got something wrong, the errors in the spec would cascade into the downstream implementation."
- **Lopopolo** (Mar 2026): write the spec after building: "It is easier to build the concrete thing, engage with it as a team, and distill the accepted decisions into a spec than it is to anticipate every consequential decision up front."
- **Pocock** (AFK entry) argues the opposite direction for unattended runs: "Since you can't give input during the run, give it before and after instead. Before: resolve the ambiguity up front — a grilling session, a written spec".
- **Beck** (May 2025) restricts context instead: "only telling the genie what it needs to know for the next step. I don’t give it overall context".

---

## 6. Prescribing process vs checking outcomes

- **Böckeler** (Aug 2026): "being overly specific about how we want a model to do something is not a sustainable approach. Instead, we should find as many ways as we can to monitor the outcomes and give feedback."
- **OpenAI**: "By enforcing invariants, not micromanaging implementations, we let agents ship fast without undermining the foundation."
- **Pocock** (README) on frameworks: "Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve."
- **Ronacher** (Jul 2025): "simply taking time to talk to the machine and give clear instructions outperforms elaborate pre-written prompts." Rule: "I only automate things that I do regularly."
- **Anthropic** (CC best practices): "If Claude already does something correctly without the instruction, delete it or convert it to a hook."
- **Rajasekaran**: "every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing".

---

## 7. Build for agents, or let agents use human interfaces?

- **DHH** (Feb 2026): "All the agent accommodations, like MCPs/CLIs/APIs, probably still have a place for a bit longer ... But I bet this is just a temporary crutch." / "The human affordances will be more than adequate." (His company nonetheless shipped an API, CLI and skill for agents in Mar 2026.)
- **OpenAI**: "we’ve worked to add more capabilities to the agent by making things like the application UI, logs, and app metrics themselves directly legible to Codex."
- **Pocock** (AX): "Humans tolerate tribal knowledge, slow CI, and "ask Sarah about the billing module"; agents can't."
- **Böckeler**: "Not every codebase is equally amenable to harnessing."

---

## 8. Loops/factories for lasting code

Warnings:
- **Ronacher** (Jun 2026): "When you take that behavior and you put it behind loops, you tend to amplify it. If each iteration adds another small defense, the system slowly becomes less understandable while appearing more robust. The more hands-off you are, the more that happens." Loops work for "artifacts without necessity of longevity" or "clearly verifiable mechnical translation".
- **Ronacher** (Sep 2026), after a 35-hour unsupervised factory run: "the factory has delivered absolutely nothing of value and also not taught me anything about how to operate a better one."
- **Beck** (Apr 2026): "genies naturally live down & to the left of muddling."
- **Pocock** (Ralph tips): "Agents amplify what they see. Poor code leads to poorer code." and "Ralph accelerates this."

Counter-position:
- **OpenAI**: fully agent-generated product over five months, held together by enforced architecture and garbage-collection agents — while admitting "What we don’t yet know is how architectural coherence evolves over years in a fully agent-generated system."
- **Pocock** (software factory): start narrow — "One cron job that runs one kind of session and opens one reviewable PR is a factory."

---

## 9. Merge gates and speed

- **OpenAI**: "The repository operates with minimal blocking merge gates. ... In a system where agent throughput far exceeds human attention, corrections are cheap, and waiting is expensive. This would be irresponsible in a low-throughput environment."
- **Böckeler**: "You want to have checks as far left in the path to production as possible".
- **Anthropic** (CC best practices): "If you can’t verify it, don’t ship it."
- **Beck** (Jun 2026): "Slow development to ensure that the damn stuff actually works. ... That’s how you go faster."
- **Ronacher** (Feb 2026): "When one part of the pipeline becomes dramatically faster, you need to throttle input."
- **DHH** (Aug 2026), contrasting tone: "Every idea, every hunch, every experiment is now within immediate reach."

---

## 10. Typing code and keeping competence (incl. DHH's reversal)

- **DHH** (Jul 2025): "I can literally feel competence draining out of my fingers." / "I have to do the typing myself because you learn with your fingers."
- **DHH** (Oct 2026): "it's time to put down the pencils. We're not going to write the vast majority of code by hand any longer." (The later post does not revisit the competence argument.)
- **Hashimoto** (Feb 2026) — a middle path: "you're trading off: not forming skills for the tasks you're delegating to the agent while continuing to form skills naturally in the tasks you continue to work on manually." and "The skill formation issues particularly in juniors without a strong grasp of fundamentals deeply worries me".
- **Ronacher** (Jun 2026): "What if you and your team just lose the last remaining ability to understand the code without using the machine?"

---

## 11. How much AI-written code is realistic

- **DHH** (Jan 2026): "I'm nowhere close to the claims of having agents write 90%+ of the code ... if I hold the line on quality and cohesion."
- **Ronacher** (Sep 2025): "north of 90% AI-written code" on one service, with human design and line-by-line review.
- **OpenAI** (Feb 2026): "no manually-written code" as a deliberate constraint.

---

## 12. AI-assisted contributions to open source

- **DHH** (Jun 2026): "Projects big and small have been erecting new participation barriers on contributions aided by AI to preserve the privileges of the old programmer guilds."
- **Ronacher** (Jan 2026): "Every day brings more PRs that took someone a minute to generate and take an hour to review." / "Shooting up bad code is rude because you completely disregard the time of the maintainer."

---

## 13. Hooks and deterministic automation

- **Anthropic** (CC best practices): a Stop hook "runs your check as a script and blocks the turn from ending until it passes."
- **Böckeler** (Feb 2026): hooks are context "triggered by the agent software itself, at deterministic points in time".
- **Ronacher** (Jul 2025): "I tried hard to make hooks work, but I haven’t seen any efficiency gains from them yet."

---

## 14. Is context engineering "engineering"?

- **Anthropic** (Sep 2025) treats it as a discipline: "good context engineering means finding the smallest possible set of high-signal tokens".
- **Böckeler** (Feb 2026): "In spite of the name, ultimately this is not really engineering… ... as long as LLMs are involved, we can never be certain of anything".
- **Böckeler** (Jul 2025): "once we manage to wrap them in enough scaffolding to make them predictable, we risk stripping away the very thing that makes them valuable in the first place."
