# Plan: An Accidental Guide to… Agent Skills

You are the writer. Write every word of
`packages/accidental-guides/guides/skills/guide.md`. It holds placeholder text now that only
shows the shape the builders expect. Replace every placeholder. Keep the shape exactly: the
section ids, the number of paragraphs in each section, the table columns and row labels,
and the fenced block.

No mannered prose: the writing must not call attention to itself. Make no assumption that
the reader is an expert.

## Read first, in this order

1. `packages/editorial/skills/accidental-guide-plan/references/series-rules.md` (binding).
2. `packages/editorial/skills/accidental-guide-write/references/voice.md` (binding).
3. `packages/accidental-guides/guides/agents-harnesses-skills-tools/guide.md`, the base
   guide. It already defines agent, harness, skill, tool, session and context window, and
   says a skill's name and description load at startup and the rest loads when used. Never
   contradict it and don't repeat it. Point to it by name, in this form only:
   An Accidental Guide to: Agents, Harnesses, Skills, and Tools.
4. `packages/accidental-guides/guides/lights-off-software-factories/guide.md`, a finished
   guide in this series, for length and register.
5. `drafts/skills/notes/sources.md`: the only facts you may use. Don't add
   facts that aren't there. Where products differ, say "as of October 2026".

## The reader and the question

The reader uses a coding agent and has read the base guide. They think of a skill as one
Markdown file, SKILL.md. The author's point: "Skills are often only thought about as a
markdown file and that's it. They have the ability to be much richer than that."

The question the guide answers: What can a skill folder hold, and why does it matter?

Build it up one idea at a time:

1. A skill is a folder. SKILL.md is the only file it needs, and it can hold more: scripts
   the agent runs, reference files it reads when a step needs them, and assets such as
   templates.
2. The harness only loads what a step needs. At the start of a session it loads each
   skill's name and description. It reads the rest of SKILL.md when your request matches
   the description, and other files only when a step opens or runs them. A script's code
   never enters the context window; only its output does. So a skill can carry a lot
   without costing room until it's used.
3. Scripts let the agent run code someone already wrote and tested, instead of working the
   same thing out again in each session. That is more reliable and uses less of the
   context window.
4. Skills come from several places: built into the harness, in your project, in your home
   folder, in a plugin, or set up by your organization. Read a skill from someone else
   before you use it, the way you would any program you install.
5. When is a skill the right tool? Compared with an instructions file, an MCP server and a
   sub-agent.

## Words

- "Skill", "harness", "agent", "model", "tool", "MCP server", "sub-agent", "instructions
  file", "context window", "session" keep the base guide's meanings. Don't define them again.
- The open standard is called Agent Skills (agentskills.io). Use that name once or twice;
  otherwise say "skill".
- Say "the agent" for the model working in the harness's loop, as the base guide does with
  "the main agent" where it matters. Say "the harness" for what loads files.
- Don't use "progressive disclosure" in the body except once, on the why page or the
  context page, introduced plainly as the standard's name for loading in stages. Never use
  it as a label in a diagram.
- No "token" counts in body prose beyond what the context page needs (about 100 tokens per
  description, under 5,000 recommended for the SKILL.md body, SKILL.md under 500 lines).
  Don’t explain tokens. Otherwise say "room in the context window".

## The five parts (keys)

These are the guide's entries, one page each, each with a tile. Each is a part of a skill
folder. Order and keys are fixed.

| Num | Name | Key | What it is |
|---|---|---|---|
| 01 | Description | De | The name and description at the top of SKILL.md. The only part loaded at startup, and what the agent matches your request against. |
| 02 | Instructions | In | The body of SKILL.md: the steps, which name the other files and say when to use each. |
| 03 | Script | Sc | Code in scripts/ that the agent runs through the shell tool. Only the output enters the context. |
| 04 | Reference file | Rf | Documentation in references/ that the agent reads when a step needs it. |
| 05 | Asset | As | Files in assets/ the skill uses in what it makes: templates, images, data such as lookup tables and schemas. |

## The running example

One skill throughout: release-notes, which writes release notes from merged pull requests
(GitHub's docs use this example). Its files:

- SKILL.md
- scripts/list_changes.sh, which lists the pull requests merged since the last release
- references/style.md, the team's rules for grouping and wording entries
- assets/template.md, the layout of the release notes

Use these exact paths everywhere.

## Pages, in print order, with word targets

The whole guide must read in five minutes: about 1,100 printed words including every
table, label and the sources page. Targets are printed words. Stay under them.

| Page | Section | Target | What it does |
|---|---|---|---|
| 1 | front matter | (fixed) | Cover |
| 2 | `{#why}` | 160 | Two paragraphs and the five-term table. Paragraph 1 is the blurb on the site and must stand alone: a skill is a folder, not only a file, and what it can hold. Paragraph 2: point to the base guide for the basics, and say in a sentence why the rest of the folder matters (the harness only loads what a step needs; scripts run instead of being re-worked). Term table rows: one plain sentence each. |
| 3 | `{#fit}` | 70 + diagram | The skill folder diagram, drawn by the builder from the fenced block and the table. The fenced block is the release-notes SKILL.md, shown as the file itself. Lines at most 55 characters. The table gives each part's file and a caption of at most 6 words. Then two short paragraphs: SKILL.md is the only required file; the instructions name the other files, so the agent knows what each is for and when to open it. |
| 4 | `{#ctx}` | 90 + diagram | What enters the context window, and when. One intro paragraph. The table drives a diagram of the window filling up, one row per moment: each row's "When" (at most 6 words), the part that it adds, and a label of at most 7 words. One closing paragraph: the script's code and the files no step opens never enter; what loads stays for the rest of the session. |
| 5–9 | `{#entry}` × 5 | 95 each | One page per part. Identify by: at most 14 words. What: two or three sentences, the first a short definition (it gets bolded up to the first full stop). So what: two sentences. Field marks: two rows, "In context" and "Cannot", each a short answer under 6 words with no full stop, then one sentence of detail. Confused with: one other thing (a part or a base-guide term) and one or two sentences. |
| 10 | `{#shared}` | 120 | Where skills come from and how they're shared. One intro sentence. Table: Where, Who gets it, Examples (as of October 2026). Five rows: Built in, Your project, Your home folder, Plugin, Your organization. One closing paragraph on reading a skill before using it, and where shared collections live. |
| 11 | `{#choose}` | 110 | Skill or something else? One intro sentence. Table: Use, When, For example. Four rows: Instructions file, Skill, MCP server, Sub-agent. One closing paragraph: they work together (a skill can tell the agent which MCP tools to call and which sub-agents to start), and the sign it's time for a skill. |
| 12 | `{#sources}` | (fixed) | One sentence and the sources table. Already filled in; check, don't add. |

## Rules for guide.md

- The front matter, section headings, ids, entry attributes, table header rows and the
  table row labels in the first column are fixed. Don't change them.
- No Markdown emphasis or backticks. No lists. No `&` before letters. No `<` except in
  `<br/>` in titles. No slashes in ordinary words (paths are fine: they're set in mono).
- No "e.g. " or "i.e. ". Typographic quotes and apostrophes (’ “ ”).
- A Short answer cell must not end with a full stop.
- Rows must read on their own: no row starts with "it", "its", "they" or "this".
- No self-narration ("this guide", "this page", "below", page numbers).
- No quotes, no names of people, no Microsoft-internal anything.
- Product facts only from `sources.md`, and say "as of October 2026" once on any page that
  names product folders or commands.
