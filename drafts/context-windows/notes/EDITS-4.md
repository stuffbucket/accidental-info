# Edits, round 4: Context Windows

Apply these edits in place to `packages/accidental-guides/guides/context-windows/guide.md`
(your working directory's `./guide.md`). Line numbers are from the file as it is now (commit
a284796, version 0.1.0). Replace each listed line with the new text, keeping the table row
structure: label cells stay as they are unless the edit gives a new label. Change nothing
else. Don't touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`
and `packages/editorial/skills/accidental-guide-write/references/voice.md`
first. Every rule there applies to any text you write or shorten.

## Why

The guide is on a new layout. Two entries now share a page, and the field marks sit on a grey
block as a grid of short answers, with no Detail column. An entry fits next to another only
if it stays short: in the entries, the What and So what rows can take about two printed lines
each. The lint also flagged a few phrases. This round drops the Detail column, trims the
entries to fit, and fixes the lint. Cut detail and repetition, not clarity: a reader who has
never thought about a context window should still follow every row. Short is not the same as
clipped: keep whole, natural sentences, and don't drop articles to save words.

## Keep exactly

- The front matter (lines 1 to 9). The version is changed separately.
- Every `#` heading line with its `{#…}` id, and the `## Field marks` and `## Confused with: …`
  lines.
- The `> ` at the start of lines. A line that starts with `> ` must still start with `> `
  after your edit, and `> [!TIP]` stays on its own line.
- The sources section (lines 133 to the end), exactly as it is.
- Typographic apostrophes (’). No backticks, no emphasis, no em dashes, no semicolons.

## What is the context window? (lines 11 to 26)

No changes.

## What takes up room? (lines 28 to 38)

1. Lines 30 to 33: rewrite without pointing at places in the picture ("at the bottom", "above
   it"): name each thing instead. Keep every idea: the startup context loads before you type
   and stays for the whole session, the conversation grows with every message, file and
   command output, compaction replaces the conversation with a short summary, and a new
   session has only the startup context. Keep the last sentence about example sizes. About 55
   words.
2. Lines 36 to 38 (the tip, keep `> ` on every line): drop the filler word "important". For
   example:
   > A crowded window can give worse answers before it’s full, because the model has more to
   > read and the details you need are harder to find. To see how full yours is, run /context
   > in Claude Code or GitHub Copilot CLI, or /status in Codex, as of October 2026.

## Token (lines 40 to 57)

3. Line 45, What: at most 22 words. Keep that a token is a short piece of text, often part of
   a word, and that window sizes, usage and prices are counted in tokens.
4. Line 46, So what: at most 30 words. Keep that the whole window is sent again on every call,
   so a large file or log costs its tokens on every later call. Keep the window sizes (as of
   October 2026, current Claude models have a 1 million token window and older ones 200,000)
   only if they fit in the budget.
5. Lines 50 to 53, field marks: drop the Detail column. Write exactly:
   > | Field | Short answer |
   > |---|---|
   > | Controlled by | The model you pick |
   > | Cannot | Be counted exactly from words |

## Startup context (lines 59 to 77)

6. Line 64, What: at most 30 words. Keep the list of what loads: the system prompt,
   instructions files, skill and sub-agent descriptions, and tool definitions, including MCP
   tools unless they load on demand.
7. Line 65, So what: at most 25 words. Keep that it is sent on every call and stays after
   compaction, and that long instructions files or many MCP servers take room before you
   begin. Start the sentence with "Startup context", not "It".
8. Lines 69 to 72, field marks: drop the Detail column. The point of the old Cannot detail (a
   procedure for one kind of task belongs in a skill, which loads only when it’s used) is
   already on the habits page, so it can go. Write exactly:
   > | Field | Short answer |
   > |---|---|
   > | Controlled by | You, your team and the harness |
   > | Cannot | Hold every procedure cheaply |
9. Lines 76 to 77, Confused with: Memory: at most 22 words, same meaning.

## Compaction (lines 79 to 97)

10. Line 83, Identify by: the lint flags "A note that" as throat-clearing. Write exactly:
    | Identify by | A message saying the conversation was compacted or summarized. |
11. Line 84, What: at most 25 words. Keep the GitHub Copilot CLI figure (about 80 percent
    full, as of October 2026).
12. Line 85, So what: at most 30 words. Keep what can be lost (early instructions, exact
    wording, full command output) and the advice to put rules that must last in an
    instructions file.
13. Lines 89 to 92, field marks: drop the Detail column. Write exactly:
    > | Field | Short answer |
    > |---|---|
    > | Controlled by | The harness and you |
    > | Cannot | Bring lost detail back |
14. Lines 96 to 97, Confused with: Trimming: at most 20 words, same meaning.

## New session (lines 99 to 116)

15. Line 104, What: at most 22 words, same meaning.
16. Line 105, So what: at most 30 words. Keep the advice to have the agent save its plan and
    progress to a file before you start a new session. The sentence about sub-agents can go:
    the habits page covers it.
17. Lines 109 to 112, field marks: drop the Detail column. Write exactly:
    > | Field | Short answer |
    > |---|---|
    > | Controlled by | You |
    > | Cannot | Recall the old conversation |

## What keeps the window useful? (lines 118 to 131)

18. Line 127, Read only what you need: the lint flags "instead of" as a contrast. Write
    exactly:
    > | Read only what you need | Ask for one function or only the failing tests. |
19. Line 131: delete it (and the blank line before it). It repeats the intro on line 120.

## Check before you finish

- Every line not named above is unchanged.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people. No question marks outside
  headings.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
