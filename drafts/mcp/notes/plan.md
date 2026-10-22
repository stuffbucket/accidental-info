# Plan: An Accidental Guide to… Model Context Protocol

Slug `mcp`. Builder copied from `lights-off-software-factories/`. Target about 1,100 printed
words, 10 pages. Facts only from `sources.md`.

## The reader

A programmer, or someone who works with programmers, who has read or skimmed An Accidental
Guide to: Agents, Harnesses, Skills, and Tools. They know an agent acts through tool calls
that the harness runs. They have seen "MCP server" in settings and docs and can't say what it
is for, and the word "server" makes them picture a service somewhere on the network.

## The questions, in order

1. What is MCP for? A standard way for a harness to offer an agent extra tools and data.
2. Why do the names seem backwards? The server is often a small program on your own machine
   that the harness starts. The harness holds the clients.
3. How do the parts fit? Diagram.
4. One page per part: server, client, server entry, transport.
5. What can a server offer, and which of those do agents use? Tools, resources, prompts. Tools
   by far. What every tool definition costs in the context window.
6. Common questions: not a service, not a model, not required for tools, not always the thing
   you're connecting to.

## Key concepts (four, each with a page and a tile)

| No. | Part | Key | Colour (series rule) |
|---|---|---|---|
| 01 | Server | Sv | brand (blue) |
| 02 | Client | Cl | success (green) |
| 03 | Server entry | Se | figjam (purple) |
| 04 | Transport | Tr | warning (yellow) |

Order puts server entry before transport so no key repeats another guide's key in the same
colour (`Tr` is purple in the specs guide; `Se` is pink in the harness guide; `Cl` is yellow
in lights-off).

Harness, host, tool, resource and prompt are not parts here and get no tile. Harness and tool
come from the base guide.

## Pages

| Page | Section | Content |
|---|---|---|
| 1 | cover | Kicker, "Model / Context / Protocol", subtitle, four tiles |
| 2 | `{#why}` What is MCP? | Three short paragraphs: what it's for (the blurb), how it works in one pass, why the names seem backwards. Terms table: Host, Server, Client, Server entry, Transport. Points to the base guide |
| 3 | `{#fit}` How do the parts fit together? | Diagram drawn in code: a server entry feeds the harness; inside the harness frame, one client per server; arrows labelled stdio, stdio, HTTP to three servers; each server reaches files in a folder, a database, a web service. A dashed line marks your machine from the network. One or two short paragraphs under it |
| 4 | Server | entry |
| 5 | Client | entry |
| 6 | Server entry | entry, with a JSON or TOML example in words, no code block |
| 7 | Transport | entry |
| 8 | `{#offer}` What can a server offer? | Intro; table Offer / Who picks it / Where you see it, rows Tools, Resources, Prompts; closing note on the context-window cost of tool definitions and on-demand loading |
| 9 | `{#questions}` Common questions | Question / Answer table: Is MCP a service? Is MCP an AI model? Does an agent need MCP to use tools? Is the server the system I'm connecting to? Closing note |
| 10 | `{#sources}` Sources | Source / Date / Address, eight rows, checked October 2026 |

Each entry: Identify by, What, So what; two field marks; Confused with. Field mark labels:
Server and Client and Transport use "Runs on" and "Cannot"; Server entry uses "Kept in" and
"Cannot".

## Word budget

| Page | Words |
|---|---|
| Cover | 40 |
| What is MCP? | 220 |
| How the parts fit | 110 (diagram labels plus 70 of text) |
| Four entries | 4 x 120 = 480 |
| What can a server offer? | 150 |
| Common questions | 110 |
| Sources | 90 |
| Total | about 1,200 before cuts; cut to about 1,100 |

## Builder changes

- `content.py`: front matter, `{#why}`, `{#fit}`, entries, table pages `offer` and
  `questions`, sources. Voice comment rewritten for this guide.
- `build_guide.py`: `PART_TOKEN`, `NAME2MONO`, `COVER_LINES`, `MONO_RE` (add .json, .toml),
  new `page_fit()` diagram and its labels, `TABLE_WIDTHS` for `offer` and `questions`, page
  order.
- `build_docx.py`: page order for the new table pages, default output name, `fit_box()` from
  the new `fit_layout()`.
