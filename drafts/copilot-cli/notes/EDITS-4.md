# Edits, round 4: GitHub Copilot CLI

Apply these edits in place to `packages/accidental-guides/guides/copilot-cli/guide.md` (your
working directory's `./guide.md`). Line numbers are from the file as it is now (commit
after 588d180, version 0.1.0). Replace each listed line with the new text, keeping the table
row structure and any `> ` at the start of a line: label cells stay as they are unless the edit
gives a new label. Change nothing else. Don't touch any other file, and don't change the
`version:` line.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`
and `packages/editorial/skills/accidental-guide-write/references/voice.md` first.
Every rule there applies to any text you write or shorten.

## Why

The body is about 1,190 printed words and must come down to about 1,100, a five-minute read.
Each entry now has to fit half a page, so the field marks keep only their short answer. Four of
the five parts are explained in their own guides, so those entries now say what is specific to
Copilot CLI and name the guide that explains the part, in the colon form. Settings has no guide
of its own, so its entry defines it in one plain line. Some lines also break the lint: semicolons,
"Just you" ("just" is filler), "key", and wrong guide titles.

## Instructions file (lines 28 to 45)

1. Line 33: | What | Copilot CLI reads every instructions file that applies and adds them all to the session. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains instructions files. |
2. Lines 38 to 41, the field marks, become exactly these four lines (the Detail column goes):

   > | Field | Short answer |
   > |---|---|
   > | Loads | At the start of a session |
   > | Check with | /instructions |

## Skill (lines 47 to 65)

3. Line 52: | What | Copilot CLI uses a skill when its description matches your request, or when you type its name, such as /release-notes. An Accidental Guide to: Agent Skills explains skills. |
4. Lines 57 to 60 become:

   > | Field | Short answer |
   > |---|---|
   > | Loads | Description first, steps when used |
   > | Check with | /skills |

## MCP server (lines 67 to 85)

5. Line 72: | What | GitHub’s own MCP server is built in and needs no setup. Copilot CLI starts the others listed in its config files. An Accidental Guide to: Model Context Protocol explains MCP servers. |
6. Line 73: | So what | Add a server when the work needs a system Copilot CLI can’t reach on its own, such as an issue tracker. |
7. Lines 77 to 80 become:

   > | Field | Short answer |
   > |---|---|
   > | Loads | When the session starts |
   > | Check with | /mcp |

## Custom agent (lines 87 to 105)

8. Line 92: | What | Copilot CLI reads custom agents from your Copilot folder, the repository and your organization. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains agents, and calls this file an agent definition. |
9. Lines 97 to 100 become:

   > | Field | Short answer |
   > |---|---|
   > | Loads | When you pick it or it’s handed work |
   > | Check with | /agent |

## Settings (lines 107 to 125)

10. Line 112: | What | Settings are the choices that control how Copilot CLI runs, such as the model. Trusted folders are kept in config.json, and tools you’ve allowed to run without asking in permissions-config.json. |
11. Lines 117 to 120 become:

    > | Field | Short answer |
    > |---|---|
    > | Loads | When the session starts |
    > | Check with | /settings |

## Where things live (lines 127 to 151)

12. Lines 134 to 138: change the first cell, "Just you", to "Your home folder". Nothing else
    changes on lines 134 to 137.
13. Line 138, all of it: | Your home folder | Settings | ~/.copilot/settings.json, with approvals in permissions-config.json and trusted folders in config.json beside it |
14. Delete line 139 (the Plugins row). Plugins aren't one of the five parts.

## How do the places combine? (lines 153 to 169)

15. Lines 155 and 156 become one paragraph: Instructions and hooks add up. Skills, MCP servers,
    custom agents and settings have one winner for each name or setting.
16. Line 164: > | Settings | Later layers win: yours, the repository’s, settings.local.json, environment variables, then flags. Managed settings win over most of them. |

## Same thing elsewhere (lines 171 to 186)

17. Lines 173 and 174 become one line: Other coding tools keep the same kinds of setup in their own files.
18. Line 176: | Copilot CLI | Claude Code | Claude Desktop | Codex | VS Code and Visual Studio |
19. Line 178: | Instructions file | CLAUDE.md | Instructions | AGENTS.md | Same file |
20. Lines 184 to 186 become one paragraph: Each of these tools has its own guide: An Accidental
    Guide to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to:
    OpenAI Codex, and An Accidental Guide to: VS Code and Visual Studio.

## Check before you finish

- Every line not named above is unchanged, including every line that starts with `> `.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
