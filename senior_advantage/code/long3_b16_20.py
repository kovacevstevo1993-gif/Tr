"""Video lungo 3 (Costco) - blocchi 16-20 (punto 3 apparecchi acustici e punto 4 visita oculistica). 1920x1080, 30 fps.
Durate dalla timeline dell'utente (07/10/2026): B16 296, B17 393, B18 309, B19 393, B20 290 fotogrammi.
Uso: OUT=cartella python3 long3_b16_20.py <blocco 16..20> [fotogrammi]
     python3 long3_b16_20.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long3_b11_15 import *

DUR.update({16: 296, 17: 393, 18: 309, 19: 393, 20: 290})
PHRASES.update({
    16: ["Costco says the price you see is the price you pay.",
         "That means the price listed for the hearing aid is the price,", "with no hidden fee added at the counter."],
    17: ["Your hearing aids come with a free warranty period,", "and the length varies by model.",
         "You also get free follow up visits,", "free cleanings and check ups,",
         "and loss and damage coverage with no deductible."],
    18: ["A hearing test is not a commitment to buy anything.", "It is only information.",
         "You will know where you stand,", "and you can take that result anywhere you like."],
    19: ["My advice is simple.", "Get the free test,", "ask for the printed result,",
         "and compare it with what other clinics quote you.", "Models and prices change,",
         "so confirm everything at the hearing aid center near you."],
    20: ["Four.", "The eye exam.", "You do not need a membership to book an eye exam",
         "with the independent optometrist who works at or near most Costco warehouses."],
})

# ------------------------------------------------------------------ icone nuove
def shield(c, cx, cy, s=1.0, col=GOLD, ink=GREEN_D):
    c.poly([(cx - 52 * s, cy - 56 * s), (cx + 52 * s, cy - 56 * s), (cx + 52 * s, cy + 6 * s), (cx, cy + 62 * s), (cx - 52 * s, cy + 6 * s)], fill=col)
    check_ic(c, cx, cy - 2 * s, 0.9 * s, ink)

def calendar(c, cx, cy, s=1.0):
    c.rrect((cx - 56 * s, cy - 50 * s, cx + 56 * s, cy + 56 * s), 12 * s, fill=IVORY)
    c.rrect((cx - 56 * s, cy - 50 * s, cx + 56 * s, cy - 14 * s), 12 * s, fill=CORAL)
    c.d.rectangle(c._b((cx - 56 * s, cy - 28 * s, cx + 56 * s, cy - 14 * s)), fill=CORAL)
    for k in range(2):
        c.rrect((cx - 30 * s + k * 52 * s, cy - 62 * s, cx - 20 * s + k * 52 * s, cy - 36 * s), 4, fill=GREEN_D)
    for r_ in range(2):
        for k in range(3):
            c.rrect((cx - 40 * s + k * 30 * s, cy + (-2 + r_ * 28) * s, cx - 20 * s + k * 30 * s, cy + (16 + r_ * 28) * s), 4, fill=(190, 200, 192))
    check_ic(c, cx + 22 * s, cy + 36 * s, 0.4 * s, GREEN_L)

def sparkle(c, cx, cy, s=1.0):
    for dx, dy, k in ((0, 0, 1.0), (46, -34, 0.5), (-44, 38, 0.55)):
        r = 46 * k * s
        c.poly([(cx + dx * s, cy + dy * s - r), (cx + dx * s + r * 0.28, cy + dy * s - r * 0.28), (cx + dx * s + r, cy + dy * s),
                (cx + dx * s + r * 0.28, cy + dy * s + r * 0.28), (cx + dx * s, cy + dy * s + r), (cx + dx * s - r * 0.28, cy + dy * s + r * 0.28),
                (cx + dx * s - r, cy + dy * s), (cx + dx * s - r * 0.28, cy + dy * s - r * 0.28)], fill=GOLD if k == 1.0 else IVORY)

def pin(c, cx, cy, s=1.0, col=CORAL):
    c.ell((cx - 34 * s, cy - 58 * s, cx + 34 * s, cy + 10 * s), fill=col)
    c.poly([(cx - 30 * s, cy - 10 * s), (cx + 30 * s, cy - 10 * s), (cx, cy + 56 * s)], fill=col)
    c.ell((cx - 13 * s, cy - 37 * s, cx + 13 * s, cy - 11 * s), fill=IVORY)

def eye_chart(c, cx, cy, s=1.0):
    c.rrect((cx - 48 * s, cy - 62 * s, cx + 48 * s, cy + 62 * s), 8 * s, fill=IVORY)
    for k, (txt, sz) in enumerate((("E", 40), ("F P", 26), ("T O Z", 20), ("L P E D", 15))):
        c.text((cx, cy + (-40 + k * 28) * s), txt, FONT_SANS, sz * s, GREEN_D)

def report_sheet(c, cx, cy, s=1.0):
    c.rrect((cx - 70 * s, cy - 80 * s, cx + 70 * s, cy + 80 * s), 10 * s, fill=IVORY)
    c.text((cx, cy - 58 * s), "RESULT", FONT_SANS, 19 * s, GREEN_D, track=2)
    pts = [(cx - 52 * s, cy - 18 * s), (cx - 26 * s, cy - 2 * s), (cx, cy + 14 * s), (cx + 26 * s, cy + 26 * s), (cx + 52 * s, cy + 40 * s)]
    c.line(pts, CORAL, 5 * s)
    for p_ in pts:
        c.ell((p_[0] - 5 * s, p_[1] - 5 * s, p_[0] + 5 * s, p_[1] + 5 * s), fill=GREEN_D)
    c.line([(cx - 56 * s, cy + 56 * s), (cx + 56 * s, cy + 56 * s)], (190, 200, 192), 3)

def info_i(c, cx, cy, r):
    c.ell((cx - r, cy - r, cx + r, cy + r), fill=(110, 170, 200))
    c.text((cx, cy + r * 0.04), "i", FONT_SERIF, r * 1.5, IVORY)

def crossed(c, cx, cy, r=70):
    c.ell((cx - r, cy - r, cx + r, cy + r), outline=CORAL, width=10)
    c.line([(cx - r * 0.7, cy - r * 0.7), (cx + r * 0.7, cy + r * 0.7)], CORAL, 10)

def row19(n, text):
    def mk():
        w, h = 1500, 120
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 36, fill=CARD, outline=GOLD, width=5)
        c.ell((22, 15, 112, 105), fill=GOLD)
        c.text((67, 62), str(n), FONT_SERIF, 58, GREEN_D)
        c.text((150, h / 2 + 2), text, FONT_SANS, 46, IVORY, anchor="lm")
        return c.done()
    return cache(("row19", n), mk)

def chip_wide(w, h, fill, border, icon_fn, text, color=IVORY, size=46):
    def mk():
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), h / 2, fill=fill, outline=border, width=7)
        c.ell((24, h / 2 - (h - 36) / 2, 24 + h - 36, h / 2 + (h - 36) / 2), fill=GREEN_D)
        icon_fn(c, 24 + (h - 36) / 2, h / 2)
        c.text((24 + h, h / 2 + 2), text, FONT_SANS, size, color, anchor="lm")
        return c.done()
    return cache(("cw", w, h, text), mk)

# ============================================================ BLOCCO 16
def tag16(txt, sub, col):
    def mk():
        w, h = 620, 330
        c = Cv(w, h)
        c.rrect((6, 6, w - 6, h - 6), 40, fill=IVORY, outline=col, width=10)
        c.ell((38, h / 2 - 22, 82, h / 2 + 22), fill=GREEN_D)
        c.text((w / 2 + 34, 108), txt, FONT_SANS, 62, GREEN_D)
        c.text((w / 2 + 34, 196), sub, FONT_SANS, 80, col)
        return c.done()
    return cache(("t16", txt), mk)

def draw16(img, t):
    ts = starts(16)
    common3(img, t, "THE PRICE YOU SEE", 3)
    a = pop(t, 0.5, 0.5)
    put(img, tag16("PRICE YOU SEE", "$$$", CORAL_D), 520, 330, scale=a[0], alpha=a[1], rot=-3, shadow=16)
    e = pop(t, ts[0] + 2.0, 0.45)
    if e[2] > 0:
        put(img, tspr("=", FONT_SANS, 220, GOLD), 960, 330, scale=e[0], alpha=e[1])
    b = pop(t, ts[0] + 2.4, 0.5)
    if b[2] > 0:
        put(img, tag16("PRICE YOU PAY", "$$$", GREEN_L), 1400, 330, scale=b[0], alpha=b[1], rot=3, shadow=16)
        burst(img, t, ts[0] + 2.6, 1400, 330, n=10, seed=5, rad=240)
    h1 = pop(t, ts[1], 0.5)
    if h1[2] > 0:
        put(img, chip_wide(1500, 150, GREEN_L, GOLD, lambda c, x, y: ic_hear(c, x + 4, y), "THE LISTED HEARING AID PRICE IS THE PRICE", IVORY, 42),
            960, 650, scale=h1[0], alpha=h1[1], shadow=12)
    f = pop(t, ts[2], 0.5)
    if f[2] > 0:
        def fee_icon(c, x, y):
            c.ell((x - 36, y - 36, x + 36, y + 36), fill=GOLD)
            c.text((x, y + 2), "$", FONT_SANS, 48, GREEN_D)
            crossed(c, x, y, 60)
        put(img, chip_wide(1500, 150, PANEL_FILL, CORAL, fee_icon, "NO HIDDEN FEE AT THE COUNTER", CORAL, 52),
            960, 850, scale=f[0], alpha=f[1], shadow=12)

# ============================================================ BLOCCO 17
def card17(i):
    def mk():
        w, h = 410, 420
        l = (("FREE", "WARRANTY"), ("FREE FOLLOW UP", "VISITS"), ("FREE CLEANINGS", "AND CHECK UPS"), ("LOSS AND DAMAGE", "COVERAGE"))[i]
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 36, fill=CARD, outline=GOLD, width=6)
        cx, cy = w / 2, 130
        c.ell((cx - 92, cy - 92, cx + 92, cy + 92), fill=GREEN_L)
        (lambda: shield(c, cx, cy, 1.05) if i == 0 else calendar(c, cx, cy, 1.0) if i == 1 else sparkle(c, cx, cy, 1.1) if i == 2
         else (shield(c, cx, cy, 1.05, SAGE, GREEN_D)))()
        c.text((cx, 268), l[0], FONT_SANS, 34, IVORY)
        c.text((cx, 330), l[1], FONT_SANS, 46 if i != 3 else 42, GOLD)
        return c.done()
    return cache(("c17", i), mk)

def draw17(img, t):
    ts = starts(17)
    common3(img, t, "WHAT COMES WITH THEM", 3)
    for i, k in enumerate((0, 2, 3, 4)):
        s, a, pr = pop(t, ts[k], 0.45)
        if pr > 0:
            put(img, card17(i), 255 + i * 470, 355, scale=s, alpha=a, shadow=14)
    p1 = pop(t, ts[1], 0.45)
    if p1[2] > 0:
        put(img, pill_spr("LENGTH VARIES BY MODEL", 40, 700, 90, GOLD, GREEN_D), 500, 650, scale=p1[0], alpha=p1[1], shadow=8)
    nd = pop(t, ts[4] + 1.6, 0.5)
    if nd[2] > 0:
        def nd_icon(c, x, y):
            shield(c, x, y, 0.62, SAGE, GREEN_D)
        put(img, chip_wide(1500, 150, GREEN_L, GOLD, nd_icon, "NO DEDUCTIBLE ON LOSS AND DAMAGE", IVORY, 50),
            960, 860, scale=nd[0], alpha=nd[1], shadow=12)
        burst(img, t, ts[4] + 1.8, 960, 860, n=10, seed=6, rad=300)

# ============================================================ BLOCCO 18
def draw18(img, t):
    ts = starts(18)
    common3(img, t, "NO PRESSURE", 3)
    a = pop(t, 0.4, 0.5)
    def nc_icon(c, x, y):
        ic_cart_small(c, x, y)
        crossed(c, x, y, 52)
    put(img, chip_wide(1560, 150, PANEL_FILL, CORAL, nc_icon, "A HEARING TEST IS NOT A COMMITMENT TO BUY", IVORY, 46),
        960, 200, scale=a[0], alpha=a[1], shadow=12)
    b = pop(t, ts[1], 0.5)
    if b[2] > 0:
        put(img, chip_wide(1000, 140, GREEN_L, SAGE, lambda c, x, y: info_i(c, x, y, 40), "IT IS ONLY INFORMATION", GOLD, 52),
            680, 410, scale=b[0], alpha=b[1], shadow=10)
    r = pop(t, ts[2], 0.5)
    if r[2] > 0:
        def rs():
            c = Cv(330, 400); report_sheet(c, 165, 200, 2.0); return c.done()
        put(img, cache("rs18", rs), 330, 770, scale=r[0], alpha=r[1], rot=-3, shadow=14)
        put(img, pill_spr("YOU KNOW WHERE YOU STAND", 38, 760, 90, GOLD, GREEN_D), 940, 640, scale=r[0], alpha=r[1], shadow=8)
    ar = seg(t, ts[3], 0.4)
    if ar > 0:
        put(img, arrow_spr(), 600, 790, scale=1.1 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))
    for i in range(3):
        s, a_, pr = pop(t, ts[3] + 0.4 + i * 0.3, 0.4)
        if pr > 0:
            put(img, storefront(), 890 + i * 250, 800, scale=1.15 * s, alpha=a_, shadow=6)
    ay = pop(t, ts[3] + 1.4, 0.45)
    if ay[2] > 0:
        put(img, pill_spr("TAKE THE RESULT ANYWHERE YOU LIKE", 40, 1000, 90, IVORY, GREEN_D, GOLD), 1260, 950, scale=ay[0], alpha=ay[1], shadow=8)

def ic_cart_small(c, cx, cy):
    c.poly([(cx - 34, cy - 14), (cx + 38, cy - 14), (cx + 28, cy + 20), (cx - 24, cy + 20)], fill=IVORY)
    c.line([(cx - 34, cy - 14), (cx - 42, cy - 32), (cx - 56, cy - 32)], IVORY, 7)
    c.ell((cx - 24, cy + 26, cx - 10, cy + 40), fill=GOLD); c.ell((cx + 12, cy + 26, cx + 26, cy + 40), fill=GOLD)

# ============================================================ BLOCCO 19
def draw19(img, t):
    ts = starts(19)
    common3(img, t, "MY ADVICE", 3)
    intro(img, t, "MY ADVICE", "IS SIMPLE", ts[1], size=150)
    texts = ("GET THE FREE TEST", "ASK FOR THE PRINTED RESULT", "COMPARE IT WITH OTHER CLINICS' QUOTES")
    for i, k in enumerate((1, 2, 3)):
        s, a, pr = pop(t, ts[k], 0.45)
        if pr > 0:
            put(img, row19(i + 1, texts[i]), 960, 200 + i * 150, scale=s, alpha=a, shadow=8)
    w = pop(t, ts[4], 0.45)
    if w[2] > 0:
        put(img, chip_wide(1500, 130, PANEL_FILL, CORAL, lambda c, x, y: warn_tri(c, x, y, 0.6, CORAL, PANEL_FILL), "MODELS AND PRICES CHANGE", CORAL, 50),
            960, 680, scale=w[0], alpha=w[1], shadow=10)
    cf = pop(t, ts[5], 0.45)
    if cf[2] > 0:
        put(img, chip_wide(1500, 130, GREEN_L, GOLD, lambda c, x, y: pin(c, x, y + 4, 0.6), "CONFIRM AT THE CENTER NEAR YOU", IVORY, 50),
            960, 850, scale=cf[0], alpha=cf[1], shadow=10)
        burst(img, t, ts[5] + 0.3, 960, 850, n=10, seed=2, rad=300)

# ============================================================ BLOCCO 20
def draw20(img, t):
    ts = starts(20)
    common(img, t, "SAVING NUMBER 4")
    b = pop(t, ts[0] + 0.3, 0.55)
    put(img, num_badge(4), 330, 330, scale=0.85 * b[0], alpha=b[1], shadow=16)
    burst(img, t, ts[0] + 0.6, 330, 330, n=14, seed=3, rad=250)
    h1 = fade(t, ts[1])
    if h1 > 0:
        put_left(img, tspr("THE EYE", FONT_SANS, 112, IVORY), 590, 280, 112, alpha=h1)
        put_left(img, tspr("EXAM", FONT_SANS, 130, GOLD), 590, 405, 130, alpha=h1)
    bk = pop(t, ts[2], 0.45)
    if bk[2] > 0:
        put(img, pill_spr("BOOK AN EYE EXAM", 44, 760, 92, GOLD, GREEN_D), 590 + 380, 540, scale=bk[0], alpha=bk[1], shadow=8)
    n = pop(t, ts[2] + 1.8, 0.45)
    if n[2] > 0:
        def nm_icon(c, x, y):
            c.rrect((x - 44, y - 28, x + 44, y + 28), 8, fill=GOLD)
            c.rrect((x - 44, y - 14, x + 44, y - 4), 0, fill=(196, 146, 72))
            crossed(c, x, y, 66)
        put(img, cache("c20n", lambda: chip_icon(780, 230, PANEL_FILL, CORAL, nm_icon, "NO MEMBERSHIP", "NEEDED TO BOOK", 44, 52, c2=CORAL)),
            500, 800, scale=n[0], alpha=n[1], shadow=12)
    o = pop(t, ts[3], 0.45)
    if o[2] > 0:
        def op_icon(c, x, y):
            eye_chart(c, x - 18, y, 0.85)
            person_ic(c, x + 34, y + 24, 0.62, IVORY)
        put(img, cache("c20o", lambda: chip_icon(880, 230, GREEN_L, SAGE, op_icon, "INDEPENDENT OPTOMETRIST", "AT OR NEAR COSTCO", 36, 48, tx=216)),
            1400, 800, scale=o[0], alpha=o[1], shadow=12)
        burst(img, t, ts[3] + 0.3, 1400, 800, n=10, seed=7, rad=230)

DRAW.update({16: draw16, 17: draw17, 18: draw18, 19: draw19, 20: draw20})

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
