# Lineage sources for coined terms (Huntley, Shapiro) — notes

These authors were not on the assigned list, but the assigned authors cite them as the origin of two terms ("Ralph", "dark factory"/levels to "software factory"). Kept short; only what is needed to attribute the terms. Raw: `b-raw/ghuntley-ralph/`, `b-raw/shapiro-five-levels/`.

---

## Geoffrey Huntley — Ralph Wiggum as a "software engineer"

- URL: https://ghuntley.com/ralph/
- Date: 14 Jul 2025 (from page `<time datetime="2025-07-14">`)
- Cited as the origin of "Ralph" by Pocock (links this URL), Anthropic (harness-design post: "the 'Ralph Wiggum' method"), Carlini ("Ralph-loop"), OpenAI ("Ralph Wiggum Loop", linking https://ghuntley.com/loop/), Kief Morris (footnote).

### Verbatim

> Ralph is a technique. In its purest form, Ralph is a Bash loop.
>
> while :; do cat PROMPT.md | claude-code ; done

> That's the beauty of Ralph - the technique is deterministically bad in an undeterministic world.

> Building software with Ralph requires a great deal of faith and a belief in eventual consistency. Ralph will test you. Every time Ralph has taken a wrong direction in making CURSED, I haven't blamed the tools; instead, I've looked inside. Each time Ralph does something bad, Ralph gets tuned - like a guitar.

> It begins with no playground, and Ralph is given instructions to construct one.
> Ralph is very good at making playgrounds, but he comes home bruised because he fell off the slide, so one then tunes Ralph by adding a sign next to the slide saying “SLIDE DOWN, DON’T JUMP, LOOK AROUND,” and Ralph is more likely to look and see the sign.

> There is no such thing as a perfect prompt.

> When CURSED is being built, I'm sitting there watching the stream, looking for patterns of bad behaviour—opportunities to tune Ralph.

Against multi-agent:

> While I was in SFO, everyone seemed to be trying to crack on multi-agent, agent-to-agent communication and multiplexing. At this stage, it's not needed. ... Now, consider what microservices would look like if the microservices (agents) themselves are non-deterministic—a red hot mess.

> Ralph is monolithic. Ralph works autonomously in a single repository as a single process that performs one task per loop.

> To get good outcomes with Ralph, you need to ask Ralph to do one thing per loop. Only one thing. ... you also need to trust Ralph to decide what's the most important thing to implement. This is full hands-off vibe coding that will test the bounds of what you consider "responsible engineering".

Specs:

> Specs are formed through a conversation with the agent at the beginning phase of a project. Instead of asking the agent to implement the project, what you want to do is have a long conversation with the LLM about your requirements for what you're about to implement. Once your agent has a decent understanding of the task to be done, it's at that point that you issue a prompt to write the specifications out, one per file, in the specifications folder.

> The items that you want to allocate to the stack every loop are your plan ("@fix_plan.md") and your specifications.

> One item per loop. I need to repeat myself here—one item per loop.

> Your primary context window should operate as a scheduler, scheduling other subagents to perform expensive allocation-type work

### What this source says

Coins "Ralph" (July 2025): one prompt file fed to a coding agent in an infinite bash loop; one item per loop; the agent picks the most important item from a fix plan; specs (one per file, written after a requirements conversation) and the plan are loaded every iteration; the main context acts as a scheduler for sub-agents. The operator watches and "tunes" the prompt after each bad behaviour (Kief Morris's footnote makes this point: as originally described the operator steers). Unsupported ROI claims in the post are in the hype file.

---

## Dan Shapiro — The Five Levels: from Spicy Autocomplete to the Dark Factory

- URL: https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/
- Date: 2026-01-23 (page `datetime`)
- Relevance: earliest dated use found here of "dark factory" for software; Pocock's later (2026-09-24) "dark factory" entry uses the same "lights-out factory" origin. Pocock does not cite Shapiro.

### Verbatim

> I’ve now seen dozens of companies struggling to put AI to work writing code, and each one has moved through five clear tiers of automation.

> Level Zero is your parents’ Volvo ... the code is unmistakably yours.
> At Level 1, you’ve got lanekeeping and cruise control. ... you offload specific, discrete tasks to your AI intern.
> At Level 2, you’ve got Autopilot on the highway. ... You are pairing with the AI like a colleague. ... But here is the danger: level 2, and every level after it, feels like you are done. But you are not done.
> Level 3 is a Waymo with a safety driver. ... You are the human in the loop. ... You spend your days reviewing code. So much code. Your life is diffs.
> Level 4 is a robotaxi ... You write a spec. You argue with it about the spec. You craft skills ... You review plans. Then you leave for 12 hours, and check to see if the tests pass.
> At level 5, it’s not really a car any more. ... It’s a black box that turns specs into software.

> Why Dark? Maybe you’ve heard of the Fanuc Dark Factory, the robot factory staffed by robots. It’s dark, because it’s a place where humans are neither needed nor welcome.

### What this source says

A five-level maturity ladder modelled on driving automation, ending at a "dark factory" that turns specs into software with no humans. The claim that "90% of 'AI-native' developers" are at level 2 has no method (hype file).
