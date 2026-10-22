# Plan: An Accidental Guide to… OpenAI Codex

Slug: `codex`. One of five sibling guides (Claude Code, Claude Desktop, GitHub Copilot CLI,
Codex, Visual Studio and VS Code) with the same shape. The reader uses Codex, or is about to,
and keeps losing track of where an instruction, a skill, an MCP server or a setting is kept,
and which copy wins. The guide answers: what can you set up, where does each thing live, and
how do the places combine. Calm, and easy to look things up in.

Codex here means the Codex CLI, the Codex IDE extension and Codex in the ChatGPT desktop app,
which share one set of config files, plus Codex Cloud, where settings live in a web page.
As of October 2026 the Codex docs moved from developers.openai.com/codex to
learn.chatgpt.com/docs.

Basics (agent, harness, skill, tool, session, context window) are in An Accidental Guide to:
Agents, Harnesses, Skills, and Tools. Point to it; don't repeat it.

Budget: about 1,100 printed words, 11 pages.

## Pages

| Page | Section | What it says |
|---|---|---|
| 1 | cover | Kicker, title "OpenAI Codex", subtitle, five tiles |
| 2 | `why` "What can you set up in Codex?" | Codex reads its setup from plain files in two main places, your Codex home folder and the project, and the CLI, IDE extension and desktop app share them. Five kinds of setup, one row each. The first paragraph is the site blurb. Points to the base guide. |
| 3 | entry 01 Instructions file (`In`) | AGENTS.md: ~/.codex/AGENTS.md, then root down to the current folder. Confused with: Skill |
| 4 | entry 02 Skill (`Sk`) | .agents/skills folders, ~/.agents/skills; $ or /skills. Confused with: Plugin |
| 5 | entry 03 MCP server (`Mc`) | [mcp_servers.name] in config.toml; codex mcp add; /mcp. Confused with: Tool |
| 6 | entry 04 Config file (`Cf`) | ~/.codex/config.toml, .codex/config.toml, profile files, -c. Confused with: Requirements file |
| 7 | entry 05 Permissions (`Pe`) | sandbox_mode and approval_policy; /permissions; defaults. Confused with: Rules |
| 8 | `where` "Where things live" | Grouped rows: Just you, This project, Your organization, Codex Cloud. Exact paths. |
| 9 | `combine` "How do the places combine?" | Per thing: what happens when two places set it. Trust gates the project's .codex folder. |
| 10 | `elsewhere` "Same thing elsewhere" | Five rows, four sibling columns; colon-form pointers. |
| 11 | `sources` | OpenAI's Codex documentation, checked 22 October 2026 |

Field marks in each entry: two rows, such as "Loads" (when Codex reads it) and "Add with" or
"Check with" (the command).

## Rules for the writer

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert. Plain English, one idea at a time, no paragraph by list, no
self-narration, no quotes or names of people, colon form for other guides. Exact paths only
from `sources.md`. Say "as of October 2026" where things change often.
