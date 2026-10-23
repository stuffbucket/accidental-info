---
title: GitHub Copilot CLI
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to where Copilot CLI keeps its setup, and which copy wins, as of October 2026.
running_footer: GitHub Copilot CLI
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: friend@accidental.info · October 2026
collection: Accidental Intelligence
collection_mark: square
number: 04
version: 0.3.0
---

# What can you set up<br/>in Copilot CLI? {#why}

Copilot CLI reads its setup from files. There are five kinds, and each can sit in your home
folder, in the repository you’re working in, or come from your organization. When two copies
disagree, Copilot CLI has a rule for which one wins.

The words agent, skill, tool and session are explained in An Accidental Guide to: Agents,
Harnesses, Skills, and Tools.

> | Term | Meaning |
> |---|---|
> | Instructions file | Rules about your project, read in every session. |
> | Skill | Steps for one kind of task, read when it comes up. |
> | MCP server | A program that adds tools for another system. |
> | Custom agent | A separate agent with its own job and tools. |
> | Settings | How Copilot CLI runs, including trust and approvals. |

# Instructions file {#entry num=01 mono=In}

| Field | Text |
|---|---|
| Identify by | AGENTS.md or .github/copilot-instructions.md. |
| What | Copilot CLI adds every instructions file that applies to the session. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains them. |
| So what | Put rules for every session here. No file outranks another, so keep each rule in one place. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Loads | At the start of a session |
> | Check with | /instructions |

## Confused with: Skill

A skill’s steps are read only when a task calls for them, so a long procedure belongs in a skill.

# Skill {#entry num=02 mono=Sk}

| Field | Text |
|---|---|
| Identify by | A folder in .github/skills/ with a SKILL.md file. |
| What | Copilot CLI uses a skill when your request matches its description, or when you type / and its name. An Accidental Guide to: Agent Skills explains skills. |
| So what | A skill keeps the way you do a task in a file that can be reviewed and shared like code. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Loads | Description first |
> | Check with | /skills |

## Confused with: Custom agent

The agent you’re talking to follows a skill’s steps itself. A custom agent is a separate agent
with its own instructions and tools.

# MCP server {#entry num=03 mono=Mc}

| Field | Text |
|---|---|
| Identify by | An entry in ~/.copilot/mcp-config.json or .mcp.json. |
| What | GitHub’s own MCP server is built in and needs no setup. An Accidental Guide to: Model Context Protocol explains MCP servers. |
| So what | Add a server when the work needs a system Copilot CLI can’t reach on its own, such as an issue tracker. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Loads | When the session starts |
> | Check with | /mcp |

## Confused with: Plugin

A plugin is a package you install that can bring MCP servers, skills, custom agents and hooks
with it.

# Custom agent {#entry num=04 mono=Ag}

| Field | Text |
|---|---|
| Identify by | A file such as .github/agents/reviewer.agent.md. |
| What | Copilot CLI reads custom agents from your Copilot folder, the repository and your organization. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains agents. |
| So what | You can pick one to run your session, or Copilot CLI can hand one part of a task. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Loads | When it runs |
> | Check with | /agent |

## Confused with: Subagent

A subagent is any agent the main agent hands work to. A custom agent can be either the main agent
or a subagent.

# Settings {#entry num=05 mono=Se}

| Field | Text |
|---|---|
| Identify by | A settings.json file in ~/.copilot, or in .github/copilot in the repository. |
| What | Settings are the choices that control how Copilot CLI runs, such as the model. Trusted folders are kept in config.json, and tools you’ve allowed to run without asking in permissions-config.json. |
| So what | Trust and approvals decide what Copilot CLI does without asking you first. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Loads | When the session starts |
> | Check with | /settings |

## Confused with: Policy

A policy is a setting your organization or enterprise manages, such as which models you can use.
Its value overrides yours.

# Where things live {#where}

~/.copilot is your Copilot folder. If you set COPILOT_HOME, Copilot CLI uses that
directory instead.

| Scope | Thing | Path |
|---|---|---|
| Your home folder | Instructions | ~/.copilot/copilot-instructions.md or ~/.copilot/instructions/ |
| Your home folder | Skills | ~/.copilot/skills/ or ~/.agents/skills/ |
| Your home folder | MCP servers | ~/.copilot/mcp-config.json |
| Your home folder | Custom agents | ~/.copilot/agents/ |
| Your home folder | Settings | ~/.copilot/settings.json, with approvals in permissions-config.json and trusted folders in config.json beside it |
| This repository | Instructions | .github/copilot-instructions.md, .github/instructions/*.instructions.md, AGENTS.md, CLAUDE.md or GEMINI.md |
| This repository | Skills | .github/skills/, .agents/skills/ or .claude/skills/ |
| This repository | MCP servers | .github/mcp.json to share, or .mcp.json |
| This repository | Custom agents | .github/agents/ or .claude/agents/ |
| This repository | Settings | .github/copilot/settings.json, or .github/copilot/settings.local.json for you only |
| This repository | Hooks | .github/hooks/*.json |
| Your organization | Custom agents | agents/ in the organization’s .github or .github-private repository |
| Your organization | Policies | copilot/managed-settings.json in the .github-private repository, plus policies an administrator sets on GitHub |

> [!NOTE]
> As of October 2026, custom instructions that an organization sets on GitHub don’t reach Copilot
> CLI. The CLI reads only the instruction files in your Copilot folder and in the repository.

# How do the places combine? {#combine}

Instructions and hooks add up. Skills, MCP servers, custom agents and settings have one winner for each name or setting.

> | Thing | When two places set it |
> |---|---|
> | Instructions | Every file that applies is used, and none outranks another. |
> | Skills | The first found wins: the repository’s, then yours, then a plugin’s. |
> | MCP servers | From highest: --additional-mcp-config, a plugin, the repository, then ~/.copilot/mcp-config.json. |
> | Custom agents | Yours wins, then the repository’s, a plugin’s, the organization’s, then the enterprise’s. |
> | Settings | Later layers win: yours, the repository’s, settings.local.json, environment variables, then flags. Managed settings win over most of them. |
> | Hooks | Every hook runs. |

> [!TIP]
> Repository MCP servers, hooks and plugin settings load only after you trust the folder. /env
> shows everything the session loaded.

# Same thing elsewhere {#elsewhere}

| Copilot CLI | Claude Code | Claude Desktop | Codex | VS Code and Visual Studio |
|---|---|---|---|---|
| Instructions file | CLAUDE.md | Instructions | AGENTS.md | Same file |
| Skill | Skills | Skills | Skills | Same folder |
| MCP server | .mcp.json | Connectors | config.toml | Same file |
| Custom agent | Subagents | None documented | Custom agents | Same folder |
| Settings | settings.json | Settings | config.toml | IDE settings |

Each of these tools has its own guide: An Accidental Guide to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to: OpenAI Codex, and An Accidental Guide to: VS Code and Visual Studio.

# Sources {#sources}

These public sources were checked on 22 October 2026.

| Source | Publisher | Address |
|---|---|---|
| GitHub Copilot CLI configuration directory | GitHub Docs | docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference |
| GitHub Copilot CLI command reference | GitHub Docs | docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference |
| Adding custom instructions for GitHub Copilot CLI | GitHub Docs | docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions |
| Adding MCP servers for GitHub Copilot CLI | GitHub Docs | docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers |
| Invoking custom agents | GitHub Docs | docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents |
| Allowing and denying tool use | GitHub Docs | docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools |
| copilot help | GitHub Copilot CLI 1.0.102 | copilot --help, copilot help config |
