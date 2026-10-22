// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

import tableFocus from "./scripts/table-focus.mjs";

export default defineConfig({
  site: "https://stuffbucket.github.io",
  base: "/accidentalguide/",
  integrations: [
    // Wide tables scroll sideways; this lets a keyboard reach and scroll them, and turns them into cards on a phone.
    tableFocus(),
    starlight({
      title: "Accidental Guides",
      description: "Short guides to AI coding agents and the ways teams use them to build software.",
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
