# Plan: Plugins, Connectors, and Marketplaces

Slug `plugins-and-marketplaces`. Kicker "An Accidental Guide to…". Version 0.1.0.
Facts: `sources.md` in this folder, fetched 22 October 2026.

## What the reader needs

Someone who uses a coding agent or a Claude or ChatGPT app keeps meeting words like plugin,
marketplace, connector and extension, and can't tell which are the same thing and which are
different. The guide sorts every name into five kinds of thing, shows them on one map, and
then gives each kind a page. It points to An Accidental Guide to: Agents, Harnesses, Skills,
and Tools for agent, harness, skill, tool and MCP server, and doesn't define those again.

## The five kinds (one line each on the map, one entry each)

| No. | Key | Entry name | Line on the map | Names on the line |
|---|---|---|---|---|
| 01 | Tl | Tools | Tools: reach other systems | MCP server (connector, app), desktop extension (local connector), extension |
| 02 | In | Instructions | Instructions: how to work | instructions file (project instructions), skill, slash command (command), prompt file (custom prompt), agent definition (custom agent, subagent) |
| 03 | Hk | Hooks | Hooks: run at set moments | hook |
| 04 | Pk | Packages | Packages: install in one step | plugin (agent plugin), extension |
| 05 | Mk | Marketplaces | Marketplaces: lists to install from | marketplace (Visual Studio Marketplace, Claude Marketplace), directory (Connectors Directory), MCP registry |

Interchanges: Extension is on two lines (a tool module or packaged MCP server, and an editor
add-on). Every station with other names under it is one thing with several names.

## Pages (10)

1. Cover: title on three lines, subtitle, five tiles.
2. `{#why}` What are all these things? Two or three short paragraphs, no table. The first
   paragraph stands alone as the site blurb.
3. `{#map}` The map. One-sentence intro, the subway map (data in guide.md), key, one note.
4–8. `{#entry}` × 5: Identify by, What, So what; a table of the names on that line (Name,
   Where, What it is); Confused with.
9. `{#who}` Which product uses which word: rows are the five kinds, columns are the six
   products (Claude Code, Claude apps, Copilot CLI, VS Code, Visual Studio, Codex). The note
   points to the per-product guides and the Skills and MCP guides.
10. `{#sources}` Sources and colophon.

## Budget

About 1,100 printed words in all. Entries about 100 words each. The map's labels count.

## Builder

`build_guide.py` adds `page_map()`, a transit-map diagram drawn from the `{#map}` block:
`line`, `station`, `also`. `build_docx.py` places it as an image cropped with `map_box()`,
from `map_layout()`. Entries print a names table where earlier guides print field marks.
The product table is a `TABLE_PAGES` page with smaller cells.

## Cross-references (colon form, body only)

- An Accidental Guide to: Agents, Harnesses, Skills, and Tools (basics)
- An Accidental Guide to: Skills
- An Accidental Guide to: MCP
- An Accidental Guide to: Claude Code, Claude Desktop, GitHub Copilot CLI, Codex, Visual
  Studio, VS Code
