# Writer instructions, round 2: targeted edits to guide.md

Apply these edits in place to packages/accidental-guides/guides/codex/guide.md. Line numbers
refer to the file as it is now. Use the suggested wording as given unless a builder rule in
writer-round1.md would break; don't change anything else. Keep every table's shape, the
section ids and the number of paragraphs per section.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Why: round 1 was cut so hard it reads staccato and uses vague stand-ins ("connections to other
systems", "command limits", "three Codex apps", "contain unwanted commands"). These edits put
back plain connected sentences at about the same length.

## Page 2 (why)

- L13: You can give Codex standing instructions, skills, MCP servers, settings and permissions. Each one is a plain file, and the Codex CLI, the IDE extension and the ChatGPT desktop app all read the same files.
- L15: Most of the files live in two places: your Codex home folder, which is ~/.codex unless CODEX_HOME says otherwise, and your project. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains the basics.
- L20 Skill: Steps for one kind of task, read when the task comes up.
- L22 Config file: The file that holds settings such as the model and MCP servers.
- L23 Permissions: What commands may change, and when Codex stops to ask you.

## Instructions file

- L29 Identify by: AGENTS.md, in ~/.codex/ or anywhere in a project.
- L30 What: An instructions file holds guidance Codex should always have. Build and test commands and project conventions belong here. Keep it short, since Codex reads all of it every session.
- L31 So what: Put guidance in the folder it’s about. Codex reads from the project root down to your folder, so the file closest to your work has the last word.
- L37 Loads: short answer "At the start of a session", detail "~/.codex/AGENTS.md first, then the project’s files."
- L42: Codex reads an instructions file every session. A skill’s steps are read only when the skill is used.

## Skill

- L48: A folder with a SKILL.md file.
- L49 What: A skill is a written procedure for one kind of task. SKILL.md starts with a name and a description, and Codex reads the rest only when your task matches the description or you type $ and the skill’s name.
- L50 So what: You can keep many skills without crowding the session. Yours go in ~/.agents/skills/, and a project’s go in .agents/skills/, so everyone on the project gets them.
- L56 Loads: short answer "In two steps", detail "The name and description at the start, the steps when the skill is used."
- L57 Check with: short answer "/skills", detail "Shows the skills you can use."
- L61: A plugin packages skills, MCP servers and hooks so they install together. In the CLI, /plugins opens the plugin browser. As of October 2026, the IDE extension doesn’t support plugins.

## MCP server

- L67: A [mcp_servers.docs] table in config.toml.
- L68 What: An MCP server is a program that gives Codex tools for another system. The entry gives either a command that starts the server on your computer or the url of a remote one.
- L69 So what: Set a server up once and it works in the CLI, the IDE extension and the desktop app. enabled_tools and disabled_tools choose which of its tools Codex sees.
- L75 detail: Writes the entry into config.toml for you.
- L76 detail: Shows the servers Codex is connected to.
- L80: The MCP server is the program. The tools it offers are what Codex calls.

## Config file

- L86: config.toml, in ~/.codex/ or in a project’s .codex/ folder.
- L87 What: The config file holds Codex settings in TOML, a plain format of keys and values. The model, MCP servers, permissions and feature flags all go here. In the IDE extension, open it from the gear icon, then Codex Settings, then Open config.toml.
- L88 So what: Your ~/.codex/config.toml applies to every project on your computer, and a project’s .codex/config.toml changes settings for that project. A profile file, such as ~/.codex/deep-review.config.toml, holds a set of changes you pick with --profile.
- L94 Loads: short answer "At the start", detail "Restart Codex after a change."
- L95 Override with: short answer "-c", detail "-c key=value changes one setting for one run."
- L99: Your config.toml sets defaults you can change. An administrator’s requirements.toml sets limits you can’t.

## Permissions

- L106 What: Permissions are two settings. The sandbox decides what commands can touch: read-only, workspace-write for the folder you’re working in, or danger-full-access. The approval policy, on-request or never, decides when Codex stops to ask.
- L107 So what: The sandbox keeps a wrong command away from files outside your work. In a Git folder Codex starts with workspace-write and on-request, and elsewhere it starts read-only.
- L113: replace the row with Field "Network", short answer "Off by default", detail "network_access = true under [sandbox_workspace_write] turns it on."
- L114: short answer "/permissions", detail "During a session, or start Codex with --sandbox and --ask-for-approval."
- L118: Rules files in ~/.codex/rules/ say whether a command may run outside the sandbox: allow, prompt or forbidden. As of October 2026, rules are experimental.

## Where things live

- L122: Your own files apply in every project. A project’s files travel with its repository.
- L143: Codex reads a project’s .codex folder only after you trust the project, so a repository you just cloned can’t change your settings, hooks or rules. Your own files and your organization’s still load.

## How do the places combine?

- L147: For a setting, one value wins. Most other kinds of setup add up.
- L151: One value wins. From strongest: a flag or -c, the project’s .codex/config.toml closest to where you work, a profile, your ~/.codex/config.toml, your organization’s defaults, then built-in defaults.
- L152: Codex joins them: ~/.codex/AGENTS.md first, then the project’s files from the root down, so a later file has the last word. In each folder AGENTS.override.md replaces AGENTS.md. Codex stops at 32 KiB in total by default.
- L153: Codex offers all of them. Two skills with the same name both appear.
- L154: Servers can be in your config.toml or a project’s. A setting for the same server follows the config file order, so -c mcp_servers.docs.enabled=false turns one off for a run.
- L155: They add up. A hook in a stronger place doesn’t replace one in a weaker place.
- L156: Codex reads every rules/ folder. When two rules match a command, the strictest wins: forbidden, then prompt, then allow.
- L157: Limits an administrator sets. Your files can’t override them, and Codex uses an allowed value and tells you.
- L159: When a setting isn’t what you expect, look from the strongest place down: the command line, the project’s .codex/config.toml, your profile, then your own config.toml.

## Same thing elsewhere

- L163: Other coding tools have the same kinds of setup under their own names.
- L165: header row becomes: | Codex | Claude Code | Claude Desktop | Copilot CLI | VS Code and Visual Studio |
- L167–171: replace the five rows with:
  | Instructions file | Instructions file | Instructions | Instructions file | Instructions file |
  | Skill | Skill | Skills | Skill | Skill |
  | MCP server | MCP server | Connectors | MCP server | MCP server |
  | Config file | Settings | Settings | Settings | Setting |
  | Permissions | Settings | Settings and permissions | Settings | Setting |
- L173: Each one has its own guide: An Accidental Guide to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to: GitHub Copilot CLI, and An Accidental Guide to: VS Code and Visual Studio.

When done, build with
`cd packages/accidental-guides && .venv/bin/python guides/codex/build_guide.py /tmp/codex-r2.pdf`
and confirm "no overflow". Don't touch expected.sha256 or any other file.
