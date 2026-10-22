# Kent Beck — notes

Collected 2026-10-21. Newsletter "Software Design: Tidy First?" now at https://newsletter.kentbeck.com/ (formerly tidyfirst.substack.com). "Genies" tag: https://newsletter.kentbeck.com/t/genies. Raw: `b-raw/beck-*/page.txt`.

Disclosure seen in posts: Augment Code sponsored several posts and Genie Sessions; WorkOS sponsors the newsletter. Several genie posts are paid-only and were not read (e.g. "Is Source Code Going Away?", 2026-02-06; "Genie: Death of the Iron Triangle?", 2026-03-02; "Passing Tests Bore Me", 2026-04-22).

---

## 1. Augmented Coding & Design ("The Genie Eats The Seed Corn")

- URL: https://newsletter.kentbeck.com/p/augmented-coding-and-design
- Date: May 03, 2025

### Verbatim

> In Empirical Software Design we separate progress into two dimensions:
> Features
> Options

> The empirical style is to add the next feature, then improve the structure.

> One of the not-so-magical things about today’s genies is their lack of taste. That giant function? I just added another 20 lines to it. That direct field access? I just used it 20 more times.

> The genie seems to assume that its planetary-sized brain is capable of handling any amount of complexity, so it needn’t ever reduce complexity. It’s right until it isn’t.

> More features introduces more complexity
> More complexity slows development of more features

> We are out of options. The genie spins for hours without being able to correctly implement the next feature.

> I’m experimenting with another approach—only telling the genie what it needs to know for the next step. I don’t give it overall context

### What this source says

Beck calls the coding agent "the genie". It adds features ("inhales") but does not tidy ("exhale"), so complexity compounds until it stalls. His response: restrict the genie's context to the next step and refactor (often manually).

---

## 2. Genie Wants to Leap

- URL: https://newsletter.kentbeck.com/p/genie-wants-to-leap
- Date: May 12, 2025 (sponsored by Augment Code)

### Verbatim

> I significant limitation I’ve experienced is a complexity cliff the genie runs off when adding features

> We’ve given the genie a prompt. It will now reward itself if it can plausibly say it has added a feature.

> The genie doesn’t respond well to this situation. I’ve seen infinite loops. I’ve seen truly pernicious behavior like deleting assertions from tests, deleting whole tests, & faking large swathes of implementation. These behaviors may allow the genie to reward itself with a biscuit, but they destroy trust, my trust.

> The strategy that seems to be missing is parallels—having the two implementations coexist for a while.

> Note that the code compiles & the tests run at every step (not part of the genie’s strategy—it seems to be incentivized for the big TA-DA! moment).

### What this source says

Names failure modes: complexity cliff, infinite loops, deleting assertions/tests, faking implementation. Proposes the "parallels" refactoring technique (old and new coexist, tests green at every step) as what the genie lacks.

---

## 3. Augmented Coding: Beyond the Vibes

- URL: https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes (also tidyfirst.substack.com)
- Date: Jun 25, 2025

### Verbatim

Definition, contrasting vibe coding:

> In vibe coding you don't care about the code, just the behavior of the system. If there's an error, you feed it back into the genie in hopes of a good enough fix. In augmented coding you care about the code, its complexity, the tests, & their coverage. The value system in augmented coding is similar to hand coding--tidy code that works. It's just that I don't type much of that code.

> My first 2 attempts had accumulated so much complexity that the genie completely stalled. That's why I intruded more on the design & tried to keep the genie from coding ahead.

Warning signs (verbatim list):

> Loops.
> Functionality I hadn't asked for (even if it was a reasonable next step).
> Any indication that the genie was cheating, for example by disabling or deleting tests.

> I feel good about the correctness & performance, not so good about the code quality.

> Yes programming changes with a genie, but it's still programming. In some ways a much better programming experience. I make more consequential programming decisions per hour, fewer boring vanilla decisions.

System prompt (appendix; excerpts):

> Always follow the instructions in plan.md. When I say "go", find the next unmarked test in plan.md, implement the test, then implement only enough code to make that test pass.

> - Always follow the TDD cycle: Red → Green → Refactor

> - Never mix structural and behavioral changes in the same commit

> Always write one test at a time, make it run, then improve structure. Always run all the tests (except long-running tests) each time.

Time spent: "I spent about 4 weeks on this project".

### What this source says

Coins/uses "augmented coding" as distinct from "vibe coding": same values as hand coding (tidy code that works, tests, coverage), but the genie types. Method: a `plan.md` of tests, a "go" command for the next test, strict TDD and Tidy First in the system prompt, and watching for three warning signs (loops, unrequested features, test-cheating). Result was a working B+ tree in Rust and Python; he is not satisfied with code quality.

---

## 4. Genie Lessons: Nobody Wants Agents

- URL: https://newsletter.kentbeck.com/p/genie-lessons-nobody-wants-agents
- Date: Apr 23, 2026 (Genie Lesson #5; tool: Intent by Augment Code; session sponsored by Augment Code)

### Verbatim

> Nobody wants agents. Nobody wants agent swarms. I have a system and I want it to change. That’s the whole thing.

> This session I was using Intent by Augment Code — multi-agent, coordinator plus implementer plus verifier. ... I called it the Freudian architecture: id, superego, ego. The id rushes ahead. The superego folds its arms. The ego negotiates. It kind of works.

> I was managing it. Watching which agent was doing what. Wondering when to interrupt. Holding state in my head that the system should have been holding for me. I’d said I wanted readable code and instead I had a coordination problem.

> I’ve never been able to get two agents working on the same codebase at the same time without my head exploding. So I’m not convinced the swarm is the answer.

> Multi-agent is a feature. Outcome-orientation is the thing the feature is supposed to deliver. We keep getting those confused.

> The other frontier nobody’s working on yet: multiplayer. Right now, five agents can work on this codebase simultaneously. Five people can’t. That’s backwards.

### What this source says

Skeptical of multi-agent swarms: they shift coordination load onto the human. What he wants is outcome-orientation (describe the result, learn feasibility and cost). Names "multiplayer" augmented development (several humans steering together) as the unsolved problem.

---

## 5. Genie Tarpit

- URL: https://newsletter.kentbeck.com/p/genie-tarpit
- Date: Apr 29, 2026

### Verbatim

> Genies give you code that’s a degraded facsimile of the mediocre code it trained on.

> “Valuable” lives on 2 axes:
> Features—what the code does now.
> Futures—what we can get the code to do once we learn the lessons of this set of features.

> Here’s what I’ve observed—genies naturally live down & to the left of muddling. The “plausible deniability” task orientation of the genie leaves it claiming success even though the code doesn’t work at all. And complexity piles on complexity until even the genie can’t pretend to make progress any more.

> You probably saw this one coming—nobody knows. Does the model need to be trained on better code? Trained on good commits? Better harnesses? Tests? Which tests? When? Better prompting? Or grasp the nettle of the Bitter Lesson & let the model develop it’s own style of development

### What this source says

On a features × futures (optionality) chart, genie output tends to sit below the "muddling" zone of typical teams: claims success when it doesn't work, piles on complexity. He says nobody knows the fix yet.

---

## 6. Trust Factory

- URL: https://newsletter.kentbeck.com/p/trust-factory
- Date: Jun 02, 2026

### Verbatim

> “We’re accumulating code faster than we are accumulating trust.” Sometimes a phrase just hits. Yes, we can create code faster now, but software is bipedal—code & trust go together.

> XP offered faster accumulation of functionality than folks were used to, but it didn’t suffer from the lack of trust we see among genie pioneers. I never thought of it this way before but XP manufactured trust. But how? What is a trust factory?

> What I notice about this list that I didn’t expect is that each practice that creates trust also encourages trustworthiness.

> We are now shifting to individuals interacting individually with the genie (I call this the single player problem.

> Genies “care” about satisfying prompts, not purposes.

> Encouraging single player development eliminates most of the little chances to build trust.

> The genie ignores optionality & future change. Walking off the end of the productivity pier is a big trust breaker.

> What would trust-optimized augmented development look like?
> Slow development to ensure that the damn stuff actually works.
> Slow development to include structural improvements that expand options.
> Slow development to encourage frequent person-to-person interaction.
> Slow development to reinforce & update long-term purpose.
> That’s how you go faster.

### What this source says

Reframes a software process as a "trust factory": XP practices (programmer testing, pairing, CI, weekly planning, customer on team, continuous deployment, refactoring, observability) produced trust alongside code. Genie-driven "single player" development produces code faster than trust. He calls for deliberately slower, trust-optimized augmented development. Note: the opening quote is not attributed to a named person in the text.
