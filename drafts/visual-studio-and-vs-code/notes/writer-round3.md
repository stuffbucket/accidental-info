# Writer instructions, round 3: cut to five minutes

Edit `packages/accidental-guides/guides/visual-studio-and-vs-code/guide.md` in place. Line
numbers refer to the file as it is now (210 lines). The printed guide is about 1,700 words and
has to come down to about 1,200. Most of the text below is given exactly: use it as written.
You may change a word only to make a sentence read more naturally, and never to add words.
Keep every heading, id and table shape except where an edit says otherwise.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

## 1. Remove every “## Field marks” block

In all five entries, delete the “## Field marks” heading and its table (lines 33–38, 52–57,
71–76, 90–95, 109–114) and the blank lines around them. Each entry keeps its first table
(Identify by, What, So what) and its “## Confused with: …” heading and paragraph.

## 2. Page 2, lines 15–23

Line 15 becomes:

The default harness in VS Code is the Copilot harness, which reads .github/ in the repo and ~/.copilot/ in your home folder. Other harnesses read other places, noted where they differ. For the basics, see An Accidental Guide to: Agents, Harnesses, Skills, and Tools.

Table rows (lines 19–23):

| Instructions file | Rules the agent follows in every request, or for matching files. |
| Custom agent | A role with its own instructions, tools and model. |
| Skill | Steps the agent loads when a task needs them. |
| MCP server | A program that gives the agent more tools. |
| Setting | A switch that turns a feature on or changes what’s read. |

## 3. Entries

Instructions file:
- Identify by: .github/copilot-instructions.md, AGENTS.md, or a file ending in .instructions.md.
- What: An instructions file is text Copilot adds to your requests. copilot-instructions.md and AGENTS.md apply to every request, and a .instructions.md file can apply only to files that match its applyTo pattern.
- So what: Put the rules you’d otherwise repeat in every chat here. When one seems ignored, check where the file is and what its applyTo pattern matches.
- Confused with: Setting. Paragraph: An instructions file tells the agent how to work. A setting changes what VS Code itself does.

Custom agent:
- Identify by: keep line 48.
- What: A custom agent is a saved role with its own instructions, tools and model. You pick one from the Agent dropdown, and another agent can start it as a sub-agent.
- So what: Limiting a custom agent’s tools limits what it can change. While it’s selected, its instructions are added to your instructions files and win if the two conflict.
- Confused with: Instructions file. Paragraph: keep line 61, but write “and .chatmode.md files” instead of “and old .chatmode.md files”.

Skill:
- Identify by: A folder with a SKILL.md file whose name matches the folder.
- What: A skill is a written procedure in a folder. Only its name and description load at first, and the rest loads when your request matches or you type /skill-name.
- So what: A skill can hold long steps without taking up room until it’s needed. When a skill doesn’t run, check its description first.
- Confused with: Prompt file. Paragraph: A prompt file, .github/prompts/*.prompt.md, is a saved prompt you run with /name. Prompt files only work in the Local harness, so VS Code suggests a skill instead.

MCP server:
- Identify by: keep line 86.
- What: An MCP server is a separate program that gives the agent more tools. The harness connects to it and passes the model’s tool calls to it.
- So what: A local MCP server can run code on your machine with your permissions. Add only servers you trust, and check whether your organization limits which ones you can use.
- Confused with: Extension. Paragraph: keep line 99.

Setting:
- Identify by: A value in the Settings editor, your user settings or .vscode/settings.json.
- What: A setting is a switch or value that changes how VS Code behaves. Copilot’s settings turn features on and off, such as chat.useAgentSkills for skills.
- So what: When something works for a teammate and not for you, compare settings. Your user settings apply in every repo you open.
- Confused with: Instructions file. Paragraph: keep line 118.

## 4. Where things live, lines 122–146

- Line 122: The Copilot harness reads these places. Use the repo for what the team shares and your home folder for what’s only yours.
- Line 127 Location: AGENTS.md, from the root down to the working folder
- Line 143 Location: Your user settings.json
- Line 146: The Local harness also reads .vscode/mcp.json and files kept in your VS Code profile. The Claude harness reads .claude/ and ~/.claude/ instead.

## 5. How scopes combine, lines 150–160

- Line 150: Instructions add up, and settings override. Custom agents, skills and MCP servers from every scope are offered together.
- Line 154: | Instructions file | Every file that applies is added, and none ranks above another. |
- Line 155: | Custom agent | All appear in the Agent dropdown. The selected agent’s instructions win a conflict. |
- Line 156: | Skill | All are offered, and each loads when it matches or you name it. |
- Line 157: | MCP server | All are added. Nothing decides between two servers with the same name, so give each its own. Your organization can limit which ones run. |
- Line 158: | Setting | The later scope wins: Default, then User, then Workspace. An administrator’s policy wins over all three. |
- Line 160: keep.

## 6. What’s different in Visual Studio, lines 164–175

- Line 164: Visual Studio reads many of the same files, but not all, and keeps its settings in Tools › Options.
- Line 168: | Instructions file | .github/copilot-instructions.md and .github/instructions/*.instructions.md. Visual Studio 2026 adds personal instructions in %USERPROFILE%/copilot-instructions.md. |
- Line 169: | Prompt file | .github/prompts/*.prompt.md. Type / or #prompt: in chat. |
- Line 170: | Custom agent | .github/agents/*.agent.md, or %USERPROFILE%\.github\agents for your own. Version 18.4 or later. |
- Line 171: | Skill | The same folders as VS Code. Version 18.5 or later. |
- Line 172: | MCP server | Reads %USERPROFILE%\.mcp.json, then .vs\mcp.json, .mcp.json, .vscode\mcp.json and .cursor\mcp.json in the solution folder. Browse in Extensions › MCP Registries… |
- Line 173: | Setting | Tools › Options › GitHub › Copilot, where a checkbox turns instructions files on. |
- Line 175: Visual Studio doesn’t list AGENTS.md as supported as of October 2026, so put rules both editors need in .github/copilot-instructions.md.

## 7. Same thing elsewhere, lines 179–189

- Line 179: Other agent tools have the same kinds of setup in their own places. Copilot CLI uses the same Copilot harness, so it reads the same .github/ and ~/.copilot/ folders, but it doesn’t run prompt files.
- Line 189: Each tool has its own guide: An Accidental Guide to: Claude Code, An Accidental Guide to: Claude Desktop, An Accidental Guide to: GitHub Copilot CLI and An Accidental Guide to: Codex.

## 8. Sources

Delete line 202 (MCP configuration reference). Keep the rest.
