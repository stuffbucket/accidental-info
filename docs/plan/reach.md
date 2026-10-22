# Reach plan

The goal is 1,000,000 stars by the end of 2026. On 22 October 2026 the most-starred
repositories on GitHub had between 360,000 and 556,000 stars, so the goal is about twice the
record, in ten weeks. The plan works toward it in steps and measures each one.

| By | Stars | What has to be true |
|---|---|---|
| 1 November 2026 | 1,000 | Five finished guides readable on the site, shared once in each place listed under Launch. |
| 1 December 2026 | 25,000 | Ten finished guides, translations started, other people writing drafts in the open. |
| 31 December 2026 | 100,000+ | A guide for every common question about coding agents, in five or more languages. |

## What the biggest learning repositories have in common

build-your-own-x, awesome, public-apis, free-programming-books, freeCodeCamp,
system-design-primer and coding-interview-university:

- **They answer a question many people have, and the answer stays useful.** Nobody stars a
  repository for news.
- **They fit in a README.** A reader sees the value on the first screen of github.com without
  clicking anything.
- **Many people contribute.** Each contributor shares the repository with their own network.
- **They are translated.** system-design-primer and coding-interview-university each have more
  than ten languages.
- **They are linked from places people already read:** course syllabi, onboarding documents,
  newsletters, Hacker News, Reddit, X, LinkedIn.

## Work in this repository

1. **The README is the front page.** It shows the covers and a one-line answer per guide, with
   links to read online, PDF and Word. Most visitors decide on github.com, not the site.
2. **Every guide reads in the browser.** One HTML page per guide, so search engines and
   language models can index the text and people can link to a section.
3. **Drafts in the open.** `drafts/` holds guides still being written, marked as drafts on the
   site, so people can watch a guide take shape and suggest changes.
4. **Releases.** Each guide version is a GitHub release with the PDF and Word files attached.
   Watchers get a notification, and the release page is something people can share.
5. **Easy to contribute.** CONTRIBUTING.md, issue forms for "suggest a guide", "a word is
   used two ways" and "this is wrong", and a label for good first issues.
6. **Easy to share.** Open Graph images (the cover) for every page, short guide URLs,
   and a cover image in each release.
7. **Easy to reuse.** A license for the text that lets people copy it into their own
   training material with credit (CC BY 4.0 is the usual choice; the code stays MIT).
   This is Brian's decision.
8. **Translations.** The Markdown source makes translation a pull request per guide:
   `guides/<slug>/guide.<lang>.md`, built the same way.
9. **Repository metadata.** Topics (ai, coding-agents, claude-code, codex, github-copilot,
   mcp, software-factory, learning), a social preview image, Discussions on.

## Launch

Post one guide at a time, with the question it answers as the title:

- Hacker News (Show HN), r/programming, r/ChatGPTCoding, r/ClaudeAI, r/LocalLLaMA
- X, Bluesky, LinkedIn, Mastodon
- Newsletters that cover coding agents
- Listings: awesome-claude-code, awesome-ai-agents and the other awesome lists for coding agents

## Measure

Each week: stars, unique visitors and referrers from the repository's Insights → Traffic,
PDF downloads from release assets, and which guide pages are read most. Write the numbers
into this file, and change the plan when they say to.
