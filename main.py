#!/usr/bin/env python3
"""Deliver the finished front page for 20 November 2026 to the grader.

This repository holds a single finished image, ``entry.png``: a newspaper
front page drawn from the world news of Friday 20 November 2026. The
program below is the entrypoint the grader runs. It does one thing and
checks its own work: it reads the committed image, makes sure it is a
real PNG inside the size cap, writes those exact bytes to the output
directory, and then reads the copy back and compares it byte for byte
before saying anything went well.

The output directory comes from, in order: an optional first command-line
argument, the ``MAKEFUN_OUTPUT_DIR`` environment variable, or ``/output``.
Outside the grader's container the usual way to try it is:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3 standard library only; nothing is downloaded and nothing leaves
the machine.
"""

import hashlib
import os
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_IMAGE_BYTES = 1_048_576  # the bounty caps the image at 1 MiB
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"


def die(message: str) -> "SystemExit":
    """Report a failure on stderr and stop with a non-zero exit."""
    print(f"error: {message}", file=sys.stderr)
    return SystemExit(1)


def committed_image() -> Path:
    """The image file committed beside this program."""
    return Path(__file__).resolve().parent / IMAGE_NAME


def output_dir(argv: list[str]) -> Path:
    """Where the grader reads the entry from, honouring overrides."""
    if argv:
        return Path(argv[0])
    return Path(os.environ.get(OUTPUT_ENV_VAR, DEFAULT_OUTPUT_DIR))


def png_dimensions(data: bytes) -> tuple[int, int]:
    """Width and height from the PNG IHDR chunk, if the header is intact."""
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise ValueError("PNG header is truncated or missing its IHDR chunk")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if width <= 0 or height <= 0:
        raise ValueError("PNG header carries non-positive dimensions")
    return width, height


def read_checked_image(path: Path) -> bytes:
    """Read the image, refusing anything that is not a capped PNG."""
    if not path.is_file():
        raise FileNotFoundError(f"committed image {path} is missing")
    data = path.read_bytes()
    if len(data) > MAX_IMAGE_BYTES:
        raise ValueError(
            f"{path} is {len(data)} bytes, over the "
            f"{MAX_IMAGE_BYTES} byte cap"
        )
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError(f"{path} does not start with a PNG signature")
    png_dimensions(data)
    return data


def deliver(data: bytes, directory: Path) -> Path:
    """Write the bytes out and prove the copy matches, byte for byte."""
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / IMAGE_NAME
    target.write_bytes(data)
    if target.read_bytes() != data:
        raise IOError(f"copy at {target} differs from the committed image")
    return target


def main(argv: list[str]) -> int:
    try:
        data = read_checked_image(committed_image())
        target = deliver(data, output_dir(argv))
    except (FileNotFoundError, ValueError, OSError) as problem:
        print(f"error: {problem}", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    width, height = png_dimensions(data)
    print(
        f"wrote {target} ({width}x{height}, {len(data)} bytes, "
        f"sha256 {digest})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
