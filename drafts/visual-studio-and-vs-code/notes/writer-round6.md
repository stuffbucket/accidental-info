# Edits, round 6: VS Code and Visual Studio

Apply these edits in place to `packages/accidental-guides/guides/visual-studio-and-vs-code/guide.md`
(your working directory's `./guide.md`). Line numbers are from the file as it is now (after
round 5, version 0.1.1, 198 lines). Replace each listed line with the new text, keeping the
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

After round 5 the guide is about 1,170 printed words without the sources page, and two entries
still don't fit on one page together. Each entry can have about eight lines of text in its four
rows. This round takes a line or two out of the longer entries and cuts a few repeated words on
the later pages, which brings the guide to about 1,100 words.

## Page 2

1. Line 15: VS Code’s default harness, the Copilot harness, reads .github/ in the repo and ~/.copilot/ in your home folder. For the basics, see An Accidental Guide to: Agents, Harnesses, Skills, and Tools.

## Entries

2. Line 29: | Identify by | copilot-instructions.md, AGENTS.md or a .instructions.md file. |
3. Line 31: | So what | Put rules you’d otherwise repeat in every chat here. An applyTo pattern makes a file apply only to matching files. |
4. Line 46: | Identify by | A .agent.md file, or a name in the Agent dropdown. |
5. Line 47: | What | A custom agent is a saved role with its own instructions, tools and model. See An Accidental Guide to: Agents, Harnesses, Skills, and Tools. |
6. Line 55: ## Confused with: Chat mode
7. Line 57: Chat mode is the old name for a custom agent, and a .chatmode.md file can be renamed to .agent.md.
8. Line 64: | What | A skill is a written procedure in a folder. Type /skill-name to run one. See An Accidental Guide to: Agent Skills. |
9. Line 74: A prompt file (.prompt.md) is a saved prompt you run with /name. Only the Local harness runs them, so VS Code suggests a skill.
10. Line 81: | What | An MCP server is a program that gives the agent more tools. Search @mcp in Extensions to find one. See An Accidental Guide to: Model Context Protocol. |
11. Line 99: | So what | When something works for a teammate and not for you, compare your settings. |

## How scopes combine

12. Line 145: | Custom agent | The selected agent’s instructions win a conflict. |
13. Line 146: | MCP server | Give each server its own name. Your organization can limit which ones run. |

## What’s different in Visual Studio

14. Line 164: Visual Studio doesn’t list AGENTS.md as supported, so put rules both editors need in .github/copilot-instructions.md.

## Same thing elsewhere

15. Line 168: Copilot CLI uses the same Copilot harness, so it reads the same .github/ and ~/.copilot/ folders.

## Check before you finish

- Every line not named above is unchanged, including the version line.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
