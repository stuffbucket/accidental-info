# Writer instructions, round 2: GitHub Copilot CLI

Edit `./guide.md` in place. Apply the edits below by line number (line numbers are from the file
as it is now; work from the bottom up so they stay right). The proposed wording is checked
against `drafts/copilot-cli/notes/sources.md`; use it as given, or smooth it lightly
for flow, but don't add facts or change paths. Keep the format rules from writer-round1.md.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

## What's wrong with round 1

The text was cut too hard. The entries read like notes: short clipped sentences that don't
connect ("Both show skills." "Applicable files combine."), and a newcomer can't tell why any of
it matters. The author wants pocket-sized without being staccato: connected sentences, one idea
building on the last, the way a colleague would explain it. Round 2 makes page 2 and the five
entries fuller and plainer, and fixes three facts on the combine page.

## Edits

Lines 13-17 (page 2 intro). Replace both paragraphs with:

> Copilot CLI reads its setup from files. There are five kinds: instructions files, skills, MCP
> servers, custom agents and settings. Each kind can sit in your home folder, in the repository
> you’re working in, or come from your organization, and when two copies disagree, Copilot CLI
> has a rule for which one wins.
>
> The words agent, skill, tool and session are explained in An Accidental Guide to: Agents,
> Harnesses, Skills, and Tools.

Lines 21-25 (page 2 table). Meanings:
- Instructions file: Rules and facts about your project that Copilot CLI reads at the start of every session.
- Skill: Written steps for one kind of task, read only when that task comes up.
- MCP server: A separate program that gives Copilot CLI tools for another system.
- Custom agent: A file that sets up a separate agent with its own job, instructions and tools.
- Settings: Your choices for how Copilot CLI runs, including which folders you trust and which tools run without asking.

Lines 31-45 (Instructions file entry):
- Identify by: A Markdown file of plain sentences, such as .github/copilot-instructions.md or AGENTS.md.
- What: An instructions file tells Copilot CLI about your project and how you want the work done. Copilot CLI reads every file that applies, from your Copilot folder and from the repository, and adds them all to the session. A file ending in .instructions.md applies only when its applyTo pattern matches a file being worked on.
- So what: Put rules here that should hold in every session, such as how to run the tests. All the files are combined and none outranks another, so two files that disagree leave the model to choose.
- Loads | At the start of a session | A change reaches the next session, not the one that’s running.
- Check with | /instructions | Lists the files the session loaded and lets you turn one off. From the shell, copilot instruction list shows the same.
- Cannot | Settle a conflict | Keep each rule in one file.
- Confused with Skill: Instructions are read at the start of every session. A skill’s steps are read only when the task calls for them, so a long procedure belongs in a skill.

Lines 51-65 (Skill entry):
- Identify by: A folder with a SKILL.md file, such as .github/skills/release-notes/SKILL.md.
- What: A skill is a written procedure for one kind of task. SKILL.md starts with a name and a description, followed by the steps. Copilot CLI uses a skill when the description matches what you asked for, or you run it yourself by typing its name, such as /release-notes.
- So what: A skill keeps the way you do a task, such as writing release notes, in a file that can be reviewed and shared like code. Only the descriptions load at the start, so many skills can sit ready without filling the context.
- Loads | Description first, steps when used | The rest of SKILL.md joins the context when the skill is used.
- Check with | /skills | Lists the skills the session found. From the shell, copilot skill list shows the same.
- Cannot | Add a tool | A step that runs a script still needs the shell tool, and your approval to run it.
- Confused with Custom agent: A skill’s steps are followed by the agent you’re already talking to. A custom agent is a separate agent, with its own instructions and tools.

Lines 71-85 (MCP server entry):
- Identify by: An entry with a start command or a URL in ~/.copilot/mcp-config.json, .github/mcp.json or .mcp.json.
- What: An MCP server is a separate program that gives Copilot CLI tools for another system, such as a database or an issue tracker. Copilot CLI connects to each server when the session starts. GitHub’s own MCP server is built in and needs no setup.
- So what: Add a server when the work needs a system Copilot CLI can’t reach on its own. Servers listed in the repository load only after you trust the folder.
- Loads | When the session starts | Copilot CLI connects to each server and asks for its tools.
- Check with | /mcp | Shows the servers and lets you add, turn off or remove one. From the shell, copilot mcp list shows the same.
- Cannot | Get past your organization’s list | If your organization or enterprise allows only listed servers, other servers don’t load.
- Confused with Plugin: A plugin is a package you install with copilot plugin install. It can bring MCP servers with it, along with skills, custom agents and hooks, so a server can appear without you adding it yourself.

Lines 91-105 (Custom agent entry):
- Identify by: A Markdown file ending in .agent.md in an agents folder, such as .github/agents/reviewer.agent.md.
- What: A custom agent is a file that sets up an agent for one job, with its own instructions and the tools it may use. An Accidental Guide to: Agents, Harnesses, Skills, and Tools calls this an agent definition. You can pick one to run your session, or Copilot CLI can hand it part of a task.
- So what: A custom agent keeps a specialist job, such as reviewing or refactoring, in one file the whole repository can share. Your organization can share agents with all its repositories too.
- Loads | When you pick it or Copilot CLI hands it work | The body of the file becomes that agent’s instructions.
- Check with | /agent | Lists the custom agents you can pick. To start a session with one, add --agent and the agent’s name.
- Cannot | Read repository instructions as a subagent | Add include-custom-instructions: true to the file to give it them.
- Confused with Subagent: A subagent is any agent that the main agent hands work to. A custom agent can be the main agent, when you pick it, or a subagent, when Copilot CLI hands it a task.

Lines 111-125 (Settings entry):
- Identify by: A settings.json file in ~/.copilot, or in .github/copilot in the repository.
- What: Settings hold your choices for how Copilot CLI runs, such as the model, the plugins to turn on and the hooks to run. Two choices are kept apart from settings.json: the folders you trust, in config.json, and the tools you’ve allowed to run without asking, in permissions-config.json.
- So what: Trust and approvals decide what Copilot CLI does without asking you. When you trust a folder, its repository setup loads. When you approve a tool for a repository, Copilot CLI stops asking before it runs there.
- Loads | When the session starts | Flags such as --allow-tool apply to that run only and aren’t saved.
- Check with | /settings | Shows each setting and lets you change it. From the shell, copilot config --list prints them.
- Cannot | Undo a deny rule | A denied tool stays denied, even with --allow-all-tools.
- Confused with Policy: A policy is a setting your organization or enterprise manages, such as whether Copilot CLI is allowed or which models you can use. /settings shows it, but its value overrides yours.

Line 147 (where, Policies row): copilot/managed-settings.json in the .github-private repository, plus policies an administrator sets on GitHub

Lines 149-150 (where, closing note): As of October 2026, custom instructions that an organization sets on GitHub don’t reach Copilot CLI. The CLI reads only the instruction files in your Copilot folder and in the repository.

Lines 154-155 (combine intro): When the same kind of setup is in more than one place, Copilot CLI either uses all of it or picks one copy. Instructions and hooks add up. Skills, MCP servers, custom agents and settings have one winner for each name or key.

Lines 159-164 (combine rows), facts corrected:
- Instructions: Copilot CLI uses every file that applies and drops exact duplicates. None outranks another, so keep rules from disagreeing.
- Skills: When two skills share a name, the first one found wins: the repository’s, then yours, then a plugin’s.
- MCP servers: When two servers share a name, the order from highest is --additional-mcp-config, then a plugin’s server, then the repository’s files, nearest your working folder first, then ~/.copilot/mcp-config.json.
- Custom agents: When two agents share a name, yours wins, then the repository’s, then a plugin’s, then your organization’s, then your enterprise’s.
- Settings: Each layer overrides the one before: ~/.copilot/settings.json, the repository’s settings.json, settings.local.json, environment variables, then command-line flags. Settings your organization manages lock most keys.
- Hooks: Every hook from every place runs.

Lines 166-167 (combine closing): The first time you start Copilot CLI in a folder, it asks whether you trust it. Repository MCP servers, hooks and plugin settings load only after you say yes, and /env shows everything the session loaded.

Lines 171-172 (elsewhere intro): The other tools keep the same kinds of setup under their own names. Copilot CLI also reads CLAUDE.md, .claude/skills/, .agents/skills/, .claude/agents/ and .mcp.json, so a repository set up for Claude Code or Codex already partly works in Copilot CLI.

Lines 182-184 (elsewhere closing): Each of these has its own guide: An Accidental Guide to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to: Codex, and An Accidental Guide to: Visual Studio and VS Code.

When done, print `wc -w guide.md` and stop.
