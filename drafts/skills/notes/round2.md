Round 2 for the writer: targeted edits to packages/accidental-guides/guides/skills/guide.md
(relative to the repository root). Apply each edit in place. Line numbers are from the file as
it stands now; replace the whole line or table row named. Where a replacement is given, use it
word for word unless it breaks a rule in the plan; then fix it the smallest way and say so.
Don't change anything else.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Why: the printed guide is 1,332 words and must come down to about 1,150. Several rows repeat
the base guide (for example "check the description first"), and some labels say "it" with
nothing for "it" to point to.

Front matter
- Line 4: subtitle: A pocket-sized guide to what a skill folder can hold, as of October 2026.

{#why}
- Line 13: It’s easy to think of a skill as one Markdown file, SKILL.md. A skill is a folder, and next to SKILL.md it can hold scripts the agent runs, reference files it reads when a step needs them, and assets such as templates.
- Line 15: An Accidental Guide to: Agents, Harnesses, Skills, and Tools covers the basics. The rest of the folder matters for two reasons: the harness loads each file only when a step needs it, and a script gives the same result every time without the agent working it out again.
- Line 19 row: | Description | The name and description at the top of SKILL.md, which the agent matches your request against. |
- Line 21 row: | Script | Code in the folder that the agent runs for a step. |
- Line 22 row: | Reference file | Documentation the agent reads only when a step needs it. |
- Line 23 row: | Asset | A file the skill uses in what it makes, such as a template. |

{#fit}
- Line 31: "  requests. Use when preparing a release." (keep the two leading spaces)
- Line 33: 1. Run scripts/list_changes.sh to list the changes.
- Line 40 row caption: Says what it does and when
- Line 44 row caption: The layout of the notes
- Line 46: SKILL.md is the only file a skill needs.
- Line 48: Each step names the file it uses, so the agent knows what each file is for and when to open or run it.

{#ctx}
- Line 52: The harness loads a skill in stages, as each step needs it. The Agent Skills standard calls this progressive disclosure.
- Lines 56 to 60, the five rows, become:
  | Session starts | Description | Every skill’s name and description |
  | Your request matches | Instructions | The rest of SKILL.md |
  | A step runs the script | Script | Only what list_changes.sh prints |
  | A step needs the rules | Reference file | references/style.md |
  | A step fills in the template | Asset | assets/template.md |
- Line 62: The script’s code and any file no step opens never enter the context window, so a big skill costs little until it’s used. What does load stays for the rest of the session.

Description
- Line 69 What: A description says what the skill does and when to use it. The agent reads every skill’s description and picks the one that matches your request.
- Line 70 So what: Name the task and the words people use for it. Some harnesses shorten long descriptions, so put the main use first.
- Line 76 row: | In context | Every call | Used or not, each description takes room. |
- Line 77 row: | Cannot | Run past 1,024 characters | The standard’s limit. The detail goes in the instructions. |
- Line 81: The description decides whether the skill is used. The instructions say what to do once it is.

Instructions
- Line 87 Identify by: The Markdown under the description in SKILL.md.
- Line 88 What: Instructions are the steps the agent follows. Each step names the script, reference file or asset it uses.
- Line 89 So what: The same task gets done the same way each time. The whole body loads at once and stays, so keep it under 500 lines and move detail into reference files.
- Line 95 row: | In context | From first use | The whole body loads at once. |

Script
- Line 106 Identify by: A file in scripts/, such as scripts/list_changes.sh.
- Line 107 What: A script is code the agent runs instead of writing it. The agent runs it through the shell tool, and only what it prints enters the context window.
- Line 108 So what: Code someone wrote and tested gives the same result every time. The agent doesn’t work the task out again in each session, which saves time and room in the context window.
- Line 114 row: | In context | Output only | The code itself never loads. |
- Line 115 row: | Cannot | Run where its tools are missing | A script that calls git or python needs them installed where the agent runs. |

Reference file
- Line 126 What: A reference file holds detail that only some requests need. The agent opens it when a step says to.
- Line 127 So what: A skill can hold many reference files, and the agent opens only the one the task needs. SKILL.md stays short.
- Line 133 row: | In context | When a step reads it | Files no step opens take no room. |
- Line 134 row: | Cannot | Be found on its own | If no step names the file, the agent won’t open it. |

Asset
- Line 145 What: An asset is a file the skill uses in what it makes. Assets include templates, images, lookup tables and schemas.
- Line 146 So what: Each set of release notes starts from the same layout. A script can also fill in an asset without the agent reading it.
- Line 152 row: | In context | Only if the agent reads it | A script that copies or fills in the file uses no room. |
- Line 153 row: | Cannot | Change to suit a request | An asset is a fixed file. The agent or a script fills it in. |

{#shared}
- Line 161: The folder format is an open standard, so the same skill folder can be used in Claude Code, Codex and GitHub Copilot. Where you put it decides who gets it.
- Lines 165 to 169, the five rows, become:
  | Built in | Everyone using that harness | Claude Code’s /code-review and /debug, and Codex’s system skills |
  | Your project | Everyone with the repository | .claude/skills, .github/skills or .agents/skills, committed with the code |
  | Your home folder | You, in every project on that machine | ~/.claude/skills, ~/.copilot/skills or ~/.agents/skills |
  | Plugin | Everyone who installs the plugin | Claude Code and Codex plugins, which can bundle several skills |
  | Your organization | Everyone your admins set up | Claude Code managed settings, Codex’s /etc/codex/skills or a Claude API workspace |
- Line 171: Read every file in a skill from someone else before you use it, as you would any program you install. Shared collections include anthropics/skills and github/awesome-copilot.

{#choose}
- Line 175: Choose by what you need: standing rules, a procedure, a connection to another system, or a separate context window.
- Lines 179 to 182, the four rows, become:
  | Instructions file | A fact or rule applies to every task | Use pnpm, not npm |
  | Skill | A procedure or reference is needed for some tasks | Write release notes the same way each time |
  | MCP server | The agent needs to reach another system | Query a database or post to a chat channel |
  | Sub-agent | Side work would fill your context window | Search many files and return a summary |
- Line 184: They work together. A skill can tell the agent which MCP tools to call and which sub-agents to start. When you paste the same steps into a conversation for the third time, or a section of your instructions file has grown into a procedure, make it a skill.

{#sources}
- Line 188: These public pages were checked in October 2026.
- Source names (first column only), lines 192 to 200, in order: Agent Skills specification; Anthropic: Agent Skills; Anthropic: Skill authoring best practices; Anthropic: Equipping agents for the real world with Agent Skills; Claude Code: Skills; Claude Code: Extend Claude Code; GitHub: About agent skills; VS Code: Agent skills; OpenAI: Build skills.

When you're done, reply with one line: done.
