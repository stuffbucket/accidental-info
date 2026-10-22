# Edits to Context Windows, round 2

File: `packages/accidental-guides/guides/context-windows/guide.md`. Line numbers are from the
file as it is now (commit b66821f, version 0.1.0). Edit in place. Do not touch any line this
list doesn't name, and do not edit any other file.

The rules in `drafts/context-windows/notes/WRITER-1.md` still apply to every
word you write. No mannered prose: the writing must not call attention to itself. Make no
assumption that the reader is an expert.

The guide prints at 1,178 words. The target is about 1,100. Use the wording given here,
and don't add words anywhere else.

## Edits

1. Line 4, subtitle. Replace the value with:
   `A pocket-sized guide to what fills a coding agent’s context window, as of October 2026.`
   (The old one runs off the end page.)

2. Lines 18–19. "The four ideas below" is page talk. Replace the second sentence with:
   "These four ideas explain how the window fills up and how you keep room for the work."

3. Line 25, Compaction meaning. Compaction is something the harness does. Replace with:
   "Replacing older conversation with a summary when the window is nearly full."

4. Lines 36–37. Make the last sentence a plain instruction to the reader, such as:
   "To see how full yours is, run /context in Claude Code or GitHub Copilot CLI, or /status
   in Codex, as of October 2026."

5. Line 45, Token So what, second sentence. "other Claude models" is wrong for the reader
   who doesn't use Claude. Say: "As of October 2026, current Claude models have a 1 million
   token window, and older ones have 200,000."

6. Line 56, Confused with: Word. "part of a token" is confusing. Replace with: "A short,
   common word is often one token. A long or rare word can take several."

7. Line 63, Startup context What. The second sentence repeats "Startup context". Keep the
   first sentence. Replace the second with one that lists the same things without starting
   with "Startup context", "It" or "This", such as: "That includes the system prompt,
   instructions files, skill and sub-agent descriptions, and tool definitions, including
   MCP tools unless they load on demand."

8. Lines 75–76, Confused with: Memory. Replace with: "Memory in a harness is a file of
   notes that loads with the startup context. The model itself keeps nothing between
   calls."

9. Line 82, Compaction Identify by. Replace with: "A note that the conversation was
   compacted or summarized."

10. Line 83, Compaction What. Delete "The harness runs it automatically, or you can run
    /compact." Change the last sentence to "As of October 2026, GitHub Copilot CLI
    compacts at about 80 percent full."

11. Line 84, Compaction So what. "Compaction loses early instructions" overstates it.
    Replace the row text with: "Compaction can lose detail, such as instructions you gave
    early on, exact wording and full command output. Put rules that must last in an
    instructions file, which is still there after compaction."

12. Line 90, Controlled by detail. Replace with: "The harness compacts on its own. You can
    compact sooner and say what to keep, such as /compact focus on the login bug."

13. Lines 95–96, Confused with: Trimming. Replace with: "Trimming drops old content, such
    as old tool output, with no summary. Some harnesses trim before they compact."

14. Line 104, New session So what. "First have the agent…" is unclear about when. Replace
    the second sentence with: "Before you start one, have the agent save its plan and
    progress to a file the next session can read."

15. Line 111, Cannot detail. Repeats the So what row. Replace the detail with: "Some
    harnesses let you go back to it, such as /resume in Claude Code."

16. Lines 119–120, habits intro. Replace with: "A few habits keep the window small and on
    topic, so the model can find what matters."

17. Line 129. Delete the "Turn off unused MCP servers" row. The Startup context entry
    already says it.

18. Line 130, Compact at a natural break. Replace the Why cell with: "When one part of the
    work is done, run /compact and say what to keep."

19. Lines 132–133, habits closing. Replace with: "Each habit keeps old or unneeded material
    out of the window, which leaves room for the work you’re doing now."

## When you finish

Check that no table cell has a "|" in it, that Short answer cells don't end with a full
stop, and that nothing else changed (`git diff`). Reply with a one-line summary.
