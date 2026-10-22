# Writer instructions, round 3: GitHub Copilot CLI (cut to five minutes)

Edit `./guide.md` in place. Round 2 reads well but prints about 1,880 words; the target is about
1,200. Replace the line ranges below with the given text, word for word (only fix a typo if you
see one). Work from the bottom of the file up so the line numbers stay right. Keep all format
rules from writer-round1.md: table shapes, header rows, ids, no full stop at the end of a Short
answer cell, typographic apostrophes.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

## Edits

Lines 206 and 209: delete these two source rows (Adding agent skills; plugin reference).

Lines 160-177 (combine section, from the heading through the closing paragraph) become:

```
# How do the places combine? {#combine}

When the same kind of setup is in more than one place, instructions and hooks add up. Skills,
MCP servers, custom agents and settings have one winner for each name or key.

| Thing | When two places set it |
|---|---|
| Instructions | Every file that applies is used, and none outranks another. |
| Skills | The first found wins: the repository’s, then yours, then a plugin’s. |
| MCP servers | From highest: --additional-mcp-config, a plugin, the repository, then ~/.copilot/mcp-config.json. |
| Custom agents | Yours wins, then the repository’s, a plugin’s, the organization’s, then the enterprise’s. |
| Settings | Later layers win: yours, the repository’s, settings.local.json, environment variables, then flags. Managed settings lock most keys. |
| Hooks | Every hook runs. |

The first time you start Copilot CLI in a folder, it asks whether you trust it. Repository MCP
servers, hooks and plugin settings load only after you say yes. /env shows everything the session
loaded.
```

Lines 181-183 (elsewhere intro) become:

```
The other tools keep the same kinds of setup under their own names. Copilot CLI also reads
CLAUDE.md, .claude/skills/, .agents/skills/, .claude/agents/ and .mcp.json.
```

Lines 114-133 (Settings entry, heading through its Confused with paragraph) become:

```
# Settings {#entry num=05 mono=Se}

| Field | Text |
|---|---|
| Identify by | A settings.json file in ~/.copilot, or in .github/copilot in the repository. |
| What | Settings hold your choices for how Copilot CLI runs, such as the model and which plugins are on. The folders you trust are kept in config.json, and the tools you’ve allowed to run without asking in permissions-config.json. |
| So what | Trust and approvals decide what Copilot CLI does without asking you first. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Loads | When the session starts | Flags such as --allow-tool last for that run only. |
| Check with | /settings | Shows each setting and lets you change it. |

## Confused with: Policy

A policy is a setting your organization or enterprise manages, such as which models you can use.
Its value overrides yours.
```

Lines 93-112 (Custom agent entry) become:

```
# Custom agent {#entry num=04 mono=Ag}

| Field | Text |
|---|---|
| Identify by | A file such as .github/agents/reviewer.agent.md. |
| What | A custom agent is a file that sets up an agent for one job, with its own instructions and tools. An Accidental Guide to: Agents, Harnesses, Skills, and Tools calls this an agent definition. |
| So what | You can pick one to run your session, or Copilot CLI can hand one part of a task. A repository or an organization can share agents with everyone who works there. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Loads | When you pick it or it’s handed work | The body becomes that agent’s instructions. |
| Check with | /agent | Lists the agents you can pick. |

## Confused with: Subagent

A subagent is any agent the main agent hands work to. A custom agent can be either the main agent
or a subagent.
```

Lines 71-91 (MCP server entry) become:

```
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
```

Lines 50-69 (Skill entry) become:

```
# Skill {#entry num=02 mono=Sk}

| Field | Text |
|---|---|
| Identify by | A folder with a SKILL.md file, such as .github/skills/release-notes/SKILL.md. |
| What | A skill is a written procedure for one kind of task. Copilot CLI uses it when the skill’s description matches your request, or when you type its name, such as /release-notes. |
| So what | A skill keeps the way you do a task in a file that can be reviewed and shared like code. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Loads | Description first, steps when used | Only the name and description are there from the start. |
| Check with | /skills | Lists the skills the session found. |

## Confused with: Custom agent

The agent you’re talking to follows a skill’s steps itself. A custom agent is a separate agent
with its own instructions and tools.
```

Lines 29-48 (Instructions file entry) become:

```
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
```

Lines 13-27 (page 2, the two paragraphs and the table) become:

```
Copilot CLI reads its setup from files. There are five kinds, and each can sit in your home
folder, in the repository you’re working in, or come from your organization. When two copies
disagree, Copilot CLI has a rule for which one wins.

The words agent, skill, tool and session are explained in An Accidental Guide to: Agents,
Harnesses, Skills, and Tools.

| Term | Meaning |
|---|---|
| Instructions file | Rules and facts about your project, read at the start of every session. |
| Skill | Written steps for one kind of task, read when that task comes up. |
| MCP server | A separate program that gives Copilot CLI tools for another system. |
| Custom agent | A separate agent with its own job, instructions and tools. |
| Settings | Your choices for how Copilot CLI runs, including trust and approvals. |
```

When done, print `wc -w guide.md` and stop.
