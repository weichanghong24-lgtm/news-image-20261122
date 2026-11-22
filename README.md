# The world in one day — 22 November 2026

One 1024×1024 poster that sums up 22 November 2026 in six beats:
a COP31 lead panel, then a vertical timeline — Iran, Ukraine, Mexico,
markets — and an ALSO strip at the bottom.

## Build

    python3 build_image.py entry.png

Needs Python 3 and Pillow; uses the DejaVu fonts shipped with the system.
The render is deterministic: running it twice gives the same bytes.

## Entrypoint

    MAKEFUN_OUTPUT_DIR=/output python3 main.py

`main.py` only copies `entry.png` into `$MAKEFUN_OUTPUT_DIR/entry.png`.
It builds nothing and needs only the standard library.

## Sources

Wire reports from 22 November 2026. Figures as reported that day:
S&P 500 -3.7%, Nasdaq -5.3%, Nikkei -5.06%.
