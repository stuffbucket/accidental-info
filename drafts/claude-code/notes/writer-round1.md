# Writer instructions, round 1: An Accidental Guide to… Claude Code

You are writing `guide.md` in the current folder
(`packages/accidental-guides/guides/claude-code/guide.md`). Replace the whole file. Write only
that file. Don't touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

## Read first

1. `packages/editorial/skills/accidental-guide-plan/references/series-rules.md` (binding writing rules).
2. `packages/editorial/skills/accidental-guide-write/references/voice.md` (binding voice).
3. `packages/accidental-guides/guides/agents-harnesses-skills-tools/guide.md`, the base guide.
   Never contradict it and don't repeat it. Point to it for the basics (agent, harness, skill,
   tool, session, context window) as "An Accidental Guide to: Agents, Harnesses, Skills, and
   Tools".
4. `packages/accidental-guides/guides/lights-off-software-factories/guide.md`, an example of a
   finished short guide in the same format.
5. `drafts/claude-code/notes/sources.md`: the only facts you may use about Claude
   Code. Don't add facts from memory.

## What the guide is for

The author's own words on the problem: where skills, MCP servers and the rest of the harness
setup live is a mess and a headache. This guide is the calm page you open to look things up.
It answers: what can I set up in Claude Code, where does each file go, and which one wins when
the same thing is set in two places. A reader should find a path in seconds.

It's one of five sibling guides with the same shape: Claude Code, Claude Desktop, GitHub
Copilot CLI, Codex, and Visual Studio and VS Code.

## Length

Five minutes, front to back: about 1,100 printed words in total, tables and sources included.
Rough budget: page 2 about 150 words, each entry about 95 words, the where page about 170, the
scopes page about 150, the elsewhere page about 90, sources about 80. Cut detail, not clarity.

## Rules for the text

- Regular English, one idea at a time, to a smart colleague who is new to this. Say "you".
- No paragraph by list. If it's a list, it's a table row. Otherwise connected sentences.
- No "A person can", no "this guide", no page talk, no hooks, trivia, sarcasm, snark, slogans,
  rhetorical questions, "not X but Y", em dashes, rhythm triplets, borrowed framing.
- No quotes or names of people. No Microsoft-internal anything.
- Cross-references in body text use the colon form: "An Accidental Guide to: Codex".
- Say "as of October 2026" once on page 2, where it helps; don't repeat it everywhere.
- One name per scope, used everywhere: "you, in every project" for user, "the project" for the
  shared committed files, "you, in this project" for local, and "your organization" for managed.
  The scope words "user", "project", "local" and "managed" may appear once each where you name
  them, because the docs and the `--scope` flags use them.
- Format rules the parser needs: no Markdown emphasis or backticks (bold and mono are applied
  automatically; anything shaped like a path or file name is set in mono), no lists, no `&`
  before letters, no `<` (so write `~/.claude/skills/` and not `<name>`), no slashes in ordinary
  words ("and/or" is out). Use typographic quotes and apostrophes (’ “ ”). A Short answer cell
  never ends with a full stop. No "e.g." in the first sentence of a What or So what row (the
  builder bolds up to the first ". ").
- In entries, rows must read on their own: no sentence starts with "It", "Its", "They" or
  "This".

## The exact structure

Keep this skeleton exactly: the front matter values, the headings and ids, the table shapes and
the number of paragraphs in each section. Fill in the text marked with …

```
---
title: Claude Code
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to where Claude Code keeps its setup, as of October 2026.
running_footer: Accidental Guide to Claude Code
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: October 2026
version: 0.1.0
---

# What can you set up<br/>in Claude Code? {#why}

… paragraph 1: answers the title in plain words. Claude Code reads its setup from plain files,
some in your home folder and some in the project. Name the five things. This paragraph is also
shown alone on the website, so it must stand on its own. …

… paragraph 2: each of the five can be kept for yourself, shared with a project, or set by
your organization, and each kind lives in a different place, which is why it gets confusing.
Point to An Accidental Guide to: Agents, Harnesses, Skills, and Tools for what a skill, a tool
and an MCP server are. …

| Term | Meaning |
|---|---|
| Instructions file | … one line |
| Skill | … |
| MCP server | … |
| Plugin | … |
| Settings | … one line; mention permissions and hooks |

# Instructions file {#entry num=01 mono=In}

| Field | Text |
|---|---|
| Identify by | … CLAUDE.md, or AGENTS.md |
| What | … |
| So what | … |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Loads | … | … |
| Cannot | … | … |

## Confused with: Settings

… one paragraph …

# Skill {#entry num=02 mono=Sk}
(same shape; Confused with: Instructions file)

# MCP server {#entry num=03 mono=Mc}
(same shape; Confused with: Plugin)

# Plugin {#entry num=04 mono=Pl}
(same shape; Confused with: Skill. A skill is one folder you can copy into a skills folder
yourself. A plugin is a package, usually installed from a marketplace, that can carry skills,
agent definitions, hooks and MCP servers together. Explain a marketplace inside the What or So
what row; it has no page of its own.)

For MCP server, the Confused with paragraph says that a plugin can bring an MCP server with it,
and that you add or remove that server by installing or uninstalling the plugin, not with
claude mcp commands.

# Settings {#entry num=05 mono=Se}
(same shape; Confused with: Instructions file)

# Where do the<br/>files live? {#where}

… one short paragraph: most setup sits in two folders called .claude, one in your home folder
(~/.claude/) and one in the project, plus a few files beside them. …

| You, in every project | Where |
|---|---|
| Instructions | ~/.claude/CLAUDE.md |
| Skills | ~/.claude/skills/ |
| MCP servers | ~/.claude.json (… short note) |
| Plugins | … |
| Settings | ~/.claude/settings.json |

| The project | Where |
|---|---|
| Instructions | … |
| Skills | .claude/skills/ |
| MCP servers | .mcp.json … |
| Plugins | … |
| Settings | .claude/settings.json, and .claude/settings.local.json for you, in this project |

| Your organization | Where |
|---|---|
| Folder | … the three system folders by OS |
| Instructions | CLAUDE.md in that folder |
| Skills | .claude/skills/ in that folder |
| MCP servers | managed-mcp.json in that folder |
| Settings | managed-settings.json in that folder, or … MDM or the claude.ai admin console |

… one closing paragraph: how to check what loaded (/status for settings, /context for
instruction files, /mcp for servers, /plugin for plugins). …

# Which one wins? {#scopes}

… one short paragraph: when the same thing is set in more than one place, the answer depends
on the kind of thing. Some things add up, and for others one place wins. …

| Thing | When it’s set in more than one place |
|---|---|
| Settings | … order, highest first; lists such as permission rules combine |
| Permission rules | … deny, then ask, then allow, whichever file each comes from |
| Hooks | … all of them run |
| Instructions | … all load, none overrides; the closest is read last; organization’s can’t be excluded |
| Skills | … same name: organization, then you, then the project; plugin skills keep their own name |
| MCP servers | … same name: you in this project, then the project, then you in every project, then plugins; whole entry, no merge |
| Plugins | … you in this project, then the project, then you in every project |

… one closing paragraph: your organization’s settings sit above everything, and nothing in
your own files changes them. …

# The same things<br/>in other tools {#elsewhere}

… one short paragraph: the other tools have the same five kinds of thing under other names and
in other places. Each has its own guide. …

| Guide | What to look for there |
|---|---|
| (rows supplied below under "Elsewhere facts") | |

… one closing paragraph: AGENTS.md is the one file several tools read; Claude Code reads it when
there’s no CLAUDE.md. …

# Sources {#sources}

These pages were checked in October 2026. Claude Code changes often, so check the current
documentation before you rely on a path.

| Source | Date | Address |
|---|---|---|
| Anthropic, Claude Code: Settings | October 2026 | code.claude.com/docs/en/settings |
| … one row per page in sources.md, same form, no https:// … |
```

The where, scopes and elsewhere sections must each have at least one paragraph before the
table(s) and exactly one paragraph after the last table. The why section has paragraphs, then
one table, and nothing after it.

## Elsewhere facts

The facts for the other tools are still being checked. For now, write the elsewhere intro and
closing paragraphs, and put four rows in the table with these first cells and the second cell
"TBD": "An Accidental Guide to: Claude Desktop", "An Accidental Guide to: GitHub Copilot CLI",
"An Accidental Guide to: Codex", "An Accidental Guide to: Visual Studio and VS Code". Don't name
any file or path for the other tools.

## When you're done

Reply with one line: the number of words in guide.md (`wc -w guide.md`).
