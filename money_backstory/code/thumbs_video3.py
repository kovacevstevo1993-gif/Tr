"""Miniature video 3 (stile 'concorrenti USA' del video 2): 9 varianti, 3 per titolo, 1280x720."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1280, 720
OUT = os.environ.get("OUT", "/home/user/Tr/money_backstory/miniature_video3")
os.makedirs(OUT, exist_ok=True)
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

NAVY = (22, 32, 60)
RED = (224, 40, 40)
YEL = (255, 214, 60)
GRN = (46, 160, 90)
GRN_L = (92, 178, 120)
WHITE = (255, 255, 255)
BLK = (0, 0, 0)
GOLD = (212, 160, 40)


def F(size, serif=False):
    return ImageFont.truetype(FS if serif else FB, size)


def bg(kind="light"):
    im = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(im)
    for y in range(H):
        t = y / H
        if kind == "light":
            c = (int(245 - 32 * t), int(243 - 34 * t), int(238 - 32 * t))
        else:
            c = (int(18 + 10 * t), int(30 + 14 * t), int(56 + 20 * t))
        d.line([0, y, W, y], fill=c)
    return im


def text(d, s, font, x, y, fill, anchor="l", stroke=0, sc=BLK):
    b = d.textbbox((0, 0), s, font=font, stroke_width=stroke)
    w = b[2] - b[0]
    X = x - b[0] if anchor == "l" else (x - w / 2 - b[0] if anchor == "c" else x - w - b[0])
    d.text((X, y - b[1]), s, font=font, fill=fill, stroke_width=stroke, stroke_fill=sc)
    return w, b[3] - b[1]


def fit(d, s, maxw, start=200, serif=False):
    size = start
    while size > 12 and d.textlength(s, font=F(size, serif)) > maxw:
        size -= 2
    return F(size, serif)


def pill(d, x, y, s, size, fill, fg=WHITE, outline=BLK, ow=6, pad=36, h=None):
    f = F(size)
    b = d.textbbox((0, 0), s, font=f)
    tw, th = b[2] - b[0], b[3] - b[1]
    h = h or int(size * 1.7)
    d.rounded_rectangle([x, y, x + tw + 2 * pad, y + h], radius=h // 4, fill=fill, outline=outline, width=ow)
    d.text((x + pad - b[0], y + h / 2 - th / 2 - b[1]), s, font=f, fill=fg)
    return tw + 2 * pad, h


def hl(d, x, y, s, size, fill=YEL, fg=(15, 15, 15), pad=20):
    f = F(size)
    b = d.textbbox((0, 0), s, font=f)
    tw, th = b[2] - b[0], b[3] - b[1]
    h = int(size * 1.45)
    d.rounded_rectangle([x - pad, y, x + tw + pad, y + h], radius=12, fill=fill)
    d.text((x - b[0], y + h / 2 - th / 2 - b[1]), s, font=f, fill=fg)
    return tw + 2 * pad, h


def down_arrow(d, cx, top, w=110, h=170, fill=RED):
    pts = [(cx - w / 2, top), (cx + w / 2, top), (cx + w / 2, top + h * 0.45), (cx + w, top + h * 0.45),
           (cx, top + h), (cx - w, top + h * 0.45), (cx - w / 2, top + h * 0.45)]
    d.polygon(pts, fill=fill)
    d.line(pts + [pts[0]], fill=BLK, width=7)


def check(d, cx, cy, r, fill=GRN):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill, outline=BLK, width=6)
    d.line([(cx - r * .5, cy + r * .02), (cx - r * .12, cy + r * .42), (cx + r * .55, cy - r * .38)],
           fill=WHITE, width=int(r * .28), joint="curve")


def cross(d, cx, cy, r, fill=RED):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill, outline=BLK, width=6)
    k = r * .45
    d.line([(cx - k, cy - k), (cx + k, cy + k)], fill=WHITE, width=int(r * .28))
    d.line([(cx - k, cy + k), (cx + k, cy - k)], fill=WHITE, width=int(r * .28))


def warn(d, cx, cy, s, fill=YEL):
    pts = [(cx, cy - s), (cx + s * 1.1, cy + s * .8), (cx - s * 1.1, cy + s * .8)]
    d.polygon(pts, fill=fill)
    d.line(pts + [pts[0]], fill=BLK, width=8, joint="curve")
    d.rounded_rectangle([cx - s * .09, cy - s * .35, cx + s * .09, cy + s * .25], radius=6, fill=BLK)
    d.ellipse([cx - s * .11, cy + s * .35, cx + s * .11, cy + s * .57], fill=BLK)


def cash_stack(d, cx, base, n=5, w0=360):
    for i in range(n):
        w = w0 - i * 34
        y = base - i * 62
        d.rounded_rectangle([cx - w / 2, y - 56, cx + w / 2, y], radius=10, fill=GRN_L, outline=(20, 60, 35), width=5)
        d.ellipse([cx - 26, y - 78 + 22, cx + 26, y - 34], outline=(20, 60, 35), width=5)
        text(d, "$", F(34), cx, y - 50, (20, 60, 35), "c")


def padlock(d, cx, cy, s, open_=False, fill=GOLD):
    d.rounded_rectangle([cx - s, cy - s * .1, cx + s, cy + s * 1.2], radius=int(s * .2), fill=fill, outline=BLK, width=7)
    sh = [cx - s * .6, cy - s * 1.15, cx + s * .6, cy + s * .35]
    if open_:
        sh = [cx + s * .1, cy - s * 1.35, cx + s * 1.3, cy + s * .15]
    d.arc(sh, 180, 360, fill=BLK, width=int(s * .28))
    if open_:
        d.line([(sh[0], cy - s * .55), (sh[0], cy - s * .1)], fill=BLK, width=int(s * .28))
    else:
        d.line([(cx - s * .6, cy - s * .4), (cx - s * .6, cy - s * .1)], fill=BLK, width=int(s * .28))
        d.line([(cx + s * .6, cy - s * .4), (cx + s * .6, cy - s * .1)], fill=BLK, width=int(s * .28))
    d.ellipse([cx - s * .16, cy + s * .3, cx + s * .16, cy + s * .62], fill=BLK)
    d.rectangle([cx - s * .06, cy + s * .5, cx + s * .06, cy + s * .95], fill=BLK)


def chart_cliff(d, x0, x1, ybase, ytop):
    pts = []
    for k in range(0, 61):
        t = k / 60
        pts.append((x0 + (x1 - x0) * t * .62, ybase - (ybase - ytop) * (t ** .7)))
    cx, cy = pts[-1]
    pts += [(cx + 8, cy), (cx + 30, ybase - 20)]
    pts += [(x1, ybase - 20)]
    d.line(pts, fill=RED, width=14, joint="curve")
    d.line([x0, ybase, x1, ybase], fill=NAVY, width=5)
    d.line([x0, ybase, x0, ytop - 20], fill=NAVY, width=5)
    return cx, cy


def save(im, name):
    im.save(f"{OUT}/{name}.png")
    print("ok", name)


# ---------------------------------------------------------------- TITOLO 1
def t1a():
    im = bg(); d = ImageDraw.Draw(im)
    text(d, "59½", F(300, True), 60, 20, NAVY, "l", stroke=0)
    text(d, "RULE", F(84), 70, 330, RED, "l")
    hl(d, 70, 430, "5 CHANGES", 80)
    text(d, "THAT COST THOUSANDS", F(50), 70, 560, NAVY, "l")
    pill(d, 60, 630, "#4 IS A TRAP", 46, RED, ow=5, h=70)
    cash_stack(d, 1010, 640, 5, 340)
    down_arrow(d, 1010, 80, 110, 200)
    return im


def t1b():
    im = bg(); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W // 2, H], fill=(214, 240, 224))
    d.rectangle([W // 2, 0, W, H], fill=(252, 220, 220))
    d.line([W // 2, 0, W // 2, H], fill=BLK, width=8)
    text(d, "59½", F(210, True), W // 2, 170, NAVY, "c", stroke=8, sc=WHITE)
    d.rounded_rectangle([W // 2 - 260, 24, W // 2 + 260, 96], radius=30, fill=WHITE, outline=BLK, width=5)
    text(d, "THE DAY YOU TURN", F(40), W // 2, 40, NAVY, "c")
    check(d, 320, 470, 70)
    text(d, "10% PENALTY", F(50), 320, 570, NAVY, "c")
    text(d, "GONE", F(76), 320, 625, GRN, "c")
    warn(d, 960, 460, 90)
    text(d, "#4 IS", F(50), 960, 570, NAVY, "c")
    text(d, "A TRAP", F(76), 960, 625, RED, "c")
    return im


def t1c():
    im = bg(); d = ImageDraw.Draw(im)
    text(d, "59½ RULE", F(70), 60, 40, NAVY, "l")
    text(d, "$10,000", F(190), 60, 130, RED, "l", stroke=0)
    text(d, "GONE... OR TRAPPED?", F(52), 66, 350, NAVY, "l")
    hl(d, 70, 450, "5 CHANGES", 76)
    pill(d, 60, 590, "#4 SHOCKS EVERYONE", 42, RED, ow=5, h=80)
    cx, cy = chart_cliff(d, 860, 1230, 600, 240)
    d.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=RED, outline=BLK, width=5)
    warn(d, cx + 10, cy - 105, 50)
    return im


# ---------------------------------------------------------------- TITOLO 2
def t2a():
    im = bg(); d = ImageDraw.Draw(im)
    text(d, "401(k)", F(140), 60, 30, NAVY, "l")
    text(d, "59½ RULE", F(110), 60, 190, RED, "l")
    hl(d, 70, 350, "5 CHANGES", 80)
    text(d, "YOU MUST CHECK", F(56), 66, 470, NAVY, "l")
    pill(d, 60, 570, "#4 IS A TRAP", 54, RED, ow=6, h=90)
    padlock(d, 1000, 330, 150, open_=True)
    text(d, "UNLOCKS AT 59½", F(44), 1000, 580, NAVY, "c")
    return im


def t2b():
    im = bg(); d = ImageDraw.Draw(im)
    text(d, "401k 59½ RULE", F(74), 60, 30, NAVY, "l")
    text(d, "CHECK THESE 5", F(100), 60, 130, RED, "l")
    items = [("10% penalty", True), ("In-service withdrawal", True), ("Roth 5-year rule", True), ("SEPP / 72(t) trap", False), ("Catch-up limit", True)]
    y = 310
    for name, ok in items:
        if ok:
            check(d, 100, y + 35, 32)
            text(d, name, F(46), 165, y + 8, NAVY, "l")
        else:
            cross(d, 100, y + 35, 32)
            hl(d, 165, y - 2, name.upper(), 46, fill=RED, fg=WHITE)
        y += 82
    warn(d, 1080, 330, 110)
    text(d, "#4", F(140), 1080, 430, RED, "c")
    text(d, "TRAPS", F(56), 1080, 590, NAVY, "c")
    text(d, "THOUSANDS", F(44), 1080, 650, NAVY, "c")
    return im


def t2c():
    im = bg("dark"); d = ImageDraw.Draw(im)
    text(d, "401k RULE", F(70), W // 2, 30, YEL, "c")
    text(d, "59½", F(360, True), W // 2, 80, WHITE, "c", stroke=8, sc=BLK)
    pill(d, 200, 560, "5 CHANGES", 50, YEL, fg=(15, 15, 15), h=90)
    pill(d, 690, 560, "#4 IS A TRAP", 50, RED, h=90)
    text(d, "YOU MUST CHECK", F(36), W // 2, 668, WHITE, "c")
    d.ellipse([40, 400, 180, 540], fill=YEL, outline=BLK, width=7)
    text(d, "$", F(110), 110, 415, (15, 15, 15), "c")
    d.ellipse([1100, 400, 1240, 540], fill=YEL, outline=BLK, width=7)
    text(d, "%", F(96), 1170, 420, RED, "c")
    return im


# ---------------------------------------------------------------- TITOLO 3
def t3a():
    im = bg(); d = ImageDraw.Draw(im)
    text(d, "RETIRE AT", F(90), 60, 30, NAVY, "l")
    text(d, "59½?", F(260, True), 60, 110, RED, "l")
    text(d, "THE 5 RULES", F(66), 66, 400, NAVY, "l")
    hl(d, 70, 490, "NOBODY WARNS YOU", 62)
    pill(d, 60, 620, "#4 TRAPS THOUSANDS", 40, RED, ow=5, h=70)
    for i in range(3):
        x = 900 + i * 110
        d.rounded_rectangle([x, 220 + i * 40, x + 90, 520], radius=8, fill=(120, 80, 40), outline=BLK, width=6)
        d.ellipse([x + 62, 380, x + 76, 394], fill=YEL)
    padlock(d, 1030, 130, 60)
    return im


def t3b():
    im = bg(); d = ImageDraw.Draw(im)
    text(d, "RETIRE AT 59½", F(80), W // 2, 25, NAVY, "c")
    text(d, "SAME AGE. DIFFERENT RESULT.", F(44), W // 2, 125, RED, "c")
    d.rounded_rectangle([60, 210, 610, 560], radius=24, fill=(252, 220, 220), outline=BLK, width=7)
    d.rounded_rectangle([670, 210, 1220, 560], radius=24, fill=(214, 240, 224), outline=BLK, width=7)
    text(d, "FRANK", F(70), 335, 230, NAVY, "c")
    text(d, "MARY", F(70), 945, 230, NAVY, "c")
    cross(d, 335, 400, 85)
    check(d, 945, 400, 85)
    text(d, "Thinks it is total freedom", F(30), 335, 510, NAVY, "c")
    text(d, "Checks all 5 rules", F(30), 945, 510, NAVY, "c")
    pill(d, 330, 600, "#4 TRAPS THOUSANDS", 48, RED, ow=6, h=80)
    return im


def t3c():
    im = bg(); d = ImageDraw.Draw(im)
    text(d, "5", F(430, True), 30, 10, RED, "l")
    text(d, "RULES", F(120), 360, 60, NAVY, "l")
    text(d, "AT 59½", F(120), 360, 200, NAVY, "l")
    hl(d, 370, 350, "NOBODY WARNS YOU", 50)
    text(d, "HOW TO RETIRE", F(56), 60, 570, NAVY, "l")
    pill(d, 60, 645, "#4 IS A TRAP", 40, RED, ow=5, h=62)
    cash_stack(d, 1090, 690, 4, 260)
    warn(d, 1090, 150, 90)
    return im


VARIANTS = {
    "T1-A-cash-arrow": t1a, "T1-B-split-verde-rosso": t1b, "T1-C-10000-grafico": t1c,
    "T2-A-lucchetto": t2a, "T2-B-checklist": t2b, "T2-C-scuro-59": t2c,
    "T3-A-porte": t3a, "T3-B-frank-vs-mary": t3b, "T3-C-5-regole": t3c,
}

if __name__ == "__main__":
    for n, f in VARIANTS.items():
        save(f(), n)
