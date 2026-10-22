---
title: Context Windows
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to what fills a coding agent’s context window, as of October 2026.
running_footer: Context Windows
edition: [Co]Lab · bstucker · October 2026
cover_footer: October 2026
version: 0.1.0
---

# What is the<br/>context window? {#why}

The context window is everything the model can see on one call. It holds the instructions
and tool descriptions the harness loads, your conversation, and every file and command
output the agent has read. The window has a fixed size, so a long session fills it.

An Accidental Guide to: Agents, Harnesses, Skills, and Tools covers the basics and lists
what the window holds. These four ideas explain how the window fills up and how you keep
room for the work.

> | Term | Meaning |
> |---|---|
> | Token | A short piece of text used to count the window’s size and usage. |
> | Startup context | What the harness loads before your first message. |
> | Compaction | Replacing older conversation with a summary when the window is nearly full. |
> | New session | An empty conversation that starts with only the startup context. |

# What takes up room? {#fit}

The startup context at the bottom loads before you type and stays for the whole session.
The conversation above it grows with every message, file and command output. After
compaction, a short summary replaces that conversation. A new session has only the startup
context. The sizes in the picture are examples.

> [!TIP]
> A crowded window can give worse answers before it is full. The model has more to read, so
> important details are harder to find. To see how full yours is, run /context in Claude
> Code or GitHub Copilot CLI, or /status in Codex, as of October 2026.

# Token {#entry num=01 mono=Tk}

| Field | Text |
|---|---|
| Identify by | A window size, usage count or price stated in tokens. |
| What | A token is a short piece of text, often part of a word. Windows, usage and prices are counted in tokens. |
| So what | Everything in the window is sent again on every call, so a large file or log costs its tokens on every later call. As of October 2026, current Claude models have a 1 million token window, and older ones have 200,000. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Controlled by | The model you pick | Each model sets its context window size. |
> | Cannot | Be counted exactly from words | Token counts for the same text can differ by model. |

## Confused with: Word

A short, common word is often one token. A long or rare word can take several.

# Startup context {#entry num=02 mono=St}

| Field | Text |
|---|---|
| Identify by | Content in the window before your first message. |
| What | Startup context is what the harness loads when a session begins. That includes the system prompt, instructions files, skill and sub-agent descriptions, and tool definitions, including MCP tools unless they load on demand. |
| So what | Startup context is sent on every call and remains after compaction. Long instructions files or many MCP servers can take a large share before you begin. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Controlled by | You, your team and the harness | You choose the instructions files and MCP servers. The harness writes the system prompt. |
> | Cannot | Hold every procedure cheaply | A procedure used for one kind of task belongs in a skill, which loads only when used. |

## Confused with: Memory

Memory in a harness is a file of notes that loads with the startup context. The model
itself keeps nothing between calls.

# Compaction {#entry num=03 mono=Cp}

| Field | Text |
|---|---|
| Identify by | A note that the conversation was compacted or summarized. |
| What | Compaction replaces older conversation with a summary when the window is nearly full. As of October 2026, GitHub Copilot CLI compacts at about 80 percent full. |
| So what | Compaction can lose detail, such as instructions you gave early on, exact wording and full command output. Put rules that must last in an instructions file, which is still there after compaction. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Controlled by | The harness and you | The harness compacts on its own. You can compact sooner and say what to keep, such as /compact focus on the login bug. |
> | Cannot | Bring lost detail back | A completed compaction can’t be undone. |

## Confused with: Trimming

Trimming drops old content, such as old tool output, with no summary. Some harnesses trim
before they compact.

# New session {#entry num=04 mono=Ns}

| Field | Text |
|---|---|
| Identify by | An empty conversation after /clear, /new or opening a session. |
| What | A new session starts with only the startup context. Only content saved in files carries over from the old conversation. |
| So what | A fresh window has room for a new task. Before you start one, have the agent save its plan and progress to a file the next session can read. A sub-agent also gets a fresh window for one task and sends back only a summary. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Controlled by | You | Open a session, or use /clear or /new where supported. |
> | Cannot | Recall the old conversation | Some harnesses let you go back to it, such as /resume in Claude Code. |

## Confused with: Compaction

Compaction keeps a summary in the same session. A new session keeps only files.

# What keeps the<br/>window useful? {#habits}

A few habits keep the window small and on topic, so the model can find what matters.

> | Habit | Why it helps |
> |---|---|
> | Start fresh for unrelated work | A new session gives the next task an empty conversation. |
> | Save the plan and progress | A file carries what matters into the next session. |
> | Send long work to sub-agents | Searches, test runs and log reading stay in separate windows. Only summaries return. |
> | Read only what you need | Ask for one function or the failing tests instead of the full output. |
> | Keep instructions files short | Startup context is sent on every call. Move specific procedures into skills. |
> | Compact at a natural break | When one part of the work is done, run /compact and say what to keep. |

Each habit leaves more room for the work you’re doing now.

# Sources {#sources}

These public sources were checked on 22 October 2026, and harnesses change often.

| Source | Date | Address |
|---|---|---|
| Anthropic, Claude Code: Explore the context window |  | code.claude.com/docs/en/context-window |
| Anthropic, Claude Code: How Claude Code works |  | code.claude.com/docs/en/how-claude-code-works |
| Anthropic, Claude Code: Manage costs effectively |  | code.claude.com/docs/en/costs |
| Anthropic, Context windows |  | platform.claude.com/docs/en/build-with-claude/context-windows |
| Anthropic, Effective context engineering for AI agents |  | anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| GitHub, About context management |  | docs.github.com/en/copilot/concepts/prompting-and-context/context-management |
| OpenAI, Codex commands |  | learn.chatgpt.com/docs/developer-commands |
| Chroma, Context Rot |  | trychroma.com/research/context-rot |
| HumanLayer, Getting AI to Work in Complex Codebases |  | github.com/humanlayer/advanced-context-engineering-for-coding-agents |
