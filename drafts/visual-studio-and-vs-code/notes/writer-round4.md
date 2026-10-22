# Edits, round 4: VS Code and Visual Studio

Apply these edits in place to `packages/accidental-guides/guides/visual-studio-and-vs-code/guide.md`
(your working directory's `./guide.md`). Line numbers are from the file as it is now (commit
3948316, version 0.1.1, 175 lines). Replace each listed line with the new text, keeping the
table row structure: label cells stay as they are unless the edit gives a new label. Change
nothing else. Don't touch any other file. Lines that start with `> ` are a grey block: keep the
`> ` at the start of each of those lines, and start every new field marks line with `> ` too.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`
and `packages/editorial/skills/accidental-guide-write/references/voice.md` first.
Every rule there applies to any text you write or shorten. The text below is given exactly: use
it as written. You may change a word only to make a sentence read more naturally, never to add
words.

## Why

The printed guide is 1,285 words without the sources page and must come down to about 1,100,
five minutes. The series now has one owning guide for each concept: instructions files and
custom agents are explained in An Accidental Guide to: Agents, Harnesses, Skills, and Tools,
skills in An Accidental Guide to: Agent Skills, and MCP servers in An Accidental Guide to: Model
Context Protocol. Each of those entries here keeps a one-line definition, says only what is
particular to VS Code, and points to the owning guide. Settings has no owning guide, so its
entry defines it in one plain line. Every entry gets two short field marks on a grey block, as
in the sibling guides for Claude Code and GitHub Copilot CLI. Codex's guide is titled OpenAI
Codex.

## Page 2 (lines 13 to 23)

1. Line 13: You can set up five things for GitHub Copilot’s agent in VS Code: instructions files, custom agents, skills, MCP servers and settings. Each can belong to a repo, to you or to your organization.
2. Line 15: The default harness in VS Code is the Copilot harness. It reads .github/ in the repo and ~/.copilot/ in your home folder. For the basics, see An Accidental Guide to: Agents, Harnesses, Skills, and Tools.
3. Line 23: > | Setting | A switch or value that changes what VS Code does. |

## Instructions file (lines 29 to 35)

4. Line 30: | What | An instructions file is text Copilot adds to your requests. A .instructions.md file can apply only to files that match its applyTo pattern. See An Accidental Guide to: Agents, Harnesses, Skills, and Tools. |
5. Line 31: | So what | Put rules you’d otherwise repeat in every chat here. If a file seems ignored, check where it is and what its applyTo pattern matches. |
6. After line 32 (the blank line after the table), insert these lines, then one blank line:

> | Field | Short answer |
> |---|---|
> | Loads | With each request it applies to |
> | Cannot | Settle a conflict |

## Custom agent (lines 41 to 47)

7. Line 41: | Identify by | A .agent.md file in .github/agents/, or a name in the Agent dropdown. Older ones are .chatmode.md files. |
8. Line 42: | What | A custom agent is a saved role with its own instructions, tools and model. You pick one from the Agent dropdown, or another agent starts it as a sub-agent. See An Accidental Guide to: Agents, Harnesses, Skills, and Tools. |
9. Line 43: | So what | Limiting a custom agent’s tools limits what it can change. |
10. After line 44 (the blank line after the table), insert these lines, then one blank line:

> | Field | Short answer |
> |---|---|
> | Loads | When picked or started |
> | Cannot | Replace your instructions files |

11. Line 47: An instructions file applies to every request. A custom agent applies only while it’s selected or running.

## Skill (lines 53 to 59)

12. Line 54: | What | A skill is a written procedure in a folder. In VS Code it loads when your request matches or you type /skill-name. See An Accidental Guide to: Agent Skills. |
13. Line 55: | So what | A skill holds long steps without taking up room until it’s needed. When one doesn’t run, check its description first. |
14. After line 56 (the blank line after the table), insert these lines, then one blank line:

> | Field | Short answer |
> |---|---|
> | Loads | Name and description first |
> | Cannot | Add a tool |

15. Line 59: A prompt file, .github/prompts/*.prompt.md, is a saved prompt you run with /name. Prompt files work only in the Local harness, so VS Code suggests a skill instead.

## MCP server (lines 65 to 71)

16. Line 66: | What | An MCP server is a program that gives the agent more tools. In VS Code, search @mcp in the Extensions view to find one. See An Accidental Guide to: Model Context Protocol. |
17. Line 67: | So what | A local MCP server runs code on your machine with your permissions. Add only servers you trust. |
18. After line 68 (the blank line after the table), insert these lines, then one blank line:

> | Field | Short answer |
> |---|---|
> | Loads | When the harness connects |
> | Cannot | Act by itself |

19. Line 71: An extension adds features to VS Code itself. MCP servers show up in the same view, where you choose Install for yourself or Install in Workspace for the repo.

## Setting (lines 77 to 83)

20. After line 80 (the blank line after the table), insert these lines, then one blank line:

> | Field | Short answer |
> |---|---|
> | Loads | From each scope in turn |
> | Cannot | Tell the agent how to work |

21. Line 81: ## Confused with: Policy
22. Line 83: A policy is a setting an administrator makes for your organization. It wins over your own settings.

## How scopes combine (lines 115 to 123)

23. Line 115: Instructions add up, and settings override.
24. Line 119: | Instructions file | Every file that applies is added. None ranks above another. |
25. Line 121: | Skill | All are offered. |
26. Line 122: | MCP server | All are added, so give each server its own name. Your organization can limit which ones run. |
27. Line 123: | Setting | Default, then User, then Workspace, and the later one wins. An administrator’s policy wins over all three. |

## What’s different in Visual Studio (lines 134 to 138)

28. Line 134: | Instructions file | .github/copilot-instructions.md and .github/instructions/*.instructions.md. In Visual Studio 2026, personal instructions go in %USERPROFILE%/copilot-instructions.md. |
29. Line 138: | MCP server | %USERPROFILE%\.mcp.json, then .vs\mcp.json, .mcp.json, .vscode\mcp.json and .cursor\mcp.json in the solution folder. |

## Same thing elsewhere (lines 145 to 155)

30. Line 145: Other agent tools keep the same kinds of setup in their own places. Copilot CLI uses the same Copilot harness, so it reads the same .github/ and ~/.copilot/ folders.
31. Line 155: Each tool has its own guide: An Accidental Guide to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to: GitHub Copilot CLI and An Accidental Guide to: OpenAI Codex.

## Check before you finish

- Every line not named above is unchanged, including the version line.
- The five new field marks tables each start every line with `> `, and each has a blank line
  before and after it.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
