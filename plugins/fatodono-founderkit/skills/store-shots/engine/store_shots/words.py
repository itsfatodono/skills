"""How a console line counts things and names the first of many."""

from __future__ import annotations


def plural(count: int, word: str) -> str:
    return f"{count} {word}{'' if count == 1 else 's'}"


def first_of(items: list) -> str:
    """The first of [items], then how many more there are."""
    more = f" (+{len(items) - 1} more)" if len(items) > 1 else ""
    return f"{items[0]}{more}"
