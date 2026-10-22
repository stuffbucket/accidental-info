# Accidental Guides

Short guides to AI coding agents and the ways teams use them to build software. Each one
answers one question, a few parts at a time, and uses one name for each thing in every
guide.

**Read them at https://stuffbucket.github.io/accidentalguide/**, or download the PDF or
Word document of each.

## Guides

<!-- guides:start -->
| Guide | What it covers | Version | Download |
| --- | --- | --- | --- |
| [Accidental Intelligence](https://stuffbucket.github.io/accidentalguide/guides/accidental-intelligence/) | A pocket-sized guide to the Accidental Guides, as of October 2026. | 0.3.0 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/accidental-intelligence.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/accidental-intelligence.docx) |
| [Agents, Harnesses, Skills, and Tools](https://stuffbucket.github.io/accidentalguide/guides/agents-harnesses-skills-tools/) | A pocket-sized guide to the AI coding systems of mid-October 2026 (morning edition). | 1.0.0 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/agents-harnesses-skills-tools.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/agents-harnesses-skills-tools.docx) |
| [Specs and Reviews](https://stuffbucket.github.io/accidentalguide/guides/specs-and-reviews/) | A pocket-sized guide to agreeing on work as a team and checking when it’s done. | 0.4.0 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/specs-and-reviews.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/specs-and-reviews.docx) |
| [Software Factories](https://stuffbucket.github.io/accidentalguide/guides/software-factories/) | A pocket-sized guide to software delivery run by coding agents, as of October 2026. | 0.1.0 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/software-factories.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/software-factories.docx) |
| [Lights-Off Software Factories](https://stuffbucket.github.io/accidentalguide/guides/lights-off-software-factories/) | A pocket-sized guide to software factories where nobody reads the code, as of October 2026. | 0.3.0 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/lights-off-software-factories.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/lights-off-software-factories.docx) |
<!-- guides:end -->

## Drafts

Guides still being written, in `drafts/`. Their words and parts may change.
[Suggestions are welcome](https://github.com/stuffbucket/accidentalguide/issues).

<!-- drafts:start -->
| Guide | What it covers | Version | Download |
| --- | --- | --- | --- |
| [Claude Code](https://stuffbucket.github.io/accidentalguide/drafts/claude-code/) | A pocket-sized guide to where Claude Code keeps its setup, as of October 2026. | 0.1.1 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/claude-code.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/claude-code.docx) |
| [Claude Desktop](https://stuffbucket.github.io/accidentalguide/drafts/claude-desktop/) | A pocket-sized guide to where Claude Desktop keeps its settings, as of October 2026. | 0.1.1 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/claude-desktop.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/claude-desktop.docx) |
| [OpenAI Codex](https://stuffbucket.github.io/accidentalguide/drafts/codex/) | A pocket-sized guide to where Codex keeps its setup, and which copy wins, as of October 2026. | 0.1.0 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/codex.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/codex.docx) |
| [Context Windows](https://stuffbucket.github.io/accidentalguide/drafts/context-windows/) | A pocket-sized guide to what fills a coding agent’s context window, as of October 2026. | 0.1.0 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/context-windows.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/context-windows.docx) |
| [GitHub Copilot CLI](https://stuffbucket.github.io/accidentalguide/drafts/copilot-cli/) | A pocket-sized guide to where Copilot CLI keeps its setup, and which copy wins, as of October 2026. | 0.1.0 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/copilot-cli.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/copilot-cli.docx) |
| [Model Context Protocol](https://stuffbucket.github.io/accidentalguide/drafts/mcp/) | A pocket-sized guide to MCP servers and clients, as of October 2026. | 0.1.0 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/mcp.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/mcp.docx) |
| [Plugins, Connectors, and Marketplaces](https://stuffbucket.github.io/accidentalguide/drafts/plugins-and-marketplaces/) | A pocket-sized guide to the names for things you add to a coding agent or AI app. | 0.1.0 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/plugins-and-marketplaces.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/plugins-and-marketplaces.docx) |
| [Agent Skills](https://stuffbucket.github.io/accidentalguide/drafts/skills/) | A pocket-sized guide to what a skill folder can hold, as of October 2026. | 0.1.0 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/skills.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/skills.docx) |
| [VS Code and Visual Studio](https://stuffbucket.github.io/accidentalguide/drafts/visual-studio-and-vs-code/) | A pocket-sized guide to where GitHub Copilot’s agent setup lives, as of October 2026. | 0.1.1 | [PDF](https://stuffbucket.github.io/accidentalguide/guides/visual-studio-and-vs-code.pdf) · [Word](https://stuffbucket.github.io/accidentalguide/guides/visual-studio-and-vs-code.docx) |
<!-- drafts:end -->

## Contributing

Suggest a guide, report a wrong fact or a word used two ways, or start a draft. See
[CONTRIBUTING.md](CONTRIBUTING.md) for how, and for the rules the guides' text follows.

## How the guides are built

This is a pnpm and Turborepo workspace:

| Folder | What it holds |
| --- | --- |
| `guides/<slug>/` | A finished guide: `guide.md` (the text), `content.py` (reads it), `build_guide.py` (the PDF layout), `build_docx.py` (the Word layout), `fonts/` and `expected.sha256` |
| `drafts/<slug>/` | A guide still being written, laid out the same way |
| `packages/pipeline/` | Builds one guide into its `dist/`: the PDF, the Word document and `guide.json`. Also pins the Python packages and keeps the workspace's `package.json` files in step |
| `site/` | The Astro and Starlight site. It turns each guide's text into a page, and its landing page lists every guide |

Tool versions are in `mise.toml`. Package registries come from your own `~/.npmrc` and pip
configuration; the repository sets none.

```sh
mise install            # Node, pnpm and Python
pnpm install
pnpm build              # every guide, then the site (site/dist/)
pnpm test
pnpm preview            # http://localhost:4321/accidentalguide/
```

A guide's build fails if a page has content past its bottom margin, or if its PDF differs
from its `expected.sha256`. The Pages workflow runs the same build on every push to `main`
and deploys the site.

### Editing a guide

Change the text in the guide's `guide.md`, then build. Each guide's README describes its
Markdown. Bump the `version:` in the front matter (semver) when the text changes, and
write the new PDF's hash into `expected.sha256`.

- **The Markdown holds the words**, and the data a diagram is drawn from. It has no layout
  in it.
- **Each output has its own layout:** `build_guide.py` for the PDF and `build_docx.py` for
  the Word document, which imports the PDF's visual rules.
- **Diagrams are drawn once,** by the PDF build. The Word document and the site use
  images of them rendered from the built PDF, so they never disagree.
- **The PDF is the oracle.** Its build is deterministic, so a change that alters the PDF
  shows up as a different hash.

### Adding a guide

Copy a guide folder into `drafts/<slug>/`, change its text, and run `pnpm sync` to add it
to the workspace. When it's finished, move it to `guides/` and run `pnpm sync` again.
[CONTRIBUTING.md](CONTRIBUTING.md) has the steps.

### Releases

On each push to `main`, the Pages workflow makes a GitHub release for every guide version
that doesn't have one yet: tag `<slug>-v<version>`, named "<Title> <version>", with the PDF
and Word files attached. A draft's release is marked as a prerelease.

### Changing Python package versions

Edit `packages/pipeline/requirements.in`, then regenerate `requirements.txt` with
`pip-compile --generate-hashes --strip-extras requirements.in`. A guide's PDF matches its
`expected.sha256` only with the versions it was built with.

## License

The code and the guides' text are under the MIT License in `LICENSE`. The fonts in each
guide's `fonts/` folder, and their copies in `site/public/fonts/`, keep their own licenses,
in `fonts/licenses/`: TeX Gyre Heros under the GUST Font License and Liberation Mono under
the GNU GPL v2 with its font exception.
