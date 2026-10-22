# DHH (David Heinemeier Hansson) — notes

Collected 2026-10-21. Blog: https://world.hey.com/dhh. Raw: `b-raw/dhh-*/page.txt`. DHH created Ruby on Rails; co-owner/CTO of 37signals.

His position moved sharply between July 2025 and October 2026. Sources below are in date order so the shift is visible. He is the counterweight voice through mid-2025 and becomes an advocate by late 2026, while keeping a quality bar he says is far from "90%+" claims as of January 2026.

---

## 1. Lex Fridman Podcast #474 — "DHH: Future of Programming, AI, Ruby on Rails, Productivity & Parenting"

- URL (transcript): https://lexfridman.com/dhh-david-heinemeier-hansson-transcript/
- Date: July 2025 (DHH's Jan 2026 post refers to it as "the Lex Fridman podcast last summer")
- Raw: `b-raw/dhh-lex-transcript/page.txt` (speaker labels checked; all quotes below are DHH's turns, sections "Future of programming" and "Vibe coding")

### Verbatim

How he used AI then:

> Now, I actually love collaborating with AI too. I love chiseling my code, and the way I use AI is in a separate window. I don’t let it drive my code. I’ve tried that. I’ve tried the Cursors and the Windsurfs and I don’t enjoy that way of writing.

Competence and typing:

> One of the reasons I don’t enjoy that way of writing is, I can literally feel competence draining out of my fingers. That level of immediacy with the material disappears.

> But what I found myself doing was asking AI for the same way of expressing a conditional, for example, in Bash over and over again. That by not typing it, I wasn’t learning it. I was using it, I was getting the expression I wanted, but I wasn’t learning it. I got a little scared.

> It’s such a better experience as a programmer to look up APIs, to get a second opinion on something, to do a draft, but I have to do the typing myself because you learn with your fingers.

On Claude Code then:

> When I use Claude’s Code, the terminal version of Claude … which is actually my preferred way of using it, I get too impatient. ... But I think the more crucial aspect for me is, I really care about the competence. I’ve seen what happens to even great programmers the moment they put away the keyboard

What he keeps human, and why:

> This is not just about outcomes. This is what’s crucial to understand, programming for programmers who like to code is not just about the programs they get out of it. That may be the economic value. It’s not the only human value. The human value is just as much in the expression.

> If I elevate, if I promote myself out of programming, I turn myself into a project manager, a project manager of a murder of AI crows, as I wrote the other day.

> I’ve done some vibe coding where I didn’t care that I wasn’t playing myself. I just wanted to see something that was an idea in my head.

> I don’t actually use it very much for Ruby code. I’m occasionally impressed whenever I try it ... And then I’ll ask two more questions and I go like, oh yeah, okay, if you were my junior programmer I’d start tapping my fingers and going like, you’ve got to shape up.

On vibe coding and learning:

> You’re going to learn in this superficial way that feels like learning but is completely empty calories, and secondly, if you can just vibe code it, you’re not a programmer.

On "editor" roles (reviewing without doing):

> That’s the dream of the prompt engineer. I think it’s complete pipe dream. I don’t think editors exist that aren’t good at writing. ... You cannot give someone pointers if you don’t know how to do it. ... The capacity to be a good editor is the reward you get from being a good doer. You have to be a doer first.

On vibe coding real systems:

> The vibe coding is able to build a veneer at the current present moment of something that looks like it works, but it’s flawed in all sorts of ways. ... its capacity to get lost in its own Labyrinth is very great right now. You let it code something and then you want to change something and it becomes a game of Whack-A-Mole real quick.

### What this source says

Mid-2025 DHH uses AI daily as a lookup tool, second opinion, and drafter in a separate window, but types his own code. Reasons: competence is learned and kept "with your fingers"; programming has value as expression, not only output; reviewers ("editors") must be doers first; vibe-coded systems become whack-a-mole when changed. Delegating everything would make him "a project manager of a murder of AI crows".

---

## 2. Promoting AI agents

- URL: https://world.hey.com/dhh/promoting-ai-agents-3ee04945
- Date: January 7, 2026

### Verbatim

> At the end of last year, AI agents really came alive for me. Partly because the models got better, but more so because we gave them the tools to take their capacity beyond pure reasoning. Now coding agents are controlling the terminal, running tests to validate their work, searching the web for documentation, and using web services with skills we taught them in plain English.

> See, I never really cared much for the in-editor experience of having AI autocomplete your code as you were writing it. ... When I code, I want to finish my own thoughts and sentences. That was the sentiment I expressed on the Lex Fridman podcast last summer.

> But with these autonomous agents, the experience is very different. It's more like working on a team and less like working with an overly-zealous pair programmer who can't stop stealing the keyboard to complete the code you were in the middle of writing. With a team of agents, they're doing their work autonomously, and I just review the final outcome, offer guidance when asked

> Yes, I'm ready to give the current crop of AI agents a promotion. ... They're fully capable of producing production-grade contributions to real-life code bases.

> Yet pure vibe coding remains an aspirational dream for professional work for me, for now. Supervised collaboration, though, is here today.

> I'm nowhere close to the claims of having agents write 90%+ of the code, as I see some boast about online. I don't know what code they're writing to hit those rates, but that's way off what I'm able to achieve, if I hold the line on quality and cohesion.

> The hype drones on relentlessly, the most fantastical claims are still far off from being substantiated

### What this source says

The shift: his objection was to in-editor autocomplete interrupting his own thinking; autonomous terminal agents (tools, tests, skills) feel like a team whose output he reviews. He calls it "supervised collaboration", not vibe coding, and says 90%+ AI-written is far beyond what he gets while holding quality and cohesion.

---

## 3. Clankers with claws

- URL: https://world.hey.com/dhh/clankers-with-claws-9f86fa71
- Date: February 5, 2026

### Verbatim

> I set up mine on a Proxmox virtual machine to be fully isolated from my personal data and logins.

> I didn't install any skills, any MCPs, or give it access to any APIs. Zero machine accommodations.

> All the agent accommodations, like MCPs/CLIs/APIs, probably still have a place for a bit longer, as doing all this work cold is both a bit slow and token-intensive. But I bet this is just a temporary crutch.

> if I was going to skate to where the puck is going to be, it'd be a world where agents, like self-driving cars, don't need special equipment, like LIDAR or MCPs, to interact with the environment. The human affordances will be more than adequate.

### What this source says

A personal-agent (OpenClaw) experiment run in an isolated VM. He predicts agents will use human interfaces directly and machine-specific accommodations are temporary. (Contrast: OpenAI and Böckeler invest in agent legibility; see disagreements.)

---

## 4. Basecamp becomes agent accessible

- URL: https://world.hey.com/dhh/basecamp-becomes-agent-accessible-3ae6b949
- Date: March 25, 2026

### Verbatim

> In the past 18 months, we've experimented with a ton of AI-infused features at 37signals. ... But as Microsoft and many others have realized, it's not that easy to make something that's actually good and would welcomed by users. So we didn't ship.

> In the meantime, agents have emerged has the killer app for AI. Not only are LLMs much smarter when they can check their thinking using tools, but the file system also gives them the memory implant they needed to learn between prompts.

> We've revamped our API, created a brand-new CLI, and wrapped it all in a skill to teach agents how best to use it all.

### What this source says

37signals shipped agent access (API, CLI, skill) rather than in-app AI features. Agents are "the killer app" because tools let them check their work and the file system gives them memory.

---

## 5. Let the agents democratize open source

- URL: https://world.hey.com/dhh/let-the-agents-democratize-open-source-9fd630a9
- Date: June 1, 2026

### Verbatim

> Projects big and small have been erecting new participation barriers on contributions aided by AI to preserve the privileges of the old programmer guilds.

> Humans have been writing shitty software, with dodgy attribution and plenty of bugs, since five minutes after the profession materialized. Agents aren't perfect, slop is a problem, but giving more people the power to enjoy malleable computers is undoubtedly a huge win for the founding vision of open source.

### What this source says

Argues against projects that bar AI-assisted contributions; acknowledges slop but calls the barriers protectionist. (Contrast: Ronacher on maintainer burden.)

---

## 6. Endless execution

- URL: https://world.hey.com/dhh/endless-execution-4157e065
- Date: August 9, 2026

### Verbatim

> The age of agents has brought us endless execution. Every idea, every hunch, every experiment is now within immediate reach.

> Now I could write at length about all the caveats. All the potential dangers. All the ways it's not quite there yet. But it would be an insult to the marvel of this moment.

### What this source says

Enthusiasm piece; explicitly sets caveats aside. Low technical content; included to document the shift.

---

## 7. Over my dead pencil

- URL: https://world.hey.com/dhh/over-my-dead-pencil-fb0f3647
- Date: October 6, 2026 (refers to his Rails World keynote "two weeks ago", i.e. late September 2026)

### Verbatim

> Two weeks ago at Rails World, I told my fellow programmers that it's time to put down the pencils. We're not going to write the vast majority of code by hand any longer. Coding agents have gotten so good that it's simply not an economically viable enterprise going forward to have humans typing out lines of Ruby, Rust, or C++.

> When I polled the room for how many people were still writing a material amount of code by hand on a weekly basis, only a handful put up their hands.

> But this isn't just another technology, because AI isn't just another tool. It's far more like gaining some new coworkers who are exceptionally good and fast at a wide range of tasks, but still need a bit of help with some, and whose choices you might occasionally disagree with.

> It's fine to be skeptical about the areas where our new clanker colleagues still occasionally get it wrong, but refusing collaboration is not a viable career path for almost anyone.

### What this source says

Full reversal of the July 2025 "type it yourself" stance on economic grounds: hand-typing most code is no longer viable. Agents are framed as coworkers who need help and whose choices you sometimes overrule. He does not, in this post, address his earlier competence-and-learning argument.

---

## 8. Redundancy is the engine of progress

- URL: https://world.hey.com/dhh/redundancy-is-the-engine-of-progress-76499402
- Date: October 7, 2026

### Verbatim

> With the price of software creation cratering, we're likely to see an unprecedented bloom in apps and services. There's still so much paperwork and other white-collar toil we could automate, and we'll still need agent wranglers to do the work.

> What is entirely possible, however, is that some companies won't need as many programmers as they did before, while others will hire their first programmers or staff up dramatically.

### What this source says

Labor-market framing: "agent wranglers" as the role; expects redistribution of programming jobs.

---

## Not used

- "I'm sorry, Dave" (July 27, 2026) — about a model refusing a translation and open-weight models; political, not about building software. Raw saved.
- "The malleable computer" (April 15, 2026) — end users modifying open-source/Linux with AI. Raw saved.
