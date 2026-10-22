# Writing instructions, round 1: An Accidental Guide to… Model Context Protocol

You are writing one file: `packages/accidental-guides/guides/mcp/guide.md` (relative to the
repository root; from your working directory it is `./guide.md`). Create it. Don't touch any
other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

## Read first, in this order

1. `packages/editorial/skills/accidental-guide-plan/references/series-rules.md`: the author's rules and feedback. Binding.
2. `packages/editorial/skills/accidental-guide-write/references/voice.md`: his voice. Binding.
3. `packages/accidental-guides/guides/agents-harnesses-skills-tools/guide.md`: the base guide.
   It is fixed and well reviewed. Never contradict it and don't repeat it. Point to it for the
   basics (agent, harness, tool, tool call, context window).
4. `packages/accidental-guides/guides/lights-off-software-factories/guide.md`: the shape and
   length to copy. Same section ids for why, fit, entries and sources.
5. `drafts/mcp/notes/plan.md`: the page plan.
6. `drafts/mcp/notes/sources.md`: every fact you may use. Use no fact that isn't
   there. Where products differ or change often, say "as of October 2026".

## Who it's for, and what the author said

A programmer, or someone who works with them, who keeps seeing “MCP server” and can't say what
it is. The author: there's a lot of confusion about what an MCP is even for someone who is a
programmer; the naming looks backwards and makes people assume the thing it connects to has to
be a service somewhere.

So the guide answers, plainly and in this order: what MCP is for (a standard way for a harness
to offer an agent extra tools and data); why the names seem backwards (the “server” is often a
small program on your own machine that the harness starts, and the harness is the side with
the clients); local servers over stdio versus remote servers over HTTP; what a server can offer
(tools, resources, prompts) and that agents mostly use tools; how a harness is told about a
server (an entry in its settings); what every tool definition costs in the context window; and
what MCP is not (not a service, not an AI model, not required for an agent to use tools).

## Length

Five minutes front to back: about 1,000 words in guide.md, tables included, sources included.
Cut detail, not clarity. Short is good; staccato isn't.

## Writing rules (summary; the files above are binding)

- Regular English, one idea at a time, as if to a smart colleague who is new to this. Say
  “you” where that's natural. Each sentence follows from the last.
- No paragraph by list. No “A person can”, “One may”. No self-narration (“this guide”, “this
  page”, “below”). No hooks, teasers, trivia, sarcasm, slogans, rhetorical questions, “not X
  but Y”, em dashes, rhythm triplets, borrowed framing. No quotes, no people's names.
- Ask questions plainly in titles (“What is MCP?”). No embedded-question noun phrases (“what
  MCP is”, “how a server works”).
- Name the real thing (“a small program on your machine”, “a URL”), never stand-ins
  (“behind”, “around”, “on top of”).
- In body prose cite the base guide with the colon form: An Accidental Guide to: Agents,
  Harnesses, Skills, and Tools.
- Rows must read on their own: no row or cell sentence starts with “It”, “Its”, “They” or
  “This”.
- Say “harness”, never “host”, except once on the terms page to say the specification calls
  the harness the host. Say “agent” for the model running in the harness's loop. Say “tool
  definition” for a tool's name, description and arguments.

## Format rules the parser needs

- Typographic quotes and apostrophes (’ “ ”). No Markdown emphasis, no backticks, no lists, no
  “&”, no “<” except `<br/>` in a `#` title. No “e.g. ” or “i.e.”.
- No slashes in ordinary words (“and/or”, “stdin/stdout”): write “standard input and output”.
  File names such as .mcp.json, config.toml, ~/.codex/config.toml and mcp.json are fine and
  print in mono.
- A “Short answer” cell must not end with a full stop. The builder adds one.
- The first sentence of a What or So what row is printed bold, up to the first “. ”. Make that
  first sentence the short answer.
- A cell can't contain “|”.

## The exact skeleton

Keep every heading, id, table header and row label exactly as here. Fill in the text marked
with angle-bracket descriptions (and delete the descriptions). Section and table shapes are
read by position, so don't add or drop paragraphs or rows except where it says you may.

```
---
title: Model Context Protocol
kicker: An Accidental Guide to…
subtitle: <one sentence, starts “A pocket-sized guide to”, ends “as of October 2026.”, about 16 words>
running_footer: Model Context Protocol
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: October 2026
version: 0.1.0
---

# What is MCP? {#why}

<P1, the blurb; must stand alone on the website: MCP, the Model Context Protocol, is a
standard way for a harness to offer an agent extra tools and data. About 45 words. Start from
what the reader knows: an agent acts only through tools, and the harness runs every tool call.>

<P2: how it works in one pass: someone writes a small program called an MCP server; you add
an entry for it to the harness's settings; the harness starts it or connects to it, asks for
its list of tools, and passes the agent's calls to it. Any harness that supports MCP can use
the same server. Point to the base guide for tools and tool calls. About 60 words.>

<P3: why the names seem backwards. “Server” makes you picture a service on another machine.
Often the server is a small program on your own machine that the harness starts and talks to
through standard input and output. The harness is the side that asks, so the harness holds the
clients. A server serves tools to the harness. About 60 words.>

| Term | Meaning |
|---|---|
| Host | <the specification's word for the harness> |
| Server | <one line> |
| Client | <one line> |
| Server entry | <one line> |
| Transport | <one line: stdio or HTTP> |

# How do the parts fit together? {#fit}

<One or two paragraphs, about 70 words in all, under a diagram drawn in code. The diagram
shows: a server entry that tells the harness each server's command or URL; inside the
harness, one client per server; two servers on your machine reached through stdio, one
reaching files in a folder and one a database; a remote server at a URL reached through HTTP,
reaching a web service. Don't describe the drawing. Say what to take from it: one client per
server; the server, wherever it runs, does the reaching with its own code and credentials; a
local server can still call a web service, as the GitHub MCP server can.>

# Server {#entry num=01 mono=Sv}

| Field | Text |
|---|---|
| Identify by | <what you see: a name in the harness's MCP settings, such as github or filesystem, and tool names from it> |
| What | <short answer first sentence. A program that offers tools, and sometimes resources and prompts, over MCP. Local or remote.> |
| So what | <short answer first sentence. Why it matters: one server works in every harness that supports MCP, and the server holds the credentials, so access control for that system belongs in the server.> Keep to the base guide, don't repeat its wording. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Runs on | <short> | <detail> |
| Cannot | <short> | <detail> |

## Confused with: Web service

<One paragraph, two or three sentences.>

# Client {#entry num=02 mono=Cl}

| Field | Text |
|---|---|
| Identify by | <you rarely see one: the harness makes one for each server; in Claude Code, the server's status in /mcp> |
| What | <...> |
| So what | <...> |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Runs on | <short> | <detail> |
| Cannot | <short> | <detail> |

## Confused with: Harness

<One paragraph: the harness is the whole program; a client is the part of it that talks to one
server, so a harness with three servers has three clients.>

# Server entry {#entry num=03 mono=Se}

| Field | Text |
|---|---|
| Identify by | <the file and its shape: .mcp.json with mcpServers in Claude Code, ~/.codex/config.toml with an mcp_servers table in Codex, mcp.json with servers in VS Code. As of October 2026.> |
| What | <a name plus either a command that starts a local server or a URL for a remote one, with any environment variables or headers it needs; commands such as claude mcp add write it for you> |
| So what | <...> |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Kept in | <short> | <detail: project file you can commit and share, or your user settings> |
| Cannot | <short> | <detail> |

## Confused with: <pick the most useful: Server, or Connector, or Instructions file>

<One paragraph.>

# Transport {#entry num=04 mono=Tr}

| Field | Text |
|---|---|
| Identify by | <the type in the server entry, stdio or http; a command means stdio, a URL means HTTP> |
| What | <the way the client and the server pass messages. stdio: the harness starts the server and they talk through its standard input and output; the server stops with the session. HTTP: the server runs on its own at a URL and can serve many clients.> |
| So what | <...> |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Runs on | <short> | <detail> |
| Cannot | <short> | <detail> |

## Confused with: Remote server

<One paragraph: HTTP usually means remote, but a server can run on your own machine and listen
on localhost.>

# What can a server offer? {#offer}

<One paragraph, about 35 words: three kinds; who picks each one is the difference.>

| Offer | Who picks it | Where you see it |
|---|---|---|
| Tools | <short> | <detail> |
| Resources | <short> | <detail: @ mention in Claude Code, Add Context in VS Code> |
| Prompts | <short> | <detail: slash commands> |

<Closing paragraph, about 80 words: agents mostly use tools, the only kind the model picks
for itself; some harnesses support only tools, as of October 2026. Then the cost: every tool
definition from every server takes room in the context window, on every call, unless the
harness loads definitions on demand. A server with many tools you never use still costs room.
Claude Code loads MCP tool definitions on demand by default. Advice: add the servers you use
and turn off tools you don't need.>

# Common questions {#questions}

| Question | Answer |
|---|---|
| Is MCP a service? | <...> |
| Is MCP an AI model? | <...> |
| Does an agent need MCP to use tools? | <...> |
| Is the server the system I’m connecting to? | <...> |

<One closing paragraph, one or two sentences: when MCP is worth it versus a script or CLI in
the repo. Don't repeat the base guide's wording.>

# Sources {#sources}

These public sources were checked in October 2026.

| Source | Date | Address |
|---|---|---|
| Model Context Protocol, Architecture overview | October 2026 | modelcontextprotocol.io/docs/learn/architecture |
| Model Context Protocol, Specification 2026-07-28 | October 2026 | modelcontextprotocol.io/specification/2026-07-28 |
| Model Context Protocol, Understanding MCP servers | October 2026 | modelcontextprotocol.io/docs/learn/server-concepts |
| Model Context Protocol, Client best practices | October 2026 | modelcontextprotocol.io/docs/develop/clients/client-best-practices |
| Anthropic, Claude Code: MCP | October 2026 | code.claude.com/docs/en/mcp |
| OpenAI, Codex: MCP | October 2026 | learn.chatgpt.com/docs/extend/mcp |
| Microsoft, VS Code: Use MCP servers | October 2026 | code.visualstudio.com/docs/copilot/chat/mcp-servers |
| GitHub Docs, Configure MCP servers for Copilot | October 2026 | docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers |
```

The Sources section is final: copy it exactly.

When you finish, print the word count of guide.md (`wc -w guide.md`) and nothing else.
