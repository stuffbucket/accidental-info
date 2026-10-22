# Sources for An Accidental Guide to… Agent Skills

All fetched 22 October 2026. Excerpts are verbatim and short. Only public, official
documentation. Nothing internal.

## 1. Agent Skills specification

agentskills.io, "Specification". https://agentskills.io/specification

- Folder: "A skill is a directory containing, at minimum, a `SKILL.md` file" with optional
  `scripts/` ("Optional: executable code"), `references/` ("Optional: documentation") and
  `assets/` ("Optional: templates, resources").
- Frontmatter: `name` "Max 64 characters. Lowercase letters, numbers, and hyphens only." and
  "Must match the parent directory name". `description` "Max 1024 characters. Non-empty.
  Describes what the skill does and when to use it." Optional: `license`, `compatibility`,
  `metadata`, `allowed-tools` ("Experimental").
- Body: "The Markdown body after the frontmatter contains the skill instructions. There are
  no format restrictions." "the agent will load this entire file once it's decided to
  activate a skill."
- scripts/: "Contains executable code that agents can run." "Common options include Python,
  Bash, and JavaScript."
- references/: "additional documentation that agents can read when needed" ...
  "Agents load these on demand, so smaller files mean less use of context."
- assets/: "Templates (document templates, configuration templates)", "Images (diagrams,
  examples)", "Data files (lookup tables, schemas)".
- Progressive disclosure: "1. Metadata (~100 tokens): The `name` and `description` fields
  are loaded at startup for all skills 2. Instructions (< 5000 tokens recommended): The full
  `SKILL.md` body is loaded when the skill is activated 3. Resources (as needed): Files ...
  are loaded only when required". "Keep your main `SKILL.md` under 500 lines."
- "Keep file references one level deep from `SKILL.md`."

agentskills.io, "Agent Skills Overview". https://agentskills.io/home

- "Agent Skills are a lightweight, open format for extending AI agent capabilities with
  specialized knowledge and workflows."
- "Skills can also bundle scripts, reference materials, templates, and other resources."
- Three stages: "Discovery", "Activation", "Execution: The agent follows the instructions,
  optionally executing bundled code or loading referenced files as needed."
- "The Agent Skills format was originally developed by Anthropic, released as an open
  standard, and has been adopted by a growing number of agent products."

## 2. Anthropic: Agent Skills overview

Claude Platform docs, "Agent Skills".
https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

- Level table: Metadata "Always (at startup)", "~100 tokens per Skill"; Instructions "When
  Skill is triggered", "Under 5k tokens"; Resources "As needed", "None until accessed",
  "Reference files load into context when read. Scripts run through bash, and only their
  output enters context."
- "When Claude runs `validate_form.py`, the script's code never loads into the context
  window. Only its output ... consumes tokens, which makes scripts far more efficient than
  having Claude generate equivalent code during the task."
- "A Skill can include dozens of reference files, but if your task only needs the sales
  schema, that's the one file Claude loads."
- "instructions for flexible guidance, code for reliability, resources for factual lookup."
- Sharing scope: "claude.ai: Individual user only." "Claude API: Workspace-wide." "Claude
  Code: Personal (`~/.claude/skills/`) or project-based (`.claude/skills/`). Can also be
  shared through Claude Code Plugins." "Custom Skills do not sync across surfaces".
- Security: "Use Skills only from trusted sources" ... "a malicious Skill can direct Claude
  to call tools or run code in ways that don't match the Skill's stated purpose." "Treat like
  installing software". "Review all files bundled in the Skill: `SKILL.md`, scripts, images,
  and other resources."

## 3. Anthropic: Skill authoring best practices

https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

- "Even if Claude could write a script, pre-made scripts offer advantages: Are more reliable
  than generated code; Save tokens (no need to include code in context); Save time (no code
  generation required); Ensure consistency across uses".
- "Make clear in your instructions whether Claude should: Run the script (most common) ...
  Read it as reference (for complex logic)".
- "Prefer scripts for deterministic operations: Write `validate_form.py` rather than asking
  Claude to generate validation code."
- "The context window is a public good."
- "Claude uses it to choose the right Skill from potentially 100+ available Skills."
- Template pattern: "Provide templates for output format."

## 4. Anthropic engineering blog

"Equipping agents for the real world with Agent Skills", 16 October 2025 (note added
18 December 2025: published as an open standard).
https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

- "sorting a list via token generation is far more expensive than simply running a sorting
  algorithm."
- "because code is deterministic, this workflow is consistent and repeatable."
- "the amount of context that can be bundled into a skill is effectively unbounded."
- "We recommend installing skills only from trusted sources."

## 5. Claude Code: skills

https://code.claude.com/docs/en/skills

- Locations: Enterprise (managed settings), Personal `~/.claude/skills/<skill-name>/SKILL.md`,
  Project `.claude/skills/<skill-name>/SKILL.md` ("Commit it so your team gets it too"),
  Plugin `<plugin>/skills/<skill-name>/SKILL.md`.
- "Unlike CLAUDE.md content, a skill's body loads only when it's used, so long reference
  material costs almost nothing until you need it."
- "Every skill in the skill listing adds to your context on every turn, whether or not
  Claude ever uses it."
- Folder example: "scripts/helper.py (utility script - executed, not loaded)".
- "Once a skill loads, its content stays in context across turns, so every line is a
  recurring token cost."
- "Create a skill when you keep pasting the same instructions, checklist, or multi-step
  procedure into chat, or when a section of CLAUDE.md has grown into a procedure rather than
  a fact."
- `disable-model-invocation: true` "to prevent Claude from automatically loading this
  skill"; `context: fork` runs a skill in a subagent.
- "Claude Code skills follow the Agent Skills open standard".

## 6. Claude Code: extend Claude Code (features overview)

https://code.claude.com/docs/en/features-overview

- CLAUDE.md "Persistent context loaded every conversation"; "Project conventions, 'always do
  X' rules".
- Skill vs subagent: skill "Adds to your main window"; subagent "Uses a separate window".
- "MCP connects Claude to external services. Skills extend what Claude knows, including how
  to use those services effectively."
- "Skill + MCP: MCP provides the connection; a skill teaches Claude how to use it well".
- "A plugin bundles skills, hooks, subagents, and MCP servers into a single installable unit."
- Trigger table: "You paste the same playbook or multi-step procedure into chat for the third
  time: Capture it as a skill".

## 7. GitHub Copilot: about agent skills

https://docs.github.com/en/copilot/concepts/agents/about-agent-skills (no date shown)

- Skills are "folders of instructions, scripts, and resources that Copilot can load when
  relevant".
- Project skills: `.github/skills`, `.claude/skills`, or `.agents/skills`. Personal skills:
  `~/.copilot/skills` or `~/.agents/skills`.
- Release notes example: a skill "can include your team's template, a script for gathering
  changes, and instructions for grouping them".
- Shared sources: `anthropics/skills`, `github/awesome-copilot`; "use `gh skill` in GitHub
  CLI to discover and install skills from GitHub repositories".
- Surfaces: Copilot app, Copilot CLI, cloud agent and code review, agent mode in VS Code,
  Visual Studio and JetBrains IDEs.

## 8. VS Code: agent skills

https://code.visualstudio.com/docs/copilot/customization/agent-skills (updated 10/21/2026)

- "If a file isn't referenced in the instructions, it won't be loaded."
- Skills vs custom instructions: Skills "Teach specialized capabilities and workflows",
  "Instructions, scripts, examples, and resources", "Task-specific, loaded on-demand".
  Custom instructions "Define coding standards and guidelines", "Instructions only", "Always
  applied (or via glob patterns)".
- "Always review shared skills before using them"; "Copy the skill directory to your
  `.github/skills/` folder".
- "Type `/` in the chat input field to see a list of available skills".

## 9. OpenAI Codex: build skills

https://learn.chatgpt.com/docs/build-skills (redirected from developers.openai.com/codex/skills;
no date shown)

- "A skill is a directory with a `SKILL.md` file plus optional scripts and references."
- Locations: repo `.agents/skills` (every directory up to the repository root), user
  `$HOME/.agents/skills`, admin `/etc/codex/skills`, system "Bundled with Codex by OpenAI".
- "In Codex, the initial list also includes each skill's file path." Budget "at most 2% of
  the model's context window".
- Invocation: "run `/skills` or type `$` to mention a skill"; implicit when "your task matches
  the skill `description`".
- "Prefer instructions over scripts unless you need deterministic behavior or external
  tooling."
- `$skill-installer`; "For reusable distribution of your own skills, prefer plugins."
