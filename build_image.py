#!/usr/bin/env python3
"""Poster for 22 November 2026: one day, six beats, as a vertical timeline.

Fresh build for the make.fun news-image-20261122 bounty. Dark navy page,
a spine down the left, one numbered node per story, big market numbers
with dividers between them, and an ALSO strip at the bottom.

Run: python3 build_image.py entry.png
"""
import sys
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
NAVY = (15, 28, 48)
PANEL = (27, 45, 72)
PAPER = (244, 241, 234)
MUTED = (175, 187, 203)
AMBER = (242, 183, 5)
CORAL = (228, 87, 46)
TEAL = (46, 196, 182)
SPINE = (76, 98, 130)
RULE = (58, 78, 106)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

MX = 48            # side margin
TX = 124           # timeline text x
SPINE_X = 82       # timeline spine x
TW = W - MX - TX   # timeline text width


def load(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, width):
    lines = []
    for chunk in text.split("\n"):
        words = chunk.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for w in words[1:]:
            trial = cur + " " + w
            if draw.textlength(trial, font=font) <= width:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def para(draw, x, y, width, text, font, fill, leading=5):
    for line in wrap(draw, text, font, width):
        draw.text((x, y), line, font=font, fill=fill)
        y += font.size + leading
    return y


def node(draw, y, num, kicker, color, headline, body):
    kick_f = load(SANS_B, 17)
    head_f = load(SERIF_B, 25)
    body_f = load(SANS, 19)
    draw.ellipse([SPINE_X - 10, y + 1, SPINE_X + 10, y + 21], fill=color)
    draw.text((TX, y), num + "  " + kicker, font=kick_f, fill=color)
    y += 26
    y = para(draw, TX, y, TW, headline, head_f, PAPER, leading=3)
    y += 4
    y = para(draw, TX, y, TW, body, body_f, MUTED, leading=5)
    return y + 14


def main(out_path):
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # ---- header ----
    y = 38
    d.text((MX, y), "SUNDAY, 22 NOVEMBER 2026", font=load(SANS_B, 19), fill=AMBER)
    y += 30
    d.text((MX, y), "One day, six beats", font=load(SERIF_B, 46), fill=PAPER)
    y += 62
    d.line([(MX, y), (W - MX, y)], fill=RULE, width=2)

    # ---- lead panel: COP31 ----
    top = 148
    d.rounded_rectangle([MX, top, W - MX, top + 150], radius=14, fill=PANEL)
    d.rectangle([MX, top + 12, MX + 6, top + 150 - 12], fill=AMBER)
    d.text((MX + 30, top + 16), "LEAD  ·  CLIMATE — COP31", font=load(SANS_B, 18), fill=AMBER)
    d.text((MX + 30, top + 46), "COP31 ends in Antalya with no deal", font=load(SERIF_B, 32), fill=PAPER)
    para(d, MX + 30, top + 96, W - MX - 30 - (MX + 30),
         "Two days past its deadline, the climate summit closed without an "
         "agreement: the EU and others rejected a draft that left out fossil fuels.",
         load(SANS, 20), MUTED, leading=5)

    # ---- timeline spine ----
    d.line([(SPINE_X, 338), (SPINE_X, 712)], fill=SPINE, width=3)

    y = 328
    y = node(d, y, "01", "IRAN  ·  THE GULF", CORAL,
             "Missiles strike Bahrain; tankers hit near Hormuz",
             "Iran fired missiles and drones at Bahrain's Sitra zone, injuring "
             "two, one seriously, and hit three tankers near Hormuz. Saudi "
             "Arabia, Kuwait and Qatar condemned the strikes.")
    y = node(d, y, "02", "UKRAINE  ·  THE WAR", TEAL,
             "Drone hits Kyiv apartment block; ship burns at sea",
             "A Russian drone hit a five-storey apartment in Dymer near Kyiv, "
             "leaving 14 missing. Sparta II caught fire in the Gulf of Finland; "
             "a Russian missile landed in Poland.")
    y = node(d, y, "03", "MEXICO  ·  CARTELS", AMBER,
             "FBI-wanted cartel boss seized in Sinaloa",
             "Special forces captured Fausto Isidro Meza Flores, known as "
             "\"El Chapo Isidro\", in Sinaloa. Eleven people were killed, "
             "including four soldiers.")

    # ---- markets node: headline plus a row of big numbers ----
    kick_f = load(SANS_B, 17)
    head_f = load(SERIF_B, 25)
    num_f = load(SERIF_B, 34)
    lab_f = load(SANS, 16)
    d.ellipse([SPINE_X - 10, y + 1, SPINE_X + 10, y + 21], fill=CORAL)
    d.text((TX, y), "04  MARKETS  ·  THE SELL-OFF", font=kick_f, fill=CORAL)
    y += 26
    y = para(d, TX, y, TW, "AI sell-off drags world markets down", head_f, PAPER, leading=3)
    y += 8
    marks = [("S&P 500", "-3.7%"), ("Nasdaq", "-5.3%"), ("Nikkei", "-5.06%")]
    col_w = TW // 3
    num_top = y
    for i, (label, val) in enumerate(marks):
        cx = TX + i * col_w
        d.text((cx, y), val, font=num_f, fill=AMBER)
        d.text((cx, y + 42), label, font=lab_f, fill=MUTED)
    for i in (1, 2):
        dx = TX + i * col_w - 18
        d.line([(dx, num_top + 2), (dx, num_top + 58)], fill=RULE, width=1)
    y += 66
    y = para(d, TX, y, TW,
             "US stocks slid into correction on Friday as the sell-off spread.",
             load(SANS, 19), MUTED, leading=5)
    y += 14

    # ---- ALSO band ----
    d.line([(MX, y), (W - MX, y)], fill=RULE, width=2)
    y += 12
    d.text((MX, y), "ALSO", font=load(SANS_B, 17), fill=AMBER)
    y += 26
    y = para(d, MX, y, W - 2 * MX,
             "World Court: Myanmar committed genocide against the Rohingya "
             "in 2017  ·  Xi, Trump and Putin meet in Shenzhen  ·  EU-Indonesia "
             "trade deal  ·  Cikande factory fire: 3 dead, 36 missing  ·  "
             "FBI probes suspected NCIC breach  ·  BepiColombo enters "
             "Mercury orbit",
             load(SANS, 17), PAPER, leading=5)
    y += 8
    d.line([(MX, H - 44), (W - MX, H - 44)], fill=RULE, width=2)
    foot = "Sources: wire reports  ·  22 November 2026"
    ff = load(SANS, 15)
    d.text(((W - d.textlength(foot, font=ff)) / 2, H - 34), foot, font=ff, fill=MUTED)

    print("last content y:", y)
    img.save(out_path, "PNG")
    print("wrote", out_path, img.size)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "entry.png")
