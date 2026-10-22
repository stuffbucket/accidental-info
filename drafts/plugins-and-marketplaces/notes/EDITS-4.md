# Edits, round 4: Plugins, Connectors, and Marketplaces

Apply these edits in place to `packages/accidental-guides/guides/plugins-and-marketplaces/guide.md`
(your working directory's `./guide.md`). Line numbers are from the file as it is now (commit
2e0810d, version 0.1.1). Replace each listed line with the new text, word for word, keeping
the table row structure: label cells stay as they are unless the edit gives a new label. Lines
that start with `> ` keep the `> ` at the start. Change nothing else, including the front
matter and the map block. Don't touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`
and `packages/editorial/skills/accidental-guide-write/references/voice.md`
first. Every rule there applies to any text you write or shorten.

## Why

The body must read in five minutes, about 1,100 printed words, and it is about 1,130 now.
Short entries also let two entries share a page. Tools and Instructions are defined in An
Accidental Guide to: Agents, Harnesses, Skills, and Tools, so those entries point there and
cover only the names. Three rows use semicolons and the product table uses dashes for "no";
both break the series' rules. Work from the bottom of the file up so the line numbers hold.

## Which product uses which word (lines 164 to 183)

1. Lines 166 to 167: replace the paragraph (both lines) with one line, word for word:
   These are the words each product uses, and what they mean there, as of October 2026. No means the product’s documentation doesn’t use the word.
2. Line 172: `> | Connector | from claude.ai | MCP server | no | no | no | inside plugins |`
3. Line 175: `> | Prompt file | merged into skills | no | no | Local harness only | yes | deprecated |`
4. Line 177: `> | Hook | yes | Cowork only | yes | preview | no | yes |`
5. Line 178: `> | Plugin | yes | yes | yes | agent plugin | no | not in the IDE |`

## Marketplaces (lines 142 to 162)

6. Lines 160 to 162: replace the paragraph (all three lines) with one line, word for word:
   The Visual Studio Marketplace is a store for editor extensions, and Claude Marketplace is a website. Neither one is a plugin marketplace.

## Packages (lines 122 to 140)

7. Line 126: `| What | A plugin installs skills, agent definitions, hooks and MCP servers in one step. |`
8. Line 127: `| So what | Copilot CLI, VS Code and Codex read Claude Code’s plugin files, but each loads only the parts it supports. |`

## Hooks (lines 103 to 120)

9. Line 108: `| So what | Use a hook for anything that must happen every time, such as a check before each commit. |`
10. Lines 119 to 120: replace the paragraph (both lines) with one line, word for word:
    A tool runs when the model calls it. A hook runs when its event happens.

## Instructions (lines 82 to 101)

11. Line 86: `| What | Instructions tell the agent how to work. An instructions file loads every session. See An Accidental Guide to: Agents, Harnesses, Skills, and Tools. |`
12. Line 87: `| So what | Put rules in an instructions file. Steps for one kind of task go in a skill, which loads only when a task needs it. See An Accidental Guide to: Agent Skills. |`
13. Line 93: `> | Instructions file | Read every session, such as AGENTS.md or CLAUDE.md. Claude apps say project instructions. |`
14. Line 96: `> | Custom agent | Sets up a sub-agent. Claude Code and Codex say subagent. |`
15. Lines 100 to 101: replace the paragraph (both lines) with one line, word for word:
    Instructions guide the model. A hook runs every time, even if the model skips an instruction.

## Tools (lines 62 to 80)

16. Line 66: `| What | Most tools you add come from MCP servers, which some products call connectors, apps or extensions. See An Accidental Guide to: Agents, Harnesses, Skills, and Tools. |`
17. Line 67: `| So what | One MCP server works in all these products, so ask for one when the agent needs a new system. See An Accidental Guide to: Model Context Protocol. |`
18. Line 74: `> | Connector | What Claude apps call an MCP server. OpenAI says app. |`
19. Line 75: `> | Desktop extension | A local MCP server in one file, for Claude Desktop |`
20. Line 80: `A tool reaches another system. Instructions say when to use it.`

## The map (lines 21 to 60)

21. Lines 23 to 24: replace the paragraph (both lines) with one line, word for word:
    Each colored line is one kind of thing, and each stop is a name you’ll see.

## What are all these things? (lines 11 to 19)

22. Lines 17 to 19: replace the paragraph (all three lines) with one line, word for word:
    Claude apps means claude.ai and the Claude Desktop app. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains the basic terms.

## Check before you finish

- Every line not named above is unchanged.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, en dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
