#!/usr/bin/env python3
"""Render the news-image-20261121 front page (1024x1024 PNG).

Saturday 21 November 2026 in one picture: 37 dated stories, 9 regions.
3 leads, 12 mains, 21 briefs, a numbered world map, a UTC timeline and a
BY THE NUMBERS strip. Everything is drawn with PIL from data written in
this file: no network, no clock, no randomness, so every run writes the
same bytes.

Run:  python3 draw_20261121.py   (writes entry.png next to this file)
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W = H = 1024
PAPER = (246, 241, 231)
INK = (20, 32, 43)
NAVY = (14, 42, 71)
NAVY_SOFT = (27, 68, 110)
RED = (179, 38, 30)
GOLD = (201, 162, 39)
GOLD_BG = (242, 230, 196)
LINE = (180, 172, 156)
CARD = (255, 255, 255)
MUTED = (90, 98, 108)
GREEN = (31, 122, 74)

REGION_COLORS = {
    "NORTH AMERICA": (31, 122, 74),
    "SOUTH AMERICA": (186, 104, 24),
    "EUROPE": (27, 68, 110),
    "MIDDLE EAST": (179, 38, 30),
    "AFRICA": (122, 74, 158),
    "SOUTH ASIA": (196, 94, 20),
    "EAST ASIA": (14, 120, 122),
    "OCEANIA": (32, 120, 168),
    "GLOBAL": (90, 98, 108),
}

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
F_B = lambda s: font("DejaVuSans-Bold.ttf", s)
F_R = lambda s: font("DejaVuSans.ttf", s)
F_OB = lambda s: font("DejaVuSerif.ttf", s)

# ---------------------------------------------------------------- data
# (number, kicker, headline, summary, region, lat, lon)  lat/lon None
# means the story has no map pin (space / global markets).

LEADS = [
    (1, "CLIMATE · ANTALYA", "COP31 overtime: new text out, decision Sunday",
     "Talks run past Friday's deadline into Saturday night. The presidency "
     "circulates a final text with no fossil fuels named — only a nod to the "
     "2023 Dubai deal — and calls a 06:00 GMT Sunday session. Longest COP ever.", "EUROPE", 36.90, 30.71),
    (2, "MIDDLE EAST · CLAIM", "Iran claims strikes on two US bases in Bahrain",
     "The IRGC says missiles and drones hit US Patriot radars at Al-Riffa and "
     "Awali after US drones entered Iranian airspace. Bahrain says an "
     "industrial site burned and no one was hurt.", "MIDDLE EAST", 26.23, 50.59),
    (3, "DISASTER · PERU", "M6.7 quake shakes central Peru; felt in Lima",
     "USGS: 00:09 UTC, 9 km from Carhuamayo in Junín, 108 km deep. No deaths "
     "in early reports; residents took to the streets in Lima. A M5.0 "
     "aftershock followed at 05:12 UTC.", "SOUTH AMERICA", -10.86, -75.98),
]

MAINS = [
    (4, "MIDDLE EAST", "Riyadh intercepts 3 Houthi missiles",
     "Saudi coalition destroys three ballistic missiles aimed at the capital.",
     "MIDDLE EAST", 24.71, 46.68),
    (5, "SPACE", "BepiColombo enters Mercury orbit",
     "ESA–JAXA probe captured at 18:24 UTC after 8 years; 2nd ever at Mercury.",
     "GLOBAL", None, None),
    (6, "WAR · UKRAINE", "Russia hits Kyiv again; boy, 7, killed in Kryvyi Rih",
     "3 missiles, 148 drones overnight; boy, 7, and a paramedic killed.",
     "EUROPE", 50.45, 30.52),
    (7, "EUROPE", "Rutte: NATO will defend every inch of Poland",
     "A day after three objects, likely Russian, crossed Polish airspace.",
     "EUROPE", 52.23, 21.01),
    (8, "AMERICAS", "Mexico captures 'El Chapo Isidro'",
     "Fausto Isidro Meza Flores, 44, FBI top-10 fugitive, taken in Guasave.",
     "NORTH AMERICA", 25.57, -108.47),
    (9, "USA · DIPLOMACY", "Trump hails Shenzhen summit; few gains",
     "President defends the trilateral; few concrete gains.",
     "NORTH AMERICA", 38.89, -77.04),
    (10, "MIDDLE EAST", "Israeli strike kills 3 in Gaza food truck",
     "Three killed in Tel al-Hawa; truck bore a WCK logo, WCK says not its truck.",
     "MIDDLE EAST", 31.50, 34.47),
    (11, "MARKETS", "Bitcoin breaks $60,000; low $55,130",
     "Lowest since Sep 2024, ~53% below its October peak; $1.8–2.4bn liquidated.",
     "GLOBAL", None, None),
    (12, "EUROPE", "France marches shrink on cost of living",
     "82,500 nationwide, 21,500 in Paris — down from 106,000 a week earlier.",
     "EUROPE", 48.85, 2.35),
    (13, "AMERICAS", "Bolsonaro taken to ICU",
     "Ex-president, 71, stable after an abdominal obstruction; serves 27 years.",
     "SOUTH AMERICA", -15.79, -47.88),
    (14, "AFRICA", "Nigeria boat toll rises to 24",
     "Boat of mourners capsized Friday; 24 bodies found, 24 rescued.",
     "AFRICA", 4.87, 6.17),
    (15, "ASIA", "Toxic alcohol kills 11 in Manipur",
     "At least 11 dead, 180+ in hospital after tainted liquor in Chandel.",
     "SOUTH ASIA", 24.21, 94.05),
]

BRIEFS = [
    ("Leeds stun Chelsea 4-1 at Stamford Bridge.", 51.48, -0.19),
    ("Newcastle 2-2 Arsenal; Madueke's late leveller.", 54.98, -1.62),
    ("Man City held 1-1 by Fulham at the Etihad.", 53.48, -2.24),
    ("Bournemouth 2-0 Forest; ninth straight win.", 50.74, -1.83),
    ("Tottenham 2-0 Ipswich; teen Williams-Barnett scores.", 51.60, -0.07),
    ("Malen hits four as Roma rout Parma 5-1.", 44.80, 10.33),
    ("Bayern held 1-1 by Cologne.", 48.22, 11.65),
    ("Real Madrid fight back to beat Celta 2-1.", 40.45, -3.69),
    ("Boca beat Mineiro 2-0; third Copa Sudamericana title.", 10.96, -74.80),
    ("Kansas City Current win first NWSL title, 2-1.", 38.87, -77.00),
    ("Columbus Crew stun Messi's Inter Miami 3-0.", 25.76, -80.19),
    ("Hearts thrash Dundee 8-0 in Scotland.", 56.47, -2.99),
    ("PSG beat Nice 3-2; Doué suffers knee injury.", 43.70, 7.27),
    ("IG Metall calls Monday strike; 23,000 workers, 19 firms.", 53.55, 10.00),
    ("Sudan: UN says 2,500+ displaced in West Kordofan.", 12.35, 29.25),
    ("Estonia to shut Russia road border from 1 Dec.", 59.38, 28.20),
    ("Peru aftershock M5.0 at 05:12 UTC, Junín.", -11.16, -75.99),
    ("NATO Council to meet Monday on Poland airspace.", 50.85, 4.35),
    ("Mexico: $5m US reward stood behind El Chapo Isidro.", 19.43, -99.13),
    ("Rahul 136 puts India 118 ahead of New Zealand.", -41.29, 174.78),
    ("Cyclone Xavier weakens over the Cook Islands.", -21.24, -159.77),
    ("Cricket Australia backs Cummins for NZ Tests.", -33.87, 151.21),
]

NUMBERS = [
    ("$55,130", "Bitcoin's Saturday low,\nlowest since Sep 2024"),
    ("148", "drones Russia launched\nat Ukraine overnight"),
    ("82,500", "marchers across France,\npolice count"),
    ("24", "dead in the Nigeria boat\ndisaster, toll updated Sat"),
]

UTC_STRIP = ("00:09 UTC  M6.7 quake, Peru  ·  05:12 UTC  M5.0 aftershock  ·  "
             "18:24 UTC  BepiColombo at Mercury  ·  LATE SAT  COP31 text out; "
             "decision 06:00 GMT Sun")

# Rough continent outlines (lon, lat), equirectangular.
CONTINENTS = [
    # North America
    [(-168, 66), (-158, 71), (-140, 70), (-125, 71), (-110, 73), (-95, 80),
     (-85, 80), (-80, 73), (-75, 72), (-65, 60), (-55, 52), (-60, 47),
     (-70, 44), (-75, 35), (-80, 32), (-85, 30), (-90, 21), (-95, 19),
     (-100, 16), (-105, 20), (-110, 23), (-115, 30), (-125, 40),
     (-125, 49), (-135, 58), (-150, 60), (-165, 60)],
    # Greenland
    [(-58, 64), (-45, 60), (-40, 65), (-30, 68), (-20, 70), (-25, 76),
     (-40, 80), (-55, 76), (-60, 70)],
    # South America
    [(-80, 10), (-75, 7), (-70, 12), (-60, 8), (-52, 5), (-50, 0),
     (-40, -5), (-35, -8), (-40, -20), (-48, -28), (-55, -35), (-65, -45),
     (-70, -52), (-73, -50), (-73, -40), (-72, -30), (-70, -18),
     (-77, -12), (-80, -5), (-81, 0), (-80, 7)],
    # Africa
    [(-17, 15), (-10, 30), (-5, 35), (10, 37), (20, 32), (32, 31),
     (35, 28), (40, 15), (48, 11), (51, 12), (48, 0), (40, -10),
     (35, -18), (32, -28), (25, -34), (18, -35), (15, -27), (12, -18),
     (9, -1), (9, 4), (-8, 5), (-13, 8), (-17, 12)],
    # Eurasia
    [(-10, 36), (-9, 43), (-2, 48), (-5, 50), (0, 52), (5, 58), (8, 57),
     (10, 59), (18, 56), (21, 55), (24, 58), (28, 60), (30, 70), (40, 68),
     (55, 68), (70, 72), (90, 75), (110, 76), (130, 72), (150, 70),
     (170, 66), (178, 65), (170, 60), (160, 58), (145, 55), (140, 50),
     (135, 43), (127, 40), (122, 32), (115, 23), (108, 18), (105, 10),
     (100, 8), (98, 12), (95, 16), (90, 22), (85, 20), (80, 13),
     (77, 8), (72, 20), (66, 25), (60, 25), (55, 26), (50, 30), (48, 30),
     (44, 29), (40, 35), (36, 36), (30, 36), (26, 38), (22, 37),
     (19, 40), (15, 44), (12, 44), (8, 44), (3, 43), (-2, 37), (-9, 37)],
    # Australia
    [(113, -22), (114, -30), (115, -35), (120, -34), (130, -32), (135, -35),
     (140, -38), (145, -38), (150, -37), (153, -32), (153, -27), (150, -22),
     (146, -19), (142, -15), (142, -11), (137, -12), (135, -15), (132, -12),
     (130, -13), (126, -14), (122, -17), (118, -20)],
    # Japan
    [(130, 31), (133, 34), (137, 35), (140, 38), (141, 41), (143, 43),
     (141, 45), (140, 42), (138, 38), (135, 34), (132, 33)],
]

# ---------------------------------------------------------------- helpers

def wrap_text(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def pill(draw, x, y, text, color):
    fnt = F_B(11)
    tw = draw.textlength(text, font=fnt)
    pad = 7
    draw.rounded_rectangle([x, y, x + tw + pad * 2, y + 17],
                           radius=8, fill=color)
    draw.text((x + pad, y + 2), text, font=fnt, fill=(255, 255, 255))
    return tw + pad * 2


def motif(draw, kind, cx, cy, r, color):
    """A small pictogram for a lead story: globe, burst, or quake line."""
    if kind == "globe":
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=3)
        draw.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r],
                     outline=color, width=2)
        draw.line([cx - r, cy, cx + r, cy], fill=color, width=2)
        draw.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
                 start=200, end=340, fill=color, width=2)
    elif kind == "burst":
        for ang in range(0, 360, 45):
            import math
            a = math.radians(ang)
            x2 = cx + r * math.cos(a)
            y2 = cy + r * math.sin(a)
            draw.line([cx, cy, x2, y2], fill=color, width=3)
        draw.ellipse([cx - r * 0.35, cy - r * 0.35, cx + r * 0.35,
                      cy + r * 0.35], fill=color)
    else:  # quake zigzag
        pts = [(cx - r, cy), (cx - r * 0.5, cy - r * 0.5),
               (cx - r * 0.2, cy + r * 0.6), (cx + r * 0.15, cy - r * 0.7),
               (cx + r * 0.45, cy + r * 0.4), (cx + r, cy)]
        draw.line(pts, fill=color, width=3, joint="curve")


# ---------------------------------------------------------------- page

def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ------------------------------------------------------
    d.rectangle([0, 0, W, 96], fill=NAVY)
    d.rectangle([0, 96, W, 99], fill=GOLD)
    d.text((24, 14), "THE WORLD IN ONE DAY", font=F_SERIF_B(40), fill=(255, 255, 255))
    d.text((24, 62), "37 STORIES  ·  9 REGIONS  ·  ALL DATED SAT 21 NOV 2026",
           font=F_B(14), fill=(201, 162, 39))
    right = "SATURDAY\n21 NOVEMBER 2026"
    d.text((W - 24, 12), "SATURDAY", font=F_SERIF_B(26),
           fill=(255, 255, 255), anchor="ra")
    d.text((W - 24, 46), "21 NOVEMBER 2026", font=F_B(20),
           fill=(201, 162, 39), anchor="ra")

    # ---- UTC strip ------------------------------------------------------
    d.rectangle([0, 99, W, 124], fill=GOLD_BG)
    d.text((24, 105), UTC_STRIP, font=F_B(11), fill=INK)
    d.line([0, 124, W, 124], fill=LINE, width=1)

    # ---- leads ----------------------------------------------------------
    lead_y, lead_h = 132, 172
    col_w = (W - 48 - 2 * 12) // 3
    kinds = ["globe", "burst", "quake"]
    for i, (num, kick, head, summ, region, lat, lon) in enumerate(LEADS):
        x = 24 + i * (col_w + 12)
        color = REGION_COLORS[region]
        d.rounded_rectangle([x, lead_y, x + col_w, lead_y + lead_h],
                            radius=6, fill=CARD, outline=LINE, width=1)
        d.rectangle([x, lead_y, x + col_w, lead_y + 5], fill=color)
        motif(d, kinds[i], x + col_w - 34, lead_y + 30, 16, color)
        d.text((x + 12, lead_y + 12), "LEAD %d" % num, font=F_B(12),
               fill=color)
        pill(d, x + 12, lead_y + 34, kick, color)
        lines = wrap_text(d, head, F_B(19), col_w - 24)
        draw_lines(d, lines[:3], x + 12, lead_y + 60, F_B(19), INK, 23)
        slines = wrap_text(d, summ, F_R(12), col_w - 24)
        draw_lines(d, slines[:4], x + 12, lead_y + 60 + 23 * min(3, len(lines)),
                   F_R(12), (60, 68, 78), 14)

    # ---- by the numbers --------------------------------------------------
    num_y, num_h = 312, 44
    d.rectangle([24, num_y, W - 24, num_y + num_h], fill=NAVY)
    d.text((36, num_y + 12), "BY THE NUMBERS", font=F_B(13), fill=GOLD)
    seg_w = (W - 48 - 170) // 4
    for i, (val, lab) in enumerate(NUMBERS):
        x = 24 + 170 + i * seg_w
        d.text((x, num_y + 4), val, font=F_B(19), fill=(255, 255, 255))
        for j, lab_line in enumerate(lab.split("\n")):
            d.text((x, num_y + 25 + j * 10), lab_line, font=F_R(9),
                   fill=(190, 200, 212))

    # ---- mains grid ------------------------------------------------------
    grid_y = 364
    gw = (W - 48 - 3 * 10) // 4
    gh = 92
    for i, (num, kick, head, summ, region, lat, lon) in enumerate(MAINS):
        r, c = divmod(i, 4)
        x = 24 + c * (gw + 10)
        y = grid_y + r * (gh + 8)
        color = REGION_COLORS[region]
        d.rounded_rectangle([x, y, x + gw, y + gh], radius=5, fill=CARD,
                            outline=LINE, width=1)
        d.rectangle([x, y, x + 5, y + gh], fill=color)
        d.text((x + 12, y + 6), "%d · %s" % (num, kick), font=F_B(10),
               fill=color)
        hlines = wrap_text(d, head, F_B(13), gw - 20)
        draw_lines(d, hlines[:2], x + 12, y + 24, F_B(13), INK, 16)
        slines = wrap_text(d, summ, F_R(10), gw - 20)
        draw_lines(d, slines[:2], x + 12, y + 24 + 16 * min(2, len(hlines)),
                   F_R(10), MUTED, 12)

    # ---- map + briefs ----------------------------------------------------
    sec_y, sec_h = 656, 300
    d.line([24, sec_y - 6, W - 24, sec_y - 6], fill=LINE, width=1)
    map_x0, map_y0, map_x1, map_y1 = 24, sec_y + 22, 430, sec_y + sec_h - 8
    d.text((map_x0, sec_y + 2), "WHERE IT HAPPENED", font=F_B(13), fill=NAVY)
    d.rectangle([map_x0, map_y0, map_x1, map_y1], fill=(226, 234, 240),
                outline=LINE, width=1)

    def project(lon, lat):
        px = map_x0 + (lon + 180.0) / 360.0 * (map_x1 - map_x0)
        py = map_y0 + (84.0 - lat) / (84.0 + 58.0) * (map_y1 - map_y0)
        return px, py

    for poly in CONTINENTS:
        pts = [project(lon, lat) for lon, lat in poly]
        d.polygon(pts, fill=(148, 168, 150), outline=(110, 130, 114))
    # graticule
    for lon in range(-150, 181, 30):
        x0, _ = project(lon, 0)
        _, y_top = project(lon, 84)
        _, y_bot = project(lon, -58)
        d.line([x0, y_top, x0, y_bot], fill=(205, 216, 224), width=1)

    pins = [(n, lat, lon) for (n, *_rest, lat, lon) in
            [(l[0], l[1], l[2], l[3], l[4], l[5], l[6]) for l in LEADS]
            if lat is not None]
    pins += [(n, lat, lon) for (n, _k, _h, _s, _r, lat, lon) in MAINS
             if lat is not None]
    for n, lat, lon in pins:
        px, py = project(lon, lat)
        d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=RED,
                  outline=(255, 255, 255), width=1)
        d.text((px, py - 1), str(n), font=F_B(10), fill=(255, 255, 255),
               anchor="mm")

    # briefs column
    bx = 448
    d.text((bx, sec_y + 2), "ALSO ON SATURDAY 21 NOVEMBER  —  22 MORE STORIES",
           font=F_B(13), fill=NAVY)
    f_brief = F_R(11)
    y = sec_y + 22
    for i, (text, _lat, _lon) in enumerate(BRIEFS, start=16):
        d.text((bx, y), "%d." % i, font=F_B(11), fill=RED)
        d.text((bx + 26, y), text, font=f_brief, fill=INK)
        y += 12
    d.text((bx, y + 2), "Numbered 16–37. Pins 1–15 on the map.",
           font=F_OB(10), fill=MUTED)

    # ---- footer ----------------------------------------------------------
    fy = 964
    d.line([24, fy, W - 24, fy], fill=LINE, width=1)
    d.text((24, fy + 6),
           "SOURCES: Reuters · AP · BBC · AFP · UN · ESA · USGS · Xinhua. "
           "Full source list in SOURCES.md.",
           font=F_R(10), fill=MUTED)
    d.text((24, fy + 22),
           "DATE CHECK: every story above happened or was first reported "
           "Saturday 21 November 2026 (UTC).",
           font=F_B(10), fill=INK)
    d.text((24, fy + 38),
           "LEFT OUT AS OTHER DAYS' NEWS: COP31 collapse (22 Nov) · Korea "
           "minister resigns (22 Nov) · GTA VI $3.79bn (20 Nov) · Anthropic "
           "IPO (19 Nov) · Shenzhen summit (19 Nov).",
           font=F_R(10), fill=MUTED)

    img.save(OUT, optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    build()
