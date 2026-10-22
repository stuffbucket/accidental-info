# Equivalents in the sibling products (checked 22 October 2026)

Short names for the "Same thing elsewhere" table. Each from the vendor's official docs, fetched
22 October 2026. Keep cells to one to four words.

| Copilot CLI | Claude Code | Claude Desktop | Codex | VS and VS Code |
|---|---|---|---|---|
| Instructions file | CLAUDE.md (AGENTS.md also works) | “Instructions for Claude” in Settings, no file | AGENTS.md | .github/copilot-instructions.md, the same file the CLI reads |
| Skill | Skills in .claude/skills/ | Skills, uploaded as a ZIP in Customize | Skills in .agents/skills/ | Skills in .github/skills/, the same folder |
| MCP server | MCP servers, .mcp.json | Connectors, claude_desktop_config.json | MCP servers in config.toml | MCP servers, .mcp.json |
| Custom agent | Subagents, .claude/agents/ | None documented | Custom agents, .codex/agents/ | Custom agents, .github/agents/ |
| Settings | .claude/settings.json, permission rules | Settings in the app | config.toml, approval policy | IDE settings |

Sources:

- Claude Code: code.claude.com/docs/en/claude-directory, code.claude.com/docs/en/settings
- Claude Desktop: support.claude.com/en/articles/10185728 (instructions),
  support.claude.com/en/articles/12512180 (skills),
  modelcontextprotocol.io/docs/develop/connect-local-servers and
  support.claude.com/en/articles/10949351 (connectors). Custom agents: no page documents them;
  "None documented" is a reading, not a quote.
- Codex: learn.chatgpt.com/docs/customization/overview (AGENTS.md),
  learn.chatgpt.com/docs/build-skills, learn.chatgpt.com/docs/extend/mcp,
  learn.chatgpt.com/docs/agent-configuration/subagents (.codex/agents/*.toml),
  learn.chatgpt.com/docs/config-file/config-reference (approval_policy, sandbox_mode).
  developers.openai.com/codex now redirects to learn.chatgpt.com/docs.
- VS Code: code.visualstudio.com/docs/copilot/customization/custom-instructions,
  …/customization/agent-skills, …/customization/mcp-servers (.mcp.json; .vscode/mcp.json labelled
  deprecated), …/customization/custom-agents (.github/agents/*.agent.md),
  code.visualstudio.com/docs/agents/run/approvals.
- Visual Studio: learn.microsoft.com/visualstudio/ide/copilot-chat-context
  (.github/copilot-instructions.md), …/ide/copilot-agent-skills, …/ide/mcp-servers (.mcp.json),
  …/ide/copilot-specialized-agents (.github/agents/*.agent.md), …/ide/copilot-agent-mode.
  Visual Studio's docs don't mention AGENTS.md or CLAUDE.md.

Overlap worth one sentence: Copilot CLI also reads CLAUDE.md, .claude/skills/, .agents/skills/,
.claude/agents/ and .mcp.json (see sources.md sections 1 to 4), so a repository set up for
Claude Code or Codex is partly set up for Copilot CLI too.
