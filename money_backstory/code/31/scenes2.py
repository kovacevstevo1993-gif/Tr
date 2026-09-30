import sys, math, random
sys.path.insert(0, "/home/claude/slides")
from eng2 import *

# =====================================================================
# SPRITE
# =====================================================================
def badge_spr(kind):
    def mk():
        c = Cv(190, 190)
        c.ell((6, 6, 184, 184), fill=CARD, outline=SAGE_D, width=5)
        c.ell((17, 17, 173, 173), outline=LINE, width=2)
        if kind == "food":
            for x in (58, 70, 82):
                c.rrect((x - 3, 44, x + 3, 86), 3, fill=IVORY)
            c.rrect((55, 80, 85, 94), 6, fill=IVORY)
            c.rrect((67, 90, 73, 146), 3, fill=IVORY)
            c.poly([(112, 44), (128, 52), (128, 106), (112, 106)], fill=IVORY)
            c.rrect((112, 102, 128, 146), 5, fill=IVORY)
        elif kind == "phone":
            c.rrect((66, 38, 124, 152), 14, outline=IVORY, width=6)
            c.rrect((86, 52, 104, 57), 2, fill=IVORY)
            c.ell((90, 130, 100, 140), fill=IVORY)
        elif kind == "ticket":
            c.rrect((40, 64, 150, 126), 8, fill=IVORY)
            c.ell((32, 87, 50, 105), fill=CARD)
            c.ell((140, 87, 158, 105), fill=CARD)
            for y in range(72, 122, 10):
                c.line([112, y, 112, y + 5], CARD, 3)
        else:
            c.poly([(38, 142), (80, 72), (104, 110), (124, 84), (154, 142)], fill=IVORY)
            c.poly([(80, 72), (69, 92), (80, 88), (91, 93)], fill=SAGE)
        return c.done()
    return cache(("badge", kind), mk)

def no_spr():
    def mk():
        c = Cv(250, 250)
        c.ell((12, 12, 238, 238), outline=CORAL, width=18)
        c.line([52, 52, 198, 198], CORAL, 18)
        return c.done()
    return cache("no", mk)

def burger_spr():
    def mk():
        c = Cv(640, 560)
        c.ell((30, 380, 610, 540), fill=IVORY)
        c.ell((30, 380, 610, 540), outline=(198, 190, 172), width=4)
        c.ell((90, 402, 550, 520), fill=(226, 220, 204))
        # panino sopra
        c.ell((140, 120, 500, 300), fill=GOLD)
        c.ell((190, 138, 310, 182), fill=(240, 205, 140))
        for (x, y) in [(230, 176), (300, 152), (372, 178), (424, 206), (262, 222), (340, 236), (196, 214), (452, 180)]:
            c.ell((x, y, x + 18, y + 10), fill=IVORY)
        # pomodoro e insalata
        c.rrect((150, 262, 490, 292), 12, fill=CORAL)
        for i in range(9):
            c.ell((140 + i * 41, 276, 190 + i * 41, 306), fill=SAGE)
        # hamburger
        c.rrect((135, 300, 505, 362), 28, fill=(74, 48, 36))
        # formaggio
        c.poly([(138, 302), (502, 302), (476, 350), (436, 322), (396, 356), (356, 322), (316, 354),
                (276, 322), (236, 350), (196, 322), (166, 346)], fill=(240, 208, 120))
        # panino sotto
        c.rrect((150, 350, 490, 420), 34, fill=GOLD)
        return c.done()
    return cache("burger", mk)

_steam_mask = {}
def steam(img, t, cx, cy, alpha=1.0):
    lay = Image.new("RGBA", (320, 260), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    for k in range(3):
        pts = []
        for j in range(40):
            y = 250 - j * 6
            x = 60 + k * 100 + math.sin(j * 0.35 - t * 3 + k * 1.7) * 14
            pts.append((x, y))
        d.line(pts, fill=(246, 241, 229, 255), width=8, joint="curve")
    if "m" not in _steam_mask:
        g = Image.new("L", (320, 260), 0)
        gd = ImageDraw.Draw(g)
        for y in range(260):
            gd.line([0, y, 320, y], fill=int(255 * (y / 260) ** 1.3))
        _steam_mask["m"] = g
    a = ImageChops.multiply(lay.getchannel("A"), _steam_mask["m"]).point(lambda v: int(v * 0.5 * alpha))
    lay.putalpha(a)
    put(img, lay, cx, cy)

def badge10_spr():
    def mk():
        c = Cv(340, 340)
        pts = []
        for i in range(32):
            ang = math.pi * 2 * i / 32 - math.pi / 2
            r = 160 if i % 2 == 0 else 140
            pts.append((170 + r * math.cos(ang), 170 + r * math.sin(ang)))
        c.poly(pts, fill=GOLD)
        c.ell((34, 34, 306, 306), outline=(190, 140, 60), width=4)
        c.text((170, 146), "10%", FONT_SANS, 106, DARK)
        c.text((170, 238), "OFF", FONT_SANS, 60, DARK, track=4)
        return c.done()
    return cache("b10", mk)

def age_spr():
    def mk():
        c = Cv(250, 250)
        c.ell((6, 6, 244, 244), fill=SAGE, outline=IVORY, width=7)
        c.text((125, 66), "AGE", FONT_SANS, 34, DARK, track=6)
        c.text((125, 136), "55+", FONT_SANS, 96, DARK)
        c.text((125, 200), "OR OLDER", FONT_SANS, 22, DARK, track=3)
        return c.done()
    return cache("age", mk)

# ---------------- scena 3
def phone_spr():
    def mk():
        c = Cv(340, 640)
        c.rrect((0, 0, 340, 640), 54, fill=(8, 22, 18), outline=SAGE_D, width=6)
        c.rrect((16, 16, 324, 624), 40, fill=CARD)
        c.rrect((122, 30, 218, 54), 12, fill=(5, 15, 12))
        for i in range(4):
            h = 12 + i * 9
            c.rrect((236 + i * 17, 90 - h, 246 + i * 17, 90), 3, fill=SAGE)
        c.text((58, 78), "5G", FONT_SANS, 28, SAGE, anchor="lm")
        c.rrect((50, 122, 290, 182), 30, fill=GOLD)
        c.text((170, 152), "SENIOR PLAN", FONT_SANS, 26, DARK, track=2)
        c.ell((70, 236, 270, 436), outline=SAGE, width=10)
        c.ell((86, 252, 254, 420), outline=LINE, width=3)
        c.text((170, 326), "55+", FONT_SERIF, 92, IVORY)
        c.text((170, 392), "YEARS", FONT_SANS, 26, SAGE, track=3)
        c.rrect((50, 480, 290, 520), 20, fill=DARK, outline=SAGE_D, width=3)
        c.rrect((56, 486, 214, 514), 14, fill=SAGE)
        c.text((170, 566), "SAVINGS", FONT_SANS, 26, SAGE, track=4)
        return c.done()
    return cache("phone", mk)

def waves(img, t, cx, cy):
    lay = Image.new("RGBA", (760, 420), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    for k in range(3):
        ph = ((t * 0.9) + k / 3) % 1
        r = 80 + ph * 220
        al = int(255 * (1 - ph) * 0.55)
        d.arc([380 - r, 400 - r, 380 + r, 400 + r], 215, 325, fill=(154, 200, 170, al), width=10)
    put(img, lay, cx, cy - 190)

def carrier_spr(name):
    def mk():
        c = Cv(820, 108)
        c.rrect((3, 3, 817, 105), 32, fill=CARD, outline=LINE, width=3)
        c.ell((18, 18, 90, 90), fill=(28, 74, 60))
        c.line([36, 55, 50, 69, 74, 39], SAGE, 8)
        c.text((118, 54), name, FONT_SANS, 52, IVORY, anchor="lm")
        c.rrect((668, 24, 796, 84), 30, fill=GOLD)
        c.text((732, 54), "55+", FONT_SANS, 42, DARK)
        return c.done()
    return cache(("car", name), mk)

def tag_spr(text, w=380, h=130, fill=GOLD, size=72):
    def mk():
        c = Cv(w, h)
        c.rrect((2, 2, w - 2, h - 2), 30, fill=fill)
        c.text((w / 2, h / 2), text, FONT_SANS, size, DARK)
        return c.done()
    return cache(("tag", text, w, h, fill, size), mk)

# ---------------- scena 4
def ticket_spr():
    def mk():
        c = Cv(780, 340)
        c.rrect((0, 0, 780, 340), 30, fill=IVORY)
        c.ell((-34, 136, 34, 204), fill=(0, 0, 0, 0))
        c.ell((746, 136, 814, 204), fill=(0, 0, 0, 0))
        c.ell((538, -22, 582, 22), fill=(0, 0, 0, 0))
        c.ell((538, 318, 582, 362), fill=(0, 0, 0, 0))
        for y in range(34, 310, 22):
            c.line([560, y, 560, y + 11], (170, 170, 158), 4)
        c.text((44, 120), "SENIOR", FONT_SANS, 108, DARK, anchor="lm")
        c.text((48, 214), "MOVIE TICKET", FONT_SANS, 46, (70, 110, 90), anchor="lm", track=3)
        c.text((48, 278), "ADMIT ONE", FONT_SANS, 30, (120, 140, 128), anchor="lm", track=5)
        c.text((670, 50), "AGE", FONT_SANS, 28, (120, 140, 128), track=6)
        return c.done()
    return cache("ticket", mk)

def stub_spr():
    def mk():
        c = Cv(220, 220)
        c.ell((6, 6, 214, 214), fill=GOLD, outline=(190, 140, 60), width=6)
        c.text((110, 112), "60+", FONT_SANS, 92, DARK)
        return c.done()
    return cache("stub", mk)

def bucket_spr():
    def mk():
        c = Cv(340, 440)
        rnd = random.Random(5)
        cols = [IVORY, (240, 226, 190), (232, 212, 160)]
        for i in range(28):
            x = rnd.uniform(46, 294)
            y = rnd.uniform(46, 132)
            r = rnd.uniform(22, 34)
            c.ell((x - r, y - r, x + r, y + r), fill=cols[i % 3])
        tl, tr, bl, br, yt, yb = 28, 312, 72, 268, 150, 430
        n = 6
        for i in range(n):
            xl0 = tl + (tr - tl) * i / n
            xl1 = tl + (tr - tl) * (i + 1) / n
            xb0 = bl + (br - bl) * i / n
            xb1 = bl + (br - bl) * (i + 1) / n
            c.poly([(xl0, yt), (xl1, yt), (xb1, yb), (xb0, yb)], fill=CORAL if i % 2 == 0 else IVORY)
        c.rrect((16, 138, 324, 176), 14, fill=IVORY, outline=(198, 190, 172), width=3)
        return c.done()
    return cache("bucket", mk)

def kernel_spr():
    def mk():
        c = Cv(56, 56)
        for (x, y, r) in [(20, 30, 14), (34, 30, 14), (27, 20, 14)]:
            c.ell((x - r + 4, y - r + 4, x + r + 4, y + r + 4), fill=(240, 226, 190))
        c.ell((13, 12, 28, 27), fill=IVORY)
        return c.done()
    return cache("kernel", mk)

def beam_spr():
    def mk():
        m = Image.new("L", (1080, 900), 0)
        d = ImageDraw.Draw(m)
        d.polygon([(100, 0), (260, 0), (800, 900), (420, 900)], fill=70)
        d.polygon([(980, 0), (820, 0), (280, 900), (660, 900)], fill=70)
        m = m.filter(ImageFilter.GaussianBlur(26))
        g = Image.new("L", (1080, 900), 0)
        gd = ImageDraw.Draw(g)
        for y in range(900):
            gd.line([0, y, 1080, y], fill=int(255 * (1 - y / 900)))
        m = ImageChops.multiply(m, g)
        im = Image.new("RGBA", (1080, 900), (246, 241, 229, 0))
        im.putalpha(m)
        return im
    return cache("beam", mk)

def arrow_spr():
    def mk():
        c = Cv(100, 130)
        c.rrect((34, 0, 66, 70), 6, fill=SAGE)
        c.poly([(0, 62), (100, 62), (50, 128)], fill=SAGE)
        return c.done()
    return cache("arrow", mk)

# ---------------- scena 5
def panel_mtn():
    def mk():
        c = Cv(900, 520)
        for y in range(520):
            k = y / 520
            col = (int(18 + 52 * k), int(70 + 60 * k), int(56 + 48 * k), 255)
            c.line([0, y, 900, y], col, 1.6)
        gl = Image.new("RGBA", c.im.size, (0, 0, 0, 0))
        ImageDraw.Draw(gl).ellipse([(640 - 160) * 2, (250 - 160) * 2, (640 + 160) * 2, (250 + 160) * 2],
                                   fill=(228, 179, 99, 120))
        gl = gl.filter(ImageFilter.GaussianBlur(44))
        c.im = Image.alpha_composite(c.im, gl)
        c.d = ImageDraw.Draw(c.im)
        c.ell((575, 185, 705, 315), fill=GOLD)
        c.poly([(0, 430), (170, 230), (300, 340), (470, 150), (640, 345), (760, 255), (900, 440), (900, 520), (0, 520)],
               fill=(36, 96, 76))
        c.poly([(470, 150), (428, 210), (455, 198), (472, 220), (492, 196), (516, 210)], fill=IVORY)
        c.poly([(170, 230), (140, 274), (162, 266), (172, 282), (188, 264), (206, 274)], fill=IVORY)
        c.poly([(0, 470), (160, 350), (330, 430), (520, 340), (700, 430), (900, 360), (900, 520), (0, 520)],
               fill=(24, 78, 60))

        def tree(x, base, h, col):
            w = h * 0.42
            c.poly([(x, base - h), (x - w * 0.6, base - h * 0.5), (x + w * 0.6, base - h * 0.5)], fill=col)
            c.poly([(x, base - h * 0.72), (x - w * 0.85, base - h * 0.2), (x + w * 0.85, base - h * 0.2)], fill=col)
            c.poly([(x, base - h * 0.45), (x - w, base), (x + w, base)], fill=col)
        for (x, h) in [(60, 190), (130, 150), (210, 210), (700, 170), (780, 210), (850, 160)]:
            tree(x, 520, h, (9, 46, 36))
        mask = Image.new("L", c.im.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, c.im.width - 1, c.im.height - 1], radius=80, fill=255)
        c.im.putalpha(ImageChops.multiply(c.im.getchannel("A"), mask))
        c.rrect((3, 3, 897, 517), 40, outline=SAGE_D, width=5)
        return c.done()
    return cache("mtn", mk)

def birds(img, t, cx, cy):
    d = ImageDraw.Draw(img)
    for k in range(3):
        x = ((t * 90 + k * 300) % 1100) - 100
        if not (60 < x < 840):
            continue
        y = 130 + k * 46 + math.sin(t * 3 + k) * 8
        amp = 11 * math.sin(t * 12 + k)
        ax, ay = cx - 450 + x, cy - 260 + y
        d.line([ax - 16, ay - amp, ax, ay, ax + 16, ay - amp], fill=IVORY, width=4, joint="curve")

def card_spr():
    def mk():
        c = Cv(700, 440)
        c.rrect((3, 3, 697, 437), 42, fill=GREEN_L, outline=GOLD, width=7)
        c.rrect((18, 18, 682, 422), 32, outline=LINE, width=2)
        c.poly([(410, 0), (470, 0), (300, 440), (240, 440)], fill=(255, 255, 255, 18))
        c.poly([(500, 0), (520, 0), (350, 440), (330, 440)], fill=(255, 255, 255, 14))
        c.text((44, 70), "SENIOR PASS", FONT_SANS, 44, IVORY, anchor="lm", track=5)
        c.line([44, 108, 330, 108], GOLD, 4)
        c.poly([(580, 96), (612, 44), (634, 74), (652, 56), (676, 96)], fill=IVORY)
        return c.done()
    return cache("card", mk)

def pill_life_spr():
    def mk():
        c = Cv(300, 64)
        c.rrect((0, 0, 300, 64), 32, fill=SAGE)
        c.text((28, 32), "LIFETIME", FONT_SANS, 32, DARK, anchor="lm", track=3)
        c.ell((226, 20, 254, 44), outline=DARK, width=5)
        c.ell((246, 20, 274, 44), outline=DARK, width=5)
        return c.done()
    return cache("life", mk)

def badge62_spr():
    def mk():
        c = Cv(200, 200)
        c.ell((6, 6, 194, 194), fill=IVORY, outline=GOLD, width=9)
        c.text((100, 58), "AGE", FONT_SANS, 28, (70, 110, 90), track=5)
        c.text((100, 118), "62+", FONT_SANS, 84, DARK)
        return c.done()
    return cache("b62", mk)

# ---------------- scena 6
def register_spr():
    def mk():
        c = Cv(520, 560)
        c.rrect((0, 330, 520, 560), 36, fill=CARD, outline=SAGE_D, width=5)
        c.rrect((22, 352, 498, 380), 12, fill=(28, 74, 60))
        c.rrect((60, 200, 460, 344), 26, fill=(30, 70, 60), outline=SAGE_D, width=5)
        c.rrect((110, 50, 410, 190), 24, fill=(8, 22, 18), outline=SAGE_D, width=5)
        c.rrect((126, 66, 394, 174), 14, fill=DARK)
        c.text((144, 94), "TOTAL", FONT_SANS, 24, SAGE_D, anchor="lm", track=3)
        c.text((378, 142), "$41.80", FONT_SANS, 56, SAGE, anchor="rm")
        for r in range(2):
            for k in range(5):
                x = 92 + k * 70
                y = 222 + r * 44
                c.rrect((x, y, x + 54, y + 32), 8, fill=LINE)
        c.rrect((92, 312, 428, 330), 8, fill=LINE)
        c.rrect((110, 410, 410, 490), 16, fill=(8, 22, 18), outline=SAGE_D, width=3)
        c.rrect((232, 440, 288, 460), 8, fill=SAGE_D)
        return c.done()
    return cache("reg", mk)

def stamp_spr(text):
    def mk():
        c = Cv(600, 130)
        c.rrect((4, 4, 596, 126), 20, outline=CORAL, width=9)
        c.text((300, 66), text, FONT_SANS, 58, CORAL, track=4)
        return c.done()
    return cache(("stamp", text), mk)

def subpill_spr():
    def mk():
        c = Cv(960, 100)
        c.rrect((3, 3, 957, 97), 46, fill=CARD, outline=SAGE_D, width=4)
        f = font(FONT_SANS, 52)
        d0 = ImageDraw.Draw(Image.new("L", (4, 4)))
        t1, t2, tr = "SUBSCRIBE", "PROGRAMS CHANGE AND DEADLINES PASS", 3
        w1 = sum(d0.textlength(ch, font=font(FONT_SANS, 26)) + tr for ch in t1) - tr
        w2 = sum(d0.textlength(ch, font=font(FONT_SANS, 26)) + tr for ch in t2) - tr
        gap = 56
        total = w1 + gap + w2
        x0 = 480 - total / 2
        c.text((x0, 50), t1, FONT_SANS, 26, IVORY, anchor="lm", track=tr)
        dx = x0 + w1 + gap / 2
        c.poly([(dx - 11, 50), (dx, 39), (dx + 11, 50), (dx, 61)], fill=SAGE)
        c.text((x0 + w1 + gap, 50), t2, FONT_SANS, 26, IVORY, anchor="lm", track=tr)
        return c.done()
    return cache("subpill", mk)

# =====================================================================
# SCENE
# =====================================================================
def sc1(img, t):
    ambient(img, t, "%$", n=8, seed=1)
    label(img, t, "SENIOR DISCOUNTS", 300, SAGE)
    s, al, a = pop(t, 0.10, 0.55)
    if a > 0:
        val = min(4, 1 + int(4 * ease(seg(t, 0.12, 0.6))))
        put(img, glow_spr(), 400, 650, alpha=0.30 * al)
        put(img, tspr(str(val), FONT_SERIF, 520, IVORY), 400, 650, scale=s, alpha=al, shadow=22)
        burst(img, t, 0.12, 400, 650, n=10, color=SAGE, dur=0.6, rad=300, seed=11)
        pl = seg(t, 0.35, 0.5)
        if pl > 0:
            put(img, tspr("PLACES", FONT_SANS, 84, SAGE), 735, 765 + 24 * (1 - ease(pl)), alpha=ease(pl))
    xs = [186, 422, 658, 894]
    for i, k in enumerate(["food", "phone", "ticket", "peak"]):
        s, al, a = pop(t, 0.85 + 0.22 * i, 0.5)
        if a > 0:
            put(img, badge_spr(k), xs[i], 1010 + 8 * math.sin(t * 3 + i), scale=s, alpha=al, shadow=12)
            burst(img, t, 0.85 + 0.22 * i, xs[i], 1010, n=6, color=GOLD, dur=0.5, rad=120, seed=20 + i)
    s, al, a = pop(t, 2.35, 0.45)
    if a > 0:
        put(img, bubble_spr(560, 190), 540, 1230, scale=s, alpha=al, shadow=14)
        if a >= 0.6:
            for k in range(3):
                dl = 0.35 + 0.65 * max(0.0, math.sin(t * 6 - k * 0.9))
                put(img, dot_spr(), 540 + (k - 1) * 64, 1208, alpha=dl)
    s, al, a = pop(t, 3.05, 0.4)
    if a > 0:
        put(img, no_spr(), 540, 1212, scale=s * 0.92, alpha=al)
    a = seg(t, 2.5, 0.5)
    if a > 0:
        put(img, tspr("AND NEVER SAY A WORD", FONT_SANS, 64, GOLD), 540, 1440 + 30 * (1 - ease(a)),
            alpha=ease(a), shadow=10)

def sc2(img, t):
    ambient(img, t, "%", n=7, seed=2)
    label(img, t, "PLACE NUMBER ONE", 300, SAGE)
    s, al, a = pop(t, 0.05, 0.6)
    if a > 0:
        put(img, glow_spr(), 540, 850, scale=1.5, alpha=0.22 * al)
        put(img, burger_spr(), 540, 850 + 8 * math.sin(t * 2.2), scale=s, alpha=al, shadow=18)
        if t > 0.6:
            steam(img, t, 540, 610, alpha=min(1.0, (t - 0.6) * 2))
    s, al, a = pop(t, 0.55, 0.45)
    if a > 0:
        put(img, panel_spr(720, 120, "CHILI'S", 68), 540, 1270, scale=s, alpha=al, shadow=14)
    s, al, a = pop(t, 1.45, 0.55)
    if a > 0:
        wob = 5 * math.sin((t - 1.45) * 5) * max(0.0, 1 - (t - 1.45) / 1.5)
        put(img, badge10_spr(), 810, 690, scale=s, alpha=al, rot=-8 + wob, shadow=16)
        burst(img, t, 1.45, 810, 690, n=12, color=GOLD, dur=0.7, rad=240, seed=4)
    s, al, a = pop(t, 2.55, 0.5)
    if a > 0:
        put(img, age_spr(), 260, 1040, scale=s, alpha=al, shadow=14)
        burst(img, t, 2.55, 260, 1040, n=10, color=SAGE, dur=0.7, rad=200, seed=5)

def sc3(img, t):
    ambient(img, t, "$%", n=8, seed=3)
    label(img, t, "PHONE PLANS", 300, SAGE)
    a = seg(t, 0.05, 0.6)
    if a > 0:
        waves(img, t, 540, 478)
        put(img, glow_spr(), 540, 780, scale=1.4, alpha=0.20 * ease(a))
        put(img, phone_spr(), 540, 780 + 6 * math.sin(t * 2), scale=max(ease_back(a), 0.01),
            alpha=min(1.0, a * 3), rot=5 * (1 - ease(a)), shadow=20)
    for i, (nm, t0) in enumerate([("AT&T", 0.75), ("T-Mobile", 1.95), ("Verizon", 3.05)]):
        a = seg(t, t0, 0.5)
        if a > 0:
            put(img, carrier_spr(nm), 540 - 680 * (1 - ease(a)), 1215 + i * 128, alpha=min(1.0, a * 3), shadow=10)
    s, al, a = pop(t, 4.25, 0.5)
    if a > 0:
        put(img, tag_spr("SENIOR PLANS", 430, 110, SAGE, 50), 300, 585, scale=s, alpha=al,
            rot=7 + 2 * math.sin(t * 4), shadow=12)
    s, al, a = pop(t, 5.35, 0.5)
    if a > 0:
        put(img, tag_spr("FROM 55"), 790, 540, scale=s, alpha=al, rot=-8 + 3 * math.sin((t - 5.35) * 6), shadow=14)
        burst(img, t, 5.35, 790, 540, n=12, color=GOLD, dur=0.7, rad=220, seed=7)

def sc4(img, t):
    ambient(img, t, "%$", n=7, seed=4)
    put(img, beam_spr(), 540, 560, alpha=0.55 + 0.25 * math.sin(t * 2))
    label(img, t, "MOVIE TICKETS", 300, SAGE)
    a = seg(t, 0.5, 0.6)
    tk_rot = 0.0
    if a > 0:
        tk_rot = -12 * (1 - ease(a)) + 1.5 * math.sin(t * 2.4) * ease(a)
        cy = 720 - 260 * (1 - ease(a))
        sp = ticket_spr()
        if a >= 1.0:
            sa = ((t - 1.3) % 2.6) / 1.5
            if sa <= 1.0:
                sp = shined(sp, sa)
        put(img, sp, 540, cy, rot=tk_rot, alpha=min(1.0, a * 3), shadow=20)
        s, al, b = pop(t, 2.85, 0.5)
        if b > 0:
            ox, oy = rot_off(280, 0, tk_rot)
            put(img, stub_spr(), 540 + ox, 720 + oy, scale=s, alpha=al, rot=tk_rot, shadow=10)
            burst(img, t, 2.85, 540 + ox, 720 + oy, n=12, color=GOLD, dur=0.7, rad=230, seed=9)
    a = seg(t, 1.05, 0.55)
    if a > 0:
        put(img, bucket_spr(), 300, 1150 + 320 * (1 - ease(a)), scale=1.0, alpha=min(1.0, a * 3),
            rot=2.5 * math.sin(t * 3), shadow=16)
    for i in range(10):
        t0 = 1.5 + 0.13 * i
        tau = t - t0
        if 0 < tau < 1.2:
            rnd = random.Random(40 + i)
            vx = rnd.uniform(-170, 170)
            vy = rnd.uniform(-820, -560)
            x = 300 + rnd.uniform(-50, 50) + vx * tau
            y = 960 + vy * tau + 0.5 * 1500 * tau * tau
            put(img, kernel_spr(), x, y, alpha=1 - tau / 1.2, rot=tau * rnd.uniform(-300, 300))
    s, al, a = pop(t, 1.85, 0.5)
    if a > 0:
        put(img, panel_spr(470, 220, "CHEAPER", 64, IVORY, GOLD, sub="TICKETS"), 740, 1140, scale=s, alpha=al, shadow=14)
        put(img, arrow_spr(), 740, 1330 + 12 * abs(math.sin(t * 6)), alpha=al)

def sc5(img, t):
    ambient(img, t, "$", n=7, seed=5)
    label(img, t, "NATIONAL PARKS", 300, SAGE)
    s, al, a = pop(t, 0.05, 0.6)
    if a > 0:
        put(img, panel_mtn(), 540, 760, scale=s, alpha=al, shadow=20)
        if a >= 0.99:
            birds(img, t, 540, 760)
    a = seg(t, 0.7, 0.7)
    if a > 0:
        cy = 1230 + 420 * (1 - ease(a))
        rot = -10 * (1 - ease(a))
        sp = card_spr()
        if a >= 1.0:
            sa = ((t - 1.6) % 2.8) / 1.5
            if sa <= 1.0:
                sp = shined(sp, sa)
        put(img, sp, 540, cy, alpha=min(1.0, a * 3), rot=rot, shadow=20)
    if t >= 1.5:
        v = int(80 * ease(seg(t, 2.2, 1.1)))
        s2 = min(1.0, 0.85 + 0.15 * ease(seg(t, 1.5, 0.3)))
        put(img, tspr("$" + str(v), FONT_SERIF, 180, GOLD), 540 - 350 + 240, 1230 - 6, scale=s2, shadow=8)
    s, al, a = pop(t, 3.4, 0.5)
    if a > 0:
        put(img, pill_life_spr(), 540 - 350 + 44 + 150, 1230 - 220 + 366, scale=s, alpha=al, shadow=8)
        burst(img, t, 3.4, 540 - 350 + 194, 1230 - 220 + 366, n=10, color=SAGE, dur=0.6, rad=180, seed=12)
    s, al, a = pop(t, 4.3, 0.5)
    if a > 0:
        put(img, badge62_spr(), 760, 1330, scale=s, alpha=al, rot=6 * math.sin((t - 4.3) * 5) * max(0.0, 1 - (t - 4.3) / 1.0),
            shadow=14)
        burst(img, t, 4.3, 760, 1330, n=12, color=GOLD, dur=0.7, rad=230, seed=13)

def sc6(img, t):
    ambient(img, t, "$%", n=8, seed=6)
    label(img, t, "THE CATCH", 300, GOLD)
    s, al, a = pop(t, 0.05, 0.6)
    if a > 0:
        put(img, register_spr(), 540, 780, scale=s, alpha=al, shadow=18)
    if t < 2.7:
        s, al, a = pop(t, 0.4, 0.45)
        if a > 0:
            put(img, bubble_spr(300, 140), 800, 540, scale=s, alpha=al, shadow=10)
            if a >= 0.6:
                for k in range(3):
                    dl = 0.35 + 0.65 * max(0.0, math.sin(t * 6 - k * 0.9))
                    put(img, dot_spr(), 800 + (k - 1) * 50, 518, alpha=dl)
    else:
        s, al, a = pop(t, 2.7, 0.45)
        put(img, bubble_spr(300, 140, GOLD, ["Sure!"], size=58), 800, 540, scale=s, alpha=al, shadow=10)
        burst(img, t, 2.7, 800, 520, n=10, color=GOLD, dur=0.6, rad=170, seed=14)
    s, al, a = pop(t, 0.95, 0.4)
    if a > 0 and t < 2.0:
        fade = 1.0 if t < 1.8 else max(0.0, (2.0 - t) / 0.2)
        put(img, stamp_spr("NOBODY OFFERS"), 540, 900, scale=s, alpha=al * fade, rot=-12)
    s, al, a = pop(t, 1.85, 0.5)
    if a > 0:
        put(img, bubble_spr(600, 200, IVORY, ["Any senior", "discount?"], size=52), 380, 1170,
            scale=s, alpha=al, shadow=14)
    s, al, a = pop(t, 2.25, 0.5)
    if a > 0:
        put(img, tspr("JUST ASK.", FONT_SANS, 124, GOLD), 540, 1400, scale=s, alpha=al, shadow=14)
        burst(img, t, 2.25, 540, 1400, n=14, color=GOLD, dur=0.7, rad=300, seed=15)
    a = seg(t, 2.9, 0.5)
    if a > 0:
        put(img, subpill_spr(), 540, 1520 + 30 * (1 - ease(a)), alpha=ease(a), shadow=10)

SCENES = {1: (sc1, 114), 2: (sc2, 105), 3: (sc3, 198), 4: (sc4, 124), 5: (sc5, 162), 6: (sc6, 108)}
