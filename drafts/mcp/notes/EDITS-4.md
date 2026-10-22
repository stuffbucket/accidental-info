# Edits, round 4: Model Context Protocol

Apply these edits in place to `packages/accidental-guides/guides/mcp/guide.md` (your working
directory's `./guide.md`). Line numbers are from the file as it is now (commit c07ffcc,
version 0.1.0). Replace each listed line with the new text, keeping the table row structure:
label cells stay as they are unless the edit gives a new label. Lines that start with `> `
keep the `> ` at the start. Change nothing else. Don't touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`
and `packages/editorial/skills/accidental-guide-write/references/voice.md`
first. Every rule there applies to any text you write or shorten.

## Why

The guide now uses packed pages: two entries share a page when they fit. The entries are
each a few lines too long to pair up, so the guide runs to 9 pages. The body is about 1,060
printed words, and the first page has 214 words where it should have about 170. The idea
that a local server often calls a web service is said four times. This round shortens the
first page, trims each entry by a line or two, and drops the fourth repeat. The field marks
now print only their short answer, in narrow columns, so each short answer must fit on one
line of about 18 characters. Work from the bottom of the file up so the line numbers hold.

## Front matter

- Line 8: `version: 0.2.0`

## What is MCP? (lines 11 to 25)

1. Line 17: replace with, word for word:
   “Server” can make you picture a service on another machine, but an MCP server is often a small program on your own machine. The harness does the asking, so in MCP the clients live in the harness.

## MCP server (lines 31 to 48)

2. Line 44: `> | Cannot | See the conversation |`

## Client (lines 50 to 67)

3. Line 56: `| So what | One client per server keeps the servers apart. A server can’t see another server’s calls or results. |`

## Server entry (lines 69 to 86)

4. Line 73: `| Identify by | An entry in .mcp.json for Claude Code, ~/.codex/config.toml for Codex or mcp.json for VS Code, as of October 2026. |`
5. Line 74: `| What | A server entry is a name plus the command that starts a local server or the URL of a remote one. Commands such as claude mcp add write it for you. |`
6. Line 81: `> | Kept in | A project or user file |`

## Transport (lines 88 to 105)

7. Line 93: `| What | A transport is how the client and server pass messages. With stdio, the harness starts the server on your machine and talks to it directly. With HTTP, the server runs on its own at a URL. |`
8. Line 101: `> | Cannot | Change the tools |`
9. Line 105: `HTTP usually means a remote server, but a server on your own machine can use HTTP too.`

## Common questions (lines 122 to 131)

10. Line 129: delete the whole line (the row "Is the server the system I’m connecting to?").
    The same point is made on the overview page and in the MCP server entry.

## Check before you finish

- Every line not named above is unchanged.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) and quotes (“ ”) everywhere.

When you're done, reply with one line: done.
