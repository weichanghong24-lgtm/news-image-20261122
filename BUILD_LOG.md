# Build log — make.fun bounty `news-image-20261122`

- Bounty: "Sum up 22 November's world news in one image"
  (https://make.fun/bounty/news-image-20261122), prize $100 (50 places paid:
  1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th $1.20 each),
  deadline 2026-11-24 00:00 UTC (01:00 CET).
- Built: 2026-11-22 ~22:35 CET. Fresh layout this time (cover style: dark
  hero panel, three story columns, big-figures markets strip) instead of
  reusing the 21 November newspaper layout.

## Specs followed

Same harness as 21 November (`program/v1`): entrypoint `main.py` at repo
root, run as `python3 -P -s /bot/main.py` (Python 3.13), standard library
only, no network, 60 s wall budget, 1 CPU, 512 MB, read-only repo at
`/bot`, empty writable `/output`. Program writes one image to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`); whole PNG,
at most 1 MiB and 1024×1024 px. Two runs must write identical bytes.

## News chosen (Sunday 22 November 2026)

Verified from reporting published 22 Nov 2026 (AP, Reuters, Xinhua and
other wire/press reporting, cross-checked across sources):

1. **Lead — COP31:** Antalya summit ended Sunday with no agreement; EU and
   others rejected a draft omitting fossil fuels; talks ran two days past
   deadline.
2. **Iran:** missiles/drones hit Sitra industrial zone in Bahrain, 2
   wounded (1 seriously); 3 tankers attacked near the Strait of Hormuz;
   Saudi Arabia, Kuwait, Qatar condemned the strikes.
3. **Ukraine:** Russian drone hit a 5-storey apartment block in Dymer near
   Kyiv, 14 missing; Russian cargo ship Sparta II caught fire in the Gulf
   of Finland after a suspected Ukrainian drone attack; Russian missile
   landed in Poland, NATO called it a violation.
4. **Mexico:** special forces captured FBI-wanted drug lord Fausto Isidro
   Meza Flores ("El Chapo Isidro") in Sinaloa; 11 dead including 4
   soldiers.
5. **Markets:** S&P 500 −3.7% Friday, Nasdaq −5.3%, Nikkei −5.06%; AI
   sell-off spreading.
6. **Also strip:** ICJ ruled Myanmar committed genocide against the
   Rohingya in 2017 (first state-responsibility finding); first
   Xi–Trump–Putin summit in Shenzhen, joint nuclear-risk statement, no
   Ukraine breakthrough; EU–Indonesia milestone trade deal; Indonesia
   Cikande candy-factory fire, 3 dead, 36 missing; FBI probing suspected
   NCIC database breach; BepiColombo entered Mercury orbit after 8 years.

## What the program does

- `build_image.py` — build-time generator (Pillow + DejaVu fonts on this
  machine). Renders the cover-style poster from the news text embedded in
  the script. Kept in the repo for provenance; the entry program does not
  run it. Final image inspected visually: clean, nothing clipped.
- `entry.png` — finished image, 1024×1024, 110,737 bytes.
- `main.py` — entrypoint. Stdlib only (`os`, `shutil`); copies the bundled
  `entry.png` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.png`. No network,
  no clock, no randomness.
- `README.md`, `LICENSE` (MIT, required repo file).

## Determinism verification

Grader-style invocation, two runs into separate empty output dirs:

```
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 -P -s main.py   -> exit 0
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 -P -s main.py   -> exit 0
```

SHA-256 (all three identical):

```
6e7f2abf331871bb04fc6adef8291d5667a407a28fba45c4e907e84f94cf68aa  entry.png
6e7f2abf331871bb04fc6adef8291d5667a407a28fba45c4e907e84f94cf68aa  /tmp/out1/entry.png
6e7f2abf331871bb04fc6adef8291d5667a407a28fba45c4e907e84f94cf68aa  /tmp/out2/entry.png
```

Output checks: 1024×1024 PNG, 110,737 bytes (limit 1,048,576).

## Requirements status

All met. Next steps: download this competition's kit, create public repo
`weichanghong24-lgtm/news-image-20261122` with these files (set repo About
website + topics BEFORE submitting — the 21 November entry was rejected
once for missing them), bundle transcripts with the make.fun kit CLI
(`--redact` Shuang's personal details), submit before 2026-11-24 01:00 CET.
