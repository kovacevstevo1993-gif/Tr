"""Video lungo 3 (Costco) - blocco 1 (gancio). 1920x1080, 30 fps.
Uso: OUT=cartella python3 long3_b01.py [fotogrammi]      (default 301)
     python3 long3_b01.py frame <secondi> <file.png>     (anteprima di un fotogramma)
Voce: "If you are over sixty, there is a good chance you are paying sixty five dollars a year
for a Costco card, and using only a small part of what comes with it." """
import os, sys, math
os.environ["SA_W"] = "1920"; os.environ["SA_H"] = "1080"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eng2 import *
from PIL import Image, ImageDraw, ImageChops

NFR = 301

def _line(self, p, fill, width):
    flat = [v for pt in p for v in pt] if isinstance(p[0], (tuple, list)) else list(p)
    self.d.line(self._b(flat), fill=fill, width=max(1, int(width * self.ss)), joint="curve")
Cv.line = _line
CX_L = 410            # centro colonna sinistra
CORAL_D = (176, 70, 62)
SKIN = (240, 200, 166)
HAIR = (236, 238, 236)
AMBER = (222, 150, 64)
PANEL_FILL = (9, 44, 34)

# ------------------------------------------------------------------ sprite
def senior_badge():
    def mk():
        S = 320
        c = Cv(S, S)
        c.ell((4, 4, S - 4, S - 4), fill=GREEN_L)
        # spalle (cardigan) + colletto
        c.ell((40, 215, 280, 420), fill=(190, 140, 66))
        c.poly([(125, 222), (160, 268), (195, 222)], fill=IVORY)
        c.rrect((146, 190, 174, 236), 10, fill=SKIN)
        # testa
        c.ell((106, 78, 214, 206), fill=SKIN)
        c.ell((98, 128, 114, 164), fill=SKIN); c.ell((206, 128, 222, 164), fill=SKIN)
        # capelli bianchi
        c.d.pieslice(c._b((98, 62, 222, 190)), 180, 360, fill=HAIR)
        c.ell((98, 98, 122, 150), fill=HAIR); c.ell((198, 98, 222, 150), fill=HAIR)
        c.ell((118, 70, 202, 112), fill=HAIR)
        c.ell((124, 100, 196, 124), fill=SKIN)
        # sopracciglia, occhi, occhiali, sorriso
        c.line([(130, 118), (150, 114)], HAIR, 5); c.line([(170, 114), (190, 118)], HAIR, 5)
        c.ell((131, 132, 149, 150), fill=(255, 255, 255)); c.ell((171, 132, 189, 150), fill=(255, 255, 255))
        c.ell((137, 137, 145, 147), fill=GREEN_D); c.ell((177, 137, 185, 147), fill=GREEN_D)
        c.ell((124, 124, 156, 158), outline=GREEN_D, width=5); c.ell((164, 124, 196, 158), outline=GREEN_D, width=5)
        c.line([(156, 138), (164, 138)], GREEN_D, 5)
        c.arc((136, 150, 184, 190), 20, 160, (160, 80, 70), 5)
        im = c.done()
        mask = Image.new("L", (S * 2, S * 2), 0)
        ImageDraw.Draw(mask).ellipse((8, 8, S * 2 - 8, S * 2 - 8), fill=255)
        mask = mask.resize((S, S), Image.LANCZOS)
        im.putalpha(ImageChops.multiply(im.getchannel("A"), mask))
        ring = Cv(S, S)
        ring.ell((5, 5, S - 5, S - 5), outline=GOLD, width=12)
        ring.ell((16, 16, S - 16, S - 16), outline=GREEN_D, width=3)
        r = ring.done()
        im.paste(r, (0, 0), r)
        return im
    return cache("badge", mk)


def sixty_chip():
    def mk():
        c = Cv(170, 170)
        c.ell((4, 4, 166, 166), fill=IVORY, outline=GOLD, width=8)
        c.text((85, 88), "60+", FONT_SANS, 70, GREEN_D)
        return c.done()
    return cache("chip", mk)


def card_spr():
    def mk():
        w, h = 560, 340
        c = Cv(w, h)
        c.rrect((2, 2, w - 2, h - 2), 34, fill=(236, 188, 108))
        c.rrect((2, 2, w - 2, 110), 34, fill=(196, 146, 72))
        c.d.rectangle(c._b((2, 70, w - 2, 110)), fill=(196, 146, 72))
        c.rrect((14, 14, w - 14, h - 14), 24, outline=(255, 226, 160), width=3)
        c.text((40, 58), "COSTCO MEMBER", FONT_SANS, 44, GREEN_D, anchor="lm", track=3)
        c.text((40, 100), "MEMBERSHIP CARD", FONT_SANS_M, 24, GREEN_D, anchor="lm", track=5)
        # chip
        c.rrect((40, 150, 130, 218), 12, fill=(210, 160, 80), outline=(150, 105, 40), width=3)
        for yy in (172, 196):
            c.line([(40, yy), (130, yy)], (150, 105, 40), 2)
        c.line([(85, 150), (85, 218)], (150, 105, 40), 2)
        # foto
        c.rrect((w - 168, 140, w - 40, 262), 14, fill=GREEN_L, outline=GREEN_D, width=4)
        c.ell((w - 126, 156, w - 82, 204), fill=SKIN)
        c.d.pieslice(c._b((w - 134, 150, w - 74, 196)), 180, 360, fill=HAIR)
        c.ell((w - 152, 214, w - 56, 300), fill=(190, 140, 66))
        # codice a barre
        x = 40
        for i, bw_ in enumerate([5, 3, 7, 3, 4, 8, 3, 5, 3, 6, 4, 3, 7, 3, 5, 4, 8, 3, 4, 6, 3]):
            c.d.rectangle(c._b((x, 262, x + bw_, 308)), fill=GREEN_D)
            x += bw_ + 4
        return c.done()
    return cache("card", mk)


def tag_spr(num):
    def mk():
        w, h = 360, 220
        c = Cv(w, h)
        c.rrect((6, 6, w - 6, h - 6), 28, fill=IVORY, outline=CORAL, width=8)
        c.ell((34, h / 2 - 17, 68, h / 2 + 17), fill=GREEN_D)
        c.text((w / 2 + 28, 92), f"${num}", FONT_SANS, 112, CORAL_D)
        c.text((w / 2 + 22, 168), "EVERY YEAR", FONT_SANS, 36, GREEN_D, track=3)
        return c.done()
    return cache(("tag", num), mk)


def coin_spr():
    def mk():
        c = Cv(80, 80)
        c.ell((2, 2, 78, 78), fill=GOLD, outline=(168, 118, 40), width=4)
        c.ell((13, 13, 67, 67), outline=(168, 118, 40), width=3)
        c.text((40, 42), "$", FONT_SANS, 44, GREEN_D)
        return c.done()
    return cache("coin", mk)


def arrow_spr():
    def mk():
        c = Cv(110, 90)
        c.poly([(2, 28), (62, 28), (62, 4), (108, 45), (62, 86), (62, 62), (2, 62)], fill=GOLD)
        return c.done()
    return cache("arrow", mk)


def check_spr():
    def mk():
        c = Cv(80, 80)
        c.ell((2, 2, 78, 78), fill=GOLD, outline=GREEN_D, width=4)
        c.line([(20, 42), (35, 57), (61, 25)], GREEN_D, 11)
        return c.done()
    return cache("check", mk)


# ------------------------------------------------------------------ icone dei riquadri (centro cx, cy)
def ic_cart(c, cx, cy):
    c.poly([(cx - 52, cy - 22), (cx + 56, cy - 22), (cx + 42, cy + 28), (cx - 38, cy + 28)], fill=IVORY)
    c.line([(cx - 52, cy - 22), (cx - 62, cy - 48), (cx - 84, cy - 48)], IVORY, 9)
    c.ell((cx - 38, cy + 38, cx - 16, cy + 60), fill=GOLD); c.ell((cx + 18, cy + 38, cx + 40, cy + 60), fill=GOLD)
    c.ell((cx - 30, cy - 50, cx - 2, cy - 22), fill=GOLD); c.ell((cx + 6, cy - 46, cx + 34, cy - 18), fill=(214, 108, 96))
    for k in (-26, 0, 26):
        c.line([(cx + k, cy - 14), (cx + k - 4, cy + 20)], (170, 190, 180), 4)

def ic_pill(c, cx, cy):
    c.rrect((cx - 38, cy - 34, cx + 38, cy + 56), 14, fill=AMBER)
    c.rrect((cx - 44, cy - 58, cx + 44, cy - 30), 10, fill=IVORY)
    c.rrect((cx - 28, cy - 8, cx + 28, cy + 36), 8, fill=IVORY)
    c.rrect((cx - 6, cy - 2, cx + 6, cy + 30), 3, fill=CORAL); c.rrect((cx - 16, cy + 8, cx + 16, cy + 20), 3, fill=CORAL)

def ic_hear(c, cx, cy):
    c.arc((cx - 28, cy - 58, cx + 46, cy + 50), 270, 90, IVORY, 11)
    c.arc((cx - 8, cy - 32, cx + 26, cy + 22), 270, 90, IVORY, 8)
    c.rrect((cx - 60, cy - 14, cx - 30, cy + 46), 14, fill=GOLD)
    c.ell((cx - 52, cy + 2, cx - 38, cy + 16), fill=GREEN_D)

def ic_glasses(c, cx, cy):
    c.ell((cx - 66, cy - 30, cx - 8, cy + 28), fill=(154, 200, 170), outline=IVORY, width=9)
    c.ell((cx + 8, cy - 30, cx + 66, cy + 28), fill=(154, 200, 170), outline=IVORY, width=9)
    c.line([(cx - 10, cy - 6), (cx + 10, cy - 6)], IVORY, 8)
    c.line([(cx - 66, cy - 12), (cx - 84, cy - 22)], IVORY, 8); c.line([(cx + 66, cy - 12), (cx + 84, cy - 22)], IVORY, 8)

def ic_tech(c, cx, cy):
    c.rrect((cx - 56, cy - 50, cx + 56, cy + 20), 10, fill=GREEN_D, outline=IVORY, width=8)
    c.poly([(cx - 74, cy + 30), (cx + 74, cy + 30), (cx + 58, cy + 48), (cx - 58, cy + 48)], fill=IVORY)
    c.text((cx, cy - 14), "?", FONT_SANS, 62, GOLD)

def ic_tire(c, cx, cy):
    c.ell((cx - 56, cy - 56, cx + 56, cy + 56), fill=(46, 54, 52), outline=IVORY, width=5)
    for k in range(14):
        a = k * 2 * math.pi / 14
        c.line([(cx + math.cos(a) * 44, cy + math.sin(a) * 44), (cx + math.cos(a) * 56, cy + math.sin(a) * 56)], (150, 160, 156), 6)
    c.ell((cx - 32, cy - 32, cx + 32, cy + 32), fill=SAGE_D, outline=IVORY, width=4)
    c.ell((cx - 10, cy - 10, cx + 10, cy + 10), fill=IVORY)
    for k in range(5):
        a = k * 2 * math.pi / 5 - math.pi / 2
        c.ell((cx + math.cos(a) * 20 - 4, cy + math.sin(a) * 20 - 4, cx + math.cos(a) * 20 + 4, cy + math.sin(a) * 20 + 4), fill=GREEN_D)

TILES = [("SHOPPING", ic_cart), ("PHARMACY", ic_pill), ("HEARING", ic_hear),
         ("EYE EXAM", ic_glasses), ("TECH HELP", ic_tech), ("TIRES", ic_tire)]
TW, TH = 300, 260

def tile_spr(i, lit):
    def mk():
        name, ic = TILES[i]
        c = Cv(TW, TH)
        c.rrect((3, 3, TW - 3, TH - 3), 28, fill=CARD, outline=GOLD if lit else SAGE_D, width=7 if lit else 4)
        ic(c, TW / 2, 100)
        c.text((TW / 2, 214), name, FONT_SANS, 38, GOLD if lit else IVORY)
        return c.done()
    return cache(("tile", i, lit), mk)


def panel_bg():
    def mk():
        w, h = 1040, 840
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 40, fill=PANEL_FILL, outline=SAGE_D, width=5)
        c.rrect((3, 3, w - 3, 96), 40, fill=GOLD)
        c.d.rectangle(c._b((3, 60, w - 3, 96)), fill=GOLD)
        c.text((w / 2, 52), "WHAT COMES WITH THE CARD", FONT_SANS, 46, GREEN_D, track=3)
        return c.done()
    return cache("panel", mk)


def banner_spr():
    def mk():
        w, h = 960, 104
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 52, fill=GOLD, outline=(168, 118, 40), width=4)
        c.text((w / 2, h / 2 + 2), "YOU USE ONLY A SMALL PART", FONT_SANS, 50, GREEN_D, track=2)
        return c.done()
    return cache("banner", mk)


# ------------------------------------------------------------------ scena
PX, PY = 800, 170                       # angolo del pannello
TX0, TY0 = PX + 40, PY + 120            # prima tessera
def tile_pos(i):
    col, row = i % 3, i // 3
    return TX0 + col * (TW + 30) + TW / 2, TY0 + row * (TH + 30) + TH / 2

def draw(img, t):
    ambient(img, t, "$", n=6, alpha=0.08)
    label(img, t, "OVER 60  ·  COSTCO MEMBERSHIP", 70, GOLD, t0=0.1)

    # --- personaggio (0.3 s)  "If you are over sixty"
    s, a, p = pop(t, 0.3, 0.55)
    put(img, senior_badge(), CX_L, 320, scale=0.92 * s, alpha=a, shadow=16)
    s2, a2, _ = pop(t, 0.9, 0.45)
    put(img, sixty_chip(), CX_L + 120, 440, scale=0.9 * s2, alpha=a2, shadow=8, rot=-8)
    burst(img, t, 0.9, CX_L + 120, 440, n=10, seed=2)

    # --- tessera (1.9 s)  "a Costco card"
    p = ease(seg(t, 1.9, 0.7))
    if p > 0:
        fl = math.sin(t * 1.6) * 3 if t > 2.8 else 0
        put(img, card_spr(), CX_L - 700 * (1 - p), 735 + fl, scale=0.96, rot=-3 * p, alpha=min(1, p * 3), shadow=18)

    # --- monete verso la tessera + cartellino $65 (3.0 s)  "paying sixty five dollars a year"
    for k in range(5):
        st = 3.0 + k * 0.22
        pp = seg(t, st, 1.0)
        if 0 < pp < 1:
            e = ease(pp)
            x = CX_L + (k - 2) * 46 * (1 - e) + math.sin(pp * 3.1) * 40
            y = 440 + (735 - 440) * e
            put(img, coin_spr(), x, y, scale=0.8, alpha=min(1, pp * 6) * (1 - seg(pp, 0.8, 0.2)), rot=pp * 360)
    ts = seg(t, 3.0, 0.45)
    if ts > 0:
        num = int(round(65 * ease(seg(t, 3.15, 0.8))))
        bump = 1 + 0.12 * max(0.0, 1 - seg(t, 4.0, 0.3)) if t > 4.0 else 1
        sc = max(ease_back(ts), 0.01) * bump
        put(img, tag_spr(num), CX_L + 200, 905, scale=0.95 * sc, rot=-5, alpha=min(1, ts * 3), shadow=14)
        burst(img, t, 4.0, CX_L + 200, 905, n=12, color=GOLD, rad=200, seed=5)

    # --- freccia + pannello (6.0 s)  "and using only a small part of what comes with it"
    pa = seg(t, 6.0, 0.5)
    if pa > 0:
        put(img, arrow_spr(), 745 + (1 - ease(pa)) * -30, 420, scale=0.8 * max(ease_back(pa), 0.01), alpha=min(1, pa * 3))
    pp_ = ease(seg(t, 6.1, 0.6))
    if pp_ > 0:
        put(img, panel_bg(), PX + 520 + 160 * (1 - pp_), PY + 420, alpha=pp_, shadow=22)
    # tessere (6.8 s ... una ogni 0.22 s); dopo 8.3 s solo la prima resta accesa
    dim = ease(seg(t, 8.3, 0.5))
    for i in range(6):
        st = 6.8 + i * 0.22
        s_, a_, pr = pop(t, st, 0.4)
        if pr <= 0:
            continue
        x, y = tile_pos(i)
        if i == 0:
            put(img, tile_spr(0, True), x, y, scale=s_ * (1 + 0.04 * math.sin(max(0, t - 8.8) * 0) ), alpha=a_)
        else:
            put(img, tile_spr(i, False), x, y, scale=s_, alpha=a_ * (1 - 0.62 * dim))
    # spunta sulla prima tessera
    sc_, ac_, pc_ = pop(t, 8.5, 0.35)
    if pc_ > 0:
        put(img, check_spr(), tile_pos(0)[0] + 118, tile_pos(0)[1] - 98, scale=sc_, alpha=ac_)
        burst(img, t, 8.5, tile_pos(0)[0] + 118, tile_pos(0)[1] - 98, n=8, seed=9, rad=120)
    # striscia finale (8.7 s)
    sb, ab, pb = pop(t, 8.7, 0.4)
    if pb > 0:
        put(img, banner_spr(), PX + 520, PY + 770, scale=sb, alpha=ab, shadow=10)


def render_clip(n, out):
    render_seq(draw, n, out)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "frame":
        img = background(float(sys.argv[2])); draw(img, float(sys.argv[2])); img.save(sys.argv[3]); sys.exit()
    n = int(sys.argv[1]) if len(sys.argv) > 1 else NFR
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_clip(n, f"{out}/costco-blocco01.mp4")
    print("ok", n, "fotogrammi")
