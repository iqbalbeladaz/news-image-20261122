#!/usr/bin/env python3
"""Draw the 22 November 2026 world-news summary image.

One 1024x1024 PNG, built only from the day's verified headlines:
COP31 collapse, Iran-Bahrain/Hormuz, Kyiv drone strike, the Shenzhen
Trump-Xi-Putin summit, the ICJ Rohingya genocide ruling, the global
AI sell-off, plus Mexico, Peru, Indonesia and BepiColombo in brief.
Run: python3 generate.py  -> writes entry.png beside this file.
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap, os

W = 1024
BG = (247, 243, 232)
INK = (18, 18, 20)
PAPER = (255, 255, 255)
MUTED = (84, 84, 88)

FD = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)

BOLD = "DejaVuSans-Bold.ttf"
REG = "DejaVuSans.ttf"

img = Image.new("RGB", (W, W), BG)
d = ImageDraw.Draw(img)

# ---- Masthead -------------------------------------------------------------
d.rectangle([0, 0, W, 150], fill=(16, 24, 48))
d.text((36, 18), "THE WORLD IN ONE DAY", font=font(BOLD, 52), fill=(255, 255, 255))
d.rectangle([36, 86, 988, 90], fill=(232, 64, 52))
d.text((36, 100), "SUNDAY  22 NOVEMBER 2026", font=font(BOLD, 34), fill=(255, 209, 64))
d.text((988, 100), "ONE IMAGE  •  THE DAY'S NEWS", font=font(BOLD, 20),
       fill=(210, 218, 235), anchor="ra")

# ---- Story panels ----------------------------------------------------------
# (accent, kicker, headline, body)
stories = [
    ((22, 138, 90), "CLIMATE  •  ANTALYA, TURKIYE",
     "COP31 TALKS COLLAPSE",
     "Climate summit ends with NO DEAL. EU rejects final draft that left out fossil fuels."),
    ((200, 52, 40), "CONFLICT  •  BAHRAIN / HORMUZ",
     "IRAN STRIKES BAHRAIN",
     "Missiles hit a Sitra industrial site, 2 injured. Tankers struck near Strait of Hormuz."),
    ((52, 92, 180), "WAR  •  KYIV REGION, UKRAINE",
     "DRONE LEVELS APARTMENTS",
     "Russian drone collapses a Kyiv-region apartment block. At least 14 people missing."),
    ((128, 70, 170), "DIPLOMACY  •  SHENZHEN, CHINA",
     "TRUMP, XI & PUTIN MEET",
     "First-ever trilateral summit issues joint call on nuclear risks. No Ukraine breakthrough."),
    ((176, 120, 20), "JUSTICE  •  THE HAGUE",
     "MYANMAR: GENOCIDE RULING",
     "World Court rules Myanmar committed genocide against the Rohingya in 2017."),
    ((10, 130, 140), "MARKETS  •  NEW YORK / TOKYO",
     "AI SELL-OFF: STOCKS SINK",
     "S&P 500 falls 3.7% into correction. Nasdaq -5.3%, Nikkei -5.1% as AI rout goes global."),
]

margin, gap = 36, 20
panel_w = (W - 2 * margin - gap) // 2
panel_h = 178
top = 172
for i, (accent, kicker, head, body) in enumerate(stories):
    x = margin + (i % 2) * (panel_w + gap)
    y = top + (i // 2) * (panel_h + gap)
    d.rounded_rectangle([x, y, x + panel_w, y + panel_h], radius=14, fill=PAPER,
                        outline=(215, 208, 190), width=2)
    d.rectangle([x, y, x + panel_w, y + 10], fill=accent)
    d.text((x + 20, y + 24), kicker, font=font(BOLD, 17), fill=accent)
    # headline may need two lines for the longest ones
    hy = y + 52
    for line in textwrap.wrap(head, width=24):
        size = 27
        while size > 18 and d.textlength(line, font=font(BOLD, size)) > panel_w - 40:
            size -= 1
        d.text((x + 20, hy), line, font=font(BOLD, size), fill=INK)
        hy += 32
    by = hy + 4
    for line in textwrap.wrap(body, width=39):
        d.text((x + 20, by), line, font=font(REG, 19), fill=MUTED)
        by += 24

# ---- Also today strip -------------------------------------------------------
strip_y = top + 3 * (panel_h + gap) + 2
d.rounded_rectangle([margin, strip_y, W - margin, 962], radius=14,
                    fill=(16, 24, 48))
d.text((margin + 20, strip_y + 14), "ALSO TODAY", font=font(BOLD, 22),
       fill=(255, 209, 64))
briefs = [
    "MEXICO: Cartel boss 'El Chapo Isidro' captured in Sinaloa - 11 killed in the raid.",
    "PERU: Magnitude 6.7 earthquake shakes the Andes near Junin.",
    "INDONESIA: Candy-factory fire in Banten kills 3 workers, 36 still missing.",
    "SPACE: BepiColombo reaches Mercury orbit after an 8-year journey.",
    "TRADE: EU-Indonesia deal signed, scrapping tariffs on 98.5% of goods.",
]
by = strip_y + 50
for b in briefs:
    d.text((margin + 20, by), "•  " + b, font=font(BOLD, 19), fill=(240, 243, 250))
    by += 27

d.text((W // 2, 982), "The day's biggest stories, across every region - in a single picture.",
       font=font(REG, 18), fill=MUTED, anchor="ma")

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, optimize=True)
print("wrote", out, os.path.getsize(out), "bytes")
