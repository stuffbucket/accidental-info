# Writer instructions, round 3: cuts and the order of config files

Apply these edits in place to packages/accidental-guides/guides/codex/guide.md. Line numbers
refer to the file as it is now. Use the wording given; don't change anything else.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Why: the guide prints about 1,480 words and should be close to 1,150. These edits cut detail,
not clarity. They also move the order of config files out of a crowded table cell into a small
table of its own, which the builder now prints above the main table on the combine page.

## Page 2

- L15: Most of these files live in your Codex home folder, ~/.codex unless CODEX_HOME says otherwise, or in your project. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains the basics.
- L21: A program that gives Codex tools for another system.

## Entries

- L30 What: An instructions file holds guidance Codex should always have, such as build and test commands and project conventions. Keep it short, since Codex reads all of it every session.
- L37 Loads detail: Yours first, then the project’s.
- L49 What: A skill is a written procedure for one kind of task. Codex reads its name and description at the start, and the rest when your task matches the description or you type $ and the skill’s name.
- L50 So what: You can keep many skills without crowding the session. A project’s skills in .agents/skills/ reach everyone who works on it.
- L56 Loads detail: Name and description at the start, steps when used.
- L61: A plugin packages skills, MCP servers and hooks to install together, using /plugins in the CLI. As of October 2026, the IDE extension doesn’t support plugins.
- L68 What: An MCP server is a program that gives Codex tools for another system. The entry gives a command that starts it on your computer, or the url of a remote one.
- L69 So what: Set a server up once and it works in the CLI, the IDE extension and the desktop app. enabled_tools and disabled_tools limit which of its tools Codex sees.
- L87 What: The config file holds Codex settings, such as the model, MCP servers and permissions, as keys and values in TOML. In the IDE extension, open it from the gear icon, then Codex Settings.
- L88 So what: Your own config.toml applies everywhere, and a project’s .codex/config.toml changes settings for that project. A profile file, such as ~/.codex/deep-review.config.toml, holds a set of changes you pick with --profile.
- L106 What: Permissions are two settings. The sandbox decides what commands can touch: read-only, workspace-write for your working folder, or danger-full-access. The approval policy, on-request or never, decides when Codex stops to ask.
- L107 So what: The sandbox keeps a wrong command away from everything outside your work. In a Git folder Codex starts with workspace-write and on-request, and elsewhere read-only.
- L113: replace the row with: | Network | Off by default | Turn it on with network_access under sandbox_workspace_write. |
- L118: Rules files in ~/.codex/rules/ say whether a command may run outside the sandbox: allow, prompt or forbidden. Rules are experimental as of October 2026.

## Where things live

- L122: Your own files apply in every project. A project’s files travel with its repository.  (keep)
- Delete L129 (Profiles) and L136 (This project, Plugins).
- L128 path: ~/.codex/config.toml, which also holds MCP servers and permissions; profiles sit beside it  (keep the path exactly ~/.codex/config.toml)
- L132 path: AGENTS.md in any folder
- L133 path: .agents/skills/ in any folder
- L134 path: .codex/config.toml
- L140 path: Settings, Codex Cloud, Environments
- L143: Codex reads a project’s .codex folder only after you trust the project, so a repository you just cloned can’t change your settings, hooks or rules.

## How do the places combine?

- L147: For a config file setting, the first place on this list that sets a value wins.
- Insert directly after L147 (with a blank line before and after) this new table:

| Config file | Where the value comes from, strongest first |
|---|---|
| 1 | A flag or -c on the command line |
| 2 | The project’s .codex/config.toml closest to where you work |
| 3 | A profile picked with --profile |
| 4 | Your ~/.codex/config.toml |
| 5 | Your organization’s defaults |
| 6 | Codex’s built-in defaults |

- Change the main table's header (L149) to: | Other setup | When two places set it |
- Delete L151 (the Config file row).
- L152: Codex joins them, yours first, then the project’s from the root down, so the closest file has the last word. AGENTS.override.md replaces AGENTS.md in its folder. The total stops at 32 KiB by default.
- L153: Codex offers all of them. Two with the same name both appear.
- L154: Servers can be in your config.toml or a project’s, and a setting for the same server follows the order above.
- L155: They add up, so a stronger place doesn’t replace a weaker one’s hooks.
- L156: When two rules match a command, the strictest wins: forbidden, then prompt, then allow.
- L157: Limits an administrator sets. Your files can’t override them.
- L159: When a setting isn’t what you expect, check the places in order, starting at the top.

## Same thing elsewhere

- L173: The details are in An Accidental Guide to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to: GitHub Copilot CLI, and An Accidental Guide to: VS Code and Visual Studio.

When done, build with
`cd packages/accidental-guides && .venv/bin/python guides/codex/build_guide.py /tmp/codex-r3.pdf`
and confirm "no overflow". Don't touch any other file.
