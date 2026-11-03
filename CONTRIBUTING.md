# Contributing

## Where things go

- `plugins/<kit>/skills/<skill>/`: everything the skill needs when it runs on a user's machine.
- `workshop/<skill>/`: everything that is only needed to develop the skill, such as research, tools, tests and fixtures.

Each skill can set its own rules in `workshop/<skill>/CONTRIBUTING.md`. Read that file before you change the skill.

## Branches

- `main` is what users install. Only the maintainer merges into it, from `staging`.
- `staging` is where development happens. Open every pull request against `staging`, not `main`.

## Before you open a pull request

Run `npm run check`. It checks that the manifests and the `ask-fato` router agree with each other.

You don't need to write a changeset or bump a version. The maintainer handles releases.
