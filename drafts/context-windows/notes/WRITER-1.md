# Writer instructions: An Accidental Guide to… Context Windows

You are the writer. Write every word of
`packages/accidental-guides/guides/context-windows/guide.md`. The file holds placeholder
text now that shows the exact shape the builders expect. Replace every PLACEHOLDER and keep
the shape: the same sections, ids, attributes, headings, tables, column counts and row
labels. Edit only `guide.md`. Do not touch any other file.

## Read first, in this order

1. `packages/editorial/skills/accidental-guide-plan/references/series-rules.md` (binding).
2. `packages/editorial/skills/accidental-guide-write/references/voice.md` (binding).
3. `packages/accidental-guides/guides/agents-harnesses-skills-tools/guide.md`, the base
   guide. Read its "The model and the context window" page closely.
4. `drafts/context-windows/notes/plan.md`, the page plan and the diagram.
5. `drafts/context-windows/notes/sources.md`, the only facts you may use.
6. `packages/accidental-guides/guides/lights-off-software-factories/guide.md`, a guide in
   the same series at the right length and register.

## The author's direction, verbatim and binding

> remember no mannered prose and the writing is clear, easy to follow, doesn't put a lot of
> burden on the reader and makes no assumptions that they have a lot of depth in a topic nor
> are they an expert. These are 5 minute reads, tops.

No mannered prose: the writing must not call attention to itself. Make no assumption that
the reader is an expert.

## Voice and rules

- Regular English, as if to a smart colleague who is new to this. Build one idea at a time.
  Say "you" where that is natural. Vary sentence length the way speech does.
- No paragraph by list. No stiff "A person can". No self-narration ("this guide", page
  talk). No hooks, trivia, sarcasm or snark. No borrowed framing (no birds, field guides or
  travel). No quotes and no names of people. No Microsoft-internal anything.
- No em dashes, no semicolons, no "not X but Y", no "rather than" contrasts, no rhythm
  triplets, no set-up and reveal, no slogans, no rhetorical questions.
- In table rows, no sentence starts with "it", "its", "they" or "this". Rows must read on
  their own.
- Use the curly apostrophe (’) and curly quotes. No backticks, no Markdown emphasis, no
  lists, no "&". No slashes in ordinary words. Slash commands such as /compact, /clear,
  /new, /context and /status are fine, and file names such as CLAUDE.md and AGENTS.md.
- No "e.g." or "i.e.". The builder bolds a What or So what row up to the first ". ", so
  make each first sentence a complete short answer.
- A Short answer cell (middle column of Field marks) must not end with a full stop. The
  builder adds one.
- Cross-reference other guides in the colon form only: An Accidental Guide to: Agents,
  Harnesses, Skills, and Tools.
- Where a product detail or threshold changes often, say "as of October 2026".

## The base guide

The base guide already explains the model, harness, agent, sub-agent, skill, tool, session
and the context window. It says the model only knows what’s in its context window, the
harness sends the whole context on every call, the window has a fixed size, a fuller window
is slower and more expensive and makes the model more likely to miss details, and the
harness trims or summarizes older content when the window fills. Its table lists what’s in
the main agent’s context window and when. Point to it for those basics. Don’t repeat its
table or its definitions, and never contradict it. Use its words with its meanings: main
agent, sub-agent, instructions file, skill, tool definitions, tool call, tool result,
session, harness.

## Length

About 1,100 printed words for the whole guide, including tables, the diagram labels (about
40 words, already written) and the sources page. Aim for: why page 140 words, fit page 90,
each entry 120 to 130, habits page 170, sources intro 15. Cut detail, not clarity.

## Section by section

### Front matter

Keep it as it is.

### `{#why}` What is the context window?

Two short paragraphs, then the four-row Term | Meaning table.

- Paragraph 1 is shown on the website on its own. It says plainly what the context window
  is in a coding agent: everything the model can see on one call. Name what fills it in
  everyday words (the instructions and tool descriptions the harness loads, your
  conversation, and every file and command output the agent has read), and that it has a
  fixed size and a long session fills it.
- Paragraph 2 points to An Accidental Guide to: Agents, Harnesses, Skills, and Tools for
  the basics and the list of what’s in the window, and says these four ideas explain how
  the window fills up and how to keep room in it.
- Table: one plain sentence per term. Token, Startup context, Compaction, New session.

### `{#fit}` What takes up room?

The page shows the diagram described in plan.md. Write two short paragraphs under it.

- Paragraph 1 walks through the picture in plain words: the startup context at the bottom
  loads before you type and stays all session; the conversation above it grows with every
  message, file and command output; after compaction a short summary replaces the
  conversation; a new session has only the startup context. The sizes are an example.
- Paragraph 2: a crowded window gives worse answers even before it is full, because the
  model has more to read and the detail that matters is harder to find. Then how to see
  your own: /context in Claude Code and GitHub Copilot CLI, /status in Codex, as of
  October 2026.

### Entries

Each entry has Identify by, What, So what, then Field marks with exactly two rows,
`Controlled by` and `Cannot` (change the placeholder label `Set by` to `Controlled by`),
then Confused with. Keep the Confused with names as given: Word, Memory, Trimming,
Compaction.

- Token: the unit the window, usage and price are counted in. A short piece of text, often
  part of a word. Window sizes as of October 2026 (1 million tokens for current Claude
  models, 200,000 for others). Everything is resent on every call, so a big file or log
  costs its tokens on every later call. Controlled by: the model you pick sets the size.
  Cannot: be counted from words exactly, since the same text can be a different number of
  tokens on different models. Confused with: Word.
- Startup context: what the harness loads before your first message (system prompt,
  instructions files, skill and sub-agent descriptions, tool definitions including MCP
  ones unless loaded on demand). Sent on every call, still there after compaction. A long
  instructions file or many MCP servers can take a large share before you start.
  Controlled by: you and your team for the files and servers, the harness for the system
  prompt. Cannot: hold every procedure cheaply; a procedure for one kind of task belongs in
  a skill, which loads only when used. Confused with: Memory (harness memory features save
  notes to files that load at startup; the model itself keeps nothing between calls).
- Compaction: the harness replaces older conversation with a summary so the session can go
  on. Runs on its own when the window is nearly full (Copilot CLI starts at about 80% as of
  October 2026), or when you run /compact, which can take a focus such as
  /compact focus on the login bug. Detail goes: early instructions, exact wording, full
  command output. Put rules that must last in an instructions file, which is still there
  after compaction. Controlled by: the harness, and you. Cannot: bring lost detail back, a
  completed compaction can’t be undone. Confused with: Trimming (some harnesses first drop
  old tool output outright; trimming removes content, compaction keeps a summary of it).
- New session: /clear or /new, or opening a new session, gives an empty conversation with
  only the startup context. Nothing from the old conversation carries over except what’s
  in files. A sub-agent gives one task the same fresh window and sends back only a summary.
  Before you clear, have the agent write the plan and progress to a file the next session
  can read. Controlled by: you. Cannot: recall the old conversation. Confused with:
  Compaction (compaction keeps a summary in the same session; a new session keeps only
  files).

### `{#habits}` What keeps the window useful?

One short intro paragraph, then the Habit | Why it helps table with six or seven rows, then
one closing paragraph. The Habit cell is a short imperative of three to seven words. The
Why cell is one or two plain sentences. Habits, from sources.md: a new session for each
unrelated task; write the plan and progress to a file; send searches, test runs and log
reading to a sub-agent; ask for only the part you need (a function, the failing tests);
keep instructions files short and move procedures into skills; turn off MCP servers you
aren’t using; compact at a natural break and say what to keep. The closing paragraph is one
or two sentences that tie the habits back to keeping room for the work. Don’t repeat the
/context advice from the fit page.

### `{#sources}`

Intro paragraph: one sentence saying these public sources were checked on 22 October 2026
and that harnesses change often. Replace the table with exactly these rows, date column
left empty:

| Source | Date | Address |
|---|---|---|
| Anthropic, Claude Code: Explore the context window |  | code.claude.com/docs/en/context-window |
| Anthropic, Claude Code: How Claude Code works |  | code.claude.com/docs/en/how-claude-code-works |
| Anthropic, Claude Code: Manage costs effectively |  | code.claude.com/docs/en/costs |
| Anthropic, Context windows |  | platform.claude.com/docs/en/build-with-claude/context-windows |
| Anthropic, Effective context engineering for AI agents |  | anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| GitHub, About context management |  | docs.github.com/en/copilot/concepts/prompting-and-context/context-management |
| GitHub, Optimizing AI usage |  | docs.github.com/en/copilot/tutorials/optimize-ai-usage |
| Visual Studio Code, Context |  | code.visualstudio.com/docs/copilot/concepts/context |
| OpenAI, Codex commands |  | learn.chatgpt.com/docs/developer-commands |
| Chroma, Context Rot |  | trychroma.com/research/context-rot |
| HumanLayer, Getting AI to Work in Complex Codebases |  | github.com/humanlayer/advanced-context-engineering-for-coding-agents |

## When you finish

Read the whole file once more as a newcomer. Check every rule above, the word budget, and
that nothing contradicts the base guide. Reply with the word count of guide.md's body.
