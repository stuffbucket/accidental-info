# Edits, round 3: guide.md (Model Context Protocol)

Apply these edits in place to `./guide.md`. Line numbers refer to the file as it is now; apply
from the bottom up. Replace each listed line's text with the new text, word for word, keeping
the table row structure. Change nothing else. Don't touch other files.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Why: the guide prints about 1,360 words and must come down toward 1,150 for a five-minute
read. Each edit removes a clause that repeats another row, without making the sentences
clipped.

## What is MCP?

- Line 22, Meaning cell: A program that offers tools and data to a harness through MCP.
- Line 24, Meaning cell: A setting that says how to start or reach a server.
- Line 25, Meaning cell: How the client and server pass messages, through stdio or HTTP.

## Server

- Line 35, Text cell: A name in the harness’s MCP settings, such as github.
- Line 36, Text cell: A server is a program that offers tools to a harness over MCP. Some servers also offer resources and prompts.
- Line 44: | Cannot | See the whole conversation | A server gets only the calls its client sends. |

## Client

- Line 54, Text cell: Nothing you set up. The harness makes one for each server.
- Line 55, Text cell: A client is the part of the harness that talks to one server. The client asks the server what it offers and passes it the agent’s calls.
- Line 56, Text cell: One client per server keeps the servers apart, so a server can’t see another server’s calls or results.
- Line 62: | Runs on | Inside the harness | The harness makes one when it starts or connects to a server. |
- Line 63: | Cannot | Choose a tool | The agent chooses each call, and the client carries it. |
- Line 67: The harness is the whole program you start. A client is one part of it, so three servers mean three clients.

## Server entry

- Line 73, Text cell: An entry under mcpServers in .mcp.json for Claude Code, mcp_servers in ~/.codex/config.toml for Codex, or servers in mcp.json for VS Code, as of October 2026.
- Line 74, Text cell: A server entry is a name plus a command that starts a local server or a URL for a remote one. Commands such as claude mcp add write it for you.
- Line 75, Text cell: When a server’s tools don’t show up, check the entry first. A wrong command, URL or key stops the harness from reaching the server.  (unchanged)
- Line 82: | Cannot | Add tools by itself | The tools come from the server. |
- Line 86: The entry is a few lines of settings. The server is the program they start or point to.

## Transport

- Line 92, Text cell: The type in the server entry. A command means stdio, and a URL means HTTP.
- Line 93, Text cell: A transport is how the client and server pass messages. With stdio, the harness starts the server on your machine and talks to it through its standard input and output. With HTTP, the server runs on its own at a URL.
- Line 94, Text cell: When a server won’t connect, the transport tells you where to look. Check the command for stdio, or the URL and sign-in for HTTP.
- Line 101: | Cannot | Change what the server offers | The messages are the same over stdio and HTTP. |
- Line 105: HTTP usually means a remote server, but a server on your own machine can also listen for HTTP on localhost.

## What can a server offer?

- Line 109: A server can offer three kinds of thing, and the difference is who picks each one.
- Line 117: Agents mostly use tools, the only kind they pick for themselves, and as of October 2026 some harnesses support only tools. Every tool definition also takes room in the context window on every call, unless the harness loads definitions on demand, as Claude Code does by default. Add only the servers you use.

## Common questions

- Line 123, Answer cell: No. MCP is a set of rules for the messages between a harness and a server.
- Line 124, Answer cell: No. Your harness picks the model. MCP only carries calls, results and data.
- Line 125, Answer cell: No. Built-in tools, scripts and CLIs work without it.
- Line 128: MCP is worth it when the same tools should work in several harnesses. Otherwise a script or CLI is often enough.

## Sources

- Delete the row for “Model Context Protocol, Client best practices”.

When you finish, print `wc -w guide.md` and nothing else.
