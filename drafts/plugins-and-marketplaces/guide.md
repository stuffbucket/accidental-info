---
title: Plugins, Connectors, and Marketplaces
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to the names for things you add to a coding agent or AI app.
running_footer: Plugins, Connectors, and Marketplaces
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: hi@accidental.info · October 2026
version: 0.2.0
---

# What are all these things? {#why}

Every product lets you add things to a coding agent or AI app, but each product uses its
own names and the same word can mean different things. Every one of them is one of five
kinds of thing: tools, instructions, hooks, packages and marketplaces.

Claude apps means claude.ai and the Claude Desktop app. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains the basic terms.

# The map {#map}

Each colored line is one kind of thing, and each stop is a name you’ll see.

```map
line To | Tools: reach other systems | MCP server, Desktop extension, Extension
line In | Instructions: how to work | Instructions file, Skill, Slash command, Prompt file, Agent definition
line Hk | Hooks: run at set moments | Hook
line Pl | Packages: install in one step | Extension, Plugin
line Mk | Marketplaces: lists to install from | Marketplace, Directory, MCP registry
station MCP server | 0 0 | r
also MCP server | Connector | Claude apps
also MCP server | App | ChatGPT, Codex
station Desktop extension | 0 1.8 | r
also Desktop extension | Local connector | Claude apps
station Extension | 0.8 3.6 | br
station Instructions file | 4 0 | l
also Instructions file | Project instructions | Claude apps
station Skill | 4 1.1 | l
station Slash command | 4 2.2 | l
also Slash command | Command | Claude Code
station Prompt file | 4 3.3 | l
also Prompt file | Custom prompt | Codex, deprecated
station Agent definition | 3.6 4.9 | l
also Agent definition | Custom agent | Copilot, VS Code, Visual Studio
also Agent definition | Subagent | Claude Code, Codex
station Hook | 1.2 5.5 | r
station Plugin | 2 3.6 | b
also Plugin | Agent plugin | VS Code
station Marketplace | 0 7 | ar
also Marketplace | Visual Studio Marketplace | editor extensions
also Marketplace | Claude Marketplace | a website
station Directory | 2 7 | b
also Directory | Connectors Directory | Claude apps
station MCP registry | 4 7 | al
```

> [!TIP]
> Find a new word on its line, then check the product because names can overlap.

# Tools {#entry num=01 mono=To}

| Field | Text |
|---|---|
| What | Most tools you add come from MCP servers, which some products call connectors, apps or extensions. See An Accidental Guide to: Agents, Harnesses, Skills, and Tools. |
| So what | One MCP server works in all these products, so ask for one when the agent needs a new system. See An Accidental Guide to: Model Context Protocol. |

## Names

> | Name | What it is |
> |---|---|
> | MCP server | A program that gives the agent tools |
> | Connector | What Claude apps call an MCP server. OpenAI says app. |
> | Desktop extension | A local MCP server in one file, for Claude Desktop |
> | Extension | A tool module in Copilot CLI, or a VS Code add-on that adds tools |

## Confused with: Instructions

A tool reaches another system. Instructions say when to use it.

# Instructions {#entry num=02 mono=In}

| Field | Text |
|---|---|
| What | Instructions tell the agent how to work. An instructions file loads every session. See An Accidental Guide to: Agents, Harnesses, Skills, and Tools. |
| So what | Put rules in an instructions file. Steps for one kind of task go in a skill, which loads only when a task needs it. See An Accidental Guide to: Agent Skills. |

## Names

> | Name | What it is |
> |---|---|
> | Instructions file | Read every session, such as AGENTS.md or CLAUDE.md. Claude apps say project instructions. |
> | Skill | Loaded when the task matches or when you type /name |
> | Prompt file | A saved prompt you run with /name |
> | Custom agent | Sets up a sub-agent. Claude Code and Codex say subagent. |

## Confused with: Hooks

Instructions guide the model. A hook runs every time, even if the model skips an instruction.

# Hooks {#entry num=03 mono=Hk}

| Field | Text |
|---|---|
| What | A hook is a command the harness runs at a set moment, such as after every edit. The model does not choose whether it runs. |
| So what | Use a hook for anything that must happen every time. A check before each commit is one example. |

## Names

> | Name | What it is |
> |---|---|
> | Hook | A command the harness runs on an event |
> | Hook | In Claude apps, only inside a plugin, in Cowork |

## Confused with: Tools

A tool runs when the model calls it. A hook runs when its event happens.

# Packages {#entry num=04 mono=Pl}

| Field | Text |
|---|---|
| What | A plugin is a package of skills, agent definitions, hooks and MCP servers. You install it in one step. |
| So what | Copilot CLI, VS Code and Codex read Claude Code’s plugin files. Each loads only the parts it supports. |

## Names

> | Name | What it is |
> |---|---|
> | Plugin | A folder of agent parts installed as one package |
> | Agent plugin | VS Code’s name for a plugin |
> | Extension | An add-on for the VS Code or Visual Studio editor |
> | IDE extension | Claude Code or Codex itself, inside the editor |

## Confused with: Marketplaces

A plugin is a package you install. A marketplace tells your product where to find it.

# Marketplaces {#entry num=05 mono=Mk}

| Field | Text |
|---|---|
| What | A plugin marketplace is a marketplace.json catalog in a Git repository. Add it, then install plugins by name. |
| So what | Anyone can publish a marketplace, so adding one means trusting whoever runs it. Anthropic reviews the plugins in its directory, but not ones added from a marketplace. |

## Names

> | Name | What it is |
> |---|---|
> | Marketplace | A list of plugins kept in a Git repository |
> | Directory | A list the company reviews, such as the Connectors Directory |
> | MCP registry | GitHub’s list of MCP servers |
> | Visual Studio Marketplace | The store for VS Code and Visual Studio extensions |

## Confused with: Visual Studio Marketplace

The Visual Studio Marketplace is a store for editor extensions, and Claude Marketplace is a website. Neither one is a plugin marketplace.

# Which product uses which word {#who}

These are the words each product uses, and what they mean there, as of October 2026. No means the product’s documentation doesn’t use the word.

> | Word | Claude Code | Claude apps | Copilot CLI | VS Code | Visual Studio | Codex |
> |---|---|---|---|---|---|---|
> | MCP server | yes | as connector | yes | yes | yes | yes |
> | Connector | from claude.ai | MCP server | no | no | no | inside plugins |
> | Extension | harness in an editor | local MCP server | tool module | editor add-on | editor add-on | harness in an editor |
> | Instructions file | CLAUDE.md | project instructions | yes | yes | yes | AGENTS.md |
> | Prompt file | merged into skills | no | no | Local harness only | yes | deprecated |
> | Custom agent | subagent | Cowork only | yes | yes | yes | subagent |
> | Hook | yes | Cowork only | yes | preview | no | yes |
> | Plugin | yes | yes | yes | agent plugin | no | not in the IDE |
> | Marketplace | plugin list | plugin list | plugin list | both kinds | extension store | plugin list |

Each product has its own guide: An Accidental Guide to: Claude Code, An Accidental Guide
to: Claude Desktop, An Accidental Guide to: GitHub Copilot CLI, An Accidental Guide to:
OpenAI Codex, and An Accidental Guide to: VS Code and Visual Studio.

# Sources {#sources}

These public sources were checked in October 2026.

| Source | Date | Address |
|---|---|---|
| Anthropic, Claude Code: plugins | October 2026 | code.claude.com/docs/en/plugins |
| Anthropic, Claude: plugins | October 2026 | claude.com/docs/plugins/overview |
| Anthropic, Claude: connectors | October 2026 | claude.com/docs/connectors |
| GitHub, Plugins for GitHub Copilot | October 2026 | docs.github.com/en/copilot/concepts/customizations/plugins |
| Microsoft, Agent plugins in VS Code | October 2026 | code.visualstudio.com/docs/agent-customization/agent-plugins |
| Microsoft, Use MCP servers to extend GitHub Copilot in Visual Studio | October 2026 | learn.microsoft.com/en-us/visualstudio/ide/mcp-servers |
| OpenAI, Plugins | October 2026 | learn.chatgpt.com/docs/plugins |
| OpenAI, Plugin controls | October 2026 | learn.chatgpt.com/docs/enterprise/apps-and-connectors |
