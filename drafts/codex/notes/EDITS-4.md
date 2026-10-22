# Edits, round 4: OpenAI Codex

Apply these edits in place to `packages/accidental-guides/guides/codex/guide.md` (your working
directory's `./guide.md`). Line numbers are from the file as it is now (commit after 588d180,
version 0.1.0). Replace each listed line with the new text, keeping the table row structure and
any `> ` at the start of a line: label cells stay as they are unless the edit gives a new label.
Change nothing else. Don't touch any other file, and don't change the `version:` line.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`
and `packages/editorial/skills/accidental-guide-write/references/voice.md` first.
Every rule there applies to any text you write or shorten.

## Why

The body is about 1,230 printed words and must come down to about 1,100, a five-minute read.
Each entry now has to fit half a page, so the field marks keep only their short answer. Four of
the five parts are explained in their own guides, so those entries now say what is specific to
Codex and name the guide that explains the part, in the colon form. The config file is Codex’s
settings, which have no guide of their own, so its entry defines settings in one plain line.
The "Same thing elsewhere" table now names each tool’s own file, as the GitHub Copilot CLI
guide does. Some lines also break the lint: semicolons, "Just you" ("just" is filler), "key",
"travel" and "above".

## Instructions file (lines 25 to 42)

1. Line 30: | What | Codex reads your AGENTS.md first, then each one from the project’s root down to where you work, and adds them all to the session. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains instructions files. |
2. Lines 35 to 38, the field marks, become exactly these four lines (the Detail column goes):

   > | Field | Short answer |
   > |---|---|
   > | Loads | At the start of a session |
   > | Add with | /init |

## Skill (lines 44 to 61)

3. Line 49: | What | Codex reads each skill’s name and description at the start, and the rest when your task matches the description or you type $ and the skill’s name. An Accidental Guide to: Agent Skills explains skills. |
4. Lines 54 to 57 become:

   > | Field | Short answer |
   > |---|---|
   > | Loads | Description first, steps when used |
   > | Check with | /skills |

5. Line 61: A plugin packages skills, MCP servers and hooks to install together, using /plugins in the CLI.

## MCP server (lines 63 to 80)

6. Line 68: | What | Each server’s entry gives a command that starts it on your computer, or the url of a remote one. An Accidental Guide to: Model Context Protocol explains MCP servers. |
7. Line 69: | So what | Set a server up once and it works in the CLI, the IDE extension and the desktop app. |
8. Lines 73 to 76 become:

   > | Field | Short answer |
   > |---|---|
   > | Add with | codex mcp add |
   > | Check with | /mcp |

## Config file (lines 82 to 99)

9. Line 87: | What | Settings are the choices that control how Codex runs, such as the model. Codex keeps them in config.toml, along with MCP servers and permissions. |
10. Line 88: | So what | Your own config.toml applies everywhere, and a project’s .codex/config.toml changes settings for that project. A profile, such as ~/.codex/deep-review.config.toml, holds a set of changes you pick with --profile. |
11. Lines 92 to 95 become:

    > | Field | Short answer |
    > |---|---|
    > | Loads | When Codex starts |
    > | Override with | -c for one run |

## Permissions (lines 101 to 118)

12. Line 106: | What | Codex has two permission settings. The sandbox decides what commands can touch: read-only, workspace-write or danger-full-access. The approval policy, on-request or never, decides when Codex stops to ask. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains permissions. |
13. Lines 111 to 114 become:

    > | Field | Short answer |
    > |---|---|
    > | Network | Off by default |
    > | Change with | /permissions |

14. Line 118: Rules files in ~/.codex/rules/ say whether a command may run outside the sandbox: allow, prompt or forbidden.

## Where things live (lines 120 to 142)

15. Line 122: Your own files apply in every project. A project’s files are kept in its repository.
16. Lines 126 to 129: change the first cell, "Just you", to "Your home folder". Nothing else
    changes on lines 126, 127 and 129.
17. Line 128, all of it: | Your home folder | Config file | ~/.codex/config.toml, which also holds MCP servers and permissions, with profiles beside it |
18. Delete line 130 (the Plugins row) and line 138 (the Codex Cloud Environment row).
19. Line 139: | Codex Cloud | Skills | Only the repository’s skills. Personal skills aren’t synced. |

## How do the places combine? (lines 144 to 167)

20. Line 159: > | Instructions | Codex joins them, yours first, then the project’s from the root down, so the closest file has the last word. |
21. Line 161: > | MCP servers | Servers can be in your config.toml or a project’s, and a setting for the same server follows the numbered list. |
22. Delete line 164 (the Requirements row). The config file entry already covers requirements.

## Same thing elsewhere (lines 169 to 181)

23. Line 171: Other coding tools keep the same kinds of setup in their own files.
24. Lines 175 to 179 become exactly these five rows:

    | Instructions file | CLAUDE.md | Instructions | AGENTS.md | AGENTS.md |
    | Skill | Skills | Skills | Skills | Skills |
    | MCP server | .mcp.json | Connectors | mcp-config.json | .mcp.json |
    | Config file | settings.json | Settings | settings.json | Settings |
    | Permissions | settings.json | Settings | permissions-config.json | Settings |

25. Line 181: Each of these tools has its own guide: An Accidental Guide to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to: GitHub Copilot CLI, and An Accidental Guide to: VS Code and Visual Studio.

## Check before you finish

- Every line not named above is unchanged, including every line that starts with `> `.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
