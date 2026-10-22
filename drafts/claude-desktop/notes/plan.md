# Plan: An Accidental Guide to… Claude Desktop

Slug: `claude-desktop`. One of five sibling guides written in parallel: Claude Code, Claude
Desktop, GitHub Copilot CLI, Codex, Visual Studio and VS Code. They share one shape: page 2
answers "What can you set up in …?", five or fewer key concepts with one page each, a "Where
things live" table page, an account-vs-organization page, and a short "Same thing elsewhere"
table.

Reader: someone who uses Claude Desktop (or claude.ai) and has lost track of where a skill, a
connector or a setting is kept. Not an expert. Wants to look things up quickly.

Budget: about 1,100 printed words including tables, sources and footers.

## Front matter

- title: Claude Desktop
- kicker: An Accidental Guide to…
- subtitle: A pocket-sized guide to where Claude Desktop keeps its settings, as of October 2026.
- running_footer: Claude Desktop
- version: 0.1.0
- Cover lines: "Claude", "Desktop".

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | cover | Title, five tiles | 30 |
| 2 | `why` | What can you set up in Claude Desktop? First paragraph stands alone as the site blurb. Says most things belong to your Claude account and follow you to claude.ai; a few belong to this computer. Points to the base guide for agent, skill, tool. Table of the five concepts. | 130 |
| 3 | entry 01 Instructions (In) | Instructions for Claude in Settings > General; project instructions. Confused with: Memory. | 80 |
| 4 | entry 02 Skills (Sk) | Customize > Skills; needs code execution; also load in Claude Code. Confused with: Instructions. | 80 |
| 5 | entry 03 Connectors (Cn) | Remote MCP servers in Customize > Connectors; tool permissions; local MCP servers via desktop extensions or the config file. Confused with: Desktop extension. | 85 |
| 6 | entry 04 Plugins (Pl) | Customize > Plugins; bundles of skills, connectors, sub-agents; saved to the account; paid plans. Confused with: Skills. | 80 |
| 7 | entry 05 Settings and permissions (Se) | Settings: General, Capabilities, Memory, Extensions, Developer; the permission setting in the message box; tool permissions; trusted folders. Confused with: Customize. | 85 |
| 8 | `where` | Where things live. Table: What, Lives in, Where to find it. Exact macOS and Windows paths for the config file and logs; Code tab reads ~/.claude. | 170 |
| 9 | `account` | Your account or your organization? Table: Setting, You, Owner. Plus IT's managed settings on the computer. | 170 |
| 10 | `elsewhere` | Same thing elsewhere. Table naming the equivalent in the four sibling guides, colon form in the note. | 100 |
| 11 | `sources` | Sources, date checked, colophon. | 110 |

Five concepts, tiles in series colours: 01 brand, 02 success, 03 figjam, 04 warning, 05 assistive.

## Field marks on each entry

Two rows: Works in (web, desktop, mobile, Code tab, Cowork) and Cannot.

## Builder changes

- `content.py`: table pages for `where`, `account`, `elsewhere`.
- `build_guide.py`: five keys, cover lines, `MONO_RE` for macOS and Windows paths, `>` menu
  paths kept in the body face, `&` escaped, entry title shrinks to fit beside the tile, back
  pages `where`, `account`, `elsewhere`.
- `build_docx.py`: same page list.
- No overview diagram: the three tables carry the locations.

## Facts

Only from `sources.md` in this folder, all checked 22 October 2026.
