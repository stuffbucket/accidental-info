# Sources for An Accidental Guide to: Claude Code

All pages fetched 22 October 2026. Excerpts are verbatim. Only official Claude Code docs
(code.claude.com) are used for Claude Code facts.

## Settings files and precedence

https://code.claude.com/docs/en/settings

- Scopes table: "User | `~/.claude/settings.json` | You, in every project on this machine"; "Shared
  project | `.claude/settings.json` | Everyone working in the folder that contains it. In a git
  repository, commit it so teammates get it"; "Project local | `.claude/settings.local.json` | You,
  in this one project only"; "Managed | `managed-settings.json` and other managed sources |
  Everyone your organization deploys it to".
- "Installing Claude Code doesn't create any settings file."
- "Claude Code also keeps a fifth file, `~/.claude.json`, that it writes for itself; you don't need
  to edit it. It holds your account details, MCP server configurations, per-project state such as
  trust decisions, and the global config keys that `/config` writes for you."
- "On Windows, `~/.claude` means `%USERPROFILE%\.claude`."
- Precedence: "Settings precedence, highest first: managed settings, command line, project local,
  shared project, user. A key set at a higher level overrides the same key set lower down."
- "Command line: JSON you pass with `--settings <file-or-json>` when you start `claude`, for that
  session only"
- "When you set the same list key, such as `permissions.allow`, in more than one file, Claude Code
  combines the lists instead of picking one"
- "Claude Code watches your settings files and reloads them when they change, so it applies most
  edits to the running session without a restart, including edits to `permissions`, `hooks`"
- "Run `/status` inside Claude Code to see which settings sources are active. The Status tab
  includes a `Setting sources` line"
- "Settings files are strict JSON: a `//` comment or a trailing comma is a syntax error"
- "`permissions.allow` rules, `permissions.additionalDirectories`, `extraKnownMarketplaces`, and
  most `env` values apply only after each teammate trusts the folder."

## Managed settings

https://code.claude.com/docs/en/managed-settings

- "macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`"; "Linux and WSL:
  `/etc/claude-code/managed-settings.json`"; "Windows: `C:\Program Files\ClaudeCode\managed-settings.json`"
- "File-based: `managed-settings.json`, an optional `managed-settings.d/` directory, and
  `managed-mcp.json` in the system directory: `/Library/Application Support/ClaudeCode/` on macOS,
  `/etc/claude-code/` on Linux and WSL, and `C:\Program Files\ClaudeCode\` on Windows."
- "macOS configuration profile: the `com.anthropic.claudecode` managed preferences domain."
- "Windows HKLM registry: the JSON as a `REG_SZ` or `REG_EXPAND_SZ` value named `Settings` under
  `HKLM\SOFTWARE\Policies\ClaudeCode`."
- Sources order: server-managed (claude.ai admin console), MDM or OS-level policies, managed
  settings files, HKCU registry. "`"first-wins"`, the default: Claude Code uses the
  highest-ranked source that delivers at least one policy key and ignores the rest"

## CLAUDE.md, rules and AGENTS.md

https://code.claude.com/docs/en/memory

- Managed policy CLAUDE.md: "macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md` • Linux and
  WSL: `/etc/claude-code/CLAUDE.md` • Windows: `C:\Program Files\ClaudeCode\CLAUDE.md`"
- "User instructions | `~/.claude/CLAUDE.md` | Personal preferences for all projects"
- "Project instructions | `./CLAUDE.md` or `./.claude/CLAUDE.md`"
- "Local instructions | `./CLAUDE.local.md` | Personal project-specific preferences; add to
  `.gitignore`"
- "Claude Code loads `CLAUDE.md` and `CLAUDE.local.md` from your current working directory and every
  directory above it."
- "All discovered files are concatenated into context rather than overriding each other."
- "instructions closer to where you launched Claude are read last"
- "Files in subdirectories load on demand."
- "Claude treats them as context, not enforced configuration. To block an action regardless of what
  Claude decides, use a PreToolUse hook instead."
- "Personal rules in `~/.claude/rules/` apply to every project on your machine."
- AGENTS.md: "By default, Claude reads `AGENTS.md` only when you have no `CLAUDE.md` in your working
  directory or above it."; "An `AGENTS.md` and a `CLAUDE.md` or `CLAUDE.local.md` in your working
  directory or above it | Your `CLAUDE.md` files only"; "Reading `AGENTS.md` directly requires Claude
  Code v2.1.277 or later."
- "Developers can exclude other CLAUDE.md files with the `claudeMdExcludes` setting, but not this
  one." (the managed CLAUDE.md)
- "Run `/init` to generate a starting CLAUDE.md automatically."; "run `/context` in a session and
  check the list under Memory files"
- Auto memory: "Each project gets its own memory directory at `~/.claude/projects/<project>/memory/`."

## The .claude directory

https://code.claude.com/docs/en/claude-directory

- "Claude Code reads instructions, settings, skills, subagents, and memory from your project
  directory and from `~/.claude` in your home directory. Commit project files to git to share them
  with your team"
- "Most users only edit `CLAUDE.md` and `settings.json`."
- "Connect external tools over MCP | `.mcp.json` | project only"
- "Installed plugins | `~/.claude/plugins` | Cloned marketplaces, installed plugin versions, the
  `installed_plugins.json` install record, and per-plugin data"
- "`agents/*.md` | Project and global | Subagent definitions with their own prompt and tools"

## Skills

https://code.claude.com/docs/en/skills

- "Enterprise | `.claude/skills/<skill-name>/SKILL.md` in the managed settings directory"
- "Personal | `~/.claude/skills/<skill-name>/SKILL.md` | All your projects on this machine"
- "Project | `.claude/skills/<skill-name>/SKILL.md` | Sessions in this repository ... Commit it so
  your team gets it too"
- "Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | Wherever the plugin is enabled, as
  `/plugin-name:skill-name`"
- "Two of enterprise, personal, and project | Enterprise over personal, and personal over project."
- "A plugin skill and a skill at any of the locations above | Both load, because plugin skills are
  namespaced"
- "Custom commands have been merged into skills. A file at `.claude/commands/deploy.md` and a skill
  at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way."
- "A skill and a file in `.claude/commands/` | The skill"

## MCP

https://code.claude.com/docs/en/mcp

- "Local | Current project only | No | `~/.claude.json`"; "Project | Current project only | Yes, via
  version control | `.mcp.json` in project root"; "User | All your projects | No | `~/.claude.json`"
- "Local scope is the default."
- "When the same server is defined in more than one place, Claude Code connects to it once, using
  the definition from the highest-precedence source. The entire server entry from that source is
  used; fields are not merged across scopes. 1. Local scope 2. Project scope 3. User scope
  4. Plugin-provided servers 5. claude.ai connectors"
- "A server your organization provides through the `managedMcpServers` managed setting ranks above
  all of these"
- "Claude Code prompts for approval in interactive sessions before using project-scoped servers from
  `.mcp.json` files."
- "claude mcp add --transport http shared-server --scope project https://example.com/mcp"

## Plugins and marketplaces

https://code.claude.com/docs/en/plugins

- "A Claude Code plugin is a directory of skills, agents, hooks, MCP servers, or other components
  that Claude Code installs and loads as one unit. Most plugins come from a marketplace, which is a
  catalog that lists plugins and where to fetch each one."
- "The manifest, a JSON file at `.claude-plugin/plugin.json`"
- "A marketplace is a repository or directory with a `.claude-plugin/marketplace.json` file"
- "Claude Code adds Anthropic's official marketplace the first time you start an interactive
  terminal session"
- "An enabled plugin is part of every session, not only the sessions where you use it."
- "what the plugin runs, it runs as you."

https://code.claude.com/docs/en/plugins/install (also served at /docs/en/discover-plugins)

- "User scope: ... The entry goes in `enabledPlugins` in `~/.claude/settings.json`."
- "Project scope: ... The entry goes in `.claude/settings.json`, which you commit. Committing that
  entry turns the plugin on for your collaborators but doesn't download it to their machines"
- "Local scope: ... The entry goes in `.claude/settings.local.json`."
- "When the same plugin is set at several scopes, the local setting overrides the project setting,
  and the project setting overrides the user setting."
- "/plugin install commit-commands@claude-plugins-official"
- "/plugin marketplace add anthropics/claude-code"
- "The tab can also show plugins at Managed scope. Your organization installed those through managed
  settings"

## Permissions

https://code.claude.com/docs/en/permissions

- "Rules are evaluated in order: deny, then ask, then allow. The first match in that order
  determines the outcome"
- "if user settings allow a permission and project settings deny it, the deny rule blocks it. The
  reverse is also true"
- "`permissions.allow` rules ... in a project's `.claude/settings.json` grant capability, so Claude
  Code applies them only after you accept the workspace trust dialog"

## Hooks

https://code.claude.com/docs/en/hooks

- "Hooks are user-defined shell commands, HTTP endpoints, MCP tool calls, LLM prompts, or subagents
  that execute automatically at specific points in Claude Code's lifecycle."
- Locations: `~/.claude/settings.json`, `.claude/settings.json`, `.claude/settings.local.json`,
  "Managed policy settings", "Plugin `hooks/hooks.json`", "Skill frontmatter", "Subagent frontmatter"
- "Hook entries merge across settings levels rather than replacing each other"

## The sibling tools (for the "same things in other tools" table only)

Checked 22 October 2026 on each product's official docs.

- Claude Desktop, https://modelcontextprotocol.io/docs/develop/connect-local-servers:
  `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS),
  `%APPDATA%\Claude\claude_desktop_config.json` (Windows); "Click the "Edit Config" button".
  Instructions, skills, connectors and plugins are set in the app (support.claude.com articles
  10185728, 12512180, 11176164, 13837440): "Navigate to Customize > Skills."
- GitHub Copilot CLI,
  https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference:
  `~/.copilot/settings.json` "This is the primary configuration file for Copilot CLI.";
  `~/.copilot/mcp-config.json`; "Project-level MCP configurations (in `.mcp.json` or
  `.github/mcp.json`) take precedence". Skills,
  https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-skills:
  "specific to a single repository, create a `.github/skills`, `.claude/skills`, or
  `.agents/skills`". Instructions: `.github/copilot-instructions.md`, `AGENTS.md`.
- Codex, https://learn.chatgpt.com/docs/config-file/config-basic (developers.openai.com/codex
  redirects here): "Codex stores user-level configuration at `~/.codex/config.toml`." MCP:
  "Configure each MCP server with a `[mcp_servers.<server-name>]` table". Skills,
  https://learn.chatgpt.com/docs/build-skills: `.agents/skills`, `$HOME/.agents/skills`.
  Instructions, https://learn.chatgpt.com/docs/agent-configuration/agents-md: "it checks for
  `AGENTS.override.md`, then `AGENTS.md`".
- VS Code, https://code.visualstudio.com/docs/copilot/customization/custom-instructions:
  "use `.github/copilot-instructions.md` for project-wide guidance"; "Use an `AGENTS.md` file".
  Skills, https://code.visualstudio.com/docs/copilot/customization/agent-skills: `.github/skills/`,
  `.claude/skills/`, `.agents/skills/`. MCP: workspace-root `.mcp.json`.
- Visual Studio, https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers:
  "`<SOLUTIONDIR>\.mcp.json` Works well if you're looking for an MCP configuration that you can
  track in source control"; instructions in `.github/copilot-instructions.md`
  (https://learn.microsoft.com/en-us/visualstudio/ide/copilot-chat-context).
