#!/usr/bin/env python3
"""Render the make.fun news-image-20261117 entry: a newspaper front page
summing up Tuesday 17 November 2026 world news. 48 stories, 15 illustrated.
Deterministic: fixed fonts, fixed layout, PNG saved with fixed parameters."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
W, H = 1024, 1024
PAPER = (246, 241, 229)
INK = (20, 20, 20)
RED = (163, 18, 18)
GREY = (90, 86, 76)
RULE = (60, 58, 50)
TILE = (232, 224, 205)

F_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
F_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_image(path, w, h):
    im = Image.open(path).convert("RGB")
    return ImageOps.fit(im, (w, h), Image.LANCZOS)


# ---------------------------------------------------------------- stories
# (region, headline, summary, icon or None). Lead stories are in LEADS.
STORIES = {
    "ME": [
        ("'DIRTY BOMB' PLOT CLAIM",
         "Trump says reports of an Iranian plot on Washington are taken seriously; intel unverified.", None),
        ("HOUTHI DRONES ON SAUDI PIPELINE",
         "Five drones hit two East-West pipeline stations near Riyadh.", None),
        ("GAZA'S WINTER RAINS WORSEN CRISIS",
         "UN: rains flood shelters and wreck food supplies in Gaza.", None),
        ("WEST URGES ISRAEL TO OPEN GAZA AID",
         "UK, Australia, Canada, Italy: open crossings; 'catastrophic'.", None),
        ("ISRAEL STRIKES SOUTH LEBANON",
         "Airstrikes, artillery fire and detonations reported across southern Lebanon.", None),
        ("HOUTHIS ADVANCE IN YEMEN",
         "Government forces pull back from the Red Sea coast to defend Aden.", None),
        ("TURKEY SEEKS DEFENCE PACTS",
         "FM announces pact meetings with Saudi Arabia, Pakistan, Egypt and European states.", None),
        ("MILITIA DEFIES BAGHDAD DEADLINE",
         "Kataib Hezbollah refuses to leave Jurf al-Sakhar after oil probe.", None),
        ("IRAN STRIKES BAHRAIN",
         "Third round of strikes on Bahrain, host of the US Navy's 5th Fleet.", None),
        ("THIRD US CARRIER REACHES THE GULF",
         "Another aircraft carrier arrives, boosting US options as fire is exchanged.", None),
        ("IRAQ OIL FLOWS RESUME",
         "Oil flows again via the rehabilitated Kirkuk-Ceyhan pipeline to Turkey.", None),
        ("UK SANCTIONS SETTLEMENT BUILDERS",
         "Britain sanctions companies building settlements in the West Bank.", None),
    ],
    "AF": [
        ("EBOLA 'OUT OF CONTROL' IN CONGO",
         "Africa CDC: 11,200+ cases, 5,500 dead across eight provinces.", "cross"),
        ("GUINEA GOLD-MINE CRACKDOWN",
         "More than 1,260 arrested in Siguiri after a ban on illegal gold mining.", None),
        ("IFC PLEDGES $500M FOR AFRICA",
         "New projects agreed at the Africa Financial Summit in Luanda.", None),
    ],
    "EU": [
        ("RUSSIA HITS KYIV BRIDGES",
         "Retaliation strikes on Kyiv's bridges after the Kerch attack.", "bridge"),
        ("DEPARDIEU PLEADS GUILTY",
         "French actor admits sexual assault and drops his appeal.", "gavel"),
        ("EU STATES PLAN RWANDA RETURNS HUB",
         "Austria, Denmark, Germany, Greece, Netherlands plan migrant hub; transfers from 2027.", None),
        ("EQUINOR HIT BY CYBERATTACK",
         "Norwegian energy giant reports an ongoing attack on its IT systems.", "lock"),
        ("RUSSIAN DRONES OVER MOLDOVA",
         "Seven drones enter Moldovan airspace for 2.5 hours; one flies over Chisinau.", None),
        ("TANKER SINKS IN THE BLACK SEA",
         "Liberian-flagged gas tanker goes down in Bulgaria's exclusive economic zone.", "tanker"),
        ("CZECH RAIL CRASHES",
         "Four railway incidents in two days, near Hluboka nad Vltavou and Prague.", None),
        ("ASSASSINATION PLOT ARRESTS",
         "North Macedonia arrests five over an alleged plot in Greece, on Iranian orders.", None),
        ("BERLIN RAIDS HEZBOLLAH-LINKED GROUP",
         "Germany bans an association suspected of backing Hezbollah; 28 sites raided.", None),
        ("ZAPORIZHZHIA TOLL RISES TO 40",
         "Russian strike toll raised to 40; aid-centre attack kills 26.", None),
    ],
    "AP": [
        ("TRUMP-XI-PUTIN SUMMIT SET",
         "Unprecedented trilateral summit planned in China as Trump travels on.", None),
        ("US CLOSES CHIP LOOPHOLE",
         "New rule targets third-country data centres renting compute to China.", "chip"),
        ("JAPAN SCRAMBLES JETS",
         "Two suspected Russian aircraft violate airspace near Okinoshima; Tokyo protests.", "jet"),
        ("PAKISTAN CUTS FUEL PRICES",
         "Petrol and diesel cut by Rs2 a litre from today.", None),
    ],
    "AM": [
        ("US LOSES MEASLES STATUS",
         "PAHO: measles elimination status lost, first time since 2000.", "cross"),
        ("NSA NETWORK GOES DOWN",
         "Classified internal network offline amid a week of outages; DNI denies cyberattack.", "globe"),
        ("EPSTEIN DEATH 'WAS MURDER'",
         "Forensic expert says the prison death was murder, not suicide.", "gavel"),
        ("WALL STREET FALLS",
         "US indexes close lower; AI and tech stocks under pressure.", "chart"),
        ("C-130 DESTROYED, ACTIVIST CHARGED",
         "Irish activist charged in New York over a $60M US aircraft.", "plane"),
        ("ETHANOL PLANT BOMB PLOT",
         "Illinois plant employee indicted over an alleged bomb plot.", "blast"),
        ("TIGER WOODS RETURNS",
         "Tiger Woods returns to golf.", "golf"),
        ("WAYMO PULLED FROM FREEWAYS",
         "Waymo robotaxis pulled from freeway service.", "car"),
        ("CALIFORNIA LANDFILL BLAST",
         "Explosion at a landfill in California.", "blast"),
        ("FLORIDA FLOODS, WESTERN STORM",
         "Flooding in Florida as a storm hits the west.", None),
    ],
    "GL": [
        ("NVIDIA SPY SCANDAL",
         "Record revenue amid a spy scandal around ex-CEO Jensen Huang.", "chip"),
        ("NATGEO PICTURES OF THE YEAR",
         "National Geographic publishes its 2026 Pictures of the Year.", None),
        ("APPLE OUTAGES RESOLVED",
         "Sign-in and App Store problems hit Apple services on Tuesday.", "phone"),
        ("DUBAI TRAFFIC DROPS 28%",
         "Dubai Airports: 50.4M passengers in 9 months, down 28.1%.", "plane"),
        ("NIGERIA INFLATION EASES",
         "Annual rate cools to 14.06% in October, lowest since September 2020.", "chart"),
    ],
}

LEADS = [
    ("media-generation-lead-hormuz-0-ab4307ac-0fb0-44da-b30d-33e166a2ef9e.webp",
     "WAR IN THE GULF: US HITS IRAN",
     "US warplanes strike Qeshm Island; gas tanker Tara Gas ablaze, 24 crew evacuated."),
    ("media-generation-lead-kerch-0-ef92b521-1f73-47e0-8850-77f6828a4276.webp",
     "KERCH BRIDGE HIT AGAIN",
     "Ukraine strikes the Crimean Bridge a 2nd day; a road span falls into the sea."),
    ("media-generation-lead-manila-0-63c85e3c-319d-468c-a4ff-0ecfa65bc29a.webp",
     "TRUMP LANDS IN MANILA",
     "Arrives for the Quad summit; ~1,500 protesters rally; China trilateral next."),
]

COLUMNS = [
    ("MIDDLE EAST & AFRICA", STORIES["ME"] + STORIES["AF"]),
    ("EUROPE & ASIA-PACIFIC", STORIES["EU"] + STORIES["AP"]),
    ("AMERICAS & GLOBAL", STORIES["AM"] + STORIES["GL"]),
]

REGION_COLORS = {"ME": (163, 18, 18), "AF": (176, 106, 12), "EU": (26, 72, 140),
                 "AP": (18, 110, 88), "AM": (94, 52, 140), "GL": (60, 60, 60)}

ICON_COLORS = {"chip": (26, 72, 140), "cross": (163, 18, 18), "globe": (18, 110, 88),
               "gavel": (94, 52, 140), "chart": (26, 72, 140), "plane": (18, 110, 88),
               "jet": (94, 52, 140), "lock": (163, 18, 18), "golf": (18, 110, 88),
               "car": (26, 72, 140), "blast": (176, 106, 12), "phone": (60, 60, 60),
               "bridge": (60, 60, 60), "tanker": (163, 18, 18)}


def draw_icon(d, kind, x, y, s, color):
    """Simple flat geometric pictogram inside an s x s box at (x, y)."""
    if kind == "chip":
        d.rounded_rectangle([x + 5, y + 5, x + s - 5, y + s - 5], 3, fill=color)
        d.rectangle([x + 9, y + 9, x + s - 9, y + s - 9], outline=PAPER, width=2)
        for i in range(3):
            d.line([x + 8 + i * 6, y + 2, x + 8 + i * 6, y + 5], fill=color, width=2)
            d.line([x + 8 + i * 6, y + s - 5, x + 8 + i * 6, y + s - 2], fill=color, width=2)
    elif kind == "cross":
        d.rectangle([x + s // 2 - 3, y + 4, x + s // 2 + 3, y + s - 4], fill=color)
        d.rectangle([x + 4, y + s // 2 - 3, x + s - 4, y + s // 2 + 3], fill=color)
    elif kind == "globe":
        d.ellipse([x + 3, y + 3, x + s - 3, y + s - 3], outline=color, width=3)
        d.ellipse([x + s // 2 - 5, y + 3, x + s // 2 + 5, y + s - 3], outline=color, width=2)
        d.line([x + 3, y + s // 2, x + s - 3, y + s // 2], fill=color, width=2)
    elif kind == "gavel":
        d.rectangle([x + 4, y + 5, x + s - 8, y + 12], fill=color)
        d.line([x + s - 8, y + 12, x + s - 3, y + s - 4], fill=color, width=4)
    elif kind == "chart":
        for i, hgt in enumerate((8, 13, 18)):
            d.rectangle([x + 4 + i * 8, y + s - 4 - hgt, x + 9 + i * 8, y + s - 4], fill=color)
    elif kind in ("plane", "jet"):
        d.polygon([(x + 3, y + s // 2), (x + s - 4, y + s // 2 - 3), (x + s - 4, y + s // 2 + 3)],
                  fill=color)
        d.polygon([(x + s // 2 - 2, y + s // 2 - 2), (x + s // 2 + 6, y + 3),
                   (x + s // 2 + 9, y + 3), (x + s // 2 + 4, y + s // 2)], fill=color)
        d.polygon([(x + s // 2 - 2, y + s // 2 + 2), (x + s // 2 + 6, y + s - 3),
                   (x + s // 2 + 9, y + s - 3), (x + s // 2 + 4, y + s // 2)], fill=color)
    elif kind == "lock":
        d.arc([x + 7, y + 4, x + s - 7, y + 16], 180, 360, fill=color, width=3)
        d.rounded_rectangle([x + 5, y + 14, x + s - 5, y + s - 4], 2, fill=color)
    elif kind == "golf":
        d.line([x + 8, y + 4, x + 8, y + s - 4], fill=color, width=2)
        d.polygon([(x + 8, y + 4), (x + s - 4, y + 8), (x + 8, y + 12)], fill=color)
        d.ellipse([x + s - 8, y + s - 7, x + s - 4, y + s - 3], fill=color)
    elif kind == "car":
        d.rounded_rectangle([x + 3, y + 12, x + s - 3, y + s - 7], 3, fill=color)
        d.polygon([(x + 8, y + 12), (x + 11, y + 6), (x + s - 11, y + 6), (x + s - 8, y + 12)],
                  fill=color)
        d.ellipse([x + 6, y + s - 9, x + 11, y + s - 4], fill=INK)
        d.ellipse([x + s - 11, y + s - 9, x + s - 6, y + s - 4], fill=INK)
    elif kind == "blast":
        cx, cy, r1, r2 = x + s // 2, y + s // 2, s // 2 - 2, s // 4
        pts = []
        import math
        for i in range(12):
            r = r1 if i % 2 == 0 else r2
            a = math.pi * i / 6
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        d.polygon(pts, fill=color)
    elif kind == "phone":
        d.rounded_rectangle([x + 8, y + 3, x + s - 8, y + s - 3], 3, outline=color, width=3)
        d.line([x + 11, y + 8, x + s - 11, y + 8], fill=color, width=2)
        d.line([x + 11, y + 13, x + s - 11, y + 13], fill=color, width=2)
    elif kind == "bridge":
        d.line([x + 3, y + s - 6, x + s - 3, y + s - 6], fill=color, width=3)
        d.line([x + 6, y + s - 6, x + 6, y + 6], fill=color, width=2)
        d.line([x + s - 6, y + s - 6, x + s - 6, y + 6], fill=color, width=2)
        d.arc([x + 4, y + 4, x + s - 4, y + s - 2], 180, 360, fill=color, width=2)
    elif kind == "tanker":
        d.polygon([(x + 3, y + s - 8), (x + s - 3, y + s - 8), (x + s - 6, y + s - 3),
                   (x + 6, y + s - 3)], fill=color)
        d.rectangle([x + s - 12, y + 6, x + s - 5, y + s - 8], fill=color)
        d.rectangle([x + 6, y + 12, x + s - 13, y + s - 8], fill=color)


def trunc(draw, text, fnt, max_w):
    if draw.textlength(text, font=fnt) <= max_w:
        return text
    # cut at a word boundary so the ellipsis never splits a word
    words = text.split(" ")
    out = ""
    for w in words:
        t = (out + " " + w).strip()
        if draw.textlength(t + " …", font=fnt) > max_w:
            break
        out = t
    return (out + " …") if out else "…"


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    f_mast = font(F_SERIF, 46)
    f_date = font(F_BOLD, 21)
    f_deck = font(F_BOLD, 13)
    f_lead_h = font(F_BOLD, 13)
    f_lead_s = font(F_SANS, 11)
    f_col = font(F_BOLD, 12)
    f_head = font(F_BOLD, 12)
    f_sum = font(F_SANS, 10)
    f_map = font(F_BOLD, 10)
    f_foot = font(F_BOLD, 12)
    f_small = font(F_SANS, 10)

    # ---- masthead
    d.text((W // 2, 12), "THE WORLD IN ONE DAY", font=f_mast, fill=INK, anchor="ma")
    d.text((W // 2, 66), "TUESDAY  ·  17 NOVEMBER 2026", font=f_date, fill=RED, anchor="ma")
    d.line([16, 96, W - 16, 96], fill=RULE, width=2)
    d.text((W // 2, 102), "48 STORIES  •  SIX CONTINENTS  •  ONE DAY OF WORLD NEWS",
           font=f_deck, fill=INK, anchor="ma")

    # ---- lead strip: 3 photos + captions
    lead_y, lead_h, gap = 122, 100, 12
    pw = (W - 32 - 2 * gap) // 3
    for i, (fname, head, summ) in enumerate(LEADS):
        x = 16 + i * (pw + gap)
        photo = fit_image(os.path.join(ASSETS, fname), pw, lead_h)
        img.paste(photo, (x, lead_y))
        d.rectangle([x, lead_y, x + pw - 1, lead_y + lead_h - 1], outline=RULE, width=1)
        cy = lead_y + lead_h + 6
        for line in wrap(d, head, f_lead_h, pw):
            d.text((x, cy), line, font=f_lead_h, fill=INK)
            cy += 15
        for line in wrap(d, summ, f_lead_s, pw):
            d.text((x, cy), line, font=f_lead_s, fill=(40, 40, 40))
            cy += 13
    d.line([16, 292, W - 16, 292], fill=RULE, width=2)

    # ---- map row: world map + at-a-glance box
    map_y, map_h = 300, 224
    map_w = 470
    world = Image.open(os.path.join(
        ASSETS, "media-generation-world-map-0-b54c4680-b71b-4924-8433-f49a9201cf56.webp")).convert("RGB")
    # crop to content (dark continents) bounding box
    grey = world.convert("L")
    bbox = grey.point(lambda p: 255 if p < 200 else 0).getbbox()
    world = world.crop(bbox)
    world.thumbnail((map_w, map_h), Image.LANCZOS)
    mx, my = 16, map_y + (map_h - world.height) // 2
    img.paste(world, (mx, my))
    d.rectangle([mx, my, mx + world.width - 1, my + world.height - 1], outline=RULE, width=1)
    # region dots + labels (fractions of the placed map)
    labels = [
        (0.16, 0.30, "N. AMERICA"), (0.27, 0.66, "S. AMERICA"), (0.47, 0.24, "EUROPE"),
        (0.50, 0.52, "AFRICA"), (0.585, 0.36, "M. EAST"), (0.70, 0.28, "ASIA"),
        (0.88, 0.62, "OCEANIA"),
    ]
    for fx, fy, name in labels:
        px, py = mx + int(fx * world.width), my + int(fy * world.height)
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=RED, outline=(255, 255, 255), width=1)
        d.text((px + 6, py - 6), name, font=f_map, fill=INK,
               stroke_width=2, stroke_fill=(246, 241, 229))

    # at-a-glance box
    bx, bw = 16 + map_w + 14, W - 16 - (16 + map_w + 14)
    d.rectangle([bx, map_y, bx + bw - 1, map_y + map_h - 1], outline=RULE, width=1)
    d.rectangle([bx, map_y, bx + bw - 1, map_y + 24], fill=INK)
    d.text((bx + 10, map_y + 5), "THE DAY AT A GLANCE", font=f_col, fill=(246, 241, 229))
    stats = [
        ("24", "seafarers evacuated from the burning gas tanker Tara Gas"),
        ("5", "Houthi drones fired at Saudi Arabia's East-West pipeline"),
        ("7", "Russian drones crossed Moldova; one flew over Chisinau"),
        ("50.4M", "Dubai airport passengers in 9 months — down 28.1%"),
    ]
    sy = map_y + 32
    for num, txt in stats:
        d.text((bx + 10, sy), num, font=f_col, fill=RED)
        nw = d.textlength(num, font=f_col)
        for line in wrap(d, txt, f_small, bw - 24 - nw):
            d.text((bx + 16 + nw, sy + 1), line, font=f_small, fill=INK)
            sy += 13
        sy += 5
    d.text((bx + 10, map_y + map_h - 20),
           "War in the Gulf  •  Bridges under fire  •  A summit in Manila",
           font=f_small, fill=GREY)
    d.line([16, 532, W - 16, 532], fill=RULE, width=2)

    # ---- story grid: 3 columns
    grid_y, grid_bottom = 540, 978
    col_w = (W - 32 - 2 * 12) // 3
    cell_h = 27
    for ci, (title, items) in enumerate(COLUMNS):
        cx = 16 + ci * (col_w + 12)
        d.rectangle([cx, grid_y, cx + col_w - 1, grid_y + 17], fill=INK)
        d.text((cx + 6, grid_y + 2), title, font=f_col, fill=(246, 241, 229))
        y = grid_y + 22
        for (head, summ, icon) in items:
            region = region_of(head)
            tx = cx
            if icon:
                d.rectangle([cx, y + 1, cx + 23, y + 24], fill=TILE, outline=RULE, width=1)
                draw_icon(d, icon, cx, y + 1, 24, ICON_COLORS[icon])
                tx = cx + 28
            rc = REGION_COLORS[region]
            f_tag = font(F_BOLD, 9)
            d.text((tx, y), region, font=f_tag, fill=rc)
            rw = d.textlength(region, font=f_tag)
            d.text((tx + rw + 5, y),
                   trunc(d, head, f_head, col_w - (tx - cx) - rw - 5), font=f_head, fill=INK)
            d.text((tx, y + 14),
                   trunc(d, summ, f_sum, col_w - (tx - cx)), font=f_sum, fill=(50, 48, 42))
            y += cell_h
        if ci < 2:
            d.line([cx + col_w + 6, grid_y, cx + col_w + 6, grid_bottom], fill=(200, 192, 170), width=1)

    # ---- footer
    d.line([16, 988, W - 16, 988], fill=RULE, width=2)
    d.text((W // 2, 994), "48 STORIES  •  15 ILLUSTRATED  •  TUESDAY 17 NOVEMBER 2026",
           font=f_foot, fill=INK, anchor="ma")
    d.text((W // 2, 1010),
           "Events of 17 Nov 2026, as reported by Reuters, AP, CNN, PAHO, the UN, Euronews and allAfrica.",
           font=f_small, fill=GREY, anchor="ma")

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, img.size, os.path.getsize(out), "bytes")


def region_of(head):
    for region, items in STORIES.items():
        for h, _s, _i in items:
            if h == head:
                return region
    return "GL"


if __name__ == "__main__":
    main()
