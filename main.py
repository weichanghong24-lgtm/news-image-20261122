#!/usr/bin/env python3
"""Entrypoint: drop the finished poster into the make.fun output folder.

The build step (build_image.py) renders entry.png next to this file.
This script only moves those bytes to $MAKEFUN_OUTPUT_DIR/entry.png,
creating the folder if needed. Standard library only.

Run: MAKEFUN_OUTPUT_DIR=/output python3 main.py
"""
import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        sys.exit("MAKEFUN_OUTPUT_DIR is not set")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    print("copied", src, "->", os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
