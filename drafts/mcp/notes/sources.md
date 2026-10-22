# Sources for An Accidental Guide to… MCP

All fetched on 22 October 2026. Current MCP specification revision: 2026-07-28.
Excerpts are verbatim.

## Model Context Protocol, Architecture overview

https://modelcontextprotocol.io/docs/learn/architecture (redirects to the 2026-07-28 docs)

- "MCP focuses solely on the protocol for context exchange—it does not dictate how AI
  applications use LLMs or manage the provided context."
- "an MCP host — an AI application like Claude Code or Claude Desktop — establishes
  connections to one or more MCP servers. The MCP host accomplishes this by creating one MCP
  client for each MCP server. Each MCP client maintains a dedicated connection with its
  corresponding MCP server."
- "MCP Host: The AI application that coordinates and manages one or multiple MCP clients"
- "MCP Client: A component that maintains a connection to an MCP server and obtains context
  from an MCP server for the MCP host to use"
- "MCP Server: A program that provides context to MCP clients"
- "Note that MCP server refers to the program that serves context data, regardless of where
  it runs. MCP servers can execute locally or remotely. For example, when Claude Desktop
  launches the filesystem server, the server runs locally on the same machine because it uses
  the STDIO transport. This is commonly referred to as a "local" MCP server. The official
  Sentry MCP server runs on the Sentry platform, and uses the Streamable HTTP transport. This
  is commonly referred to as a "remote" MCP server."
- "Local MCP servers that use the STDIO transport typically serve a single MCP client, whereas
  remote MCP servers that use the Streamable HTTP transport will typically serve many MCP
  clients."
- "Stdio transport: Uses standard input/output streams for direct process communication
  between local processes on the same machine"
- "Streamable HTTP transport: Uses HTTP POST for client-to-server messages ... This transport
  enables remote server communication and supports standard HTTP authentication methods
  including bearer tokens, API keys, and custom headers. MCP recommends using OAuth"
- "Tools: Executable functions that AI applications can invoke to perform actions"
- "Resources: Data sources that provide contextual information to AI applications"
- "Prompts: Reusable templates that help structure interactions with language models"
- "The AI application fetches available tools from all connected MCP servers and combines
  them into a unified tool registry that the language model can access."
- "When the language model decides to use a tool during a conversation, the AI application
  intercepts the tool call, routes it to the appropriate MCP server, executes it, and returns
  the results back to the LLM"
- Sampling (server asks the host's model for a completion) is "deprecated as of protocol
  version 2026-07-28".

## Model Context Protocol, Specification (2026-07-28)

https://modelcontextprotocol.io/specification/latest

- "The protocol uses JSON-RPC 2.0 messages to establish communication between: Hosts: LLM
  applications that initiate connections; Clients: Connectors within the host application;
  Servers: Services that provide context and capabilities"
- "MCP takes some inspiration from the Language Server Protocol"
- "Resources: Context and data, for the user or the AI model to use; Prompts: Templated
  messages and workflows for users; Tools: Functions for the AI model to execute"
- "descriptions of tool behavior such as annotations should be considered untrusted, unless
  obtained from a trusted server."
- "Hosts must obtain explicit user consent before invoking any tool"

## Specification, Architecture (2026-07-28)

https://modelcontextprotocol.io/specification/2026-07-28/architecture

- "Each client is created by the host and communicates with exactly one server"
- "Servers should not be able to read the whole conversation, nor "see into" other servers"
- "Servers receive only necessary contextual information" / "Full conversation history stays
  with the host"
- Servers "Can be local processes or remote services"
- Its diagram: host process with three clients; servers 1 and 2 on the "Local machine" reach
  local resources; server 3 on the "Internet" reaches a remote resource.

## Specification, Server features overview

https://modelcontextprotocol.io/specification/2026-07-28/server

| Primitive | Control | Description | Example |
|---|---|---|---|
| Prompts | User-controlled | Interactive templates invoked by user choice | Slash commands, menu options |
| Resources | Application-controlled | Contextual data attached and managed by the client | File contents, git history |
| Tools | Model-controlled | Functions exposed to the LLM to take actions | API POST requests, file writing |

## Understanding MCP servers

https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts

- "MCP servers are programs that expose specific capabilities to AI applications through
  standardized protocol interfaces."
- "Tools ... Functions that your LLM can actively call, and decides when to use them based on
  user requests." Who controls it: Model.
- "Resources ... Passive data sources that provide read-only access to information for
  context" Who controls it: Application.
- "Prompts ... Pre-built instruction templates" Who controls it: User.
- "Prompts are user-controlled, requiring explicit invocation rather than automatic
  triggering."

## Specification, stdio transport

https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio

- "In the stdio transport, the client launches the MCP server as a subprocess."
- "The server reads JSON-RPC messages from stdin and writes JSON-RPC messages to stdout."
- "The client SHOULD initiate shutdown by: Closing the input stream to the child process"

## Specification, Streamable HTTP transport

https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http

- "the server operates as an independent process that can handle multiple client connections."
- "The server MUST provide a single HTTP endpoint path ... For example, this could be a URL
  like https://example.com/mcp."
- "When running locally, servers SHOULD bind only to localhost (127.0.0.1)"

## Client best practices

https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices

- "Loading every tool definition into the model's context window upfront wastes tokens,
  increases latency, and degrades model performance."
- "when a host has access to dozens of servers exposing hundreds of tools, those definitions
  alone can consume the majority of the context window before the model has even read the
  user's message."
- Figure caption: "The upfront approach consumes ~150,000 tokens on definitions alone, while
  progressive discovery uses ~2,000 tokens by loading only what the task requires."
- "For a handful of tools, this is perfectly reasonable."

## Claude Code, Connect Claude Code to tools via MCP

https://code.claude.com/docs/en/mcp

- `claude mcp add --transport http notion https://mcp.notion.com/mcp`
- `claude mcp add [options] <name> -- <command> [args...]`
- "Stdio servers run as local processes on your machine."
- "Project-scoped servers enable team collaboration by storing configurations in a .mcp.json
  file at your project's root directory."
- `.mcp.json`: `{"mcpServers": {"shared-server": {"type": "http", "url": "https://example.com/mcp"}}}`
- "Claude Code reads an entry with no type as a stdio server."
- "Tool search keeps MCP context usage low by deferring tool definitions until Claude needs
  them. Only tool names and server instructions load at session start"
- "Tool search is enabled by default: MCP tools are deferred and discovered on demand."
- "each upfront tool consumes context that would otherwise be available for your conversation."
- "Claude Code displays a warning when any MCP tool output exceeds 10,000 tokens"
- Resources: "MCP servers can expose resources that you can reference using @ mentions"
- Prompts: "MCP servers can expose prompts that become available as commands in Claude Code."

## Codex, Model Context Protocol

https://learn.chatgpt.com/docs/extend/mcp?surface=cli (redirected from developers.openai.com/codex/mcp)

- "By default this is ~/.codex/config.toml."
- "Configure each MCP server with a [mcp_servers.<server-name>] table in the configuration file."
- "STDIO servers: Servers that run as a local process (started by a command)."
- "Streamable HTTP servers: Servers that you access at an address."
- `[mcp_servers.context7]` / `command = "npx"` / `args = ["-y", "@upstash/context7-mcp"]`
- The page's per-server controls are all about tools (`enabled_tools`, `disabled_tools`). It
  doesn't mention resources or prompts.

## VS Code, Use MCP servers

https://code.visualstudio.com/docs/copilot/chat/mcp-servers

- "Portable files use a top-level mcpServers object. The VS Code format uses servers."
- "Workspace .vscode/mcp.json or user-profile mcp.json."
- "Command (stdio)" ... "The server communicates through standard input and output."
- "Servers can provide more than tools." Lists tools, resources, prompts.
- Prompts: "typing /<server>.<prompt> in chat." Resources: "Add Context > MCP Resources".

## GitHub Docs, Configure MCP servers for Copilot

https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- "Copilot cloud agent and Copilot code review only support MCP tools."
- "They do not currently support resources or prompts provided by the MCP server."
- "The JSON must contain an mcpServers object."

## GitHub MCP server README

https://github.com/github/github-mcp-server

- Remote: hosted by GitHub at "https://api.githubcopilot.com/mcp/".
- Local: "docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN ghcr.io/github/github-mcp-server",
  or "the github-mcp-server stdio command". The same server can run on your machine and call
  GitHub's web API, or run at GitHub's URL.

## Notes for the writer (not for the guide)

- "Host" is the spec's word for the harness. The guide says harness and mentions host once.
- The spec's own overview calls servers "Services that provide context and capabilities",
  which is part of why people expect a server to be a service somewhere.
- Tools are the one kind of offer the model chooses for itself. Resources are picked by the
  harness or by you (@ mentions, Add Context), prompts by you (slash commands). Copilot cloud
  agent and code review support only tools; Codex's page lists only tool controls. Claude
  Code and VS Code support all three. So: every harness that supports MCP uses tools; support
  for resources and prompts varies. Say "as of October 2026".
