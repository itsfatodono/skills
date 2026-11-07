"""PNGs written byte by byte, so a test states exactly what a file holds."""

from __future__ import annotations

import struct
import zlib

IPHONE = (1320, 2868)
PANEL_COPY = "Every note you take, searchable.\nFind anything you've noted, in seconds."


def _chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))


def icc(description: str) -> bytes:
    """The smallest ICC profile that carries a 'desc' tag reading [description]."""
    text = description.encode() + b"\x00"
    desc = b"desc" + b"\x00" * 4 + struct.pack(">I", len(text)) + text
    tag_offset = 128 + 4 + 12
    header = struct.pack(">I", tag_offset + len(desc)) + b"\x00" * 124
    return header + struct.pack(">I", 1) + b"desc" + struct.pack(">II", tag_offset, len(desc)) + desc


def png(size=IPHONE, color_type=2, profile="srgb", copy: str | None = PANEL_COPY,
        trns=False) -> bytes:
    """A one-colour PNG. [color_type] 2 is RGB, 6 RGBA, 4 grey + alpha;
    [profile] is "srgb" (an sRGB chunk), None, or an ICC description to embed.
    [copy] is the text the renderer records in the image (None: none)."""
    width, height = size
    channels = {2: 3, 6: 4, 4: 2}[color_type]
    row = b"\x00" + b"\xf4" * (width * channels)
    chunks = [_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, color_type, 0, 0, 0))]
    if profile == "srgb":
        chunks.append(_chunk(b"sRGB", b"\x00"))
    elif profile:
        chunks.append(_chunk(b"iCCP", b"icc\x00\x00" + zlib.compress(icc(profile))))
    if trns:
        chunks.append(_chunk(b"tRNS", b"\x00\xf4\x00\xf4\x00\xf4"))
    if copy is not None:
        chunks.append(_chunk(b"iTXt", b"Copy\x00\x00\x00\x00\x00" + copy.encode()))
    chunks.append(_chunk(b"IDAT", zlib.compress(row * height)))
    chunks.append(_chunk(b"IEND", b""))
    return b"\x89PNG\r\n\x1a\n" + b"".join(chunks)
