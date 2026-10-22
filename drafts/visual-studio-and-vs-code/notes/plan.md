# Plan: An Accidental Guide to… VS Code and Visual Studio

Slug `visual-studio-and-vs-code`. Version 0.1.0. About 1,100 printed words, 12 pages, five
minutes. Facts only from `sources.md` (code.visualstudio.com, learn.microsoft.com,
docs.github.com, checked 22 October 2026), plus the sibling-product facts listed under page 11.

## Who it's for

Someone who uses GitHub Copilot's agent in VS Code (or Visual Studio) and has found
instructions, agents, skills, MCP servers and settings scattered across `.github/`, `~/.copilot/`,
`.vscode/` and the settings UI. They want to know what each thing is, where it goes, and what
wins when two of them disagree. They are not experts. The basics (agent, harness, skill, tool,
session, context window) are in An Accidental Guide to: Agents, Harnesses, Skills, and Tools.

## The one idea that makes it calm

VS Code can run more than one harness, picked in the session target. The default is the
Copilot harness, and it reads Copilot's folders: `.github/` in the repo and `~/.copilot/` in your
home folder. Older VS Code places (`.vscode/mcp.json`, files kept in the VS Code profile, the
`chat.*FilesLocations` settings) are read only by the Local harness. The guide describes the
Copilot harness and says where Local differs, once.

Second idea: instructions add up, settings override. Nothing ranks instructions files against
each other, so fix conflicts in the files.

## The five parts (entry pages, colours by number)

| # | Part | Key | One line |
|---|---|---|---|
| 01 | Instructions file | In | Text added to every request: `.github/copilot-instructions.md`, `AGENTS.md`, `*.instructions.md` |
| 02 | Custom agent | Ag | A `.agent.md` file that sets a role, tools and model; picked from the Agent dropdown; once called chat modes |
| 03 | Skill | Sk | A folder with `SKILL.md`; only name and description load until used; `/name` runs it |
| 04 | MCP server | Mc | A program that adds tools; `.mcp.json` in the repo, `~/.copilot/mcp-config.json` for you; gallery is `@mcp` in Extensions |
| 05 | Setting | Se | A switch in VS Code's settings: harness, what's read, org discovery, MCP access; `.vscode/settings.json` or user settings |

Prompt files appear only as "Confused with" on the Skill page (they run only in the Local harness;
VS Code suggests a skill instead). Hooks and plugins are not parts; at most one mention.

## Pages

1. Cover. Title "VS Code and Visual Studio", subtitle "A pocket-sized guide to where GitHub
   Copilot’s agent setup lives, as of October 2026."
2. `{#why}` What can you set up in VS Code? First paragraph stands alone on the site (blurb).
   Plain words: the agent reads files and settings you can change; five kinds; they live in
   three scopes (the repo, you, your organization). The harness note. Table of five parts, one
   line each. Pointer to the base guide for the basics. ~150 words.
3–7. Entries. Identify by, What, So what, two field marks (Loaded, Cannot), Confused with.
   ~90 words each.
8. `{#where}` Where things live. Table Thing | Scope | Location, grouped by part, exact paths
   for the Copilot harness. Closing note on the Local harness. ~170 words.
9. `{#scopes}` How scopes combine. Instructions add up with no ranking; a custom agent's
   instructions win over custom instructions if they conflict; skills and agents from every
   scope are offered; MCP servers need unique names; settings: later scope wins (Default,
   User, Workspace, then Policy), objects merge; organization adds instructions and agents
   and can restrict MCP servers. ~120 words.
10. `{#vs}` What’s different in Visual Studio. Table by part. ~140 words.
11. `{#elsewhere}` Same thing elsewhere. Table by part naming the equivalent in Claude Code,
    Claude Desktop, GitHub Copilot CLI and Codex. Note naming the sibling guides in colon form.
    ~90 words.
12. `{#sources}` Sources, checked 22 October 2026.
