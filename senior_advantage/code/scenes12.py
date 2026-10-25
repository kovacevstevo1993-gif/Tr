import sys, math, random, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes11 import *
from scenes11 import xtext
import subprocess
from PIL import Image, ImageDraw, ImageFilter

# =====================================================================
# SHORT 12: Walmart (correlato al lungo 8). Stile NUOVO rispetto agli short 5-11 (ordine utente 24/10: "un po diversi
# dagli altri e piu professionali"): sfondo a scaffali di negozio che scorrono lenti + luce che passa, contatore a
# cartellini da scaffale 1-10 in alto (stessi numeri del lungo), schede a scontrino, registratore di cassa, banco farmacia,
# flacone, cartellini prezzo, planimetria con corsie. Colori del canale (verde bosco, avorio, oro).
# Durate (fotogrammi, dagli screenshot CapCut del 24/10, riletti senza sottrarre 1 s): 316 286 164 257 195 243 207 (totale 1668).
# Nelle slide compare SOLO cio' che la voce dice. Niente nomi (price match, resi, programma a 4 dollari), cifre di prezzo,
# frasi, passi: restano nel lungo. Ultimo elemento entro l'80%; elementi fermi negli ultimi 15 fotogrammi.
# uso: S12_OUT=cartella SA_TMP=/tmp/x python3 scenes12.py <blocco>
# =====================================================================
HERE = os.path.dirname(os.path.abspath(__file__))
TEXT = {int(m.group(1)): m.group(2) for m in re.finditer(r"(?m)^(\d+) (.*)$",
        open(os.path.join(HERE, "..", "COPIONE-SHORT-12-WALMART.md"), encoding="utf-8").read())}
DUR = {1: 316, 2: 286, 3: 164, 4: 257, 5: 195, 6: 243, 7: 207}
PAPER = (250, 247, 238)
INK = (24, 40, 34)
AMB = (232, 150, 60)
OKG = (110, 200, 130)

_cur = {"b": 1}
def D():
    return DUR[_cur["b"]] / 30.0

def T(key, n=1):
    """secondo in cui la voce arriva a 'key' nel blocco corrente (voce ~95% del blocco); mai oltre l'80%"""
    b = _cur["b"]; s = TEXT[b]; i = -1
    for _ in range(n):
        i = s.index(key, i + 1)
    return min(0.15 + D() * 0.95 * i / len(s), D() * 0.8)

def env(t):
    d = D()
    if t <= d - 0.95:
        return 1.0
    return max(0.0, (d - 0.5 - t) / 0.45)

def bob(t, amp=6, f=0.7, ph=0.0):
    return amp * math.sin(2 * math.pi * f * t + ph) * env(t)

def bst(img, t, t0, cx, cy, n=8, color=GOLD, dur=0.5, rad=160, seed=1):
    if t0 + dur <= D() - 0.45:
        burst(img, t, t0, cx, cy, n=n, color=color, dur=dur, rad=rad, seed=seed)

def pp(img, t, t0, spr, cx, cy, sc=1.0, rot=0.0, dur=0.5, shadow=10, amp=5, ph=0.0, f=0.7, fx=0.0):
    """pop-in poi piccolo movimento vivo (fermo negli ultimi 15 fotogrammi)"""
    s, al, a = pop(t, t0, dur)
    if a <= 0:
        return 0.0
    put(img, spr, cx + bob(t, fx, 0.5, ph + 1.3), cy + bob(t, amp, f, ph), scale=sc * s,
        rot=rot + bob(t, 0.8, 0.45, ph), alpha=al, shadow=shadow)
    return a

# ------------------------------------------------------------------ sfondo a scaffali (scorre lento + luce)
_BG = {}
def background12(t):
    P = 270
    if "tile" not in _BG:
        th = H + P
        im = Image.new("RGB", (W, th), (9, 46, 36))
        d = ImageDraw.Draw(im)
        rnd = random.Random(12)
        for sy in range(0, th, P):
            # ripiano
            d.rectangle([0, sy + P - 30, W, sy + P - 14], fill=(34, 92, 72))
            d.rectangle([0, sy + P - 14, W, sy + P], fill=(6, 30, 24))
            x = 20
            while x < W - 30:
                w = rnd.choice([70, 90, 110, 64])
                h = rnd.choice([110, 140, 170, 96])
                col = rnd.choice([(18, 70, 55), (22, 80, 62), (16, 62, 50), (26, 88, 70), (20, 74, 58)])
                if rnd.random() < 0.5:
                    d.rounded_rectangle([x, sy + P - 30 - h, x + w, sy + P - 30], radius=8, fill=col)
                    d.rectangle([x + 8, sy + P - 30 - h * 0.55, x + w - 8, sy + P - 30 - h * 0.30], fill=(34, 98, 78))
                else:
                    d.rounded_rectangle([x, sy + P - 30 - h, x + w * 0.8, sy + P - 30], radius=int(w * 0.3), fill=col)
                    d.rectangle([x + 6, sy + P - 30 - h * 0.6, x + w * 0.8 - 6, sy + P - 30 - h * 0.35], fill=(34, 98, 78))
                x += w + rnd.choice([10, 18, 26])
        im = im.filter(ImageFilter.GaussianBlur(1.6))
        _BG["tile"] = im
        vig = Image.new("L", (W, H), 0)
        vd = ImageDraw.Draw(vig)
        vd.rectangle([0, 0, W, H], fill=170)
        vd.ellipse([-W * 0.35, -H * 0.12, W * 1.35, H * 1.12], fill=0)
        _BG["vig"] = vig.filter(ImageFilter.GaussianBlur(150))
        _BG["dark"] = Image.new("RGB", (W, H), (3, 18, 14))
        _BG["lite"] = Image.new("RGB", (W, H), (96, 168, 136))
    off = (t * 46) % P
    img = _BG["tile"].crop((0, int(P - off), W, int(P - off) + H)).copy()
    img = Image.composite(_BG["dark"], img, _BG["vig"])
    # fascio di luce che attraversa lento
    x0 = int((t * 110) % (W + 900)) - 450
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).polygon([(x0, 0), (x0 + 200, 0), (x0 - 300, H), (x0 - 500, H)], fill=22)
    sh = sh.filter(ImageFilter.GaussianBlur(60))
    img = Image.composite(_BG["lite"], img, sh)
    return img

def render12(draw_fn, nframes, out):
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", "30",
           "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(nframes):
        t = i / 30.0
        img = background12(t)
        draw_fn(img, t)
        p.stdin.write(img.tobytes())
    p.stdin.close(); p.wait()

# ------------------------------------------------------------------ contatore a cartellini da scaffale 1-10
def stag(k, on, q=False):
    def mk():
        c = Cv(84, 104)
        fill = GOLD if on else (14, 52, 42)
        edge = (190, 140, 60) if on else SAGE_D
        c.poly([(3, 20), (81, 20), (81, 92), (42, 100), (3, 92)], fill=fill)
        c.line([3, 20, 81, 20, 81, 92, 42, 100, 3, 92, 3, 20], edge, 3)
        c.ell((34, 5, 50, 21), outline=edge, width=3)
        c.text((42, 58), "?" if q else str(k), FONT_SANS, 40, DARK if on else SAGE_D)
        return c.done()
    return cache(("stag12", k, on, q), mk)

def counter(img, t, lit, t0=0.0, y=190, q_others=False):
    a = seg(t, t0, 0.4)
    if a <= 0:
        return
    for k in range(1, 11):
        x = 540 + (k - 5.5) * 94
        lt = lit.get(k)
        on = lt is not None and t >= lt
        sc = 1.0
        if on:
            u = seg(t, lt, 0.4)
            sc = 1.0 + 0.3 * math.sin(math.pi * min(1.0, u))
        put(img, stag(k, on, q=(q_others and not on)), x, y - 26 * (1 - ease(a)) + (bob(t, 3, 0.6, k) if on else 0), scale=sc, alpha=ease(a), shadow=6)
        if on and lt is not None:
            bst(img, t, lt, x, y, n=7, dur=0.5, rad=80, seed=500 + k)

# ------------------------------------------------------------------ sprite
def spark_spr(S=120, col=GOLD):
    def mk():
        c = Cv(S, S)
        cx = cy = S / 2
        for k in range(6):
            a = math.radians(k * 60)
            ux, uy = math.cos(a), math.sin(a)
            nx, ny = -uy, ux
            r0, r1, hw = S * 0.10, S * 0.46, S * 0.055
            pts = [(cx + ux * r0 + nx * hw, cy + uy * r0 + ny * hw), (cx + ux * r1 + nx * hw, cy + uy * r1 + ny * hw),
                   (cx + ux * r1 - nx * hw, cy + uy * r1 - ny * hw), (cx + ux * r0 - nx * hw, cy + uy * r0 - ny * hw)]
            c.poly(pts, fill=col)
            c.ell((cx + ux * r1 - hw, cy + uy * r1 - hw, cx + ux * r1 + hw, cy + uy * r1 + hw), fill=col)
        return c.done()
    return cache(("spark12", S, col), mk)

def wordmark_spr():
    def mk():
        c = Cv(640, 150)
        c.rrect((3, 3, 637, 147), 36, fill=PAPER, outline=GOLD, width=6)
        c.text((250, 78), "WALMART", FONT_SANS, 74, INK, track=2)
        sp = spark_spr(96)
        c.im.paste(sp.resize((192, 192), Image.LANCZOS), (int(520 * 2), int(54 * 2) - 20), sp.resize((192, 192), Image.LANCZOS))
        return c.done()
    return cache("wordmark12", mk)

def browser12(n, state):
    word = "senior discount"
    def mk():
        c = Cv(940, 560)
        c.rrect((4, 4, 936, 556), 36, fill=PAPER, outline=GOLD, width=7)
        c.rrect((4, 4, 936, 96), 36, fill=(20, 60, 50))
        c.rrect((4, 60, 936, 96), 2, fill=(20, 60, 50))
        for i, col in enumerate((CORAL, GOLD, SAGE)):
            c.ell((34 + i * 40, 36, 58 + i * 40, 60), fill=col)
        c.text((520, 50), "WALMART OFFICIAL PAGES", FONT_SANS, 34, IVORY, track=2)
        c.rrect((40, 130, 900, 226), 48, fill=(236, 240, 232), outline=(150, 170, 156), width=4)
        c.ell((70, 152, 124, 206), outline=INK, width=8)
        c.line([112, 196, 134, 218], INK, 9)
        c.text((160, 178), word[:n] + ("|" if state == 0 and n < len(word) else ""), FONT_SANS, 54, INK, anchor="lm")
        if state >= 1:
            c.ell((330, 270, 520, 460), outline=(120, 140, 128), width=14)
            c.line([500, 440, 590, 530], (120, 140, 128), 20)
            c.line([382, 322, 468, 408], CORAL, 18); c.line([468, 322, 382, 408], CORAL, 18)
        return c.done()
    return cache(("browser12", n, state), mk)

def shopper_spr():
    def mk():
        c = Cv(240, 420)
        c.ell((70, 8, 170, 108), fill=SKIN, outline=(190, 150, 110), width=4)
        c.rrect((62, 4, 178, 50), 20, fill=(214, 214, 208))     # capelli
        c.rrect((40, 112, 200, 300), 40, fill=(60, 120, 190), outline=DARK, width=5)
        c.rrect((60, 292, 112, 412), 14, fill=(40, 60, 60)); c.rrect((128, 292, 180, 412), 14, fill=(40, 60, 60))
        c.line([196, 150, 232, 220], SKIN, 22)
        return c.done()
    return cache("shopper12", mk)

def cashier_spr(vest=GOLD):
    def mk():
        c = Cv(220, 400)
        c.ell((60, 8, 160, 108), fill=SKIN, outline=(190, 150, 110), width=4)
        c.rrect((52, 2, 168, 44), 22, fill=(70, 70, 76))
        c.rrect((30, 112, 190, 300), 36, fill=(70, 120, 190), outline=DARK, width=5)
        c.poly([(60, 112), (160, 112), (180, 300), (40, 300)], fill=vest)
        c.rrect((118, 156, 168, 190), 6, fill=PAPER)
        c.rrect((52, 292, 104, 396), 12, fill=(40, 60, 60)); c.rrect((116, 292, 168, 396), 12, fill=(40, 60, 60))
        return c.done()
    return cache(("cashier12", vest), mk)

def register_spr():
    def mk():
        c = Cv(420, 400)
        c.rrect((20, 170, 400, 390), 22, fill=(70, 110, 100), outline=DARK, width=6)
        c.rrect((8, 150, 412, 188), 14, fill=IVORY, outline=DARK, width=5)
        c.rrect((120, 36, 300, 150), 14, fill=(30, 44, 42), outline=DARK, width=6)
        c.rrect((136, 52, 284, 132), 8, fill=(30, 120, 88))
        for k in range(4):
            c.rrect((150, 66 + k * 16, 150 + 80 - (k % 2) * 30, 72 + k * 16), 3, fill=(170, 230, 190))
        c.rrect((60, 186, 160, 206), 6, fill=(120, 170, 190))
        for r in range(2):
            for q in range(5):
                c.rrect((196 + q * 38, 214 + r * 44, 226 + q * 38, 246 + r * 44), 6, fill=(150, 190, 176))
        c.rrect((300, 4, 380, 150), 6, fill=PAPER)                 # scontrino che esce
        for k in range(5):
            c.rrect((312, 22 + k * 22, 366 - (k % 2) * 22, 30 + k * 22), 3, fill=(180, 184, 172))
        return c.done()
    return cache("register12", mk)

def bubble12(w, h, bars=3, tail="r"):
    def mk():
        c = Cv(w, h + 44)
        c.rrect((3, 3, w - 3, h - 3), 38, fill=PAPER, outline=GOLD, width=5)
        if tail == "r":
            c.poly([(w - 120, h - 8), (w - 56, h - 8), (w - 36, h + 40)], fill=PAPER)
        else:
            c.poly([(56, h - 8), (120, h - 8), (40, h + 40)], fill=PAPER)
        n = bars
        for i in range(n):
            y = h / 2 + (i - (n - 1) / 2) * 44
            ww = (w - 120) - (i % 2) * 90
            c.rrect((60, y - 14, 60 + ww, y + 14), 8, fill=INK)
        return c.done()
    return cache(("bubble12", w, h, bars, tail), mk)

def lane_card(w, h, border, fill=None):
    def mk():
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 36, fill=fill or CARD, outline=border, width=6)
        return c.done()
    return cache(("lane12", w, h, border, fill), mk)

def check_spr(col=OKG, S=120):
    def mk():
        c = Cv(S, S)
        c.ell((3, 3, S - 3, S - 3), fill=col, outline=DARK, width=5)
        c.line([S * 0.26, S * 0.52, S * 0.43, S * 0.70, S * 0.76, S * 0.32], DARK, S * 0.11)
        return c.done()
    return cache(("check12", col, S), mk)

def cross_spr(col=CORAL, S=120):
    def mk():
        c = Cv(S, S)
        c.ell((3, 3, S - 3, S - 3), fill=col, outline=DARK, width=5)
        c.line([S * 0.32, S * 0.32, S * 0.68, S * 0.68], IVORY, S * 0.11)
        c.line([S * 0.68, S * 0.32, S * 0.32, S * 0.68], IVORY, S * 0.11)
        return c.done()
    return cache(("cross12", col, S), mk)

def calendar12_spr():
    def mk():
        c = Cv(340, 390)
        c.rrect((6, 6, 334, 384), 26, fill=PAPER, outline=DARK, width=6)
        c.rrect((6, 6, 334, 110), 26, fill=CORAL)
        c.rrect((6, 70, 334, 110), 2, fill=CORAL)
        c.ell((70, -2, 100, 28), fill=DARK); c.ell((240, -2, 270, 28), fill=DARK)
        c.text((170, 66), "DEADLINE", FONT_SANS, 46, IVORY, track=3)
        for r in range(4):
            for q in range(5):
                c.rrect((30 + q * 56, 138 + r * 58, 64 + q * 56, 176 + r * 58), 6, fill=(206, 212, 206))
        c.rrect((30 + 3 * 56, 138 + 2 * 58, 64 + 3 * 56, 176 + 2 * 58), 6, fill=(240, 190, 180))
        c.ell((190, 244, 268, 330), outline=CORAL, width=9)
        return c.done()
    return cache("cal12", mk)

def gift_spr():
    def mk():
        c = Cv(300, 300)
        c.rrect((30, 120, 270, 280), 14, fill=CORAL, outline=DARK, width=6)
        c.rrect((20, 84, 280, 138), 12, fill=(232, 130, 118), outline=DARK, width=6)
        c.rrect((130, 84, 170, 280), 4, fill=GOLD)
        c.ell((70, 18, 150, 96), outline=GOLD, width=16)
        c.ell((150, 18, 230, 96), outline=GOLD, width=16)
        c.ell((132, 66, 168, 100), fill=GOLD)
        return c.done()
    return cache("gift12", mk)

def pill_spr():
    def mk():
        c = Cv(300, 440)
        c.rrect((60, 10, 240, 90), 16, fill=IVORY, outline=DARK, width=6)
        for k in range(7):
            c.line([76 + k * 24, 20, 76 + k * 24, 80], (190, 190, 180), 4)
        c.rrect((44, 80, 256, 420), 30, fill=AMB, outline=(150, 90, 30), width=6)
        c.rrect((44, 80, 256, 120), 8, fill=(244, 170, 80))
        c.rrect((70, 170, 230, 340), 14, fill=PAPER)
        c.text((150, 232), "Rx", FONT_SANS, 74, CORAL)
        for k in range(3):
            c.rrect((92, 276 + k * 20, 208 - (k % 2) * 34, 286 + k * 20), 4, fill=(176, 180, 170))
        return c.done()
    return cache("pill12", mk)

def pillbox_cross():
    def mk():
        c = Cv(150, 150)
        c.ell((4, 4, 146, 146), fill=OKG, outline=DARK, width=6)
        c.rrect((60, 24, 90, 126), 6, fill=PAPER); c.rrect((24, 60, 126, 90), 6, fill=PAPER)
        return c.done()
    return cache("rxcross12", mk)

def badge20_spr():
    def mk():
        c = Cv(360, 440)
        c.poly([(110, 280), (60, 430), (130, 396), (170, 436), (190, 290)], fill=CORAL)
        c.poly([(250, 280), (300, 430), (230, 396), (190, 436), (170, 290)], fill=(180, 70, 62))
        c.ell((10, 10, 350, 350), fill=GOLD, outline=(190, 140, 60), width=10)
        c.ell((34, 34, 326, 326), outline=(190, 140, 60), width=4)
        for k in range(24):
            a = math.radians(k * 15)
            c.ell((180 + 150 * math.cos(a) - 5, 180 + 150 * math.sin(a) - 5, 180 + 150 * math.cos(a) + 5, 180 + 150 * math.sin(a) + 5), fill=(190, 140, 60))
        c.text((180, 150), "20", FONT_SANS, 170, DARK)
        c.text((180, 262), "YEARS", FONT_SANS, 62, DARK, track=6)
        return c.done()
    return cache("badge20", mk)

def ptag_spr(w, h, big, fill, ink, hole=True):
    def mk():
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 30, fill=fill, outline=(190, 140, 60) if fill == GOLD else SAGE_D, width=6)
        if hole:
            c.ell((26, h / 2 - 20, 66, h / 2 + 20), fill=(0, 0, 0, 0))
            c.ell((26, h / 2 - 20, 66, h / 2 + 20), outline=DARK, width=4)
        c.text(((w + 70) / 2, h / 2 + 4), big, FONT_SANS, int(h * 0.62), ink)
        return c.done()
    return cache(("ptag12", w, h, big, fill, ink), mk)

def neq_spr():
    def mk():
        c = Cv(130, 130)
        c.rrect((20, 34, 110, 52), 8, fill=CORAL); c.rrect((20, 78, 110, 96), 8, fill=CORAL)
        c.line([86, 14, 44, 116], CORAL, 16)
        return c.done()
    return cache("neq12", mk)

def aisle_spr():
    def mk():
        c = Cv(960, 330)
        c.rrect((3, 3, 957, 327), 32, fill=(8, 36, 29), outline=SAGE_D, width=5)
        c.rrect((20, 270, 940, 306), 8, fill=(30, 80, 64))
        for k in range(6):
            x = 36 + k * 150
            c.rrect((x, 150, x + 130, 262), 12, fill=(24, 74, 60), outline=SAGE_D, width=4)
            c.poly([(x - 6, 150), (x + 136, 150), (x + 120, 112), (x + 10, 112)], fill=(46, 104, 82) if k % 2 else (36, 90, 72))
            c.rrect((x + 30, 28, x + 100, 84), 8, fill=(14, 52, 42), outline=SAGE_D, width=4)
            c.line([x + 65, 84, x + 65, 112], SAGE_D, 4)
            c.text((x + 65, 58), "?", FONT_SANS, 46, SAGE)
        return c.done()
    return cache("aisle12", mk)

def vcard12_spr():
    def mk():
        c = Cv(940, 600)
        c.rrect((4, 4, 936, 596), 44, fill=CARD, outline=GOLD, width=7)
        c.rrect((30, 30, 910, 440), 28, fill=(22, 82, 64))
        for k in range(14):
            c.line([30 + k * 68, 30, 30 + k * 68 - 100, 440], (28, 96, 76), 6)
        c.ell((380, 60, 560, 240), fill=GOLD, outline=(190, 140, 60), width=6)
        c.poly([(444, 104), (444, 196), (520, 150)], fill=DARK)
        for k in range(10):
            x = 58 + k * 84
            c.poly([(x, 276), (x + 74, 276), (x + 74, 380), (x + 37, 392), (x, 380)], fill=GOLD)
            c.ell((x + 29, 262, x + 45, 278), outline=(190, 140, 60), width=3)
            c.text((x + 37, 332), str(k + 1), FONT_SANS, 40, DARK)
        c.text((470, 508), "ALL TEN IN ONE VIDEO", FONT_SANS, 58, GOLD, track=2)
        c.text((470, 566), "THE EXACT SENTENCE INSIDE", FONT_SANS, 28, SAGE, track=3)
        return c.done()
    return cache("vcard12", mk)

def pharmacy_spr():
    def mk():
        c = Cv(940, 420)
        c.rrect((4, 4, 936, 416), 40, fill=CARD, outline=OKG, width=7)
        c.rrect((30, 40, 450, 104), 18, fill=OKG)
        c.text((240, 74), "PHARMACY", FONT_SANS, 46, DARK, track=5)
        c.rrect((30, 300, 910, 400), 18, fill=(70, 110, 100), outline=DARK, width=5)
        c.rrect((22, 280, 918, 312), 12, fill=IVORY, outline=DARK, width=4)
        for k in range(4):
            c.rrect((60 + k * 44, 190, 92 + k * 44, 280), 5, fill=AMB)
            c.rrect((60 + k * 44, 178, 92 + k * 44, 194), 4, fill=IVORY)
        return c.done()
    return cache("pharm12", mk)

def receipt12(w, h):
    def mk():
        c = Cv(w, h + 30)
        c.rrect((0, 14, w, h), 10, fill=PAPER)
        for k in range(0, w, 30):
            c.poly([(k, 16), (k + 15, 0), (k + 30, 16)], fill=PAPER)
            c.poly([(k, h - 2), (k + 15, h + 24), (k + 30, h - 2)], fill=PAPER)
        return c.done()
    return cache(("receipt12", w, h), mk)

def barcode_spr(w=520, h=110):
    def mk():
        c = Cv(w, h)
        rnd = random.Random(3)
        x = 4
        while x < w - 12:
            bw = rnd.choice([4, 6, 10, 14])
            c.rrect((x, 4, x + bw, h - 4), 1, fill=INK)
            x += bw + rnd.choice([5, 8, 12])
        return c.done()
    return cache(("barcode12", w, h), mk)

# ------------------------------------------------------------------ B1 (286 f = 9,53 s)
def c1(img, t):
    _cur["b"] = 1
    lit = {k: T("ten things") + 0.1 * k for k in range(1, 11)}
    counter(img, t, lit, t0=T("But I did find") - 0.2, y=190)
    pp(img, t, 0.1, wordmark_spr(), 540, 330, sc=1.0, amp=4)
    # finestra del browser: scrittura della ricerca, poi nessun risultato
    s, al, aa = pop(t, 0.5, 0.5)
    if aa > 0:
        t_type0 = T("I searched") + 0.3
        t_end = T("senior discount")
        n = int(max(0.0, min(1.0, (t - t_type0) / max(0.4, (T("and I couldn't") - t_type0)))) * 15)
        state = 2 if t >= T("couldn't find") else (0 if n < 15 else 1)
        spr = browser12(n, 2 if state == 2 else 0)
        put(img, spr, 540 + bob(t, 4, 0.4, 0.5), 880 + bob(t, 6, 0.7), scale=min(1.0, s), alpha=al, shadow=14)
    if t >= T("couldn't find"):
        s2, al2, a2 = pop(t, T("couldn't find"), 0.45)
        put(img, stamp_spr("NO SENIOR DISCOUNT", 900, 120, CORAL), 540, 1290 + bob(t, 4, 0.6), scale=min(1.0, s2), alpha=al2, rot=-2, shadow=12)
        bst(img, t, T("couldn't find"), 540, 1290, n=10, color=CORAL, rad=220, seed=11)
    t10 = T("But I did find")
    s, al, a = pop(t, t10, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1550, scale=1.5, alpha=0.26 * al)
        put(img, ptag_spr(660, 230, "10", GOLD, DARK), 540 + bob(t, 4, 0.5, 2), 1520 + bob(t, 7, 0.6, 1), scale=min(1.0, s), alpha=al, shadow=14, rot=-2)
        bst(img, t, t10, 540, 1520, n=12, rad=300, seed=12)
    ptext(img, t, T("ten things") + 0.2, "THINGS WALMART WILL GIVE YOU", 1690, 48, IVORY, 8, track=1, maxw=960)
    ptext(img, t, T("if you know how to ask"), "IF YOU KNOW HOW TO ASK", 1760, 50, GOLD, 8, track=2, maxw=960)

# ------------------------------------------------------------------ B2 (316 f = 10,53 s)
def c2(img, t):
    _cur["b"] = 2
    counter(img, t, {1: T("One of them") + 0.2}, t0=0.0, y=190)
    ptext(img, t, T("One of them"), "AT THE REGISTER", 290, 70, GOLD, 10, track=4)
    t_scene = T("a rule at the register")
    s, al, a = pop(t, t_scene - 0.2, 0.55)
    if a > 0:
        put(img, lane_card(960, 600, GOLD), 540, 700, scale=min(1.0, s), alpha=al, shadow=14)
        k = min(1.0, s)
        put(img, shopper_spr(), 540 - 330 * k, 740 + bob(t, 4, 0.6), scale=0.92 * k, alpha=al)
        put(img, register_spr(), 540 + 30 * k, 750, scale=0.95 * k, alpha=al)
        put(img, cashier_spr(), 540 + 330 * k, 740 + bob(t, 4, 0.6, 1.5), scale=0.9 * k, alpha=al)
    t_sp = T("only works if you speak up")
    s, al, a = pop(t, t_sp, 0.5)
    if a > 0:
        put(img, bubble12(380, 150, 2, "l"), 250 + bob(t, 3, 0.5), 520 + bob(t, 6, 0.8), scale=min(1.0, s), alpha=al, shadow=10)
        bst(img, t, t_sp, 290, 520, n=8, rad=150, seed=21)
    ptext(img, t, t_sp + 0.1, "ONLY IF YOU SPEAK UP", 1150, 64, IVORY, 10, track=2, maxw=960)
    t_pol = T("Walmart's own policy")
    s, al, a = pop(t, t_pol, 0.5)
    if a > 0:
        put(img, stamp_spr("WALMART'S OWN POLICY", 860, 100, GOLD), 540, 1280 + bob(t, 4, 0.6), scale=min(1.0, s), alpha=al, rot=-1.5, shadow=10)
    t_c = T("on the customer")
    s, al, a = pop(t, t_c, 0.5)
    if a > 0:
        put(img, lane_card(440, 360, OKG), 300, 1580, scale=min(1.0, s), alpha=al, shadow=12)
        put(img, shopper_spr(), 300, 1560 + bob(t, 4, 0.6), scale=0.42 * min(1.0, s), alpha=al)
        put(img, check_spr(), 300, 1695 + bob(t, 3, 0.7), scale=0.7 * min(1.0, s), alpha=al, shadow=6)
        xtext(img, t, t_c + 0.2, "CUSTOMER", 300, 1435, 40, OKG, track=2, maxw=400)
        bst(img, t, t_c, 300, 1580, n=9, color=OKG, rad=180, seed=22)
    t_s = T("not the store")
    s, al, a = pop(t, t_s, 0.5)
    if a > 0:
        put(img, lane_card(440, 360, CORAL), 780, 1580, scale=min(1.0, s), alpha=al, shadow=12)
        put(img, cashier_spr(), 780, 1560 + bob(t, 4, 0.6, 1), scale=0.42 * min(1.0, s), alpha=al)
        put(img, cross_spr(), 780, 1695 + bob(t, 3, 0.7, 1), scale=0.7 * min(1.0, s), alpha=al, shadow=6)
        xtext(img, t, t_s + 0.2, "STORE", 780, 1435, 40, CORAL, track=2, maxw=400)

# ------------------------------------------------------------------ B3 (134 f = 4,47 s)
def c3(img, t):
    _cur["b"] = 3
    counter(img, t, {2: T("Another") + 0.15}, t0=0.0, y=190)
    pp(img, t, 0.2, calendar12_spr(), 540, 700, sc=1.5, amp=6, shadow=14, rot=-3)
    t_d = T("a deadline")
    ptext(img, t, t_d, "A DEADLINE", 1080, 92, GOLD, 12, track=4)
    t_s = T("this season")
    ptext(img, t, t_s, "THIS SEASON", 1190, 84, IVORY, 10, track=4)
    t_g = T("buy a gift")
    s, al, a = pop(t, t_g, 0.45)
    if a > 0:
        put(img, glow_spr(), 540, 1480, scale=1.2, alpha=0.24 * al)
        put(img, gift_spr(), 540 + bob(t, 3, 0.5), 1450 + bob(t, 7, 0.8), scale=1.3 * min(1.0, s), alpha=al, shadow=12, rot=-4)
        bst(img, t, t_g, 540, 1470, n=9, rad=200, seed=31, dur=0.4)
    ptext(img, t, t_g + 0.1, "WHEN TO BUY A GIFT", 1690, 56, GOLD, 8, track=2, maxw=960)

# ------------------------------------------------------------------ B4 (287 f = 9,57 s)
def c4(img, t):
    _cur["b"] = 4
    counter(img, t, {9: T("two of them") + 0.1, 10: T("two of them") + 0.45}, t0=0.0, y=190)
    t_a = T("And two of them")
    ptext(img, t, t_a, "TWO OF THEM", 290, 70, GOLD, 10, track=4)
    pp(img, t, T("your medicine") - 0.3, pill_spr(), 500, 650, sc=1.15, amp=6, shadow=14, rot=-3)
    s, al, a = pop(t, T("your medicine"), 0.45)
    if a > 0:
        put(img, pillbox_cross(), 850, 560 + bob(t, 4, 0.6), scale=0.9 * min(1.0, s), alpha=al, shadow=8)
    ptext(img, t, T("your medicine"), "YOUR MEDICINE", 990, 66, IVORY, 10, track=3)
    t_y = T("One program")
    s, al, a = pop(t, t_y, 0.55)
    if a > 0:
        put(img, glow_spr(), 540, 1260, scale=1.4, alpha=0.22 * al)
        put(img, badge20_spr(), 540 + bob(t, 3, 0.4), 1260 + bob(t, 6, 0.7), scale=0.85 * min(1.0, s), alpha=al, shadow=12, rot=-3 * (1 - ease(a)))
        bst(img, t, t_y, 540, 1260, n=10, rad=240, seed=41)
    t_h = T("but the price in the headline")
    s, al, a = pop(t, t_h, 0.5)
    if a > 0:
        put(img, ptag_spr(380, 190, "?", GOLD, DARK), 250, 1600 + bob(t, 5, 0.7), scale=min(1.0, s), alpha=al, shadow=12, rot=-3)
    xtext(img, t, t_h + 0.15, "PRICE IN THE HEADLINE", 250, 1730, 36, GOLD, track=1, maxw=420)
    t_p = T("is not always")
    s, al, a = pop(t, t_p, 0.5)
    if a > 0:
        put(img, neq_spr(), 540, 1600, scale=min(1.0, s), alpha=al, shadow=8)
    t_y2 = T("the price you pay")
    s, al, a = pop(t, t_y2, 0.5)
    if a > 0:
        put(img, ptag_spr(380, 190, "?", PAPER, INK), 830, 1600 + bob(t, 5, 0.7, 1.5), scale=min(1.0, s), alpha=al, shadow=12, rot=3)
    xtext(img, t, t_y2 + 0.15, "PRICE YOU PAY", 830, 1730, 36, IVORY, track=1, maxw=420)

# ------------------------------------------------------------------ B5 (165 f = 5,5 s)
def c5(img, t):
    _cur["b"] = 5
    q = {1: 0.0, 2: 0.0, 9: 0.0, 10: 0.0}
    counter(img, t, q, t0=0.0, y=190, q_others=True)
    ptext(img, t, 0.2, "FOUR OF TEN", 320, 110, GOLD, 12, track=4)
    # griglia 5x2: 4 accesi, 6 con ?
    ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lit_ids = {1, 2, 9, 10}
    size_w, size_h, gx, gy = 150, 186, 36, 20
    x0 = 540 - 2 * (size_w + gx)
    for i, k in enumerate(ids):
        r, qn = divmod(i, 5)
        cx, cy = x0 + qn * (size_w + gx), 590 + r * (size_h + gy)
        on = k in lit_ids
        ti = (0.45 + 0.07 * i) if on else (T("The other six") + 0.05 * i)
        a = seg(t, ti, 0.35)
        if a <= 0:
            continue
        sp = stag(k, on, q=not on)
        put(img, sp, cx, cy + (bob(t, 4, 0.7, i) if on else 0), scale=1.8 * (0.6 + 0.4 * ease(a)), alpha=ease(a), shadow=8)
    ptext(img, t, T("The other six"), "THE OTHER SIX", 1015, 60, IVORY, 8, track=3)
    t_sp = T("spread across")
    s, al, a = pop(t, t_sp, 0.5)
    if a > 0:
        put(img, aisle_spr(), 540, 1290, scale=min(1.0, s), alpha=al, shadow=12)
    xtext(img, t, t_sp + 0.1, "DIFFERENT COUNTERS", 540, 1495, 46, GOLD, track=3, maxw=900)
    # chi passa davanti ai banconi senza fermarsi
    tw0 = T("so it's easy")
    a = seg(t, tw0, 0.4)
    if a > 0:
        u = seg(t, tw0, min(1.7, D() * 0.8 - tw0 - 0.05))
        x = 110 + 820 * ease(u)
        put(img, shopper_spr(), x, 1305 + 5 * math.sin(u * 40) * (1 - u), scale=0.52, alpha=ease(a), shadow=6)
    ptext(img, t, T("walk right past"), "WALK RIGHT PAST THEM", 1660, 62, CORAL, 8, track=2, maxw=960)

# ------------------------------------------------------------------ B6 (243 f = 8,1 s)
def c6(img, t):
    _cur["b"] = 6
    counter(img, t, {k: T("all ten") + 0.08 * k for k in range(1, 11)}, t0=0.0, y=190)
    pp(img, t, 0.35, vcard12_spr(), 540, 600, sc=1.0, amp=6, shadow=18, rot=-2)
    bst(img, t, 0.35, 540, 600, n=12, rad=440, seed=61)
    t_s = T("the exact sentence")
    s, al, a = pop(t, t_s - 0.25, 0.5)
    if a > 0:
        put(img, pharmacy_spr(), 540, 1130, scale=min(1.0, s), alpha=al, shadow=14)
        put(img, cashier_spr(vest=OKG), 790 * 1.0, 1070 + bob(t, 3, 0.6), scale=0.6 * min(1.0, s), alpha=al)
    s, al, a = pop(t, t_s, 0.5)
    if a > 0:
        put(img, bubble12(420, 190, 3, "l"), 290, 1000 + bob(t, 6, 0.8), scale=min(1.0, s) * 0.95, alpha=al, shadow=10)
        bst(img, t, t_s, 290, 1000, n=8, rad=170, seed=62)
    xtext(img, t, t_s + 0.1, "AT THE PHARMACY COUNTER", 540, 1380, 40, GOLD, track=2, maxw=920)
    ptext(img, t, T("right below"), "RIGHT BELOW", 1520, 100, GOLD, 12, track=4)
    ptext(img, t, T("Tap it now"), "TAP IT NOW", 1620, 84, IVORY, 10, track=4)
    for k in range(3):
        a = seg(t, T("Tap it now") + 0.1 * k, 0.3)
        if a > 0:
            put(img, chevron_spr(), 540, 1710 + k * 40 + 14 * (1 - ease(a)), alpha=ease(a) * (1 - 0.25 * k), scale=0.5)

# ------------------------------------------------------------------ B7 (207 f = 6,9 s)
def c7(img, t):
    _cur["b"] = 7
    tl = T("like this short"); ts_ = T("subscribe"); tm = T("so you don't miss")
    a = seg(t, 0.15, 0.7)
    h = 1180
    if a > 0:
        put(img, receipt12(880, h), 540 + bob(t, 4, 0.35), 960 - 160 * (1 - ease(a)) + bob(t, 5, 0.6), alpha=ease(a), shadow=18)
    if t > 0.7:
        ptext(img, t, 0.7, "THE SENIOR ADVANTAGE", 440, 52, INK, 0, track=3, maxw=800)
        a2 = seg(t, 0.9, 0.4)
        if a2 > 0:
            put(img, barcode_spr(700, 90), 540, 1480, alpha=ease(a2))
    # riga 1: mi piace
    s, al, a = pop(t, tl, 0.45)
    if a > 0:
        put(img, thumb_spr(), 230, 700, scale=0.85 * min(1.0, s), alpha=al, shadow=8, rot=-4)
        xtext(img, t, tl + 0.1, "LIKE THIS SHORT", 650, 700, 58, INK, shadow=0, maxw=520)
        bst(img, t, tl, 230, 700, n=9, rad=130, seed=71, dur=0.45)
    # riga 2: iscriviti
    s, al, a = pop(t, ts_, 0.5)
    if a > 0:
        put(img, channel11_spr(t >= ts_ + 0.9), 540 + bob(t, 2, 0.5), 1000 + bob(t, 4, 0.7, 1), scale=0.93 * min(1.0, s), alpha=al, shadow=10)
    if t >= ts_ + 0.9:
        bst(img, t, ts_ + 0.9, 540, 1040, n=10, rad=200, seed=72, dur=0.45)
    ah = seg(t, ts_ + 0.3, 0.6)
    if 0 < ah and t < ts_ + 1.3:
        u = ease(min(1.0, ah))
        put(img, hand_spr(), 630 + 60 * (1 - u), 1145 + 120 * (1 - u), scale=0.55, alpha=min(1.0, ah * 3))
    # riga 3: non perdere il prossimo
    s, al, a = pop(t, tm, 0.45)
    if a > 0:
        put(img, bell_spr(), 230, 1320, scale=0.75 * min(1.0, s), alpha=al, shadow=8, rot=(10 * math.sin((t - tm) * 14) * max(0.0, 1 - (t - tm) / 0.8)))
        xtext(img, t, tm + 0.1, "DON'T MISS THE NEXT ONE", 660, 1320, 46, INK, shadow=0, maxw=560)

SCENES12 = {1: c1, 2: c2, 3: c3, 4: c4, 5: c5, 6: c6, 7: c7}
DRAW = SCENES12
DUR12 = DUR

if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or sorted(SCENES12)
    out_dir = os.environ.get("S12_OUT", "short12")
    os.makedirs(out_dir, exist_ok=True)
    for k in ks:
        _cur["b"] = k
        render12(zoomed(SCENES12[k]), DUR[k], f"{out_dir}/SA-walmart-short-blocco{k:02d}.mp4")
