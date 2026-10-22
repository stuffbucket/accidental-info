# Copilot CLI: where configuration lives (source notes)

All pages fetched from docs.github.com on 22 October 2026 (markdown via the docs article API). Excerpts are verbatim. No github.blog changelog was needed.

## Pages

| # | Title | URL |
|---|---|---|
| A | Adding custom instructions for GitHub Copilot CLI | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions |
| B | GitHub Copilot CLI command reference | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference |
| C | GitHub Copilot CLI configuration directory | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference |
| D | Support for different types of custom instructions | https://docs.github.com/en/copilot/reference/custom-instructions-support |
| E | Custom instructions for GitHub Copilot (concept) | https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions |
| F | Adding agent skills for GitHub Copilot CLI | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills |
| G | Agent skills (concept) | https://docs.github.com/en/copilot/concepts/agents/about-agent-skills |
| H | Adding MCP servers for GitHub Copilot CLI | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers |
| I | Creating and using custom agents for GitHub Copilot CLI | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli |
| J | Invoking custom agents | https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents |
| K | GitHub Copilot CLI plugin reference | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference |
| L | Plugins for GitHub Copilot (concept) | https://docs.github.com/en/copilot/concepts/agents/about-plugins |
| M | Finding and installing plugins for GitHub Copilot CLI | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing |
| N | Configuring GitHub Copilot CLI | https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/configure-copilot-cli |
| O | Allowing and denying tool use | https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools |
| P | Changing settings with the /settings command | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/change-settings |
| Q | GitHub Copilot hooks reference | https://docs.github.com/en/copilot/reference/hooks-reference |
| R | Administering Copilot CLI for your enterprise | https://docs.github.com/en/copilot/how-tos/copilot-cli/administer-copilot-cli-for-your-enterprise |
| S | Enterprise managed settings | https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings |
| T | Getting started with enterprise-managed settings | https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started |
| U | About enterprise-managed plugin standards | https://docs.github.com/en/copilot/concepts/enterprise/plugin-standards |
| V | Restrict MCP server access to a custom registry | https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/restrict-based-on-registry |
| W | Configuring an MCP server allowlist for your enterprise | https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-enterprise-allowlist |
| X | Copilot customization cheat sheet | https://docs.github.com/en/copilot/reference/customization-cheat-sheet |

Date checked for every page: 22 October 2026.

---

## 1. Custom instructions

**Locations (A, table "Types of custom instructions"):**

> | `$HOME/.copilot/copilot-instructions.md` | User-level instructions that apply across repositories. |
> | `$HOME/.copilot/instructions/**/*.instructions.md` | Modular user-level instructions. |
> | `.github/copilot-instructions.md` | Repository-wide instructions, discovered in the standard locations. |
> | `.github/instructions/**/*.instructions.md` | Modular repository instructions, discovered in the standard locations but not intermediate directories. |
> | `AGENTS.md` | Agent instructions, discovered in the standard locations. |
> | `CLAUDE.md` | Agent instructions, discovered in the standard locations. Copilot CLI also uses `.claude/CLAUDE.md`. |
> | `GEMINI.md` | Agent instructions, discovered in the standard locations. |
> | Directories listed in `COPILOT_CUSTOM_INSTRUCTIONS_DIRS` | Additional `AGENTS.md` and `*.instructions.md` files. Separate multiple directories with commas. |

**"Standard locations" (A):**

> Copilot CLI discovers repository and agent instruction files in the **standard locations**: the repository root, the current working directory, intermediate directories between them, and any directories nested in the path of a file it is working on.

**COPILOT_HOME (A):**

> If you set the `COPILOT_HOME` environment variable, Copilot CLI uses that directory instead of `$HOME/.copilot` for both user-level instruction locations.

**How they combine (A):**

> When multiple applicable user-level and repository instruction files exist, Copilot CLI combines their instructions. It removes duplicate copies of identical user-level `copilot-instructions.md`, repository-wide, and agent instructions, but does not define a general precedence order between these files. Avoid conflicting instructions.

> Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with. An instruction file that you disable using `/instructions` is not included.

E agrees: "Most surfaces and clients, including Copilot CLI, Visual Studio Code and Visual Studio, combine applicable instruction files without defining a general precedence order."

**applyTo frontmatter (A):** "At the start of the file, create a frontmatter block containing the `applyTo` keyword. Use glob syntax to specify what files or directories the instructions apply to." Example: `applyTo: "**/*.ts,**/*.tsx"`.

**When changes take effect (A):** "Changes you make to custom instructions files are not immediately available for use in active CLI sessions."

**B, "Custom instructions locations" (narrower wording, extra location):**

> Copilot CLI loads custom instructions from these locations simultaneously (all are merged):

Table lists `CLAUDE.md`, `GEMINI.md`, `AGENTS.md`, `.github/instructions/**/*.instructions.md`, `.claude/rules/**/*.md`, `.github/copilot-instructions.md` each with "In Git root and cwd", plus `$HOME/.copilot/copilot-instructions.md`, `$HOME/.copilot/instructions/**/*.instructions.md`, `COPILOT_CUSTOM_INSTRUCTIONS_DIRS`.

> Copilot CLI reads Claude Code rule files from `.claude/rules/**/*.md` the same way it reads `.github/instructions/**/*.instructions.md` files. Scope a rule to matching files with a `paths` (or `applyTo`) frontmatter key

**DISAGREEMENT:** A says files are found in repo root, cwd, intermediate directories and directories nested in the path of a file being worked on; B says "In Git root and cwd". A does not list `.claude/rules/**/*.md`; B does. A says `@` imports must stay in the repo and "Absolute paths and paths beginning with `~/` are not loaded"; B says "Paths can be relative to the instruction file's directory or absolute."

**Opt out:** B: "`--no-custom-instructions` | Disable loading of custom instructions from `AGENTS.md` and related files."

**Organization instructions:** D's "Copilot CLI" section lists only Repository-wide, Path-specific, Agent instructions (AGENTS.md, CLAUDE.md or GEMINI.md) and "👤 Personal instructions (using ~/.copilot/copilot-instructions.md or ~/.copilot/instructions/**/*.instructions.md files)". Organization instructions are listed for GitHub.com Chat, cloud agent and code review, not for CLI. E: "Personal instructions configured on GitHub.com apply to GitHub Copilot Chat in GitHub. Other clients, such as Copilot CLI, use local files for personal instructions."

**Subagents (B):** "A custom agent spawned as a subagent ... doesn't receive repository instruction files (`copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`) by default. Set `include-custom-instructions: true` in its frontmatter to opt in".

---

## 2. Skills

**Locations (F):**

> For **project skills**, specific to a single repository, create a `.github/skills`, `.claude/skills`, or `.agents/skills` directory in your repository.
> For **personal skills**, shared across projects, create a `~/.copilot/skills` or `~/.agents/skills` directory in your local home directory.

(`~/.claude/skills` is not listed on any page checked.)

**Format (F):** "Skill files must be named `SKILL.md`." Frontmatter: "**name** (required) ... **description** (required) ... **license** (optional)". B adds optional `argument-hint`, `allowed-tools`, `user-invocable`, `disable-model-invocation`.

**When they load (F):** "When Copilot chooses to use a skill, the `SKILL.md` file will be injected in the agent's context". Also invoked as `/SKILL-NAME`. Reload with `/skills reload`.

**Priority (B, "Skill locations"):**

> Skills are loaded from these locations in priority order (first found wins for duplicate names).

Order: `.github/skills/` (Project), `.agents/skills/` (Project), `.claude/skills/` (Project), Parent `.github/skills/` (Inherited), `~/.copilot/skills/` (Personal), `~/.agents/skills/` (Personal), Plugin directories, `COPILOT_SKILLS_DIRS` (Custom), `--add-dir <path>` (Added root), (bundled with CLI) Built-in, then:

> | (org/enterprise) | Remote | Skills hosted by your organization or enterprise, projected via the AHP relay. Content is fetched on demand when the skill is invoked. |
> Remote skills are projected alongside local skills and follow the same name-based priority when a local skill has the same name.

C agrees: "Project-level skills take precedence over personal skills if they share the same name."

**Settings:** C user settings: `skillDirectories` "Additional directories to search for custom skill definitions (in addition to `~/.copilot/skills/`)"; `disabledSkills`; `ignoredSkillsLocations`.

**Commands (B):** "Commands are an alternative to skills stored as individual `.md` files in `.claude/commands/` ... Commands have lower priority than skills with the same name."

**CLI management (B):** `copilot skill add <source> [--project]` — "# Install a skill into the current project (.github/skills; file or URL skills only)".

---

## 3. MCP servers

**User config (B):** "Configure persistent servers in `~/.copilot/mcp-config.json`. Use `--additional-mcp-config` to add servers for a single session." `copilot mcp add` "Writes to `~/.copilot/mcp-config.json`." H: "In interactive mode, enter `/mcp add`."

**Project config (H):**

> | `.mcp.json` (in any directory from your working directory up to the repository root) | Local or per-checkout configuration; commonly placed at the project root |
> | `.github/mcp.json` | Shared configuration that is committed to the repository |

> If both `.mcp.json` and `.github/mcp.json` exist in the same directory, `.mcp.json` takes precedence. When server names conflict, definitions in files closer to your working directory take precedence. Project-level definitions also take precedence over those in `~/.copilot/mcp-config.json`.

> Project-level MCP servers are loaded only after you confirm folder trust on first launch. They are silently skipped in untrusted directories.

> The `.vscode/mcp.json` file for VS Code is not read by Copilot CLI.

**Loading priority (B):**

> 1. `--additional-mcp-config` option (highest)
> 2. Plugin-provided servers
> 3. Workspace servers—`.mcp.json` and `.github/mcp.json` loaded from the working directory upward to the Git root; requires the folder to be trusted
> 4. `~/.copilot/mcp-config.json` (lowest)

**DISAGREEMENT (minor):** K's precedence diagram for MCP lists only `~/.copilot/mcp-config.json` (lowest), plugin configs, `--additional-mcp-config` (highest); it omits workspace servers.

**Built-in GitHub MCP server (H):** "The GitHub MCP server is built into Copilot CLI and is already available without any additional configuration." B lists built-ins `github-mcp-server`, `playwright`, `fetch`, `time`; "Use `--disable-builtin-mcps` to disable all built-in servers".

**Org/enterprise MCP (H):** "If your organization or enterprise has configured a registry URL and allowlist policy, those settings apply to Copilot CLI."

R: "Enterprise and organization MCP policies apply to Copilot CLI."

B "Enterprise MCP allowlist": "This check is fail-closed ... Built-in default servers are always exempt from allowlist enforcement."

V (preview): "This feature is in public preview and is not the recommended method for restricting access to MCP servers. The more secure, generally available method is to define settings in your enterprise's `managed-settings.json` file."

W: "These lists are defined in your enterprise's `managed-settings.json`, which you can store on GitHub." Prerequisite: "the **MCP servers in Copilot** policy must be enabled".

C, managed keys: `allowedMcpServers` — "Leaving this key unset allows all non-default servers; an empty array denies all of them." "**Deny always wins**".

`/mcp search` is experimental (H): "The `/mcp search` command is currently an experimental feature."

---

## 4. Custom agents

**CLI locations and priority (B, "Custom agent locations"):**

> The CLI loads custom agents in the following priority order. When agents have the same ID, the first agent loaded is used.
> | 1 (highest) | User | `~/.copilot/agents/` |
> | 2 | Project | `.github/agents/`, from the current working directory upward to the Git root |
> | 3 | Project | `.claude/agents/`, from the current working directory upward to the Git root |
> | 4 | Added root | `.github/agents/` under a directory added with `--add-dir` ... |
> | 5 | Plugin | `<plugin>/agents/` |
> | 6 (lowest) | Remote | Organization or enterprise agents |

**ID (B):** "The CLI removes the `.agent.md` or `.md` extension and replaces directory separators with `--`. For example, `agents/team/reviewer.agent.md` has the ID `team--reviewer`." "The optional `name` frontmatter field does not control deduplication."

**User vs repo (I):** "If personal and repository custom agents have the same ID, the personal agent is used." C agrees: "the personal agent takes precedence."

**Org and enterprise paths (J):**

> | Organization-level custom agent | `/agents` directory in the organization's `.github` or `.github-private` repository | All projects within the organization |
> | Enterprise-level custom agent | `/agents` directory in the `.github-private` repository of an organization designated in enterprise settings. |

> In the case of naming conflicts (where agents share the same filename), a user-level agent overrides a repository-level agent, a repository-level agent overrides an organization-level agent, and an organization-level agent overrides an enterprise-level agent.

R: "Enterprise-configured custom agents are available to use with Copilot CLI."

**Invoking:** I: "In interactive mode, enter `/agent`." J: `copilot --agent=refactor-agent --prompt "Refactor this code block"`. B: "`--agent=AGENT` | Specify a custom agent to use."

Note: X (cheat sheet) gives the repo path as `.github/agents/AGENT-NAME.md`; CLI pages use `.agent.md` (B says both `.agent.md` and `.md` are accepted).

---

## 5. Plugins

**What a plugin bundles (L):** "Custom agents ... (`*.agent.md` files in `agents/`)", "Skills ... (skills subdirectories in `skills/`, containing a `SKILL.md` file)", "Hooks ... (a `hooks.json` file in the plugin root, or in `hooks/`)", "Extensions", "MCP server configurations", "LSP server configurations ... (an `lsp.json` file in the plugin root, or in `.github/`)". Manifest: "a `plugin.json` manifest file".

**Install (L):** "In Copilot CLI, you can install plugins using the `copilot plugin install` command or the `/plugin install` slash command, or by adding the plugin to the `enabledPlugins` field of either a user-level `~/.copilot/settings.json` file or a repository-level `.github/copilot/settings.json` file."

M: `copilot plugin install PLUGIN-NAME@MARKETPLACE-NAME`; `copilot plugin marketplace add OWNER/REPO`.

**Where stored (K):**

> | Installed plugins | `~/.copilot/installed-plugins/MARKETPLACE/PLUGIN-NAME` (installed via a marketplace) and `~/.copilot/installed-plugins/_direct/SOURCE-ID/` (installed directly) |
> | Marketplace cache | Platform cache directory: `~/.cache/copilot/marketplaces/` (Linux), `~/Library/Caches/copilot/marketplaces/` (macOS). Overridable with `COPILOT_CACHE_HOME`. |

**Precedence (K, "Loading order and precedence"):**

> * **Agents and skills** use first-found-wins precedence.
> If you have a project-level custom agent or skill with the same name or ID as one in a plugin you install, the agent or skill in the plugin is silently ignored. The plugin cannot override project-level or personal configurations.
> * **MCP servers** use last-wins precedence.
> If you install a plugin that defines an MCP server with the same server name as an MCP server you have already installed, the plugin's definition takes precedence.
> * **Built-in tools and agents** are always present and cannot be overridden by user-defined components.

**Repo-scoped plugin (C):** "A plugin enabled only through a repository's `enabledPlugins` is scoped to that repository: it auto-installs and activates in the declaring repository, but stays disabled globally".

**Default marketplaces — DISAGREEMENT:** M: "Copilot comes with one marketplace already registered by default: `awesome-copilot`." L lists "copilot-plugins (added by default)" and "awesome-copilot (added by default)".

**Enterprise (U):** "By configuring a `managed-settings.json` file, administrators can specify which plugin marketplaces are available to users and which plugins are installed automatically." C/K: "A plugin or marketplace pinned by an organization or MDM managed policy (`enabledPlugins`, `extraKnownMarketplaces`) can't be re-enabled, disabled, or repointed locally".

---

## 6. Settings, trust, permissions, hooks

**Config directory (C):** "By default, this directory is `~/.copilot` (that is, `$HOME/.copilot`)." "`COPILOT_HOME` replaces the entire `~/.copilot` path." `--config-dir` is "a legacy option" (B: "deprecated").

**settings.json vs config.json (C):**

> User-editable settings are stored in `settings.json`. These settings were originally stored in `config.json`. Any user settings in `config.json` are ignored. That file is used to store internal state, such as installed plugins and trusted folders.

**Precedence (C, "Configuration file settings"):**

> Settings are applied in this order (later overrides earlier):
> 1. Built-in defaults
> 2. Mobile Device Management (MDM) managed settings
> 3. User settings (`~/.copilot/settings.json`)
> 4. Repository settings (`.github/copilot/settings.json`)
> 5. Local settings (`.github/copilot/settings.local.json`)
> 6. Environment variables
> 7. Command-line flags

Caveat in the same section: "For most keys, user settings can override that baseline. For `permissions.disableBypassPermissionsMode`, an MDM value of `"disable"` always wins. Managed `sandbox` settings are another exception." Also S/C note "Most managed keys lock the entire row: a local edit is silently overridden by the managed value on the next load." (So the list order understates managed-setting strength.)

> | Local | `.github/copilot/settings.local.json` | Personal overrides (add this to `.gitignore`). |

> The CLI also reads `.claude/settings.json` and `.claude/settings.local.json` for the shared cross-tool subset of repository settings (such as `companyAnnouncements`, `disableAllHooks`, `enabledPlugins`, `extraKnownMarketplaces`, and `hooks`).

Repo keys are limited (C): "Only the keys listed in the following table are supported at the repository level. Any other keys ... are silently ignored." Supported: `companyAnnouncements`, `contextTier`, `deniedUrls`, `disableAllHooks`, `disabledMcpServers`, `disabledSkills`, `effortLevel`, `enabledPlugins`, `extraKnownMarketplaces`, `hooks`, `includeCoAuthoredBy`, `mergeStrategy`, `model`, `respectGitignore`. "`model`, `effortLevel`, and `contextTier` overrides only apply when the working directory is trusted."

Repo model allowlist (C): "a plain-text allowlist at `.github/allowed_models.txt`".

P: "**Settings managed by your repository or organization** are shown for reference, but their values come from those sources and override your personal value."

**Trusted folders (N):**

> When you start a GitHub Copilot CLI session, you'll be asked to confirm that you trust the files in, and below, the directory from which you launched the CLI.

> Trusted directories are stored in the automatically managed `config.json` file. ... Edit the contents of the `trustedFolders` array.

B: "`--trust-folder` | Trust the working directory's hooks, workspace MCP servers, and repository plugin settings for one new non-interactive session ... The trust is not saved to `trustedFolders`".

**Tool approvals (O):**

> When you approve a tool for the current location, the approval is saved to `permissions-config.json` in your configuration directory. By default, this file is `~/.copilot/permissions-config.json`.

> When you approve a URL permanently, its domain is added to the `allowedUrls` list in your `settings.json`.

> Command-line options such as `--allow-tool` and `--deny-tool` apply only to the current session and aren't written to `permissions-config.json`. Deny rules still take precedence over saved approvals.

> `--allow-all` or `--yolo` — Equivalent to using all of the `--allow-all-tools`, `--allow-all-paths`, and `--allow-all-urls` options ... Within an interactive session, you can use the `/allow-all` or `/yolo` slash commands

C: "`permissions-config.json` doesn't support deny rules, "ask" rules, default modes, URL rules, tool filtering, or repository-local shared policy."

Note: N's description of the approval prompt only shows "this time" and "for the rest of the running session" options; O describes the persisted "don't ask again in this repo" option. Treat O and C as current.

**Hooks (Q):**

> Hooks are loaded from the following sources in order (policy, then user, then project, then plugins) and combined. When the same event appears in multiple sources, all hook entries from all sources are run.

Sources: "Policy-level hook files", "`.github/hooks/*.json` in the repository root", "`~/.copilot/hooks/`", "the `hooks` field at the top level of `.github/copilot/settings.json` ... or `.github/copilot/settings.local.json` ... Cross-tool `.claude/settings.json` and `.claude/settings.local.json` files in the repository are also read", "the `hooks` field at the top level of `~/.copilot/settings.json`. The CLI no longer reads `~/.copilot/config.json` for hooks.", and plugin `hooks.json`.

Q, trust: "Repository and inherited-agent hooks require workspace admission."

---

## 7. Organization and enterprise controls

**R, "How do other AI controls affect Copilot CLI?"** Controls that apply: "Copilot CLI enablement" ("You can enable or disable Copilot CLI at the enterprise or organization level"), "Model selection" ("Users can only access AI models that are enabled at the enterprise level"), "Custom agents", "Content exclusion", "MCP server policies", "Copilot cloud agent enablement" (needed for `/delegate`), "Audit logging", "Seat assignment". Not applying: "**IDE-specific policies**".

R: "If you set the policy to "Enabled everywhere" or "Disabled everywhere," this overrides all organization-level settings." With "Let organizations decide", "Copilot CLI must be enabled in **at least one** of the organization granting them a GitHub Copilot license."

R: "users can also provide their own LLM keys locally. This is not controlled by enterprise policies."

O: "If you have a Copilot Business or Copilot Enterprise license, these commands may be blocked by an enterprise administrator." (allow-all options)

**Managed settings sources (C):** MDM plist `com.github.copilot`; files `/Library/Application Support/GitHubCopilot/managed-settings.json` (macOS), `%ProgramFiles%\GitHubCopilot\managed-settings.json` (Windows), `/etc/github-copilot/managed-settings.json` (Linux); registry `HKLM\SOFTWARE\Policies\GitHubCopilot`.

C: "Copilot CLI also loads server-managed settings at startup, in addition to MDM. ... MDM's value wins for any key it sets, and the server's value fills in keys MDM leaves unset." "Long-running sessions re-fetch and re-apply managed settings hourly".

**Server-managed location (T):** "In the `.github-private` repository, create a file at `copilot/managed-settings.json`." Team overrides in `copilot/teams/` mapped by `copilot/team-mappings.json`. "users on a supported client see the specified settings within about an hour."

C managed keys include `allowedMcpServers`, `deniedMcpServers`, `enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`, `model`, `autoTier`, `permissions` (`deny`/`ask`/`allow`, `limitTo`, `disableBypassPermissionsMode`), `sandbox`, `forceLoginOrgs`, `telemetry`. Rule order: "deny always wins, then ask, then allow".

---

## 8. Pages that explain how locations combine

- C ("GitHub Copilot CLI configuration directory") is the main reference: directory layout, settings precedence, repo/local settings, managed settings.
- B ("command reference"): instruction locations, MCP loading priority, skill locations, agent locations.
- K ("plugin reference", "Loading order and precedence"): diagram covering agents, skills, MCP.
- Q ("hooks reference"): hook sources.

## Preview / experimental notes

- V: registry-based MCP restriction "is in public preview".
- H: "`/mcp search` command is currently an experimental feature" (needs `--experimental` or `/experimental on`).
- B: "GitHub Copilot CLI extensions are currently an experimental feature and are subject to change." `/extensions`, `/after`, `/every` "Only available in experimental mode."
- B: "The experimental `/plugins` command was removed. Its resources have been moved to `/plugin`, `/mcp`, and `/skills`."
- C: `policyHelper` "The registration is accepted and validated, but the runtime doesn't yet invoke the helper".
- C/B: `--config-dir` deprecated; settings moved from `config.json` to `settings.json`; legacy `permissions-config` (no extension) still honored.
- No page states the CLI docs as a whole are in preview.

---

## 9. How a custom agent gets used (added by the editor, 22 October 2026)

Page: Invoking custom agents, https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents

> Using the slash command in the CLI's interactive interface to select from the list of available custom agents

> Calling out to the custom agent directly in a prompt: ... Copilot will automatically infer the agent you want to use.

> The AI model being used by the CLI can choose to delegate a task to a subsidiary subagent process ... that operates using a custom agent with specific expertise ... if it judges that this would result in the work being completed more effectively.

## 10. The CLI's own help (copilot 1.0.102, run 22 October 2026)

`copilot --help`, `copilot help config`, `copilot help permissions`, `copilot help environment`,
`copilot help commands`, and `copilot mcp|skill|plugin|instruction --help`.

> `copilot mcp --help`: Configuration is loaded from multiple sources: User ~/.copilot/mcp-config.json / Workspace .mcp.json or .github/mcp.json / Plugin Installed plugins with MCP servers

> `copilot skill --help`: Project .github/skills/, .agents/skills/, or .claude/skills/ / Personal ~/.copilot/skills/ or ~/.agents/skills/ / Plugin Installed plugins that bundle skills

> `copilot help config`: Use --repo or --local to change .github/copilot/settings.json or settings.local.json.

> `copilot help config`: `trustedFolders`: list of folders where permission to read or execute files has been granted.

> `copilot help environment`: `COPILOT_HOME`: override the directory where configuration and state files are stored; defaults to `$HOME/.copilot`.

> `copilot help permissions`: Denial rules always take precedence over allow rules, even --allow-all-tools.

> `copilot help commands`: /env Show loaded environment details (instructions, MCP servers, skills, agents, hooks, plugins, LSPs, extensions)

> `copilot help commands`: /instructions View and toggle custom instruction files

> `copilot instruction --help`: Inspect the instruction sources a session would load.
