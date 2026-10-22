# Edits to Context Windows, round 3

File: `packages/accidental-guides/guides/context-windows/guide.md`. Line numbers are from the
file as it is now (commit 958e3be). Edit in place. Do not touch any line this list doesn't
name, and do not edit any other file.

The rules in `drafts/context-windows/notes/WRITER-1.md` still apply. No
mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

The guide prints at 1,177 words. These edits are cuts and small fixes toward about 1,100.
Use the wording given, and don't add words anywhere else.

## Edits

1. Line 24, Startup context meaning. Replace with: "What the harness loads before your
   first message."

2. Line 45, Token So what, first sentence. "Every call resends the window" reads as if the
   window itself is sent. Replace the first sentence with: "Everything in the window is
   sent again on every call, so a large file or log costs its tokens on every later call."
   Keep the second sentence.

3. Line 70, Startup context Controlled by detail. Replace with: "You choose the
   instructions files and MCP servers. The harness writes the system prompt."

4. Line 123, Why cell. Replace with: "A new session gives the next task the whole window."

5. Line 124, Why cell. Replace with: "A file carries what matters into the next session."

6. Lines 130–131, closing paragraph. Replace with: "Each habit leaves more room for the
   work you’re doing now."

7. Lines 145 and 146. Delete the rows "GitHub, Optimizing AI usage" and "Visual Studio
   Code, Context". Their facts are in the other sources.

## When you finish

Check `git diff` shows only these changes. Reply with a one-line summary.
