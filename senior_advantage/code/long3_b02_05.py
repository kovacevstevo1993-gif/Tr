"""Video lungo 3 (Costco) - blocchi 2-5. 1920x1080, 30 fps.
Durate in fotogrammi dalla timeline dell'utente (07/10/2026): B2 543, B3 524, B4 352, B5 542.
Uso: OUT=cartella python3 long3_b02_05.py <blocco 2..5> [fotogrammi]
     python3 long3_b02_05.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long3_b01 import *      # imposta 1920x1080, carica engine + sprite comuni

DUR = {2: 543, 3: 524, 4: 352, 5: 542}
PHRASES = {
    2: ["Let me say the first thing clearly.", "Costco does not have a senior discount.",
        "I checked Costco's own website, and its customer service page says it does not offer discounted memberships for seniors.",
        "Every month, thousands of people search for one anyway."],
    3: ["But that is not the end of the story.",
        "I went through Costco's official pages, one by one, and found fourteen things that really do save seniors money.",
        "Some are free,", "some need no membership at all,",
        "and one of them can cost you money if you choose it for the wrong reason."],
    4: ["I will tell you what each one is,", "who it helps,", "what to do,", "and what to watch out for.",
        "Stay to the end, because number fourteen is the one almost everyone gets wrong."],
    5: ["First, the basics.", "A basic Gold Star membership costs sixty five dollars a year.",
        "Executive costs one hundred thirty.", "The price is the same at every age,",
        "so the savings in this video come from what Costco already offers, not from an age discount."],
}

def starts(b):
    """secondi in cui comincia ogni frase (proporzionale ai caratteri, voce circa 96% del blocco)"""
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

def put_left(img, spr, left, cy, size, **kw):
    put(img, spr, left - int(size * 0.35) + spr.width / 2, cy, **kw)

def fade(t, t0, dur=0.35):
    return ease(seg(t, t0, dur))

# ------------------------------------------------------------------ icone / sprite comuni
def magnifier(c, cx, cy, r, col, w=10):
    c.ell((cx - r, cy - r, cx + r, cy + r), outline=col, width=w)
    c.line([(cx + r * 0.7, cy + r * 0.7), (cx + r * 1.6, cy + r * 1.6)], col, w * 1.3)

def person_ic(c, cx, cy, s, col, head=SKIN):
    c.ell((cx - 22 * s, cy - 58 * s, cx + 22 * s, cy - 14 * s), fill=head)
    c.d.pieslice(c._b((cx - 42 * s, cy - 6 * s, cx + 42 * s, cy + 78 * s)), 180, 360, fill=col)

def warn_tri(c, cx, cy, s, col=GOLD, ink=GREEN_D):
    c.poly([(cx, cy - 58 * s), (cx + 62 * s, cy + 46 * s), (cx - 62 * s, cy + 46 * s)], fill=col)
    c.rrect((cx - 6 * s, cy - 22 * s, cx + 6 * s, cy + 14 * s), 3, fill=ink)
    c.ell((cx - 7 * s, cy + 22 * s, cx + 7 * s, cy + 36 * s), fill=ink)

def check_ic(c, cx, cy, s, col=GOLD):
    c.line([(cx - 28 * s, cy), (cx - 8 * s, cy + 22 * s), (cx + 30 * s, cy - 24 * s)], col, 14 * s)

def pill_spr(text, size, w, h, fill, ink, border=None, track=0):
    def mk():
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), h / 2, fill=fill, outline=border, width=5 if border else 1)
        c.text((w / 2, h / 2 + 2), text, FONT_SANS, size, ink, track=track)
        return c.done()
    return cache(("pill", text, size, w, h, fill, ink, border, track), mk)

def common(img, t, text):
    ambient(img, t, "$", n=6, alpha=0.08)
    label(img, t, text, 70, GOLD, t0=0.1)

# ============================================================ BLOCCO 2
def senior_tag():
    def mk():
        w, h = 560, 270
        c = Cv(w, h)
        c.rrect((6, 6, w - 6, h - 6), 34, fill=IVORY, outline=GOLD, width=9)
        c.ell((34, h / 2 - 20, 74, h / 2 + 20), fill=GREEN_D)
        c.text((w / 2 + 26, 100), "SENIOR", FONT_SANS, 84, GREEN_D, track=4)
        c.text((w / 2 + 26, 190), "DISCOUNT", FONT_SANS, 84, CORAL_D, track=4)
        return c.done()
    return cache("stag", mk)

def no_sign():
    def mk():
        S = 440
        c = Cv(S, S)
        c.ell((14, 14, S - 14, S - 14), outline=CORAL, width=34)
        c.line([(88, 88), (S - 88, S - 88)], CORAL, 34)
        return c.done()
    return cache("nosign", mk)

def browser():
    def mk():
        w, h = 860, 480
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 30, fill=IVORY, outline=SAGE_D, width=5)
        c.rrect((3, 3, w - 3, 78), 30, fill=(214, 224, 214))
        c.d.rectangle(c._b((3, 40, w - 3, 78)), fill=(214, 224, 214))
        for i, col in enumerate(((214, 108, 96), GOLD, (110, 190, 130))):
            c.ell((30 + i * 36, 28, 52 + i * 36, 50), fill=col)
        c.rrect((170, 18, w - 40, 62), 22, fill=IVORY)
        c.text((200, 41), "costco.com", FONT_SANS_M, 30, GREEN_D, anchor="lm")
        c.d.rectangle(c._b((3, 78, w - 3, 160)), fill=GREEN_D)
        c.text((46, 120), "CUSTOMER SERVICE", FONT_SANS, 40, IVORY, anchor="lm", track=3)
        # righe "pagina"
        for i, ww in enumerate((520, 420)):
            c.rrect((46, 196 + i * 40, 46 + ww, 214 + i * 40), 9, fill=(206, 214, 206))
        c.rrect((46, 276, w - 46, 446), 22, fill=(238, 232, 214), outline=(206, 190, 150), width=3)
        c.text((80, 322), "Senior memberships", FONT_SANS, 42, GREEN_D, anchor="lm")
        return c.done()
    return cache("browser", mk)

def search_bar(txt, cursor):
    def mk():
        w, h = 980, 120
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 60, fill=IVORY, outline=GOLD, width=7)
        magnifier(c, 82, 56, 24, GREEN_D, 9)
        if txt:
            c.text((140, h / 2 + 2), txt + ("|" if cursor else ""), FONT_SANS_M, 52, GREEN_D, anchor="lm")
        elif cursor:
            c.text((140, h / 2 + 2), "|", FONT_SANS_M, 52, GREEN_D, anchor="lm")
        return c.done()
    return cache(("sbar", txt, cursor), mk)

def draw2(img, t):
    ts = starts(2)
    common(img, t, "THE FIRST THING, CLEARLY")
    # etichetta cartellino (sempre fermo, poi barrato)
    s, a, p = pop(t, 0.5, 0.5)
    put(img, senior_tag(), 560, 400, scale=s, rot=-4, alpha=a, shadow=18)
    sg = seg(t, ts[1] + 0.1, 0.4)
    if sg > 0:
        put(img, no_sign(), 560, 400, scale=max(ease_back(sg), 0.01) * 0.92, alpha=min(1, sg * 3))
        burst(img, t, ts[1] + 0.35, 560, 400, n=10, color=CORAL, rad=260, seed=4)
    ta = pop(t, ts[1] + 0.7, 0.4)
    if ta[2] > 0:
        put(img, pill_spr("NO SENIOR DISCOUNT", 56, 760, 110, PANEL_FILL, CORAL, CORAL), 560, 700, scale=ta[0], alpha=ta[1], shadow=8)
    # sito web ufficiale
    wb = pop(t, ts[2], 0.5)
    if wb[2] > 0:
        put(img, browser(), 1400, 410, scale=wb[0], alpha=wb[1], shadow=20)
    tc = ts[2] + 0.5 * (ts[3] - ts[2])
    st = pop(t, tc, 0.4)
    if st[2] > 0:
        put(img, pill_spr("NO DISCOUNT OFFERED", 36, 560, 78, CORAL, IVORY), 1350, 556, scale=st[0], alpha=st[1])
        burst(img, t, tc + 0.1, 1350, 556, n=8, color=CORAL, rad=160, seed=8)
    cw = pop(t, ts[2] + 0.5, 0.4)
    if cw[2] > 0:
        put(img, pill_spr("COSTCO'S OWN WEBSITE", 38, 620, 84, GOLD, GREEN_D), 1400, 700, scale=cw[0], alpha=cw[1], shadow=8)
    # ricerca: "thousands of people search for one anyway"
    sb = pop(t, ts[3], 0.45)
    if sb[2] > 0:
        full = "costco senior discount"
        n = int(len(full) * seg(t, ts[3] + 0.5, 1.8))
        cur = int(t * 2.4) % 2 == 0 and seg(t, ts[3] + 0.5, 1.8) < 1.0
        put(img, search_bar(full[:n], cur), 640, 880, scale=sb[0], alpha=sb[1], shadow=10)
    bd = pop(t, ts[3] + 2.4, 0.45)
    if bd[2] > 0:
        put(img, pill_spr("THOUSANDS SEARCH IT EVERY MONTH", 36, 760, 120, PANEL_FILL, GOLD, GOLD), 1440, 880, scale=bd[0], alpha=bd[1], shadow=8)

# ============================================================ BLOCCO 3
def badge14():
    def mk():
        S = 380
        c = Cv(S, S)
        c.ell((6, 6, S - 6, S - 6), fill=GOLD)
        c.ell((24, 24, S - 24, S - 24), outline=GREEN_D, width=5)
        c.text((S / 2, S / 2 + 6), "14", FONT_SERIF, 210, GREEN_D)
        return c.done()
    return cache("b14", mk)

def tile_num(n):
    def mk():
        c = Cv(100, 116)
        c.rrect((2, 2, 98, 114), 18, fill=IVORY, outline=GOLD, width=4)
        c.rrect((2, 2, 98, 30), 18, fill=GOLD)
        c.d.rectangle(c._b((2, 18, 98, 30)), fill=GOLD)
        c.text((50, 74), str(n), FONT_SERIF, 54, GREEN_D)
        return c.done()
    return cache(("tn", n), mk)

def chip3(kind):
    def mk():
        w, h = 560, 200
        col = {"free": (GREEN_L, SAGE), "nomem": (CARD, GOLD), "cost": (PANEL_FILL, CORAL)}[kind]
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 36, fill=col[0], outline=col[1], width=7)
        c.ell((26, h / 2 - 54, 134, h / 2 + 54), fill=col[1])
        cx, cy = 80, h / 2
        if kind == "free":
            check_ic(c, cx, cy, 1.0, GREEN_D)
        elif kind == "nomem":
            c.rrect((cx - 36, cy - 24, cx + 36, cy + 24), 8, fill=GREEN_D)
            c.rrect((cx - 36, cy - 12, cx + 36, cy - 2), 0, fill=GOLD)
            c.line([(cx - 44, cy + 34), (cx + 44, cy - 34)], CORAL, 9)
        else:
            warn_tri(c, cx, cy - 2, 0.8, PANEL_FILL, CORAL)
        lines = {"free": ("SOME ARE", "FREE"), "nomem": ("SOME NEED NO", "MEMBERSHIP"),
                 "cost": ("ONE CAN COST", "YOU MONEY")}[kind]
        c.text((156, h / 2 - 32), lines[0], FONT_SANS, 40, IVORY, anchor="lm")
        c.text((156, h / 2 + 24), lines[1], FONT_SANS, 46, col[1], anchor="lm")
        return c.done()
    return cache(("chip3", kind), mk)

def draw3(img, t):
    ts = starts(3)
    common(img, t, "BUT THERE IS MORE")
    # frase 0: grande, poi lascia il posto al 14
    a0 = fade(t, 0.4) * (1 - fade(t, ts[1] - 0.1, 0.35))
    if a0 > 0:
        shadow_a = a0
        put(img, tspr("BUT THAT IS NOT", FONT_SANS, 118, IVORY), 960, 400 - 30 * (1 - a0), alpha=a0)
        put(img, tspr("THE END OF THE STORY", FONT_SANS, 118, GOLD), 960, 540 - 30 * (1 - a0), alpha=a0)
    # frase 1: badge 14 + titolo + pagine ufficiali + 14 tessere
    b = pop(t, ts[1] + 0.1, 0.55)
    if b[2] > 0:
        put(img, badge14(), 340, 330, scale=0.92 * b[0], alpha=b[1], shadow=16)
        burst(img, t, ts[1] + 0.3, 340, 330, n=14, seed=3, rad=250)
    h1 = fade(t, ts[1] + 0.5)
    if h1 > 0:
        put_left(img, tspr("THINGS THAT REALLY", FONT_SANS, 80, IVORY), 590, 280, 80, alpha=h1)
        put_left(img, tspr("SAVE SENIORS MONEY", FONT_SANS, 80, GOLD), 590, 378, 80, alpha=h1)
    cp = fade(t, ts[1] + 1.0)
    if cp > 0:
        put_left(img, tspr("FROM COSTCO'S OFFICIAL PAGES", FONT_SANS_M, 38, SAGE, track=3), 590, 462, 38, alpha=cp)
    x0 = 169
    for i in range(14):
        st = ts[1] + 1.7 + i * 0.2
        s, a, pr = pop(t, st, 0.3)
        if pr > 0:
            put(img, tile_num(i + 1), x0 + 50 + i * 114, 610, scale=s, alpha=a, shadow=6)
    # frasi 2-4: tre risposte
    for k, kind, x in ((2, "free", 360), (3, "nomem", 960), (4, "cost", 1560)):
        s, a, pr = pop(t, ts[k], 0.45)
        if pr > 0:
            put(img, chip3(kind), x, 850, scale=s, alpha=a, shadow=10)

# ============================================================ BLOCCO 4
def card4(i):
    def mk():
        w, h = 410, 420
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 36, fill=CARD, outline=GOLD if i < 3 else CORAL, width=7)
        cx, cy = w / 2, 130
        c.ell((cx - 92, cy - 92, cx + 92, cy + 92), fill=GREEN_L)
        if i == 0:
            magnifier(c, cx - 8, cy - 8, 38, IVORY, 11)
            c.text((cx - 8, cy - 7), "?", FONT_SANS, 44, GOLD)
        elif i == 1:
            person_ic(c, cx - 30, cy + 8, 0.9, (190, 140, 66))
            person_ic(c, cx + 34, cy + 20, 0.7, SAGE, head=(226, 190, 160))
        elif i == 2:
            c.rrect((cx - 46, cy - 62, cx + 46, cy + 62), 12, fill=IVORY)
            c.rrect((cx - 22, cy - 72, cx + 22, cy - 50), 8, fill=GOLD)
            for k in range(3):
                yy = cy - 28 + k * 34
                c.line([(cx - 32, yy), (cx - 22, yy + 10), (cx - 6, yy - 10)], GREEN_L, 7)
                c.rrect((cx + 4, yy - 5, cx + 34, yy + 5), 4, fill=(190, 200, 190))
        else:
            warn_tri(c, cx, cy + 4, 1.0, CORAL, IVORY)
        l1, l2 = (("WHAT", "IT IS"), ("WHO", "IT HELPS"), ("WHAT", "TO DO"), ("WATCH", "OUT FOR"))[i]
        c.text((cx, 270), l1, FONT_SANS, 50, IVORY)
        c.text((cx, 332), l2, FONT_SANS, 56, GOLD if i < 3 else CORAL)
        return c.done()
    return cache(("c4", i), mk)

def banner4():
    def mk():
        w, h = 1560, 240
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), 60, fill=GOLD, outline=(168, 118, 40), width=5)
        c.ell((34, h / 2 - 80, 194, h / 2 + 80), fill=CORAL_D)
        c.text((114, h / 2 + 6), "14", FONT_SERIF, 100, IVORY)
        c.text((236, 88), "STAY TO THE END", FONT_SANS, 86, GREEN_D, anchor="lm")
        c.text((236, 172), "NUMBER 14 IS THE ONE ALMOST EVERYONE GETS WRONG", FONT_SANS, 37, GREEN_D, anchor="lm")
        return c.done()
    return cache("b4", mk)

def draw4(img, t):
    ts = starts(4)
    common(img, t, "WHAT YOU WILL GET")
    for i in range(4):
        s, a, pr = pop(t, ts[i], 0.45)
        if pr > 0:
            put(img, card4(i), 255 + i * 470, 360, scale=s, alpha=a, shadow=14)
    bn = pop(t, ts[4], 0.5)
    if bn[2] > 0:
        put(img, banner4(), 960, 830, scale=bn[0], alpha=bn[1], shadow=14)
        burst(img, t, ts[4] + 0.3, 330, 830, n=10, seed=6, rad=200)

# ============================================================ BLOCCO 5
def card5(kind):
    def mk():
        w, h = 560, 340
        gold = kind == "gold"
        base, band, edge, ink, sub = ((236, 188, 108), (196, 146, 72), (255, 226, 160), GREEN_D, GREEN_D) if gold else \
                                     ((24, 78, 62), GOLD, GOLD, IVORY, SAGE)
        c = Cv(w, h)
        c.rrect((2, 2, w - 2, h - 2), 34, fill=base)
        c.rrect((2, 2, w - 2, 110), 34, fill=band)
        c.d.rectangle(c._b((2, 70, w - 2, 110)), fill=band)
        c.rrect((14, 14, w - 14, h - 14), 24, outline=edge, width=3)
        c.text((40, 58), "GOLD STAR" if gold else "EXECUTIVE", FONT_SANS, 46, GREEN_D, anchor="lm", track=4)
        c.text((40, 100), "COSTCO MEMBERSHIP", FONT_SANS_M, 24, GREEN_D, anchor="lm", track=5)
        c.rrect((40, 150, 130, 218), 12, fill=(210, 160, 80), outline=(150, 105, 40), width=3)
        for yy in (172, 196):
            c.line([(40, yy), (130, yy)], (150, 105, 40), 2)
        c.line([(85, 150), (85, 218)], (150, 105, 40), 2)
        if not gold:   # stella
            cx, cy = w - 110, 196
            pts = []
            for k in range(10):
                r = 56 if k % 2 == 0 else 24
                a = -math.pi / 2 + k * math.pi / 5
                pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
            c.poly(pts, fill=GOLD)
        else:
            c.rrect((w - 168, 140, w - 40, 262), 14, fill=GREEN_L, outline=GREEN_D, width=4)
            c.ell((w - 126, 156, w - 82, 204), fill=SKIN)
            c.d.pieslice(c._b((w - 134, 150, w - 74, 196)), 180, 360, fill=HAIR)
            c.ell((w - 152, 214, w - 56, 300), fill=(190, 140, 66))
        x = 40
        for bw_ in [5, 3, 7, 3, 4, 8, 3, 5, 3, 6, 4, 3, 7, 3, 5, 4, 8, 3, 4, 6, 3]:
            c.d.rectangle(c._b((x, 262, x + bw_, 308)), fill=ink if not gold else GREEN_D)
            x += bw_ + 4
        return c.done()
    return cache(("c5", kind), mk)

def tag5(num):
    def mk():
        w, h = 420, 220
        c = Cv(w, h)
        c.rrect((6, 6, w - 6, h - 6), 28, fill=IVORY, outline=CORAL, width=8)
        c.ell((34, h / 2 - 17, 68, h / 2 + 17), fill=GREEN_D)
        c.text((w / 2 + 26, 92), f"${num}", FONT_SANS, 112 if num < 100 else 98, CORAL_D)
        c.text((w / 2 + 26, 170), "A YEAR", FONT_SANS, 44, GREEN_D, track=5)
        return c.done()
    return cache(("t5", num), mk)

def draw5(img, t):
    ts = starts(5)
    common(img, t, "THE BASICS")
    CY = 300
    g = pop(t, ts[1], 0.5)
    if g[2] > 0:
        put(img, card5("gold"), 500, CY, scale=0.86 * g[0], alpha=g[1], rot=-2, shadow=16)
    tg = pop(t, ts[1] + 2.2, 0.45)
    if tg[2] > 0:
        put(img, tag5(65), 500, 565, scale=0.8 * tg[0], alpha=tg[1], rot=-3, shadow=10)
        burst(img, t, ts[1] + 2.4, 500, 565, n=10, seed=2, rad=170)
    e = pop(t, ts[2], 0.5)
    if e[2] > 0:
        put(img, card5("exec"), 1420, CY, scale=0.86 * e[0], alpha=e[1], rot=2, shadow=16)
    te = pop(t, ts[2] + 1.5, 0.45)
    if te[2] > 0:
        put(img, tag5(130), 1420, 565, scale=0.8 * te[0], alpha=te[1], rot=3, shadow=10)
        burst(img, t, ts[2] + 1.7, 1420, 565, n=10, seed=5, rad=170)
    # stesso prezzo a ogni eta
    t3 = fade(t, ts[3])
    dim = 1 - fade(t, ts[4] + 4.6, 0.35)
    if t3 > 0:
        put(img, tspr("SAME PRICE AT EVERY AGE", FONT_SANS, 46, GOLD, track=3), 960, 715, alpha=t3 * dim)
    for i, ag in enumerate((55, 65, 75, 85)):
        s, a, pr = pop(t, ts[3] + 0.5 + i * 0.28, 0.35)
        if pr > 0:
            put(img, pill_spr(f"AGE {ag}", 42, 240, 84, IVORY, GREEN_D, GOLD), 510 + i * 300, 800, scale=s, alpha=a * dim, shadow=6)
            if i < 3:
                put(img, tspr("=", FONT_SANS, 60, GOLD), 660 + i * 300, 800, alpha=a * dim)
    # il risparmio viene da cio che Costco gia offre, non da uno sconto per eta
    bn = pop(t, ts[4], 0.5)
    if bn[2] > 0:
        put(img, pill_spr("SAVINGS COME FROM WHAT COSTCO ALREADY OFFERS", 44, 1560, 104, GOLD, GREEN_D, (168, 118, 40)), 960, 960, scale=bn[0], alpha=bn[1], shadow=10)
    sm = pop(t, ts[4] + 4.7, 0.4)
    if sm[2] > 0:
        put(img, pill_spr("NOT AN AGE DISCOUNT", 62, 880, 120, PANEL_FILL, CORAL, CORAL), 960, 800, scale=sm[0], alpha=sm[1], rot=-3, shadow=12)

DRAW = {2: draw2, 3: draw3, 4: draw4, 5: draw5}

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/costco-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
