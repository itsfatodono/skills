#!/usr/bin/env python3
"""Morpheme matrix expander — Phase 2 of the brand-naming process.

Vercel came out of 55 prefixes x 102 suffixes, run three times. Typing those
combinations by hand is where volume dies, so this does it: cartesian product
across N slots, with elision, pronounceability filtering and dedupe.

    python3 combine.py --parts prefixes.txt suffixes.txt --min-len 4 --max-len 9

Parts are files (one morpheme per line, # comments and blanks ignored) or inline
comma-separated lists. Output is a plain candidate list for the Phase 2 file.
"""

import argparse
import os
import sys
from itertools import product

VOWELS = set("aeiouy")


def load_parts(spec):
    """A --parts entry is either a path to a list file or an inline a,b,c list."""
    if os.path.exists(spec):
        with open(spec, encoding="utf-8") as f:
            lines = [ln.split("#", 1)[0].strip() for ln in f]
        return [ln.lower() for ln in lines if ln]
    return [p.strip().lower() for p in spec.split(",") if p.strip()]


def joins(a, b, elide):
    """Ways of fusing two morphemes. Elision is where the good ones hide:
    penta + ium -> pentium, not pentaium."""
    out = {a + b}
    if elide:
        if a[-1] == b[0]:                              # ver + rel -> verel
            out.add(a + b[1:])
        if a[-1] in VOWELS and b[0] in VOWELS:         # penta + ium -> pentium
            out.add(a[:-1] + b)
    return out


def pronounceable(name):
    """Cheap phonotactic screen. Rejects the obvious sludge, keeps the rest --
    a false negative here silently deletes a candidate, so it stays permissive."""
    if not any(c in VOWELS for c in name):
        return False
    run = 0
    for c in name:
        run = 0 if c in VOWELS else run + 1
        if run >= 4:                                   # 4+ consonants in a row
            return False
    for i in range(len(name) - 2):                     # tripled letter
        if name[i] == name[i + 1] == name[i + 2]:
            return False
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--parts", nargs="+", required=True, metavar="SLOT",
                    help="one entry per slot: a file path or an inline 'a,b,c' list")
    ap.add_argument("--min-len", type=int, default=3)
    ap.add_argument("--max-len", type=int, default=12)
    ap.add_argument("--require", default="", metavar="CHARS",
                    help="keep only names containing at least one of these letters "
                         "(e.g. v,z for the 'alive' sound strategy)")
    ap.add_argument("--forbid", default="", metavar="CHARS",
                    help="drop names containing any of these letters")
    ap.add_argument("--elide", action="store_true",
                    help="also emit seam-collapsed forms (penta+ium -> pentium)")
    ap.add_argument("--no-filter", action="store_true",
                    help="skip the pronounceability screen")
    ap.add_argument("--limit", type=int, default=0, help="cap output count (0 = no cap)")
    ap.add_argument("--out", help="write here instead of stdout")
    args = ap.parse_args()

    slots = [load_parts(s) for s in args.parts]
    if any(not s for s in slots):
        sys.exit("error: a slot resolved to zero morphemes -- check the file paths")

    require = {c for c in args.require.lower() if c.isalpha()}
    forbid = {c for c in args.forbid.lower() if c.isalpha()}

    names = set()
    for combo in product(*slots):
        forms = {combo[0]}
        for part in combo[1:]:
            forms = {f for base in forms for f in joins(base, part, args.elide)}
        names |= forms

    kept = sorted(
        n for n in names
        if args.min_len <= len(n) <= args.max_len
        and (not require or require & set(n))
        and not (forbid & set(n))
        and (args.no_filter or pronounceable(n))
    )

    total = len(kept)
    if args.limit:
        kept = kept[:args.limit]

    body = "\n".join(kept)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(body + "\n")
        print(f"{len(kept)} candidates written to {args.out}"
              + (f" (of {total} passing filters)" if args.limit else ""))
    else:
        print(body)
        print(f"\n# {len(kept)} candidates"
              + (f" of {total} passing filters" if args.limit else ""), file=sys.stderr)


if __name__ == "__main__":
    main()
