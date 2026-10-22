# Plan: An Accidental Guide to… Claude Code

Slug `claude-code`. Version 0.1.0. One of five sibling guides on where things live and how
they're configured (Claude Code, Claude Desktop, GitHub Copilot CLI, Codex, Visual Studio and
VS Code). Same shape in all five. About 1,100 printed words.

Reader: someone who uses Claude Code, or is about to, and keeps losing track of which file does
what and which one wins. Not an expert. Points to An Accidental Guide to: Agents, Harnesses,
Skills, and Tools for agent, harness, skill, tool, session, context window.

## Pages

| Page | Section | What it does |
|---|---|---|
| 1 | cover | Kicker, title "Claude Code", subtitle, five tiles |
| 2 | `why` | "What can you set up in Claude Code?" Two short paragraphs, then a table of the five things in one line each |
| 3–7 | `entry` × 5 | Instructions file, Skill, MCP server, Plugin, Settings. Identify by, What, So what, two field marks (Loads, Cannot), Confused with |
| 8 | `where` | "Where do the files live?" Three groups (you in every project, the project, your organization), two columns: thing, exact path |
| 9 | `scopes` | "Which one wins?" Thing, what happens when it's set in more than one place |
| 10 | `elsewhere` | "The same things in other tools" One row per sibling guide, colon form |
| 11 | `sources` | Official pages, date checked |

## Key concepts and tiles

| # | Name | Key | Colour (series rule) |
|---|---|---|---|
| 01 | Instructions file | In | brand |
| 02 | Skill | Sk | success |
| 03 | MCP server | Mc | figjam |
| 04 | Plugin | Pl | warning |
| 05 | Settings | Se | assistive |

Sk and Mc match the keys in the base guide. Hooks and permissions sit inside Settings.
Sub-agents (`.claude/agents/`) are mentioned once, under Plugin, and not given a page.

## Builder changes (done by hand)

- Copied from `lights-off-software-factories/`.
- Five parts in `PART_TOKEN` and `NAME2MONO`; cover title one line.
- `MONO_RE` also sets `.json` and `.toml` file names, `~/` paths, leading-slash paths, and the
  two system folders whose names contain a space.
- Table pages extended to `scopes` and `elsewhere`. New `where` page: a grey group label per
  scope over a two-column table, in both builders.
- `MONO_RE` also sets command-line flags such as `--settings`.
- Sources: a row with an empty date prints only the address (the intro gives the date
  checked), and an address too long for one line breaks after the last slash that fits.

## Rounds

1. First draft from the skeleton and `sources.md`.
2. Concrete wording, scope names from the docs (user, project, local, managed), other tools
   filled in from their official docs.
3. Cut from about 1,700 to about 1,400 printed words; where page fits.
