# Writer instructions, round 1

You are writing `guide.md` for a new pocket guide: An Accidental Guide to… VS Code and Visual
Studio. Write the file at
`packages/accidental-guides/guides/visual-studio-and-vs-code/guide.md` (relative to the repo
root the repository root).
Write only that file. Don't touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

## Read first

1. `drafts/visual-studio-and-vs-code/notes/plan.md`: the page plan.
2. `drafts/visual-studio-and-vs-code/notes/sources.md`: the only facts you may use,
   plus the facts for page 11 below. Don't add facts from memory. Paths, file names and setting
   names must be copied exactly.
3. `packages/editorial/skills/accidental-guide-plan/references/series-rules.md` and `packages/editorial/skills/accidental-guide-write/references/voice.md`:
   the voice rules. They are binding.
4. `packages/accidental-guides/guides/agents-harnesses-skills-tools/guide.md`: the base guide.
   Don't contradict it and don't repeat it. Point to it in the colon form ("An Accidental Guide
   to: Agents, Harnesses, Skills, and Tools") for the basics.
5. `packages/accidental-guides/guides/lights-off-software-factories/guide.md`: the format to
   copy (front matter, `{#why}`, entries). Its length per entry is about right.

## The reader and the job

The reader uses GitHub Copilot’s agent in VS Code or Visual Studio and has found its setup
scattered across many folders and settings. They want to look things up calmly: what each thing
is, where it goes, and what happens when two places disagree. Smart colleague, new to this.
Write in regular English, one idea at a time, the way you'd explain it over coffee. Say “you”.

Five minutes front to back: about 1,100 printed words in total, tables included. Budgets: page 2
about 150 words, each entry about 90, where-things-live about 170, scopes about 120, Visual
Studio about 140, elsewhere about 90, sources intro one sentence. Cut detail, not clarity.

## Avoid

Paragraph by list (if it's a list, make it a table row). Stiff generic subjects (“A person
can”, “One may”, “Users can”). Self-narration (“this guide”, “this page”, “below”, page numbers).
Hooks, teaser titles, trivia, sarcasm, snark. Borrowed framing (birds, field guides, travel,
maps, kitchens). Slogans, rhetorical questions, “not X but Y”, em dashes, rhythm triplets,
stacked metaphors. Quotes or names of people. Anything non-public from Microsoft. Jargon the
reader hasn't been given. Rows that start with “It”, “Its”, “They” or “This”.

## Markdown rules (the parser is strict)

- Front matter exactly as given below. Every `#` heading ends with `{#id}`.
- No backticks, no bold or italics, no lists, no `&`, no `<` or `>` characters anywhere in the
  text (write “Tools, then Options” style paths as “Tools › Options › GitHub › Copilot”).
- No slashes in ordinary words (no “and/or”). Anything with a slash is set in a code font.
- Typographic quotes and apostrophes (’ “ ”).
- A “Short answer” cell must not end with a full stop. Don't put “e.g.” or “i.e.” anywhere.
- Each entry’s What and So what: the first sentence is printed bold, so make it the short answer.
- Table cells can't contain `|`.
- Part names that label a table row must be spelled exactly: Instructions file, Custom agent,
  Skill, MCP server, Setting (singular). Other row labels (Prompt file, Hook) are plain text.
- In the where, scopes, vs and elsewhere tables, a row whose first cell is empty continues the
  group above it (no rule, no tile). Use that to group a part's rows.

## Skeleton (keep every id and column count)

```
---
title: VS Code and Visual Studio
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to where GitHub Copilot’s agent setup lives, as of October 2026.
running_footer: VS Code and Visual Studio
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: October 2026
version: 0.1.0
---

# What can you set up<br/>in VS Code? {#why}

(two or three short paragraphs; the first stands on its own as the site summary and answers the
title question in plain words; mention the harness choice once: VS Code runs the Copilot
harness by default, which reads Copilot’s folders, .github/ in the repo and ~/.copilot/ in your
home folder; everything in the guide is for that harness unless it says otherwise; point to the
base guide for the basics)

| Term | Meaning |
|---|---|
| Instructions file | … |
| Custom agent | … |
| Skill | … |
| MCP server | … |
| Setting | … |

# Instructions file {#entry num=01 mono=In}

| Field | Text |
|---|---|
| Identify by | … |
| What | … |
| So what | … |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Loaded | … | … |
| Cannot | … | … |

## Confused with: Setting

(one or two sentences)

# Custom agent {#entry num=02 mono=Ag}
(same shape; confused with: Instructions file, or with a sub-agent as the base guide uses it;
say they were called chat modes and .chatmode.md files become .agent.md)

# Skill {#entry num=03 mono=Sk}
(same shape; Confused with: Prompt file — prompt files, .github/prompts/*.prompt.md, run as
/name only in the Local harness, and VS Code suggests a skill instead)

# MCP server {#entry num=04 mono=Mc}
(same shape; mention the gallery: Extensions view, search @mcp, Install or Install in
Workspace; .mcp.json uses mcpServers, the older .vscode/mcp.json uses servers; Confused with:
Extension or with Skill)

# Setting {#entry num=05 mono=Se}
(same shape; settings switch features on and off and choose what gets read; user settings vs
.vscode/settings.json; Confused with: Instructions file)

# Where things live {#where}

(one short paragraph)

| Thing | Scope | Location |
|---|---|---|
| Instructions file | Repo | .github/copilot-instructions.md |
|  |  | AGENTS.md … |
|  | You | ~/.copilot/copilot-instructions.md … |
|  | Organization | … |
| Custom agent | Repo | … |
(and so on for all five parts; keep each Location cell short, paths under 45 characters;
put two paths in one cell separated by “ or ” or a comma when they're alternatives)

(exactly one closing paragraph: where the Local harness and the Claude harness differ)

# How scopes combine {#scopes}

(one short paragraph: instructions add up, settings override)

| Thing | When more than one scope has one |
|---|---|
| Instructions file | … |
| Custom agent | … |
| Skill | … |
| MCP server | … |
| Setting | … |

(exactly one closing paragraph: what to do about conflicts)

# What’s different<br/>in Visual Studio {#vs}

(one short paragraph)

| Thing | In Visual Studio |
|---|---|
| Instructions file | … |
| Prompt file | … |
| Custom agent | … |
| Skill | … |
| MCP server | … |
| Setting | … |

(exactly one closing paragraph)

# Same thing elsewhere {#elsewhere}

(one short paragraph)

| Thing | In the other tools |
|---|---|
| Instructions file | … |
| Custom agent | … |
| Skill | … |
| MCP server | … |
| Setting | … |

(exactly one closing paragraph that names the sibling guides in colon form: An Accidental Guide
to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to: GitHub Copilot
CLI, An Accidental Guide to: Codex)

# Sources {#sources}

These public pages were checked on 22 October 2026.

| Source | Publisher | Address |
|---|---|---|
| (title) | (publisher) | (address without https://) |
```

The `{#where}`, `{#scopes}`, `{#vs}` and `{#elsewhere}` sections each need one or more intro
paragraphs, exactly one table, and exactly one paragraph after the table. Sources: about ten
rows, the most useful pages from sources.md.

## Page 11 (Same thing elsewhere)

Leave the `{#elsewhere}` section out of this round entirely. It will be added in the next round
when its facts are ready. Write every other section.
