---
title: OpenAI Codex
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to where Codex keeps its setup, and which copy wins, as of October 2026.
running_footer: OpenAI Codex
edition: [Co]Lab · bstucker · October 2026
cover_footer: October 2026
version: 0.1.0
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
| What | An instructions file holds guidance Codex should always have, such as build and test commands and project conventions. Keep it short, since Codex reads all of it every session. |
| So what | Put guidance in the folder it’s about. The file closest to your work has the last word. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Loads | At the start of a session | Yours first, then the project’s. |
> | Add with | /init | Writes a starter AGENTS.md for the project. |

## Confused with: Skill

Codex reads an instructions file every session. A skill’s steps are read only when the skill is used.

# Skill {#entry num=02 mono=Sk}

| Field | Text |
|---|---|
| Identify by | A folder with a SKILL.md file. |
| What | A skill is a written procedure for one kind of task. Codex reads its name and description at the start, and the rest when your task matches the description or you type $ and the skill’s name. |
| So what | You can keep many skills without crowding the session. A project’s skills in .agents/skills/ reach everyone who works on it. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Loads | In two steps | Name and description at the start, steps when used. |
> | Check with | /skills | Shows the skills you can use. |

## Confused with: Plugin

A plugin packages skills, MCP servers and hooks to install together, using /plugins in the CLI. As of October 2026, the IDE extension doesn’t support plugins.

# MCP server {#entry num=03 mono=Mc}

| Field | Text |
|---|---|
| Identify by | A [mcp_servers.docs] table in config.toml. |
| What | An MCP server is a program that gives Codex tools for another system. The entry gives a command that starts it on your computer, or the url of a remote one. |
| So what | Set a server up once and it works in the CLI, the IDE extension and the desktop app. enabled_tools and disabled_tools limit which of its tools Codex sees. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Add with | codex mcp add | Writes the entry into config.toml for you. |
> | Check with | /mcp | Shows the servers Codex is connected to. |

## Confused with: Tool

The MCP server is the program. The tools it offers are what Codex calls.

# Config file {#entry num=04 mono=Se}

| Field | Text |
|---|---|
| Identify by | config.toml, in ~/.codex/ or in a project’s .codex/ folder. |
| What | The config file holds Codex settings, such as the model, MCP servers and permissions, as keys and values in TOML. In the IDE extension, open it from the gear icon, then Codex Settings. |
| So what | Your own config.toml applies everywhere, and a project’s .codex/config.toml changes settings for that project. A profile file, such as ~/.codex/deep-review.config.toml, holds a set of changes you pick with --profile. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Loads | At the start | Restart Codex after a change. |
> | Override with | -c key=value | Changes one setting for one run. |

## Confused with: Requirements file

Your config.toml sets defaults you can change. An administrator’s requirements.toml sets limits you can’t.

# Permissions {#entry num=05 mono=Pe}

| Field | Text |
|---|---|
| Identify by | sandbox_mode and approval_policy in config.toml. |
| What | Permissions are two settings. The sandbox decides what commands can touch: read-only, workspace-write for your working folder, or danger-full-access. The approval policy, on-request or never, decides when Codex stops to ask. |
| So what | The sandbox keeps a wrong command away from everything outside your work. In a Git folder Codex starts with workspace-write and on-request, and elsewhere read-only. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Network | Off by default | Turn it on with network_access under sandbox_workspace_write. |
> | Change with | /permissions | During a session, or start Codex with --sandbox and --ask-for-approval. |

## Confused with: Rules

Rules files in ~/.codex/rules/ say whether a command may run outside the sandbox: allow, prompt or forbidden. Rules are experimental as of October 2026.

# Where things live {#where}

Your own files apply in every project. A project’s files travel with its repository.

| Scope | Thing | Path |
|---|---|---|
| Just you | Instructions | ~/.codex/AGENTS.md, or AGENTS.override.md beside it |
| Just you | Skills | ~/.agents/skills/ |
| Just you | Config file | ~/.codex/config.toml, which also holds MCP servers and permissions; profiles sit beside it |
| Just you | Hooks, rules, agents | ~/.codex/hooks.json, ~/.codex/rules/, ~/.codex/agents/ |
| Just you | Plugins | installed under ~/.codex/plugins/cache/ |
| This project | Instructions | AGENTS.md in any folder |
| This project | Skills | .agents/skills/ in any folder |
| This project | Config file | .codex/config.toml |
| This project | Hooks, rules, agents | .codex/hooks.json, .codex/rules/, .codex/agents/ |
| Your organization | Config file | /etc/codex/config.toml, or defaults from the admin console |
| Your organization | Skills | /etc/codex/skills/ |
| Your organization | Requirements | /etc/codex/requirements.toml, or the admin console |
| Codex Cloud | Environment | Settings, Codex Cloud, Environments |
| Codex Cloud | Skills | the repository’s skills only; personal skills aren’t synced |

> [!NOTE]
> Codex reads a project’s .codex folder only after you trust the project, so a repository you just cloned can’t change your settings, hooks or rules.

# How do the places combine? {#combine}

For a config file setting, the first place on this list that sets a value wins.

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
> | Instructions | Codex joins them, yours first, then the project’s from the root down, so the closest file has the last word. Codex stops reading at 32 KiB by default. |
> | Skills | Codex offers all of them. Two with the same name both appear. |
> | MCP servers | Servers can be in your config.toml or a project’s, and a setting for the same server follows the order above. |
> | Hooks | Codex keeps all of them. |
> | Rules | The strictest match wins: forbidden, then prompt, then allow. |
> | Requirements | Limits an administrator sets. Your files can’t override them. |

> [!TIP]
> When a setting isn’t what you expect, check the list from the top.

# Same thing elsewhere {#elsewhere}

Other coding tools have the same kinds of setup under their own names.

| Codex | Claude Code | Claude Desktop | Copilot CLI | VS Code and Visual Studio |
|---|---|---|---|---|
| Instructions file | Instructions file | Instructions | Instructions file | Instructions file |
| Skill | Skill | Skills | Skill | Skill |
| MCP server | MCP server | Connectors | MCP server | MCP server |
| Config file | Settings | Settings | Settings | Setting |
| Permissions | Settings | Settings and permissions | Settings | Setting |

The details are in An Accidental Guide to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to: GitHub Copilot CLI, and An Accidental Guide to: VS Code and Visual Studio.

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
