# Writer instructions, round 1: An Accidental Guide to… Claude Desktop

Write the file `guide.md` in the current folder (packages/accidental-guides/guides/claude-desktop/).
Overwrite it if it exists. Write only that file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the reader is an expert.

## Read first

1. `packages/editorial/skills/accidental-guide-plan/references/series-rules.md` (binding writing rules)
2. `packages/editorial/skills/accidental-guide-write/references/voice.md` (binding voice)
3. `packages/accidental-guides/guides/agents-harnesses-skills-tools/guide.md` (the base guide;
   never contradict it, don't repeat it, point to it for basics: agent, harness, skill, tool,
   MCP server, session, context window)
4. `packages/accidental-guides/guides/lights-off-software-factories/guide.md` (a finished
   guide in the same Markdown format; copy its format exactly)
5. `drafts/claude-desktop/notes/sources.md` (the ONLY facts you may use)
6. `drafts/claude-desktop/notes/plan.md` (the page plan)

`<root>` is the repository root

## Who it's for

Someone who uses Claude Desktop or claude.ai and has lost track of where a skill, a connector
or a setting is kept. The author says the mess of where skills, MCP servers and other
configuration live is a headache. The guide should feel calm and make things easy to look up.
Plain, everyday English, one idea at a time, as if to a smart colleague who is new to this.
A five-minute read: about 1,100 printed words in total, including every table and the sources.
Cut detail, not clarity.

## Rules (all binding)

- No paragraph by list. If it's a list, it goes in a table. Otherwise connected sentences.
- No "A person can", "One may", "A team that". Say "you".
- No self-narration ("this guide", "this page", "below", page numbers), no hooks, trivia,
  sarcasm, snark, slogans, rhetorical questions, "not X but Y", em dashes, rhythm triplets.
- No borrowed framing (no birds, field guides, travel).
- No quotes, no names of people.
- Cross-references in body text use the colon form, exactly:
  "An Accidental Guide to: Agents, Harnesses, Skills, and Tools",
  "An Accidental Guide to: Claude Code", "An Accidental Guide to: GitHub Copilot CLI",
  "An Accidental Guide to: Codex", "An Accidental Guide to: Visual Studio and VS Code".
- Facts only from sources.md. Where the product changes often, say "as of October 2026" (once
  or twice in the whole guide, not on every page).
- Markdown limits: no emphasis, no backticks, no lists, no "<" except "<br/>" in # titles,
  no "&" directly before a letter, no slashes in ordinary words (anything with a slash is set
  in mono, so only paths use slashes), no "e.g. ". Use typographic quotes and apostrophes (’ “ ”).
- Menu paths are written like the app shows them, with " > " between steps: Customize > Connectors.
- A "Short answer" cell must not end with a full stop.
- In entry rows, no sentence starts with "It", "Its", "They" or "This". Each row reads on its own.
- First sentence of What and So what rows is printed bold (up to the first ". "), so make the
  first sentence a complete short point.

## The skeleton to fill (keep every heading, id and table shape exactly)

```
---
title: Claude Desktop
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to where Claude Desktop keeps its settings, as of October 2026.
running_footer: Claude Desktop
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: October 2026
version: 0.1.0
---

# What can you set up<br/>in Claude Desktop? {#why}

(Paragraph 1, about 45 words. Stands alone on the website as the blurb. Say in plain words what
you can set up: how Claude should answer you, steps for tasks you repeat, the apps and services
Claude can reach, and how much Claude may do without asking. Say that most of it belongs to your
Claude account, so it follows you to claude.ai, and a few things belong to this computer only.)

(Paragraph 2, about 35 words. Where the two sets of screens are: Settings and Customize, both in
the app; on Team and Enterprise plans an owner can also set limits. Point to An Accidental Guide
to: Agents, Harnesses, Skills, and Tools for what a skill, a tool and an MCP server are.)

| Term | Meaning |
|---|---|
| Instructions | (one short sentence) |
| Skills | (one short sentence) |
| Connectors | (one short sentence; say a connector is an MCP server you add in Customize) |
| Plugins | (one short sentence) |
| Settings and permissions | (one short sentence) |

# Instructions {#entry num=01 mono=In}

| Field | Text |
|---|---|
| Identify by | (where you see it: Instructions for Claude in Settings > General, and Set project instructions on a project’s page) |
| What | (2 sentences) |
| So what | (1–2 sentences) |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Works in | (short) | (detail) |
| Cannot | (short) | (detail) |

## Confused with: Memory

(1–2 sentences: instructions are what you write; memory is what Claude picks up from your chats,
in Settings > Memory, and each project has its own.)

# Skills {#entry num=02 mono=Sk}
(same shape; Identify by: Customize > Skills; needs Code execution and file creation on in
Settings > Capabilities; enabled skills also load in Claude Code when you sign in with the same
account. Confused with: Instructions)

# Connectors {#entry num=03 mono=Cn}
(same shape; Identify by: Customize > Connectors, or the + button in the message box. A connector
is an MCP server reached over the internet; works on web, desktop and mobile once connected;
tool permissions per connector: Always allow, Needs approval, Blocked. A server that runs on your
computer needs Claude Desktop: install a desktop extension (.mcpb file) in Settings > Extensions,
or list it in the config file. Free plans: one custom connector. Confused with: Desktop extension)

# Plugins {#entry num=04 mono=Pl}
(same shape; Identify by: Customize > Plugins, Discover tab. A plugin bundles skills, connectors
and sub-agents. Saved to your account, not your computer. Paid plans. A plugin with a local MCP
server only works through the desktop app. Confused with: Skills)

# Settings and permissions {#entry num=05 mono=Se}
(same shape; Identify by: Settings, from your initials in the lower left. General, Capabilities,
Memory; and on desktop only, Extensions and Developer under Desktop app. Permissions: the
permission setting in the message box, default Manual, Claude asks before it takes actions;
tool permissions per connector; folders you gave access to are under Trusted folders.
Confused with: Customize)

# Where things live {#where}

(One paragraph, about 40 words: most things live in your Claude account and show up wherever you
sign in; a few live on this computer, and those need Claude Desktop. After you edit the config
file, quit Claude Desktop completely and open it again.)

| What | Lives in | Where to find it |
|---|---|---|
| Instructions | Account | Settings > General, and each project’s page |
| (Memory) | Account | Settings > Memory |
| Skills | Account | Customize > Skills |
| Connectors | Account | Customize > Connectors, with tool permissions on each connector |
| Plugins | Account | Customize > Plugins |
| (Code execution) | Account | Settings > Capabilities |
| (Desktop extensions) | This computer | Settings > Extensions |
| (Local MCP servers) | This computer | Settings > Developer > Edit Config opens claude_desktop_config.json. macOS: ~/Library/Application Support/Claude/claude_desktop_config.json Windows: %APPDATA%\Claude\claude_desktop_config.json |
| (MCP logs) | This computer | macOS: ~/Library/Logs/Claude Windows: %APPDATA%\Claude\logs |
| (Code tab) | This computer | ~/.claude/settings.json and ~/.claude/skills, the same files Claude Code uses |

(Closing paragraph, one or two sentences: Claude Desktop’s Cowork work takes skills, plugins and
connectors from your account (Customize), while the Code tab reads ~/.claude, the way Claude Code
does. Point to An Accidental Guide to: Claude Code.)

# Your account or<br/>your organization? {#account}

(One paragraph, about 40 words: on Free, Pro and Max you set everything yourself. On Team and
Enterprise, owners set limits in Organization settings, and IT can set some of the desktop app’s
settings on the computer itself.)

| Setting | You | An owner, in Organization settings |
|---|---|---|
| Skills | (short) | (Plugins & skills: turn skills on, add skills for everyone, turn off creating skills) |
| Connectors | (short) | (Connectors: add for the team, each person still signs in; limits nobody can override) |
| Plugins | (short) | (marketplaces; some required and can’t be removed) |
| (Desktop extensions) | (short) | (allowlist under Connectors, Desktop tab) |
| (Memory) | (short) | (Capabilities: turns memory on for the organization) |

(Closing paragraph, about 40 words: on managed computers, IT can set keys in the preference
domain com.anthropic.claudefordesktop on macOS or HKLM\SOFTWARE\Policies\Claude in the Windows
registry, for example to turn off desktop extensions or local MCP servers. Those override the
in-app allowlist. When something you expect is missing, ask your owner.)

# Same thing elsewhere {#elsewhere}

(One short sentence.)

| In Claude Desktop | Elsewhere |
|---|---|
| Instructions | (CLAUDE.md in Claude Code; AGENTS.md in Codex; copilot-instructions.md or AGENTS.md for GitHub Copilot, in Copilot CLI and VS Code) |
| Skills | (a folder with a SKILL.md file in Claude Code, Copilot CLI and VS Code; Claude Code reads ~/.claude/skills; Codex has skills too) |
| Connectors | (MCP servers: .mcp.json in Claude Code, ~/.codex/config.toml in Codex, the User or Workspace group in VS Code) |
| Plugins | (plugins in Claude Code, Codex, Copilot CLI and VS Code) |
| Settings and permissions | (~/.claude/settings.json in Claude Code; approval_policy and sandbox_mode in ~/.codex/config.toml) |

(Closing paragraph naming the four sibling guides in colon form.)

# Sources {#sources}

These public sources were checked on 22 October 2026.

| Source | Date | Address |
|---|---|---|
(One row per source in sources.md, in this form:
| Anthropic, Use connectors to extend Claude’s capabilities | Checked 22 October 2026 | support.claude.com/en/articles/11176164 |
Drop "https://" and the slug after the article number for support.claude.com addresses. Keep
only the sources the text relies on, with short titles. For the Date column write "Checked 22 October 2026".)
```

Every word count above is a ceiling, not a target. Shorter is better if it stays clear.
