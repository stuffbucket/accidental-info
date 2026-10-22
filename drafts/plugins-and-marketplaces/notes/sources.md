# Sources: Plugins, Connectors, and Marketplaces

Notes for An Accidental Guide to… Plugins, Connectors, and Marketplaces. Every page below was fetched on 22 October 2026 from public, official documentation. Each entry gives a plain summary, the URL, a short verbatim excerpt and the page title and publisher.

## Research notes: plugin, marketplace, connector and related words in Claude products

Fetched 2026-10-22 with WebFetch. Every excerpt below is quoted from the page as fetched that day. Publishers: code.claude.com is "Claude Code Docs" (Anthropic); claude.com/docs is "Claude docs" (Anthropic); support.claude.com is the "Claude Help Center" (Anthropic); claude.com/blog and claude.com/marketplace are Anthropic marketing pages.

Note on URLs: some Claude Code URLs serve a page under a newer path. Where that happened, the URL fetched is given first and the page's own path second.

---

### Product 1: Claude Code

### plugin

A plugin is a directory of components (skills, agents, hooks, MCP servers and more) that Claude Code installs and loads as one unit.

- https://code.claude.com/docs/en/plugins (page path: /docs/en/plugins/overview)
- "A Claude Code plugin is a directory of skills, agents, hooks, MCP servers, or other components that Claude Code installs and loads as one unit. Most plugins come from a marketplace, which is a catalog that lists plugins and where to fetch each one."
- Plugins overview, Claude Code Docs (Anthropic)

The glossary gives a shorter list than the manifest reference does.

- https://code.claude.com/docs/en/glossary
- "A bundle of skills, hooks, subagents, and MCP servers packaged as a single installable unit. Plugin skills are namespaced as `plugin-name:skill-name` so multiple plugins coexist."
- Glossary, Claude Code Docs (Anthropic)

The same word also names the JetBrains IDE plugin, which is a different thing.

- https://code.claude.com/docs/en/plugins (page path: /docs/en/plugins/overview)
- "**You want Claude Code inside VS Code or a JetBrains IDE**: that's the VS Code extension or the JetBrains plugin, not a Claude Code plugin."
- Plugins overview, Claude Code Docs (Anthropic)

A plugin with a JavaScript hooks module is called a "mod".

- https://code.claude.com/docs/en/plugins (page path: /docs/en/plugins/overview)
- "**A hooks module**: hooks written as JavaScript functions, which can also draw panes and add commands. A plugin that has one is called a mod."
- Plugins overview, Claude Code Docs (Anthropic)

### What a Claude Code plugin can contain

Default layout: manifest, skills, commands, agents, hooks, MCP servers, LSP servers, output styles, workflows, themes, monitors, `bin/` executables and `settings.json`. Channels are declared in the manifest. Only `name` is required in the manifest, and the manifest itself is optional.

- https://code.claude.com/docs/en/plugins-reference (page path: /docs/en/plugins/manifest-reference)
- "Save the manifest at `.claude-plugin/plugin.json` under the plugin root. Put every other plugin file at the plugin root, not inside `.claude-plugin/`. That includes `skills/`, `commands/`, and `hooks/`."
- Standard layout table rows (verbatim): "Skills | `skills/` | One `<name>/SKILL.md` per skill" ... "Commands | `commands/` | Flat Markdown command files. Prefer `skills/` for new plugins" ... "Agents | `agents/` | Agent Markdown files" ... "Hooks | `hooks/hooks.json` | Hook configuration" ... "MCP servers | `.mcp.json` | MCP server definitions" ... "LSP servers | `.lsp.json` | LSP server configurations" ... "Output styles | `output-styles/` | Output style Markdown files" ... "Workflows | `workflows/` | Workflow `.js` files" ... "Themes | `themes/` | Theme JSON files" ... "Monitors | `monitors/monitors.json` | The monitors array" ... "Executables | `bin/` | Files here are on the Bash tool's `PATH` while the plugin is enabled" ... "Settings | `settings.json` | `agent` and `subagentStatusLine` defaults applied while the plugin is enabled"
- Plugin manifest reference, Claude Code Docs (Anthropic)

A plugin can ship a packaged MCPB (desktop extension format) server.

- https://code.claude.com/docs/en/plugins/components
- "The `mcpServers` key also accepts a packaged server as an [MCPB file](https://github.com/modelcontextprotocol/mcpb), whose extension is `.mcpb` or the older `.dxt`."
- Add components to a plugin, Claude Code Docs (Anthropic)

A `CLAUDE.md` inside a plugin is not loaded.

- https://code.claude.com/docs/en/plugins-reference (page path: /docs/en/plugins/manifest-reference)
- "A `CLAUDE.md` at the plugin root isn't loaded as context, and `claude plugin validate` warns when it finds one. To include instructions that load into Claude's context, put them in a skill."
- Plugin manifest reference, Claude Code Docs (Anthropic)

### plugin marketplace / marketplace

A marketplace is a git repo or directory with `.claude-plugin/marketplace.json` that lists plugins and where to fetch each. It is a catalog, not a store.

- https://code.claude.com/docs/en/plugins (page path: /docs/en/plugins/overview)
- "A marketplace is a repository or directory with a `.claude-plugin/marketplace.json` file that lists plugins and where to fetch each one. It's a catalog, not a hosted store."
- Plugins overview, Claude Code Docs (Anthropic)

The website called Claude Marketplace is a different thing.

- https://code.claude.com/docs/en/plugins (page path: /docs/en/plugins/overview)
- "A plugin marketplace isn't [Claude Marketplace](https://claude.com/marketplace). Claude Marketplace is the website at claude.com/marketplace where you browse plugins, connectors, partner products, and service partners. It isn't a marketplace you add with `/plugin marketplace add`."
- Plugins overview, Claude Code Docs (Anthropic)

marketplace.json requires `name`, `owner` and `plugins`; each entry needs `name` and `source`.

- https://code.claude.com/docs/en/plugin-marketplaces (page path: /docs/en/plugins/create-marketplace)
- "Save `marketplace.json` at `my-marketplace/.claude-plugin/marketplace.json`. The file requires a `name`, an `owner`, and a `plugins` array. Each object in `plugins` is a plugin entry and needs a `name` and a `source`."
- Create a marketplace, Claude Code Docs (Anthropic)

Plugin sources: relative path, `github`, `git-subdir`, `url`, `archive`, `npm`, `command`.

- https://code.claude.com/docs/en/plugin-marketplaces (page path: /docs/en/plugins/create-marketplace)
- "A plugin can also come from one of these source types: `url`: a git repository by URL, on any host; `archive`: a zip file downloaded over HTTPS; `npm`: an npm package; `command`: a directory produced by running a command on the machine where the plugin is installed"
- Create a marketplace, Claude Code Docs (Anthropic)

`/plugin marketplace add` takes a GitHub repo, any git URL, a local path, or a hosted marketplace.json URL.

- https://code.claude.com/docs/en/discover-plugins (page path: /docs/en/plugins/install)
- "In a Claude Code session, run `/plugin marketplace add` followed by the marketplace's source: a GitHub repository, a git repository on any host, a local directory or file, or a hosted `marketplace.json`."
- Install and manage plugins, Claude Code Docs (Anthropic)

Install ID is `plugin@marketplace`.

- https://code.claude.com/docs/en/plugin-marketplaces (page path: /docs/en/plugins/create-marketplace)
- "Install the plugin. The install id is the entry's `name`, an `@`, and the marketplace `name`."
- Create a marketplace, Claude Code Docs (Anthropic)

The official Anthropic marketplace is `claude-plugins-official`. Claude Code adds it on its own; community (`claude-community`) and demo (`claude-code-plugins`) marketplaces you add yourself.

- https://code.claude.com/docs/en/plugins/anthropic-marketplaces
- "Anthropic publishes three general-purpose plugin marketplaces for Claude Code: official, community, and demo. Each is a catalog of plugins in its own GitHub repository."
- Table row (verbatim): "How you get it | Claude Code adds it the first time you start an interactive terminal session, unless a managed policy or `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL` blocks it"
- "The community marketplace's name is `claude-community`, not its repository name."
- Anthropic's marketplaces, Claude Code Docs (Anthropic)

Anthropic's "directory" is a separate catalog on claude.ai; its plugins reach Claude Code by account sync.

- https://code.claude.com/docs/en/plugins/anthropic-marketplaces
- "Anthropic's directory is separate from these marketplaces. The directory is the catalog on claude.ai. A plugin you add from the directory on claude.ai reaches Claude Code through account sync."
- Anthropic's marketplaces, Claude Code Docs (Anthropic)

Plugins from a claude.ai account sync into Claude Code as `<name>@synced`; it does not go the other way.

- https://code.claude.com/docs/en/discover-plugins (page path: /docs/en/plugins/install)
- "**Where you see them**: in `/plugin` and `claude plugin list` under the ID `<name>@synced`." ... "**What doesn't go the other way**: plugins you install with `/plugin` or `claude plugin install` stay on this machine and aren't added to your claude.ai account."
- Install and manage plugins, Claude Code Docs (Anthropic)

Cloud sessions (claude.ai/code) do not load your locally installed plugins.

- https://code.claude.com/docs/en/discover-plugins (page path: /docs/en/plugins/install)
- "A cloud session, including the browser at claude.ai/code, has no plugin browser and doesn't load the plugins you installed on your own machine or the ones your repository's `.claude/settings.json` turns on."
- Install and manage plugins, Claude Code Docs (Anthropic)

### connector

In Claude Code, a connector is an MCP server added to your claude.ai account (not configured in Claude Code). It shows up in `/mcp`.

- https://code.claude.com/docs/en/glossary
- "An MCP server added to your claude.ai account rather than configured in Claude Code. When you sign in to Claude Code with that account, your connectors appear in `/mcp` alongside the servers you added locally."
- Glossary, Claude Code Docs (Anthropic)

- https://code.claude.com/docs/en/mcp
- "If you've logged into Claude Code with a claude.ai account, MCP servers you've added in claude.ai, known as connectors, are automatically available in Claude Code"
- Connect Claude Code to tools via MCP, Claude Code Docs (Anthropic)

Desktop extensions are not defined in the Claude Code docs; the glossary sends you to the Help Center.

- https://code.claude.com/docs/en/glossary
- "For Claude Desktop terms such as desktop extension, MCPB, and DXT, see the Claude Help Center."
- Glossary, Claude Code Docs (Anthropic)

### extension

Used in three ways: (a) the VS Code extension, which is the Claude Code UI inside VS Code; (b) the Chrome extension, an "integration"; (c) a general word for all the ways to extend Claude Code (CLAUDE.md, skills, MCP, hooks, plugins...).

- https://code.claude.com/docs/en/vs-code
- "The VS Code extension provides a native graphical interface for Claude Code, integrated directly into your IDE. This is the recommended way to use Claude Code in VS Code."
- Use Claude Code in VS Code, Claude Code Docs (Anthropic)

The VS Code extension can itself install Claude Code plugins.

- https://code.claude.com/docs/en/vs-code
- "The VS Code extension includes a graphical interface for installing and managing plugins. Type `/plugins` in the prompt box to open the **Manage plugins** interface."
- Use Claude Code in VS Code, Claude Code Docs (Anthropic)

- https://code.claude.com/docs/en/glossary (entry "Surface")
- "Slack and the Chrome extension are integrations that connect to a surface rather than surfaces themselves."
- Glossary, Claude Code Docs (Anthropic)

- https://code.claude.com/docs/en/features-overview
- "This guide covers the extension layer: features you add to customize what Claude knows, connect it to external services, and automate workflows." ... "Extensions plug into different parts of the agentic loop"
- Extend Claude Code, Claude Code Docs (Anthropic)

### MCP server

A program that gives Claude tools, prompts or resources over MCP. Added with `claude mcp add`, `.mcp.json`, a plugin, or as a claude.ai connector.

- https://code.claude.com/docs/en/glossary
- "A program that gives Claude tools, prompts, or resources over MCP. You add servers with `claude mcp add`, in `.mcp.json`, through a plugin, or as a claude.ai connector."
- Glossary, Claude Code Docs (Anthropic)

Scopes: local (default, `~/.claude.json`), project (`.mcp.json`), user (`~/.claude.json`), then plugin servers, then claude.ai connectors in precedence.

- https://code.claude.com/docs/en/mcp
- "MCP servers can be configured at three scopes. The scope you choose controls which projects the server loads in and whether the configuration is shared with your team."
- Connect Claude Code to tools via MCP, Claude Code Docs (Anthropic)

Claude Code can import MCP servers configured in Claude Desktop.

- https://code.claude.com/docs/en/mcp
- "If you've already configured MCP servers in Claude Desktop, you can import them"
- Connect Claude Code to tools via MCP, Claude Code Docs (Anthropic)

### skill

A `SKILL.md` file of instructions Claude loads when relevant or that you run with `/name`. Follows the Agent Skills open standard.

- https://code.claude.com/docs/en/skills
- "Skills extend what Claude can do. Create a `SKILL.md` file with instructions, and Claude adds it to its toolkit. Claude uses skills when relevant, or you can invoke one directly with `/skill-name`."
- "Claude Code skills follow the Agent Skills open standard, which works across multiple AI tools. Claude Code extends the standard with additional features like invocation control, subagent execution, and dynamic context injection."
- Extend Claude with skills, Claude Code Docs (Anthropic)

Skills enabled on a claude.ai account sync into Claude Code terminal sessions.

- https://code.claude.com/docs/en/skills
- "In your terminal, Claude Code syncs those skills in sessions where you sign in with your claude.ai account."
- Extend Claude with skills, Claude Code Docs (Anthropic)

### sub-agent / custom agent

"Subagent" is the term. Markdown files in `.claude/agents/` or a plugin's `agents/`. Separate from "agent teams" (several sessions).

- https://code.claude.com/docs/en/sub-agents
- "Subagents are specialized AI assistants that handle specific types of tasks." ... "Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions."
- Create custom subagents, Claude Code Docs (Anthropic)

- https://code.claude.com/docs/en/glossary (entry "Agent teams")
- "Multiple independent Claude Code sessions coordinated by a team lead, with a shared task list and peer-to-peer messaging. Unlike subagents, which run within a single session and report only to the parent, teammates each have their own context window"
- Glossary, Claude Code Docs (Anthropic)

### hook

A handler Claude Code runs at a fixed lifecycle point: shell command, HTTP request, MCP tool, prompt, or agent. Deterministic.

- https://code.claude.com/docs/en/glossary
- "A user-defined handler that executes automatically at a specific point in Claude Code's lifecycle, such as before a tool runs, after a file edit, or at session start. Handlers can be a shell command, HTTP endpoint, MCP tool, LLM prompt, or subagent."
- Glossary, Claude Code Docs (Anthropic)

- https://code.claude.com/docs/en/hooks-guide
- "Most hooks use `"type": "command"`, which runs a shell command. Four other types are available"
- Automate actions with hooks, Claude Code Docs (Anthropic)

### slash command / custom commands

"Slash commands" are now just "commands". Custom commands were merged into skills; `.claude/commands/` files still work.

- https://code.claude.com/docs/en/skills
- "**Custom commands have been merged into skills.** A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way. Your existing `.claude/commands/` files keep working."
- Extend Claude with skills, Claude Code Docs (Anthropic)

- https://code.claude.com/docs/en/glossary (Deprecated and renamed terms table)
- "Custom commands | Skills | `.claude/commands/` files still work" ... "Slash commands | Commands | \"Slash\" dropped from product copy"
- Glossary, Claude Code Docs (Anthropic)

"Command" has two unrelated meanings as well.

- https://code.claude.com/docs/en/glossary (entry "Command")
- "Two other uses of the word are unrelated: `claude` CLI subcommands such as `claude mcp add`, listed in the CLI reference, and the `command` field of a stdio MCP server entry"
- Glossary, Claude Code Docs (Anthropic)

In plugins, commands are the older format.

- https://code.claude.com/docs/en/plugins/components
- "Commands are the older format, and skills supersede them for new work. A skill runs by name the same way, and it can also carry supporting files in its directory."
- Add components to a plugin, Claude Code Docs (Anthropic)

### instructions file

CLAUDE.md (managed, user `~/.claude/CLAUDE.md`, project `./CLAUDE.md` or `./.claude/CLAUDE.md`, local `./CLAUDE.local.md`), plus `.claude/rules/`. Claude Code also reads `AGENTS.md` when there is no CLAUDE.md.

- https://code.claude.com/docs/en/memory
- "CLAUDE.md files are markdown files that give Claude persistent instructions for a project, your personal workflow, or your entire organization. You write these files in plain text; Claude reads them at the start of every session."
- How Claude remembers your project, Claude Code Docs (Anthropic)

- https://code.claude.com/docs/en/glossary (entry "AGENTS.md")
- "A markdown file of project instructions you write for AI coding agents. If your repository has one and no CLAUDE.md, Claude reads it as your project instructions without you adding a second file."
- Glossary, Claude Code Docs (Anthropic)

### app / integration

"Desktop app" is the Claude Desktop app's Code tab. "Integrations" is used loosely for MCP-connected services and for Slack/Chrome. No Claude Code feature is named "apps" or "integrations".

- https://code.claude.com/docs/en/glossary (entry "MCP")
- "MCP servers give Claude new tools for Slack, Jira, databases, browsers, and hundreds of other integrations."
- Glossary, Claude Code Docs (Anthropic)

---

### Product 2: Claude Desktop app and claude.ai (chat, Cowork)

### plugin

Yes, claude.ai and Claude Desktop support plugins, in the same folder format as Claude Code. Added at Customize > Plugins; saved to your account; also load in Cowork and sync to Claude Code.

- https://claude.com/docs/plugins/overview
- "A plugin packages skills, MCP connectors, and commands and agents so you can add them to Claude as one unit. You add plugins from **Customize > Plugins** in claude.ai or the Claude desktop app; **Customize** is the page that holds your connectors, skills, and plugins."
- Plugins, Claude docs (Anthropic)

Each surface loads a different subset. Chat: skills, commands (as skills), remote MCP. Cowork adds agents, hooks, local MCP. Only Claude Code loads LSP, output styles, themes, settings, `bin/`.

- https://claude.com/docs/plugins/platform-support
- "You can install the same plugin folder everywhere you use Claude, but chat, Cowork, and Claude Code each load a different subset of what the folder can contain."
- Table rows (verbatim): "Agents (`agents/*.md`) | Ignored | Loads | Loads" ... "Hooks (`hooks/hooks.json`) | Ignored | Loads | Loads" ... "Executables in a top-level `bin/` directory | Can't be installed | Can't be installed | Loads" ... "LSP servers, output styles, themes, `settings` | Ignored | Ignored | Loads"
- Plugin feature support across platforms, Claude docs (Anthropic)

### plugin marketplace / marketplace / directory

On claude.ai you add plugins from Discover (Anthropic's default marketplaces, the directory, your org), Add marketplace (a Git repo), or Upload plugin (.zip or .plugin).

- https://claude.com/docs/plugins/overview
- "On the **Plugins** page, you add a plugin from **Discover**, **Add > Add marketplace**, or **Add > Upload plugin**"
- "**Add > Add marketplace**: add a plugin marketplace, a Git repository that contains plugins, so its plugins appear alongside the others."
- Plugins, Claude docs (Anthropic)

Directory plugins are reviewed by Anthropic; marketplace-URL and uploaded plugins are not.

- https://claude.com/docs/plugins/overview
- "Anthropic reviews plugins listed in the directory: every version gets automated validation and a security scan, and a person reviews a new listing before it goes live ... That review doesn't cover a plugin you add from a marketplace URL or upload yourself"
- Plugins, Claude docs (Anthropic)

Claude Marketplace (website) lists connectors, plugins, partner "agents and products", and service partners.

- https://claude.com/marketplace
- "Claude Marketplace is now one place to find plugins, agents, and more" ... "Purchase Claude-powered software from our partners."
- Claude Marketplace | Claude by Anthropic (Anthropic)

### connector

A connector links Claude to an outside app or service. Each is a connection to an MCP server. Remote connectors work everywhere; a local connector is a desktop extension.

- https://claude.com/docs/extend/overview
- "MCP connectors connect Claude to an external service ... Each one is a connection to an MCP server, which the service runs so Claude can reach it. In Claude's settings, connectors appear under **Connectors**"
- Connectors, skills, and plugins, Claude docs (Anthropic)

- https://claude.com/docs/connectors
- "Most connectors are remote services that you sign in to, as the steps on this page describe. A local connector is a desktop extension, packaged as an MCP Bundle (MCPB), that runs on your computer in the Claude desktop app."
- Get started with connectors, Claude docs (Anthropic)

A custom connector is a remote MCP server added by URL; it is reached from Anthropic's cloud, not your machine.

- https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
- "Custom connectors (remote MCP servers) are reached from Anthropic's cloud infrastructure, not from your local machine."
- Use connectors to extend Claude's capabilities, Claude Help Center (Anthropic)

"MCP Connector" is also an API feature name.

- https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
- "Connectors work across Claude, Claude Desktop, Claude Code, and the API (via the MCP Connector)."
- Use connectors to extend Claude's capabilities, Claude Help Center (Anthropic)

Connectors Directory: one catalog of MCP servers for all Claude products.

- https://claude.com/docs/connectors/directory
- "The Connectors Directory is a catalog of MCP servers that work across all Claude products: claude.ai, Claude Desktop, Claude Mobile, Claude Code, and Cowork."
- Connectors directory, Claude docs (Anthropic)

### desktop extension / .mcpb / .dxt / Settings > Extensions

A desktop extension is a local MCP server packaged with MCPB, installed in Claude Desktop under Settings > Extensions. It is also called a "local connector". The `.dxt` extension is the older name for `.mcpb` (stated in the Claude Code docs; the Help Center page fetched mentions only `.mcpb`).

- https://claude.com/docs/connectors/custom/add-unlisted
- "A desktop extension is a local MCP server packaged with MCPB (MCP Bundles) that runs on your device inside Claude Desktop." ... "In the Claude desktop app, go to **Settings > Extensions**."
- Add a connector that isn't in the directory, Claude docs (Anthropic)

- https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop
- Desktop extensions offer "a streamlined way to install and manage local MCP servers through single-click installable packages" ... "Navigate to Settings > Extensions on Claude Desktop." ... "Click “Browse extensions” to view our directory and click on any Anthropic-reviewed tools you want to use."
- Getting Started with Local MCP Servers on Claude Desktop, Claude Help Center (Anthropic)

### extension

On this side, "extension" means a desktop extension. MCP Apps is also described as an "extension" to MCP.

- https://support.claude.com/en/articles/13454812-use-interactive-connectors-in-claude
- "MCP Apps is the open-source extension to the Model Context Protocol that powers interactive apps."
- Use interactive connectors in Claude, Claude Help Center (Anthropic)

### MCP server

The thing behind every connector. Directly configurable in Claude Desktop's `claude_desktop_config.json` (Settings > Developer > Edit Config).

- https://claude.com/docs/connectors/building/mcp-apps/getting-started
- "Go to **Settings > Developer** and click **Edit Config**." ... "Add one of these example servers to your `claude_desktop_config.json`"
- Get started with MCP Apps, Claude docs (Anthropic)

### app / integration / MCP Apps / interactive connectors

"Integrations" was the May 2025 launch name for remote MCP connections in claude.ai. The current docs and Help Center say "connectors". None of the pages fetched states the rename outright, and the old Help Center slug "building-custom-integrations-via-remote-mcp-servers" now returns 404.

- https://claude.com/blog/integrations (redirected from https://www.anthropic.com/news/integrations)
- "Today we're announcing Integrations, a new way to connect your apps and tools to Claude." (May 1, 2025)
- Claude can now connect to your world, Claude blog (Anthropic)

An MCP App is interactive UI an MCP server renders in the conversation. The Help Center calls connectors that use it "interactive connectors".

- https://claude.com/docs/connectors/building/mcp-apps/getting-started
- "An MCP App is interactive UI that your MCP server renders inside a Claude conversation, such as an interactive chart or map."
- Get started with MCP Apps, Claude docs (Anthropic)

- https://support.claude.com/en/articles/13454812-use-interactive-connectors-in-claude
- "Some connectors can now display live, interactive apps directly within your Claude conversations." ... "Interactive connectors are available for all users on Claude, Cowork, Claude Desktop, and Claude for iOS/Android."
- Use interactive connectors in Claude, Claude Help Center (Anthropic)

### skill

Same SKILL.md format (Agent Skills spec). Managed at Customize > Skills. Needs code execution turned on. Sources: Anthropic, partners, organization, custom.

- https://claude.com/docs/skills/overview
- "Skills are directories containing instructions, scripts, and resources that Claude dynamically loads to handle specific tasks. Each skill has a `SKILL.md` file that defines when it should be activated and what instructions Claude should follow."
- "Skills follow the Agent Skills specification, an open standard, so a skill you write for Claude also works in other tools that adopt the specification."
- Skills overview, Claude docs (Anthropic)

Only the Agent Skills spec frontmatter fields work in claude.ai uploads.

- https://code.claude.com/docs/en/skills
- "claude.ai skill uploads, the Skills API, and packaging with `package_skill.py` | `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`"
- Extend Claude with skills, Claude Code Docs (Anthropic)

### sub-agent / agent

Plugin "agents" load in Cowork and Claude Code, not in chat. Claude Marketplace uses "agents" for partner software products, a different meaning.

- https://claude.com/docs/plugins/overview
- "Agents | Specialists Claude can delegate part of a task to | Cowork, Claude Code"
- Plugins, Claude docs (Anthropic)

### hook

Ignored in chat, loaded in Cowork (from plugins only). No standalone hooks feature is documented for claude.ai.

- https://claude.com/docs/plugins/overview
- "**Agents and hooks**: run commands on your computer when certain events happen"
- Plugins, Claude docs (Anthropic)

### slash command / commands

Typing `/` in chat lists skills and plugin commands. In chat a command loads as a skill; in Cowork you run `/plugin-name:command`.

- https://claude.com/docs/plugins/overview
- "Commands | Named actions. In Cowork and Claude Code you run one by typing `/plugin-name:command`. In chat a command loads as a skill."
- Plugins, Claude docs (Anthropic)

### instructions file / Projects

No instructions file. Projects have "project instructions" and a knowledge base; account-wide "Instructions for Claude" also exist.

- https://support.claude.com/en/articles/9517075-what-are-projects
- "Projects allow you to create self-contained workspaces with their own chat histories and knowledge bases." ... "you can define project instructions for each project to further tailor Claude's responses."
- What are projects?, Claude Help Center (Anthropic)

- https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features
- "Instructions are account-wide settings that help Claude understand your general instructions" ... "Project instructions help Claude understand the specific context and requirements for a particular project."
- Understanding Claude's personalization features, Claude Help Center (Anthropic)

---

### Name collisions and disagreements

1. "Marketplace" names three things: a Claude Code plugin catalog (marketplace.json), the Claude Marketplace website, and claude.ai's "Add marketplace" (a Git repo). Anthropic's "directory" is separate again.
2. "Directory" names several catalogs: Anthropic's directory (plugins and connectors on claude.ai, also `/plugin directory` in Claude Code), the Connectors Directory, and the desktop extensions directory ("Browse extensions").
3. One thing, several names: a local MCP server packaged as `.mcpb` (older `.dxt`) is a "desktop extension", a "local connector", an "MCP Bundle", and lives under Settings > Extensions. A remote MCP server is a "connector", "MCP connector", "custom connector", "web connector", and was once an "integration".
4. "Plugin" also means the JetBrains IDE plugin, which is not a Claude Code plugin. "Extension" in Claude Code means the VS Code extension, the Chrome extension, or the general extension layer.
5. "Agent" means a subagent (Claude Code), a plugin agent (claude.ai), a teammate in an agent team, or a partner software product (Claude Marketplace).
6. What a plugin holds differs by page: Claude Code glossary says skills, hooks, subagents and MCP servers; the manifest reference adds LSP servers, output styles, themes, monitors, workflows, `bin/`, settings and channels; claude.com says skills, MCP connectors, commands and agents.
7. The Help Center personalization page disagrees with itself on who gets project instructions. https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features: "Use project instructions when you need specific guidance or context for a particular project (paid plans only)." The same page also says: "Projects are available to all users, including those with free Claude accounts."


## Plugins, marketplaces and related words: GitHub Copilot CLI, VS Code, Visual Studio, OpenAI Codex

Research notes. All pages fetched on 2026-10-22. Each entry gives a one-line summary, the URL, a short verbatim excerpt, and the page title and publisher. "Not found" means the word did not appear in the pages fetched. It does not prove the product lacks the feature.

Note on Codex URLs: developers.openai.com/codex/* now answers with a 308 redirect to learn.chatgpt.com/docs/*. The Codex docs are now part of "ChatGPT Learn", and they describe ChatGPT and Codex together.

---

## 1. GitHub Copilot CLI

### plugin
A plugin is an installable directory with a `plugin.json` manifest. It can bundle custom agents, skills, hooks, extensions, MCP server configs and LSP server configs.
- https://docs.github.com/en/copilot/concepts/customizations/plugins
- "Plugins are installable packages that extend Copilot with reusable agents, skills, hooks, and integrations." / "A plugin is a directory with a specific structure and a `plugin.json` manifest file."
- "Plugins for GitHub Copilot", GitHub Docs

Supported surfaces, per the same page: "The GitHub Copilot app.", "GitHub Copilot CLI.", "Copilot cloud agent." and "Visual Studio Code. For supported components and installation, see Agent plugins in VS Code."

Two manifest formats exist. The legacy format lets the manifest name component folders. The newer "Agent Plugins 1.0" format makes skills and MCP portable and puts Copilot-only parts in a `com.github.copilot/` folder.
- https://docs.github.com/en/copilot/concepts/customizations/plugins
- "Agent Plugins 1.0 is a portable format for sharing skills and MCP server configurations across compatible clients." / "Other components, including agents, hooks, commands, and LSP servers, are client-specific."
- "Plugins for GitHub Copilot", GitHub Docs

Manifest fields and lookup order (legacy):
- https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference
- "`.plugin/plugin.json`, `plugin.json`, `.github/plugin/plugin.json`, or `.claude-plugin/plugin.json` (checked in this order)"
- Component path fields: `agents` "Path(s) to agent directories (`.agent.md` files).", `skills` "Path(s) to skill directories (`SKILL.md` files).", `commands` "Path(s) to command directories.", `hooks`, `mcpServers`, `lspServers`.
- "GitHub Copilot CLI plugin reference", GitHub Docs

The Agent Plugins format is an outside spec. Copilot CLI supports it but does not claim to have written it.
- https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference
- "Copilot CLI recognizes the canonical `$schema` values for Agent Plugins (Open Plugin Spec) v1.0.0 … (`https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`)" / "Agent Plugins 1.0 does not define portable agents, hooks, commands, rules, or LSP servers."
- "GitHub Copilot CLI plugin reference", GitHub Docs
- https://agent-plugins.org/
- "Agent Plugins is an open, vendor-neutral standard for packaging reusable components into portable plugins." / "Its initial Technical Steering Committee includes Core Maintainers from Amazon, Cursor, Microsoft, OpenAI, and Vercel."
- "Agent Plugins", agent-plugins.org

Install commands:
- https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing
- "copilot plugin install PLUGIN-NAME@MARKETPLACE-NAME" / "/plugin install PLUGIN-NAME@MARKETPLACE-NAME"
- "Finding and installing plugins for GitHub Copilot CLI", GitHub Docs

Other install sources (reference): `plugin@marketplace`, `OWNER/REPO`, `OWNER/REPO:PATH/TO/PLUGIN`, a Git URL, a local path. Installed copies live in "`~/.copilot/installed-plugins/MARKETPLACE/PLUGIN-NAME` (installed via a marketplace)" (cli-plugin-reference).

### marketplace
A plugin marketplace is a Git repo, URL or local folder with a `marketplace.json` that lists plugins. You register it, then install plugins from it by name.
- https://docs.github.com/en/copilot/concepts/customizations/plugins
- "A marketplace is a location where developers can publish, discover, install, and manage plugins." / "A marketplace is defined by a `marketplace.json` file"
- "Plugins for GitHub Copilot", GitHub Docs

Where `marketplace.json` lives. Claude Code's folder is also read.
- https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace
- "Add the `marketplace.json` file to the `.github/plugin` directory of a repository." / "Copilot CLI also looks for the `marketplace.json` file in the `.claude-plugin/` directory."
- "Creating a plugin marketplace for GitHub Copilot CLI", GitHub Docs

Fields: top-level `name`, `owner`, `metadata`, `plugins`. Each plugin entry has a `source`: "Where to fetch the plugin (relative path, GitHub, or URL)." (cli-plugin-reference)

Adding a marketplace. The docs use Claude Code's own repo as the example.
- https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing
- "copilot plugin marketplace add OWNER/REPO" / "copilot plugin marketplace add anthropics/claude-code"
- "Finding and installing plugins for GitHub Copilot CLI", GitHub Docs

Default marketplace:
- https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference
- "The built-in `awesome-copilot` default marketplace ships with the runtime and can't be removed." / "It's now an ordinary, non-default marketplace (`github/copilot-plugins`) that you register yourself"
- "GitHub Copilot CLI plugin reference", GitHub Docs

MCP registry (a separate kind of catalog, for MCP servers only):
- https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
- "You can discover and install MCP servers directly from the GitHub MCP Registry using the `/mcp search` command" / "The `/mcp search` command is currently an experimental feature."
- "Adding MCP servers for GitHub Copilot CLI", GitHub Docs

### extension
In Copilot CLI an extension is a JavaScript module that adds tools and slash commands. It is experimental, and it is not the retired GitHub App "Copilot Extensions".
- https://docs.github.com/en/copilot/concepts/customizations/extensions
- "An extension for Copilot CLI is a JavaScript module that runs as a separate Node.js process alongside an interactive session." / "These extensions are distinct from the retired GitHub App-based Copilot Extensions integration."
- "Extensions for GitHub Copilot", GitHub Docs

What extensions add, and how they relate to plugins:
- https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/agents/copilot-cli/about-cli-extensions
- "Tools that the agent can call while working on your request." / "Slash commands that you invoke yourself." / "A plugin can distribute extensions, but the surface determines how those extensions are used." / "GitHub Copilot CLI extensions are currently an experimental feature and are subject to change."
- "Extensions for GitHub Copilot", GitHub Docs (Enterprise Cloud version)

The `extensions` field in plugin.json means different things in the two manifest formats.
- https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference
- Legacy: "Path(s) to extension directories." Agent Plugins 1.0: "Client-specific data keyed by reverse-domain namespace."
- "GitHub Copilot CLI plugin reference", GitHub Docs

Old GitHub App-based "Copilot Extensions" (all surfaces) were shut down in favor of MCP.
- https://github.blog/changelog/2025-09-24-deprecate-github-copilot-extensions-github-apps/
- "We are deprecating GitHub Copilot Extensions (built as GitHub Apps) on November 10, 2025," / "in favor of Model Context Protocol (MCP) servers."
- "Sunset notice: GitHub App-based Copilot Extensions", GitHub Changelog

### connector
Not found in the Copilot CLI pages fetched.

### MCP server
The GitHub MCP server is built in. You add others with `/mcp add`, `copilot mcp add`, `~/.copilot/mcp-config.json`, or a repo `.mcp.json` / `.github/mcp.json`. The CLI does not read `.vscode/mcp.json`.
- https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
- "The GitHub MCP server is built into Copilot CLI and is already available without any additional configuration." / "The `.vscode/mcp.json` file for VS Code is not read by Copilot CLI."
- "Adding MCP servers for GitHub Copilot CLI", GitHub Docs

### skill
Agent skills are `SKILL.md` folders. The CLI reads `.github/skills`, `.claude/skills` and `.agents/skills` in the repo, and `~/.copilot/skills` and `~/.agents/skills` in your home folder. You can invoke one with `/name`.
- https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills
- "Agent skills are folders of instructions, scripts, and resources that Copilot can load when relevant" / "create a `.github/skills`, `.claude/skills`, or `.agents/skills` directory in your repository."
- "Adding agent skills for GitHub Copilot CLI", GitHub Docs
- Invocation: "include the skill name in your prompt, preceded by a forward slash."

### sub-agent / custom agent
Custom agents are `.agent.md` files in `.github/agents/` or `~/.copilot/agents/`. When the main agent hands work to one, it runs as a subagent with its own context.
- https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli
- "Each custom agent is defined by a Markdown file with an `.agent.md` extension." / "When the main agent delegates work to a custom agent, that work is carried out by a subagent with its own context window."
- "Creating and using custom agents for GitHub Copilot CLI", GitHub Docs

### hook
Hooks are shell commands that run at lifecycle events. They live in `.github/hooks/*.json` or `~/.copilot/hooks/`. Event names are camelCase (`sessionStart`, `preToolUse`, `postToolUse`, `agentStop` and others).
- https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-hooks
- "Extend GitHub Copilot agent behavior with custom shell commands at key points during agent execution."
- "Using hooks with GitHub Copilot CLI", GitHub Docs

### slash command / prompt file
Built-in slash commands exist (`/plugin`, `/mcp`, `/agent`, `/extensions`, `/instructions` and more). The fetched pages do not document user `.prompt.md` files for the CLI. Your own slash commands come from skills (`/skill-name`), from extensions (experimental), or from a plugin's client-specific `commands`.
- https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference
- `/plugin`: "Open the plugins dashboard showing your installed plugins." / `/extensions`: "Manage CLI extensions. Only available in experimental mode."
- "GitHub Copilot CLI command reference", GitHub Docs
- The plugin-creating page names `commands` only once, as a Copilot-specific component: "components such as agents, commands, rules, hooks, and LSP servers come from the `com.github.copilot` directory" (https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating, "Creating a plugin for GitHub Copilot CLI", GitHub Docs). That page does not define what a command file is.

### instructions file
The CLI reads `.github/copilot-instructions.md`, `.github/instructions/**/*.instructions.md`, `AGENTS.md`, `CLAUDE.md` (also `.claude/CLAUDE.md`), `GEMINI.md`, and user-level `$HOME/.copilot/copilot-instructions.md`.
- https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions
- `AGENTS.md`: "Agent instructions, discovered in the standard locations." / `CLAUDE.md`: "Agent instructions, discovered in the standard locations. Copilot CLI also uses `.claude/CLAUDE.md`."
- "Adding custom instructions for GitHub Copilot CLI", GitHub Docs

### app / integration
"App" here means the separate GitHub Copilot app (a desktop client). The CLI can open a session in it. "Integrations" is used loosely, for MCP in plugins.
- https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference
- `/app`: "Open the current session in the GitHub Copilot app (requires version 1.1.3 or later)"
- "GitHub Copilot CLI command reference", GitHub Docs

---

## 2. VS Code with GitHub Copilot (chat / agents)

Docs moved from /docs/copilot/ to /docs/agent-customization/ and /docs/agents/. VS Code now uses the term "harness" for the runtime behind a chat session (Local, Copilot, Anthropic Claude, OpenAI Codex).
- https://code.visualstudio.com/docs/agents/concepts/agent-harnesses
- "An agent harness is the software layer that runs an agent session." / "VS Code supports multiple agent harnesses, including Copilot, Anthropic Claude, and OpenAI Codex."
- "Understand agent harnesses", VS Code docs (Microsoft)

### plugin
"Agent plugins" bundle skills, MCP servers, custom agents, hooks and slash commands into one install. VS Code picks up plugins installed by Copilot CLI and reads the Copilot, Claude and legacy OpenPlugin formats.
- https://code.visualstudio.com/docs/agent-customization/agent-plugins
- "Agent plugins bundle related customizations into one installable setup." / "VS Code automatically discovers plugins that you install with the GitHub Copilot CLI" / "VS Code also supports existing Copilot, Claude, and legacy OpenPlugin formats."
- "Agent plugins in VS Code", VS Code docs (Microsoft)
- Caveat on same page: "Support for a package format doesn't guarantee that every component works in every harness or client."

### marketplace
In VS Code the word covers three or four different catalogs:
1. The Visual Studio Marketplace, for VS Code extensions.
   - https://code.visualstudio.com/docs/getstarted/extensions
   - "The Visual Studio Marketplace hosts thousands of extensions across a wide range of categories."
   - "Use extensions in Visual Studio Code", VS Code docs (Microsoft)
2. Plugin marketplaces (Git repos), found through `@agentPlugins` in the Extensions view, `/plugin install`, and the `chat.plugins.marketplaces` setting (experimental).
   - https://code.visualstudio.com/docs/agent-customization/agent-plugins
   - "You can discover plugins from marketplaces such as copilot-plugins and awesome-copilot." / "To configure additional marketplaces, use chat.plugins.marketplaces"
   - "Agent plugins in VS Code", VS Code docs (Microsoft)
   - The same page sends readers to Claude Code for the schema: "For the full marketplace plugin schema, see the Claude Code plugin marketplace documentation."
3. The "Customization Marketplace" (experimental), a single Discover page for skills, MCP servers and plugins, with a "GitHub Feed" source.
   - https://code.visualstudio.com/docs/agent-customization/overview
   - "a unified Discover page for finding skills, MCP servers, plugins, and other agent customizations." / "The GitHub Feed source is available by default when the marketplace is enabled."
   - "Create and manage agent customizations", VS Code docs (Microsoft)
4. The MCP server gallery (`@mcp` in the Extensions view, preview).
   - https://code.visualstudio.com/docs/agent-customization/mcp-servers
   - "Use the MCP server gallery (Preview) to browse publishers and capabilities" / "Select GitHub Feed from the source menu and search by name or with `@type:mcp`."
   - "Add MCP servers in VS Code", VS Code docs (Microsoft)

### extension
A VS Code extension is an editor extension from the Visual Studio Marketplace. Extensions can add language model tools. Chat participants (the old client-side "Copilot Extensions") are deprecated, and plugins are the recommended replacement.
- https://code.visualstudio.com/api/extension-guides/ai/ai-extensibility-overview
- "Language model tools enable you to extend agent mode in VS Code with domain-specific capabilities." / "Chat participants are not supported in the Copilot harness." / "Plugins are the recommended replacement for deprecated chat participants."
- "AI extensibility in VS Code", Visual Studio Code Extension API (Microsoft)

### connector
Not found in the VS Code pages fetched.

### MCP server
Add servers with "MCP: Add Server". The new default files are `~/.copilot/mcp-config.json` (global) and workspace `.mcp.json`. `.vscode/mcp.json` still works but is labeled deprecated. The two formats use different top-level keys.
- https://code.visualstudio.com/docs/agent-customization/mcp-servers
- "These destinations remain available for compatibility and are labeled deprecated in the guided flow." / "Portable files use a top-level mcpServers object. The VS Code format uses servers."
- "Add MCP servers in VS Code", VS Code docs (Microsoft)

### skill
VS Code supports Agent Skills (`SKILL.md`, agentskills.io). It reads `.github/skills`, `.claude/skills` and `.agents/skills` in the project, and `~/.copilot/skills`, `~/.claude/skills` and `~/.agents/skills` in your home folder. Skills appear as slash commands.
- https://code.visualstudio.com/docs/agent-customization/agent-skills
- "Agent Skills is an open standard that works across multiple AI agents" / "Skills are available as slash commands in chat, alongside prompt files."
- "Use Agent Skills in VS Code", VS Code docs (Microsoft)

### sub-agent / custom agent
Custom agents are `.agent.md` files. They used to be called custom chat modes (`.chatmode.md`). VS Code also reads Claude-format agents in `.claude/agents` and `~/.claude/agents`. Any custom agent can run as a subagent.
- https://code.visualstudio.com/docs/agent-customization/custom-agents
- "Custom agents were previously known as custom chat modes." / "If you have existing `.chatmode.md` files, rename them to `.agent.md`" / "Another agent can also run a custom agent as a subagent"
- "Custom agents in VS Code", VS Code docs (Microsoft)

### hook
Hooks are in preview. They use the same files and format as Copilot CLI (`~/.copilot/hooks/`, `.github/hooks/*.json`). VS Code also reads `.claude/settings.json`.
- https://code.visualstudio.com/docs/agent-customization/hooks
- "VS Code, the GitHub Copilot app, and GitHub Copilot CLI share this harness and its hook format." / "The VS Code hooks experience is in Preview." / "Sharing a hook file location does not establish runtime compatibility."
- "Configure agent hooks in Visual Studio Code (Preview)", VS Code docs (Microsoft)

### slash command / prompt file
Prompt files (`.prompt.md` in `.github/prompts`) are run as slash commands. They now work only in the Local harness. For other harnesses the docs say to use skills. The page does not call prompt files deprecated.
- https://code.visualstudio.com/docs/agent-customization/prompt-files
- "Prompt files run only in **Local** harness sessions in the Chat view." / "For reusable workflows in other harnesses, create an agent skill or convert an existing prompt file to a skill."
- "Use prompt files in VS Code", VS Code docs (Microsoft)

### instructions file
VS Code reads `.github/copilot-instructions.md`, `*.instructions.md` (in `.github/instructions`, `.claude/rules`, `~/.copilot/instructions`, `~/.claude/rules`), `AGENTS.md` (nested files too), and `CLAUDE.md`.
- https://code.visualstudio.com/docs/agent-customization/custom-instructions
- "`AGENTS.md` is a cross-agent format for project guidance." / "For Anthropic Claude sessions, use `CLAUDE.md` at the repository root for project-wide guidance."
- "Use custom instructions in VS Code", VS Code docs (Microsoft)

### app / integration
Not a VS Code customization term. "GitHub Copilot app" appears only as another client that shares the hook format (hooks page, above).

---

## 3. Visual Studio 2022 / 2026 with GitHub Copilot

Starting in 18.11, chat in Visual Studio can run on the same Copilot SDK as Copilot CLI and the GitHub Copilot app. You have to opt in.
- https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-chat?view=visualstudio
- "Starting in Visual Studio 2026 version 18.11, the new chat experience uses a shared Copilot SDK foundation also used by the Copilot CLI and GitHub Copilot app."
- "About GitHub Copilot Chat in Visual Studio", Microsoft Learn

### plugin
Not found. The agent mode, agents, skills, MCP and chat-context pages, and the 2026 release notes (18.4 through 18.11 sections read), do not mention plugins or plugin marketplaces.

### marketplace
The Visual Studio Marketplace distributes Visual Studio extensions (VSIX/MSI). MCP servers can come from the "GitHub MCP server registry" through Extensions > MCP Registries.
- https://learn.microsoft.com/en-us/visualstudio/ide/finding-and-using-visual-studio-extensions?view=visualstudio
- "You can install extensions from Visual Studio Marketplace or from Extension Manager in Visual Studio."
- "Find and Manage Extension Packages", Microsoft Learn
- https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers?view=visualstudio
- "You can install an MCP server directly from the GitHub MCP server registry via **Extensions** in Visual Studio."
- "Use MCP Servers to Extend GitHub Copilot", Microsoft Learn

### extension
A Visual Studio extension is a code package that runs inside the IDE. GitHub Copilot itself is installed as one.
- https://learn.microsoft.com/en-us/visualstudio/ide/finding-and-using-visual-studio-extensions?view=visualstudio
- "Extensions are code packages that run inside Visual Studio and provide new or improved features." (The page's examples include Live Share and GitHub Copilot.)
- "Find and Manage Extension Packages", Microsoft Learn

### connector
Not found.

### MCP server
Visual Studio reads `%USERPROFILE%\.mcp.json`, `<SOLUTIONDIR>\.vs\mcp.json`, `<SOLUTIONDIR>\.mcp.json`, `<SOLUTIONDIR>\.vscode\mcp.json` and `<SOLUTIONDIR>\.cursor\mcp.json`. Its example uses a `servers` key.
- https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers?view=visualstudio
- "Visual Studio also checks for MCP configurations that other development environments set up."
- "Use MCP Servers to Extend GitHub Copilot", Microsoft Learn

### skill
Supported from 18.5 (with a bug-fix mention in 18.4.1). Same folders as VS Code. Built-in .NET and Azure skills are off by default.
- https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-skills?view=visualstudio
- "Workspace or project skills (stored in your repository) | `.github/skills/`, `.claude/skills/`, `.agents/skills/`" / "Each skill is a directory containing a `SKILL.md` file that follows the agentskills.io specification."
- "Use Agent Skills with GitHub Copilot", Microsoft Learn

### sub-agent / custom agent
Custom agents (18.4+) are `.agent.md` files in `.github/agents/`. User-level agents default to `%USERPROFILE%\.github\agents`, which is not the `~/.copilot/agents` that CLI and VS Code use. There are also built-in agents (`@debugger`, `@git`, `@profiler`, `@test`, `@modernize`, Plan) and org-level agents (18.9+). The word "subagent" was not found.
- https://learn.microsoft.com/visualstudio/ide/copilot-specialized-agents
- "To create a user-level agent that applies across all your projects, store its `.agent.md` file in `%USERPROFILE%\.github\agents` by default."
- "Use GitHub Copilot agents in Visual Studio", Microsoft Learn

### hook
Not found in the Visual Studio pages or release notes read.

### slash command / prompt file
Prompt files are `.github/prompts/*.prompt.md`. In VS 2026 you can invoke one with `/`, and `/savePrompt` creates one. There are also built-in commands (`/explain`, `/fix`, `/tests`, `/generateInstructions` and others).
- https://learn.microsoft.com/en-us/visualstudio/ide/copilot-chat-context?view=visualstudio
- "save it with the `.prompt.md` extension in the `.github/prompts` folder at the root of your repository." / "Once you create prompt files, you can quickly invoke them by typing `/` in the chat input."
- "Customize chat responses", Microsoft Learn

### instructions file
Visual Studio reads `.github/copilot-instructions.md` (a setting must be turned on), `.github/instructions/*.instructions.md` with `applyTo`, org-level instructions, and user-level `%USERPROFILE%/copilot-instructions.md`. `AGENTS.md` and `CLAUDE.md` were not mentioned in the pages read.
- https://learn.microsoft.com/en-us/visualstudio/ide/copilot-chat-context?view=visualstudio
- "The `%USERPROFILE%/copilot-instructions.md` file stores these preferences."
- "Customize chat responses", Microsoft Learn

### app / integration
Not a Visual Studio term here, apart from the "GitHub Copilot app" named as a fellow user of the Copilot SDK (above).

---

## 4. OpenAI Codex (CLI, IDE extension, ChatGPT desktop app, cloud)

Codex docs now sit under ChatGPT Learn. The former Codex app is documented as the "ChatGPT desktop app", where you choose ChatGPT or Codex.
- https://learn.chatgpt.com/docs/app
- "Choose ChatGPT or Codex."
- "ChatGPT desktop app", ChatGPT Learn (OpenAI)

### plugin
Plugins are shared by ChatGPT and Codex. They can contain skills, MCP servers, browser extensions and hooks. You install them in the ChatGPT desktop app (Codex) or with `/plugins` in Codex CLI. The Codex IDE extension does not support plugins.
- https://learn.chatgpt.com/docs/plugins
- "Plugins bundle capabilities into reusable workflows in ChatGPT and Codex. They can include skills and MCP servers." / "In Codex CLI, enter `/plugins` to open the plugin browser." / "The IDE extension doesn't support plugins."
- "Plugins", ChatGPT Learn (OpenAI)

Manifest: the recommended format is root `plugin.json` using the Agent Plugins schema. `.codex-plugin/plugin.json` is still accepted.
- https://developers.openai.com/plugins/build/plugins
- "For a portable Agent Plugins package, add `plugin.json` at the plugin root and declare the Agent Plugins schema." / "Existing `.codex-plugin/plugin.json` files remain supported as a compatibility fallback." / "OpenAI also accepts legacy and Claude-compatible manifests, but new packages should use this format."
- "Package your plugin", OpenAI developer docs

### marketplace
A marketplace is a JSON catalog. Codex reads `.agents/plugins/marketplace.json` (repo), `~/.agents/plugins/marketplace.json` (personal), and the legacy `.claude-plugin/marketplace.json`. You add one with `codex plugin marketplace add`. Public plugins go to one "universal plugin directory" shared with ChatGPT, also called the ChatGPT Directory and the Plugins Directory.
- https://developers.openai.com/plugins/build/plugins
- "A marketplace is a JSON catalog of plugins." / "a legacy-compatible marketplace at `$REPO_ROOT/.claude-plugin/marketplace.json`" / "Use `codex plugin marketplace add` to add and track a marketplace source instead of editing `config.toml` by hand."
- "Package your plugin", OpenAI developer docs
- https://learn.chatgpt.com/docs/plugins
- "Both products use one universal plugin directory, so the same public plugins are discoverable from their supported surfaces." / "The CLI plugin browser groups plugins by marketplace."
- "Plugins", ChatGPT Learn (OpenAI)

Claude Code plugins can be submitted to the directory, but Claude marketplace files are not carried over.
- https://developers.openai.com/plugins/guides/submit-claude-plugin
- "Claude marketplace listings and approvals don't transfer." / for `.claude-plugin/plugin.json`: "The portal converts it to `.codex-plugin/plugin.json`."
- "Submit your Claude Code plugin to OpenAI", OpenAI developer docs

### connector
The word survives but is not a separate thing. A plugin "bundles connectors" (MCP connections). The admin page still has the URL slug "apps-and-connectors", but the page is titled "Plugin controls". No page read said "connectors were renamed to apps". The help.openai.com articles returned 403 and could not be checked.
- https://learn.chatgpt.com/docs/extend/mcp
- "In a hosted ChatGPT Work chat, install a plugin to use its bundled connectors and remote MCP tools."
- "Model Context Protocol", ChatGPT Learn (OpenAI)

### app / integration
In OpenAI admin docs, "app" and "MCP server" mean the same thing. "App" also names the ChatGPT desktop app, the "MCP Apps" UI standard, and the `apps` field / `.app.json` in plugins. https://developers.openai.com/apps-sdk now serves a page titled "Plugins", and that page never says "Apps SDK".
- https://learn.chatgpt.com/docs/enterprise/apps-and-connectors
- "In this guide, **app** and **MCP server** refer to the same connected integration and are interchangeable terms."
- "Plugin controls", ChatGPT Learn (OpenAI)
- https://developers.openai.com/plugins/build/plugins
- "Use the OpenAI extension's `apps` field only for registered MCP server mappings in `.app.json`."
- "Package your plugin", OpenAI developer docs

### extension
At least three meanings: the Codex IDE extension (VS Code, Cursor, Windsurf), "browser extensions" as a plugin part, and "OpenAI MCP Extensions" (additions to the MCP/MCP Apps protocol).
- https://learn.chatgpt.com/docs/ide
- "VS Code and compatible editors use the Codex extension; Xcode and JetBrains IDEs provide their own integrations."
- "Codex IDE extension", ChatGPT Learn (OpenAI)
- https://developers.openai.com/plugins/build/extensions
- "OpenAI MCP Extensions enables developers to hook their plugins into key surfaces of the ChatGPT user experience"
- "Plugin Extensions", OpenAI developer docs

### MCP server
Configured in `~/.codex/config.toml` or `.codex/config.toml` under `[mcp_servers.<name>]`, or with `codex mcp add`. The ChatGPT desktop app, CLI and IDE extension share this config. ChatGPT web does not read it.
- https://learn.chatgpt.com/docs/extend/mcp
- "The ChatGPT desktop app, Codex CLI, and IDE extension share this configuration." / "Installed plugins can bundle MCP servers in their plugin manifest."
- "Model Context Protocol", ChatGPT Learn (OpenAI)

### skill
`SKILL.md` folders following the open agent skills standard. Codex scans `.agents/skills` from the current directory up to the repo root, plus `$HOME/.agents/skills` and `/etc/codex/skills`. Use `/skills` or `$name` in the CLI and IDE, and `@` in ChatGPT.
- https://learn.chatgpt.com/docs/build-skills
- "Codex scans `.agents/skills` in every directory from your current working directory up to the repository root." / "In Codex CLI or the IDE extension, run `/skills` or type `$` to mention a skill."
- "Build skills", ChatGPT Learn (OpenAI)

### sub-agent / custom agent
Codex runs subagents in parallel. Custom agents are TOML files (not Markdown) in `~/.codex/agents/` or `.codex/agents/`. Built-in agents are `default`, `worker` and `explorer`.
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- "add standalone TOML files under `~/.codex/agents/` for personal agents or `.codex/agents/` for project-scoped agents"
- "Subagents", ChatGPT Learn (OpenAI)

### hook
Hooks are on by default. They live in `hooks.json` or `[hooks]` in `config.toml` (user or repo `.codex/`), or `hooks/hooks.json` inside a plugin. Event names are PascalCase (`PreToolUse`, `PostToolUse`, `SessionStart` and others). Codex sets Claude's plugin variables for compatibility.
- https://learn.chatgpt.com/docs/hooks
- "Hooks are an extensibility framework for Codex." / "Codex also sets `CLAUDE_PLUGIN_ROOT` and `CLAUDE_PLUGIN_DATA` for compatibility with existing plugin hooks."
- "Hooks", ChatGPT Learn (OpenAI)

### slash command / prompt file
Custom prompts (Markdown in `~/.codex/prompts`, run as `/prompts:name`) are deprecated in favor of skills.
- https://learn.chatgpt.com/docs/custom-prompts
- "Custom prompts are deprecated. Use skills for reusable instructions that Codex can invoke explicitly or implicitly."
- "Custom Prompts", ChatGPT Learn (OpenAI)

### instructions file
Codex reads `AGENTS.md`, with `AGENTS.override.md` taking precedence, at the global level (`~/.codex`) and in each directory from the project root down. It reads other names only if they are listed in `project_doc_fallback_filenames`. `CLAUDE.md` is not mentioned.
- https://learn.chatgpt.com/docs/agent-configuration/agents-md
- "Codex reads `AGENTS.md` files before doing any work." / "Filenames not on this list are ignored for instruction discovery."
- "Custom instructions with AGENTS.md", ChatGPT Learn (OpenAI)

---

## Where names overlap or disagree

- **"Extension"** has at least six meanings: a VS Code extension, a Visual Studio extension, a Copilot CLI extension (JS module, experimental), the retired GitHub App "Copilot Extensions" (sunset 2025-11-10), the Codex IDE extension, and OpenAI "MCP Extensions" / plugin "browser extensions". Inside one Copilot manifest, the `extensions` field also changes meaning between the legacy and Agent Plugins 1.0 formats.
- **"Marketplace"**: in VS Code and Visual Studio it first means the Visual Studio Marketplace for editor extensions. It also means plugin marketplaces (`marketplace.json` in a Git repo) in Copilot CLI, VS Code and Codex, and VS Code's experimental "Customization Marketplace". OpenAI also uses "directory" (universal plugin directory, ChatGPT Directory, Plugins Directory) for its public listing.
- **"App"**: OpenAI uses it for an MCP server ("interchangeable terms"), for the ChatGPT desktop app, for "MCP Apps" UI, and for the `apps` manifest field. GitHub uses "GitHub Copilot app" for a desktop client and, historically, "GitHub Apps" for the retired Copilot Extensions.
- **"Connector"**: only OpenAI and Claude-related pages use it. Neither GitHub nor Microsoft product pages read here use it.
- **Custom agents and chat modes**: VS Code says custom agents "were previously known as custom chat modes". GitHub products use `.agent.md` Markdown. Codex uses TOML. VS Code also reads Claude-format `.md` agents.
- **Same plugin format in several places**: Copilot CLI and OpenAI both accept the Agent Plugins 1.0 schema (agent-plugins.org). Both also read Claude Code's `.claude-plugin/` marketplace files. VS Code reads Copilot, Claude and "legacy OpenPlugin" formats.
- **Default plugin marketplace (Copilot)**: the CLI how-to names only `awesome-copilot` as the default, and the reference says `github/copilot-plugins` is no longer a default. The VS Code page names "copilot-plugins and awesome-copilot" as examples without calling either one a default.
- **Codex `/plugins`**: the Plugins page says to type `/plugins` in Codex CLI. The slash-command reference (written for the desktop app) does not list it, and the developer-commands page lists the `codex plugin` subcommand instead.
- **Codex IDE extension**: no plugin support ("The IDE extension doesn't support plugins."), even though it shares MCP config with the CLI.
- **User-level paths differ across GitHub's own clients**: Visual Studio uses `%USERPROFILE%\.github\agents` and `%USERPROFILE%/copilot-instructions.md`. Copilot CLI and VS Code use `~/.copilot/agents` and `~/.copilot/copilot-instructions.md`.
- **Skill folders**: Copilot CLI personal skills are `~/.copilot/skills` and `~/.agents/skills`, and its docs do not mention `~/.claude/skills`. VS Code and Visual Studio add `~/.claude/skills`. Codex reads only `.agents/skills`, not `.github/skills` or `.claude/skills`.
- **Hook event casing**: Copilot uses camelCase (`preToolUse`) and Codex uses PascalCase (`PreToolUse`). The VS Code Local harness accepts both. VS Code warns: "Sharing a hook file location does not establish runtime compatibility."
- **MCP config key**: VS Code's own format uses `servers`, the portable format uses `mcpServers`, and Visual Studio's example uses `servers`. Copilot CLI ignores `.vscode/mcp.json`. Visual Studio reads it, along with `.cursor/mcp.json`.
- **Prompt files**: VS Code limits them to the Local harness and points to skills. Visual Studio supports them fully (`/savePrompt`). Codex's version (custom prompts) is deprecated. The fetched Copilot CLI docs do not mention them.
