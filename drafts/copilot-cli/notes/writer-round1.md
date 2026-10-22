# Writer instructions, round 1: An Accidental Guide to… GitHub Copilot CLI

You are writing the text of a short printed guide. Edit one file in place:
`packages/accidental-guides/guides/copilot-cli/guide.md` (relative to the repo root; you are
running from that folder, so it is `./guide.md`). It holds a stub with the right structure. Replace
every "Stub" with real text and fill the tables. Do not touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

## Read first

1. `drafts/copilot-cli/notes/plan.md`: the page plan.
2. `drafts/copilot-cli/notes/sources.md`: every fact you may use. Use only facts in
   this file. Copy paths exactly.
3. `packages/editorial/skills/accidental-guide-plan/references/series-rules.md` and
   `packages/editorial/skills/accidental-guide-write/references/voice.md`: the voice. Binding.
4. `packages/accidental-guides/guides/agents-harnesses-skills-tools/guide.md`: the base guide.
   Never contradict it and don't repeat it. It explains agent, harness, skill, tool, session and
   context window; point to it for those as "An Accidental Guide to: Agents, Harnesses, Skills,
   and Tools".
5. `packages/accidental-guides/guides/lights-off-software-factories/guide.md`: an example of the
   finished form and length of a guide in this series.

## The reader and the job

The reader uses GitHub Copilot CLI, or is about to, and is lost. Instructions, skills, MCP
servers, custom agents and settings can each be kept in several places, in files with similar
names, and it isn't obvious which copy wins. The guide should make that calm and easy to look up:
what can you set up, where does each thing live, and what happens when two places set the same
thing. A smart colleague who is new to this should be able to find a path in seconds.

## Length

Five minutes, front to back: about 1,050 printed words in total, tables included. Rough budget:
page 2 about 120 words; each entry about 100 words; "Where things live" about 200 words (mostly
paths); "How do the places combine?" about 160; "Same thing elsewhere" about 80; sources as given.
Cut detail, not clarity.

## Pages and what each says

Page 2, `{#why}`, "What can you set up in Copilot CLI?" Two or three short paragraphs, then the
five-row table. The first paragraph is shown on its own on a website, so it must stand alone:
say plainly that Copilot CLI reads its setup from files, that the same kind of file can sit in
your home folder, in the repository, or come from your organization. Never say "this guide";
the following paragraph or table simply goes on to the five kinds of setup, where each lives and
which copy wins. Mention once, in the second paragraph, that the basics are in An Accidental
Guide to: Agents, Harnesses, Skills, and Tools. Table rows: Instructions file, Skill, MCP server,
Custom agent, Settings, each with a one-sentence meaning in plain words.

Entries (pages 3 to 7). Each has: Identify by (what you'd see on disk), What (two or three
sentences; the first sentence is printed bold, so make it the definition), So what (why it
matters to the reader; first sentence bold). Field marks, three rows, each "Short answer"
(no full stop, a few words) plus Detail (one sentence):
- Loads: when it reaches the model.
- Check with: the command that shows what's loaded (from sources.md section 10: /instructions,
  copilot instruction list, /skills, copilot skill list, /mcp, copilot mcp list, /agent,
  /settings, copilot config --list, /env).
- Cannot: one real limit.
Then "Confused with", one or two sentences.
- 01 Instructions file. Confused with: Skill.
- 02 Skill. Confused with: Custom agent.
- 03 MCP server. Confused with: Plugin (a plugin is a package you install that can bring MCP
  servers, skills, custom agents and hooks with it).
- 04 Custom agent. Say once that the base guide calls this an agent definition. Confused with:
  Subagent (a custom agent can run as the main agent when you pick it, or as a subagent when the
  model hands it a task).
- 05 Settings. Cover the settings files, trusted folders and tool approvals here. Confused with:
  Policy (settings your organization or enterprise manages, which you can't override).

`{#where}`, "Where things live". One short intro paragraph that says ~/.copilot is your
Copilot folder, moved if you set COPILOT_HOME. Then a three-column table: Scope, Thing, Path.
Scope is exactly one of "Just you", "This repository", "Your organization"; keep each scope's
rows together, in that order. Thing is one of: Instructions, Skills, MCP servers, Custom agents,
Settings, Plugins, Hooks, Policies. Path cells hold exact paths, separated by commas or "or",
with at most a few plain words. Include:
- Just you: Instructions (~/.copilot/copilot-instructions.md, ~/.copilot/instructions/), Skills,
  MCP servers, Custom agents, Settings (settings.json; saved tool approvals in
  permissions-config.json; trusted folders in config.json, which the CLI manages), Plugins
  (installed under ~/.copilot/installed-plugins/).
- This repository: Instructions (.github/copilot-instructions.md,
  .github/instructions/*.instructions.md, AGENTS.md; also CLAUDE.md and GEMINI.md), Skills,
  MCP servers (.github/mcp.json to share, .mcp.json), Custom agents, Settings
  (.github/copilot/settings.json, and settings.local.json for you only), Hooks
  (.github/hooks/*.json).
- Your organization: Custom agents (agents/ in the organization's .github or .github-private
  repository), Policies (copilot/managed-settings.json in .github-private; and policies an
  administrator sets on GitHub, such as whether the CLI is on, which models and which MCP
  servers are allowed). Say plainly in the closing note that organization custom instructions
  set on GitHub don't reach Copilot CLI; the CLI uses your local files.
Closing paragraph (one): the note above, and "as of October 2026".

`{#combine}`, "How do the places combine?" One or two short intro paragraphs: some things add
up, some things have one winner. Then a two-column table, Thing and "When two places set it",
one row each for Instructions, Skills, MCP servers, Custom agents, Settings, Hooks. Use the exact
rules in sources.md (instructions all combine with no precedence order, so avoid conflicts;
skills first found wins, project before personal before plugin; MCP servers closer to the
working folder win, a plugin's server beats yours in ~/.copilot, --additional-mcp-config beats
all; custom agents yours beats the repository's beats the organization's beats the
enterprise's; settings later layers win: user, repository, local, environment variables, flags,
and managed settings lock most keys; hooks all run). Closing paragraph: repository MCP servers,
hooks and plugin settings load only after you trust the folder, and /env shows what the session
actually loaded.

`{#elsewhere}`, "Same thing elsewhere". One short intro sentence. Table: first column the
Copilot CLI name (Instructions file, Skill, MCP server, Custom agent, Settings); the other four
columns are Claude Code, Claude Desktop, Codex, VS and VS Code. Each cell a name or file name of
one to four words, taken from `drafts/copilot-cli/notes/siblings.md`. The columns are
narrow (about 12 characters a line), so use short file names only (CLAUDE.md, AGENTS.md,
.mcp.json, config.toml) and no long paths; for VS and VS Code, where the IDEs read the same
.github files as the CLI, write "Same file" or "Same folder". The intro sentence can carry the
overlap from siblings.md: Copilot CLI also reads CLAUDE.md, .claude/skills/, .agents/skills/,
.claude/agents/ and .mcp.json. Closing
paragraph: name the sibling guides with the colon form: An Accidental Guide to: Claude Code,
An Accidental Guide to: Claude Desktop, An Accidental Guide to: Codex, An Accidental Guide to:
Visual Studio and VS Code.

`{#sources}`: intro "These public sources were checked on 22 October 2026." Then about seven
rows: Source (page title), Publisher ("GitHub Docs", or "GitHub Copilot CLI 1.0.102" for the
help), Address (no https://). Pick the pages that back what you wrote, from sources.md: the
configuration directory reference, the command reference, add custom instructions, add skills,
add MCP servers, invoke custom agents, the plugin reference, allowing and denying tool use, and
the CLI's own help ("copilot help", address "copilot --help, copilot help config").

## Format rules (the build breaks or prints wrongly otherwise)

- Keep the front matter, the `#` headings with their `{#ids}` and attributes, and the table
  shapes exactly as in the stub. Table header rows stay as they are.
- No Markdown emphasis or backticks. No lists. No `&` before letters. No `<` except the
  existing `<br/>` in titles.
- No slashes in ordinary words (paths are fine: they are set in mono automatically).
- A Short answer cell must not end with a full stop.
- No "e.g." or "i.e." anywhere.
- Use typographic apostrophes and quotes (’ “ ”).
- Every paragraph after a table in a section is the closing note; each such section has exactly
  one paragraph after its table.

## Voice rules (from the series brief)

Regular English that builds one idea at a time, as if to a smart colleague who is new to this.
Say "you". Avoid all of: paragraph by list; stiff "A person can"; self-narration ("this guide",
"this page", "below"); hooks; trivia; sarcasm or snark; borrowed framing (no birds, field guides,
travel, maps); mannered prose (slogans, rhetorical questions, "not X but Y", em dashes, rhythm
triplets, stacked metaphors); quotes or names of people; anything about Microsoft. Rows must read
on their own: no sentence in a table cell starts with "It", "Its", "They" or "This". Each term
keeps one meaning. Where something changes often, say "as of October 2026" once, not
everywhere.

When done, print the word count of guide.md (wc -w) and stop.
