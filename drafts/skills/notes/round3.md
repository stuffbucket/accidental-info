Round 3 for the writer: the last round. Targeted edits to
packages/accidental-guides/guides/skills/guide.md (relative to the repository root).

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Why: the printed guide is 1,452 words and must come down to about 1,150. The field marks keep
only the "In context" row, since the guide is about when each part loads; the one "Cannot"
fact that matters (a reference file nobody names is never opened) moves into that row. Every
So what row has two sentences so the first can be bolded.

Apply each edit in place. Line numbers are from the file as it stands now. "Replace" means
replace the whole line with the text given, word for word. "Delete" means remove the line.
Don't change anything else. Work from the bottom of the file up so the line numbers hold.

- Line 13: Replace with:
  It’s easy to think of a skill as one Markdown file. A skill is a folder, and next to SKILL.md it can hold scripts the agent runs, reference files it reads when a step needs them, and assets such as templates.
- Line 15: Replace with:
  An Accidental Guide to: Agents, Harnesses, Skills, and Tools covers the basics. The harness loads each part of the folder only when a step needs it, so a skill can carry a lot without filling the context window.
- Line 19: Replace with:
  | Description | The name and description at the top of SKILL.md. |
- Line 20: Replace with:
  | Instructions | The steps in SKILL.md. |
- Line 21: Replace with:
  | Script | Code the agent runs for a step. |
- Line 22: Replace with:
  | Reference file | Detail the agent reads only when a step needs it. |
- Line 23: Replace with:
  | Asset | A file used in what the skill makes, such as a template. |
- Line 40: Replace with:
  | Description | SKILL.md, top | What it does and when |
- Line 41: Replace with:
  | Instructions | SKILL.md, body | The steps |
- Line 42: Replace with:
  | Script | scripts/list_changes.sh | Lists the merged pull requests |
- Line 43: Replace with:
  | Reference file | references/style.md | The team’s writing rules |
- Line 48: Replace with:
  Each step names the file it uses, so the agent knows when to open or run it.
- Line 58: Replace with:
  | A step runs the script | Script | Only what the script prints |
- Line 62: Replace with:
  The script’s code and any file no step opens never enter the context window. What does load stays for the rest of the session.
- Line 69: Replace with:
  | What | A description says what the skill does and when to use it. The agent picks a skill by matching your request to its description. |
- Line 76: Replace with:
  | In context | Every call | Used or not, each one takes room. |
- Line 77: Delete. (Now: | Cannot | Run past 1,024 characters | The standard’s limit. The detail goes in the instructions. |)
- Line 81: Replace with:
  The description decides whether the skill is used. The instructions say what to do next.
- Line 88: Replace with:
  | What | Instructions are the steps the agent follows. Each step names the file it uses. |
- Line 89: Replace with:
  | So what | The whole body loads at once and stays, so keep it under 500 lines. Move detail into reference files. |
- Line 95: Replace with:
  | In context | From first use | The whole body loads. |
- Line 96: Delete. (Now: | Cannot | Act on their own | The agent follows the steps through tools. |)
- Line 100: Replace with:
  An instructions file loads in every session. A skill’s instructions load only when the skill is used.
- Line 106: Replace with:
  | Identify by | A file in scripts/, such as list_changes.sh. |
- Line 107: Replace with:
  | What | A script is code the agent runs instead of writing it. Only what it prints enters the context window. |
- Line 108: Replace with:
  | So what | Tested code gives the same result every time. The agent doesn’t work it out again in each session. |
- Line 114: Replace with:
  | In context | Output only | The code never loads. |
- Line 115: Delete. (Now: | Cannot | Run where its tools are missing | A script that calls git or python needs them installed where the agent runs. |)
- Line 119: Replace with:
  A script is one kind of tool. The agent runs it through the shell tool.
- Line 125: Replace with:
  | Identify by | A file in references/, such as style.md. |
- Line 127: Replace with:
  | So what | A skill can hold many reference files. The agent reads only the one the task needs. |
- Line 133: Replace with:
  | In context | When a step reads it | A file no step names stays unread. |
- Line 134: Delete. (Now: | Cannot | Be found on its own | If no step names the file, the agent won’t open it. |)
- Line 138: Replace with:
  Instructions say what to do. A reference file holds the detail for one step.
- Line 144: Replace with:
  | Identify by | A template, image or data file in assets/. |
- Line 145: Replace with:
  | What | An asset is a file the skill uses in what it makes. Templates, images and lookup tables are common. |
- Line 146: Replace with:
  | So what | Each set of release notes starts from the same layout. The steps only say where to find it. |
- Line 152: Replace with:
  | In context | Only if the agent reads it | A script can fill it in without loading it. |
- Line 153: Delete. (Now: | Cannot | Change to suit a request | An asset is a fixed file. The agent or a script fills it in. |)
- Line 157: Replace with:
  A reference file is read for guidance. An asset ends up in the result.
- Line 161: Replace with:
  The folder format is an open standard, so the same skill works in Claude Code, Codex and GitHub Copilot.
- Line 165: Replace with:
  | Built in | Everyone using the harness | Claude Code’s /code-review, Codex’s system skills |
- Line 166: Replace with:
  | Your project | Everyone with the repository | .claude/skills, .github/skills or .agents/skills |
- Line 167: Replace with:
  | Your home folder | Only you, in every project | ~/.claude/skills, ~/.copilot/skills or ~/.agents/skills |
- Line 168: Replace with:
  | Plugin | Everyone who installs it | Claude Code and Codex plugins |
- Line 169: Replace with:
  | Your organization | Everyone your admins choose | Claude Code managed settings, a Claude API workspace |
- Line 175: Replace with:
  Pick by what the agent is missing.
- Line 179: Replace with:
  | Instructions file | A rule applies to every task | Use pnpm, not npm |
- Line 180: Replace with:
  | Skill | A procedure is needed for some tasks | Write release notes |
- Line 181: Replace with:
  | MCP server | The agent needs another system | Query a database |
- Line 182: Replace with:
  | Sub-agent | Side work would fill your context window | Search many files, return a summary |
- Line 184: Replace with:
  They work together: a skill can tell the agent which MCP tools to call and which sub-agents to start. When you paste the same steps into a conversation for the third time, make them a skill.
- Line 195: Delete. (Now: | Anthropic: Equipping agents for the real world with Agent Skills | October 2025 | anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills |)

When you're done, reply with one line: done.
