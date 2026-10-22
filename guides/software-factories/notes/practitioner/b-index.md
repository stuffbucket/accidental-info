# Source index — practitioner set B

Collected 2026-10-21. Raw text for each source is under `b-raw/<name>/` (page.html/page.txt/url.txt). Notes files: `b-anthropic.md`, `b-openai-lopopolo.md`, `b-boeckeler-fowler.md`, `b-hashimoto.md`, `b-ronacher.md`, `b-beck.md`, `b-dhh.md`, `b-pocock.md`, `b-lineage-huntley-shapiro.md`. Glossary: `b-terms.md`. Disagreements: `b-disagreements.md`. Hype set aside: `../hype/flagged-practitioner-b.md`.

| Title | Author | Date | URL | Relevance |
|---|---|---|---|---|
| Building effective agents | Erik S., Barry Zhang (Anthropic) | 2024-12-19 | https://www.anthropic.com/engineering/building-effective-agents | Defines workflows vs agents; five workflow patterns; "simplest solution" rule; ACI |
| Effective context engineering for AI agents | Anthropic Applied AI (Rajasekaran et al.) | 2025-09-29 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Defines context engineering, attention budget, right altitude, just-in-time context, compaction, notes, sub-agents |
| Effective harnesses for long-running agents | Justin Young (Anthropic) | 2025-11-26 | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | Initializer + coding agent, feature list JSON, progress file; named failure modes |
| Building a C compiler with a team of parallel Claudes | Nicholas Carlini (Anthropic) | 2026-02-05 | https://www.anthropic.com/engineering/building-c-compiler | "Agent teams": 16 parallel looped agents, git locks, verifier-first; measured cost and limits |
| Harness design for long-running application development | Prithvi Rajasekaran (Anthropic) | 2026-03-24 | https://www.anthropic.com/engineering/harness-design-long-running-apps | Planner/generator/evaluator, sprint contract, context anxiety/reset; remove harness parts as models improve |
| Best practices for Claude Code | Anthropic (docs, living) | fetched 2026-10-21 (orig. blog Apr 2025) | https://code.claude.com/docs/en/best-practices | Verification gates, explore-plan-implement-commit, interview, writer/reviewer, fan-out, named anti-patterns |
| Harness engineering: leveraging Codex in an agent-first world | Ryan Lopopolo (OpenAI) | 2026-02-11 | https://openai.com/index/harness-engineering/ | The post that named harness engineering; no-hand-written-code team; repo as system of record; garbage collection |
| harness-engineering repo README | Ryan Lopopolo | 2026-07 | https://github.com/lopopolo/harness-engineering | Author's later definition of harness engineering; source index with dates |
| Stop Treating Code as the Artifact | Ryan Lopopolo | 2026-03-13 | https://hyperbo.la/w/code-is-not-the-artifact/ | Ghost library; spec-driven development in reverse; PR carries its prompt |
| Software Work Is No Longer Scheduled | Ryan Lopopolo | 2026-03-13 | https://hyperbo.la/w/software-work-not-scheduled/ | Defines "background task" suitable for agents |
| The Production Function Changed | Ryan Lopopolo | 2026-03-13 | https://hyperbo.la/w/production-function-changed/ | Executable policy as verifiers; PRs carry proof; human decides invariant and proof |
| Harness engineering for coding agent users | Birgitta Böckeler | 2026-04-02 (memo 2026-02-17) | https://martinfowler.com/articles/harness-engineering.html | Guides/sensors, computational/inferential, steering loop, harnessability, harness templates |
| Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl | Birgitta Böckeler | 2025-10-15 | https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html | Spec-first/anchored/as-source; critique of SDD tools |
| Context Engineering for Coding Agents | Birgitta Böckeler | 2026-02-05 | https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html | Who loads context (LLM/human/software); "illusion of control" |
| TDD inside the agent loop - theater or actual value? | Birgitta Böckeler | 2026-08-10 | https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html | Small eval: no benefit from TDD inside the agent loop |
| I still care about the code | Birgitta Böckeler | 2025-07-09 | https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html | LLMs are inferrers not compilers; risk = impact × probability × detectability |
| Humans and Agents in Software Engineering Loops | Kief Morris | 2026-03-04 | https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html | Why/how loops; in/on/outside the loop; agentic flywheel; Ralph footnote |
| LLMs bring new nature of abstraction | Martin Fowler | 2025-06-24 | https://martinfowler.com/articles/2025-nature-abstraction.html | Non-deterministic abstraction framing |
| Exploring Generative AI (series index) | Böckeler et al. | ongoing | https://martinfowler.com/articles/exploring-gen-ai.html | Index; other memos not read in full listed in b-boeckeler-fowler.md |
| My AI Adoption Journey | Mitchell Hashimoto | 2026-02-05 | https://mitchellh.com/writing/my-ai-adoption-journey | Six-step adoption; earliest dated use of "harness engineering" here |
| Agentic Coding Recommendations | Armin Ronacher | 2025-06-12 | https://lucumr.pocoo.org/2025/6/12/agentic-coding/ | Tool rules; simple code; language choice; parallelization |
| Agentic Coding Things That Didn't Work | Armin Ronacher | 2025-07-30 | https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/ | Rules of automation; failed hooks/commands |
| 90% | Armin Ronacher | 2025-09-29 | https://lucumr.pocoo.org/2025/9/29/90-percent/ | Measured >90% AI-written on one service, with method |
| Agent Psychosis: Are We Going Insane? | Armin Ronacher | 2026-01-18 | https://lucumr.pocoo.org/2026/1/18/agent-psychosis/ | Slop loops; review asymmetry |
| The Final Bottleneck | Armin Ronacher | 2026-02-13 | https://lucumr.pocoo.org/2026/2/13/the-final-bottleneck/ | Review as bottleneck; backpressure; accountability |
| The Coming Loop | Armin Ronacher | 2026-06-23 | https://lucumr.pocoo.org/2026/6/23/the-coming-loop/ | Agent loop vs harness-level loop; where loops work; warnings |
| Astra for Coding: Why Are We Doing This Again? | Armin Ronacher | 2026-09-07 | https://lucumr.pocoo.org/2026/9/7/astra-why/ | First-hand failed 35-hour software factory run |
| Augmented Coding & Design | Kent Beck | 2025-05-03 | https://newsletter.kentbeck.com/p/augmented-coding-and-design | Genie adds features, not structure; restrict context |
| Genie Wants to Leap | Kent Beck | 2025-05-12 | https://newsletter.kentbeck.com/p/genie-wants-to-leap | Complexity cliff; test-cheating; "parallels" technique |
| Augmented Coding: Beyond the Vibes | Kent Beck | 2025-06-25 | https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes | Augmented vs vibe coding; TDD system prompt; warning signs |
| Genie Lessons: Nobody Wants Agents | Kent Beck | 2026-04-23 | https://newsletter.kentbeck.com/p/genie-lessons-nobody-wants-agents | Against swarms; outcome-orientation; multiplayer |
| Genie Tarpit | Kent Beck | 2026-04-29 | https://newsletter.kentbeck.com/p/genie-tarpit | Features vs futures; genie output below "muddling" |
| Trust Factory | Kent Beck | 2026-06-02 | https://newsletter.kentbeck.com/p/trust-factory | XP as a trust factory; single-player problem; slow down |
| Lex Fridman Podcast #474 (transcript) | DHH | 2025-07 | https://lexfridman.com/dhh-david-heinemeier-hansson-transcript/ | Mid-2025 position: type your own code; competence; vibe coding limits |
| Promoting AI agents | DHH | 2026-01-07 | https://world.hey.com/dhh/promoting-ai-agents-3ee04945 | Shift to agents; "supervised collaboration"; rejects 90%+ claims |
| Clankers with claws | DHH | 2026-02-05 | https://world.hey.com/dhh/clankers-with-claws-9f86fa71 | Agents using human interfaces; accommodations a "temporary crutch" |
| Basecamp becomes agent accessible | DHH | 2026-03-25 | https://world.hey.com/dhh/basecamp-becomes-agent-accessible-3ae6b949 | 37signals ships API/CLI/skill for agents |
| Let the agents democratize open source | DHH | 2026-06-01 | https://world.hey.com/dhh/let-the-agents-democratize-open-source-9fd630a9 | Against barriers to AI-assisted contributions |
| Endless execution | DHH | 2026-08-09 | https://world.hey.com/dhh/endless-execution-4157e065 | Enthusiasm; documents shift |
| Over my dead pencil | DHH | 2026-10-06 | https://world.hey.com/dhh/over-my-dead-pencil-fb0f3647 | Rails World: "put down the pencils" |
| Redundancy is the engine of progress | DHH | 2026-10-07 | https://world.hey.com/dhh/redundancy-is-the-engine-of-progress-76499402 | "Agent wranglers"; labor framing |
| 11 Tips For AI Coding With Ralph Wiggum | Matt Pocock | 2026-01-08 | https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum | Ralph loop practice; HITL vs AFK; feedback loops; entropy |
| Getting Started With Ralph | Matt Pocock | 2026-01-08 | https://www.aihero.dev/getting-started-with-ralph | Ralph definition |
| Getting Started (Ralph workshop) | Matt Pocock | 2026-02-02 | https://www.aihero.dev/getting-started-m2c6l | Ralph definition |
| Skills For Real Engineers (repo) | Matt Pocock | created 2026-02-03; fetched 2026-10-21 | https://github.com/mattpocock/skills | grill-me, write-a-prd → to-spec, prd-to-issues → to-tickets, tdd, implement; failure modes |
| AI Coding Dictionary (entries: software factory, dark factory, AFK, HITL, harness, spec, grilling, smart zone, AX) | Matt Pocock | 2026-05-01 onward; factory entries 2026-09-24 | https://www.aihero.dev/ai-coding-dictionary | Definitions of software factory and dark factory |
| Ralph Wiggum as a "software engineer" | Geoffrey Huntley | 2025-07-14 | https://ghuntley.com/ralph/ | Origin of "Ralph" (lineage) |
| The Five Levels: from Spicy Autocomplete to the Dark Factory | Dan Shapiro | 2026-01-23 | https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/ | Earliest "dark factory" for software found here (lineage) |

## Gaps

- No talk transcripts or video read for Pocock (YouTube) or DHH's Rails World 2026 keynote; DHH's keynote is known only via his blog post.
- Beck's paid posts not read ("Is Source Code Going Away?", "Genie: Death of the Iron Triangle?", "Passing Tests Bore Me", "Take My Toil, Leave Me My Struggle").
- No other OpenAI engineering posts beyond harness engineering (e.g. Codex exec plans cookbook linked from it) were read.
- Origins of "context engineering", "vibe coding", "smart/dumb zone", and StrongDM's "software factory" were not traced; they predate or sit outside this source set.
- Anthropic's "How we built our multi-agent research system" (2025-06-13) and "Writing effective tools for agents" (2025-09-11) not read.
- Saved but not quoted: Böckeler "Sensors for coding agents", "The role of developer skills in agentic coding", "To vibe or not to vibe"; Edwards-Alexander "An Accidental Blackboard"; Ronacher "A Year Of Vibes", "Some Things Just Take Time"; Anthropic "Redesigning source control" (raw in `b-raw/`).
