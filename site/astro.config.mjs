// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import { existsSync, readFileSync } from "node:fs";

import tableFocus from "./scripts/table-focus.mjs";

// Where the site is served. The Pages workflow sets SITE_ORIGIN and SITE_BASE from actions/configure-pages, so
// the site follows the repository's custom domain (https://accidental.info, at the root) once it is set.
const origin = process.env.SITE_ORIGIN || "https://accidental.info";
const base = `${(process.env.SITE_BASE ?? "").replace(/\/$/, "")}/`;

// The sidebar: one group per collection in src/data/collections.json, its guides in the order listed there (a
// collection with a map: its catalog, then each group's guides). scripts/guide_pages.py writes a page for each built
// guide under src/content/docs/guides/ (finished) or drafts/ (a draft); a listed guide without a page yet is
// skipped, and so is a collection with none. src/lib/collections.mjs checks the list itself when the landing page
// is built.
const docs = new URL("./src/content/docs/", import.meta.url);
const { collections } = JSON.parse(readFileSync(new URL("./src/data/collections.json", import.meta.url), "utf8"));
const listed = (collection) => {
  const lists = collection.groups ? [{ guides: [collection.catalog] }, ...collection.groups] : [collection];
  return lists.flatMap((list) => [...(list.guides ?? []), ...(list.coming ?? []).map((guide) => guide.id)]);
};
const pageItem = (id) => {
  if (existsSync(new URL(`guides/${id}.md`, docs))) return { slug: `guides/${id}` };
  // A draft says so on its page ("Draft · Version…"); the sidebar lists it like any other guide.
  if (existsSync(new URL(`drafts/${id}.md`, docs))) return { slug: `drafts/${id}` };
  return null;
};
const sidebar = [
  { label: "All guides", link: `${base}guides/` },
  ...collections
    .map((collection) => ({
      label: collection.name,
      items: [
        ...(collection.page ? [{ label: "The map", link: `${base}${collection.page}` }] : []),
        ...listed(collection).map(pageItem).filter(Boolean),
      ],
    }))
    .filter((group) => group.items.some((item) => "slug" in item)),
];

// The share image for pages without their own. scripts/guide_pages.py writes it, and gives each guide's page its
// own card in the page's front matter.
const socialImage = new URL(`${base}social.png`, origin).href;

export default defineConfig({
  site: origin,
  base,
  // A short address for the PDFs and Word files to link to. Astro writes a page that sends the reader on (a meta
  // refresh, a canonical link and a plain link to follow), marked noindex and left out of the sitemap.
  redirects: { "/star": "https://github.com/stuffbucket/accidental-info" },
  integrations: [
    // Wide tables scroll sideways; this lets a keyboard reach and scroll them, and turns them into cards on a phone.
    tableFocus(),
    starlight({
      title: "Accidental Guides",
      description: "My friend has a lot of questions.",
      head: [
        { tag: "meta", attrs: { property: "og:image", content: socialImage } },
        { tag: "meta", attrs: { property: "og:image:width", content: "1200" } },
        { tag: "meta", attrs: { property: "og:image:height", content: "630" } },
        { tag: "meta", attrs: { property: "og:image:alt", content: "The covers of the Accidental Guides" } },
      ],
      social: [{ icon: "github", label: "GitHub", href: "https://github.com/stuffbucket/accidental-info" }],
      // The "On this page" panel opens and closes from an icon button, and closed it gives the page its room
      // (see the component). The footer adds "Leave a star" below the previous and next links.
      components: {
        TwoColumnContent: "./src/components/starlight/TwoColumnContent.astro",
        Footer: "./src/components/starlight/Footer.astro",
      },
      // The guides' typefaces and colours, and tables that do not scroll sideways where it can be helped.
      customCss: ["./src/styles/theme.css", "./src/styles/tables.css"],
      sidebar,
    }),
  ],
});
