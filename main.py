#!/usr/bin/env python3
"""Entry program for make.fun's news-image-20261120 bounty.

The repository holds one finished front-page image, entry.png, drawn by an
agent from the world news of Friday 20 November 2026. This program's only
job is to deliver those exact bytes to the grader: it copies entry.png from
beside this file into the output directory, unchanged, every run.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"


def source_image() -> Path:
    """The image committed beside this program."""
    return Path(__file__).resolve().parent / IMAGE_NAME


def output_path() -> Path:
    """Where the grader reads the entry from."""
    out_dir = Path(os.environ.get(OUTPUT_ENV_VAR, DEFAULT_OUTPUT_DIR))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / IMAGE_NAME


def main() -> int:
    src = source_image()
    if not src.is_file():
        print(f"error: {src} is missing", file=sys.stderr)
        return 1
    dst = output_path()
    shutil.copyfile(src, dst)
    digest = hashlib.sha256(dst.read_bytes()).hexdigest()
    if digest != hashlib.sha256(src.read_bytes()).hexdigest():
        print("error: copied image differs from the committed image",
              file=sys.stderr)
        return 1
    print(f"wrote {dst} ({dst.stat().st_size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
