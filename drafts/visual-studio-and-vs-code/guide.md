---
title: VS Code and Visual Studio
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to where GitHub Copilot’s agent setup lives, as of October 2026.
running_footer: VS Code and Visual Studio
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: friend@accidental.info · October 2026
version: 0.2.0
---

# What can you set up<br/>in VS Code? {#why}

You can set up five things for GitHub Copilot’s agent in VS Code: instructions files, custom agents, skills, MCP servers and settings. Each can belong to a repo, to you or to your organization.

VS Code’s default harness, the Copilot harness, reads .github/ in the repo and ~/.copilot/ in your home folder. For the basics, see An Accidental Guide to: Agents, Harnesses, Skills, and Tools.

> | Term | Meaning |
> |---|---|
> | Instructions file | Rules the agent follows, always or for matching files. |
> | Custom agent | A role with its own instructions, tools and model. |
> | Skill | Steps the agent loads when a task needs them. |
> | MCP server | A program that gives the agent more tools. |
> | Setting | A switch or value that changes what VS Code does. |

# Instructions file {#entry num=01 mono=In}

| Field | Text |
|---|---|
| Identify by | copilot-instructions.md, AGENTS.md or a .instructions.md file. |
| What | An instructions file is text Copilot adds to your requests. See An Accidental Guide to: Agents, Harnesses, Skills, and Tools. |
| So what | Put rules you’d otherwise repeat in every chat here. An applyTo pattern makes a file apply only to matching files. |

> | Field | Short answer |
> |---|---|
> | Loads | When it applies |
> | Cannot | Settle a conflict |

## Confused with: Setting

An instructions file tells the agent how to work. A setting changes what VS Code does.

# Custom agent {#entry num=02 mono=Ag}

| Field | Text |
|---|---|
| Identify by | A .agent.md file, or a name in the Agent dropdown. |
| What | A custom agent is a saved role with its own instructions, tools and model. See An Accidental Guide to: Agents, Harnesses, Skills, and Tools. |
| So what | Limiting a custom agent’s tools limits what it can change. Give each agent only the tools its job needs. |

> | Field | Short answer |
> |---|---|
> | Loads | When picked or started |
> | Cannot | Replace instructions |

## Confused with: Chat mode

Chat mode is the old name for a custom agent, and a .chatmode.md file can be renamed to .agent.md.

# Skill {#entry num=03 mono=Sk}

| Field | Text |
|---|---|
| Identify by | A folder with a SKILL.md file whose name matches the folder. |
| What | A skill is a written procedure in a folder. Type /skill-name to run one. See An Accidental Guide to: Agent Skills. |
| So what | A skill’s steps take up no room until they’re needed. When a skill doesn’t run, check its description first. |

> | Field | Short answer |
> |---|---|
> | Loads | Description first |
> | Cannot | Add a tool |

## Confused with: Prompt file

A prompt file (.prompt.md) is a saved prompt you run with /name. Only the Local harness runs them, so VS Code suggests a skill.

# MCP server {#entry num=04 mono=Mc}

| Field | Text |
|---|---|
| Identify by | An entry with a command or a URL in .mcp.json or ~/.copilot/mcp-config.json. |
| What | An MCP server is a program that gives the agent more tools. Search @mcp in Extensions to find one. See An Accidental Guide to: Model Context Protocol. |
| So what | A local MCP server runs code on your machine with your permissions. Add only servers you trust. |

> | Field | Short answer |
> |---|---|
> | Loads | When it connects |
> | Cannot | Act by itself |

## Confused with: Extension

An extension adds features to VS Code itself. MCP servers install from the same view, for you or for the workspace.

# Setting {#entry num=05 mono=Se}

| Field | Text |
|---|---|
| Identify by | A value in the Settings editor, your user settings or .vscode/settings.json. |
| What | A setting is a switch or value that changes how VS Code behaves. For example, chat.useAgentSkills turns skills on and off. |
| So what | When something works for a teammate and not for you, compare your settings. Your user settings apply in every repo. |

> | Field | Short answer |
> |---|---|
> | Loads | From every scope |
> | Cannot | Guide the agent |

## Confused with: Policy

A policy is a setting an administrator makes for your organization. It wins over your own settings.

# Where things live {#where}

The Copilot harness reads these places. Use the repo for what the team shares and your home folder for what’s only yours.

> | Thing | Scope | Location |
> |---|---|---|
> | Instructions file | Repo | .github/copilot-instructions.md |
> |  |  | AGENTS.md, from the root down to the working folder |
> |  |  | .github/instructions/*.instructions.md |
> |  | You | ~/.copilot/copilot-instructions.md |
> |  |  | ~/.copilot/instructions/*.instructions.md |
> |  | Organization | Copilot settings in your GitHub organization |
> | Custom agent | Repo | .github/agents/*.agent.md |
> |  | You | ~/.copilot/agents/*.agent.md |
> |  | Organization | agents/ in the organization’s .github-private repo |
> | Skill | Repo | .github/skills/ |
> |  |  | .agents/skills/ |
> |  | You | ~/.copilot/skills/ |
> |  |  | ~/.agents/skills/ |
> | MCP server | Repo | .mcp.json |
> |  | You | ~/.copilot/mcp-config.json |
> |  | Organization | A registry of approved servers, set in GitHub |
> | Setting | Repo | .vscode/settings.json |
> |  | You | Your user settings.json |
> |  | Organization | Policies set by an administrator |

The Local harness also reads .vscode/mcp.json. The Claude harness reads .claude/ and ~/.claude/ instead.

# How scopes combine {#scopes}

Instructions add up, and settings override.

| Thing | When more than one scope has one |
|---|---|
| Instructions file | Every file that applies is added. None takes priority. |
| Custom agent | The selected agent’s instructions win a conflict. |
| MCP server | Give each server its own name. Your organization can limit which ones run. |
| Setting | Default, then User, then Workspace, and the later one wins. An administrator’s policy wins over all three. |

> [!TIP]
> When two instructions files disagree, change them so they agree. The load order won’t settle it.

# What’s different<br/>in Visual Studio {#vs}

| Thing | In Visual Studio |
|---|---|
| Instructions file | .github/copilot-instructions.md and .github/instructions/*.instructions.md. In Visual Studio 2026, personal instructions go in %USERPROFILE%/copilot-instructions.md. |
| Custom agent | .github/agents/*.agent.md, or %USERPROFILE%\.github\agents for your own. Version 18.4 or later. |
| Skill | The same folders as VS Code. Version 18.5 or later. |
| MCP server | %USERPROFILE%\.mcp.json, then .vs\mcp.json, .mcp.json, .vscode\mcp.json and .cursor\mcp.json in the solution folder. |
| Setting | Tools › Options › GitHub › Copilot, where a checkbox turns instructions files on. |

Visual Studio doesn’t list AGENTS.md as supported, so put rules both editors need in .github/copilot-instructions.md.

# Same thing elsewhere {#elsewhere}

Copilot CLI uses the same Copilot harness, so it reads the same .github/ and ~/.copilot/ folders.

| Thing | In the other tools |
|---|---|
| Instructions file | Claude Code: CLAUDE.md. Codex: AGENTS.md. Claude Desktop: project instructions. |
| Custom agent | Claude Code: .claude/agents/. Codex: .codex/agents/. |
| Skill | Claude Code: .claude/skills/. Codex: .agents/skills/. Claude Desktop: Customize › Skills. |
| MCP server | Claude Code: .mcp.json. Codex: ~/.codex/config.toml. Claude Desktop: Customize › Connectors. |
| Setting | Claude Code: .claude/settings.json. Codex: ~/.codex/config.toml. |

Each has its own guide: An Accidental Guide to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to: GitHub Copilot CLI and An Accidental Guide to: OpenAI Codex.

# Sources {#sources}

These public pages were checked on 22 October 2026.

| Source | Publisher | Address |
|---|---|---|
| Choose an Agent Harness | VS Code | code.visualstudio.com/docs/agents/run/agent-harnesses |
| Custom instructions | VS Code | code.visualstudio.com/docs/copilot/customization/custom-instructions |
| Custom agents | VS Code | code.visualstudio.com/docs/agent-customization/custom-agents |
| Agent skills | VS Code | code.visualstudio.com/docs/agent-customization/agent-skills |
| MCP servers | VS Code | code.visualstudio.com/docs/agent-customization/mcp-servers |
| User and workspace settings | VS Code | code.visualstudio.com/docs/configure/settings |
| Customize chat responses | Microsoft Learn | learn.microsoft.com/visualstudio/ide/copilot-chat-context |
| Custom agents in Visual Studio | Microsoft Learn | learn.microsoft.com/visualstudio/ide/copilot-specialized-agents |
| MCP servers in Visual Studio | Microsoft Learn | learn.microsoft.com/visualstudio/ide/mcp-servers |
| Customization cheat sheet | GitHub Docs | docs.github.com/en/copilot/reference/customization-cheat-sheet |
| Claude Code settings | Anthropic | code.claude.com/docs/en/settings |
| Use Skills in Claude | Anthropic | support.claude.com/en/articles/12512180 |
| Codex configuration basics | OpenAI | learn.chatgpt.com/docs/config-file/config-basic |
