# Plan: An Accidental Guide to… Context Windows

Slug: `context-windows`. Folder: `packages/accidental-guides/guides/context-windows/`.
Builders copied from `lights-off-software-factories/` (the specs-and-reviews layout work has
not landed). Sources and excerpts: `drafts/context-windows/notes/sources.md`.

## The reader

Someone who uses a coding agent, or is about to, and has read An Accidental Guide to:
Agents, Harnesses, Skills, and Tools, or can be pointed to it. That guide already says: the
model only knows what's in its context window; the harness sends the whole context on every
call; the window has a fixed size; a fuller window is slower, costs more and makes the model
more likely to miss details; when it fills, the harness trims or summarizes older content.
It also has a table of what's in the main agent's context window and when. Build on that.
Don't repeat the table and never contradict it.

## The question each page answers

| Page | Section | Question |
|---|---|---|
| 1 | cover | |
| 2 | `{#why}` | What is the context window, and what does this guide add? |
| 3 | `{#fit}` | What takes up room, and what happens when it fills up? (the stacked-bar diagram) |
| 4 | Token | What is the window measured in? |
| 5 | Startup context | What's in the window before I type anything? |
| 6 | Compaction | What happens when the window is nearly full? |
| 7 | New session | How do I get an empty window back? Where do sub-agents fit? |
| 8 | `{#habits}` | What simple habits keep the window useful? |
| 9 | `{#sources}` | Where do the facts come from? |

## Key concepts (four, each with a page and a filled tile)

| # | Name | Tile | Colour |
|---|---|---|---|
| 01 | Token | Tk | blue |
| 02 | Startup context | St | green |
| 03 | Compaction | Cp | purple |
| 04 | New session | Ns | yellow |

## The diagram (page 3), drawn in build_guide.py

Three stacks, each the whole window, drawn to scale with example sizes. Bottom to top:

- Long session: system prompt, instructions files, skill and sub-agent descriptions, tool
  definitions (these four bracketed as Startup context, green), your messages and the
  model's replies, file contents and tool results (grey), free space.
- After compaction (Cp tile): the same startup context, a small purple Summary, a lot of
  free space. Dotted lines show the grey part shrinking into the summary.
- New session (Ns tile): the startup context and free space only.
- A dashed line on top: "Window size, counted in tokens", with the Tk tile.

## Facts to use (all in sources.md)

- Everything the harness sends counts: system prompt, instructions files, skill and agent
  descriptions, tool definitions (MCP ones too, unless loaded on demand), messages, tool
  calls, tool results, file contents. Tool results are often the largest.
- Windows are counted in tokens. A token is a short piece of text, often part of a word. As
  of October 2026, current Claude models have a 1 million token window, others 200,000.
- As the window fills, accuracy and recall drop, even well before the limit.
- When the window is nearly full, harnesses compact: they replace older conversation with a
  summary. Copilot CLI starts at about 80% (as of October 2026). Claude Code clears old tool
  output first. Detail is lost: early instructions, exact wording, full command output.
  Compaction can't be undone. Instructions files and the system prompt are still there
  after compaction. /compact runs it by hand, with an optional focus.
- /clear or /new starts with an empty conversation. Nothing carries over except files
  (instructions files, memory files, plans you wrote down). /clear costs nothing; /compact
  is itself a large request.
- A sub-agent works in its own window and returns a summary, so long output stays out of
  the main window.
- /context (Claude Code, Copilot CLI) and /status (Codex) show how full the window is.
- Habits: new session per unrelated task; write the plan and progress to a file; send
  searches, test runs and log reading to a sub-agent; read only what you need; keep
  instructions files short and move procedures into skills; turn off MCP servers you
  aren't using; compact at a natural break and say what to keep.

## Budget

About 1,100 printed words in all, including tables, diagram labels and sources. Roughly:
why 140, fit 90, each entry 130, habits 170, sources 130.
