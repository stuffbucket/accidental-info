---
title: Claude Code
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to where Claude Code keeps its setup, as of October 2026.
running_footer: Accidental Guide to Claude Code
edition: [Co]Lab · bstucker · October 2026
cover_footer: October 2026
version: 0.1.1
---

# What can you set up<br/>in Claude Code? {#why}

Claude Code reads its setup from plain files, some in your home folder and some in the project. There are five kinds of setup: instructions files, skills, MCP servers, plugins and settings.

Each kind can be yours alone, shared with the project, or set by your organization, and each lives in a different place. For what skills, tools and MCP servers are, see An Accidental Guide to: Agents, Harnesses, Skills, and Tools.

> | Term | Meaning |
> |---|---|
> | Instructions file | Text added to every session, such as build commands. |
> | Skill | A written procedure, loaded when a task needs it. |
> | MCP server | A program that gives Claude Code tools for another system. |
> | Plugin | A package of skills, MCP servers and hooks, installed together. |
> | Settings | JSON files for permissions, hooks and other behavior. |

# Instructions file {#entry num=01 mono=In}

| Field | Text |
|---|---|
| Identify by | CLAUDE.md, or AGENTS.md. |
| What | An instructions file holds what Claude Code should know in every session, such as build commands and conventions. AGENTS.md is read only when there’s no CLAUDE.md. |
| So what | Write down what you’d otherwise explain again each session. Run /init to start a CLAUDE.md. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Loads | At the start of each session | Files from your working folder and every folder above it combine. |
> | Cannot | Enforce a rule | To block an action, use a deny rule or a hook in settings. |

## Confused with: Settings

Instructions are guidance the model reads. Settings are rules Claude Code enforces.

# Skill {#entry num=02 mono=Sk}

| Field | Text |
|---|---|
| Identify by | A folder with a SKILL.md file. |
| What | A skill is a written procedure that Claude Code loads when a task needs it. You can also run one by name, such as /deploy. |
| So what | Steps that matter only for some tasks belong in a skill, so they don’t take up room in every session. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Loads | Name and description at startup | The rest loads when Claude Code or you call the skill. |
> | Cannot | Add a tool | A skill that reads a database still needs a tool that reaches it. |

## Confused with: Instructions file

An instructions file loads in full every session. A skill loads in full only when it’s used.

# MCP server {#entry num=03 mono=Mc}

| Field | Text |
|---|---|
| Identify by | An entry under mcpServers, with a start command or a URL. |
| What | An MCP server is a separate program that gives Claude Code tools for another system. Add one with claude mcp add. |
| So what | Servers in a project’s .mcp.json ask for your approval before first use, so a cloned repository can’t connect servers without you. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Loads | When the session starts | Claude Code connects and gets the server’s list of tools. |
> | Cannot | Act by itself | Nothing happens until the model calls one of the server’s tools. |

## Confused with: Plugin

A plugin can bring its own MCP server. You add or remove that server along with the plugin.

# Plugin {#entry num=04 mono=Pl}

| Field | Text |
|---|---|
| Identify by | A folder with .claude-plugin/plugin.json. |
| What | A plugin packages skills, agent definitions, hooks and MCP servers to install as one unit. Most come from a marketplace, a catalog you add once with /plugin marketplace add. |
| So what | An enabled plugin is part of every session, and what it runs, it runs as you. Check what a plugin adds before you install it. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Loads | At startup, when enabled | An enabledPlugins entry in a settings file turns it on. |
> | Cannot | Install itself for teammates | A project entry turns the plugin on for them, but each person still installs it once. |

## Confused with: Skill

A skill is one folder you can copy in yourself. A plugin is a package, usually from a marketplace, that can carry many skills and other parts.

# Settings {#entry num=05 mono=Se}

| Field | Text |
|---|---|
| Identify by | settings.json, settings.local.json or managed-settings.json. |
| What | Settings are JSON files that control which commands run without asking, which hooks run and which plugins are on. |
| So what | Permission rules allow, ask about or deny tool calls. Hooks are commands Claude Code runs at set points, such as before a tool call. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Loads | At startup, and again on save | Claude Code watches the files, so most edits apply right away. |
> | Cannot | Override your organization | Nothing in your own files changes a managed setting. |

## Confused with: Instructions file

Claude Code enforces settings. The model reads an instructions file as guidance.

# Where do the<br/>files live? {#where}

Most setup sits in two .claude/ folders, one in your home folder and one in the project. The group names are the scope names the Claude Code docs use.

| User: you, in every project | Where |
|---|---|
| Instructions | ~/.claude/CLAUDE.md |
| Skills | ~/.claude/skills/ |
| MCP servers | ~/.claude.json |
| Plugins | ~/.claude/plugins/, turned on in ~/.claude/settings.json |
| Settings | ~/.claude/settings.json |

| Project: shared with the team, and local: only you | Where |
|---|---|
| Instructions | CLAUDE.md or .claude/CLAUDE.md, and CLAUDE.local.md for local |
| Skills | .claude/skills/ |
| MCP servers | .mcp.json, and ~/.claude.json for local |
| Plugins | turned on in the project’s settings files |
| Settings | .claude/settings.json, and .claude/settings.local.json for local |

| Managed: set by your organization | Where |
|---|---|
| Folder | /Library/Application Support/ClaudeCode/ on macOS, /etc/claude-code/ on Linux, C:\Program Files\ClaudeCode\ on Windows |
| Instructions | CLAUDE.md in that folder |
| Skills | .claude/skills/ in that folder |
| MCP servers | managed-mcp.json in that folder |
| Settings | managed-settings.json in that folder, or a policy from MDM or the admin console |

> [!TIP]
> /status shows which settings files loaded, /context the instructions files, /mcp the servers and /plugin the plugins.

# Which one wins? {#scopes}

Some kinds add up across places. For others, one place wins.

| Thing | When it’s set in more than one place |
|---|---|
| Settings | Highest first: managed, the --settings flag, local, project, user. Lists such as permission rules combine. |
| Permission rules | All rules count. Deny is checked first, then ask, then allow, so a deny anywhere blocks the call. |
| Hooks | All of them run. |
| Instructions | All of them load. The file closest to where you started is read last. |
| Skills | Same name: managed, then user, then project. Plugin skills carry the plugin’s name, so they don’t clash. |
| MCP servers | Same name: local, then project, then user, then plugins. The whole entry comes from one place. |
| Plugins | Local, then project, then user. |

Nothing in your own files or on the command line changes a managed setting. Run /status to see which managed source applies.

# The same things<br/>in other tools {#elsewhere}

Each of these tools has its own guide. The paths are as of October 2026.

| Guide | What to look for there |
|---|---|
| An Accidental Guide to: Claude Desktop | Most setup is done in the app itself. Local MCP servers go in claude_desktop_config.json. |
| An Accidental Guide to: GitHub Copilot CLI | AGENTS.md or .github/copilot-instructions.md, .github/skills/, and ~/.copilot/ for settings and MCP servers. |
| An Accidental Guide to: Codex | AGENTS.md, .agents/skills/, and ~/.codex/config.toml for settings and MCP servers. |
| An Accidental Guide to: Visual Studio and VS Code | .github/copilot-instructions.md, .github/skills/ in VS Code, and a .mcp.json file for MCP servers. |

Codex, GitHub Copilot CLI and VS Code read AGENTS.md, and Claude Code reads it when there’s no CLAUDE.md. GitHub Copilot CLI and VS Code also read .claude/skills/.

# Sources {#sources}

Checked in October 2026. Claude Code changes often, so check the current docs before you rely on a path.

| Source | Date | Address |
|---|---|---|
| Claude Code: Settings |  | code.claude.com/docs/en/settings |
| Claude Code: Managed settings |  | code.claude.com/docs/en/managed-settings |
| Claude Code: Memory |  | code.claude.com/docs/en/memory |
| Claude Code: The .claude directory |  | code.claude.com/docs/en/claude-directory |
| Claude Code: Skills |  | code.claude.com/docs/en/skills |
| Claude Code: MCP |  | code.claude.com/docs/en/mcp |
| Claude Code: Install plugins |  | code.claude.com/docs/en/plugins/install |
| Claude Code: Permissions |  | code.claude.com/docs/en/permissions |
| Claude Code: Hooks |  | code.claude.com/docs/en/hooks |
| MCP: Connect to local servers |  | modelcontextprotocol.io/docs/develop/connect-local-servers |
| GitHub: Copilot CLI configuration |  | docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference |
| OpenAI: Codex configuration |  | learn.chatgpt.com/docs/config-file/config-basic |
| VS Code: Agent skills |  | code.visualstudio.com/docs/copilot/customization/agent-skills |
