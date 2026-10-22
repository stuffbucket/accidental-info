// Copy the guide template's Word document from packages/template/dist into public/, where the landing page links
// to it. Run before astro (see package.json); turbo builds the template first (see turbo.json).
import { copyFileSync, existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const NAME = "accidental-guide-template.docx";
const site = join(dirname(fileURLToPath(import.meta.url)), "..");
const from = join(site, "..", "packages", "template", "dist", NAME);

if (!existsSync(from)) {
  console.error(`${from} not found: build the template first (pnpm build at the repository root)`);
  process.exit(1);
}
copyFileSync(from, join(site, "public", NAME));
console.log(`copied ${NAME} to public/`);
