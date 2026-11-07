"""The store screenshot slots: what each store takes, at which sizes, in
which device frame, and which slots a listing must fill.

Every value here comes from SOURCES, as they read on CHECKED. When a store
changes them, compare this file with both pages and move CHECKED to the day
you did; a monthly workflow opens an issue once CHECKED is six months old."""

from __future__ import annotations

from dataclasses import dataclass

CHECKED = "2026-10-23"
SOURCES = {
    "app_store": "https://developer.apple.com/help/app-store-connect/reference/app-information/"
                 "screenshot-specifications",
    "play": "https://support.google.com/googleplay/android-developer/answer/9866151",
}

STORES = ("app_store", "play")


@dataclass(frozen=True)
class Slot:
    """[sizes] lists the exact sizes the store takes; a slot without them
    takes any size of [ratio] whose sides lie within [sides]. Both are
    portrait, except the Mac's; a slot that [turns] also takes each of them
    turned to landscape."""
    id: str
    store: str
    frame: str
    device: str
    most: int
    sizes: tuple[tuple[int, int], ...] = ()
    ratio: tuple[int, int] | None = None
    sides: tuple[int, int] = (0, 0)
    turns: bool = True

    def size_problem(self, size: tuple[int, int]) -> str | None:
        """Why the store rejects [size] for this slot; None when it takes it."""
        turned = self.turns and size[0] > size[1]
        width, height = (size[1], size[0]) if turned else size
        also = " (or turned to landscape)" if self.turns else ""
        if self.sizes:
            if (width, height) in self.sizes:
                return None
            return f"{self.id} takes {', '.join(f'{w}x{h}' for w, h in self.sizes)}{also}"
        low, high = self.sides
        if width * self.ratio[1] == height * self.ratio[0] and low <= width and height <= high:
            return None
        return f"{self.id} takes {self.ratio[0]}:{self.ratio[1]} with sides from {low} to {high}{also}"


@dataclass(frozen=True)
class Requirement:
    """A store rejects a listing for an app that runs on [device] unless one
    of [slots] is filled."""
    store: str
    device: str
    slots: tuple[str, ...]


# Portrait sizes, each also taken turned to landscape, except the Mac's: a
# Mac screenshot is always landscape. Play takes any ratio up to 2:1, but its
# recommendations need 9:16 or 16:9 at 1080 px or more, so that is what its
# slots take.
SLOTS = {
    slot.id: slot
    for slot in [
        Slot("app_store/iphone_69", "app_store", "iphone", "iphone", 10,
             sizes=((1320, 2868), (1290, 2796), (1260, 2736))),
        Slot("app_store/iphone_65", "app_store", "iphone", "iphone", 10,
             sizes=((1284, 2778), (1242, 2688))),
        Slot("app_store/iphone_63", "app_store", "iphone", "iphone", 10,
             sizes=((1206, 2622), (1179, 2556))),
        Slot("app_store/ipad_13", "app_store", "ipad", "ipad", 10,
             sizes=((2064, 2752), (2048, 2732))),
        Slot("app_store/mac", "app_store", "mac", "mac", 10,
             sizes=((2880, 1800), (2560, 1600), (1440, 900), (1280, 800)), turns=False),
        Slot("play/phone", "play", "android_phone", "phone", 8,
             ratio=(9, 16), sides=(1080, 3840)),
        Slot("play/tablet_7", "play", "android_tablet", "tablet", 8,
             ratio=(9, 16), sides=(1080, 7680)),
        Slot("play/tablet_10", "play", "android_tablet", "tablet", 8,
             ratio=(9, 16), sides=(1080, 7680)),
    ]
}

REQUIREMENTS = (
    Requirement("app_store", "iphone", ("app_store/iphone_69", "app_store/iphone_65")),
    Requirement("app_store", "ipad", ("app_store/ipad_13",)),
    Requirement("app_store", "mac", ("app_store/mac",)),
    Requirement("play", "phone", ("play/phone",)),
)

FEATURE_GRAPHIC_SIZE = (1024, 500)

DEFAULT_RUNS_ON = {"app_store": ("iphone",), "play": ("phone",)}


def devices(store: str) -> list[str]:
    return list(dict.fromkeys(slot.device for slot in SLOTS.values() if slot.store == store))


def required(store: str, runs_on: list[str]) -> list[Requirement]:
    return [r for r in REQUIREMENTS if r.store == store and r.device in runs_on]

FRAMES = tuple(dict.fromkeys(slot.frame for slot in SLOTS.values()))
# Frames that are landscape whatever the target: the Mac window.
LANDSCAPE_FRAMES = tuple(dict.fromkeys(slot.frame for slot in SLOTS.values() if not slot.turns))
