"""Headless Chrome turns a layout page plus its data into a store image:
exact window size, one CSS px per image pixel, sRGB forced, saved opaque RGB
with an embedded sRGB profile and an iTXt "Copy" chunk of every text shown."""

from __future__ import annotations

import io
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageCms, PngImagePlugin

from .errors import StageError

MOCKUPS = Path(__file__).resolve().parent / "mockups"
# Tried in order, before PATH. Edge is a Chromium that every Windows has.
INSTALLS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    *(os.path.join(root, *rest) for root in filter(None, [
        os.environ.get("PROGRAMFILES"), os.environ.get("PROGRAMFILES(X86)"),
        os.environ.get("LOCALAPPDATA")])
      for rest in [("Google", "Chrome", "Application", "chrome.exe"),
                   ("Chromium", "Application", "chrome.exe"),
                   ("Microsoft", "Edge", "Application", "msedge.exe")]),
]
ON_PATH = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"]
SRGB = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()


def chrome() -> str:
    found = os.environ.get("STORE_SHOTS_CHROME") \
        or next((path for path in INSTALLS if Path(path).is_file()), None) \
        or next(filter(None, map(shutil.which, ON_PATH)), None)
    if not found:
        raise StageError("no Chrome found; set STORE_SHOTS_CHROME to its binary")
    return found


def page(layout_page: Path, data: dict) -> str:
    """[layout_page] with the engine's part added: a base URL so the page's own
    links resolve, the mockup stylesheets, [data] and the mockup runtime."""
    html = layout_page.read_text(encoding="utf-8")
    if "<head>" not in html or "</body>" not in html:
        raise StageError(f"{layout_page.name} needs a <head> and a </body>")
    styles = [MOCKUPS / "mockup.css", *sorted((MOCKUPS / "frames").glob("*.css"))]
    head = "".join([
        f'<base href="{layout_page.parent.resolve().as_uri()}/">',
        *(f'<link rel="stylesheet" href="{s.as_uri()}">' for s in styles),
        '<script id="store-shots-data" type="application/json">',
        json.dumps(data, ensure_ascii=False).replace("</", "<\\/"),
        "</script>",
    ])
    runtime = f'<script src="{(MOCKUPS / "mockup.js").as_uri()}"></script>'
    return html.replace("<head>", "<head>" + head, 1).replace("</body>", runtime + "</body>", 1)


def save_opaque(source: Path, out: Path) -> None:
    """[source] as opaque RGB with an embedded sRGB profile."""
    out.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        image.convert("RGB").save(out, icc_profile=SRGB, optimize=True)


def shoot(html: str, size: tuple[int, int], out: Path, copy: list[str], work: Path, log: Path) -> None:
    """Renders [html] at [size] into [out]; Chrome's output goes to [log]."""
    width, height = size
    work.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".html", dir=work, delete=False, encoding="utf-8") as f:
        f.write(html)
        source = Path(f.name)
    shot = source.with_suffix(".png")
    argv = [
        chrome(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--allow-file-access-from-files", "--force-color-profile=srgb",
        # Headless Chrome will not lay out a window narrower than about
        # 500 px, so the image is never rendered at a device pixel ratio.
        "--force-device-scale-factor=1",
        f"--window-size={width},{height}",
        "--virtual-time-budget=5000",
        f"--screenshot={shot}", source.as_uri(),
    ]
    try:
        with log.open("a", encoding="utf-8") as f:
            f.write(f"$ render {out}\n")
            f.flush()
            done = subprocess.run(argv, stdout=f, stderr=subprocess.STDOUT)
        if done.returncode != 0 or not shot.is_file():
            raise StageError(f"Chrome failed on {out.name} (exit {done.returncode})")
        image = Image.open(io.BytesIO(shot.read_bytes()))
        if image.size != (width, height):
            raise StageError(f"Chrome rendered {out.name} at {image.size}, expected {size}")
        out.parent.mkdir(parents=True, exist_ok=True)
        info = PngImagePlugin.PngInfo()
        info.add_itxt("Copy", "\n".join(copy))
        image.convert("RGB").save(out, icc_profile=SRGB, optimize=True, pnginfo=info)
    finally:
        source.unlink(missing_ok=True)
        shot.unlink(missing_ok=True)
