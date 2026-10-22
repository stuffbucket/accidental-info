# Edits, round 4: Claude Desktop

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

The body prints about 1,200 words and must come down to about 1,100 (five minutes). The field
marks become a grid with short answers only, so their Detail column goes, and the one fact in a
detail that a reader needs moves into the So what row. Four of the five things are now defined
in their own guides, so each of those entries points to that guide by title and covers only
what Claude Desktop does. Settings has no guide of its own, so its What row defines it in plain
words. Two guide titles on the elsewhere page are wrong.

## Front matter

1. Line 8: `version: 0.2.0`

## Page 2 (lines 13 to 23)

2. Line 13: In Claude Desktop you can tell Claude how to answer you, save the steps for tasks you repeat, connect Claude to the apps you use, and choose what Claude may do without asking. Most of these settings belong to your Claude account and also apply on claude.ai.
3. Line 15: You’ll find them in Settings and in Customize, in the left sidebar. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains the basic terms.

## Instructions (lines 25 to 41)

4. Line 30, What row: | What | Instructions are text you write for Claude to follow. The ones in Settings apply to all your chats, and project instructions only inside that project. See An Accidental Guide to: Agents, Harnesses, Skills, and Tools. |
5. Line 31, So what row: | So what | Put a preference you always want in Settings, and one for a single piece of work in that project. |
6. Lines 35 to 37, the field marks table. Replace the three lines with these three (two columns, no Detail):
   > | Field | Short answer |
   > |---|---|
   > | Works in | Web, desktop and mobile |

## Skills (lines 43 to 59)

7. Line 48, What row: | What | A skill is a saved set of steps for one kind of task. Turn on an example skill or upload your own, and Claude follows it when that task comes up. See An Accidental Guide to: Agent Skills. |
8. Line 49, So what row: | So what | You explain a task once instead of in every chat. Skills need Code execution and file creation, in Settings > Capabilities. |
9. Lines 53 to 55, the field marks table:
   > | Field | Short answer |
   > |---|---|
   > | Works in | Web, desktop and Claude Code |

## Connectors (lines 61 to 77)

10. Line 66, What row: | What | A connector is an MCP server on the internet, usually for a service you sign in to. You add it once and it works wherever you use Claude. See An Accidental Guide to: Model Context Protocol. |
11. Lines 71 to 73, the field marks table:
    > | Field | Short answer |
    > |---|---|
    > | Works in | Web, desktop and mobile |
12. Line 77: A desktop extension is a local MCP server in a .mcpb file, installed in Settings > Extensions. Extensions work only on this computer, in Claude Desktop and Claude Code.

## Plugins (lines 79 to 95)

13. Line 84, What row: | What | A plugin is a package of skills, connectors and sub-agents, saved to your account. See An Accidental Guide to: Plugins, Connectors, and Marketplaces. |
14. Line 85, So what row: | So what | One install sets up what you need for a role. Plugins need a paid plan, and your organization may install some for you. |
15. Lines 89 to 91, the field marks table:
    > | Field | Short answer |
    > |---|---|
    > | Works in | Chat, Cowork and Claude Code |

## Settings and permissions (lines 97 to 113)

16. Line 102, What row (the line that defines settings): | What | Settings holds your account’s preferences, such as General, Capabilities and Memory. Extensions and Developer apply to this computer only. |
17. Lines 107 to 109, the field marks table:
    > | Field | Short answer |
    > |---|---|
    > | Works in | Your account and this computer |

## Where things live (lines 115 to 136)

18. Line 117: Most things live in your Claude account and show up wherever you sign in. A few live on this computer only.
19. Line 130, the MCP logs row: delete this line.
20. Line 133: Chats and Cowork use what’s in Customize. The Code tab reads ~/.claude, as Claude Code does. See An Accidental Guide to: Claude Code.

## Your account or your organization? (lines 138 to 150)

21. Line 150: On computers your company manages, IT can set the desktop app’s options in com.anthropic.claudefordesktop on macOS or HKLM\SOFTWARE\Policies\Claude on Windows. These override the allowlist in the app. If something is missing, ask your owner.

## Same thing elsewhere (lines 152 to 164)

22. Line 158, the second cell only: CLAUDE.md in Claude Code. AGENTS.md in Codex, Copilot CLI and VS Code.
23. Line 159, the second cell only: A folder with a SKILL.md file, under ~/.claude/skills in Claude Code. Codex, Copilot CLI and VS Code have skills too.
24. Line 164: See An Accidental Guide to: Claude Code, An Accidental Guide to: GitHub Copilot CLI, An Accidental Guide to: OpenAI Codex and An Accidental Guide to: VS Code and Visual Studio.

## Check before you finish

- Every line not named above is unchanged.
- The `> ` prefix is on every line of each field marks table, and each of those tables has
  exactly two columns.
- No line of a paragraph starts with `>` unless it is part of a grey block or the tip.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
