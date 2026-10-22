---
title: GitHub Copilot CLI
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to where Copilot CLI keeps its setup, and which copy wins, as of October 2026.
running_footer: GitHub Copilot CLI
edition: [Co]Lab · bstucker · October 2026
cover_footer: October 2026
version: 0.1.0
---

# What can you set up<br/>in Copilot CLI? {#why}

Copilot CLI reads its setup from files. There are five kinds, and each can sit in your home
folder, in the repository you’re working in, or come from your organization. When two copies
disagree, Copilot CLI has a rule for which one wins.

The words agent, skill, tool and session are explained in An Accidental Guide to: Agents,
Harnesses, Skills, and Tools.

| Term | Meaning |
|---|---|
| Instructions file | Rules about your project, read in every session. |
| Skill | Steps for one kind of task, read when it comes up. |
| MCP server | A program that adds tools for another system. |
| Custom agent | A separate agent with its own job and tools. |
| Settings | How Copilot CLI runs, including trust and approvals. |

# Instructions file {#entry num=01 mono=In}

| Field | Text |
|---|---|
| Identify by | A Markdown file such as .github/copilot-instructions.md or AGENTS.md. |
| What | An instructions file tells Copilot CLI about your project and how you want the work done. Copilot CLI reads every file that applies and adds them all to the session. |
| So what | Put rules here that should hold in every session, such as how to run the tests. No file outranks another, so keep each rule in one place. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Loads | At the start of a session | Changes reach the next session. |
| Check with | /instructions | Lists the files the session loaded and lets you turn one off. |

## Confused with: Skill

A skill’s steps are read only when a task calls for them, so a long procedure belongs in a skill.

# Skill {#entry num=02 mono=Sk}

| Field | Text |
|---|---|
| Identify by | A folder with a SKILL.md file, such as .github/skills/release-notes/SKILL.md. |
| What | A skill is a written procedure for one kind of task. Copilot CLI uses it when the skill’s description matches your request, or when you type its name, such as /release-notes. |
| So what | A skill keeps the way you do a task in a file that can be reviewed and shared like code. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Loads | Description first, steps when used |  |
| Check with | /skills | Lists the skills the session found. |

## Confused with: Custom agent

The agent you’re talking to follows a skill’s steps itself. A custom agent is a separate agent
with its own instructions and tools.

# MCP server {#entry num=03 mono=Mc}

| Field | Text |
|---|---|
| Identify by | An entry with a command or URL in ~/.copilot/mcp-config.json or .mcp.json. |
| What | An MCP server is a separate program that gives Copilot CLI tools for another system, such as an issue tracker. GitHub’s own MCP server is built in and needs no setup. |
| So what | Add a server when the work needs a system Copilot CLI can’t reach on its own. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Loads | When the session starts | Servers in the repository load only in a trusted folder. |
| Check with | /mcp | Lists the servers and lets you add, turn off or remove one. |

## Confused with: Plugin

A plugin is a package you install that can bring MCP servers, skills, custom agents and hooks
with it.

# Custom agent {#entry num=04 mono=Ag}

| Field | Text |
|---|---|
| Identify by | A file such as .github/agents/reviewer.agent.md. |
| What | A custom agent is a file that sets up an agent for one job, with its own instructions and tools. An Accidental Guide to: Agents, Harnesses, Skills, and Tools calls this an agent definition. |
| So what | You can pick one to run your session, or Copilot CLI can hand one part of a task. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Loads | When you pick it or it’s handed work | The body becomes that agent’s instructions. |
| Check with | /agent | Lists the agents you can pick. |

## Confused with: Subagent

A subagent is any agent the main agent hands work to. A custom agent can be either the main agent
or a subagent.

# Settings {#entry num=05 mono=Se}

| Field | Text |
|---|---|
| Identify by | A settings.json file in ~/.copilot, or in .github/copilot in the repository. |
| What | Settings hold your choices for how Copilot CLI runs, such as the model. Trusted folders are kept in config.json, and tools you’ve allowed to run without asking in permissions-config.json. |
| So what | Trust and approvals decide what Copilot CLI does without asking you first. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Loads | When the session starts | Flags such as --allow-tool last for that run only. |
| Check with | /settings | Shows each setting and lets you change it. |

## Confused with: Policy

A policy is a setting your organization or enterprise manages, such as which models you can use.
Its value overrides yours.

# Where things live {#where}

~/.copilot is your Copilot folder. If you set COPILOT_HOME, Copilot CLI uses that
directory instead.

| Scope | Thing | Path |
|---|---|---|
| Just you | Instructions | ~/.copilot/copilot-instructions.md or ~/.copilot/instructions/ |
| Just you | Skills | ~/.copilot/skills/ or ~/.agents/skills/ |
| Just you | MCP servers | ~/.copilot/mcp-config.json |
| Just you | Custom agents | ~/.copilot/agents/ |
| Just you | Settings | ~/.copilot/settings.json; approvals in ~/.copilot/permissions-config.json; trusted folders in ~/.copilot/config.json |
| Just you | Plugins | ~/.copilot/installed-plugins/ |
| This repository | Instructions | .github/copilot-instructions.md, .github/instructions/*.instructions.md, AGENTS.md, CLAUDE.md or GEMINI.md |
| This repository | Skills | .github/skills/, .agents/skills/ or .claude/skills/ |
| This repository | MCP servers | .github/mcp.json to share, or .mcp.json |
| This repository | Custom agents | .github/agents/ or .claude/agents/ |
| This repository | Settings | .github/copilot/settings.json, or .github/copilot/settings.local.json for you only |
| This repository | Hooks | .github/hooks/*.json |
| Your organization | Custom agents | agents/ in the organization’s .github or .github-private repository |
| Your organization | Policies | copilot/managed-settings.json in the .github-private repository, plus policies an administrator sets on GitHub |

As of October 2026, custom instructions that an organization sets on GitHub don’t reach Copilot
CLI. The CLI reads only the instruction files in your Copilot folder and in the repository.

# How do the places combine? {#combine}

Instructions and hooks add up. Skills, MCP servers, custom agents and settings have one winner
for each name or key.

| Thing | When two places set it |
|---|---|
| Instructions | Every file that applies is used, and none outranks another. |
| Skills | The first found wins: the repository’s, then yours, then a plugin’s. |
| MCP servers | From highest: --additional-mcp-config, a plugin, the repository, then ~/.copilot/mcp-config.json. |
| Custom agents | Yours wins, then the repository’s, a plugin’s, the organization’s, then the enterprise’s. |
| Settings | Later layers win: yours, the repository’s, settings.local.json, environment variables, then flags. Managed settings lock most keys. |
| Hooks | Every hook runs. |

Repository MCP servers, hooks and plugin settings load only after you trust the folder. /env
shows everything the session loaded.

# Same thing elsewhere {#elsewhere}

The other tools keep the same kinds of setup under their own names. Copilot CLI also reads
CLAUDE.md, .claude/skills/, .agents/skills/, .claude/agents/ and .mcp.json.

| Copilot CLI | Claude Code | Claude Desktop | Codex | VS and VS Code |
|---|---|---|---|---|
| Instructions file | CLAUDE.md | Instructions for Claude | AGENTS.md | Same file |
| Skill | Skills | Skills | Skills | Same folder |
| MCP server | .mcp.json | Connectors | config.toml | Same file |
| Custom agent | Subagents | None documented | Custom agents | Same folder |
| Settings | settings.json | Settings | config.toml | IDE settings |

Each of these has its own guide: An Accidental Guide to: Claude Code, An Accidental Guide to:
Claude Desktop, An Accidental Guide to: Codex, and An Accidental Guide to: Visual Studio and VS
Code.

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
