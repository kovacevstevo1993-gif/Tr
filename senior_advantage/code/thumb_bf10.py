"""Miniature video lungo 10 (BLACK FRIDAY: resi e price match), 2 versioni diverse per il test A/B. 1280x720.
Ordine utente 04/11/2026: "2 attira click, professionali e piu realistiche" (stesse regole del 23/10: oggetti lucidi, ombre, profondita,
curiosita con barre nere + cerchio e freccia rossi, colori accesi, logo vero preso dai siti ufficiali).
Loghi VERI (riferimenti/walmart/, riferimenti/logos_bf/): Walmart (parola + spark da corporate.walmart.com), Target (bullseye da
corporate.target.com), Costco (customerservice.costco.com).
Realismo: carta termica con grana, bordi a dente, ombra morbida + ombra di contatto, prospettiva, curvatura, bokeh sfocato dietro,
grana di pellicola; cartellino di cartone con occhiello metallico, spago, riflesso.
A = blu: scontrino realistico con righe coperte da barre nere, la riga "RETURN BY" cerchiata e freccia rossa, "LAST DAY TO RETURN?",
    targhetta rossa "BLACK FRIDAY", striscia bianca con i loghi Walmart / Target / Costco.
B = nero-giallo (nastro di avvertimento): logo Walmart, cartellino rosso "BLACK FRIDAY DEAL walmart.com" con divieto, "NO PRICE MATCH",
    targhetta rossa "WALMART'S OWN PAGE", striscia bianca "RETURN + PRICE MATCH RULES".
Tutte le scritte sono vere e dette nel video: la pagina di Walmart elenca tra cio che non pareggia i prezzi walmart.com delle offerte
speciali, Black Friday e Cyber Monday compresi (pagina del 2023, detto nel video).
uso: OUT=cartella python3 thumb_bf10.py"""
import os, math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageFont
from thumb_long9 import *            # F, rot, canvas, done, comp, sp, text3d, sheen, vgrad, glow, vignette, red_ring, fat_arrow, colori, W, H, SS
import cairosvg

OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/miniature")
os.makedirs(OUT, exist_ok=True)
HERE = os.path.dirname(os.path.abspath(__file__))
REFW = os.path.join(HERE, "..", "riferimenti", "walmart")
REFL = os.path.join(HERE, "..", "riferimenti", "logos_bf")
WBLUE = (0, 83, 226); WYEL = (255, 194, 32)
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
RNG = np.random.default_rng(7)


# ------------------------------------------------------------------ loghi veri
def spark(size):
    p = f"/tmp/_spark_{size}.png"
    cairosvg.svg2png(url=os.path.join(REFW, "spark.svg"), write_to=p, output_width=size)
    return Image.open(p).convert("RGBA")


def wordmark(height, col):
    w = Image.open(os.path.join(REFW, "us.png")).convert("RGBA").crop((0, 0, 483, 104))
    w = w.crop(w.getbbox())
    out = Image.new("RGBA", w.size, col + (255,)); out.putalpha(w.getchannel("A"))
    return out.resize((int(w.width * height / w.height), height), Image.LANCZOS)


def walmart_logo(h):
    """parola Walmart blu + spark giallo, senza sfondo"""
    wm = wordmark(int(h * 0.62), WBLUE); sp_ = spark(int(h * 0.70))
    lay = Image.new("RGBA", (wm.width + sp_.width + int(h * 0.12), h), (0, 0, 0, 0))
    lay.alpha_composite(wm, (0, (h - wm.height) // 2 + 2))
    lay.alpha_composite(sp_, (wm.width + int(h * 0.12), (h - sp_.height) // 2))
    return lay


def target_logo(h):
    im = Image.open(os.path.join(REFL, "target_bullseye.png")).convert("RGBA")
    return im.resize((int(im.width * h / im.height), h), Image.LANCZOS)


def costco_logo(h):
    im = Image.open(os.path.join(REFL, "costco_logo.png")).convert("RGBA")
    a = np.asarray(im).copy()
    # il PNG e a palette con bianco opaco: il bianco diventa trasparente (resta il logo rosso e blu)
    white = (a[..., 0] > 245) & (a[..., 1] > 245) & (a[..., 2] > 245)
    a[white, 3] = 0
    im = Image.fromarray(a)
    im = im.crop(im.getbbox())
    return im.resize((int(im.width * h / im.height), h), Image.LANCZOS)


# ------------------------------------------------------------------ realismo: grana, ombre, bokeh
def grain(im, amt=7):
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    n = RNG.normal(0, amt, a.shape[:2])[..., None]
    return Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))


def drop(im, lay, xy, far=(30, 40), far_blur=26, far_a=150, near=(5, 8), near_blur=5, near_a=130, col=(0, 0, 0)):
    """ombra morbida lontana + ombra di contatto vicina, poi l'oggetto"""
    base = im.convert("RGBA")
    for off, bl, al in ((far, far_blur, far_a), (near, near_blur, near_a)):
        sh = Image.new("RGBA", base.size, (0, 0, 0, 0))
        solid = Image.new("RGBA", lay.size, col + (al,))
        sh.paste(solid, (int(xy[0] + off[0]), int(xy[1] + off[1])), lay.split()[3])
        base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(bl)))
    comp(base, lay, xy)
    return base.convert("RGB")


def bokeh_bg(c_top, c_bot, lights, seed=3, n=46, blur_big=14):
    """sfondo sfumato con luci fuori fuoco (profondita di campo)"""
    rnd = random.Random(seed)
    im = vgrad(c_top, c_bot, ang=90)
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for _ in range(n):
        r = rnd.choice((18, 26, 38, 54, 78)); x = rnd.randint(-20, W + 20); y = rnd.randint(-20, H + 20)
        col = rnd.choice(lights); a = rnd.randint(34, 90)
        d.ellipse([x - r, y - r, x + r, y + r], fill=col + (a,))
        d.ellipse([x - r, y - r, x + r, y + r], outline=tuple(min(255, c + 40) for c in col) + (min(255, a + 40),), width=2)
    lay = lay.filter(ImageFilter.GaussianBlur(blur_big))
    base = im.convert("RGBA"); base.alpha_composite(lay)
    return base.convert("RGB")


def perspective(lay, top_squeeze=0.06, left_squeeze=0.0):
    """leggera prospettiva: la parte alta si restringe (foto dall'alto)"""
    w, h = lay.size
    dx = w * top_squeeze
    dy = h * left_squeeze
    src = [(dx, dy), (w - dx, 0), (w, h), (0, h - dy)]       # angoli dell'immagine sorgente da cui prendere (alto-sx, alto-dx, basso-dx, basso-sx)
    # PIL vuole i coefficienti per mappare destinazione -> sorgente
    dst = [(0, 0), (w, 0), (w, h), (0, h)]
    A = []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
    B = [c for p in src for c in p]
    coef = np.linalg.solve(np.array(A, dtype=np.float64), np.array(B, dtype=np.float64))
    return lay.transform((w, h), Image.PERSPECTIVE, tuple(coef), resample=Image.BICUBIC)


# ------------------------------------------------------------------ scontrino termico realistico
def thermal_receipt(w=470, h=900, rows=None, ang=-7):
    """rows: lista di (testo_sinistra, 'bar'|None, evidenziata). Ritorna (immagine RGBA, dict con la posizione della riga RETURN BY)"""
    S = 2
    W2, H2 = w * S, h * S
    # carta: bianco caldo + grana + variazione lenta
    base = np.full((H2, W2, 3), (251, 249, 244), np.float32)
    base += RNG.normal(0, 2.4, (H2, W2, 1))
    low = RNG.normal(0, 1, (H2 // 40 + 2, W2 // 40 + 2))
    low = np.asarray(Image.fromarray(low.astype(np.float32)).resize((W2, H2), Image.BICUBIC))
    base += low[..., None] * 2.6
    paper = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).convert("RGBA")
    d = ImageDraw.Draw(paper)
    # testo a stampa termica
    f = ImageFont.truetype(MONO, 30 * S)
    f_big = ImageFont.truetype(MONO, 40 * S)
    ink = Image.new("L", (W2, H2), 0); di = ImageDraw.Draw(ink)
    bars = Image.new("L", (W2, H2), 0); db = ImageDraw.Draw(bars)
    y = 78 * S
    pos = {}
    for txt, bar, hl in rows:
        if txt == "---":
            di.text((w * S / 2, y), "-" * 21, font=f, fill=200, anchor="mm")
            y += 38 * S; continue
        if txt.startswith("##"):
            di.text((w * S / 2, y), txt[2:], font=f_big, fill=235, anchor="mm")
            y += 62 * S; continue
        di.text((34 * S, y), txt, font=f, fill=235, anchor="lm")
        if bar:
            x0 = 34 * S + int(f.getlength(txt)) + 10 * S
            x1 = (w - 30) * S
            wob = lambda: RNG.integers(-2 * S, 2 * S + 1)
            db.rounded_rectangle([x0 + wob(), y - 21 * S + wob(), x1 + wob(), y + 21 * S + wob()], radius=5 * S, fill=255)
            if hl:
                pos = {"y": y / S, "x0": 34, "x1": w - 30}
        y += 58 * S
    # barcode
    bx = 40 * S
    while bx < (w - 40) * S:
        wd = int(RNG.integers(2, 7)) * S
        di.rectangle([bx, y + 6 * S, bx + wd, y + 96 * S], fill=225)
        bx += wd + int(RNG.integers(2, 6)) * S
    ink_f = ink.filter(ImageFilter.GaussianBlur(0.9 * S / 2))
    dark = Image.new("RGBA", (W2, H2), (38, 38, 44, 255))
    paper.paste(dark, (0, 0), ink_f.point(lambda v: int(v * 0.92)))
    # barre nere di copertura (pennarello: nere, opache, con un filo di riflesso)
    marker = Image.new("RGBA", (W2, H2), (10, 10, 12, 255))
    paper.paste(marker, (0, 0), bars)
    gl = ImageChops.multiply(bars.filter(ImageFilter.GaussianBlur(2)), Image.new("L", (W2, H2), 28))
    paper.paste(Image.new("RGBA", (W2, H2), (255, 255, 255, 255)), (0, 0), gl.point(lambda v: int(v * 0.5)))
    # ombreggiatura: bordi piu scuri + onda di curvatura
    xs = np.linspace(-1, 1, W2)[None, :]; ys = np.linspace(0, 1, H2)[:, None]
    shade = 1 - 0.13 * np.abs(xs) ** 2.2 - 0.035 * (0.5 + 0.5 * np.sin(ys * 9.5 + 0.8)) + 0.02 * ys
    a = np.asarray(paper).astype(np.float32)
    a[..., :3] *= shade[..., None]
    paper = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    # forma con bordi a dente in alto e in basso
    mask = Image.new("L", (W2, H2), 0); dm = ImageDraw.Draw(mask)
    t = 16 * S
    pts = [(0, t)]
    for i in range(0, W2 + t, t):
        pts += [(i, 0), (i + t // 2, t)]
    pts += [(W2, H2 - t)]
    for i in range(W2, -t, -t):
        pts += [(i, H2), (i - t // 2, H2 - t)]
    dm.polygon(pts, fill=255)
    out = paper.convert("RGBA"); out.putalpha(mask)
    out = out.resize((w, h), Image.LANCZOS)
    out = perspective(out, top_squeeze=0.045)
    out = rot(out, ang)
    return out, pos


def thumb_a():
    im = bokeh_bg((8, 72, 200), (0, 20, 84), [(255, 214, 80), (255, 255, 255), (120, 190, 255), (255, 120, 60)], seed=11)
    im = glow(im, 330, 330, 360, (30, 120, 255), 120)
    im = vignette(im, 110)
    # scontrino a sinistra
    rows = [("##BLACK FRIDAY", None, False), ("---", None, False),
            ("ITEM 1", "bar", False), ("ITEM 2", "bar", False), ("ITEM 3", "bar", False), ("---", None, False),
            ("TAX", "bar", False), ("TOTAL", "bar", False), ("---", None, False),
            ("RETURN BY:", "bar", True), ("---", None, False), ("THANK YOU!", None, False)]
    rc, pos = thermal_receipt(470, 840, rows, ang=-6)
    rx, ry = 36, -14
    im = drop(im, rc, (rx, ry), far=(34, 44), far_blur=28, far_a=165)
    # la riga RETURN BY (misurata sul risultato): cerchio rosso e freccia
    ring = red_ring(528, 128, col=(236, 28, 36), wd=11)
    im = sp(im, ring, (34, 510), off=(4, 7), blur=7, alpha=150)
    # testi
    im = sp(im, banner("BLACK FRIDAY", 600, 92, 60), (630, 30), off=(6, 10), blur=9, alpha=150)
    im = text3d(im, (935, 218), "LAST DAY", 124, (255, 214, 28), (170, 90, 0), stroke=16, dep=14)
    im = text3d(im, (935, 352), "TO RETURN?", 90, (255, 255, 255), (60, 70, 120), stroke=14, dep=12)
    arr = fat_arrow(250, 116, (236, 28, 36), ang=178)
    im = sp(im, arr, (586, 452), off=(5, 9), blur=8, alpha=150)
    # striscia bianca con i tre loghi veri
    im = logos_strip(im, 600, 570, 660, 128)
    return grain(sheen_all(im), 6)


def banner(text, w, h, size):
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=16, fill=(228, 24, 36, 255), outline=BLK, width=6)
    d.rounded_rectangle([8, 8, w - 9, h // 2], radius=12, fill=(255, 255, 255, 38))
    d.text((w / 2, h / 2 + 3), text, font=F(size, "Black"), fill=(255, 255, 255), anchor="mm")
    return lay


def logos_strip(im, x, y, w, h):
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=24, fill=(255, 255, 255, 255), outline=BLK, width=7)
    d.rounded_rectangle([10, 10, w - 11, h // 2 - 4], radius=16, fill=(235, 242, 255, 255))
    wl = walmart_logo(62); tl = target_logo(86); cl = costco_logo(54)
    gap = (w - wl.width - tl.width - cl.width) // 4
    xx = gap
    for lg in (wl, tl, cl):
        lay.alpha_composite(lg, (xx, (h - lg.height) // 2)); xx += lg.width + gap
    # separatori
    for sx in (gap + wl.width + gap // 2, gap + wl.width + gap + tl.width + gap // 2):
        d.line([(sx, 26), (sx, h - 26)], fill=(200, 206, 216), width=3)
    return drop(im, lay, (x, y), far=(10, 16), far_blur=14, far_a=120, near=(3, 5), near_blur=3, near_a=110)


def sheen_all(im):
    return im


# ------------------------------------------------------------------ cartellino di cartone realistico
def hang_tag(w=400, h=420, ang=8):
    S = 2
    W2, H2 = w * S, h * S
    top = 100 * S
    shape = [(58 * S, top), (118 * S, 22 * S), (W2 - 118 * S, 22 * S), (W2 - 58 * S, top), (W2 - 8 * S, H2 - 8 * S), (8 * S, H2 - 8 * S)]
    mask = Image.new("L", (W2, H2), 0); ImageDraw.Draw(mask).polygon(shape, fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(1.2))
    ys = np.linspace(0, 1, H2)[:, None, None]
    c0 = np.array([255, 222, 52], np.float32); c1 = np.array([238, 168, 0], np.float32)
    arr = c0 * (1 - ys) + c1 * ys
    arr = np.broadcast_to(arr, (H2, W2, 3)).copy()
    arr += RNG.normal(0, 3.2, (H2, W2, 1))
    card = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA")
    card.putalpha(mask)
    dc = ImageDraw.Draw(card)
    inner = [(72 * S, top + 16 * S), (124 * S, 38 * S), (W2 - 124 * S, 38 * S), (W2 - 72 * S, top + 16 * S), (W2 - 24 * S, H2 - 24 * S), (24 * S, H2 - 24 * S)]
    dc.line(inner + [inner[0]], fill=(20, 20, 24, 235), width=4 * S, joint="curve")
    dc.text((W2 / 2, 198 * S), "BLACK", font=F(84 * S, "Black"), fill=(18, 18, 22), anchor="mm")
    dc.text((W2 / 2, 282 * S), "FRIDAY", font=F(84 * S, "Black"), fill=(226, 24, 36), anchor="mm")
    dc.rounded_rectangle([46 * S, 336 * S, W2 - 46 * S, 392 * S], radius=12 * S, fill=(0, 83, 226, 255))
    dc.text((W2 / 2, 365 * S), "walmart.com DEAL", font=F(30 * S, "ExtraBold"), fill=(255, 255, 255), anchor="mm")
    lay = card
    cx, cy = W2 / 2, 84 * S
    hole = Image.new("RGBA", (W2, H2), (0, 0, 0, 0)); dh = ImageDraw.Draw(hole)
    dh.ellipse([cx - 36 * S, cy - 36 * S, cx + 36 * S, cy + 36 * S], fill=(176, 182, 190, 255), outline=(90, 96, 104, 255), width=3 * S)
    dh.arc([cx - 36 * S, cy - 36 * S, cx + 36 * S, cy + 36 * S], 200, 290, fill=(255, 255, 255, 230), width=5 * S)
    hole_cut = Image.new("L", (W2, H2), 255); ImageDraw.Draw(hole_cut).ellipse([cx - 23 * S, cy - 23 * S, cx + 23 * S, cy + 23 * S], fill=0)
    lay.putalpha(ImageChops.multiply(lay.getchannel("A"), hole_cut))
    dh.ellipse([cx - 23 * S, cy - 23 * S, cx + 23 * S, cy + 23 * S], fill=(0, 0, 0, 0))
    lay.alpha_composite(hole)
    gl = Image.new("L", (W2, H2), 0)
    ImageDraw.Draw(gl).polygon([(0, H2 * 0.05), (W2 * 0.62, 0), (W2 * 0.82, 0), (0, H2 * 0.62)], fill=70)
    gl = gl.filter(ImageFilter.GaussianBlur(18 * S))
    lay.paste(Image.new("RGBA", (W2, H2), (255, 255, 255, 255)), (0, 0), ImageChops.multiply(gl, lay.getchannel("A")))
    cord = Image.new("RGBA", (W2, H2), (0, 0, 0, 0)); dd = ImageDraw.Draw(cord)
    pts = []
    for i in range(0, 41):
        u = i / 40
        pts.append((cx + (-56 * math.sin(u * math.pi * 1.1)) * S, cy - 8 * S - u * 110 * S * 0.9))
    dd.line(pts, fill=(222, 196, 148, 255), width=9 * S, joint="curve")
    dd.line([(x + 2 * S, y + 2 * S) for x, y in pts], fill=(160, 130, 90, 200), width=3 * S, joint="curve")
    lay = lay.resize((w, h), Image.LANCZOS)
    cord = cord.resize((w, h), Image.LANCZOS)
    lay.alpha_composite(cord)
    lay = perspective(lay, top_squeeze=0.03)
    return rot(lay, ang)


def prohibition(d_px, col=(236, 28, 36)):
    S = 2
    n = d_px * S
    lay = Image.new("RGBA", (n, n), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    m = int(n * 0.07); wd = int(n * 0.13)
    d.ellipse([m, m, n - m, n - m], outline=(255, 255, 255, 255), width=wd + 12 * S)
    d.ellipse([m, m, n - m, n - m], outline=col + (255,), width=wd)
    a = math.radians(45); c = n / 2; r = n / 2 - m
    p0 = (c - r * math.cos(a), c - r * math.sin(a)); p1 = (c + r * math.cos(a), c + r * math.sin(a))
    d.line([p0, p1], fill=(255, 255, 255, 255), width=wd + 12 * S)
    d.line([p0, p1], fill=col + (255,), width=wd)
    return lay.resize((d_px, d_px), Image.LANCZOS)


def caution_tape(im, y, h, ang=-5):
    S = 1
    lay = Image.new("RGBA", (W + 600, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rectangle([0, 0, W + 600, h], fill=(255, 205, 0, 255))
    for x in range(-h, W + 700, 70):
        d.polygon([(x, h), (x + 36, h), (x + 36 + h, 0), (x + h, 0)], fill=(18, 18, 20, 255))
    lay = rot(lay, ang)
    base = im.convert("RGBA")
    shadow = Image.new("RGBA", lay.size, (0, 0, 0, 0)); shadow.paste(Image.new("RGBA", lay.size, (0, 0, 0, 150)), (0, 0), lay.split()[3])
    base.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(9)), (-300 + 6, y + 10))
    comp(base, lay, (-300, y))
    return base.convert("RGB")


def thumb_b():
    im = bokeh_bg((226, 34, 44), (96, 0, 12), [(255, 214, 60), (255, 255, 255), (255, 150, 40)], seed=5, n=44)
    im = glow(im, 400, 360, 380, (255, 90, 70), 150)
    im = vignette(im, 120)
    im = caution_tape(im, 632, 84, ang=-3)
    im = caution_tape(im, -26, 68, ang=2)
    # logo Walmart su pastiglia bianca lucida
    lg = walmart_logo(84)
    pill = Image.new("RGBA", (lg.width + 80, 124), (0, 0, 0, 0)); d = ImageDraw.Draw(pill)
    d.rounded_rectangle([0, 0, pill.width - 1, pill.height - 1], radius=62, fill=(255, 255, 255, 255), outline=BLK, width=6)
    d.rounded_rectangle([8, 8, pill.width - 9, 50], radius=40, fill=(238, 244, 255, 255))
    pill.alpha_composite(lg, (40, (124 - lg.height) // 2))
    im = drop(im, pill, (34, 52), far=(8, 14), far_blur=12, far_a=140, near=(3, 5), near_blur=3, near_a=120)
    # cartellino giallo + divieto rosso
    tg = hang_tag(400, 420, ang=8)
    im = drop(im, tg, (70, 150), far=(30, 40), far_blur=24, far_a=170)
    pr = prohibition(170)
    im = drop(im, pr, (356, 168), far=(8, 12), far_blur=10, far_a=140, near=(3, 5), near_blur=3, near_a=110)
    # testi a destra
    im = drop(im, banner("WALMART'S OWN PAGE", 640, 86, 44), (600, 70), far=(8, 12), far_blur=10, far_a=150, near=(3, 5), near_blur=3, near_a=120)
    im = text3d(im, (920, 290), "NO", 236, (255, 214, 28), (170, 90, 0), stroke=20, dep=18)
    im = text3d(im, (920, 452), "PRICE MATCH", 86, (255, 255, 255), (70, 20, 30), stroke=14, dep=12)
    band = white_band("BLACK FRIDAY RETURN + PRICE MATCH RULES", 1180, 80, 42)
    im = sp(im, band, (50, 576), off=(6, 10), blur=9, alpha=170)
    return grain(im, 6)


if __name__ == "__main__":
    a = thumb_a(); a.save(os.path.join(OUT, "blackfriday-miniatura-a.png"))
    b = thumb_b(); b.save(os.path.join(OUT, "blackfriday-miniatura-b.png"))
    print("ok", a.size, b.size)
