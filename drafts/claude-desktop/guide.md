---
title: Claude Desktop
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to where Claude Desktop keeps its settings, as of October 2026.
running_footer: Claude Desktop
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: friend@accidental.info · October 2026
collection: Accidental Intelligence
collection_mark: square
number: 03
version: 0.3.0
---

# What can you set up<br/>in Claude Desktop? {#why}

In Claude Desktop you can tell Claude how to answer you, save the steps for tasks you repeat, connect Claude to the apps you use, and choose what Claude may do without asking. Most of these settings belong to your Claude account and also apply on claude.ai.

You’ll find them in Settings and in Customize, in the left sidebar. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains the basics.

> | Term | Meaning |
> |---|---|
> | Instructions | What you want Claude to know in every chat, or in one project. |
> | Skills | Saved steps Claude follows for one kind of task. |
> | Connectors | An MCP server you add so Claude can reach another app or service. |
> | Plugins | A package of skills, connectors and sub-agents. |
> | Settings and permissions | Your preferences, and how much Claude may do before it asks. |

# Instructions {#entry num=01 mono=In}

| Field | Text |
|---|---|
| Identify by | Settings > General, or a project’s page. |
| What | Instructions are text you write for Claude to follow, in all your chats or in one project. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains instructions. |
| So what | Put a preference you always want in Settings, and one for a single piece of work in that project. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Works in | Web, desktop, mobile |

## Confused with: Memory

Memory is what Claude picks up from your chats, in Settings > Memory. Instructions are what you write yourself.

# Skills {#entry num=02 mono=Sk}

| Field | Text |
|---|---|
| Identify by | Customize > Skills. |
| What | A skill is a saved set of steps for one kind of task, which Claude follows when that task comes up. An Accidental Guide to: Agent Skills explains skills. |
| So what | You explain a task once instead of in every chat. Skills need Code execution, in Settings > Capabilities. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Works in | Web, desktop and Claude Code |

## Confused with: Instructions

Instructions apply to every chat. A skill’s steps apply only to its kind of task.

# Connectors {#entry num=03 mono=Mc}

| Field | Text |
|---|---|
| Identify by | Customize > Connectors, or the + button in the message box. |
| What | A connector is an MCP server on the internet, usually for a service you sign in to. An Accidental Guide to: Model Context Protocol explains MCP servers. |
| So what | For each of a connector’s tools you choose Always allow, Needs approval or Blocked. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Works in | Web, desktop, mobile |

## Confused with: Desktop extension

A desktop extension is a local MCP server in a .mcpb file, installed in Settings > Extensions. Extensions work only on this computer.

# Plugins {#entry num=04 mono=Pl}

| Field | Text |
|---|---|
| Identify by | Customize > Plugins, on the Discover tab. |
| What | A plugin is a package of skills, connectors and sub-agents, saved to your account. An Accidental Guide to: Plugins, Connectors, and Marketplaces explains plugins. |
| So what | One install sets up what you need for a role. Plugins need a paid plan, and your organization may install some for you. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Works in | Chat, Cowork and Claude Code |

## Confused with: Skills

A skill is one set of steps. A plugin can hold several skills, plus connectors and sub-agents.

# Settings and permissions {#entry num=05 mono=Se}

| Field | Text |
|---|---|
| Identify by | Settings, under your initials, and the permission setting in the message box. |
| What | Settings holds your account’s preferences, such as General, Capabilities and Memory. Extensions and Developer apply to this computer only. |
| So what | The permission setting decides how much Claude does without asking. The default is Manual. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Works in | Account and computer |

## Confused with: Customize

Customize is where you add skills, connectors and plugins. Settings is where you set preferences and permissions.

# Where things live {#where}

Most things live in your Claude account and show up wherever you sign in. A few live on this computer only.

| What | Lives in | Where to find it |
|---|---|---|
| Instructions | Account | Settings > General, and each project’s page |
| Memory | Account | Settings > Memory |
| Skills | Account | Customize > Skills |
| Connectors | Account | Customize > Connectors, then a connector for its tool permissions |
| Plugins | Account | Customize > Plugins |
| Code execution | Account | Settings > Capabilities |
| Folder access | Computer | Settings, under Trusted folders |
| Desktop extensions | Computer | Settings > Extensions |
| Local MCP servers | Computer | Settings > Developer > Edit Config<br/>macOS: ~/Library/Application Support/Claude/claude_desktop_config.json<br/>Windows: %APPDATA%\Claude\claude_desktop_config.json |
| Code tab | Computer | ~/.claude/settings.json and ~/.claude/skills, the same files Claude Code uses |

Chats and Cowork use what’s in Customize. The Code tab reads ~/.claude, as Claude Code does. See An Accidental Guide to: Claude Code.

> [!TIP]
> After you edit claude_desktop_config.json, quit Claude Desktop completely and open it again.

# Your account or<br/>your organization? {#account}

On Free, Pro and Max plans you set everything yourself. On Team and Enterprise plans, an owner sets limits in Organization settings.

| Setting | You | An owner, in Organization settings |
|---|---|---|
| Skills | Turn on or upload | Plugins & skills: turn skills on, add skills for everyone, stop people creating skills |
| Connectors | Add and sign in | Connectors: add for the team, set limits nobody can override |
| Plugins | Add from Discover | Add marketplaces, require plugins |
| Desktop extensions | Install allowed ones | Connectors, Desktop tab: the allowlist |
| Memory | Turn on or off | Capabilities: allow memory |

On computers your company manages, IT can set the desktop app’s options in com.anthropic.claudefordesktop on macOS or HKLM\SOFTWARE\Policies\Claude on Windows.

# Same thing elsewhere {#elsewhere}

Coding tools keep the same kinds of things in their own files.

| In Claude Desktop | Elsewhere |
|---|---|
| Instructions | CLAUDE.md in Claude Code. AGENTS.md in Codex, Copilot CLI and VS Code. |
| Skills | A folder with a SKILL.md file, under ~/.claude/skills in Claude Code. Codex, Copilot CLI and VS Code have skills too. |
| Connectors | MCP servers: .mcp.json in Claude Code, ~/.codex/config.toml in Codex, the User or Workspace group in VS Code |
| Plugins | Plugins in all four |
| Settings and permissions | ~/.claude/settings.json in Claude Code, approval_policy and sandbox_mode in ~/.codex/config.toml |

See An Accidental Guide to: Claude Code, An Accidental Guide to: GitHub Copilot CLI, An Accidental Guide to: OpenAI Codex and An Accidental Guide to: VS Code and Visual Studio.

# Sources {#sources}

These public sources were checked on 22 October 2026. The Anthropic Help Center articles, listed first, are at support.claude.com/en/articles/ and their number.

| Source | Address |
|---|---|
| Use connectors | 11176164 |
| Desktop and web connectors | 11725091 |
| Local MCP servers on Claude Desktop | 10949351 |
| Desktop extension allowlist | 12592343 |
| Enterprise configuration for Claude Desktop | 12622667 |
| Use skills in Claude | 12512180 |
| Use plugins in Claude | 13837440 |
| Personalization features | 10185728 |
| Cowork and chat are one Claude | 16761823 |
| Create and manage projects | 9519177 |
| Chat search and memory | 11817273 |
| Anthropic, Claude Code on desktop | code.claude.com/docs/en/desktop |
| Model Context Protocol, Connect to local MCP servers | modelcontextprotocol.io/docs/develop/connect-local-servers |
| OpenAI, Codex config basics | learn.chatgpt.com/docs/config-file/config-basic |
| OpenAI, Codex AGENTS.md | learn.chatgpt.com/docs/agent-configuration/agents-md |
| GitHub, Copilot customization cheat sheet | docs.github.com/en/copilot/reference/customization-cheat-sheet |
| Visual Studio Code, Agent customization overview | code.visualstudio.com/docs/agent-customization/overview |
