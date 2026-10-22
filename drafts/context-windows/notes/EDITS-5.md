# Edits, round 5: Context Windows

Apply these edits in place to `packages/accidental-guides/guides/context-windows/guide.md`
(your working directory's `./guide.md`). Line numbers are from the file as it is now (after
round 4, version 0.1.0). Replace each listed line with the new text, keeping the table row
structure: label cells stay as they are. Change nothing else. Don't touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`
and `packages/editorial/skills/accidental-guide-write/references/voice.md`
first. Every rule there applies to any text you write or shorten.

## Why

Two entries share a page only if each one is short enough, and none of them is yet. The
entries need to lose about two printed lines each. A printed line in a What or So what row
holds about 50 characters, and in Identify by or Confused with about 60. Field marks answers
sit in narrow columns that hold about 22 characters a line.

The builder also prints the first sentence of What and So what in bold, as the row's short
answer. A row with one long sentence prints with no bold. So each What and So what row is
two sentences: a short first sentence that answers the row on its own, then one more.

The examples below fit the budgets. Use them, or write your own that say the same and fit.
Keep whole, natural sentences. Don't drop articles to save characters.

## Token (lines 40 to 57)

1. Line 45, What: two sentences, at most 100 characters. For example:
   | What | A token is a short piece of text. Window sizes, usage and prices are all counted in tokens. |
2. Line 46, So what: two sentences, at most 105 characters. For example:
   | So what | The whole window is sent on every call. A large file or log costs its tokens again on every later call. |
3. Line 53: `> | Cannot | Be counted from words |`

## Startup context (lines 59 to 77)

4. Line 64, What: two sentences, at most 150 characters. Keep the four things that load. For
   example:
   | What | Startup context is what the harness loads first. That’s the system prompt, instructions files, skill and sub-agent descriptions, and tool definitions. |
5. Line 65, So what: two sentences, at most 110 characters. Keep that startup context is sent on
   every call and that long instructions files or many MCP servers take room. For example:
   | So what | Startup context is sent on every call. Long instructions files and many MCP servers take room before you start. |
6. Line 71: `> | Controlled by | You and the harness |`

## Compaction (lines 79 to 96)

7. Line 83, Identify by: at most 55 characters. For example:
   | Identify by | A message saying the conversation was compacted. |
8. Line 84, What: two sentences, at most 125 characters. Keep the GitHub Copilot CLI figure and
   "as of October 2026". For example:
   | What | Compaction swaps older conversation for a summary. GitHub Copilot CLI does it at about 80 percent full, as of October 2026. |
9. Line 85, So what: two sentences, at most 110 characters. For example:
   | So what | Compaction can lose early instructions and exact output. Rules that must last belong in an instructions file. |

## New session (lines 98 to 115)

10. Line 104, So what: two sentences, at most 100 characters. For example:
    | So what | A fresh window has room for a new task. Have the agent save its plan and progress to a file first. |

## Check before you finish

- Every line not named above is unchanged.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people. No question marks outside
  headings.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
