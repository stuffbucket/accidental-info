---
title: Claude Desktop
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to where Claude Desktop keeps its settings, as of October 2026.
running_footer: Claude Desktop
edition: [Co]Lab · bstucker · October 2026
cover_footer: October 2026
version: 0.1.1
---

# What can you set up<br/>in Claude Desktop? {#why}

In Claude Desktop you can tell Claude how to answer you, save the steps for tasks you repeat, connect Claude to the apps you use, and choose what Claude may do without asking. Most of these settings belong to your Claude account and also apply on claude.ai. A few belong to this computer only.

You’ll find them in Settings and in Customize, in the left sidebar. For what a skill, a tool and an MCP server are, see An Accidental Guide to: Agents, Harnesses, Skills, and Tools.

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
| Identify by | Settings > General, and Set project instructions on a project’s page. |
| What | Instructions are text you write for Claude to follow. The ones in Settings apply to all your chats, and project instructions apply only inside that project. |
| So what | Put a preference you always want in Settings, and one that matters for a single piece of work in that project. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Works in | Web, desktop and mobile | Instructions belong to your account. |

## Confused with: Memory

Memory is what Claude picks up from your chats, in Settings > Memory. Instructions are what you write yourself.

# Skills {#entry num=02 mono=Sk}

| Field | Text |
|---|---|
| Identify by | Customize > Skills. |
| What | A skill is a saved set of steps for one kind of task. Turn on an example skill or upload your own, and Claude follows the steps when that task comes up. |
| So what | You explain a task once instead of in every chat. Your skills also load in Claude Code when you sign in with the same account. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Works in | Web, desktop and Claude Code | Skills need Code execution and file creation, in Settings > Capabilities. |

## Confused with: Instructions

Instructions apply to every chat. A skill’s steps apply only to its kind of task.

# Connectors {#entry num=03 mono=Mc}

| Field | Text |
|---|---|
| Identify by | Customize > Connectors, or the + button in the message box. |
| What | A connector is an MCP server on the internet, usually for a service you sign in to. You add it once and it works wherever you use Claude. |
| So what | For each of a connector’s tools you choose Always allow, Needs approval or Blocked. Free plans can add one custom connector. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Works in | Web, desktop and mobile | Local files and apps need a local MCP server instead. |

## Confused with: Desktop extension

A desktop extension is a local MCP server in a .mcpb file, installed in Settings > Extensions. Extensions run on this computer and work only in Claude Desktop and Claude Code.

# Plugins {#entry num=04 mono=Pl}

| Field | Text |
|---|---|
| Identify by | Customize > Plugins, on the Discover tab. |
| What | A plugin is a package of skills, connectors and sub-agents. Plugins are saved to your account, not to your computer. |
| So what | One install sets up what you need for a role. Your organization may install some plugins for you. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Works in | Chat, Cowork and Claude Code | Paid plans only. A plugin with a local MCP server needs the desktop app. |

## Confused with: Skills

A skill is one set of steps. A plugin can hold several skills, plus connectors and sub-agents.

# Settings and permissions {#entry num=05 mono=Se}

| Field | Text |
|---|---|
| Identify by | Settings, from your initials in the lower left, and the permission setting in the message box. |
| What | Settings holds your account’s preferences, such as General, Capabilities and Memory. Claude Desktop adds Extensions and Developer, which apply to this computer only. |
| So what | The permission setting decides how much Claude does without asking. The default is Manual, where Claude asks before it acts. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Works in | Your account and this computer | Owners and IT can turn some options off. |

## Confused with: Customize

Customize is where you add skills, connectors and plugins. Settings is where you set preferences and permissions.

# Where things live {#where}

Most things live in your Claude account and show up wherever you sign in. A few live on this computer and work only in Claude Desktop.

| What | Lives in | Where to find it |
|---|---|---|
| Instructions | Account | Settings > General, and each project’s page |
| Memory | Account | Settings > Memory |
| Skills | Account | Customize > Skills |
| Connectors | Account | Customize > Connectors, then a connector for its tool permissions |
| Plugins | Account | Customize > Plugins |
| Code execution | Account | Settings > Capabilities |
| Folder access | This computer | Settings, under Trusted folders |
| Desktop extensions | This computer | Settings > Extensions |
| Local MCP servers | This computer | Settings > Developer > Edit Config<br/>macOS: ~/Library/Application Support/Claude/claude_desktop_config.json<br/>Windows: %APPDATA%\Claude\claude_desktop_config.json |
| MCP logs | This computer | macOS: ~/Library/Logs/Claude<br/>Windows: %APPDATA%\Claude\logs |
| Code tab | This computer | ~/.claude/settings.json and ~/.claude/skills, the same files Claude Code uses |

Chats and Cowork use what’s in Customize. The Code tab reads ~/.claude instead, like Claude Code; see An Accidental Guide to: Claude Code.

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

On computers your company manages, IT can set the desktop app’s options in com.anthropic.claudefordesktop on macOS or HKLM\SOFTWARE\Policies\Claude on Windows, for example to turn off desktop extensions. These override the allowlist in the app. If something is missing, ask your owner.

# Same thing elsewhere {#elsewhere}

Coding tools keep the same kinds of things in their own files.

| In Claude Desktop | Elsewhere |
|---|---|
| Instructions | CLAUDE.md in Claude Code, AGENTS.md in Codex, copilot-instructions.md or AGENTS.md in Copilot CLI and VS Code |
| Skills | A folder with a SKILL.md file, in Claude Code under ~/.claude/skills. Codex, Copilot CLI and VS Code have skills too. |
| Connectors | MCP servers: .mcp.json in Claude Code, ~/.codex/config.toml in Codex, the User or Workspace group in VS Code |
| Plugins | Plugins in all four |
| Settings and permissions | ~/.claude/settings.json in Claude Code, approval_policy and sandbox_mode in ~/.codex/config.toml |

See An Accidental Guide to: Claude Code, An Accidental Guide to: GitHub Copilot CLI, An Accidental Guide to: Codex and An Accidental Guide to: Visual Studio and VS Code.

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
