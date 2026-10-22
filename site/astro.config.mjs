// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

import tableFocus from "./scripts/table-focus.mjs";

// Where the site is served. The Pages workflow sets SITE_ORIGIN and SITE_BASE from actions/configure-pages, so
// the site follows the repository's custom domain (https://accidental.info, at the root) once it is set.
const origin = process.env.SITE_ORIGIN || "https://stuffbucket.github.io";
const base = `${(process.env.SITE_BASE ?? "/accidentalguide").replace(/\/$/, "")}/`;

// The share image for pages without their own. scripts/guide_pages.py writes it, and gives each guide's page its
// own card in the page's front matter.
const socialImage = new URL(`${base}social.png`, origin).href;

export default defineConfig({
  site: origin,
  base,
  integrations: [
    // Wide tables scroll sideways; this lets a keyboard reach and scroll them, and turns them into cards on a phone.
    tableFocus(),
    starlight({
      title: "Accidental Guides",
      description: "Short guides to AI coding agents and the ways teams use them to build software.",
      head: [
        { tag: "meta", attrs: { property: "og:image", content: socialImage } },
        { tag: "meta", attrs: { property: "og:image:width", content: "1200" } },
        { tag: "meta", attrs: { property: "og:image:height", content: "630" } },
        { tag: "meta", attrs: { property: "og:image:alt", content: "The covers of the Accidental Guides" } },
      ],
      social: [{ icon: "github", label: "GitHub", href: "https://github.com/stuffbucket/accidentalguide" }],
      // The "On this page" panel opens and closes from an icon button, and closed it gives the page its room
      // (see the component).
      components: { TwoColumnContent: "./src/components/starlight/TwoColumnContent.astro" },
      // The guides' typefaces and colours, and tables that do not scroll sideways where it can be helped.
      customCss: ["./src/styles/theme.css", "./src/styles/tables.css"],
      // scripts/guide_pages.py writes one page per guide with `sidebar.order` set, in the catalog's order.
      sidebar: [
        { label: "Guides", items: [{ autogenerate: { directory: "guides" } }] },
        { label: "Drafts", items: [{ autogenerate: { directory: "drafts" } }] },
      ],
    }),
  ],
});
