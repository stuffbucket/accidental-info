# Edits, round 2: guide.md (Model Context Protocol)

Apply these edits in place to `packages/accidental-guides/guides/mcp/guide.md` (your working
directory's `./guide.md`). Line numbers refer to the file as it is now. Replace each listed
line's text with the new text, keeping the table row structure (label cells stay exactly as
they are unless the edit gives a new label). Change nothing else. Don't touch other files.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Why: round 1 was cut into short, clipped sentences ("The harness asks, so it holds the
clients." "One connection.") that read like a list. The author wants connected sentences that
build one idea at a time, not staccato. Each row is a little longer where it explains, and
whole rows of filler are gone. Where a replacement is given, use it word for word.

## Front matter

- Line 4: `subtitle: A pocket-sized guide to MCP servers and clients, as of October 2026.`
- Line 5: `running_footer: MCP`

## What is MCP? (lines 13 to 25)

- Line 13: An agent can only act through tools, and the harness runs every tool call. MCP, the Model Context Protocol, is a standard way for a harness to offer the agent extra tools and data, such as your files, a database or a web service.
- Line 15: Someone writes a small program called an MCP server, and you add an entry for it to your harness’s settings. The harness starts the server or connects to it, asks what tools it has, and passes the agent’s calls to it. An Accidental Guide to: Agents, Harnesses, Skills, and Tools covers tools and tool calls.
- Line 17: The names trip people up. “Server” makes you picture a service on another machine, but an MCP server is often a small program on your own machine that the harness starts. In MCP the side that asks is the client, and the harness does the asking, so the clients live in the harness.
- Line 22, Meaning cell: A program that offers tools, and sometimes data, to a harness through MCP.
- Line 23, Meaning cell: The part of the harness that talks to one server.
- Line 24, Meaning cell: A setting that tells the harness how to start or reach a server.
- Line 25, Meaning cell: How the client and server pass messages: stdio on your machine, or HTTP to a URL.

## How do the parts fit together? (line 29)

- Line 29: The server does the reaching, with its own code and credentials, and a local server can still call a web service. The GitHub MCP server, for example, can run on your machine and call GitHub’s web API, or run at GitHub’s own URL.

## Server (lines 35 to 48)

- Line 35, Text cell: A name in the harness’s MCP settings, such as github, with tools listed under it.
- Line 36, Text cell: A server is a program that offers tools to a harness over MCP. Some servers also offer resources and prompts. A server runs either on your machine or at a URL.
- Line 37, Text cell: The same server works in every harness that supports MCP, and the server holds the credentials for the system it reaches.
- Line 43: | Runs on | Your machine or a URL | The harness starts a local server. A remote server is always running. |
- Line 44: | Cannot | See the whole conversation | A server gets only the calls its client sends. The rest of the session stays in the harness. |
- Line 48: A web service answers requests from any program. A local MCP server often calls one, and a remote MCP server is one.

## Client (lines 54 to 67)

- Line 54, Text cell: Nothing you set up yourself. The harness makes one client for each server in its settings.
- Line 55, Text cell: A client is the part of the harness that talks to one server. The client asks the server what it offers and passes the agent’s calls to it.
- Line 56, Text cell: One client per server keeps the servers apart. A server can’t see the calls or results of another server.
- Line 62: | Runs on | Inside the harness | The harness makes the client when it starts or connects to the server. |
- Line 63: | Cannot | Choose a tool | The agent chooses each call, and the client carries the call to the server. |
- Line 67: The harness is the whole program you start. A client is one part of it, so a harness with three servers has three clients.

## Server entry (lines 73 to 86)

- Line 73, Text cell: mcpServers in .mcp.json for Claude Code, an mcp_servers table in ~/.codex/config.toml for Codex, or servers in mcp.json for VS Code, as of October 2026.
- Line 74, Text cell: A server entry is a name plus either a command that starts a local server or a URL for a remote one. Commands such as claude mcp add write the entry for you.
- Line 75, Text cell: When a server’s tools don’t show up, check the entry first. A wrong command, URL or key stops the harness from reaching the server.
- Line 81: | Kept in | A project file or your user settings | Commit a project file and the whole team gets the same servers. |
- Line 82: | Cannot | Add tools by itself | The tools come from the server the entry points to. |
- Line 86: The entry is a few lines of settings. The server is the program those lines start or point to.

## Transport (lines 92 to 105)

- Line 92, Text cell: The type in the server entry. An entry with a command uses stdio, and an entry with a URL uses HTTP.
- Line 93, Text cell: A transport is how the client and server pass messages. With stdio, the harness starts the server on your machine and talks to it through its standard input and output. With HTTP, the server runs on its own at a URL and can serve many clients.
- Line 94, Text cell: The transport tells you where to look when a server won’t connect. For stdio, check the command. For HTTP, check the URL and the sign-in.
- Line 100: | Runs on | Your machine or the network | A stdio server always runs on your machine. An HTTP server can run anywhere. |
- Line 101: | Cannot | Change what the server offers | The messages are the same over stdio and HTTP. Only the way they travel differs. |
- Line 105: HTTP usually means a remote server, but not always. A server on your own machine can also listen for HTTP on localhost.

## What can a server offer? (lines 109 to 117)

- Line 109: A server can offer three kinds of thing. What differs is who decides to use each one.
- Line 113: | Tools | The agent | Tool calls in the session, the same as built-in tools. |
- Line 114: | Resources | You or the harness | Data you attach, with an @ mention in Claude Code or Add Context in VS Code. |
- Line 115: | Prompts | You | Ready-made instructions you run as slash commands. |
- Line 117: Agents mostly use tools, the only kind they pick for themselves, and as of October 2026 some harnesses support only tools. Each tool also costs room: its definition goes into the context window on every call, unless the harness loads definitions on demand, as Claude Code does by default. Add the servers you use and turn off the tools you don’t.

## Common questions (lines 123 to 128)

- Line 123, Answer cell: No. MCP is a set of rules for the messages between a harness and a server. Many servers are small programs on your own machine.
- Line 124, Answer cell: No. The model is whichever one your harness uses. MCP carries tool calls, results and data.
- Line 125, Answer cell: No. Built-in tools, and scripts and CLIs run through the shell tool, work without MCP.
- Line 126, Answer cell: Not always. A local server is often a go-between for the files, database or web service you care about.
- Line 128: MCP is worth it when the same tools should work in several harnesses. Otherwise a script or CLI in the repo is often enough.

## Sources

- Delete line 138 (Model Context Protocol, Understanding MCP servers).
- Line 137: | Model Context Protocol, Specification 2026-07-28 | October 2026 | modelcontextprotocol.io/specification/2026-07-28 | (unchanged)

When you finish, print `wc -w guide.md` and nothing else.
