# Writer instructions, round 3: An Accidental Guide to… Claude Desktop

Edit `guide.md` in the current folder in place. Keep every rule from writer-round1.md
(`drafts/claude-desktop/notes/writer-round1.md`).

No mannered prose: the writing must not call attention to itself. Make no assumption that the reader is an expert.

## Why

The guide prints about 1,700 words and must come down to about 1,150. Round 2 fixed the voice;
keep that voice and cut detail, not clarity. Below is the cut text for each section. Apply it as
written. Where a rule from round 1 would be broken, fix the smallest thing and keep the length.

## Edits

1. First page, the two paragraphs. Paragraph 1 becomes:
   In Claude Desktop you can tell Claude how to answer you, save the steps for tasks you repeat, connect Claude to the apps you use, and choose what Claude may do without asking. Most of these settings belong to your Claude account and also apply on claude.ai. A few belong to this computer only.
   Paragraph 2 becomes:
   You’ll find them in Settings and in Customize, in the left sidebar. For what a skill, a tool and an MCP server are, see An Accidental Guide to: Agents, Harnesses, Skills, and Tools.
   Leave the terms table as it is.

2. Every entry: delete the Cannot row from Field marks, so Field marks has only the Works in row.

3. Instructions entry:
   - Identify by: Settings > General, and Set project instructions on a project’s page.
   - What: Instructions are text you write for Claude to follow. The ones in Settings apply to all your chats, and project instructions apply only inside that project.
   - So what: Put a preference you always want in Settings, and one that matters for a single piece of work in that project.
   - Works in | Web, desktop and mobile | Instructions belong to your account.
   - Confused with: Memory: Memory is what Claude picks up from your chats, in Settings > Memory. Instructions are what you write yourself.

4. Skills entry:
   - Identify by: Customize > Skills.
   - What: A skill is a saved set of steps for one kind of task. Turn on an example skill or upload your own, and Claude follows the steps when that task comes up.
   - So what: You explain a task once instead of in every chat. Your skills also load in Claude Code when you sign in with the same account.
   - Works in | Your Claude account | Skills need Code execution and file creation, in Settings > Capabilities.
   - Confused with: Instructions: Instructions apply to every chat. A skill’s steps apply only to its kind of task.

5. Connectors entry:
   - Identify by: Customize > Connectors, or the + button in the message box.
   - What: A connector is an MCP server on the internet, usually for a service you sign in to. You add it once and it works wherever you use Claude.
   - So what: For each of a connector’s tools you choose Always allow, Needs approval or Blocked. Free plans can add one custom connector.
   - Works in | Web, desktop and mobile | Local files and apps need a local MCP server instead.
   - Confused with: Desktop extension: A desktop extension is a local MCP server in a .mcpb file, installed in Settings > Extensions. Extensions run on this computer and work only in Claude Desktop and Claude Code.

6. Plugins entry:
   - Identify by: Customize > Plugins, on the Discover tab.
   - What: A plugin is a package of skills, connectors and sub-agents. Plugins are saved to your account, not to your computer.
   - So what: One install sets up what you need for a role. Your organization may install some plugins for you.
   - Works in | Chat, Cowork and Claude Code | Paid plans only. A plugin with a local MCP server needs the desktop app.
   - Confused with: Skills: A skill is one set of steps. A plugin can hold several skills, plus connectors and sub-agents.

7. Settings and permissions entry:
   - Identify by: Settings, from your initials in the lower left, and the permission setting in the message box.
   - What: Settings holds your account’s preferences, such as General, Capabilities and Memory. Claude Desktop adds Extensions and Developer, which apply to this computer only.
   - So what: The permission setting decides how much Claude does without asking. The default is Manual, where Claude asks before it acts.
   - Works in | Your account and this computer | Owners and IT can turn some options off.
   - Confused with: Customize: Customize is where you add skills, connectors and plugins. Settings is where you set preferences and permissions.

8. Where things live. Intro paragraph becomes:
   Most things live in your Claude account and show up wherever you sign in. A few live on this computer and work only in Claude Desktop.
   In the table, the Connectors cell becomes: Customize > Connectors, then a connector for its tool permissions
   Leave the other rows as they are. The closing paragraph becomes:
   After you edit claude_desktop_config.json, quit Claude Desktop completely and open it again. Chats and Cowork use what’s in Customize. The Code tab reads ~/.claude instead, like Claude Code; see An Accidental Guide to: Claude Code.

9. Your account or your organization? Intro paragraph becomes:
   On Free, Pro and Max plans you set everything yourself. On Team and Enterprise plans, an owner sets limits in Organization settings.
   Table rows become:
   | Skills | Turn on or upload | Plugins & skills: turn skills on, add skills for everyone, stop people creating skills |
   | Connectors | Add and sign in | Connectors: add for the team, set limits nobody can override |
   | Plugins | Add from Discover | Add marketplaces, require plugins |
   | Desktop extensions | Install allowed ones | Connectors, Desktop tab: the allowlist |
   | Memory | Turn on or off | Capabilities: allow memory |
   Closing paragraph becomes:
   On computers your company manages, IT can set the desktop app’s options in com.anthropic.claudefordesktop on macOS or HKLM\SOFTWARE\Policies\Claude on Windows, for example to turn off desktop extensions. These override the allowlist in the app. If something is missing, ask your owner.

10. Same thing elsewhere. Table rows become:
    | Instructions | CLAUDE.md in Claude Code, AGENTS.md in Codex, copilot-instructions.md or AGENTS.md in Copilot CLI and VS Code |
    | Skills | A folder with a SKILL.md file, in Claude Code under ~/.claude/skills. Codex, Copilot CLI and VS Code have skills too. |
    | Connectors | MCP servers: .mcp.json in Claude Code, ~/.codex/config.toml in Codex, the User or Workspace group in VS Code |
    | Plugins | Plugins in all four |
    | Settings and permissions | ~/.claude/settings.json in Claude Code, approval_policy and sandbox_mode in ~/.codex/config.toml |
    The closing paragraph becomes:
    See An Accidental Guide to: Claude Code, An Accidental Guide to: GitHub Copilot CLI, An Accidental Guide to: Codex and An Accidental Guide to: Visual Studio and VS Code.

11. Sources. The intro becomes:
    These public sources were checked on 22 October 2026. The Anthropic Help Center articles, listed first, are at support.claude.com/en/articles/ and their number.
    In each Help Center row, drop "Anthropic Help Center, " from the Source, leaving only the short title.
