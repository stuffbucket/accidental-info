# Writer instructions, round 1: Plugins, Connectors, and Marketplaces

No mannered prose: the writing must not call attention to itself. Make no assumption that the reader is an expert.

You are writing the text of a new pocket guide. Edit one file in place:
`packages/accidental-guides/guides/plugins-and-marketplaces/guide.md` (you are run from that folder, so it is `./guide.md`).
It already has front matter, the map block and placeholder sections. Replace the placeholder text. Do not edit any other file.

Read these first, in this order:

1. `packages/editorial/skills/accidental-guide-plan/references/series-rules.md` (the rules; binding)
2. `packages/editorial/skills/accidental-guide-write/references/voice.md` (the voice; binding)
3. `packages/accidental-guides/guides/agents-harnesses-skills-tools/guide.md` (the base guide; never contradict it, don't repeat it)
4. `drafts/plugins-and-marketplaces/notes/plan.md` (the page plan)
5. `drafts/plugins-and-marketplaces/notes/sources.md` (the only facts you may use)

`<root>` is the repository root.

## Who it's for

Someone who uses a coding agent or a Claude or ChatGPT app and keeps running into plugin, marketplace, connector, extension, skill, hook and the rest, and can't tell which is which. They are smart and busy, not an expert. Talk to them directly ("you"), in regular English that builds one idea at a time. Five minutes front to back: about 1,100 printed words in the whole guide, including tables, map labels and sources. Cut detail, not clarity.

## Rules that are easy to break

- No paragraph by list. If it's a list, it belongs in a table; otherwise connected sentences.
- No "A person can", no "One may", no "this guide", no page or layout talk, no hooks, trivia, sarcasm, snark, rhetorical questions, slogans, "not X but Y", em dashes, rhythm triplets, borrowed framing (no birds, field guides, travel; the map is just a diagram, so don't build metaphors on trains, stations or journeys in the prose).
- No quotes, no names of people, nothing non-public about Microsoft.
- Ask questions plainly ("What is a plugin?"), never "what a plugin is".
- Cross-references in body text use the colon form exactly: An Accidental Guide to: Agents, Harnesses, Skills, and Tools. Others: An Accidental Guide to: Skills; An Accidental Guide to: MCP; An Accidental Guide to: Claude Code; An Accidental Guide to: Claude Desktop; An Accidental Guide to: GitHub Copilot CLI; An Accidental Guide to: Codex; An Accidental Guide to: Visual Studio; An Accidental Guide to: VS Code.
- Say "as of October 2026" once where products differ or change often (the product table's intro is a good place). Don't repeat it everywhere.
- "Claude apps" means claude.ai and the Claude Desktop app. Define it once on the first page.
- Formatting the parser needs: no Markdown emphasis or backticks; no lines starting with "- "; no "&" before letters; no "<" except `<br/>` in `#` titles; no slashes in ordinary words (anything shaped like a path is set in mono, so write "and" or "or"); a "Short answer" style cell never ends with a full stop; use typographic quotes and apostrophes (’ “ ”) and the ellipsis character. No "e.g. " in the first sentence of a What or So what row (the builder bolds up to the first ". ").
- Rows must read on their own: no row sentence starts with "it", "its", "they" or "this".

## The sections, exactly in this shape

The builder reads sections by position. Keep every `{#id}` heading and attribute as it is, and keep this shape.

### `# … {#why}` (page 2)

A short plain question as the title (keep `{#why}`), for example "What are all these things?". Then two or three short paragraphs and NO table. The first paragraph must stand on its own: it is the summary on the website. Say what the reader is up against (each product adds things to a coding agent or AI app under its own names, and the same word can mean different things), and that every one of these things is one of five kinds: tools, instructions, hooks, packages and marketplaces. Point to An Accidental Guide to: Agents, Harnesses, Skills, and Tools for the basics (agent, harness, skill, tool, MCP server) in one sentence.

### `# The map {#map}` (page 3)

Exactly two paragraphs: one before the fenced block and one after it. Keep the fenced ```map block where it is.

- Before: one or two sentences. Each coloured line is one kind of thing; each stop is a name you’ll see; where names overlap, the stop is drawn as a larger ringed circle.
- After: one or two sentences that help the reader use it, such as: if you meet a new word, find which line it's on and you know what kind of thing it is.

Inside the map block you may reword the grey captions (the last field of `station` lines and the last field of `also` lines) for plainness and accuracy, but keep each one about the same length or shorter, and don't change names, coordinates, sides, the `line` lines or the order. Check every caption against sources.md.

### Five `{#entry}` sections (pages 4 to 8)

Keep each heading exactly as it is (`# Tools {#entry num=01 mono=Tl}` and so on). Each entry has exactly this shape:

```
| Field | Text |
|---|---|
| Identify by | one line: what you see on screen or in a folder |
| What | two or three sentences |
| So what | one or two sentences: why it matters to you, what to do |

## Names on this line

| Name | Where | What it is |
|---|---|---|
| (3 or 4 rows) | product names, short | a short sentence |

## Confused with: <Other>

One paragraph of two sentences that tells the two apart.
```

About 100 words per entry, all in. The Names table is where the different product words go, so don't also list them in What. Facts to use (all in sources.md):

- **Tools (Tl).** Things that let the agent reach other systems. Nearly all of them are MCP servers under other names: a connector in Claude apps is an MCP server added in Claude’s settings, usually remote; OpenAI says app and MCP server are interchangeable; a desktop extension (also a local connector) is a local MCP server packed into one .mcpb file and installed in Claude Desktop under Settings, Extensions. In Copilot CLI an extension is an experimental JavaScript module that adds tools and commands; VS Code extensions can add tools too. So what: when you need the agent to reach a new system, ask for an MCP server; one server works in every product here. Point to An Accidental Guide to: MCP. Confused with: Packages or Instructions, your pick.
- **Instructions (In).** Text the agent reads to know how to work. Instructions file (AGENTS.md, CLAUDE.md, copilot-instructions.md; Claude apps have project instructions instead of a file) is read every session. Skill (a folder with SKILL.md, every product here) loads when the task matches or when you type /name. Prompt file (.prompt.md) in VS Code and Visual Studio runs when you type /name; Codex’s custom prompts are deprecated in favor of skills, and VS Code now points to skills too. Agent definition sets up a sub-agent: GitHub and Microsoft products call it a custom agent (.agent.md), Claude Code and Codex call it a subagent. Slash command: typing /name runs a skill, a prompt file or a built-in command; Claude Code now just says command, and custom commands were merged into skills. Point to An Accidental Guide to: Skills. Confused with: Hooks.
- **Hooks (Hk).** A command the harness runs at a set moment, such as before a tool call, after an edit or when a session starts. The model doesn’t decide when it runs, so a hook is for things that must happen every time. Where: Claude Code, Copilot CLI, VS Code (preview) and Codex; Copilot CLI and VS Code share one hook file format; in Claude apps hooks come only inside plugins, in Cowork; none found in Visual Studio. Confused with: Instructions (an instruction asks the model; a hook runs regardless).
- **Packages (Pk).** Things you install in one step that bring other things with them. A plugin is a folder with skills, agent definitions, hooks and MCP servers (Claude Code, Claude apps, Copilot CLI, Codex; VS Code calls them agent plugins and also loads plugins installed by Copilot CLI). Copilot CLI, VS Code and Codex also read Claude Code’s plugin and marketplace files. Each product loads only the parts it supports. An extension in VS Code or Visual Studio is an add-on for the editor, from the Visual Studio Marketplace; the Claude Code and Codex extensions put the whole harness in the editor. The Codex IDE extension doesn’t support plugins. Confused with: Marketplaces (a plugin is what you install; a marketplace is the list you install it from).
- **Marketplaces (Mk).** Lists you install things from. A plugin marketplace is a marketplace.json file in a Git repository that lists plugins and where to get each one; you add it, then install plugins by name (plugin@marketplace). It’s a catalog, not a store, and anyone can publish one, so adding one means trusting whoever runs it. Claude Code adds Anthropic’s official one by itself; Copilot CLI ships awesome-copilot. The Visual Studio Marketplace is the store for editor extensions. A directory is a list the company reviews: the Connectors Directory and the plugin directory on claude.ai, and one plugin directory shared by ChatGPT and Codex. Anthropic reviews plugins in its directory but not plugins added from a marketplace URL. The GitHub MCP Registry lists MCP servers (Copilot CLI, VS Code, Visual Studio). Claude Marketplace is a website, not a plugin marketplace. Confused with: Packages.

### `# Which product uses which word {#who}` (page 9)

One short intro paragraph (with "as of October 2026"), then one table, then exactly one closing paragraph. The table's header row is exactly:

`| Kind | Claude Code | Claude apps | Copilot CLI | VS Code | Visual Studio | Codex |`

Five rows, first cell exactly Tools, Instructions, Hooks, Packages, Marketplaces. Each cell lists the words that product uses for that kind, in lower case except product names, two to five words, comma-separated, or "none found" where sources.md found nothing. Columns are narrow (about 37 points at 6 pt type), so keep words short. The closing paragraph points to the product guides by title in colon form (Claude Code, Claude Desktop, GitHub Copilot CLI, Codex, Visual Studio, VS Code), in one or two sentences.

### `# Sources {#sources}` (page 10)

One intro sentence ("These public sources were checked in October 2026." is fine), then a three-column table `| Source | Date | Address |`. Seven to nine rows, the most useful official pages from sources.md: publisher and page title in the first column (such as "Anthropic, Claude Code: plugins"), "October 2026" as the date, and the address without https://.

## Finish

When done, print the guide's word count estimate and the first paragraph of `{#why}`.
