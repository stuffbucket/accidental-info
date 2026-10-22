# Writer instructions, round 2: targeted edits to guide.md

Edit `guide.md` in the current folder in place. Apply each edit below by line number (line
numbers refer to the file as it stands now). Keep every heading, id, table shape and the number
of paragraphs in each section, except where an edit says to add a table. Don't change anything
not listed. The format rules from round 1 still hold (no backticks, no emphasis, no `<`, no
slashes in ordinary words, Short answer cells don't end with a full stop, typographic quotes and
apostrophes).

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

The overall problem with the draft: many sentences are clipped and abstract ("Put information
here when Claude Code needs it throughout a session"). Say the concrete thing, in connected
sentences, the way a colleague would explain it. The text below is close to final; you may
smooth wording, but keep each fact and keep it as short.

## Scope names

Switch to the scope names the Claude Code docs and the --scope flags use: user, project, local
and managed. They are explained once, in the group labels on the where page, and then used
plainly everywhere else. Don't use "you, in every project" as a name in running text anymore.

## Edits

- Line 13 (the website blurb, must stand on its own): "Claude Code reads its setup from plain
  files, some in your home folder and some in the project. There are five kinds of setup:
  instructions files, skills, MCP servers, plugins and settings."
- Line 15: "Each kind can be kept for yourself, shared with everyone in the project, or set by
  your organization, and each lives in a different place. That’s where the confusion comes
  from. The paths here are as of October 2026. For what a skill, a tool and an MCP server are,
  see An Accidental Guide to: Agents, Harnesses, Skills, and Tools."
- Lines 19–23, the Meaning cells:
  - Instructions file: "Text added to every session, such as build commands and house rules."
  - Skill: "A written procedure in a folder, loaded when a task calls for it."
  - MCP server: "A program that gives Claude Code tools for another system, such as a tracker."
  - Plugin: "A package of skills, MCP servers, hooks and agent definitions installed together."
  - Settings: "JSON files for permissions, hooks, the model and other behavior."
- Line 30, What: "An instructions file holds what Claude Code should know in every session, such
  as build commands and conventions. Claude Code reads AGENTS.md in place of CLAUDE.md when
  there’s no CLAUDE.md in the working directory or above it."
- Line 31, So what: "Write down what you’d otherwise explain again each session. Run /init to
  start a CLAUDE.md, and /context to see which files loaded."
- Line 37: Short "At the start of each session", Detail "Files in the working directory and
  every folder above it combine. Files in subfolders load when Claude Code works there."
- Line 38: Short "Enforce a rule", Detail "Claude treats the text as guidance. To block an
  action, use a deny rule or a hook in settings."
- Line 42: "An instructions file is guidance the model reads. Settings are rules Claude Code
  enforces, such as which commands need your approval."
- Line 48: "A folder with a SKILL.md file, in .claude/skills/ or ~/.claude/skills/."
- Line 49: "A skill is a written procedure that Claude Code loads when a task needs it. You can
  also run one by name, such as /deploy. Older single files in .claude/commands/ work the same
  way."
- Line 50: "Steps that matter only for some tasks belong in a skill, so they don’t take up room
  in every session."
- Line 56: Short "Name and description at startup", Detail "The rest loads when Claude Code or
  you call the skill."
- Line 57: Short "Add a tool", Detail "A skill that reads a database still needs a tool that
  can reach the database."
- Line 61: "An instructions file loads in full every session. A skill loads in full only when
  it’s used."
- Line 67: "An entry under mcpServers in .mcp.json or ~/.claude.json, with a start command or a
  URL."
- Line 68: "An MCP server is a separate program that gives Claude Code tools for another
  system. Add one with claude mcp add and pick where it’s saved with --scope."
- Line 69: "Servers in a project’s .mcp.json ask for your approval before first use, so a
  cloned repository can’t connect servers without you."
- Line 75: Short "When the session starts", Detail "Claude Code connects to each server and
  gets its list of tools."
- Line 76: Short "Act by itself", Detail "Nothing happens until the model calls one of the
  server’s tools."
- Line 86: "A folder with .claude-plugin/plugin.json, installed with /plugin."
- Line 87: "A plugin packages skills, agent definitions, hooks and MCP servers so they install
  as one unit. Most plugins come from a marketplace, a catalog you add once with /plugin
  marketplace add. Claude Code adds Anthropic’s official marketplace for you."
- Line 88: "An enabled plugin is part of every session, and whatever it runs, it runs as you.
  Read what a plugin adds before you install it."
- Line 94: Short "At startup, when enabled", Detail "An enabledPlugins entry in a settings file
  turns it on. The installed files are kept in ~/.claude/plugins/."
- Line 95: Short "Install itself for teammates", Detail "A project entry turns the plugin on
  for them, but each person still installs it once."
- Line 106: "Settings are JSON files that control which commands run without asking, which
  hooks run, which plugins are on and which model starts."
- Line 107: "Permission rules allow, ask about or deny each kind of tool call. Hooks are
  commands Claude Code runs at set points, such as before a tool call. When something behaves
  oddly, run /status to see which settings files loaded."
- Line 113: Short "At startup, and again on save", Detail "Claude Code watches the files, so
  most edits apply without a restart."
- Line 114: Short "Override your organization", Detail "Nothing in your own files changes a
  managed setting."
- Line 118: "Claude Code enforces settings. An instructions file is guidance the model reads
  and doesn’t always follow."
- Line 122: "Most setup sits in two folders named .claude, one in your home folder and one in
  the project, with a few files beside them. Each group is named with the scope word the
  Claude Code docs use."
- Lines 124–146: replace the three tables with these four (keep a blank line between tables):

```
| User: you, in every project | Where |
|---|---|
| Instructions | ~/.claude/CLAUDE.md |
| Skills | ~/.claude/skills/ |
| MCP servers | ~/.claude.json, which Claude Code also uses for its own state |
| Plugins | enabledPlugins in ~/.claude/settings.json, with the files in ~/.claude/plugins/ |
| Settings | ~/.claude/settings.json |

| Project: shared through the repository | Where |
|---|---|
| Instructions | CLAUDE.md or .claude/CLAUDE.md, or AGENTS.md when there’s no CLAUDE.md |
| Skills | .claude/skills/ |
| MCP servers | .mcp.json at the project root |
| Plugins | enabledPlugins in .claude/settings.json |
| Settings | .claude/settings.json |

| Local: you, in this project only | Where |
|---|---|
| Instructions | CLAUDE.local.md |
| MCP servers | ~/.claude.json, under the project’s folder |
| Settings | .claude/settings.local.json, which also holds your local plugin choices |

| Managed: set by your organization | Where |
|---|---|
| Folder | /Library/Application Support/ClaudeCode/ on macOS, /etc/claude-code/ on Linux and WSL, C:\Program Files\ClaudeCode\ on Windows |
| Instructions | CLAUDE.md in that folder |
| Skills | .claude/skills/ in that folder |
| MCP servers | managed-mcp.json in that folder |
| Settings | managed-settings.json in that folder, or a policy from MDM or the claude.ai admin console |
```

- Line 148: "To check what loaded, run /status for settings, /context for instructions files, /mcp
  for servers and /plugin for plugins."
- Line 152: "When the same thing is set in more than one place, some kinds add up and for others
  one place wins."
- Lines 156–162, second cells:
  - Settings: "Highest first: managed, the --settings flag, local, project, user. Lists such as
    permission rules combine across files."
  - Permission rules: "Every rule from every file counts. Claude Code checks deny, then ask,
    then allow, so a deny rule anywhere blocks the call."
  - Hooks: "All of them run. A project hook doesn’t replace a user hook."
  - Instructions: "All of them load and none replaces another. The file closest to where you
    started is read last. A managed file can’t be excluded."
  - Skills: "Same name: managed, then user, then project. Plugin skills carry the plugin’s name
    in front, so they don’t clash."
  - MCP servers: "Same name: local, then project, then user, then plugins. The whole entry comes
    from one place, and a server your organization provides comes first."
  - Plugins: "Local, then project, then user."
- Line 164: "Managed settings sit above everything else, and nothing in your own files or on
  the command line changes them. Run /status to see which managed source applies."
- Line 168: "The other tools have the same kinds of setup under other names and in other
  places. Each has its own guide, as of October 2026."
- Lines 172–175, replace "TBD" with:
  - Claude Desktop: "Instructions, skills, connectors and plugins are set in the app. Local MCP
    servers go in claude_desktop_config.json."
  - GitHub Copilot CLI: "Instructions in .github/copilot-instructions.md or AGENTS.md, skills
    in .github/skills/, settings and MCP servers in ~/.copilot/."
  - Codex: "Instructions in AGENTS.md, skills in .agents/skills/, settings and MCP servers in
    ~/.codex/config.toml."
  - Visual Studio and VS Code: "Instructions in .github/copilot-instructions.md, skills in
    .github/skills/ in VS Code, MCP servers in a .mcp.json file."
- Line 177: "Two things carry over. Codex, GitHub Copilot CLI and VS Code read AGENTS.md, and
  Claude Code reads it when there’s no CLAUDE.md. GitHub Copilot CLI and VS Code also read
  skills from .claude/skills/."
- Lines 185–194, the sources table: drop "Anthropic, " from every name (so "Claude Code:
  Settings"), drop the row for "Claude Code: Plugins" (keep "Install plugins"), and add these
  rows at the end, in this form:
  - "Model Context Protocol: Connect to local MCP servers | October 2026 |
    modelcontextprotocol.io/docs/develop/connect-local-servers"
  - "GitHub Docs: Copilot CLI configuration directory | October 2026 |
    docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference"
  - "OpenAI: Codex config basics | October 2026 | learn.chatgpt.com/docs/config-file/config-basic"
  - "VS Code Docs: Agent skills | October 2026 |
    code.visualstudio.com/docs/copilot/customization/agent-skills"

When you're done, reply with one line: `wc -w guide.md`.
