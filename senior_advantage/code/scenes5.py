import sys, math, random, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes4 import *

# =====================================================================
# SHORT 5: SNAP per over 60 (3 regole). Stesso motore, piu' movimento e piu' oggetti.
# uso: S5_OUT=cartella python3 scenes5.py <clip>
# =====================================================================
LEAF = (110, 176, 124)
CRUST = (214, 160, 80)
CRUST_D = (190, 140, 60)

# ---------------------------------------------------------------- sprite nuovi
def person_spr(kind):
    """kind: on (oro), off (vuota), no (vuota corallo)"""
    def mk():
        c = Cv(70, 90)
        if kind == "on":
            c.rrect((6, 42, 64, 88), 22, fill=GOLD, outline=CRUST_D, width=3)
            c.ell((19, 4, 51, 38), fill=(236, 194, 154))
            c.ell((17, 2, 53, 20), fill=(240, 240, 236))
            c.ell((16, 14, 26, 30), fill=(240, 240, 236))
            c.ell((44, 14, 54, 30), fill=(240, 240, 236))
        else:
            col = SAGE_D if kind == "off" else CORAL
            c.rrect((6, 42, 64, 88), 22, fill=(16, 64, 50), outline=col, width=4)
            c.ell((19, 4, 51, 38), fill=(16, 64, 50), outline=col, width=4)
        return c.done()
    return cache(("person", kind), mk)

def apple_spr():
    def mk():
        c = Cv(110, 124)
        c.ell((4, 24, 58, 118), fill=CORAL)
        c.ell((50, 24, 106, 118), fill=CORAL)
        c.ell((22, 36, 88, 118), fill=CORAL)
        c.line([55, 34, 60, 8], (120, 78, 52), 6)
        c.poly([(62, 22), (96, 4), (92, 34)], fill=LEAF)
        c.arc((18, 44, 52, 90), 200, 270, (255, 190, 176), 7)
        return c.done()
    return cache("apple5", mk)

def bread_spr():
    def mk():
        c = Cv(170, 104)
        c.rrect((4, 20, 166, 100), 42, fill=CRUST, outline=CRUST_D, width=4)
        for x in (48, 84, 120):
            c.line([x, 36, x + 16, 62], CRUST_D, 7)
        return c.done()
    return cache("bread5", mk)

def milk_spr():
    def mk():
        c = Cv(92, 160)
        c.poly([(8, 46), (46, 6), (84, 46)], fill=(226, 220, 204))
        c.rrect((8, 42, 84, 154), 8, fill=IVORY)
        c.rrect((52, 42, 84, 154), 8, fill=(226, 220, 204))
        c.rrect((20, 78, 60, 122), 8, fill=SAGE)
        c.ell((30, 90, 50, 110), fill=IVORY)
        return c.done()
    return cache("milk5", mk)

def basket_spr():
    def mk():
        c = Cv(300, 250)
        c.arc((46, 4, 254, 190), 180, 360, CRUST_D, 14)
        c.poly([(8, 96), (292, 96), (252, 240), (48, 240)], fill=CRUST)
        c.line([8, 96, 292, 96], CRUST_D, 12)
        c.line([48, 240, 252, 240], CRUST_D, 10)
        for x in (70, 110, 150, 190, 230):
            c.line([x, 104, x - (150 - x) * 0.0 + (x - 150) * 0.28, 236], CRUST_D, 5)
        for y in (140, 184):
            c.line([20 + (y - 96) * 0.28, y, 280 - (y - 96) * 0.28, y], CRUST_D, 5)
        return c.done()
    return cache("basket5", mk)

FOODS = None
def food_list():
    return [apple_spr(), bread_spr(), milk_spr()]

def ambient_food(img, t, n=7, seed=5, alpha=0.13):
    """cibo che sale piano sullo sfondo (al posto di $ e %)"""
    rnd = random.Random(seed)
    sp_l = food_list()
    for i in range(n):
        sp = sp_l[i % 3]
        x0 = rnd.uniform(110, W - 110)
        v = rnd.uniform(24, 52)
        ph = rnd.uniform(0, 6.28)
        sc = rnd.choice([0.55, 0.7, 0.85])
        off = rnd.uniform(0, H + 260)
        y = (off - t * v) % (H + 260) - 130
        x = x0 + math.sin(t * 0.7 + ph) * 26
        put(img, sp, x, y, scale=sc, alpha=alpha, rot=math.sin(t * 0.9 + ph) * 18)

def zoomed(fn):
    """spinta lenta in avanti su tutta la clip (piu' movimento)"""
    def draw(img, t):
        fn(img, t)
        z = 1.0 + 0.0085 * t
        cw, ch = W / z, H / z
        x0, y0 = (W - cw) / 2, (H - ch) / 2
        crop = img.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.BILINEAR)
        img.paste(crop, (0, 0))
    return draw

# ---------------------------------------------------------------- scene
GX0, GY0, GST = 540 - 4.5 * 84, 520, 88

def pos(i):
    return GX0 + (i % 10) * 84, GY0 + (i // 10) * GST

def s1(img, t):
    ambient_food(img, t, n=7, seed=71)
    if t < 0.95:
        sw, al, aw = pop(t, 0.0, 0.35)
        fade = 1.0 - seg(t, 0.6, 0.3)
        shake = 7 * math.sin(t * 38) * (1 - seg(t, 0.0, 0.7))
        put(img, glow_spr(), 540, 880, scale=1.3, alpha=0.3 * fade)
        put(img, tspr("WAIT...", FONT_SERIF, 230, CORAL), 540 + shake, 880, scale=sw, alpha=al * fade, rot=-4, shadow=16)
    else:
        label(img, t, "SNAP FOR SENIORS", 300, SAGE, t0=0.95)
    # 100 persone: onda iniziale, poi 55 si accendono d'oro
    n_on = 0
    for i in range(100):
        x, y = pos(i)
        t_in = 0.55 + i * 0.0035
        s, al, a = pop(t, t_in, 0.3)
        if a <= 0:
            continue
        t_on = 1.05 + i * 0.022
        if i < 55 and t >= t_on:
            n_on += 1
            u = seg(t, t_on, 0.3)
            put(img, person_spr("on"), x, y - 10 * math.sin(u * 3.14), scale=0.74 * (1 + 0.3 * math.sin(u * 3.14)), alpha=1.0, shadow=4)
        elif i >= 55 and t > 2.4:
            u = seg(t, 2.4 + (i - 55) * 0.006, 0.4)
            put(img, person_spr("no"), x, y, scale=0.74 * (0.86 + 0.14 * ease_back(u)), alpha=0.55 + 0.25 * math.sin(t * 5 + i * 0.5))
        else:
            put(img, person_spr("off"), x, y, scale=0.74 * s, alpha=al)
    # contatore
    u = seg(t, 1.05, 1.3)
    if u > 0:
        n = int(round(55 * ease(u)))
        put(img, glow_spr(), 300, 1440, scale=0.9, alpha=0.25 * min(1.0, u * 3))
        put(img, tspr(str(n), FONT_SERIF, 300, GOLD), 300, 1440, shadow=16, scale=1.0 + 0.05 * max(0.0, math.sin(min(1.0, u) * 3.14 * 2)))
    if u >= 1.0:
        burst(img, t, 2.3, 300, 1440, n=12, color=GOLD, dur=0.7, rad=250, seed=72)
    a = seg(t, 2.2, 0.45)
    if a > 0:
        put(img, tspr("OUT OF 100", FONT_SANS, 62, IVORY), 730, 1385 + 20 * (1 - ease(a)), alpha=ease(a), shadow=8)
    a = seg(t, 2.55, 0.45)
    if a > 0:
        put(img, tspr("ELIGIBLE SENIORS", FONT_SANS, 44, SAGE, track=4), 730, 1465 + 20 * (1 - ease(a)), alpha=ease(a))
    # finale: GET SNAP + cestino con cibo
    s, al, a = pop(t, 3.55, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1685, scale=1.2, alpha=0.3 * al)
        put(img, tag_spr("GET SNAP", 620, 150, GOLD, 86), 560, 1685, scale=s, alpha=al, rot=-2, shadow=14)
        burst(img, t, 3.55, 560, 1685, n=14, color=GOLD, dur=0.7, rad=360, seed=73)
    s, al, a = pop(t, 3.7, 0.5)
    if a > 0:
        bob = 5 * math.sin((t - 3.7) * 6)
        put(img, basket_spr(), 125, 1670 + bob, scale=0.55 * s, alpha=al, shadow=10, rot=-4)
        put(img, apple_spr(), 108, 1612 + bob, scale=0.5 * s, alpha=al, rot=-10)
        put(img, bread_spr(), 158, 1616 + bob, scale=0.42 * s, alpha=al, rot=14)
    s, al, a = pop(t, 3.95, 0.5)
    if a > 0:
        put(img, milk_spr(), 960, 1670 + 6 * math.sin((t - 3.95) * 5), scale=0.7 * s, alpha=al, shadow=8, rot=8)

# durate in fotogrammi (dalla timeline CapCut, dalla fine del clip precedente)
SCENES5 = {1: (s1, 147)}

if __name__ == "__main__":
    k = int(sys.argv[1])
    out_dir = os.environ.get("S5_OUT", "short5")
    os.makedirs(out_dir, exist_ok=True)
    fn, nf = SCENES5[k]
    render_seq(zoomed(fn), nf, f"{out_dir}/short5-clip{k:02d}.mp4")
