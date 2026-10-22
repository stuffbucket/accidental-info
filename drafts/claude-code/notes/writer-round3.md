# Writer instructions, round 3: cut to five minutes, and fix the where page

Edit `guide.md` in the current folder in place. The guide prints about 1,700 words and must come
down toward 1,200, and the where page runs off the bottom. Apply each edit below by line number
(numbers refer to the file as it stands now). Use the replacement text as given; smooth a word
only if a sentence reads badly, and never make it longer. Keep every heading, id and table shape
except where an edit says otherwise. Don't change anything not listed. The format rules from
round 1 still hold.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

## Page 2

- Line 15: "Each kind can be yours alone, shared with the project, or set by your organization,
  and each lives in a different place. For what skills, tools and MCP servers are, see An
  Accidental Guide to: Agents, Harnesses, Skills, and Tools."
- Lines 19–23, the Meaning cells:
  - Instructions file: "Text added to every session, such as build commands."
  - Skill: "A written procedure, loaded when a task needs it."
  - MCP server: "A program that gives Claude Code tools for another system."
  - Plugin: "A package of skills, MCP servers and hooks, installed together."
  - Settings: "JSON files for permissions, hooks and other behavior."

## Entries

- Line 30: "An instructions file holds what Claude Code should know in every session, such as
  build commands and conventions. AGENTS.md is read only when there’s no CLAUDE.md."
- Line 31: "Write down what you’d otherwise explain again each session. Run /init to start a
  CLAUDE.md."
- Line 37 Detail: "Files from your working folder and every folder above it combine."
- Line 38 Detail: "To block an action, use a deny rule or a hook in settings."
- Line 42: "Instructions are guidance the model reads. Settings are rules Claude Code enforces."
- Line 48: "A folder with a SKILL.md file."
- Line 49: "A skill is a written procedure that Claude Code loads when a task needs it. You can
  also run one by name, such as /deploy."
- Line 57 Detail: "A skill that reads a database still needs a tool that reaches it."
- Line 67: "An entry under mcpServers, with a start command or a URL."
- Line 68: "An MCP server is a separate program that gives Claude Code tools for another
  system. Add one with claude mcp add."
- Line 75 Detail: "Claude Code connects and gets the server’s list of tools."
- Line 80: "A plugin can bring its own MCP server. You add or remove that server along with the
  plugin."
- Line 86: "A folder with .claude-plugin/plugin.json."
- Line 87: "A plugin packages skills, agent definitions, hooks and MCP servers to install as one
  unit. Most come from a marketplace, a catalog you add once with /plugin marketplace add."
- Line 88: "An enabled plugin is part of every session, and what it runs, it runs as you.
  Check what a plugin adds before you install it."
- Line 94 Detail: "An enabledPlugins entry in a settings file turns it on."
- Line 99: "A skill is one folder you can copy in yourself. A plugin is a package, usually from
  a marketplace, that can carry many skills and other parts."
- Line 106: "Settings are JSON files that control which commands run without asking, which
  hooks run and which plugins are on."
- Line 107: "Permission rules allow, ask about or deny tool calls. Hooks are commands Claude
  Code runs at set points, such as before a tool call."
- Line 113 Detail: "Claude Code watches the files, so most edits apply right away."
- Line 118: "Claude Code enforces settings. The model reads an instructions file as guidance."

## Where do the files live?

- Line 122: "Most setup sits in two .claude/ folders, one in your home folder and one in the
  project. The group names are the scope names the Claude Code docs use."
- Lines 124–152: replace the four tables with these three (blank line between tables):

```
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
```

- Line 154: "/status shows which settings files loaded, /context the instructions files, /mcp the
  servers and /plugin the plugins."

## Which one wins?

- Line 158: "Some kinds add up across places. For others, one place wins."
- Lines 162–168, second cells:
  - Settings: "Highest first: managed, the --settings flag, local, project, user. Lists such as
    permission rules combine."
  - Permission rules: "All rules count. Deny is checked first, then ask, then allow, so a deny
    anywhere blocks the call."
  - Hooks: "All of them run."
  - Instructions: "All of them load. The file closest to where you started is read last."
  - Skills: "Same name: managed, then user, then project. Plugin skills carry the plugin’s
    name, so they don’t clash."
  - MCP servers: "Same name: local, then project, then user, then plugins. The whole entry
    comes from one place."
  - Plugins: leave as is.
- Line 170: "Nothing in your own files or on the command line changes a managed setting. Run
  /status to see which managed source applies."

## The same things in other tools

- Line 174: "Each of these tools has its own guide. The paths are as of October 2026."
- Lines 178–181, second cells:
  - Claude Desktop: "Most setup is in the app’s settings. Local MCP servers go in
    claude_desktop_config.json."
  - GitHub Copilot CLI: "AGENTS.md or .github/copilot-instructions.md, .github/skills/, and
    ~/.copilot/ for settings and MCP servers."
  - Codex: "AGENTS.md, .agents/skills/, and ~/.codex/config.toml for settings and MCP servers."
  - Visual Studio and VS Code: ".github/copilot-instructions.md, .github/skills/ in VS Code,
    and a .mcp.json file for MCP servers."
- Line 183: "Codex, GitHub Copilot CLI and VS Code read AGENTS.md, and Claude Code reads it
  when there’s no CLAUDE.md. GitHub Copilot CLI and VS Code also read .claude/skills/."

## Sources

- Line 187: "Checked in October 2026. Claude Code changes often, so check the current docs
  before you rely on a path."
- Lines 200–203, the names only: "MCP: Connect to local servers", "GitHub: Copilot CLI
  configuration", "OpenAI: Codex configuration", "VS Code: Agent skills".

When you're done, reply with one line: `wc -w guide.md`.
