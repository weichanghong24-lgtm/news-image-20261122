# Build log — news-image-20261122

## v1 (first write)
- Wrote build_image.py from scratch: dark navy page, vertical timeline
  with four numbered nodes, a lead panel for COP31, big market numbers,
  and an ALSO strip. Ran it once: entry.png 1024x1024, 127,536 bytes,
  sha256 e91114be920bdf2b05f2225cdc0e246264da8b17bb1fd22d520b2244b3303bb2.
- Looked at the picture: clean, nothing overflowed, but the body grey
  was dim and the market numbers had no separation.

## v2 (revision)
- Brightened the body text, added hairline dividers between the three
  market columns, tightened the lead panel and moved the timeline up
  so the bottom has breathing room.
- Ran build_image.py twice: both runs sha256
  5969e158e856ce2d1f3973dee9661209f7723e4fa7184103d31710df86e29f5c.
- entry.png: 1024x1024, 128,557 bytes.

## Entrypoint check
- Ran main.py twice into two fresh folders; both copies sha256
  5969e158e856ce2d1f3973dee9661209f7723e4fa7184103d31710df86e29f5c,
  identical to entry.png.
