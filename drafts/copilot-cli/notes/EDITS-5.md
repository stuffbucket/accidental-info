# Edits, round 5: GitHub Copilot CLI

Apply these edits in place to `packages/accidental-guides/guides/copilot-cli/guide.md` (your
working directory's `./guide.md`). Line numbers are from the file as it is now (version
0.2.0). Replace each listed line with the new text, keeping the table row structure and any
`> ` at the start of a line. Change nothing else. Don't touch any other file, and don't change
the `version:` line.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`
and `packages/editorial/skills/accidental-guide-write/references/voice.md` first.

## Why

Two entries now share a page, but only if each entry is a line or two shorter. These edits
take one or two lines out of the first four entries, and drop the sentence under "Same thing
elsewhere", which repeats its title.

## Edits

1. Line 32: | Identify by | AGENTS.md or .github/copilot-instructions.md. |
2. Line 33: | What | Copilot CLI adds every instructions file that applies to the session. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains them. |
3. Line 34: | So what | Put rules for every session here. No file outranks another, so keep each rule in one place. |
4. Line 51: | Identify by | A folder in .github/skills/ with a SKILL.md file. |
5. Line 52: | What | Copilot CLI uses a skill when your request matches its description, or when you type / and its name. An Accidental Guide to: Agent Skills explains skills. |
6. Line 59: > | Loads | Description first |
7. Line 71: | Identify by | An entry in ~/.copilot/mcp-config.json or .mcp.json. |
8. Line 72: | What | GitHub’s own MCP server is built in and needs no setup. An Accidental Guide to: Model Context Protocol explains MCP servers. |
9. Line 92: | What | Copilot CLI reads custom agents from your Copilot folder, the repository and your organization. An Accidental Guide to: Agents, Harnesses, Skills, and Tools explains agents. |
10. Line 99: > | Loads | When it runs |
11. Delete line 171 ("Other coding tools keep the same kinds of setup in their own files.") and the
    blank line after it.

## Check before you finish

- Every line not named above is unchanged.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.

When you're done, reply with one line: done.
