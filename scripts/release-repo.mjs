#!/usr/bin/env node
// Creates the repo's GitHub release, "fatodono <version>", tagged v<version>.
// The repo version is the root package.json version; bump it by hand to cut a release.
// The notes list each plugin whose version changed since the previous v* tag,
// with the lines from its CHANGELOG for the versions in between.
// Runs as the changesets action's publish step, so on every push to main:
// it does nothing when the tag already exists.
// With --dry-run it prints the title and notes and creates nothing.

import { execFileSync } from "node:child_process";
import { existsSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repo = join(dirname(fileURLToPath(import.meta.url)), "..");
const dryRun = process.argv.includes("--dry-run");
const git = (...args) => execFileSync("git", args, { cwd: repo, encoding: "utf8" }).trim();

const version = JSON.parse(readFileSync(join(repo, "package.json"), "utf8")).version;
if (!version) {
  console.error("release-repo: root package.json has no version");
  process.exit(1);
}
const tag = `v${version}`;
const title = `fatodono ${version}`;

git("fetch", "--tags", "--quiet");
if (git("tag", "-l", tag)) {
  console.log(`release-repo: ${tag} exists, nothing to release`);
  process.exit(0);
}

const previous = git("tag", "-l", "v*", "--sort=-v:refname").split("\n").filter(Boolean)[0];

const parse = (v) => v.split(".").map(Number);
const newer = (a, b) => {
  const [x, y] = [parse(a), parse(b)];
  for (let i = 0; i < 3; i++) if (x[i] !== y[i]) return x[i] > y[i];
  return false;
};

// Lines from CHANGELOG sections in (from, to], newest first, without the commit-hash prefix.
function changelogLines(path, from, to) {
  if (!existsSync(path)) return [];
  const lines = [];
  for (const section of readFileSync(path, "utf8").split(/^## /m).slice(1)) {
    const [heading, ...body] = section.split("\n");
    const v = heading.trim();
    if (newer(v, to) || (from && !newer(v, from))) continue;
    for (const line of body) {
      const m = line.match(/^- (?:[0-9a-f]{7,}: )?(.+)/);
      if (m && !m[1].startsWith("Updated dependencies")) lines.push(m[1]);
    }
  }
  return lines;
}

const entries = [];
const pluginsDir = join(repo, "plugins");
for (const name of readdirSync(pluginsDir, { withFileTypes: true }).filter((e) => e.isDirectory()).map((e) => e.name).sort()) {
  const current = JSON.parse(readFileSync(join(pluginsDir, name, "package.json"), "utf8")).version;
  let before = null;
  if (previous) {
    try {
      before = JSON.parse(git("show", `${previous}:plugins/${name}/package.json`)).version;
    } catch {
      before = null; // the plugin is new since the previous release
    }
  }
  if (before === current) continue;
  const lines = changelogLines(join(pluginsDir, name, "CHANGELOG.md"), before, current);
  if (lines.length === 1) entries.push(`- **${name} ${current}**: ${lines[0]}`);
  else entries.push([`- **${name} ${current}**`, ...lines.map((l) => `  - ${l}`)].join("\n"));
}

const notes = entries.length ? entries.join("\n") : "No plugin changed in this release.";

if (dryRun) {
  console.log(`${title} (${tag}, previous: ${previous ?? "none"})\n\n${notes}`);
  process.exit(0);
}

const notesFile = join(tmpdir(), `release-${tag}.md`);
writeFileSync(notesFile, notes + "\n");
execFileSync(
  "gh",
  ["release", "create", tag, "--title", title, "--notes-file", notesFile, "--target", git("rev-parse", "HEAD"), "--latest"],
  { cwd: repo, stdio: "inherit" },
);
console.log(`release-repo: created ${title}`);
