# Writer instructions, round 1: An Accidental Guide to… OpenAI Codex

You are writing `guide.md` in this folder (packages/accidental-guides/guides/codex/). Replace
the whole file. Do not touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

## Read first

1. `packages/editorial/briefs/new-guide.md` (what the author wants)
2. `packages/editorial/skills/accidental-guide-plan/references/series-rules.md` and
   `packages/editorial/skills/accidental-guide-write/references/voice.md` (binding writing rules)
3. `packages/accidental-guides/guides/agents-harnesses-skills-tools/guide.md` (the base guide;
   never contradict it, never repeat it, point to it for the basics)
4. `drafts/codex/notes/plan.md` (the page plan)
5. `drafts/codex/notes/sources.md` (the ONLY facts you may use; every path,
   command and key must come from here)
6. `packages/accidental-guides/guides/lights-off-software-factories/guide.md` (a finished guide
   in the same format, for shape and tone)

## Who it's for

Someone who uses Codex, or is about to, and keeps losing track of where an instruction, a
skill, an MCP server or a setting lives, and which copy wins. They are not an expert. The
guide should feel calm and make things easy to look up. Five minutes to read, front to back.

## Length

About 1,100 printed words in total, tables included. That is tight. Budget roughly:
page 2 about 130 words; each entry about 100 words; where about 170; combine about 150;
elsewhere about 70; sources about 90. Cut detail, not clarity.

## What Codex means here

The Codex CLI, the Codex IDE extension and Codex in the ChatGPT desktop app share one set of
config files under your Codex home folder (~/.codex unless CODEX_HOME says otherwise) and the
project. Codex Cloud runs tasks in a VM and keeps its settings in a web settings page
(Settings, Codex Cloud, Environments); it uses the skills in the repository but not your
personal ones. Say "as of October 2026" once or twice where things change often (the docs
moved, plugins, permission settings), not everywhere.

## Exact format (the parser is strict)

Copy this skeleton. Section ids, attributes, table headers, the number of paragraphs and the
row labels must stay exactly as shown. Replace each ✎ with text.

```
---
title: OpenAI Codex
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to where Codex keeps its setup, and which copy wins, as of October 2026.
running_footer: OpenAI Codex
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: October 2026
version: 0.1.0
---

# What can you set up<br/>in Codex? {#why}

✎ paragraph 1: stands on its own as the site blurb. What you can set up in Codex, in plain
words, and that it's all plain files the CLI, IDE extension and desktop app share.

✎ paragraph 2: the two main places (your Codex home folder, the project) and where the basics
are explained: An Accidental Guide to: Agents, Harnesses, Skills, and Tools.

| Term | Meaning |
|---|---|
| Instructions file | ✎ one sentence |
| Skill | ✎ |
| MCP server | ✎ |
| Config file | ✎ |
| Permissions | ✎ |

# Instructions file {#entry num=01 mono=In}

| Field | Text |
|---|---|
| Identify by | ✎ short, names the files |
| What | ✎ 2–3 sentences; the first sentence is printed bold |
| So what | ✎ 2 sentences; the first sentence is printed bold |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Loads | ✎ short answer, no full stop | ✎ one sentence |
| Add with | /init | ✎ one sentence |

## Confused with: Skill

✎ one or two sentences.

(… same shape for:)
# Skill {#entry num=02 mono=Sk}          Field marks: Loads, Check with (/skills or $)   Confused with: Plugin
# MCP server {#entry num=03 mono=Mc}     Field marks: Add with (codex mcp add), Check with (/mcp)   Confused with: Tool
# Config file {#entry num=04 mono=Cf}    Field marks: Loads (restart after a change), Override with (-c or --profile)   Confused with: Requirements file
# Permissions {#entry num=05 mono=Pe}    Field marks: Default, Change with (/permissions, --sandbox, --ask-for-approval)   Confused with: Rules

# Where things live {#where}

✎ one short intro paragraph.

| Scope | Thing | Path |
|---|---|---|
(rows below; keep each scope's rows together; you may shorten the Path wording but keep
every path exactly as given)

✎ exactly one closing paragraph: the project's .codex folder only loads once you trust the
project; user and organization files still load.

# How do the places combine? {#combine}

✎ one short intro paragraph.

| Thing | When two places set it |
|---|---|
(rows below)

✎ exactly one closing paragraph.

# Same thing elsewhere {#elsewhere}

✎ one short intro paragraph.

| Codex | Claude Code | Claude Desktop | Copilot CLI | VS and VS Code |
|---|---|---|---|---|
(use the table given below unchanged)

✎ exactly one closing paragraph naming the sibling guides in colon form.

# Sources {#sources}

These public sources were checked on 22 October 2026.

| Source | Publisher | Address |
|---|---|---|
(rows below)
```

## Rows to use

Where things live (Scope, Thing, Path). Thing names that are parts must be spelled exactly:
Instructions, Skills, MCP servers, Config file, Permissions. Other things are plain words.

| Scope | Thing | Path |
|---|---|---|
| Just you | Instructions | ~/.codex/AGENTS.md, or AGENTS.override.md beside it |
| Just you | Skills | ~/.agents/skills/ |
| Just you | Config file | ~/.codex/config.toml, which also holds MCP servers and permissions |
| Just you | Profiles | ~/.codex/profile-name.config.toml |
| Just you | Hooks, rules, agents | ~/.codex/hooks.json, ~/.codex/rules/, ~/.codex/agents/ |
| Just you | Plugins | installed under ~/.codex/plugins/cache/ |
| This project | Instructions | AGENTS.md in the root and in any folder down to where you work |
| This project | Skills | .agents/skills/ in any folder from where you work up to the root |
| This project | Config file | .codex/config.toml, in the root or a subfolder |
| This project | Hooks, rules, agents | .codex/hooks.json, .codex/rules/, .codex/agents/ |
| This project | Plugins | a list to install from in .agents/plugins/marketplace.json |
| Your organization | Config file | /etc/codex/config.toml, or defaults from the admin console |
| Your organization | Skills | /etc/codex/skills/ |
| Your organization | Requirements | /etc/codex/requirements.toml, or the admin console |
| Codex Cloud | Environment | Settings, Codex Cloud, Environments, on the web or in the desktop app |
| Codex Cloud | Skills | the repository’s skills only; personal skills aren’t synced |

How do the places combine (Thing, When two places set it). Facts to cover, one row each, in
plain sentences:
- Config file: one value wins. Order, strongest first: flags and -c; the project’s
  .codex/config.toml (the one closest to where you work wins); a profile picked with
  --profile; ~/.codex/config.toml; your organization’s defaults; built-in defaults.
- Instructions: Codex joins them, ~/.codex/AGENTS.md first, then from the root down to your
  folder, so closer files come later and win; one file per folder (AGENTS.override.md beats
  AGENTS.md); stops at 32 KiB in total by default.
- Skills: all of them are offered; two with the same name both show up, nothing merges.
- MCP servers: they live in the config file, so they follow its order; a project can add its
  own in .codex/config.toml.
- Hooks: they add up; a stronger place doesn’t replace a weaker one’s hooks.
- Rules: Codex reads every rules/ folder; when two match, the strictest wins (forbidden, then
  prompt, then allow).
- Requirements: limits an admin sets; your files can’t override them, and Codex falls back to
  an allowed value and tells you.

Same thing elsewhere: use exactly this table.

| Codex | Claude Code | Claude Desktop | Copilot CLI | VS and VS Code |
|---|---|---|---|---|
| Instructions file | CLAUDE.md | Project instructions | Instructions file | Instructions file |
| Skill | Skill | Skill | Skill | Skill |
| MCP server | MCP server | Connector | MCP server | MCP server |
| Config file | Settings file | App settings | Settings | Settings |
| Permissions | Permissions | Tool permissions | Tool approval | Tool approval |

Closing paragraph names: An Accidental Guide to: Claude Code; An Accidental Guide to: Claude
Desktop; An Accidental Guide to: GitHub Copilot CLI; An Accidental Guide to: Visual Studio and
VS Code. Write it as a normal sentence.

Sources (Source, Publisher, Address — address without https://):

| Source | Publisher | Address |
|---|---|---|
| Config basics | OpenAI | learn.chatgpt.com/docs/config-file/config-basic |
| Advanced Configuration | OpenAI | learn.chatgpt.com/docs/config-file/config-advanced |
| Custom instructions with AGENTS.md | OpenAI | learn.chatgpt.com/docs/agent-configuration/agents-md |
| Build skills | OpenAI | learn.chatgpt.com/docs/build-skills |
| Model Context Protocol | OpenAI | learn.chatgpt.com/docs/extend/mcp |
| Agent approvals and security | OpenAI | learn.chatgpt.com/docs/agent-approvals-security |
| Package your plugin | OpenAI | developers.openai.com/plugins/build/plugins |
| Hooks | OpenAI | learn.chatgpt.com/docs/hooks |
| Rules | OpenAI | learn.chatgpt.com/docs/agent-configuration/rules |
| Cloud environments | OpenAI | learn.chatgpt.com/docs/environments/cloud-environments |
| Managed configuration | OpenAI | learn.chatgpt.com/docs/enterprise/managed-configuration |

## Content for the entries (facts from sources.md)

- Instructions file: AGENTS.md. Codex reads ~/.codex/AGENTS.md, then AGENTS.md files from the
  project root down to the folder you're in, and joins them. It's guidance the model reads
  every session, such as build and test commands and conventions. Keep it small. /init writes
  a starter AGENTS.md. Confused with Skill: an instructions file is read every session; a
  skill's steps are read only when the skill is used.
- Skill: a folder with SKILL.md (name and description at the top). Codex reads names and
  descriptions at the start and the rest when the skill is chosen, either because the task
  matches the description or because you type $ and the skill's name, or use /skills. Your
  own skills go in ~/.agents/skills/, the project's in .agents/skills/. Turn one off with a
  [[skills.config]] entry with enabled = false. Confused with Plugin: a plugin is how skills
  (and MCP servers and hooks) are packaged and installed; you browse plugins with /plugins in
  the CLI. The IDE extension doesn't support plugins (as of October 2026).
- MCP server: an entry in config.toml, a [mcp_servers.docs] table (use "docs" as the example
  name) with either a command (local) or a url (remote). codex mcp add writes one; /mcp shows
  connected servers. The CLI, IDE extension and desktop app share these. enabled_tools and
  disabled_tools limit which tools a server offers. Confused with Tool: the server is the
  program; its tools are what the model calls.
- Config file: config.toml, in TOML. Holds the model, MCP servers, permissions, feature flags
  and more. Yours is ~/.codex/config.toml; a project's is .codex/config.toml. A profile is a
  second file, ~/.codex/profile-name.config.toml, that you pick with --profile and that holds
  only the values that differ. -c key=value overrides one setting for one run. In the IDE
  extension, the gear icon, then Codex Settings, then Open config.toml. Restart Codex after a
  change. Confused with Requirements file: requirements.toml is set by an admin and sets
  limits you can't change; config.toml sets defaults you can.
- Permissions: two settings. The sandbox (sandbox_mode: read-only, workspace-write,
  danger-full-access) decides what commands can touch; approvals (approval_policy:
  on-request, never) decide when Codex stops to ask. Network access is off by default. In a
  Git folder Codex starts with workspace-write and on-request; elsewhere read-only. Change in
  a session with /permissions, or start with --sandbox and --ask-for-approval. Confused with
  Rules: rules are .rules files that say which commands may run outside the sandbox (allow,
  prompt or forbidden); they're experimental (as of October 2026).

## Text rules the builder enforces

- No backticks, no * or _ emphasis, no lists (a line starting "- " prints literally).
- No "&" before letters. No "<" anywhere except "<br/>" in # titles. Don't write
  "<server-name>" or similar; use a real example name.
- No slashes in ordinary words (and/or, CI/CD). Paths are fine and print in mono.
- No "|" inside a table cell.
- A Short answer cell must not end with a full stop.
- No "e.g. " or "i.e. " in the first sentence of a What or So what row.
- Use typographic quotes and apostrophes (’ “ ”).
- Rows must read on their own: no sentence starts with "It", "Its", "They" or "This".
- No "this guide", no page numbers, no talk about the layout.
