# Sources: An Accidental Guide to… Claude Desktop

All checked 22 October 2026 with WebFetch. Excerpts are verbatim from the page as fetched.
Most support articles show only "Updated over N weeks ago", not a date.

## Anthropic Help Center (support.claude.com)

### Use connectors to extend Claude's capabilities
https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities ("Updated this week")
- "Navigate to **Customize > Connectors**." "Click the “+” button next to **Connectors**."
- "Custom connectors using remote MCP are available on Claude, Cowork, and Claude Desktop"
- "Free users are limited to one custom connector."
- "Your server must be reachable over the public internet."
- "For each permission category or individual permission, select Always allow, Needs approval, or Blocked."
- Admins: "Navigate to **Organization settings > Connectors**." "an Owner or Primary Owner needs to enable them for the organization." "Each person still needs to authenticate individually before they can use it."

### When to use desktop and web connectors
https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors
- "Most connectors are remote—they're the default choice and work everywhere you use Claude."
- Desktop fits when "The tool runs on your computer—local files, a database on localhost, a desktop application."
- "Install a desktop extension: Open Claude Desktop → Settings → Extensions"
- "Remote connectors work across all Claude surfaces."
- "Desktop extensions run locally and are only available in Claude Desktop and Claude Code—not on web or mobile."
- "A plugin can bundle either remote or local MCP servers (or both)." "One that references a local MCP works in Cowork and Claude Code, not in chat."

### Getting started with local MCP servers on Claude Desktop
https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop
- "install and manage local MCP servers through single-click installable packages"
- "Navigate to Settings > Extensions on Claude Desktop." "Select the .mcpb file and follow the prompts to install."
- "Extensions from the official directory update automatically by default."
- "visit Developer settings (under **Desktop app**) to see connection status and look at the logs"
- Sensitive values stored in "Keychain on macOS, Credential Manager on Windows"
- "Owners and Primary Owners of Team and Enterprise organizations can manage which desktop extensions are enabled"

### Enabling and using the desktop extension allowlist
https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist (March 16, 2026)
- "available for Owners and Primary Owners of Team and Enterprise plans."
- "Navigate to Organization settings > Connectors" "Switch to the "Desktop" tab"
- "Enterprise policy controls at the user-machine level, these will override the in-app allowlist."

### Enterprise configuration for Claude Desktop
https://support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop
- "Claude Desktop reads preferences from the domain `com.anthropic.claudefordesktop`"
- Windows example path "HKLM:\SOFTWARE\Policies\Claude"; "Settings can be configured at machine-wide (HKLM) or per-user (HKCU) level."
- Keys: `isDesktopExtensionEnabled` "Enable/disable extensions"; `isLocalDevMcpEnabled` "Enable local MCP servers"; `disableAutoUpdates`; `isClaudeCodeForDesktopEnabled`; `secureVmFeaturesEnabled` "Enable Cowork access in desktop"; `allowedWorkspaceFolders` "Filepath or filepaths the user can mount to Cowork"; `forceLoginOrgUUID` "Require login to belong to a specific organization."
- "Machine-level settings take priority over user-level settings when both are configured."

### Use skills in Claude
https://support.claude.com/en/articles/12512180-use-skills-in-claude
- "You can enable example skills and upload your own in Customize > Skills."
- "This feature requires code execution to be enabled." "Navigate to Settings > Capabilities and ensure that Code execution and file creation is enabled."
- "Skills are available for users on Free, Pro, Max, Team, and Enterprise plans."
- Org: "Organization settings > Plugins & skills" (Policy tab). "Owners can also upload skills to provision them organization-wide—these skills automatically appear for all users." "an organization owner can turn off skill creation for users."
- Enabled skills "also load in Claude Code in your terminal when you sign in with the same Claude account"

### Use plugins in Claude
https://support.claude.com/en/articles/13837440-use-plugins-in-claude
- "Each plugin bundles skills, connectors, and sub-agents into a single package"
- "open the **Customize** menu in the left sidebar" "Open the **Plugins** tab."
- "You can add and use plugins in chat on the web, the Chat tab in Claude Desktop, and Claude Cowork."
- "Plugins are available to all paid plans (Pro, Max, Team, Enterprise)."
- "saved to your account, not to your computer"
- "an owner can distribute plugins across your organization through plugin marketplaces" "required plugins can't be turned off or removed."

### Browse skills, connectors, and plugins in one directory
https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory
- "Click "Customize" in the left sidebar." "Click on the tab you want to view: Skills, Connectors, or Plugins." "Open the **Discover** tab."
- "On Team and Enterprise plans, the directory is also where skills and plugins published to your organization appear."

### Understanding Claude's personalization features
https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features (September 16, 2026)
- "Instructions are account-wide settings" "Any instructions you add here will be applied to all of your conversations with Claude."
- Project instructions: "These instructions only apply to chats within that project."

### Claude Cowork and chat are one Claude
https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude (September 16, 2026)
- "rolling out gradually, starting with Pro and Max plans on web, desktop, and mobile."
- "The Cowork Global instructions setting is now part of Instructions for Claude in Settings > General."
- "Set preferences that apply to every conversation in Settings > General." "Connect apps in Customize > Connectors."
- "A permission setting in the message box controls how independently Claude works" — default Manual: "Claude asks before it takes actions"
- "Folders you gave Cowork access to are listed under Trusted folders."

### Get started with Claude Cowork
https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- "Claude can only read and write files in folders you've connected"
- "plugins that include local MCP servers work through the desktop app only"
- "Team or Enterprise plan owners can turn off web search for Cowork and Chat in Organization settings > Capabilities"
- "your admin controls whether "Automatically approve" is available to your organization"

### How can I create and manage projects?
https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- "Click on "Set project instructions."" "Claude will use these instructions for all the chats within the project."
- "If you're on a Team or Enterprise plan, you can share projects with other users in your organization" "unless your admin has turned off project sharing."

### Use Claude's chat search and memory to build on previous context
https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
- "Settings > Memory" "Generate memory from chats". "Each project has its own memory."
- "Owners and Primary Owners can turn memory on for the organization in Organization settings > Capabilities."

## Claude Code docs

### Claude Code on desktop
https://code.claude.com/docs/en/desktop
- "The desktop app reads the same settings files as the CLI."
- "Local sessions load your personal skills from `~/.claude/skills/`."
- "Cowork in the Desktop app sources its skills, plugins, and connectors from this Customize configuration, which syncs through your claude.ai account, not from the CLI's `~/.claude` directory."
- "Connectors are MCP servers with a graphical setup flow."
- view-only files "such as `.mcp.json` and `.claude/settings.json`"

## Model Context Protocol

### Connect to local MCP servers
https://modelcontextprotocol.io/docs/develop/connect-local-servers
- "This opens the Claude Desktop configuration window, which is separate from your Claude account settings."
- "navigate to the "Developer" tab" "Click the "Edit Config" button"
- "**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`" "**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`"
- "completely quit Claude Desktop and restart it."
- Logs: "macOS: `~/Library/Logs/Claude`" "Windows: `%APPDATA%\Claude\logs`"
- "The server runs with your user account permissions"

## Sibling products (for the "Same thing elsewhere" table only)

### OpenAI Codex, Config basics
https://learn.chatgpt.com/docs/config-file/config-basic (redirected from developers.openai.com/codex/config-basic)
- "Codex stores user-level configuration at `~/.codex/config.toml`."
- `approval_policy`, `sandbox_mode`

### OpenAI Codex, AGENTS.md
https://learn.chatgpt.com/docs/agent-configuration/agents-md
- "Codex reads `AGENTS.override.md` if it exists. Otherwise, Codex reads `AGENTS.md`." Example at `~/.codex/AGENTS.md`.

### GitHub Docs, Copilot customization cheat sheet
https://docs.github.com/en/copilot/reference/customization-cheat-sheet
- "`.github/copilot-instructions.md` (repo-wide)" "`AGENTS.md` (third-party agents)"
- Copilot CLI supports custom instructions, agent skills, hooks and MCP servers.

### VS Code, Agent customization overview
https://code.visualstudio.com/docs/agent-customization/overview
- "always-on instructions (`copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`)"
- "Copilot reads customizations from `~/.copilot`, and Anthropic Claude reads them from `~/.claude`."
- MCP: "select **Add Server** (**+**) in the **User** or **Workspace** group"
