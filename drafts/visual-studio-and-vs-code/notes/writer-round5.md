# Edits, round 5: VS Code and Visual Studio

Apply these edits in place to `packages/accidental-guides/guides/visual-studio-and-vs-code/guide.md`
(your working directory's `./guide.md`). Line numbers are from the file as it is now (after
round 4, version 0.1.1, 200 lines). Replace each listed line with the new text, keeping the
table row structure: label cells stay as they are unless the edit gives a new label. Change
nothing else. Don't touch any other file. Keep the `> ` at the start of every line that has one.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`
and `packages/editorial/skills/accidental-guide-write/references/voice.md` first.
Every rule there applies to any text you write or shorten. The text below is given exactly: use
it as written. You may change a word only to make a sentence read more naturally, never to add
words.

## Why

After round 4 the printed guide is 1,265 words without the sources page, and it has to come
down to about 1,100. Each entry is also a little too tall for two entries to share a page.
This round shortens the entries by a line or two each, keeps each field mark's short answer
to three words or so, so it fits on one line, and cuts repeated detail from the later pages.

## Entries

1. Line 30: | What | An instructions file is text Copilot adds to your requests. See An Accidental Guide to: Agents, Harnesses, Skills, and Tools. |
2. Line 31: | So what | Put rules you’d otherwise repeat in every chat here. A .instructions.md file can apply only to files that match its applyTo pattern. |
3. Line 35: > | Loads | When it applies |
4. Line 47: | What | A custom agent is a saved role with its own instructions, tools and model. You pick one from the Agent dropdown. See An Accidental Guide to: Agents, Harnesses, Skills, and Tools. |
5. Line 53: > | Cannot | Replace instructions |
6. Line 64: | What | A skill is a written procedure in a folder. Type /skill-name to run one yourself. See An Accidental Guide to: Agent Skills. |
7. Line 65: | So what | A skill’s steps take up no room until they’re needed. When a skill doesn’t run, check its description first. |
8. Line 69: > | Loads | Description first |
9. Line 81: | What | An MCP server is a program that gives the agent more tools. Search @mcp in the Extensions view to find one. See An Accidental Guide to: Model Context Protocol. |
10. Line 86: > | Loads | When it connects |
11. Line 91: An extension adds features to VS Code itself. MCP servers install from the same view, for you or for the workspace.
12. Line 98: | What | A setting is a switch or value that changes how VS Code behaves, such as chat.useAgentSkills for skills. |
13. Line 103: > | Loads | From every scope |
14. Line 104: > | Cannot | Guide the agent |

## Where things live

15. Line 136: The Local harness also reads .vscode/mcp.json. The Claude harness reads .claude/ and ~/.claude/ instead.

## How scopes combine

16. Line 146: delete this line (the Skill row).

## What’s different in Visual Studio

17. Line 155: Visual Studio reads many of the same files, but not all.
18. Line 160: delete this line (the Prompt file row).

## Same thing elsewhere

19. Line 170: Copilot CLI uses the same Copilot harness, so it reads the same .github/ and ~/.copilot/ folders. Other tools keep these things in their own places.

## Check before you finish

- Every line not named above is unchanged, including the version line.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
