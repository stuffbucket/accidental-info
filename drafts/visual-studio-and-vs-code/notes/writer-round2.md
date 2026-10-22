# Writer instructions, round 2: targeted edits

Edit `packages/accidental-guides/guides/visual-studio-and-vs-code/guide.md` in place. Line
numbers refer to the file as it is now (196 lines). Apply every edit below, then stop. Don't
change anything that isn't listed. Keep every heading, id and table shape.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

The rules from `writer-round1.md` still apply (no `<`, `>`, `&`, backticks, lists, em dashes,
“e.g.”; Short answer cells don't end with a full stop; the first sentence of What and So what
is printed bold, so each of those cells needs at least two sentences). Facts only from
`drafts/visual-studio-and-vs-code/notes/sources.md`.

Length: the printed guide is about 1,365 words and must come down to about 1,150 after the new
page is added. Each entry should end up about 75 words. Prefer fewer, fuller sentences over
clipped ones; the draft reads a little staccato in places.

## Page 2, lines 13–17

Rewrite the three paragraphs as two. The first paragraph is shown on its own on the website,
so it must answer the title in plain words. Something close to this, in your words:

“You can set up five things for GitHub Copilot’s agent in VS Code: instructions files, custom
agents, skills, MCP servers and settings. Each one is a file or a setting, and each can belong
to a repo, to you, or to your organization.”

Second paragraph: explain calmly why the locations feel scattered and how to read the rest.
VS Code can run more than one harness, and each harness reads its own folders. The default,
the Copilot harness, reads .github/ in the repo and ~/.copilot/ in your home folder, and
everything here describes that harness unless a page says otherwise. End with one sentence
pointing to An Accidental Guide to: Agents, Harnesses, Skills, and Tools for the basics.

Lines 21–25, the table: keep it, but make each meaning say what you'd use it for, in about
8–12 words. Line 25 (Setting): “A switch in VS Code that turns features on and chooses what’s read.”

## Instructions file, lines 31–44

- Line 32 What: two sentences. First: an instructions file is text Copilot adds to your
  requests. Second: .github/copilot-instructions.md and AGENTS.md apply to every request, and a
  .instructions.md file can apply only to files that match its applyTo pattern.
- Line 33 So what: first sentence: put the rules you’d otherwise repeat in every chat here.
  Second: when one seems ignored, check the file’s location and its applyTo pattern.
- Line 39: Short answer “Every request, or when files match”. Detail: “Files with a
  description can also load when the task matches.”
- Line 40: keep the meaning; Detail: “Every file that applies is added, and none outranks
  another.”

## Custom agent, lines 50–63

- Line 50 Identify by: “A .agent.md file in .github/agents/, or a name in the Agent dropdown.”
- Line 51 What: first sentence: a custom agent is a saved role with its own instructions, tools
  and model. Second: you pick it from the Agent dropdown, and another agent can also start it
  as a sub-agent.
- Line 52 So what: first sentence: limiting a custom agent’s tools limits what it can change.
  Second: a planning or review agent can be set to read and search only.
- Line 58: Short answer “When you pick it, or when another agent starts it”. Detail: “Its
  instructions are added to your instructions files and win if the two conflict.”
- Line 59: Short answer “Switch off instructions files”. Detail: “Every instructions file that
  applies still loads.”
- Line 63: “An instructions file applies to every request. A custom agent applies only while
  it’s selected or running. Custom agents used to be called chat modes, and old .chatmode.md
  files can be renamed to .agent.md.”

## Skill, lines 69–82

- Line 70 What: “A skill is a written procedure in a folder. Only its name and description load
  at first. The rest of SKILL.md loads when your request matches the description, or when you
  type /skill-name.”
- Line 71 So what: “A skill can hold long steps without taking up room until it’s needed. When a
  skill doesn’t run, check its description first.”
- Line 77: Short answer “Name and description first”. Detail: “The steps load when used, and
  other files in the folder only when a step reads them.”
- Line 78: keep.
- Line 82: “A prompt file, .github/prompts/*.prompt.md, is a saved prompt you run with
  /name. Prompt files run only in the Local harness, and VS Code suggests a skill instead
  for other harnesses.”

## MCP server, lines 88–101

- Line 88 Identify by: “An entry with a command or a URL in .mcp.json or
  ~/.copilot/mcp-config.json.”
- Line 89 What: “An MCP server is a separate program that gives the agent more tools. The
  harness starts or connects to the server and passes the model’s tool calls to it.”
- Line 90 So what: “A local MCP server can run code on your machine with your permissions.
  Only add servers you trust, and expect your organization to limit which ones you can use.”
- Line 96: Short answer “When the session starts”. Detail: “The server’s tools are offered
  to the model.”
- Line 99 heading: change to “## Confused with: Extension”.
- Line 101: “An extension adds features to VS Code itself. MCP servers are listed in the same
  Extensions view: search @mcp, then choose Install for yourself or Install in Workspace for
  the repo.”

## Setting, lines 107–120

- Line 107 Identify by: “A value in the Settings editor, in your user settings or in
  .vscode/settings.json.”
- Line 108 What: two sentences. First: a setting is a switch or value that changes how VS Code
  behaves. Second: Copilot settings turn features on and off, such as
  chat.useAgentSkills for skills. (Don't use a longer setting name; long names don't fit the line.)
- Line 109 So what: first sentence: when something works for a teammate and not for you, compare
  settings. Second: your user settings can differ from theirs even in the same repo.
- Lines 115–116: keep.
- Line 120: “A setting decides what VS Code does. An instructions file tells the agent how to
  work.”

## Where things live, lines 124–148

- Line 124: “The Copilot harness reads these places. Choose the narrowest scope that fits:
  the repo for the team, your home folder for yourself.”
- Lines 133, 143, 146: write “Organization” in full in the Scope column (the column is now wider).
- Line 133 Location: “Copilot settings in your GitHub organization”.
- Line 136 Location: “agents/ in the organization’s .github-private repo”.
- Lines 137–140 (Skill): use only Copilot’s folders. Repo: “.github/skills/” and on the next row
  “.agents/skills/”. You: “~/.copilot/skills/” and on the next row “~/.agents/skills/”.
- Line 143 Location: “A registry of approved servers, set in GitHub”.
- Line 145 Location: “User settings, opened with Preferences: Open User Settings”.
- Line 146 Location: “Policies set by an administrator”.
- Line 148: “The Local harness reads older places too: .vscode/mcp.json, files kept in your VS
  Code profile, and folders added through chat settings. The Claude harness reads .claude/ and
  ~/.claude/ instead.”

## How scopes combine, lines 152–162

- Line 152: “Instructions add up, and settings override. Everything else is offered from every
  scope at once.”
- Line 157: “All are offered in the Agent dropdown. The selected agent’s instructions win over
  instructions files that conflict.”
- Line 158: “All are offered, and each loads when your request matches or you name it.”
- Line 159: “All servers are added. Nothing decides between two with the same name, so give
  each a unique one. Your organization can limit which servers run.”
- Line 160: “The later scope wins: Default, then User, then Workspace. Policies set by an
  administrator win over all of them.”
- Line 162: “When two instructions files disagree, change the files so they agree. Neither the
  folder nor the load order settles it.”

## What’s different in Visual Studio, lines 166–177

- Line 166: “Visual Studio reads many of the same files, but not all of them, and its settings
  live in Tools › Options instead of settings.json.”
- Line 170: “.github/copilot-instructions.md and .github/instructions/*.instructions.md. In
  Visual Studio 2026, personal instructions go in %USERPROFILE%/copilot-instructions.md.”
- Line 171: “.github/prompts/*.prompt.md. Type / or #prompt: in chat to use one.”
- Line 172: “.github/agents/*.agent.md, or %USERPROFILE%\.github\agents for your own. Needs
  version 18.4 or later.”
- Line 173: “The same folders as VS Code. Needs version 18.5 or later.”
- Line 174: “Reads %USERPROFILE%\.mcp.json, then these in the solution folder: .vs\mcp.json,
  .mcp.json, .vscode\mcp.json and .cursor\mcp.json. Find servers in Extensions › MCP
  Registries…”
- Line 175: “Tools › Options › GitHub › Copilot. Instructions files load only when the option to load
  custom instructions is checked there.”
- Line 177: “AGENTS.md isn’t listed as supported in Visual Studio as of October 2026, so keep
  rules you need in both editors in .github/copilot-instructions.md.”

## New page: Same thing elsewhere (insert after line 177, before “# Sources”)

Add this section, with your own plain wording for the two paragraphs and the facts exactly as
given in the table cells:

```
# Same thing elsewhere {#elsewhere}

(one short paragraph: the other agent tools have the same five kinds of thing, in their own
places. Copilot CLI uses the same Copilot harness as VS Code, so it reads the same .github/
and ~/.copilot/ folders, except that it doesn’t run prompt files.)

| Thing | In the other tools |
|---|---|
| Instructions file | Claude Code: CLAUDE.md. Codex: AGENTS.md. Claude Desktop: project instructions. |
| Custom agent | Claude Code: .claude/agents/. Codex: .codex/agents/. |
| Skill | Claude Code: .claude/skills/. Codex: .agents/skills/. Claude Desktop: Customize › Skills. |
| MCP server | Claude Code: .mcp.json. Codex: ~/.codex/config.toml. Claude Desktop: Customize › Connectors. |
| Setting | Claude Code: .claude/settings.json. Codex: ~/.codex/config.toml. |

(exactly one closing paragraph naming the guides in colon form, joined plainly: An Accidental
Guide to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to: GitHub
Copilot CLI and An Accidental Guide to: Codex.)
```

## Sources, lines 183–196

Keep the header row. Use “VS Code” as the publisher for code.visualstudio.com pages, “Microsoft
Learn” for learn.microsoft.com, “GitHub Docs” for docs.github.com. Drop the rows for “Agent
customization concepts” and “Agent skills in Visual Studio”. Add these rows at the end:

```
| Customization cheat sheet | GitHub Docs | docs.github.com/en/copilot/reference/customization-cheat-sheet |
| Claude Code settings | Anthropic | code.claude.com/docs/en/settings |
| Use Skills in Claude | Anthropic | support.claude.com/en/articles/12512180 |
| Codex configuration basics | OpenAI | learn.chatgpt.com/docs/config-file/config-basic |
```
