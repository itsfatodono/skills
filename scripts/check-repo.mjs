#!/usr/bin/env node
// Checks what would break an install or the router. Exits 1 with one line per problem.
// Node standard library only.

import { existsSync, readdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repo = join(dirname(fileURLToPath(import.meta.url)), "..");
const ROUTER = "fatodono";
const ROUTER_SKILL = join("plugins", ROUTER, "skills", "ask-fato", "SKILL.md");

const problems = [];
const fail = (where, message) => problems.push(`${where}: ${message}`);
const read = (path) => readFileSync(join(repo, path), "utf8");
const readJson = (path) => JSON.parse(read(path));
const dirs = (path) =>
  existsSync(join(repo, path))
    ? readdirSync(join(repo, path), { withFileTypes: true }).filter((e) => e.isDirectory()).map((e) => e.name).sort()
    : [];

function frontmatter(text) {
  const match = text.match(/^---\n([\s\S]*?)\n---\n/);
  if (!match) return null;
  const fields = {};
  for (const line of match[1].split("\n")) {
    const kv = line.match(/^([a-z-]+):\s*(.*)$/);
    if (kv) fields[kv[1]] = kv[2].trim();
  }
  return fields;
}

// Marketplace and plugins/ list the same plugins, and every entry points at its own folder.
const marketplacePath = ".claude-plugin/marketplace.json";
const marketplace = readJson(marketplacePath);
const pluginNames = dirs("plugins");
const entryNames = marketplace.plugins.map((p) => p.name);

for (const name of pluginNames) {
  if (!entryNames.includes(name)) fail(marketplacePath, `plugins/${name} has no marketplace entry`);
}
for (const entry of marketplace.plugins) {
  if (!pluginNames.includes(entry.name)) fail(marketplacePath, `entry ${entry.name} has no plugins/${entry.name} folder`);
  if (entry.source !== `./plugins/${entry.name}`) fail(marketplacePath, `entry ${entry.name} must have source ./plugins/${entry.name}`);
  if ("version" in entry) fail(marketplacePath, `entry ${entry.name} sets version; versions live in plugin.json only`);
}

// Each plugin: manifest and package agree on name, and every plugin but the router depends on it.
const router = existsSync(join(repo, ROUTER_SKILL)) ? read(ROUTER_SKILL) : "";
if (!router) fail(ROUTER_SKILL, "missing");

const skillOwner = new Map();
for (const name of pluginNames) {
  const manifestPath = `plugins/${name}/.claude-plugin/plugin.json`;
  const pkgPath = `plugins/${name}/package.json`;
  if (!existsSync(join(repo, manifestPath))) {
    fail(manifestPath, "missing");
    continue;
  }
  if (!existsSync(join(repo, pkgPath))) {
    fail(pkgPath, "missing (changesets versions plugins through it)");
    continue;
  }
  const manifest = readJson(manifestPath);
  const pkg = readJson(pkgPath);
  if (manifest.name !== name) fail(manifestPath, `name is ${manifest.name}, folder is ${name}`);
  if (pkg.name !== name) fail(pkgPath, `name is ${pkg.name}, folder is ${name}`);
  if (pkg.private !== true) fail(pkgPath, "must be private");

  if (name !== ROUTER) {
    const deps = (manifest.dependencies ?? []).map((d) => (typeof d === "string" ? d : d.name));
    if (!deps.includes(ROUTER)) fail(manifestPath, `must depend on ${ROUTER}`);
  }

  // Each skill: frontmatter name matches its folder (OpenCode and skills.sh require it),
  // names are unique across plugins (skills.sh installs them side by side), and the router names it.
  for (const skill of dirs(`plugins/${name}/skills`)) {
    const skillPath = `plugins/${name}/skills/${skill}/SKILL.md`;
    if (!existsSync(join(repo, skillPath))) {
      fail(skillPath, "missing");
      continue;
    }
    const fields = frontmatter(read(skillPath));
    if (!fields) fail(skillPath, "no frontmatter");
    else {
      if (fields.name !== skill) fail(skillPath, `name is ${fields.name}, folder is ${skill}`);
      if (!fields.description) fail(skillPath, "no description");
    }
    if (skillOwner.has(skill)) fail(skillPath, `skill name ${skill} is also used in plugins/${skillOwner.get(skill)}`);
    skillOwner.set(skill, name);

    if (name !== ROUTER && !router.includes(skill)) fail(ROUTER_SKILL, `does not name skill ${skill}`);
  }
}

if (problems.length) {
  console.error(problems.join("\n"));
  process.exit(1);
}
console.log(`check-repo: ${pluginNames.length} plugins, ${skillOwner.size} skills, no problems`);
