#!/usr/bin/env python3
"""Render the 22 November 2026 world-news cover (1024x1024 PNG).

Fresh design for the make.fun news-image-20261122 bounty: a modern
cover layout -- dark hero panel for the lead story, three story columns,
a big-figures markets strip, and an ALSO band. News verified from
reporting published 22 Nov 2026 (multiple wire/press sources).
Run: python3 build_image.py entry.png
"""
import sys
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (246, 241, 231)      # paper
INK = (26, 26, 26)        # near-black
NAVY = (20, 32, 46)       # hero panel
GOLD = (232, 180, 60)     # hero kicker
RED = (163, 22, 33)       # accent red
GREY = (90, 86, 78)
RULE = (26, 26, 26)
LIGHT = (233, 226, 210)   # panel fill
CREAM = (250, 248, 242)   # hero text

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        words = para.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for w in words[1:]:
            trial = cur + " " + w
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def para(draw, x, y, width, text, fnt, fill=INK, leading=6):
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def main(out_path):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    mx = 40
    x0, x1 = mx, W - mx

    # ---- Masthead ----
    y = 28
    d.line([(x0, y), (x1, y)], fill=RED, width=4)
    y += 12
    title = "THE WORLD IN ONE DAY"
    tf = font(SERIF, 44)
    d.text(((W - d.textlength(title, font=tf)) / 2, y), title, font=tf, fill=INK)
    y += 56
    sub = "Sunday, 22 November 2026  \u00b7  The day's world news in one image"
    sf = font(SERIF_R, 20)
    d.text(((W - d.textlength(sub, font=sf)) / 2, y), sub, font=sf, fill=GREY)
    y += 32
    d.line([(x0, y), (x1, y)], fill=RULE, width=2)
    y += 16

    # ---- Hero: COP31 ----
    hero_top = y
    hero_h = 228
    d.rectangle([x0, y, x1, y + hero_h], fill=NAVY)
    hy = y + 18
    d.text((x0 + 24, hy), "CLIMATE  \u00b7  COP31", font=font(SANS_B, 19), fill=GOLD)
    hy += 32
    hf = font(SERIF, 42)
    d.text((x0 + 24, hy), "COP31 ends with no deal", font=hf, fill=CREAM)
    hy += 58
    bf = font(SANS, 21)
    hero_body = ("The Antalya summit closed on Sunday with no agreement at all, "
                 "after the EU and others rejected a draft that left out fossil "
                 "fuels. Talks ran two days past their deadline.")
    for line in wrap(d, hero_body, bf, x1 - x0 - 48):
        d.text((x0 + 24, hy), line, font=bf, fill=(215, 212, 205))
        hy += 29
    y = hero_top + hero_h + 18

    # ---- Three columns ----
    cols = [
        ("IRAN", "Missiles hit Bahrain",
         "Iran fired missiles and drones at an industrial zone in Sitra, "
         "Bahrain, wounding two, and hit three tankers near the Strait of "
         "Hormuz. Gulf states condemned the attacks."),
        ("UKRAINE", "Drone hits Kyiv suburb",
         "A Russian drone struck a five-storey apartment block in Dymer, "
         "near Kyiv, leaving 14 people missing. A Russian cargo ship "
         "burned in the Gulf of Finland, and a missile landed in Poland."),
        ("MEXICO", "Cartel boss captured",
         "Special forces seized FBI most-wanted drug lord Fausto Isidro "
         "Meza Flores, \u201cEl Chapo Isidro\u201d, in Sinaloa. Eleven "
         "people died in the raid, including four soldiers."),
    ]
    col_w = (x1 - x0 - 2 * 24) // 3
    col_top = y
    for i, (kick, head, body) in enumerate(cols):
        cx = x0 + i * (col_w + 24)
        d.line([(cx, col_top), (cx + col_w, col_top)], fill=RED, width=3)
        cy = col_top + 12
        d.text((cx, cy), kick, font=font(SANS_B, 16), fill=RED)
        cy += 26
        hy2 = cy
        for line in wrap(d, head, font(SERIF, 22), col_w):
            d.text((cx, hy2), line, font=font(SERIF, 22), fill=INK)
            hy2 += 28
        by = hy2 + 8
        by = para(d, cx, by, col_w, body, font(SANS, 17), fill=INK, leading=5)
    y = col_top + 252

    # ---- Markets strip: big figures ----
    d.rectangle([x0, y, x1, y + 138], fill=LIGHT)
    my = y + 14
    d.text((x0 + 22, my), "MARKETS", font=font(SANS_B, 18), fill=RED)
    summ = "The AI sell-off deepened on Friday as fears grew that heavy AI spending will not pay off."
    d.text((x0 + 200, my + 1), summ, font=font(SANS, 17), fill=INK)
    my += 40
    figs = [("S&P 500", "\u22123.7%"), ("Nasdaq", "\u22125.3%"),
            ("Nikkei", "\u22125.06%")]
    fw = (x1 - x0 - 44) // 3
    for i, (label, num) in enumerate(figs):
        fx = x0 + 22 + i * fw
        nf = font(SERIF, 36)
        d.text((fx, my), num, font=nf, fill=RED)
        lf = font(SANS_B, 17)
        d.text((fx, my + 48), label, font=lf, fill=INK)
    y = y + 138 + 16

    # ---- ALSO band ----
    d.text((x0, y), "ALSO", font=font(SANS_B, 18), fill=RED)
    y += 26
    also = ("World court: Myanmar guilty of genocide against the Rohingya in "
            "2017  \u00b7  First Xi\u2013Trump\u2013Putin summit in Shenzhen  "
            "\u00b7  EU\u2013Indonesia sign milestone trade deal  \u00b7  "
            "Indonesia factory fire: 3 dead, 36 missing  \u00b7  FBI probes "
            "suspected NCIC database breach  \u00b7  BepiColombo enters "
            "Mercury orbit")
    y = para(d, x0, y, x1 - x0, also, font(SANS, 17), fill=INK, leading=5)
    y += 4

    # ---- Footer ----
    d.line([(x0, H - 52), (x1, H - 52)], fill=RULE, width=2)
    foot = "Sources: AP \u00b7 Reuters \u00b7 Xinhua \u2014 22 Nov 2026"
    ff = font(SANS, 16)
    d.text(((W - d.textlength(foot, font=ff)) / 2, H - 40), foot, font=ff, fill=GREY)

    img.save(out_path, "PNG")
    print(f"wrote {out_path}: {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "entry.png")
