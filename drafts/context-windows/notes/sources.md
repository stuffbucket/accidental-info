# Sources for An Accidental Guide to… Context Windows

All fetched on 22 October 2026. Excerpts are verbatim. Public material only. People are not
named in the guide's body; publishers appear on the Sources page.

## Anthropic: Claude Code, Explore the context window

code.claude.com/docs/en/context-window

- "Claude Code's context window holds everything Claude knows about your session: your
  instructions, the files it reads, its own responses, and content that never appears in
  your terminal."
- "Before you type anything: CLAUDE.md, auto memory, MCP tool names, and skill descriptions
  all load into context."
- "a subagent handles the research in its own separate context window, so the large file
  reads stay out of yours. Only the summary and a small metadata trailer come back."
- "you run /compact, which replaces the conversation with a structured summary. Most
  startup content reloads automatically"
- What survives compaction (table): "System prompt and output style | Both still apply";
  "Project-root CLAUDE.md and unscoped rules | Re-injected from disk"; "Files Claude read or
  edited | Claude Code re-reads up to five, most recently modified first"; "Context that
  hooks added earlier | Summarized with the rest of the conversation".
- "Claude Code compacts automatically as you approach the limit, so a full context window
  doesn't end your session."
- "Compact with a focus: run /compact with instructions, like /compact focus on the auth bug
  fix, before starting a long new task. The summary keeps what you choose instead of what
  the automatic pass guesses is important."
- "Clear between tasks: run /clear when switching to unrelated work. Old conversation crowds
  out the files you need next and costs tokens on every message."
- "Delegate large reads: send research to a subagent so the file contents stay in its
  context window, not yours."
- "run /context for a live breakdown by category"

## Anthropic: Claude Code, How Claude Code works

code.claude.com/docs/en/how-claude-code-works

- "Claude's context window holds your conversation history, file contents, command outputs,
  CLAUDE.md, auto memory, loaded skills, and system instructions. As you work, context fills
  up. Claude compacts automatically, but instructions from early in the conversation can get
  lost. Put persistent rules in CLAUDE.md"
- "It clears older tool outputs first, then summarizes the conversation if needed. Your
  requests and key code snippets are preserved; detailed instructions from early in the
  conversation may be lost."
- "Sessions are independent. Each new session starts with a fresh context window, without
  the conversation history from previous sessions."
- "Subagents work in their own context window. A subagent starts fresh unless it's a fork
  ... Either way, the subagent's tool calls stay out of your context, and Claude gets back a
  summary when the subagent finishes."

## Anthropic: Claude Code, Manage costs effectively

code.claude.com/docs/en/costs

- "Token costs scale with context size: the more context Claude processes, the more tokens
  you use."
- "Clear between tasks: Use /clear to start fresh when switching to unrelated work. Stale
  context wastes tokens on every subsequent message."
- "/compact Focus on code samples and API usage tells Claude what to preserve during
  summarization."
- "MCP tool definitions are deferred by default, so only tool names and server instructions
  enter context until Claude uses a specific tool. Run /context to see what's consuming
  space."
- "Disable unused servers: Run /mcp to see configured servers and disable any you're not
  actively using."
- "Your CLAUDE.md file is loaded into context at session start. If it contains detailed
  instructions for specific workflows ... those tokens are present even when you're doing
  unrelated work. Skills load on-demand only when invoked ... Aim to keep CLAUDE.md under
  200 lines"
- "Instead of Claude reading a 10,000-line log file to find errors, a hook can grep for
  ERROR and return only matching lines, reducing context from tens of thousands of tokens
  to hundreds."
- "Delegate these to subagents so the verbose output stays in the subagent's context while
  only a summary returns to your main conversation."
- "Compaction: /compact reads the conversation it summarizes, so compacting a large context
  is itself a large request. When you want a fresh start instead of continuity, /clear costs
  nothing"

## Anthropic: Context windows (Claude API docs)

platform.claude.com/docs/en/build-with-claude/context-windows

- "The "context window" refers to all the text a language model can reference when
  generating a response, including the response itself."
- "more context isn't automatically better. As token count grows, accuracy and recall
  degrade, a phenomenon known as context rot."
- "Everything in the request counts toward the context window: the system prompt, every
  message in messages (including tool results, images, and documents), and your tool
  definitions."
- "Claude ... Opus 5.5 ... Sonnet 5.5 ... Haiku 5.5 ... have a 1M-token context window ...
  Other Claude models, including Claude Sonnet 4.5 (deprecated), have a 200k-token context
  window."
- "Compaction automatically summarizes earlier parts of the conversation on the server, so
  the conversation can continue past the context window limit."

## Anthropic: Glossary

platform.claude.com/docs/en/about-claude/glossary

- "Tokens are the smallest individual units of a language model, and can correspond to
  words, subwords, characters, or even bytes"
- "For Claude, the number of characters a token represents depends on the model and the
  language." Earlier models: "a token represents approximately 3.5 English characters";
  newer tokenizer "produces approximately 30 percent more tokens for the same text".

## Anthropic: Effective context engineering for AI agents (29 September 2025)

anthropic.com/engineering/effective-context-engineering-for-ai-agents

- "Context, therefore, must be treated as a finite resource with diminishing marginal
  returns."
- "Compaction is the practice of taking a conversation nearing the context window limit,
  summarizing its contents"
- "a technique where the agent regularly writes notes persisted to memory outside of the
  context window"
- sub-agent "returns only a condensed, distilled summary of its work (often 1,000-2,000
  tokens)"
- "One of the safest lightest touch forms of compaction is tool result clearing"

## GitHub: About context management (Copilot docs)

docs.github.com/en/copilot/concepts/prompting-and-context/context-management

- holds "every message you send, every response from Copilot, every tool call and its
  result, and the system instructions"; "Tool results can be especially large"
- CLI compaction begins "when your conversation reaches approximately 80% of the context
  window's capacity"
- "Replaces the old conversation history with the summary, along with any original user
  instructions"
- lost: "fine-grained details—such as the exact wording of every message, the full output of
  every command"; "You can't reverse a completed compaction."
- "use /context to check usage for the current session"
- start a new session when "You're switching to an unrelated task", "a clean context window
  means more space for the new task"
- "Copilot can delegate work to subagents, which have context windows separate from the main
  agent."

## GitHub: Optimizing AI usage (Copilot docs)

docs.github.com/en/copilot/tutorials/optimize-ai-usage

- "A long thread carries its entire history into every new request."
- "In Copilot CLI use /new (or /clear)"
- "Large tool sets (for example, a full MCP server's worth of tools) add to the context on
  every request." "enable only the toolsets relevant to the task."
- "Subagents run in their own session and don't inherit the main agent's conversation
  history."

## GitHub: Copilot CLI best practices

docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices

- "/context" shows "System/tools tokens," "Message history tokens," "Free space," and
  "Buffer allocation."
- "Use /clear or /new between unrelated tasks." "This resets context and improves response
  quality."

## Visual Studio Code: Context (Copilot concepts)

code.visualstudio.com/docs/copilot/concepts/context

- "The context window is the maximum amount of information a language model can process in
  one request."
- "The user message, conversation history, instructions, referenced files, and tool outputs
  all use space in this window."
- "When a conversation approaches the limit, VS Code automatically compacts older parts of
  the conversation into a summary." "details from earlier messages might be summarized or
  omitted"
- "Neither action removes saved files, applicable custom instructions, or persistent memory."
- "An agent can delegate a focused task to a subagent that works in its own context and
  returns a result."

## OpenAI: Codex commands

learn.chatgpt.com/docs/developer-commands?surface=cli (redirected from
developers.openai.com/codex/cli/slash-commands)

- /compact: "Summarize the visible chat to free tokens." "Codex replaces earlier turns with a
  concise summary, freeing context while keeping critical details."
- /new: "Reset the chat context without leaving the CLI when you want a fresh prompt in the
  same repo."
- /status: "Confirm the active model, approval policy, writable roots, and remaining context
  capacity."

## OpenAI: Compaction (API docs)

developers.openai.com/api/docs/guides/compaction

- "reduce context size while preserving state needed for subsequent turns"
- "When the rendered token count crosses the configured threshold, the server runs
  server-side compaction."

## Practitioner background (not quoted or named in the body)

Chroma, Context Rot: How Increasing Input Tokens Impacts LLM Performance (14 July 2025),
trychroma.com/research/context-rot

- "model performance varies significantly as input length changes, even on simple tasks."
- "Across all experiments, model performance consistently degrades with increasing input
  length."

HumanLayer, Getting AI to Work in Complex Codebases (2025),
github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md

- "keeping utilization in the 40%-60% range (depends on complexity of the problem )"
- "Write everything we did so far to progress.md, ensure to note the end goal, the approach
  we're taking"
- "Subagents are about context control." "use a fresh context window to do
  finding/searching/summarizing"

## Notes for the writer

- Not used: OpenAI's tokens help article returned 403.
- Products differ and change often: say "as of October 2026" for thresholds and commands.
- Commands, as of October 2026: /context (Claude Code, Copilot CLI), /status (Codex), /compact
  (all three and VS Code), /clear (Claude Code, Copilot CLI, Codex), /new (Copilot CLI, Codex).
