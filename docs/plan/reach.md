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
   used two ways" and "this is wrong", and a label for good first issues. A Word template
   for writing a guide, and a "send a guide" form for the few we publish from other writers
   (see "Submissions and AI slop").
6. **Easy to share.** Open Graph images (the cover) for every page, short guide URLs,
   and a cover image in each release.
7. **Easy to reuse.** The guides' text is under CC BY 4.0, so people can copy it into their
   own training material with credit. The code stays MIT.
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

## Submissions and AI slop

**The risk.** A popular repository attracts submissions a model wrote and nobody read. One
takes minutes to generate and an hour to review: every fact checked against its source, every
source opened. Enough of them and reviewing crowds out writing.

curl went through this with security reports. In May 2025 its HackerOne form started asking
whether AI was used, and reporters who sent AI slop were banned at once
([The Register, 7 May 2025](https://www.theregister.com/security/2025/05/07/curl-takes-action-against-time-wasting-ai-bug-reports/267311)).
By July 2025 about a fifth of its reports were AI slop and about one in twenty was genuine
([Death by a thousand slops, 14 July 2025](https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/)).
In January 2026 it ended its bug bounty, from 31 January, to remove the incentive to make up
problems ([The end of the curl bug-bounty, 26 January 2026](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/)).
curl still accepts reports made with AI help, if the reporter says so.

**The policy,** in CONTRIBUTING.md under "Sending us a guide" and in the
`send-a-guide.yml` form:

- No rewards: no payment, prize or ranking.
- A named person is accountable for every sentence and answers questions about it.
- AI use is disclosed in the form. It isn't banned: our own guides are drafted with AI help
  and checked line by line by a person, and the rule is the same for everyone.
- Every fact has a source the submitter has read.
- Submissions that are low effort or can't be checked are closed quickly, without comment
  or debate.
- Accounts that keep sending them are blocked.
- Submissions get one line in the README and one short section on the site. Corrections and
  topic suggestions come first.

**If it gets bad,** in this order:

1. Turn on GitHub's temporary interaction limits (repository Settings → Moderation options →
   Interaction limits), which limit issues and pull requests to prior contributors or
   collaborators for up to six months.
2. Require an accepted issue before any pull request, and close pull requests without one.
3. Close the form: remove `send-a-guide.yml` and the line about sending a guide from the site,
   and keep the template for people writing for themselves.

Each week, count the submissions received, closed and published, next to the other numbers.

## Measure

Each week: stars, unique visitors and referrers from the repository's Insights → Traffic,
PDF downloads from release assets, and which guide pages are read most. Write the numbers
into this file, and change the plan when they say to.
