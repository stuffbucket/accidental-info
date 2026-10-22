# Edits, round 4: Claude Code

Apply these edits in place to `guide.md` (your working directory's `./guide.md`). Line numbers
are from the file as it is now (commit 92e1d55, version 0.1.1). Replace each listed line with
the new text, keeping the table row structure: label cells stay as they are unless the edit
gives a new label. Lines that start with `> ` are part of a grey block: keep the `> ` at the
start of every such line, including new ones. Change nothing else. Don't touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`
and `packages/editorial/skills/accidental-guide-write/references/voice.md` first.
Every rule there applies to any text you write or shorten.

## Why

The body prints about 1,270 words and must come down to about 1,100 (five minutes). The field
marks become a grid with short answers only, so their Detail column goes. Four of the five
things are now defined in their own guides, so each of those entries points to that guide by
title and covers only what Claude Code does. Settings has no guide of its own, so its What row
defines it in one plain line. Two guide titles on the last page are wrong.

## Front matter

1. Line 8: `version: 0.2.0`

## Page 2 (lines 13 to 23)

2. Line 13: Claude Code reads its setup from plain files, some in your home folder and some in the project. There are five kinds: instructions files, skills, MCP servers, plugins and settings.
3. Line 15: Each kind can be yours alone, shared with the project, or set by your organization. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains the basic terms.

## Instructions file (lines 25 to 42)

4. Line 30, What row: | What | An instructions file holds what Claude Code should know in every session, such as build commands. Claude Code reads AGENTS.md only when there’s no CLAUDE.md. See An Accidental Guide to: Agents, Harnesses, Skills, and Tools. |
5. Lines 35 to 38, the field marks table. Replace the four lines with these four (two columns, no Detail):
   > | Field | Short answer |
   > |---|---|
   > | Loads | Every session, from your folder and each folder above it |
   > | Cannot | Enforce a rule |

## Skill (lines 44 to 61)

6. Line 49, What row: | What | A skill is a written procedure that Claude Code loads when a task needs it, or when you type its name, such as /deploy. See An Accidental Guide to: Agent Skills. |
7. Line 50, So what row: | So what | Steps needed only for some tasks belong in a skill, so they don’t fill every session. |
8. Lines 54 to 57, the field marks table:
   > | Field | Short answer |
   > |---|---|
   > | Loads | Name and description at startup, the rest when used |
   > | Cannot | Add a tool |

## MCP server (lines 63 to 80)

9. Line 68, What row: | What | An MCP server is a separate program that gives Claude Code tools for another system. Add one with claude mcp add. See An Accidental Guide to: Model Context Protocol. |
10. Lines 73 to 76, the field marks table:
    > | Field | Short answer |
    > |---|---|
    > | Loads | When the session starts |
    > | Cannot | Act until the model calls one of its tools |

## Plugin (lines 82 to 99)

11. Line 87, What row: | What | A plugin packages skills, agent definitions, hooks and MCP servers to install as one unit. Most come from a marketplace, which you add with /plugin marketplace add. See An Accidental Guide to: Plugins, Connectors, and Marketplaces. |
12. Line 88, So what row: | So what | An enabled plugin is part of every session and runs as you. Check what a plugin adds before you install it. |
13. Lines 92 to 95, the field marks table:
    > | Field | Short answer |
    > |---|---|
    > | Loads | At startup, once a settings file turns it on |
    > | Cannot | Install itself for teammates |
14. Line 99: A skill is one folder you can copy in yourself. A plugin is a package that can carry many skills and other parts.

## Settings (lines 101 to 118)

15. Line 106, What row (the one line that defines settings): | What | Settings are JSON files that decide which commands run without asking, which hooks run and which plugins are on. |
16. Lines 111 to 114, the field marks table:
    > | Field | Short answer |
    > |---|---|
    > | Loads | At startup, and again when you save |
    > | Cannot | Override your organization |

## Where do the files live? (lines 120 to 149)

17. Line 122: Most setup sits in two .claude/ folders, one in your home folder and one in the project.

## Which one wins? (lines 151 to 165)

18. Line 158, Permission rules row: | Permission rules | Deny is checked first, then ask, then allow, so a deny anywhere blocks the call. |
19. Line 162, MCP servers row: | MCP servers | Same name: local, then project, then user, then plugins. |
20. Line 165: Run /status to see which managed settings apply.

## The same things in other tools (lines 167 to 178)

21. Line 169: Each of these tools has its own guide.
22. Line 173, the second cell only: Most setup is in the app. Local MCP servers go in claude_desktop_config.json.
23. Line 175, the first cell only: An Accidental Guide to: OpenAI Codex
24. Line 176, the first cell only: An Accidental Guide to: VS Code and Visual Studio

## Check before you finish

- Every line not named above is unchanged.
- The `> ` prefix is on every line of each field marks table, and each of those tables has
  exactly two columns.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
