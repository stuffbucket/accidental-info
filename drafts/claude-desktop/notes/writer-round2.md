# Writer instructions, round 2: An Accidental Guide to… Claude Desktop

Edit `guide.md` in the current folder in place. Change only what this list asks for. Line numbers
refer to guide.md as it stands now. Keep every rule from writer-round1.md
(`drafts/claude-desktop/notes/writer-round1.md`).

No mannered prose: the writing must not call attention to itself. Make no assumption that the reader is an expert.

## What's wrong with round 1

The draft got short by turning into notes. Sentences like "Settings controls behavior." and
"Instructions set preferences. Skills give task steps." are staccato and don't explain anything
to a newcomer. Each row should be one or two plain, complete sentences that say what the thing is
and why it matters, the way a colleague would say it. The replacement text below shows the
register. Use it as written unless it breaks a rule; then fix the smallest thing.

The first column of the tables must not have parentheses: "(Memory)" becomes "Memory".

## Edits

1. Lines 13–15 (the two paragraphs on the first page). Replace with:

   In Claude Desktop you can tell Claude how to answer you, save the steps for tasks you repeat, connect Claude to the apps and services you use, and choose what Claude may do without asking. Most of these settings belong to your Claude account, so they also apply on claude.ai. A few belong to this computer only.

   You’ll find them in two places in the app: Settings, and Customize in the left sidebar. On Team and Enterprise plans, an owner can also set limits for everyone. For what a skill, a tool and an MCP server are, see An Accidental Guide to: Agents, Harnesses, Skills, and Tools.

2. Lines 19–23 (Meaning column). Replace the meanings with:
   - Instructions: What you want Claude to know in every chat, or in every chat in one project.
   - Skills: Steps Claude follows for one kind of task, saved so you don’t have to repeat them.
   - Connectors: An MCP server you add in Customize so Claude can reach another app or service.
   - Plugins: A package that adds skills, connectors and sub-agents in one install.
   - Settings and permissions: Your preferences, and how much Claude may do before it asks you.

3. Instructions entry, lines 29–42. Rows become:
   - Identify by: Instructions for Claude in Settings > General, and Set project instructions on a project’s page.
   - What: Instructions are text you write for Claude to follow. The ones in Settings apply to all your chats, and project instructions apply only to chats in that project.
   - So what: Put each preference where it belongs. Something you always want goes in Settings, and something that only matters for one piece of work goes in that project.
   - Works in | All your conversations | Project instructions apply only inside their project.
   - Cannot | Carry facts between chats | Files you want every chat in a project to use go in the project’s knowledge.
   - Confused with: Memory, paragraph: Memory is what Claude picks up from your chats, and you manage it in Settings > Memory. Instructions are what you write yourself. Each project keeps its own memory.

4. Skills entry, lines 48–61. Rows become:
   - Identify by: Customize > Skills, where you turn skills on and off or add your own.
   - What: A skill is a saved set of steps for one kind of task. You can turn on the example skills or upload one you wrote, and Claude follows the steps when that task comes up.
   - So what: You explain a task once instead of in every chat. When you sign in to Claude Code with the same account, your skills load there too.
   - Works in | Your Claude account | Turn on Code execution and file creation in Settings > Capabilities first, because skills need it.
   - Cannot | Be changed from Claude Code | Claude Code reads your skills from your account and never changes them.
   - Confused with: Instructions, paragraph: Instructions apply to every chat. A skill holds the steps for one kind of task, and Claude uses it when that task comes up.

5. Connectors entry, lines 67–80. Rows become:
   - Identify by: Customize > Connectors, or the + button in the message box.
   - What: A connector is an MCP server on the internet that Claude can use, usually for a service you sign in to. You add it and sign in once, and it works wherever you use Claude.
   - So what: Each connector has tool permissions. For each tool you choose Always allow, Needs approval or Blocked, so you decide what Claude can do in that service.
   - Works in | Web, desktop and mobile | Free plans can add one custom connector.
   - Cannot | Reach things on your computer | Local files and apps need a local MCP server, which runs only in Claude Desktop and Claude Code.
   - Confused with: Desktop extension, paragraph: A desktop extension is a local MCP server in a .mcpb file that you install in Settings > Extensions. Extensions run on this computer and work only in Claude Desktop and Claude Code. You can also add a local MCP server by hand in the config file.

6. Plugins entry, lines 86–99. Rows become:
   - Identify by: Customize > Plugins, on the Discover tab.
   - What: A plugin is a package of skills, connectors and sub-agents. Plugins are saved to your account, not to your computer.
   - So what: One install sets up what you need for a role or a kind of work. On Team and Enterprise plans, your organization may install some plugins for you.
   - Works in | Chat, Cowork and Claude Code | Paid plans only: Pro, Max, Team and Enterprise.
   - Cannot | Run a local MCP server on the web | A plugin that includes one works through the desktop app only.
   - Confused with: Skills, paragraph: A skill is one set of steps. A plugin can hold several skills along with connectors and sub-agents.

7. Settings and permissions entry, lines 105–118. Rows become:
   - Identify by: Settings, from your initials in the lower left, and the permission setting in the message box.
   - What: Settings holds your account’s preferences, in sections such as General, Capabilities and Memory. Claude Desktop adds Extensions and Developer, which apply to this computer only.
   - So what: The permission setting decides how much Claude does without asking. The default is Manual, where Claude asks before it takes actions.
   - Works in | Your account and this computer | Account settings follow you when you sign in elsewhere. Extensions and Developer stay on this computer.
   - Cannot | Go past your organization’s limits | On Team and Enterprise plans, owners and IT can turn options off.
   - Confused with: Customize, paragraph: Customize, in the left sidebar, is where you add skills, connectors and plugins. Settings is where you set preferences and permissions.

8. Where things live, line 122. Replace with: Most things live in your Claude account, so they show up wherever you sign in. A few live on this computer and work only in Claude Desktop.

9. Where things live table, lines 126–135. Remove every parenthesis in the first column. After the
   Code execution row, add: | Folder access | This computer | Settings, under Trusted folders |
   In the Local MCP servers row, drop the words "opens claude_desktop_config.json." so the cell
   reads: Settings > Developer > Edit Config<br/>macOS: …<br/>Windows: … (keep the two paths exactly).

10. Line 137. Replace with: After you edit claude_desktop_config.json, quit Claude Desktop completely and open it again. Chats and Cowork tasks take skills, plugins and connectors from Customize, but the Code tab reads ~/.claude, the same as Claude Code. For that side, see An Accidental Guide to: Claude Code.

11. Account page, lines 141–151. Remove the parentheses in the first column. In the Skills row,
    write the screen name exactly as the app shows it: "Plugins & skills: turn skills on, add
    skills for everyone, or turn off creating skills". In the Desktop extensions row write
    "Connectors, Desktop tab: choose which extensions are allowed". Line 151: replace with:
    On computers your company manages, IT can also set the desktop app’s options in the preference domain com.anthropic.claudefordesktop on macOS, or under HKLM\SOFTWARE\Policies\Claude in the Windows registry. These can turn off desktop extensions or local MCP servers, and they override the allowlist in the app. When something you expect is missing, ask your organization’s owner.

12. Elsewhere page, line 155. Replace with: Coding tools keep the same kinds of things in their own files.
    Line 160: "A folder with a SKILL.md file in Claude Code, Copilot CLI and VS Code. Claude Code reads ~/.claude/skills, and Codex has skills too."
    Line 165: "For more, see An Accidental Guide to: Claude Code, An Accidental Guide to: GitHub Copilot CLI, An Accidental Guide to: Codex and An Accidental Guide to: Visual Studio and VS Code."

13. Sources, lines 169–191. The sources table now has two columns, Source and Address. Replace
    line 169 with: These public sources were checked on 22 October 2026. Each Anthropic Help Center article is at support.claude.com/en/articles/ followed by its number.
    Header row: | Source | Address |
    For each Help Center row, the Source is "Anthropic Help Center, <short title>" and the Address
    is only the number, such as 11176164. Use these short titles: Use connectors; Desktop and web
    connectors; Local MCP servers on Claude Desktop; Desktop extension allowlist; Enterprise
    configuration for Claude Desktop; Use skills in Claude; Use plugins in Claude; Personalization
    features; Cowork and chat are one Claude; Create and manage projects; Chat search and memory.
    Drop the rows for 14328846 and 13345190.
    The other rows keep their full address without https://, with these sources:
    Anthropic, Claude Code on desktop | code.claude.com/docs/en/desktop
    Model Context Protocol, Connect to local MCP servers | modelcontextprotocol.io/docs/develop/connect-local-servers
    OpenAI, Codex config basics | learn.chatgpt.com/docs/config-file/config-basic
    OpenAI, Codex AGENTS.md | learn.chatgpt.com/docs/agent-configuration/agents-md
    GitHub, Copilot customization cheat sheet | docs.github.com/en/copilot/reference/customization-cheat-sheet
    Visual Studio Code, Agent customization overview | code.visualstudio.com/docs/agent-customization/overview
