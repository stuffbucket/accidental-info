# Plan: An Accidental Guide to… GitHub Copilot CLI

Slug: `copilot-cli`. One of five sibling guides (Claude Code, Claude Desktop, GitHub Copilot
CLI, Codex, Visual Studio and VS Code) with the same shape. The reader uses Copilot CLI, or
is about to, and keeps losing track of where an instruction, a skill, an MCP server or a
setting is kept, and which copy wins. The guide answers: what can you set up, where does
each thing live, and how do the places combine. Calm, and easy to look things up in.

Basics (agent, harness, skill, tool, session, context window) are in An Accidental Guide
to: Agents, Harnesses, Skills, and Tools. Point to it; don't repeat it.

Budget: about 1,100 printed words, 11 pages.

## Pages

| Page | Section | What it says |
|---|---|---|
| 1 | cover | Kicker, title "GitHub Copilot CLI", subtitle, five tiles |
| 2 | `why` "What can you set up in Copilot CLI?" | Copilot CLI reads its setup from files in three places: your home folder, the repository and your organization. Five kinds of setup, one row each. The first paragraph doubles as the site blurb. Points to the base guide for the basics. |
| 3 | entry 01 Instructions file (`In`) | copilot-instructions.md, path-specific .instructions.md, AGENTS.md. Loaded every session. Confused with: Skill |
| 4 | entry 02 Skill (`Sk`) | SKILL.md folders; description always loaded, the rest when used. Confused with: Instructions file |
| 5 | entry 03 MCP server (`Mc`) | mcp-config.json, .mcp.json; GitHub's MCP server built in. Confused with: Tool (base guide) or Plugin |
| 6 | entry 04 Custom agent (`Ag`) | .agent.md files; what the base guide calls an agent definition. Confused with: Plugin, which bundles agents, skills, MCP servers and hooks |
| 7 | entry 05 Settings (`Se`) | settings files, trusted folders, tool approval. Confused with: Policy (set by the organization) |
| 8 | `where` "Where things live" | Grouped rows: Just you, This repository, Your organization. Exact paths. |
| 9 | `combine` "How do the places combine?" | Per thing: what happens when two places set it. Trust gates repository setup. |
| 10 | `elsewhere` "Same thing elsewhere" | Five rows, four sibling columns; colon-form pointers. |
| 11 | `sources` | GitHub Docs pages and the CLI's help, checked 22 October 2026 |

Field marks in each entry: "Loads" (when it reaches the model) and "Check with" (the
command that lists what's loaded). A "Cannot" row was tried in round 2 and cut in round 3 for
length.

## Rounds

1. First draft from writer-round1.md: right structure, but clipped and staccato.
2. writer-round2.md: fuller, connected entries; corrected MCP and custom agent order. Too long
   (about 1,880 printed words).
3. writer-round3.md: cut to about 1,320 printed words, then a few trims by hand. Builder: mono
   for bare ~/ paths, .github and .toml.

## Rules for the writer

No mannered prose: the writing must not call attention to itself. Make no assumption that
the reader is an expert. Plain English, one idea at a time, no paragraph by list, no
self-narration, no quotes or names of people, colon form for other guides. Exact paths
only from `sources.md`. Say "as of October 2026" where things change often.
