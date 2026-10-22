# Codex: where configuration lives (source notes)

Checked 22 October 2026. The old addresses under developers.openai.com/codex now return
308 redirects to learn.chatgpt.com/docs/… (for example developers.openai.com/codex/config-basic
→ learn.chatgpt.com/docs/config-file/config-basic). The openai/codex repo's docs/config.md,
docs/skills.md, docs/agents_md.md and docs/sandbox.md now only link to those pages. Excerpts
below are short and verbatim unless marked as a summary.

## Pages

| Key | Title | Address |
|---|---|---|
| A | Config basics | learn.chatgpt.com/docs/config-file/config-basic |
| B | Advanced Configuration | learn.chatgpt.com/docs/config-file/config-advanced |
| C | Custom instructions with AGENTS.md | learn.chatgpt.com/docs/agent-configuration/agents-md |
| D | Build skills | learn.chatgpt.com/docs/build-skills |
| E | Model Context Protocol | learn.chatgpt.com/docs/extend/mcp |
| F | Agent approvals and security | learn.chatgpt.com/docs/agent-approvals-security |
| G | Permissions (beta permission profiles) | learn.chatgpt.com/docs/permissions |
| H | Customization | learn.chatgpt.com/docs/customization/overview |
| I | Plugins | learn.chatgpt.com/docs/plugins |
| J | Package your plugin | developers.openai.com/plugins/build/plugins |
| K | Hooks | learn.chatgpt.com/docs/hooks |
| L | Rules | learn.chatgpt.com/docs/agent-configuration/rules |
| M | Subagents | learn.chatgpt.com/docs/agent-configuration/subagents |
| N | Cloud environments | learn.chatgpt.com/docs/environments/cloud-environments |
| O | Environment variables | learn.chatgpt.com/docs/config-file/environment-variables |
| P | Managed configuration | learn.chatgpt.com/docs/enterprise/managed-configuration |
| Q | Developer settings (IDE) | learn.chatgpt.com/docs/developer-settings?surface=ide |
| R | Slash commands | learn.chatgpt.com/docs/reference/slash-commands |
| S | Developer commands | learn.chatgpt.com/docs/developer-commands?surface=cli |
| T | openai/codex docs folder | github.com/openai/codex/tree/main/docs |

## Config file and layers (A, B)

- A: "Your personal defaults live in `~/.codex/config.toml`, and you can add project overrides
  with `.codex/config.toml` files."
- A: "System config (if present): `/etc/codex/config.toml` on Unix"
- A, precedence, highest first (summary with quoted parts): 1 "CLI flags and `--config`
  overrides"; 2 project `.codex/config.toml` files "ordered from the project root down to your
  current working directory" "(closest wins; trusted projects only)"; 3 "`--profile
  profile-name` (`~/.codex/profile-name.config.toml`)"; 4 user `~/.codex/config.toml`;
  5 "Cloud-managed `config.toml` defaults, when delivered for the signed-in workspace";
  6 system `/etc/codex/config.toml`; 7 "Built-in defaults".
- A: "For security, Codex loads project `.codex/` layers only when you trust the project."
  "Codex skips project-scoped `.codex/` layers, including project-local config, hooks, and
  rules." "User and system config still load."
- A: "Requirements constrain behavior; configuration values provide defaults."
- A: "The CLI and IDE extension share the same configuration layers." In the IDE: "Codex
  Settings > Open config.toml".
- B, profiles: Codex "loads `~/.codex/config.toml`, then overlays
  `~/.codex/profile-name.config.toml`". Use top-level keys and "don't nest them under
  `[profiles.profile-name]`". From 0.134.0, `--profile` no longer reads `[profiles.*]`, and
  "the top-level `profile = "profile-name"` selector is no longer supported". Project
  `.codex/config.toml` ignores `profile` and `profiles` keys.
- B: "Use `-c` / `--config` when you need to override an arbitrary key." Value "is TOML, not
  JSON". Example: `mcp_servers.context7.enabled=false`.
- B: "Codex stores its local state under `CODEX_HOME` (defaults to `~/.codex`)." Files:
  `config.toml`, `auth.json` (or OS keychain), `history.jsonl`, logs and caches.
- B: project root is a directory containing `.git` by default; `project_root_markers`.

## Instructions: AGENTS.md (C, H, R)

- C, global: "In your Codex home directory (defaults to `~/.codex`, unless you set
  `CODEX_HOME`)". Reads `AGENTS.override.md` if present, otherwise `AGENTS.md`. "Codex uses
  only the first non-empty file at this level."
- C, project: "Starting at the project root (typically the Git root), Codex walks down to your
  current working directory." In each directory "it checks for `AGENTS.override.md`, then
  `AGENTS.md`, then any fallback names in `project_doc_fallback_filenames`". "Codex includes
  at most one file per directory."
- C: "Codex concatenates files from the root down, joining them with blank lines." "Files
  closer to your current directory override earlier guidance because they appear later in the
  combined prompt." Built once per run or TUI session.
- C: stops "once the combined size reaches the limit defined by `project_doc_max_bytes` (32 KiB
  by default)".
- H: AGENTS.md is "durable project guidance that travels with your repository and applies
  before the agent starts work. Keep it small."
- R: `/init`: "Generate an `AGENTS.md` scaffold for the current project."

## Skills (D, H, N)

- D: Codex reads skills from "repository, user, admin, and system locations". It "scans
  `.agents/skills` in every directory from your current working directory up to the
  repository root."
- D table: REPO `$CWD/.agents/skills`, `$CWD/../.agents/skills`, `$REPO_ROOT/.agents/skills`;
  USER `$HOME/.agents/skills`; ADMIN `/etc/codex/skills`; SYSTEM "Bundled with Codex by
  OpenAI."
- D: "In Codex CLI or the IDE extension, run `/skills` or type `$` to mention a skill."
  Implicit: "when your task matches the skill `description`."
- D: `SKILL.md` "must include `name` and `description`".
- D: disable with `[[skills.config]]` `path = "/path/to/skill/SKILL.md"` `enabled = false` in
  `~/.codex/config.toml`. "Restart Codex after changing `~/.codex/config.toml`."
- D: same names: "Codex doesn't merge them; both can appear in skill selectors."
- H: Codex "loads `SKILL.md` only when a skill is chosen."
- N: "Skills stored in your repository are available in cloud tasks." "Personal skills from
  your local computer aren't synced."

## MCP servers (E, R, S)

- E: "By default this is `~/.codex/config.toml`, but you can also scope MCP servers to a
  project with `.codex/config.toml` (trusted projects only)."
- E: "Configure each MCP server with a `[mcp_servers.<server-name>]` table in the
  configuration file."
- E: "The ChatGPT desktop app, Codex CLI, and IDE extension share this configuration." ChatGPT
  web "doesn't read local Codex configuration files".
- E: `codex mcp add context7 -- npx -y @upstash/context7-mcp`; `codex mcp list`;
  `codex mcp login <server-name>`.
- E: STDIO `command` (required); HTTP `url` (required), `bearer_token_env_var`.
- E: `enabled_tools` "Tool allow list"; `disabled_tools` "Tool deny list (applied after
  `enabled_tools`)".
- R: `/mcp`: "Open MCP status to view connected servers."

## Sandbox and approvals (F, G, S)

- F: "Sandbox mode" controls what Codex can technically do; "Approval policy" controls when
  Codex must stop and ask. "the agent runs with network access turned off" by default.
- F: modes `read-only`, `workspace-write`, `danger-full-access`. Read-only paths inside
  writable roots: `.git`, `.agents`, `.codex`, `.aws`.
- F: `on-request`: Codex "asks for approval to edit files outside the workspace or to run
  commands that require network access." `never`. `granular`.
- F: "Codex and ChatGPT Work no longer support `approval_policy = "untrusted"`."
- F config: `approval_policy = "on-request"`, `sandbox_mode = "read-only"`,
  `[sandbox_workspace_write] network_access = true`.
- F flags: `--sandbox <mode>`, `--ask-for-approval <policy>` (`-a never`). Auto preset
  `--sandbox workspace-write --ask-for-approval on-request`. `--yolo` = no sandbox, no
  approvals, "not recommended".
- F: switch to `read-only` "with the `/permissions` command".
- F: version-controlled folders get Auto (workspace write plus on-request); others
  `read-only`. "Codex may also start in `read-only` until you explicitly trust the working
  directory."
- F, cloud: Codex Cloud (Legacy) "Secrets configured for cloud environments are available only
  during setup and are removed before the agent phase starts." CLI and IDE sandbox uses
  Seatbelt on macOS, bwrap plus seccomp on Linux.
- G (beta): permission profiles `:read-only`, `:workspace`, `:danger-full-access`,
  `default_permissions`, `[permissions.<name>]`. Profiles "do not compose with the older
  sandbox settings". Not used in the guide beyond a mention, because it's beta.
- S: `--ask-for-approval` (`on-request | never`).

## Plugins (I, J)

- I: "Plugins bundle capabilities into reusable workflows in ChatGPT and Codex." Parts:
  skills, MCP servers, browser extensions, hooks.
- I: CLI: "enter `/plugins` to open the plugin browser." "The IDE extension doesn't support
  plugins."
- J: marketplaces "`$REPO_ROOT/.agents/plugins/marketplace.json` for a repo-scoped list or
  `~/.agents/plugins/marketplace.json` for a personal list". Installed into
  "`~/.codex/plugins/cache/$MARKETPLACE_NAME/$PLUGIN_NAME/$VERSION/`".
- J: `[plugins."my-plugin@local-repo"] enabled = true` in the repo's `.codex/config.toml`.
  "Choices made in the plugin browser are stored in `~/.codex/config.toml`."
- H: "Skills remain the authoring format; plugins are the installable distribution unit."

## Hooks, rules, custom agents (K, L, M)

- K: hooks in "`hooks.json`" or "inline `[hooks]` tables inside `config.toml`"; user
  `~/.codex/hooks.json`, project `<repo>/.codex/hooks.json`. "Higher-precedence config layers
  don't replace lower-precedence hooks." "Hooks are enabled by default." "Non-managed hooks
  must be reviewed and trusted before they run." `/hooks`.
- L: rules "control which commands Codex can run outside the sandbox." "Rules are
  experimental and may change." `~/.codex/rules/default.rules`; "Project-local rules under
  `<repo>/.codex/rules/` load only when the project `.codex/` layer is trusted." Strictest
  wins "(`forbidden` > `prompt` > `allow`)".
- M: "add standalone TOML files under `~/.codex/agents/` for personal agents or
  `.codex/agents/` for project-scoped agents."

## Codex Cloud (N, F)

- N: "Codex Cloud runs coding tasks in the cloud, so work can continue while your computer is
  asleep." Settings at "Settings > Codex Cloud > Environments". Environment: install script,
  start skill, environment variables and network secrets, "Allow Codex to access internet"
  with presets. "Each cloud task runs in a VM".
- N: Codex Cloud (Legacy) still handles Code Review and Linear and GitHub integrations; "We
  plan to deprecate this experience."

## Environment and managed config (O, P)

- O: `CODEX_HOME` default `~/.codex`, used by "CLI, IDE extension, app-server, and
  installers". "Sets the root for Codex state, including config, auth, logs, sessions,
  skills, and standalone package metadata."
- P: requirements "`/etc/codex/requirements.toml` on Unix systems, including Linux and macOS";
  "`%ProgramData%\OpenAI\Codex\requirements.toml` on Windows"; cloud bundle; macOS MDM.
  Requirements: if a user value conflicts, "the local client falls back to a compatible value
  and notifies the user."

## IDE extension (Q)

- Q: Codex settings in `config.toml` cover "the model, reasoning effort, permissions,
  sandbox, MCP servers, and personalization". Editor settings use "`chatgpt.*` keys in the
  editor's settings system" and "don't go in `config.toml`". Open: "Select the gear icon in
  the Codex sidebar, then select **Codex Settings**", then "**Open config.toml**".
