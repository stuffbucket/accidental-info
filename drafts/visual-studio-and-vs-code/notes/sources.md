# Sources: VS Code and Visual Studio

Fetched 22 October 2026 with WebFetch. Excerpts are short and verbatim as returned. The VS Code
pages all show "Last updated 10/21/2026". Only official public documentation is used.

## VS Code (code.visualstudio.com)

### Choose an Agent Harness
code.visualstudio.com/docs/agents/run/agent-harnesses

- Harness: "coordinates the language model, context, and tools that an agent uses to complete your task."
- Copilot is the recommended default: "Run tasks using the Copilot SDK, which provides the shared agent experience across GitHub Copilot products." Runs in the Agent Host.
- Local: "Run tasks within VS Code's built-in agent harness." "**Local** is a harness name, not a synonym for running on your machine."
- Claude: "The Anthropic Claude Agent SDK is integrated into VS Code." Codex: "OpenAI Codex runs through the OpenAI Codex extension or the experimental Agent Host integration."
- "Harness-specific customizations, including hooks, follow the selected harness."
- Picking a Claude model in a Copilot session keeps you on the Copilot harness.

### Agent customization concepts
code.visualstudio.com/docs/agents/concepts/customization

- Scopes: user (all your workspaces), workspace or repository (shared through source control),
  organization ("centrally managed and shared across repositories", only where the type supports it).
- "Choose the narrowest scope that matches the information."
- "Customization types are building blocks rather than mutually exclusive alternatives."
- "Choosing a language model doesn't change the customization formats that a harness reads."
- "Not every customization type supports every scope or agent harness."
- Prompt files: "You run it as a slash command (Local harness only)".

### Customization overview
code.visualstudio.com/docs/copilot/customization/overview

- "User customizations are specific to you and are not committed to the project."
- "Organization customizations are configured through GitHub rather than created in the Agent Customizations editor."
- "Copilot reads customizations from `~/.copilot`, and Anthropic Claude reads them from `~/.claude`."
- Command: Chat: Open Customizations.

### Custom instructions
code.visualstudio.com/docs/copilot/customization/custom-instructions

- `.github/copilot-instructions.md` at the repo root; personal Copilot equivalent `~/.copilot/copilot-instructions.md`.
- AGENTS.md: "a cross-agent format for project guidance." Copilot looks at the repo root, the working directory and every folder between.
- `*.instructions.md` default folders: `.github/instructions` (workspace), `~/.copilot/instructions` (user); Claude: `.claude/rules`, `~/.claude/rules`.
- Front matter: `applyTo` glob, `description` lets the agent load the file on demand.
- Organization: "Set `github.copilot.chat.organizationInstructions.enabled` to `true` to enable discovery." "Organization instructions are additive to user and repository instructions."
- "Applicable instruction sources are additive." "there is no general precedence order between these files." "Do not depend on a file order or precedence rule to resolve conflicts".

### Prompt files
code.visualstudio.com/docs/copilot/customization/prompt-files

- "Prompt files are Markdown files with the `.prompt.md` extension." Workspace folder `.github/prompts`; user prompt files in the VS Code profile.
- Run by typing `/` and the name.
- "Prompt files run only in **Local** harness sessions in the Chat view." Other harnesses: use a skill.

### Custom agents
code.visualstudio.com/docs/agent-customization/custom-agents

- Workspace `.github/agents` (`.agent.md`), user (Copilot) `~/.copilot/agents`; Claude format `.claude/agents`, `~/.claude/agents`; Local harness user agents in VS Code profile storage.
- "Custom agents were previously known as custom chat modes." Rename `.chatmode.md` to `.agent.md`.
- Pick with the Agent dropdown after choosing a harness in Session Target.
- "In the Copilot harness, the agent's instructions are added to your custom instructions and take precedence if they conflict."
- "Another agent can also run a custom agent as a subagent."
- Organization agents: "Discovery of organization-level custom agents is enabled by default." Setting `github.copilot.chat.organizationCustomAgents.enabled`.

### Agent skills
code.visualstudio.com/docs/agent-customization/agent-skills

- "A skill is a directory containing a `SKILL.md` file". `name` must match the folder name.
- Workspace: `.github/skills/`, `.claude/skills/`, `.agents/skills/`. User: `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/`.
- Loading: discovery reads only name and description; body loads when matched or on `/skill-name`; referenced files load when needed.
- `chat.agentSkillsLocations` "is deprecated and isn't read by Copilot harness sessions."

### MCP servers
code.visualstudio.com/docs/agent-customization/mcp-servers

- Copilot Global "writes to `$COPILOT_HOME/mcp-config.json`, or `~/.copilot/mcp-config.json` when `COPILOT_HOME` is unset."
- Workspace root `.mcp.json` for team sharing. `.vscode/mcp.json` and profile `mcp.json`: "These destinations remain available for compatibility and are labeled deprecated in the guided flow."
- Gallery: Extensions view, search `@mcp`; Install (personal) or Install in Workspace.
- "Local MCP servers can run code on your machine, and tools can access external services using your permissions."
- "Your organization can restrict which servers are available."

### MCP configuration reference
code.visualstudio.com/docs/agents/reference/mcp-configuration

- VS Code format: `.vscode/mcp.json`, profile `mcp.json`, "It defines servers in a top-level `servers` object."
- Portable format: `.mcp.json`, `~/.copilot/mcp-config.json`, "It defines servers in a top-level `mcpServers` object."
- "Copilot harness sessions read the portable format directly." "The agent doesn't read `.vscode/mcp.json` directly." "VS Code forwards eligible servers from the VS Code format to the session, except servers that require interactive input"
- No precedence rule: "Use a unique name for each server to avoid conflicts."

### Migrate existing customizations
code.visualstudio.com/docs/agent-customization/migrate-customizations

- "The Copilot harness reads customizations from Copilot folders and portable formats."
- "The Copilot harness does not read custom agents and instructions stored in VS Code profile user data."
- Copilot ignores `chat.agentFilesLocations`, `chat.modeFilesLocations`, `chat.instructionsFilesLocations`, `chat.agentSkillsLocations`.

### Copilot settings reference
code.visualstudio.com/docs/copilot/reference/copilot-settings

- `github.copilot.chat.codeGeneration.useInstructionFiles` (true): "Automatically add custom instructions from `.github/copilot-instructions.md` to chat requests."
- `chat.useAgentsMdFile` (true): Local harness only. `chat.useClaudeMdFile` (true).
- `chat.useAgentSkills` (true): "Enable support for agent skills in VS Code."
- `chat.mcp.access` (true): "Manage which Model Context Protocol (MCP) servers can be used in VS Code."
- `github.copilot.chat.organizationInstructions.enabled` (true), `github.copilot.chat.organizationCustomAgents.enabled` (true).
- `chat.plugins.enabled` (false).
- Enterprise-managed settings turn off the Claude and Codex harnesses.

### User and workspace settings
code.visualstudio.com/docs/configure/settings

- User settings.json: macOS `$HOME/Library/Application Support/Code/User/settings.json`; Windows `%APPDATA%\Code\User\settings.json`; Linux `$HOME/.config/Code/User/settings.json`.
- "The workspace settings file is located under the `.vscode` folder in your root folder."
- "later scopes override earlier scopes": Default, User, Remote, Workspace, Workspace Folder, language-specific, Policy. Policy: "these values always override other setting values."
- Arrays and primitives are replaced; objects are merged.

## Visual Studio (learn.microsoft.com)

### Customize chat responses (copilot-chat-context), ms.date 2026-09-04
learn.microsoft.com/visualstudio/ide/copilot-chat-context

- `.github/copilot-instructions.md` "in the root of your repository".
- Option: Tools > Options > All Settings > GitHub > Copilot > Copilot Chat > "Enable custom instructions to be loaded from .github/copilot-instructions.md files and added to requests".
- `.github/instructions/*.instructions.md` with `applyTo`: "Use glob syntax to specify what files or folders the instructions apply to."
- Visual Studio 2026 personal: "The `%USERPROFILE%/copilot-instructions.md` file stores these preferences."
- Prompt files: `.github/prompts/*.prompt.md`. "Type `#prompt:` in chat input to reference any prompt files from your `.github/prompts` folder". "Type `/` in the chat input to see your custom prompts at the top of the IntelliSense list."
- "Organization-level custom instructions apply only to repositories that belong to a GitHub organization." Option "Enable organization-level custom instructions".

### Custom agents (copilot-specialized-agents), ms.date 2026-09-16
learn.microsoft.com/visualstudio/ide/copilot-specialized-agents

- "Custom agents require Visual Studio version 18.4 or later." Repo `.github/agents/` with `.agent.md`.
- User agents "in `%USERPROFILE%\.github\agents` by default. Change this location in **Tools > Options > GitHub > Copilot**."
- "Organization-level custom agents require Visual Studio version 18.9 or later."

### Agent skills (copilot-agent-skills), ms.date 2026-09-04
learn.microsoft.com/visualstudio/ide/copilot-agent-skills

- Visual Studio 2026 version 18.5 or later. Repo: `.github/skills/`, `.claude/skills/`, `.agents/skills/`. Personal: `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/`.
- "Each skill is a directory containing a `SKILL.md` file that follows the agentskills.io specification."

### MCP servers (mcp-servers), ms.date 2026-05-26
learn.microsoft.com/visualstudio/ide/mcp-servers

- Visual Studio "reads MCP server configurations from the following directories, in the following order": `%USERPROFILE%\.mcp.json`, `<SOLUTIONDIR>\.vs\mcp.json`, `<SOLUTIONDIR>\.mcp.json`, `<SOLUTIONDIR>\.vscode\mcp.json`, `<SOLUTIONDIR>\.cursor\mcp.json`.
- Files use a `servers` key. Registry: "select **Extensions** > **MCP Registries...** to open the **MCP Server Manager**".

### Admin controls (visual-studio-github-copilot-admin)
learn.microsoft.com/visualstudio/ide/visual-studio-github-copilot-admin

- MCP allowlist: "In the enterprise or organization settings, navigate to **AI Controls** and select **MCP** in the sidebar."

## GitHub (docs.github.com)

### Custom instructions support
docs.github.com/en/copilot/reference/custom-instructions-support

- VS Code Copilot Chat: repository-wide `.github/copilot-instructions.md`, path-specific `.github/instructions/**/*.instructions.md`, agent instructions "using an `AGENTS.md` file".
- Visual Studio Copilot Chat: repository-wide and path-specific. AGENTS.md not listed.
- Organization instructions: not listed for either IDE. The Visual Studio docs (copilot-chat-context) and VS Code settings reference both describe organization instructions, so the guide follows the editors' own docs and says "as of October 2026".

### Response customization
docs.github.com/en/copilot/concepts/prompting/response-customization

- Copilot CLI, VS Code and Visual Studio "combine applicable instruction files without defining a general precedence order."
- "Whenever possible, try to avoid providing conflicting sets of instructions."

### Organization custom agents
docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents

- Stored "in the `/agents` directory of your organization's `.github` or `.github-private` repository."

### MCP server access
docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-server-access

- "MCP servers in Copilot" policy, an MCP registry URL, and "Restrict MCP access to registry servers": "Registry only": "Only servers from the registry may run."

## The other tools, for "Same thing elsewhere"

Fetched 22 October 2026 by a research sub-agent. Details are left to the sibling guides.

### GitHub Copilot customization cheat sheet
docs.github.com/en/copilot/reference/customization-cheat-sheet

- Prompt files `.github/prompts/*.prompt.md`: VS Code "✓", Copilot CLI "✗".
- Custom instructions, custom agents, agent skills and MCP servers are listed for both VS Code and Copilot CLI.
- Skills, personal: "`~/.copilot/skills/<skill-name>/SKILL.md`" or "`~/.agents/skills/<skill-name>/SKILL.md`".
- VS Code's harness page: the Copilot harness "uses a shared runtime for core capabilities," aligned across VS Code, GitHub Copilot CLI and the GitHub Copilot app (code.visualstudio.com/docs/copilot/agents/overview).
- Copilot CLI user settings: `~/.copilot/settings.json` (code.visualstudio.com migrate page: "`~/.copilot/settings.json`, not `~/.copilot/config.json`").

### Claude Code
- code.claude.com/docs/en/memory: "**User instructions** | `~/.claude/CLAUDE.md`"; "A project CLAUDE.md can be stored in either `./CLAUDE.md` or `./.claude/CLAUDE.md`."
- code.claude.com/docs/en/sub-agents: "**Project subagents** (`.claude/agents/`) are ideal for subagents specific to a codebase."
- code.claude.com/docs/en/skills: "Claude Code loads project skills from `.claude/skills/` in the directory where you start it and in every parent directory up to the repository root."
- code.claude.com/docs/en/mcp: "Project-scoped servers enable team collaboration by storing configurations in a `.mcp.json` file at your project's root directory." "User-scoped servers are stored in `~/.claude.json`".
- code.claude.com/docs/en/settings: "User | `~/.claude/settings.json` | You, in every project on this machine".

### Claude Desktop
- support.claude.com/en/articles/10185728: profile preferences are "account-wide settings that help Claude understand your general instructions." Project instructions "only apply to chats within that project."
- support.claude.com/en/articles/12512180: "Navigate to Customize > Skills." "Upload a ZIP file containing your skill folder."
- support.claude.com/en/articles/11175166: "Navigate to **Customize > Connectors**."
- modelcontextprotocol.io/docs/develop/connect-local-servers: "**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`".
- No official doc found for custom agents in Claude Desktop chat.

### Codex (developers.openai.com redirects to learn.chatgpt.com)
- learn.chatgpt.com/docs/agent-configuration/agents-md: "Codex reads `AGENTS.override.md` if it exists. Otherwise, Codex reads `AGENTS.md`."
- learn.chatgpt.com/docs/agent-configuration/subagents: "add standalone TOML files under `~/.codex/agents/` for personal agents" or "`.codex/agents/` for project-scoped agents."
- learn.chatgpt.com/docs/build-skills: "Codex scans `.agents/skills` in every directory from your current working directory up to the repository root."
- learn.chatgpt.com/docs/extend/mcp: "Configure each MCP server with a `[mcp_servers.<server-name>]` table in the configuration file."
- learn.chatgpt.com/docs/config-file/config-basic: "Codex stores user-level configuration at `~/.codex/config.toml`."
