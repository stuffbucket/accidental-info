# Writer instructions, round 2: targeted edits to guide.md

No mannered prose: the writing must not call attention to itself. Make no assumption that the reader is an expert.

Edit `./guide.md` in place. Line numbers refer to the file as it is now; work from the bottom up so they stay right. Keep every rule from `writer-round1.md` in this folder (read it again first). Do not edit any other file. Facts only from `sources.md` in this folder.

The draft's shape is right, but the entries read as clipped fragments. The reader is new to all of this, so each entry should explain in connected, ordinary sentences, the way a colleague would over coffee, without getting longer. Short is fine; staccato isn't. Two-sentence Confused-with paragraphs that are both bare definitions ("A tool reaches another system. A package can install that tool with other parts.") are the main problem: say the difference the way you'd say it out loud, with a reason or an example.

The whole guide is about 280 words over budget. The product table and sources below save about 150; the rest must come from the map captions and entries, not from clarity.

## Edits

1. **Lines 180–194, Sources.** Keep the intro line. Use exactly these eight rows, in this order (date column "October 2026"):
   Anthropic, Claude Code: plugins | code.claude.com/docs/en/plugins
   Anthropic, Claude: plugins | claude.com/docs/plugins/overview
   Anthropic, Claude: connectors | claude.com/docs/connectors
   GitHub, Plugins for GitHub Copilot | docs.github.com/en/copilot/concepts/customizations/plugins
   Microsoft, Agent plugins in VS Code | code.visualstudio.com/docs/agent-customization/agent-plugins
   Microsoft, Use MCP servers to extend GitHub Copilot in Visual Studio | learn.microsoft.com/en-us/visualstudio/ide/mcp-servers
   OpenAI, Plugins | learn.chatgpt.com/docs/plugins
   OpenAI, Plugin controls | learn.chatgpt.com/docs/enterprise/apps-and-connectors

2. **Lines 162–178, product table.** The table is now indexed by word, so the reader can look up a word they've met. Replace lines 164–173 with one intro paragraph and this table, exactly (the dash is an en dash, –):

   Intro paragraph, in your words, two sentences: as of October 2026, which words each product uses and what each word means there; a dash means the product’s documentation doesn’t use the word.

   ```
   | Word | Claude Code | Claude apps | Copilot CLI | VS Code | Visual Studio | Codex |
   |---|---|---|---|---|---|---|
   | MCP server | yes | as connector | yes | yes | yes | yes |
   | Connector | from claude.ai | MCP server | – | – | – | inside plugins |
   | Extension | harness in an editor | local MCP server | tool module | editor add-on | editor add-on | harness in an editor |
   | Instructions file | CLAUDE.md | project instructions | yes | yes | yes | AGENTS.md |
   | Skill | yes | yes | yes | yes | yes | yes |
   | Prompt file | merged into skills | – | – | Local harness only | yes | deprecated |
   | Custom agent | subagent | Cowork only | yes | yes | yes | subagent |
   | Hook | yes | Cowork only | yes | preview | – | yes |
   | Plugin | yes | yes | yes | agent plugin | – | not in the IDE |
   | Marketplace | plugin list | plugin list | plugin list | both kinds | extension store | plugin list |
   | Directory | yes | yes | – | – | – | yes |
   | MCP registry | – | – | yes | MCP gallery | yes | – |
   ```

   Then the closing paragraph (lines 175–178): shorten to one sentence that names the six product guides in colon form. A sentence like "Each product has its own guide: An Accidental Guide to: Claude Code, …" is fine.

3. **Lines 153–156, Marketplaces names.** Names must match the map so they get their tile. Use four rows: Marketplace (Claude Code, Claude apps, Copilot CLI, VS Code, Codex: a marketplace.json list of plugins in a Git repository; anyone can publish one); Directory (Claude apps, ChatGPT, Codex: a list the company reviews, such as the Connectors Directory); MCP registry (Copilot CLI, VS Code, Visual Studio: GitHub’s list of MCP servers); Visual Studio Marketplace (VS Code, Visual Studio: the store for editor extensions). Drop "Named marketplace". Mention Claude Marketplace (a website, not a plugin marketplace) only if it fits in the What or So what row without adding a sentence.

4. **Lines 145–147, 160.** What: explain a plugin marketplace to a newcomer in two sentences (a list of plugins and where to get each one, kept as a marketplace.json file in a Git repository; you add the list once, then install its plugins by name). So what: anyone can publish a marketplace and adding one means trusting whoever runs it; Anthropic reviews plugins in its directory but not ones added from a marketplace URL. Rewrite line 160 as connected speech.

5. **Lines 125–140, Packages.** What: say why packages exist (installing skills, agent definitions, hooks and MCP servers one at a time is tedious, so a plugin brings them in one step). So what: Copilot CLI, VS Code and Codex also read Claude Code’s plugin files, but each product loads only the parts it supports. Names: Plugin (Claude Code, Claude apps, Copilot CLI, Codex), Agent plugin (VS Code), Extension (VS Code, Visual Studio: an add-on for the editor itself), and keep the IDE extension row. Rewrite line 140.

6. **Lines 106–120, Hooks.** Fine in content. Make What and So what read as connected sentences; give one example of a hook (running a formatter after every edit, or blocking a command). Rewrite line 120 so it explains why the difference matters (an instruction asks the model, which may not follow it; a hook always runs).

7. **Lines 86–101, Instructions.** Names: use the map’s names so they get tiles: Instructions file (Claude Code, Copilot CLI, VS Code, Visual Studio, Codex; Claude apps use project instructions), Skill (every product here; run by the model when the task matches or by you with /name), Prompt file (VS Code, Visual Studio; Codex’s custom prompts are deprecated), Custom agent (Copilot CLI, VS Code, Visual Studio; Claude Code and Codex say subagent; sets up a sub-agent). Line 97’s "Every product here" was wrong for agent definitions. What: two sentences on what instructions are and that they load at different times. Rewrite line 101.

8. **Lines 66–81, Tools.** Names: MCP server, Connector (Claude apps, and OpenAI’s app for the same thing; say both in the row), Desktop extension, Extension. What: say plainly that most of what you add to let the agent reach other systems is an MCP server under another name. Rewrite line 81 as connected speech; a good contrast is with Instructions (a tool lets the agent do something; instructions tell it how).

9. **Lines 59–60, after the map.** One sentence is enough.

10. **Lines 23–24, before the map.** The larger ringed stop marks either a name used for different things or one thing with several names. Say that plainly.

11. **Map captions (lines 26–57).** Shorten where you can without losing the meaning; the map is the densest page. Don't touch names, numbers, sides or `line` lines.

12. **Lines 13–19, first page.** Fine. The first paragraph's second sentence can say the five kinds are drawn as a map, without layout talk ("on the next page" is layout talk; avoid it).

## Finish

Print an estimate of the printed word count.
