#!/usr/bin/env node
// Writes the coverage table in the legals README, between `<!-- coverage:start -->` and
// `<!-- coverage:end -->`, from the skill's files: one row per ready item in catalog order, one
// column per region, and the latest `scanned` date of the item's files.
// A region file with a `## Sections` heading is ✅; one with only *Avoid* marks is ☑️.
// With --check it changes nothing and exits 1 if the table differs.

import { existsSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repo = join(dirname(fileURLToPath(import.meta.url)), "..");
const skill = join(repo, "plugins", "fatodono-launchkit", "skills", "legals");
const readmePath = join(skill, "README.md");
const check = process.argv.includes("--check");
const read = (path) => readFileSync(path, "utf8");
const field = (text, name) => text.match(new RegExp(`^${name}:\\s*(.*)$`, "m"))?.[1].trim();

const regions = readdirSync(join(skill, "regions"), { withFileTypes: true }).filter((e) => e.isDirectory()).map((e) => e.name).sort();
const catalogIds = (path) =>
  existsSync(path) ? [...read(path).matchAll(/^\| ([a-z0-9-]+) \|/gm)].map((m) => m[1]).filter((id) => id !== "Id") : [];

// Ready items: catalog rows that have a skeleton, or a region's own `whole` document.
const rows = [];
for (const id of catalogIds(join(skill, "helpers", "catalog.md"))) {
  const path = join(skill, "skeletons", `${id}.md`);
  if (existsSync(path)) rows.push({ id, main: path });
}
for (const region of regions) {
  for (const id of catalogIds(join(skill, "regions", region, "catalog.md"))) {
    const path = join(skill, "regions", region, `${id}.md`);
    if (existsSync(path)) rows.push({ id, main: path, only: region });
  }
}

const columns = regions.filter((r) => rows.some((row) => row.only === r || existsSync(join(skill, "regions", r, `${row.id}.md`))));
const header = `| Document | Global | ${columns.map((c) => c.toUpperCase()).join(" | ")} | Updated |`;
const rule = `|---|${"---|".repeat(columns.length + 2)}`;
const lines = rows.map((row) => {
  const text = read(row.main);
  const title = field(text, "title").replace(/ \(.*\)$/, "");
  const dates = [field(text, "scanned")];
  const cells = columns.map((region) => {
    if (row.only) return row.only === region ? "✅" : "";
    const path = join(skill, "regions", region, `${row.id}.md`);
    if (!existsSync(path)) return "";
    const block = read(path);
    dates.push(field(block, "scanned"));
    return /^## Sections$/m.test(block) ? "✅" : "☑️";
  });
  const updated = dates.filter(Boolean).sort().at(-1);
  return `| ${title} | ${row.only ? "" : "✅"} | ${cells.join(" | ")} | ${updated} |`;
});
const table = [header, rule, ...lines].join("\n");

const source = read(readmePath);
const markers = /(<!-- coverage:start -->\n)[\s\S]*?(<!-- coverage:end -->)/;
if (!markers.test(source)) {
  console.error("legals README: no coverage markers");
  process.exit(1);
}
const result = source.replace(markers, `$1${table}\n$2`);
if (result === source) process.exit(0);
if (check) {
  console.error("legals README: coverage table is out of date. Run `node scripts/sync-legals-coverage.mjs`.");
  process.exit(1);
}
writeFileSync(readmePath, result);
console.log("legals README: coverage table updated");
