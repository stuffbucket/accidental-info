---
title: VS Code and Visual Studio
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to where GitHub Copilot’s agent setup lives, as of October 2026.
running_footer: VS Code and Visual Studio
edition: [Co]Lab · bstucker · October 2026
cover_footer: October 2026
version: 0.1.1
---

# What can you set up<br/>in VS Code? {#why}

You can set up five things for GitHub Copilot’s agent in VS Code: instructions files, custom agents, skills, MCP servers and settings. Each one is a file or a setting, and each can belong to a repo, to you, or to your organization.

The default harness in VS Code is the Copilot harness, which reads .github/ in the repo and ~/.copilot/ in your home folder. Other harnesses read other places, noted where they differ. For the basics, see An Accidental Guide to: Agents, Harnesses, Skills, and Tools.

> | Term | Meaning |
> |---|---|
> | Instructions file | Rules the agent follows, always or for matching files. |
> | Custom agent | A role with its own instructions, tools and model. |
> | Skill | Steps the agent loads when a task needs them. |
> | MCP server | A program that gives the agent more tools. |
> | Setting | A switch that changes what VS Code does or reads. |

# Instructions file {#entry num=01 mono=In}

| Field | Text |
|---|---|
| Identify by | .github/copilot-instructions.md, AGENTS.md, or a file ending in .instructions.md. |
| What | An instructions file is text Copilot adds to your requests. copilot-instructions.md and AGENTS.md apply to every request, and a .instructions.md file can apply only to files that match its applyTo pattern. |
| So what | Put the rules you’d otherwise repeat in every chat here. When one seems ignored, check where the file is and what its applyTo pattern matches. |

## Confused with: Setting

An instructions file tells the agent how to work. A setting changes what VS Code itself does.

# Custom agent {#entry num=02 mono=Ag}

| Field | Text |
|---|---|
| Identify by | A .agent.md file in .github/agents/, or a name in the Agent dropdown. |
| What | A custom agent is a saved role with its own instructions, tools and model. You pick one from the Agent dropdown, and another agent can start it as a sub-agent. |
| So what | Limiting a custom agent’s tools limits what it can change. While it’s selected, its instructions are added to your instructions files and win if the two conflict. |

## Confused with: Instructions file

An instructions file applies to every request. A custom agent applies only while it’s selected or running. Custom agents used to be called chat modes, and .chatmode.md files can be renamed to .agent.md.

# Skill {#entry num=03 mono=Sk}

| Field | Text |
|---|---|
| Identify by | A folder with a SKILL.md file whose name matches the folder. |
| What | A skill is a written procedure in a folder. Only its name and description load at first, and the rest loads when your request matches or you type /skill-name. |
| So what | A skill can hold long steps without taking up room until it’s needed. When a skill doesn’t run, check its description first. |

## Confused with: Prompt file

A prompt file, .github/prompts/*.prompt.md, is a saved prompt you run with /name. Prompt files only work in the Local harness, so VS Code suggests a skill instead.

# MCP server {#entry num=04 mono=Mc}

| Field | Text |
|---|---|
| Identify by | An entry with a command or a URL in .mcp.json or ~/.copilot/mcp-config.json. |
| What | An MCP server is a separate program that gives the agent more tools. The harness connects to it and passes the model’s tool calls to it. |
| So what | A local MCP server can run code on your machine with your permissions. Add only servers you trust, and check whether your organization limits which ones you can use. |

## Confused with: Extension

An extension adds features to VS Code itself. MCP servers are listed in the same Extensions view: search @mcp, then choose Install for yourself or Install in Workspace for the repo.

# Setting {#entry num=05 mono=Se}

| Field | Text |
|---|---|
| Identify by | A value in the Settings editor, your user settings or .vscode/settings.json. |
| What | A setting is a switch or value that changes how VS Code behaves. Copilot’s settings turn features on and off, such as chat.useAgentSkills for skills. |
| So what | When something works for a teammate and not for you, compare settings. Your user settings apply in every repo you open. |

## Confused with: Instructions file

A setting decides what VS Code does. An instructions file tells the agent how to work.

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

The Local harness also reads .vscode/mcp.json and files kept in your VS Code profile. The Claude harness reads .claude/ and ~/.claude/ instead.

# How scopes combine {#scopes}

Instructions add up, and settings override. Custom agents, skills and MCP servers from every scope are offered together.

| Thing | When more than one scope has one |
|---|---|
| Instructions file | Every file that applies is added, and none ranks above another. |
| Custom agent | All appear in the Agent dropdown. The selected agent’s instructions win a conflict. |
| Skill | All are offered, and each loads when it matches or you name it. |
| MCP server | All are added, and nothing decides between two with the same name, so give each server its own. Your organization can limit which ones run. |
| Setting | The later scope wins: Default, then User, then Workspace. An administrator’s policy wins over all three. |

> [!TIP]
> When two instructions files disagree, change the files so they agree. Neither the folder nor the load order settles it.

# What’s different<br/>in Visual Studio {#vs}

Visual Studio reads many of the same files, but not all, and keeps its settings in Tools › Options.

| Thing | In Visual Studio |
|---|---|
| Instructions file | .github/copilot-instructions.md and .github/instructions/*.instructions.md. Visual Studio 2026 adds personal instructions in %USERPROFILE%/copilot-instructions.md. |
| Prompt file | .github/prompts/*.prompt.md. Type / or #prompt: in chat. |
| Custom agent | .github/agents/*.agent.md, or %USERPROFILE%\.github\agents for your own. Version 18.4 or later. |
| Skill | The same folders as VS Code. Version 18.5 or later. |
| MCP server | Reads %USERPROFILE%\.mcp.json, then .vs\mcp.json, .mcp.json, .vscode\mcp.json and .cursor\mcp.json in the solution folder. Browse in Extensions › MCP Registries… |
| Setting | Tools › Options › GitHub › Copilot, where a checkbox turns instructions files on. |

Visual Studio doesn’t list AGENTS.md as supported as of October 2026, so put rules both editors need in .github/copilot-instructions.md.

# Same thing elsewhere {#elsewhere}

Other agent tools have the same kinds of setup in their own places. Copilot CLI uses the same Copilot harness, so it reads the same .github/ and ~/.copilot/ folders, but it doesn’t run prompt files.

| Thing | In the other tools |
|---|---|
| Instructions file | Claude Code: CLAUDE.md. Codex: AGENTS.md. Claude Desktop: project instructions. |
| Custom agent | Claude Code: .claude/agents/. Codex: .codex/agents/. |
| Skill | Claude Code: .claude/skills/. Codex: .agents/skills/. Claude Desktop: Customize › Skills. |
| MCP server | Claude Code: .mcp.json. Codex: ~/.codex/config.toml. Claude Desktop: Customize › Connectors. |
| Setting | Claude Code: .claude/settings.json. Codex: ~/.codex/config.toml. |

Each tool has its own guide: An Accidental Guide to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to: GitHub Copilot CLI and An Accidental Guide to: Codex.

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
