#!/usr/bin/env python3
"""Entrypoint for the make.fun news-image-20261122 bounty.

Standard library only. Copies the bundled entry.png byte for byte to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png). No network,
no clock, no randomness, so two runs always write identical bytes.
"""
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
