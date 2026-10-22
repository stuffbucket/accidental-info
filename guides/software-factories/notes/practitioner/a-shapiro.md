# Dan Shapiro: primary-source notes

Author: Dan Shapiro (danshapiro.com). He calls himself "not a professional developer – I'm a marginally competent dabbler at best" (Dec 2025 post).

---

## 1. "The Five Levels: from Spicy Autocomplete to the Dark Factory"

- URL: https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/
- Date: January 23, 2026
- Note: the URL slug says "software-factory" but the page title says "Dark Factory". StrongDM cites it as "Five Levels from Spicy Autocomplete to the Software Factory".
- Coins: the **five levels** of AI-assisted coding (modelled on the 2013 NHTSA driving-automation levels), **dark factory** as Level 5 for software ("spicy autocomplete" is in the title). Horthy attributes "lights-off software factory" to this post, but the post itself uses "Dark Factory", not "lights-off".

Framing:

> I've now seen dozens of companies struggling to put AI to work writing code, and each one has moved through five clear tiers of automation. That felt familiar, and I realized that the federal government had been there first – but for cars.

> In 2013, the NHTSA created the five levels of driving automation¹. This was helpful, because while the highest level at the time was only level 2², it let everyone have a common language for both where things were, and where things were going.

The levels (verbatim):

> Level Zero is your parents' Volvo, maybe with an automatic transmission. Whether it's vi or Visual Studio, not a character hits the disk without your approval. You might use AI as a search engine on steroids or occasionally hit tab to accept a suggestion, but the code is unmistakably yours. This is manual labor in a deflationary world.

> At Level 1, you've got lanekeeping and cruise control. You're writing the important stuff, but you offload specific, discrete tasks to your AI intern. "Write a unit test for this." "Add a docstring." You could be using anything from copy-paste ChatGPT to Copilot. You're seeing speedups, but your job is unchanged. You're still moving at the rate you type.

> At Level 2, you've got Autopilot on the highway. As a coder, you feel free. You've got a junior buddy to hand off all your boring stuff to. This is where 90% of "AI-native" developers are living right now. You are pairing with the AI like a colleague. You get into a flow state; you're more productive than you've ever been. You're not using chat, you're getting real mileage out of an AI-native coding tool. But here is the danger: level 2, and every level after it, feels like you are done. But you are not done.

> Level 3 is a Waymo with a safety driver. You're not a senior developer anymore; that's your AI's job. You are… a manager. You are the human in the loop. Your coding agent is always running multiple tabs. You spend your days reviewing code. So much code. Your life is diffs. For many people, this feels like things got worse.
>
> And almost everyone tops out here.

> Level 4 is a robotaxi, and while it's driving, you can do something else. You're not a developer. You're not a development manager either. You've now become that which you loathed: you're a PM³. You write a spec. You argue with it about the spec. You craft skills (for Claude Code, because most folks at level 4 seem to find their way to Claude Code). You plan schedules. You review plans. Then you leave for 12 hours, and check to see if the tests pass.
>
> I'm here.

> At level 5, it's not really a car any more. You're not really running anybody else's software any more. And your software process isn't really a software process any more. It's a black box that turns specs into software.

> Why Dark? Maybe you've heard of the Fanuc Dark Factory, the robot factory staffed by robots. It's dark, because it's a place where humans are neither needed nor welcome.

> I know a handful of people who are doing this. They're small teams, less than five people. And what they're doing is nearly unbelievable – and it will likely be our future.

Footnote 3:

> Program manager? Project manager? Product manager? Yes.

Acknowledged readers include Jesse Vincent (Superpowers), whom StrongDM also cites.

### What this source says

Shapiro maps AI coding onto the NHTSA driving-automation levels. Level 0 is manual. Level 1 hands off discrete tasks. Level 2 is pairing; he says "90% of 'AI-native' developers" are there, though the number is his impression. Level 3: the human becomes a manager who reviews diffs, and "almost everyone tops out here". Level 4: the human is a PM who writes specs and skills, reviews plans, and leaves while the agent works; Shapiro places himself here. Level 5 is the "dark factory", a black box that turns specs into software with no humans in the process. He says only a handful of teams of fewer than five people do this, and gives no evidence of outcomes. The roles change from developer to manager (L3) to PM (L4) to none (L5). His stated failure mode is that every level from 2 up "feels like you are done".

---

## 2. "This is a Time of Technical Deflation"

- URL: https://www.danshapiro.com/blog/2025/12/this-is-a-time-of-technical-deflation/
- Date: December 17, 2025
- Coins: **technical deflation** (credits Ward Cunningham, 1992, for "technical debt").

> Day over day, year over year, AI is driving down the cost of writing code. Economists have a word for what happens when stuff keeps getting cheaper: deflation. And you do things differently during deflation.

> But technical debt is different: you don't owe money, you owe work. And the cost of work is what's deflating.

> This leads to a surprising conclusion for anyone managing a roadmap. You should be willing to take on more technical debt than you ever would have before⁴. Ship the prototype⁵⁶. Skip the elegant abstraction. You are borrowing expensive human hours today, and you will get to pay them back with cheap AI hours tomorrow.

> In this new world, procrastination reduces the price of perfection. Adjust your spending accordingly.

Caveats in his own footnotes (attributed by him to others):

> Deepti Srivastava points out that in an increasing number of cases, you can declare code bankruptcy at very low cost. ... now it might be as simple as 'fix spec, regenerate code'.

> Michael Natkin points out that this only addresses one of the two issues of 'shipping the prototype'. The other one is that sometimes the prototype is just bad.

> And Kurt Leafstrand points out that different types of tech debt are getting cheaper at different rates – it's harder to pay down a badly architected data model than a badly

(The footnote is cut off on the page as fetched.)

### What this source says

Because code is getting cheaper to write, Shapiro argues teams should take on more technical debt now and pay it back later with cheaper AI hours. He also says existing debt that slows a team down should be fixed now. His footnotes note that bad data models and bad prototypes do not get cheaper at the same rate. This conflicts directly with Horthy's July 2026 finding that agents degrade maintainability and the codebase becomes the bottleneck (see a-disagreements.md).
