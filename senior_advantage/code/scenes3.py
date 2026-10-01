import sys, math, random
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from scenes2 import *

# =====================================================================
# SPRITE NUOVI
# =====================================================================
def door_spr():
    def mk():
        c = Cv(500, 670)
        c.rrect((0, 0, 500, 640), 34, fill=(9, 46, 36), outline=SAGE_D, width=6)
        c.rrect((34, 34, 466, 640), 22, fill=(28, 74, 60), outline=LINE, width=4)
        for (x, y) in [(70, 70), (262, 70), (70, 320), (262, 320)]:
            c.rrect((x, y, x + 168, y + 210), 14, outline=LINE, width=4)
        c.ell((392, 300, 434, 342), fill=GOLD)
        c.ell((400, 308, 418, 326), fill=(240, 205, 140))
        c.rrect((50, 636, 450, 668), 10, fill=(52, 104, 84))
        return c.done()
    return cache("m_door", mk)

def dome_spr():
    def mk():
        c = Cv(300, 190)
        c.ell((6, 30, 294, 320), fill=(214, 218, 212))
        c.ell((60, 56, 150, 100), fill=(238, 240, 236))
        c.d.rectangle([0, 160 * c.ss, 300 * c.ss, 190 * c.ss], fill=(0, 0, 0, 0))
        c.ell((132, 4, 168, 40), fill=(190, 196, 190))
        c.rrect((0, 152, 300, 174), 10, fill=(190, 196, 190))
        return c.done()
    return cache("m_dome", mk)

def plate_spr():
    def mk():
        c = Cv(300, 120)
        c.ell((0, 40, 300, 112), fill=IVORY, outline=(198, 190, 172), width=4)
        c.ell((34, 54, 266, 100), fill=(226, 220, 204))
        c.ell((80, 44, 176, 90), fill=(120, 78, 52))
        c.ell((92, 50, 150, 70), fill=(150, 104, 70))
        for (x, y) in [(184, 50), (206, 44), (226, 54)]:
            c.ell((x, y, x + 30, y + 30), fill=SAGE)
        for (x, y) in [(58, 64), (72, 76)]:
            c.ell((x, y, x + 24, y + 14), fill=GOLD)
        return c.done()
    return cache("m_plate", mk)

def van_spr():
    def mk():
        c = Cv(560, 300)
        c.rrect((8, 30, 400, 230), 26, fill=IVORY)
        c.rrect((8, 150, 400, 182), 6, fill=GOLD)
        c.text((204, 92), "MEALS ON WHEELS", FONT_SANS, 32, DARK, track=2)
        c.poly([(388, 78), (476, 78), (548, 150), (548, 232), (388, 232)], fill=(226, 220, 204))
        c.poly([(408, 96), (466, 96), (518, 148), (408, 148)], fill=SAGE)
        c.rrect((520, 194, 552, 212), 6, fill=GOLD)
        c.rrect((8, 224, 548, 240), 6, fill=(150, 160, 152))
        return c.done()
    return cache("m_van", mk)

def wheel_spr():
    def mk():
        c = Cv(120, 120)
        c.ell((0, 0, 120, 120), fill=(7, 20, 16))
        c.ell((22, 22, 98, 98), fill=(160, 170, 162))
        for a in range(0, 180, 45):
            r = math.radians(a)
            c.line([60 - 38 * math.cos(r), 60 - 38 * math.sin(r), 60 + 38 * math.cos(r), 60 + 38 * math.sin(r)],
                   (90, 100, 92), 6)
        c.ell((46, 46, 74, 74), fill=(60, 70, 62))
        return c.done()
    return cache("m_wheel", mk)

def paystub_spr():
    def mk():
        c = Cv(420, 300)
        c.rrect((0, 0, 420, 300), 16, fill=IVORY)
        c.rrect((0, 0, 420, 72), 16, fill=SAGE)
        c.d.rectangle([0, 44 * c.ss, 420 * c.ss, 72 * c.ss], fill=SAGE)
        c.text((30, 38), "YOUR INCOME", FONT_SANS, 32, DARK, anchor="lm", track=3)
        for i in range(3):
            c.rrect((30, 104 + i * 34, 310 - i * 44, 120 + i * 34), 6, fill=(198, 196, 186))
        c.text((210, 250), "$  $  $", FONT_SANS, 62, (70, 110, 90))
        return c.done()
    return cache("m_stub", mk)

def invoice_spr():
    def mk():
        c = Cv(440, 540)
        c.rrect((0, 0, 440, 540), 16, fill=IVORY)
        c.text((220, 72), "BILL", FONT_SANS, 84, DARK, track=6)
        c.line([40, 124, 400, 124], (170, 170, 158), 4)
        for i in range(5):
            c.rrect((40, 154 + i * 46, 40 + 340 - (i % 3) * 56, 170 + i * 46), 6, fill=(198, 196, 186))
        c.line([40, 404, 400, 404], (170, 170, 158), 4)
        c.text((40, 458), "TOTAL", FONT_SANS, 40, (70, 110, 90), anchor="lm", track=3)
        c.text((400, 458), "$$$", FONT_SANS, 64, CORAL, anchor="rm")
        return c.done()
    return cache("m_invoice", mk)

def bigx_spr():
    def mk():
        c = Cv(400, 400)
        c.line([40, 40, 360, 360], CORAL, 46)
        c.line([360, 40, 40, 360], CORAL, 46)
        return c.done()
    return cache("m_bigx", mk)

def jar_spr():
    def mk():
        c = Cv(400, 540)
        c.rrect((40, 100, 360, 520), 80, fill=(154, 200, 170, 55), outline=(154, 200, 170), width=6)
        c.rrect((78, 44, 322, 112), 20, fill=GOLD, outline=(190, 140, 60), width=5)
        c.rrect((140, 68, 260, 84), 8, fill=DARK)
        c.rrect((92, 290, 308, 414), 18, fill=IVORY)
        c.text((200, 340), "DONATION", FONT_SANS, 44, DARK)
        c.text((200, 384), "PER MEAL", FONT_SANS, 26, (70, 110, 90), track=5)
        return c.done()
    return cache("m_jar", mk)

def coin_spr():
    def mk():
        c = Cv(72, 72)
        c.ell((2, 2, 70, 70), fill=GOLD, outline=(190, 140, 60), width=4)
        c.ell((12, 12, 60, 60), outline=(190, 140, 60), width=2)
        c.text((36, 37), "$", FONT_SANS, 38, (150, 100, 30))
        return c.done()
    return cache("m_coin", mk)

def house_spr():
    def mk():
        c = Cv(440, 380)
        c.rrect((332, 34, 384, 150), 4, fill=(52, 104, 84))
        c.poly([(6, 166), (220, 14), (434, 166)], fill=(52, 104, 84))
        c.rrect((50, 156, 390, 372), 18, fill=(28, 74, 60), outline=LINE, width=4)
        c.rrect((186, 232, 262, 372), 10, fill=GOLD)
        c.ell((246, 300, 256, 310), fill=(190, 140, 60))
        for x in (80, 300):
            c.rrect((x, 200, x + 70, 264), 8, fill=(232, 200, 130))
            c.line([x + 35, 200, x + 35, 264], DARK, 3)
            c.line([x, 232, x + 70, 232], DARK, 3)
        return c.done()
    return cache("m_house", mk)

def bag_spr():
    def mk():
        c = Cv(96, 124)
        c.arc((26, 4, 70, 56), 180, 360, (190, 140, 60), 6)
        c.rrect((6, 32, 90, 118), 12, fill=(232, 200, 130), outline=(190, 140, 60), width=3)
        c.rrect((6, 32, 90, 50), 8, fill=(214, 180, 110))
        c.ell((34, 66, 62, 94), fill=CORAL)
        return c.done()
    return cache("m_bag", mk)

def icon_badge(kind):
    def mk():
        c = Cv(190, 190)
        c.ell((6, 6, 184, 184), fill=CARD, outline=SAGE_D, width=5)
        c.ell((17, 17, 173, 173), outline=LINE, width=2)
        if kind == "pan":
            c.ell((30, 56, 126, 152), fill=(40, 44, 42), outline=IVORY, width=7)
            c.ell((50, 76, 108, 134), fill=(26, 28, 27))
            c.rrect((122, 98, 176, 114), 7, fill=IVORY)
        else:
            c.rrect((30, 98, 160, 134), 14, fill=IVORY)
            c.poly([(56, 98), (76, 66), (120, 66), (142, 98)], fill=IVORY)
            c.poly([(82, 72), (96, 72), (96, 96), (68, 96)], fill=(154, 200, 170))
            c.poly([(104, 72), (116, 72), (130, 96), (104, 96)], fill=(154, 200, 170))
            c.ell((50, 118, 82, 150), fill=DARK, outline=IVORY, width=4)
            c.ell((108, 118, 140, 150), fill=DARK, outline=IVORY, width=4)
        return c.done()
    return cache(("ib", kind), mk)

def center_spr():
    def mk():
        c = Cv(760, 520)
        c.poly([(40, 196), (380, 30), (720, 196)], fill=(52, 104, 84))
        c.rrect((70, 190, 690, 490), 18, fill=(28, 74, 60), outline=LINE, width=4)
        c.rrect((190, 112, 570, 172), 12, fill=DARK, outline=SAGE_D, width=3)
        c.text((380, 143), "SENIOR CENTER", FONT_SANS, 34, IVORY, track=4)
        for x in (110, 530):
            c.rrect((x, 240, x + 120, 410), 50, fill=(232, 200, 130))
            c.line([x + 60, 240, x + 60, 410], DARK, 4)
            c.line([x, 325, x + 120, 325], DARK, 4)
        c.rrect((328, 300, 432, 490), 34, fill=GOLD)
        c.rrect((300, 490, 460, 512), 8, fill=(52, 104, 84))
        return c.done()
    return cache("m_center", mk)

def table_spr():
    def mk():
        c = Cv(600, 240)
        c.rrect((10, 96, 590, 130), 12, fill=(150, 110, 70))
        c.rrect((60, 126, 84, 232), 6, fill=(120, 86, 54))
        c.rrect((516, 126, 540, 232), 6, fill=(120, 86, 54))
        for x in (120, 300, 480):
            c.ell((x - 70, 64, x + 70, 110), fill=IVORY, outline=(198, 190, 172), width=3)
            c.ell((x - 46, 72, x + 46, 100), fill=(226, 220, 204))
            c.ell((x - 24, 68, x + 20, 92), fill=(120, 78, 52))
            c.ell((x + 16, 66, x + 42, 88), fill=SAGE)
        return c.done()
    return cache("m_table", mk)

def map_spr():
    def mk():
        c = Cv(820, 380)
        c.rrect((0, 0, 820, 380), 38, fill=(16, 66, 52))
        rnd = random.Random(3)
        for _ in range(15):
            x = rnd.randint(20, 720)
            y = rnd.randint(20, 300)
            c.rrect((x, y, x + rnd.randint(60, 110), y + rnd.randint(40, 80)), 10, fill=(22, 82, 64))
        for pts in [[0, 120, 820, 160], [0, 260, 820, 230], [200, 0, 240, 380], [560, 0, 520, 380], [0, 320, 820, 70]]:
            c.line(pts, (40, 100, 80), 14)
        mask = Image.new("L", c.im.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, c.im.width - 1, c.im.height - 1], radius=76, fill=255)
        c.im.putalpha(ImageChops.multiply(c.im.getchannel("A"), mask))
        c.rrect((3, 3, 817, 377), 38, outline=SAGE_D, width=5)
        return c.done()
    return cache("m_map", mk)

def pin_spr(color):
    def mk():
        c = Cv(90, 120)
        c.poly([(10, 46), (80, 46), (45, 116)], fill=color)
        c.ell((4, 2, 86, 84), fill=color)
        c.ell((28, 26, 62, 60), fill=DARK)
        return c.done()
    return cache(("pin", color), mk)

def handset_spr():
    def mk():
        h = Cv(240, 240)
        h.rrect((46, 92, 194, 130), 18, fill=DARK)
        h.rrect((42, 92, 90, 172), 16, fill=DARK)
        h.rrect((150, 92, 198, 172), 16, fill=DARK)
        hs = h.done().rotate(32, resample=Image.BICUBIC)
        b = Cv(240, 240)
        b.ell((6, 6, 234, 234), fill=GOLD, outline=(190, 140, 60), width=7)
        base = b.done()
        return Image.alpha_composite(base, hs)
    return cache("m_handset", mk)

def rings(img, t, cx, cy):
    lay = Image.new("RGBA", (700, 700), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    for k in range(3):
        ph = ((t * 0.9) + k / 3) % 1
        r = 130 + ph * 200
        al = int(255 * (1 - ph) * 0.6)
        d.ellipse([350 - r, 350 - r, 350 + r, 350 + r], outline=(246, 241, 229, al), width=8)
    put(img, lay, cx, cy)

def locator_panel_spr():
    def mk():
        c = Cv(900, 150)
        c.rrect((3, 3, 897, 147), 40, fill=CARD, outline=GOLD, width=5)
        c.text((450, 62), "ELDERCARE LOCATOR", FONT_SANS, 54, IVORY, track=3)
        c.text((450, 114), "A U.S. GOVERNMENT SERVICE", FONT_SANS, 26, SAGE, track=4)
        return c.done()
    return cache("m_locpanel", mk)

def numpanel_spr():
    def mk():
        c = Cv(980, 200)
        c.rrect((4, 4, 976, 196), 46, fill=CARD, outline=GOLD, width=6)
        return c.done()
    return cache("m_numpanel", mk)

NUM_TXT = "1-800-677-1116"
def num_bounds():
    d0 = ImageDraw.Draw(Image.new("L", (4, 4)))
    f = font(FONT_SANS, 104, True)
    pad = int(104 * 0.35)
    b1 = pad + d0.textlength("1-800-", font=f)
    b2 = pad + d0.textlength("1-800-677-", font=f)
    return pad, b1, b2

def free_spr():
    def mk():
        c = Cv(360, 360)
        pts = []
        for i in range(32):
            ang = math.pi * 2 * i / 32 - math.pi / 2
            r = 170 if i % 2 == 0 else 148
            pts.append((180 + r * math.cos(ang), 180 + r * math.sin(ang)))
        c.poly(pts, fill=GOLD)
        c.ell((36, 36, 324, 324), outline=(190, 140, 60), width=4)
        c.text((180, 176), "FREE", FONT_SANS, 112, DARK)
        return c.done()
    return cache("m_free", mk)

def office_spr():
    def mk():
        c = Cv(300, 340)
        c.poly([(10, 110), (150, 24), (290, 110)], fill=(52, 104, 84))
        c.rrect((30, 100, 270, 330), 16, fill=(28, 74, 60), outline=LINE, width=4)
        c.rrect((118, 226, 182, 330), 12, fill=GOLD)
        for (x, y) in [(52, 130), (170, 130), (52, 200), (200, 200)]:
            c.rrect((x, y, x + 58, y + 50), 8, fill=(232, 200, 130))
        return c.done()
    return cache("m_office", mk)

def plane_spr():
    def mk():
        c = Cv(170, 130)
        c.poly([(4, 62), (166, 6), (86, 88)], fill=IVORY)
        c.poly([(86, 88), (166, 6), (112, 122)], fill=(214, 208, 194))
        c.poly([(86, 88), (70, 124), (112, 122)], fill=(190, 184, 170))
        return c.done()
    return cache("m_plane", mk)

def heart_spr():
    def mk():
        c = Cv(120, 110)
        c.ell((6, 8, 66, 68), fill=CORAL)
        c.ell((54, 8, 114, 68), fill=CORAL)
        c.poly([(10, 50), (110, 50), (60, 104)], fill=CORAL)
        return c.done()
    return cache("m_heart", mk)

# =====================================================================
# SCENE
# =====================================================================
def m1(img, t):
    ambient(img, t, "%$", n=8, seed=21)
    label(img, t, "MEALS FOR SENIORS", 300, SAGE)
    a = seg(t, 0.1, 0.4)
    if a > 0:
        put(img, tspr("OVER", FONT_SANS, 64, SAGE, track=12), 540, 455, alpha=ease(a))
    s, al, a = pop(t, 0.15, 0.55)
    if a > 0:
        put(img, glow_spr(), 540, 650, scale=1.1, alpha=0.30 * al)
        put(img, tspr("60+", FONT_SERIF, 400, IVORY), 540, 650, scale=s, alpha=al, shadow=20)
        burst(img, t, 0.15, 540, 650, n=10, color=SAGE, dur=0.6, rad=300, seed=31)
    a = seg(t, 1.0, 0.5)
    if a > 0:
        put(img, door_spr(), 540, 1090 + 160 * (1 - ease(a)), scale=0.8, alpha=min(1.0, a * 3), shadow=16)
    a = seg(t, 1.5, 0.5)
    if a > 0:
        lift = ease(seg(t, 2.5, 0.5))
        yy = 1320 - 320 * (1 - ease_back(a))
        put(img, plate_spr(), 540, yy + 30, alpha=min(1.0, a * 3), shadow=10)
        put(img, dome_spr(), 540, yy - 36 - 100 * lift, rot=10 * lift, alpha=min(1.0, a * 3), shadow=10)
        if lift > 0.2:
            steam(img, t, 540, yy - 120, alpha=min(1.0, lift))
        burst(img, t, 1.9, 540, 1320, n=8, color=GOLD, dur=0.5, rad=170, seed=32)
    a = seg(t, 2.6, 0.5)
    if a > 0:
        put(img, tspr("DELIVERED TO YOUR DOOR", FONT_SANS, 58, GOLD), 540, 1500 + 30 * (1 - ease(a)),
            alpha=ease(a), shadow=8)

def m2(img, t):
    ambient(img, t, "%", n=7, seed=22)
    label(img, t, "MEALS ON WHEELS", 300, SAGE)
    a = seg(t, 0.0, 1.1)
    sc = 1.35
    vx = -480 + (540 + 480) * ease(a)
    vy = 740 + 4 * math.sin(t * 16) * (1.0 if a < 1 else 0.4)
    if a < 1.0:
        d = ImageDraw.Draw(img)
        for k in range(5):
            d.line([vx - 470 - k * 20, vy - 90 + k * 46, vx - 380, vy - 90 + k * 46], fill=(60, 122, 100), width=7)
    put(img, van_spr(), vx, vy, scale=sc, shadow=14)
    for dx in (-170, 160):
        put(img, wheel_spr(), vx + dx * sc, vy + 100 * sc, scale=sc, rot=-(t * 540) % 360)
    a = seg(t, 2.3, 0.55)
    if a > 0:
        put(img, paystub_spr(), 540, 1215 + 80 * (1 - ease(a)), alpha=min(1.0, a * 3), shadow=14,
            rot=-3 * (1 - ease(a)))
    s, al, a = pop(t, 3.3, 0.45)
    if a > 0:
        put(img, no_spr(), 540, 1215, scale=s * 0.95, alpha=al)
    a = seg(t, 2.6, 0.5)
    if a > 0:
        put(img, tspr("IN MANY PROGRAMS", FONT_SANS, 42, SAGE, track=6), 540, 1440, alpha=ease(a))
    a = seg(t, 3.6, 0.5)
    if a > 0:
        put(img, tspr("INCOME DOESN'T DECIDE", FONT_SANS, 56, GOLD), 540, 1510 + 24 * (1 - ease(a)),
            alpha=ease(a), shadow=8)

def m3(img, t):
    ambient(img, t, "$", n=8, seed=23)
    label(img, t, "THE COST", 300, GOLD)
    a = seg(t, 0.1, 0.5)
    out = ease(seg(t, 1.8, 0.5))
    if a > 0 and out < 1:
        ix = 540 + 600 * (1 - ease(a)) - 700 * out
        rot = -4 * (1 - ease(a)) + 8 * out
        put(img, invoice_spr(), ix, 730 + 40 * out, alpha=(1 - out) * min(1.0, a * 3), rot=rot, shadow=16)
        s, al, b = pop(t, 0.95, 0.4)
        if b > 0:
            put(img, bigx_spr(), ix, 730 + 40 * out, scale=s * 0.95, alpha=al * (1 - out), rot=rot)
    s, al, a = pop(t, 1.8, 0.5)
    if a > 0:
        put(img, jar_spr(), 540, 1090, scale=s, alpha=al, shadow=16)
    s, al, a = pop(t, 2.0, 0.4)
    if a > 0:
        put(img, tag_spr("SUGGESTED", 400, 84, SAGE, 42), 540, 760, scale=s, alpha=al, shadow=8)
    if t > 2.0:
        n_in = 0
        for i in range(5):
            t0 = 2.1 + 0.42 * i
            u = (t - t0) / 0.5
            if 0 < u < 1:
                put(img, coin_spr(), 540 + (i - 2) * 9, 620 + 276 * (u * u), rot=u * 240)
            if u >= 1:
                n_in += 1
        for k, (px, py) in enumerate([(-70, 0), (0, 6), (70, 0), (-35, -28), (35, -28)][:n_in]):
            put(img, coin_spr(), 540 + px, 1298 + py, scale=0.95)
    a = seg(t, 3.3, 0.5)
    if a > 0:
        put(img, tspr("A FEW DOLLARS A MEAL", FONT_SANS, 60, GOLD), 540, 1500 + 24 * (1 - ease(a)),
            alpha=ease(a), shadow=8)

def m4(img, t):
    ambient(img, t, "%$", n=8, seed=24)
    cut = 3.95
    shift = -1300 * ease(seg(t, cut, 0.45))
    if t < cut + 0.5:
        if t < cut:
            label(img, t, "HOME DELIVERY", 300, SAGE)
        s, al, a = pop(t, 0.05, 0.5)
        if a > 0:
            put(img, house_spr(), 540 + shift, 690, scale=s, alpha=al, shadow=16)
        a = seg(t, 0.5, 0.5)
        if a > 0:
            put(img, bag_spr(), 610 + shift, 862 - 260 * (1 - ease_back(a)), alpha=min(1.0, a * 3), shadow=8)
        a = seg(t, 1.3, 0.5)
        if a > 0:
            put(img, tspr("OFTEN FOR PEOPLE WHO", FONT_SANS, 46, SAGE, track=4), 540 + shift, 1010, alpha=ease(a))
        for (x, kind, txt, t0) in [(330, "pan", "CAN'T COOK", 2.3), (750, "car", "CAN'T DRIVE", 3.0)]:
            s, al, a = pop(t, t0, 0.45)
            if a > 0:
                put(img, icon_badge(kind), x + shift, 1170, scale=s, alpha=al, shadow=12)
                put(img, tspr(txt, FONT_SANS, 40, IVORY, track=3), x + shift, 1320, alpha=al)
            s2, al2, a2 = pop(t, t0 + 0.55, 0.35)
            if a2 > 0:
                put(img, no_spr(), x + shift, 1170, scale=s2 * 0.72, alpha=al2)
    if t >= cut:
        label(img, t, "SENIOR CENTERS", 300, SAGE, t0=cut + 0.1)
        a = seg(t, cut + 0.15, 0.55)
        if a > 0:
            put(img, center_spr(), 540 + 900 * (1 - ease(a)), 720, scale=0.85, alpha=min(1.0, a * 3), shadow=16)
        a = seg(t, cut + 0.5, 0.5)
        if a > 0:
            put(img, table_spr(), 540, 1130 + 50 * (1 - ease(a)), scale=0.95, alpha=min(1.0, a * 3), shadow=12)
            if a >= 0.9:
                for dx in (-171, 0, 171):
                    steam(img, t + dx, 540 + dx, 1030, alpha=0.8)
        a = seg(t, cut + 0.7, 0.5)
        if a > 0:
            put(img, tspr("SERVE MEALS TOO", FONT_SANS, 80, GOLD), 540, 1380 + 24 * (1 - ease(a)),
                alpha=ease(a), shadow=8)
        a = seg(t, cut + 1.2, 0.5)
        if a > 0:
            put(img, tspr("RULES VARY BY AREA", FONT_SANS, 38, SAGE, track=5), 540, 1490, alpha=ease(a))

def m5(img, t):
    ambient(img, t, "$%", n=8, seed=25)
    label(img, t, "FIND YOURS", 300, SAGE)
    s, al, a = pop(t, 0.0, 0.5)
    if a > 0:
        put(img, map_spr(), 540, 690, scale=s, alpha=al, shadow=16)
    for (px, py, col, t0) in [(-250, -60, GOLD, 0.3), (60, 50, SAGE, 0.6), (280, -40, IVORY, 0.9)]:
        a = seg(t, t0, 0.45)
        if a > 0:
            put(img, pin_spr(col), 540 + px, 690 + py - 60 - 220 * (1 - ease_back(a)), alpha=min(1.0, a * 3))
    s, al, a = pop(t, 1.1, 0.5)
    if a > 0:
        rings(img, t - 1.1, 540, 690)
        put(img, handset_spr(), 540, 690, scale=s, alpha=al, rot=5 * math.sin((t - 1.1) * 13), shadow=14)
    s, al, a = pop(t, 1.4, 0.5)
    if a > 0:
        put(img, locator_panel_spr(), 540, 1010, scale=s, alpha=al, shadow=14)
    s, al, a = pop(t, 2.8, 0.45)
    if a > 0:
        put(img, numpanel_spr(), 540, 1260, scale=s, alpha=al, shadow=14)
    pad, b1, b2 = num_bounds()
    sp = tspr(NUM_TXT, FONT_SANS, 104, GOLD)
    w, h = sp.size
    if t < 3.1:
        upto = 0
    elif t < 4.3:
        upto = pad + (b1 - pad) * ease(seg(t, 3.1, 0.5))
    elif t < 5.3:
        upto = b1 + (b2 - b1) * ease(seg(t, 4.3, 0.4))
    else:
        upto = b2 + (w - b2) * ease(seg(t, 5.3, 0.6))
    if upto > 2:
        crop = sp.crop((0, 0, int(upto), h))
        img.paste(crop, (int(540 - w / 2), int(1260 - h / 2)), crop)
    a = seg(t, 5.6, 0.5)
    if a > 0:
        put(img, tspr("eldercare.acl.gov", FONT_SANS, 46, SAGE, track=2), 540, 1430, alpha=ease(a))

def m6(img, t):
    ambient(img, t, "$%", n=8, seed=26)
    cut = 3.85
    shift = -1300 * ease(seg(t, cut, 0.45))
    if t < cut + 0.5:
        if t < cut:
            label(img, t, "IT IS FREE", 300, GOLD)
        s, al, a = pop(t, 0.2, 0.55)
        if a > 0:
            put(img, glow_spr(), 540 + shift, 660, scale=1.3, alpha=0.25 * al)
            put(img, free_spr(), 540 + shift, 660, scale=s * 1.15, alpha=al, rot=-6 + 3 * math.sin(t * 4), shadow=16)
            burst(img, t, 0.2, 540, 660, n=14, color=GOLD, dur=0.7, rad=340, seed=41)
        s, al, a = pop(t, 1.3, 0.45)
        if a > 0:
            put(img, badge_spr("phone"), 200 + shift, 1120, scale=s, alpha=al, shadow=12)
            put(img, tspr("YOU", FONT_SANS, 40, SAGE, track=6), 200 + shift, 1250, alpha=al)
        prog = seg(t, 1.6, 0.9)
        if prog > 0:
            for k in range(14):
                if k / 14.0 <= ease(prog):
                    put(img, dot_spr(SAGE, 9), 330 + k * 34 + shift, 1120)
        if prog >= 1.0:
            u = ((t - 2.5) * 0.9) % 1.0
            put(img, coin_spr(), 330 + 13 * 34 * u + shift, 1120, scale=0.8)
        s, al, a = pop(t, 2.3, 0.5)
        if a > 0:
            put(img, office_spr(), 850 + shift, 1120, scale=s * 0.95, alpha=al, shadow=12)
            put(img, pin_spr(GOLD), 850 + shift, 890 + 8 * math.sin(t * 5) - 200 * (1 - ease_back(a)), alpha=al)
            put(img, tspr("NEAR YOU", FONT_SANS, 46, GOLD, track=3), 850 + shift, 1330, alpha=al)
    if t >= cut:
        label(img, t, "SHARE IT", 300, SAGE, t0=cut + 0.1)
        a = seg(t, cut + 0.1, 0.55)
        if a > 0:
            put(img, house_spr(), 540 + 900 * (1 - ease(a)), 730, scale=1.05, alpha=min(1.0, a * 3), shadow=16)
        e = seg(t, cut + 0.25, 1.0)
        if 0 < e < 1.0:
            for k in range(1, 6):
                ee = max(0.0, e - k * 0.045)
                px = 140 + 330 * ease(ee)
                py = 1160 - 280 * ease(ee) - 90 * math.sin(math.pi * ease(ee))
                put(img, dot_spr(IVORY, 6), px, py, alpha=0.6 * (1 - k / 6.0))
            px = 140 + 330 * ease(e)
            py = 1160 - 280 * ease(e) - 90 * math.sin(math.pi * ease(e))
            put(img, plane_spr(), px, py, rot=-24, shadow=8)
        s, al, a = pop(t, cut + 1.3, 0.45)
        if a > 0:
            put(img, heart_spr(), 540, 520 - 8 * math.sin(t * 6), scale=s, alpha=al)
            burst(img, t, cut + 1.3, 540, 540, n=10, color=CORAL, dur=0.6, rad=200, seed=42)
        a = seg(t, cut + 0.45, 0.5)
        if a > 0:
            put(img, tspr("SEND THIS", FONT_SANS, 118, GOLD), 540, 1200 + 24 * (1 - ease(a)), alpha=ease(a), shadow=10)
        a = seg(t, cut + 0.65, 0.5)
        if a > 0:
            put(img, tspr("TO SOMEONE", FONT_SANS, 70, IVORY), 540, 1305, alpha=ease(a))
        a = seg(t, cut + 0.85, 0.5)
        if a > 0:
            put(img, tspr("WHO LIVES ALONE", FONT_SANS, 70, IVORY), 540, 1385, alpha=ease(a))
        a = seg(t, cut + 1.4, 0.5)
        if a > 0:
            put(img, subpill_spr(), 540, 1510 + 20 * (1 - ease(a)), alpha=ease(a), shadow=10)

SCENES3 = {1: (m1, 111), 2: (m2, 158), 3: (m3, 149), 4: (m4, 191), 5: (m5, 198), 6: (m6, 187)}
