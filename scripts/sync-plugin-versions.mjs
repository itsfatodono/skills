#!/usr/bin/env node
// Copies each plugin's package.json version into its .claude-plugin/plugin.json.
// Runs as part of `npm run version`, right after `changeset version`.
// With --check it changes nothing and exits 1 if any pair differs.

import { readdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repo = join(dirname(fileURLToPath(import.meta.url)), "..");
const pluginsDir = join(repo, "plugins");
const check = process.argv.includes("--check");
let drift = false;

for (const name of readdirSync(pluginsDir).sort()) {
  const pkgPath = join(pluginsDir, name, "package.json");
  const pluginPath = join(pluginsDir, name, ".claude-plugin", "plugin.json");
  const { version } = JSON.parse(readFileSync(pkgPath, "utf8"));
  const source = readFileSync(pluginPath, "utf8");
  const current = JSON.parse(source).version;

  if (current === version) continue;

  if (check) {
    console.error(`${name}: plugin.json is ${current}, package.json is ${version}. Run \`npm run version\`.`);
    drift = true;
    continue;
  }

  // Rewrite only the version line, so key order and formatting stay as they are.
  const updated = source.replace(/("version"\s*:\s*")[^"]*(")/, `$1${version}$2`);
  if (JSON.parse(updated).version !== version) {
    console.error(`${name}: no version field to replace in ${pluginPath}.`);
    process.exit(1);
  }
  writeFileSync(pluginPath, updated);
  console.log(`${name}: plugin.json ${current} -> ${version}`);
}

if (drift) process.exit(1);
