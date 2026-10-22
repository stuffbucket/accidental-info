// The guides as the site's own pages see them: public/guides.json (written by scripts/guide_pages.py from each
// guide's dist/), each guide with its cover's size and the path of its page, checked against the collections in
// src/data/collections.json. Used by the landing page, the map page and the list of all guides.
import { readFileSync } from "node:fs";
import { join } from "node:path";
import collectionData from "../data/collections.json";
import { checkCollections } from "./collections.mjs";

export interface Guide {
  id: string;
  title: string;
  subtitle: string;
  version: string;
  blurb: string;
  pdf: string;
  docx: string | null;
  pages: number;
  status: "published" | "draft";
  // The cover's size in CSS pixels, and the guide's page under the base ("guides/<id>/" or "drafts/<id>/").
  cover: { width: number; height: number };
  page: string;
}

export interface Coming {
  id: string;
  title: string;
}

// A place on a shelf or in a group: a built guide, or one still to come.
export type Entry = { guide: Guide; coming?: undefined } | { coming: Coming; guide?: undefined };

export interface Colour {
  base: string;
  band: string;
  ink: string;
}

export interface Group {
  id: string;
  name: string;
  colour: Colour;
  image: string | null;
  guides: Guide[];
  coming: Coming[];
  entries: Entry[];
}

export interface Collection {
  id: string;
  name: string;
  line: string;
  code: string;
  colour: Colour;
  image: string | null;
  imageAlt: string;
  page: string | null;
  guides: Guide[];
  coming: Coming[];
  entries: Entry[];
  count: number;
  map: { center: Guide; groups: Group[]; codes: Record<string, string> } | null;
}

// Astro runs from the site folder, in development and in the build.
const publicDir = join(process.cwd(), "public");
const read = (path: string) => {
  try {
    return readFileSync(join(publicDir, path));
  } catch {
    throw new Error(`public/${path} is missing: run pnpm build at the repository root`);
  }
};

// The cover's width and height in pixels, from its PNG header. It is rendered at twice the size it is shown.
const coverSize = (id: string) => {
  const png = read(`guides/${id}/cover.png`);
  return { width: png.readUInt32BE(16) / 2, height: png.readUInt32BE(20) / 2 };
};

export function loadGuides(): Guide[] {
  return (JSON.parse(read("guides.json").toString()) as Omit<Guide, "cover" | "page">[]).map((guide) => ({
    ...guide,
    cover: coverSize(guide.id),
    page: `${guide.status === "draft" ? "drafts" : "guides"}/${guide.id}/`,
  }));
}

/** The collections with their guides. This throws, and fails the build, if a guide is in no collection or a
 * collection lists a guide that isn't built (see src/lib/collections.mjs). */
export function loadCollections(): Collection[] {
  return checkCollections(collectionData, loadGuides()) as Collection[];
}

/** The site's base path, ending in a slash. */
export const base = import.meta.env.BASE_URL.replace(/\/?$/, "/");
export const repo = "https://github.com/stuffbucket/accidentalguide";
