# Mitchell Hashimoto — notes

Collected 2026-10-21. Raw: `b-raw/mitchellh-adoption/page.txt`.

---

## My AI Adoption Journey

- URL: https://mitchellh.com/writing/my-ai-adoption-journey
- Date: February 5, 2026
- Author: Mitchell Hashimoto (Ghostty; co-founder of HashiCorp). Footnote disclosure: "I don't work for, invest in, or advise any AI companies."

### Verbatim

Three phases of adopting any tool:

> My experience adopting any meaningful tool is that I've necessarily gone through three phases: (1) a period of inefficiency (2) a period of adequacy, then finally (3) a period of workflow and life-altering discovery.

Six named steps (table of contents, verbatim): "Step 1: Drop the Chatbot", "Step 2: Reproduce Your Own Work", "Step 3: End-of-Day Agents", "Step 4: Outsource the Slam Dunks", "Step 5: Engineer the Harness", "Step 6: Always Have an Agent Running".

Agent definition:

> To find value, you must use an agent. An agent is the industry-adopted term for an LLM that can chat and invoke external behavior in a loop
> At a bare minimum, the agent must have the ability to: read files, execute programs, and make HTTP requests.

Step 2 method (reproduce manual commits):

> Instead of giving up, I forced myself to reproduce all my manual commits with agentic ones. I literally did the work twice. I'd do the work manually, and then I'd fight an agent to produce identical results in terms of quality and function (without it being able to see my manual solution, of course).

Lessons from Step 2:

> - Break down sessions into separate clear, actionable tasks. Don't try to "draw the owl" in one mega session.
> - For vague requests, split the work into separate planning vs. execution sessions.
> - If you give an agent a way to verify its work, it more often than not fixes its own mistakes and prevents regressions.

> The negative space here is worth reiterating: part of the efficiency gains here were understanding when not to reach for an agent.

Step 3:

> block out the last 30 minutes of every day to kick off one or more agents.

> Basically: instead of trying to do more in the time I have, try to do more in the time I don't have.

> I would NOT allow agents to respond, I just wanted reports the next day

> To be clear, I did not go as far as others went to have agents running in loops all night.

Step 4 (rule on attention):

> Very important at this stage: turn off agent desktop notifications. Context switching is very expensive. In order to remain efficient, I found that it was my job as a human to be in control of when I interrupt the agent, not the other way around.

On skill formation:

> Well, you're trading off: not forming skills for the tasks you're delegating to the agent while continuing to form skills naturally in the tasks you continue to work on manually.

Step 5 — his definition of harness engineering:

> At risk of stating the obvious: agents are much more efficient when they produce the right result the first time, or at worst produce a result that requires minimal touch-ups. The most sure-fire way to achieve this is to give the agent fast, high quality tools to automatically tell it when it is wrong.
>
> I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this "harness engineering." It is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again. I don't need to invent any new terms here; if another one exists, I'll jump on the bandwagon.

Two forms:

> Better implicit prompting (AGENTS.md). For simple things, like the agent repeatedly running the wrong commands or finding the wrong APIs, update the AGENTS.md (or equivalent).

> Each line in that file is based on a bad agent behavior, and it almost completely resolved them all.

> Actual, programmed tools. For example, scripts to take screenshots, run filtered tests, etc etc. This is usually paired with an AGENTS.md change to let it know about this existing.

Step 6:

> If an agent isn't running, I ask myself "is there something an agent could be doing for me right now?"

> I'm not [yet?] running multiple agents, and currently don't really want to.

> I'd say right now I'm maybe effective at having a background agent running 10 to 20% of a normal working day.

> I don't want to run agents for the sake of running agents.

Concern:

> The skill formation issues particularly in juniors without a strong grasp of fundamentals deeply worries me, however.

### What this source says

A staged, personal adoption path from chat to agents to a harness. Hashimoto uses "harness engineering" (Feb 5, 2026, six days before the OpenAI post) to mean: every time an agent makes a mistake, add a fix so it never repeats — either a line in AGENTS.md or a real tool (screenshot script, filtered tests). He runs one background agent, not fleets, keeps control of interruptions, and keeps doing some work by hand to keep forming skills. He presents it as measured and states he has no AI-company ties.

### Coinage

He says "I've grown to calling this 'harness engineering'" and disclaims inventing it. This is the earliest dated use of the term among sources collected here (Feb 5, 2026); OpenAI's post (Feb 11, 2026) made it a headline. Neither claims to be first.
