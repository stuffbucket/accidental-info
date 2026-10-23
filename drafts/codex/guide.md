---
title: OpenAI Codex
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to where Codex keeps its setup, and which copy wins, as of October 2026.
running_footer: OpenAI Codex
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: friend@accidental.info · October 2026
collection: Accidental Intelligence
collection_mark: square
number: 05
version: 0.3.0
---

# What can you set up<br/>in Codex? {#why}

You can give Codex standing instructions, skills, MCP servers, settings and permissions. Each one is a plain file, and the Codex CLI, the IDE extension and the ChatGPT desktop app all read the same files.

Most of these files live in your Codex home folder, ~/.codex unless CODEX_HOME says otherwise, or in your project. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains the basics.

> | Term | Meaning |
> |---|---|
> | Instructions file | Guidance Codex reads at the start of every session. |
> | Skill | Steps for one kind of task, read when the task comes up. |
> | MCP server | A program that gives Codex tools for another system. |
> | Config file | The file that holds settings such as the model and MCP servers. |
> | Permissions | What commands may change, and when Codex stops to ask you. |

# Instructions file {#entry num=01 mono=In}

| Field | Text |
|---|---|
| Identify by | AGENTS.md, in ~/.codex/ or anywhere in a project. |
| What | Codex reads your AGENTS.md, then each one from the project’s root down to where you work. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains them. |
| So what | Put guidance in the folder it’s about. The file closest to your work has the last word. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Loads | At the start of a session |
> | Add with | /init |

## Confused with: Skill

Codex reads an instructions file every session. A skill’s steps are read only when the skill is used.

# Skill {#entry num=02 mono=Sk}

| Field | Text |
|---|---|
| Identify by | A folder with a SKILL.md file. |
| What | Codex reads the rest of a skill when your task matches its description, or when you type $ and its name. An Accidental Guide to: Agent Skills explains skills. |
| So what | A project’s skills in .agents/skills/ reach everyone who works on it. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Loads | Description first |
> | Check with | /skills |

## Confused with: Plugin

A plugin packages skills, MCP servers and hooks to install together, using /plugins in the CLI.

# MCP server {#entry num=03 mono=Mc}

| Field | Text |
|---|---|
| Identify by | A [mcp_servers.docs] table in config.toml. |
| What | Each server’s entry gives a command that starts it on your computer, or the url of a remote one. An Accidental Guide to: Model Context Protocol explains MCP servers. |
| So what | Set a server up once and it works in the CLI, the IDE extension and the desktop app. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Add with | codex mcp add |
> | Check with | /mcp |

## Confused with: Tool

The MCP server is the program. The tools it offers are what Codex calls.

# Config file {#entry num=04 mono=Se}

| Field | Text |
|---|---|
| Identify by | config.toml, in ~/.codex/ or in a project’s .codex/ folder. |
| What | Settings are the choices that control how Codex runs, such as the model. Codex keeps them in config.toml, along with MCP servers and permissions. |
| So what | Your own config.toml applies everywhere, and a project’s .codex/config.toml changes settings for that project. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Loads | When Codex starts |
> | Override with | -c for one run |

## Confused with: Requirements file

Your config.toml sets defaults you can change. An administrator’s requirements.toml sets limits you can’t.

# Permissions {#entry num=05 mono=Pe}

| Field | Text |
|---|---|
| Identify by | sandbox_mode and approval_policy in config.toml. |
| What | Codex has two permission settings. The sandbox decides what commands can touch: read-only, workspace-write or danger-full-access. The approval policy, on-request or never, decides when Codex stops to ask. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains permissions. |
| So what | The sandbox keeps a wrong command away from everything outside your work. In a Git folder Codex starts with workspace-write and on-request, and elsewhere read-only. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Network | Off by default |
> | Change with | /permissions |

## Confused with: Rules

Rules files in ~/.codex/rules/ say whether a command may run outside the sandbox: allow, prompt or forbidden.

# Where things live {#where}

Your own files apply in every project. A project’s files are kept in its repository.

| Scope | Thing | Path |
|---|---|---|
| Your home folder | Instructions | ~/.codex/AGENTS.md, or AGENTS.override.md beside it |
| Your home folder | Skills | ~/.agents/skills/ |
| Your home folder | Config file | ~/.codex/config.toml, which also holds MCP servers and permissions, with profiles beside it |
| Your home folder | Hooks, rules, agents | ~/.codex/hooks.json, ~/.codex/rules/, ~/.codex/agents/ |
| This project | Instructions | AGENTS.md in any folder |
| This project | Skills | .agents/skills/ in any folder |
| This project | Config file | .codex/config.toml |
| This project | Hooks, rules, agents | .codex/hooks.json, .codex/rules/, .codex/agents/ |
| Your organization | Config file | /etc/codex/config.toml, or defaults from the admin console |
| Your organization | Skills | /etc/codex/skills/ |
| Your organization | Requirements | /etc/codex/requirements.toml, or the admin console |
| Codex Cloud | Skills | Only the repository’s skills. Personal skills aren’t synced. |

> [!NOTE]
> Codex reads a project’s .codex folder only after you trust the project, so a repository you haven’t trusted can’t change your settings, hooks or rules.

# How do the places combine? {#combine}

> | Config file | Where the value comes from, strongest first |
> |---|---|
> | 1 | A flag or -c on the command line |
> | 2 | The project’s .codex/config.toml closest to where you work |
> | 3 | A profile picked with --profile |
> | 4 | Your ~/.codex/config.toml |
> | 5 | Your organization’s defaults |
> | 6 | Codex’s built-in defaults |
>
> | Other setup | When two places set it |
> |---|---|
> | Instructions | Codex joins them, yours first, then the project’s from the root down, so the closest file has the last word. |
> | Skills | Codex offers all of them. Two with the same name both appear. |
> | MCP servers | Servers can be in your config.toml or a project’s, and a setting for the same server follows the numbered list. |
> | Hooks | Codex keeps all of them. |
> | Rules | The strictest match wins: forbidden, then prompt, then allow. |

# Same thing elsewhere {#elsewhere}

| Codex | Claude Code | Claude Desktop | Copilot CLI | VS Code and Visual Studio |
|---|---|---|---|---|
| Instructions file | CLAUDE.md | Instructions | AGENTS.md | AGENTS.md |
| Skill | Skills | Skills | Skills | Skills |
| MCP server | .mcp.json | Connectors | .mcp.json | .mcp.json |
| Config file | settings.json | Settings | settings.json | Settings |
| Permissions | settings.json | Settings | Settings | Settings |

Each of these tools has its own guide: An Accidental Guide to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to: GitHub Copilot CLI, and An Accidental Guide to: VS Code and Visual Studio.

# Sources {#sources}

These public sources were checked on 22 October 2026.

| Source | Publisher | Address |
|---|---|---|
| Config basics | OpenAI | learn.chatgpt.com/docs/config-file/config-basic |
| Advanced Configuration | OpenAI | learn.chatgpt.com/docs/config-file/config-advanced |
| Custom instructions with AGENTS.md | OpenAI | learn.chatgpt.com/docs/agent-configuration/agents-md |
| Build skills | OpenAI | learn.chatgpt.com/docs/build-skills |
| Model Context Protocol | OpenAI | learn.chatgpt.com/docs/extend/mcp |
| Agent approvals and security | OpenAI | learn.chatgpt.com/docs/agent-approvals-security |
| Package your plugin | OpenAI | developers.openai.com/plugins/build/plugins |
| Hooks | OpenAI | learn.chatgpt.com/docs/hooks |
| Rules | OpenAI | learn.chatgpt.com/docs/agent-configuration/rules |
| Cloud environments | OpenAI | learn.chatgpt.com/docs/environments/cloud-environments |
| Managed configuration | OpenAI | learn.chatgpt.com/docs/enterprise/managed-configuration |
