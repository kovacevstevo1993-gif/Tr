#!/usr/bin/env python3
"""Identita visiva v2: 5 fotogrammi tipo (uno per parte del video) sulla scrivania fotorealistica.
1 gancio (contatore a rulli)  2 apertura pratica (cartellina + polaroid)  3 trappola (lente + post-it)
4 indovina (tre cartellini + conto alla rovescia)  5 verdetto (scontrino + timbro).
Output: nuovo_canale_italia/brand/v2-*.png"""
import os, random, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__)); BR = os.path.join(HERE, "..", "brand")
FD = os.path.join(BR, "fonts"); AS = os.path.join(BR, "assets"); INTER = "/usr/share/fonts/opentype/inter/"
W, H = 1920, 1080
CARTA = (243, 240, 232); INCH = (22, 24, 29); ROSSO = (227, 33, 25); GIALLO = (255, 225, 74)
VERDE = (25, 163, 91); GRIGIO = (138, 143, 152); NERO = (8, 8, 10)

def F(n, s):
    if n == "mano":
        f = ImageFont.truetype(os.path.join(FD, "Caveat.ttf"), s); f.set_variation_by_name("Bold"); return f
    p = {"titolo": "ArchivoBlack-Regular.ttf", "mono": "IBMPlexMono-Bold.ttf", "mono2": "IBMPlexMono-Medium.ttf",
         "marker": "PermanentMarker-Regular.ttf"}.get(n)
    if p: return ImageFont.truetype(os.path.join(FD, p), s)
    return ImageFont.truetype(INTER + {"corpo": "Inter-SemiBold.otf", "corpoB": "Inter-Black.otf", "corpoR": "Inter-Regular.otf"}[n], s)

def scrivania(buio=1.0):
    img = Image.open(os.path.join(AS, "scrivania.png")).convert("RGB").resize((W, H + 8)).crop((0, 4, W, H + 4))
    if buio != 1.0: img = ImageEnhance.Brightness(img).enhance(buio)
    import numpy as np
    yy, xx = np.mgrid[0:H, 0:W]; r = np.sqrt(((xx - W * 0.45) / (W * 0.62)) ** 2 + ((yy - H * 0.45) / (H * 0.62)) ** 2)
    v = Image.fromarray((np.clip(r - 0.55, 0, 1) * 330).clip(0, 200).astype("uint8"))
    img = img.convert("RGBA"); nero = Image.new("RGBA", (W, H), (0, 0, 0, 0)); nero.putalpha(v); img.alpha_composite(nero)
    return img

def ombra(im, off=(14, 22), blur=22, alpha=190):
    """incolla un'ombra morbida sotto un oggetto RGBA (ritorna immagine piu grande con ombra)"""
    pad = blur * 3; big = Image.new("RGBA", (im.width + pad * 2, im.height + pad * 2), (0, 0, 0, 0))
    a = im.split()[3].point(lambda v: min(alpha, v))
    sh = Image.new("RGBA", im.size, (0, 0, 0, 255)); sh.putalpha(a)
    big.alpha_composite(sh, (pad + off[0], pad + off[1])); big = big.filter(ImageFilter.GaussianBlur(blur))
    big.alpha_composite(im, (pad, pad)); return big, pad

def incolla(img, obj, xy, rot=0, sh=True):
    if rot: obj = obj.rotate(rot, expand=True, resample=Image.BICUBIC)
    if sh:
        obj, pad = ombra(obj); xy = (xy[0] - pad, xy[1] - pad)
    img.alpha_composite(obj, (int(xy[0]), int(xy[1])))

def grana_carta(im, seed=2):
    """fibra della carta + leggera luce calda dall'alto a sinistra"""
    random.seed(seed); w, h = im.size; n = Image.effect_noise((w, h), 9).convert("L")
    tex = Image.merge("RGBA", (n, n, n, Image.new("L", (w, h), 16)))
    a = im.split()[3]; out = im.copy(); out.alpha_composite(tex); out.putalpha(a)
    import numpy as np
    yy, xx = np.mgrid[0:h, 0:w]; g = Image.fromarray(((xx / w + yy / h) / 2 * 26).astype("uint8"))
    dark = Image.new("RGBA", (w, h), (60, 40, 20, 0)); dark.putalpha(Image.composite(g, Image.new("L", (w, h), 0), a))
    out.alpha_composite(dark); return out

def foglio(w, h, colore=CARTA):
    im = Image.new("RGBA", (w, h), colore + (255,)); return im

def timbro(testo, colore, size, seed=7):
    f = F("titolo", size); tw = int(f.getlength(testo)); th = int(size * 1.25)
    im = Image.new("RGBA", (tw + 80, th + 60), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([8, 8, tw + 72, th + 52], radius=14, outline=colore + (235,), width=max(5, size // 10))
    d.text((40, 24), testo, font=f, fill=colore + (235,))
    random.seed(seed); a = im.split()[3].load()
    for _ in range(im.size[0] * im.size[1] // 6):
        x, y = random.randrange(im.size[0]), random.randrange(im.size[1])
        if a[x, y] > 0: a[x, y] = int(a[x, y] * random.choice([0.3, 0.6, 1, 1, 1]))
    return im

def contatore_rulli(cifre, label="STAI PERDENDO", cell=(92, 140), roll=None):
    """contatore meccanico a rulli: celle nere cilindriche con cifre rosse. cifre es. '€2.847'.
    roll = indici delle celle 'in movimento' (cifra a meta tra due numeri, sfocata)"""
    roll = roll or []; cw, ch = cell; gap = 10; f = F("mono", int(ch * 0.62)); fl = F("mono", 26)
    celle = [c for c in cifre]; w = sum((cw if c not in ".," else cw // 3) for c in celle) + gap * (len(celle) - 1) + 60
    w = max(w, int(fl.getlength(label)) + 110); xc0 = (w - (sum((cw if c not in ".," else cw // 3) for c in celle) + gap * (len(celle) - 1))) // 2
    h = ch + 110; im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=22, fill=(24, 25, 29, 255), outline=(70, 72, 78, 255), width=3)
    d.rounded_rectangle([6, 6, w - 7, h - 7], radius=18, outline=(12, 12, 14, 255), width=3)
    d.text((30, 18), label, font=fl, fill=GRIGIO)
    d.ellipse([w - 44, 26, w - 28, 42], fill=ROSSO)                                   # spia rossa "registra"
    x = xc0; y = 70
    for i, c in enumerate(celle):
        if c in ".,":
            d.ellipse([x + cw // 6 - 7, y + ch - 30, x + cw // 6 + 7, y + ch - 16], fill=ROSSO); x += cw // 3 + gap; continue
        cel = Image.new("RGBA", (cw, ch), NERO + (255,)); dc = ImageDraw.Draw(cel)
        if i in roll:                                                                  # cifra che gira: due numeri a meta
            a, b = c, str((int(c) + 1) % 10) if c.isdigit() else c
            for txt, oy in ((a, -ch * 0.55), (b, ch * 0.45)):
                dc.text((cw / 2, ch / 2 + oy), txt, font=f, fill=ROSSO, anchor="mm")
            cel = cel.filter(ImageFilter.GaussianBlur(2.2))
        else:
            dc.text((cw / 2, ch / 2), c, font=f, fill=ROSSO, anchor="mm")
        sh = Image.new("RGBA", (cw, ch), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)      # ombra cilindrica sopra/sotto
        for k in range(ch):
            t = abs(k - ch / 2) / (ch / 2); ds.line([0, k, cw, k], fill=(0, 0, 0, int(200 * t ** 2.2)))
        ds.line([0, ch * 0.5, cw, ch * 0.5], fill=(255, 255, 255, 18), width=2)
        cel.alpha_composite(sh); im.alpha_composite(cel, (x, y))
        d.rectangle([x - 2, y - 2, x + cw + 1, y + ch + 1], outline=(55, 57, 63), width=2); x += cw + gap
    gl = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(gl).rounded_rectangle([14, 64, w - 14, 64 + ch * 0.35], radius=10, fill=(255, 255, 255, 14))
    im.alpha_composite(gl); return im

def pillola(testo, colore, fs=30, fg=CARTA):
    f = F("mono", fs); w = int(f.getlength(testo)) + 60; h = int(fs * 2.1)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=h // 2, fill=colore); d.text((w / 2, h / 2), testo, font=f, fill=fg, anchor="mm")
    return im

def sottotitolo(img, frase, y=H - 128, fs=44):
    f = F("corpo", fs); fw = f.getlength(frase); d = ImageDraw.Draw(img)
    d.rounded_rectangle([(W - fw) / 2 - 30, y, (W + fw) / 2 + 30, y + fs * 1.9], radius=14, fill=NERO + (215,))
    d.text((W / 2, y + fs * 0.95), frase, font=f, fill=CARTA, anchor="mm")

def graffetta(h=150):
    im = Image.new("RGBA", (60, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im); c = (176, 180, 188, 255)
    d.rounded_rectangle([6, 4, 54, h - 4], radius=24, outline=c, width=6); d.rounded_rectangle([18, 22, 44, h - 30], radius=13, outline=c, width=6)
    d.line([20, 6, 40, 6], fill=(220, 224, 230, 255), width=2); return im

def polaroid(foto, w=360):
    ph = Image.open(os.path.join(AS, foto)).convert("RGB")
    bx = ph.crop((95, 505, 170, 590)).filter(ImageFilter.GaussianBlur(9)); ph.paste(bx, (95, 505))   # via il logo
    s = w - 36; ph = ph.resize((s, s)); ph = ImageEnhance.Contrast(ph).enhance(1.05)
    im = Image.new("RGBA", (w, w + 70), (250, 249, 245, 255)); im.paste(ph, (18, 18)); return im

def postit(testo, w=300, rot=0):
    im = Image.new("RGBA", (w, w), (255, 231, 92, 255)); d = ImageDraw.Draw(im)
    g = Image.linear_gradient("L").resize((w, w)).point(lambda v: int(v * 0.18))
    sh = Image.new("RGBA", (w, w), (120, 90, 0, 0)); sh.putalpha(g); im.alpha_composite(sh)
    y = 40
    for riga in testo.split("\n"):
        d.text((26, y), riga, font=F("mano", 66), fill=(30, 30, 40)); y += 72
    return im

def lente(sorgente, centro, r=170, zoom=1.7):
    """lente d'ingrandimento: ingrandisce l'area di 'sorgente' attorno a centro"""
    cx, cy = centro; src = r / zoom
    reg = sorgente.crop((int(cx - src), int(cy - src), int(cx + src), int(cy + src))).resize((2 * r, 2 * r), Image.LANCZOS)
    m = Image.new("L", (2 * r, 2 * r), 0); ImageDraw.Draw(m).ellipse([0, 0, 2 * r - 1, 2 * r - 1], fill=255)
    out = Image.new("RGBA", (2 * r + 260, 2 * r + 260), (0, 0, 0, 0)); out.paste(reg, (20, 20), m)
    d = ImageDraw.Draw(out)
    ang = math.radians(45); hx, hy = 20 + r + (r + 8) * math.cos(ang), 20 + r + (r + 8) * math.sin(ang)
    d.line([hx, hy, hx + 210 * math.cos(ang), hy + 210 * math.sin(ang)], fill=(20, 20, 22, 255), width=46)
    d.line([hx + 4, hy + 4, hx + 200 * math.cos(ang), hy + 200 * math.sin(ang)], fill=(60, 60, 66, 255), width=8)
    d.ellipse([20 - 14, 20 - 14, 20 + 2 * r + 14, 20 + 2 * r + 14], outline=(30, 30, 34, 255), width=18)
    d.ellipse([20 - 8, 20 - 8, 20 + 2 * r + 8, 20 + 2 * r + 8], outline=(150, 152, 160, 255), width=3)
    gl = Image.new("RGBA", out.size, (0, 0, 0, 0)); ImageDraw.Draw(gl).ellipse([20 + r * 0.25, 20 + r * 0.15, 20 + r * 0.95, 20 + r * 0.6], fill=(255, 255, 255, 40))
    out.alpha_composite(gl.filter(ImageFilter.GaussianBlur(12))); return out

def penna_cerchio(d, box, w=5):
    x0, y0, x1, y1 = box
    for k in range(3):
        d.arc([x0 - k * 2, y0 + k, x1 + k, y1 - k], 200 - k * 20, 520 - k * 15, fill=ROSSO, width=w)

def contratto(righe, evid=None, cerchio=None, w=1040, h=880, titolo="Contratto di finanziamento", n="001", tema="FINANZIAMENTO AUTO"):
    im = foglio(w, h); d = ImageDraw.Draw(im); L = 64
    d.text((L, 48), f"PRATICA N. {n}", font=F("mono", 28), fill=ROSSO)
    d.text((w - 64, 50), f"{tema}  ·  RISERVATO", font=F("mono2", 24), fill=GRIGIO, anchor="ra")
    d.line([L, 96, w - 64, 96], fill=INCH, width=3)
    d.text((L, 122), titolo, font=F("titolo", 46), fill=INCH)
    y = 222; pos = {}
    for k, v in righe:
        if k == evid: d.rectangle([L - 14, y - 8, w - 50, y + 50], fill=GIALLO)
        d.text((L, y), k, font=F("mono2", 32), fill=INCH)
        d.text((w - 64, y), v, font=F("mono", 32), fill=INCH, anchor="ra"); pos[k] = (w - 64 - F("mono", 32).getlength(v), y)
        d.line([L, y + 60, w - 64, y + 60], fill=(208, 203, 192), width=2); y += 76
    if cerchio in pos:
        x, yy = pos[cerchio]; penna_cerchio(d, (x - 26, yy - 16, w - 40, yy + 56))
    d.text((L, h - 50), "Fonte: simulazione su condizioni medie di mercato 2026", font=F("corpoR", 21), fill=GRIGIO)
    return grana_carta(im), pos

RIGHE = [("Prezzo auto", "€ 21.900"), ("Anticipo", "€ 3.000"), ("Rata mensile", "€ 199 x 35"),
         ("Maxirata finale", "€ 14.782"), ("TAN fisso", "6,95%"), ("TAEG", "9,89%"), ("Totale dovuto", "€ 24.747")]

# ---------- 1 GANCIO ----------
def f1():
    img = scrivania(0.9); d = ImageDraw.Draw(img)
    d.text((W / 2, 150), "Firma pure. Davvero.", font=F("titolo", 92), fill=CARTA, anchor="mm")
    d.text((W / 2 + 2, 247), "Questo video non ti serve… a meno che la rata non sia sotto i 200 €.", font=F("corpo", 38), fill=(0, 0, 0), anchor="mm")
    d.text((W / 2, 245), "Questo video non ti serve… a meno che la rata non sia sotto i 200 €.", font=F("corpo", 38), fill=(196, 199, 205), anchor="mm")
    c = contatore_rulli("€2.847", label="QUANTO TI COSTA IN PIÙ", cell=(130, 196), roll=[4, 5])
    incolla(img, c, ((W - c.width) / 2, 360))
    t = pillola("LA CIFRA ESATTA AL MINUTO 11", ROSSO, 30); incolla(img, t, ((W - t.width) / 2, 760), sh=False)
    sottotitolo(img, "Ma prima, guarda la riga 4 del contratto.")
    return img

# ---------- 2 APERTURA PRATICA ----------
def f2():
    img = scrivania(0.95)
    cart = Image.new("RGBA", (1100, 760), (0, 0, 0, 0)); d = ImageDraw.Draw(cart)
    d.rounded_rectangle([0, 60, 1099, 759], radius=18, fill=(214, 196, 160, 255))           # cartellina
    d.rounded_rectangle([40, 0, 420, 120], radius=18, fill=(214, 196, 160, 255))              # linguetta
    d.rectangle([60, 140, 760, 300], fill=CARTA + (255,)); d.rectangle([60, 140, 760, 300], outline=INCH, width=3)
    d.text((90, 160), "PRATICA N. 001", font=F("mono", 44), fill=ROSSO)
    d.text((90, 222), "FINANZIAMENTO AUTO", font=F("titolo", 50), fill=INCH)
    d.text((70, 30), "N. 001", font=F("mono", 34), fill=(90, 70, 40))
    for i in range(4): d.line([60, 360 + i * 56, 700, 360 + i * 56], fill=(176, 158, 122), width=3)
    d.text((60, 340), "Cliente: chi sta per firmare", font=F("mano", 54), fill=(40, 40, 60))
    d.text((60, 452), "Rata: 199 € al mese… troppo bella?", font=F("mano", 54), fill=(40, 40, 60))
    cart = grana_carta(cart, 4); incolla(img, cart, (200, 190), rot=-3)
    p = polaroid("auto.png", 380); incolla(img, p, (1170, 230), rot=6)
    incolla(img, graffetta(170), (1300, 170), rot=8, sh=False)
    t = timbro("RISERVATO", ROSSO, 60, 3).rotate(-12, expand=True); img.alpha_composite(t, (690, 738))
    c = contatore_rulli("€0", label="STAI PERDENDO", cell=(70, 104)); incolla(img, c, (W - c.width - 70, 40))
    pl = pillola("3 TRAPPOLE", ROSSO, 32); incolla(img, pl, (W - pl.width - 80, 900), sh=False)
    sottotitolo(img, "Tre trappole. L'ultima è quella che costa di più.")
    return img

# ---------- 3 TRAPPOLA ----------
def f3():
    img = scrivania(0.92); ct, pos = contratto(RIGHE, evid="Maxirata finale")
    x0, y0 = 120, 70; incolla(img, ct, (x0, y0), rot=-1.5)
    base = img.copy()
    cx, cy = 1022, 556                                                                          # centro sulla cifra della maxirata
    le = lente(base.convert("RGB"), (cx, cy), r=185, zoom=1.55); incolla(img, le, (cx - 205, cy - 205))
    pi = postit("riga 4!\nleggi qui", 290); incolla(img, pi, (1380, 560), rot=-7)
    c = contatore_rulli("€1.290", cell=(70, 104)); incolla(img, c, (W - c.width - 70, 40))
    pl = pillola("TRAPPOLA 2 DI 3", ROSSO, 30); incolla(img, pl, (W - pl.width - 80, 300), sh=False)
    sottotitolo(img, "La rata è bassa perché il conto vero arriva alla fine.")
    return img

# ---------- 4 INDOVINA ----------
def f4():
    img = scrivania(0.8); d = ImageDraw.Draw(img)
    d.text((W / 2, 120), "INDOVINA", font=F("mono", 34), fill=GIALLO, anchor="mm")
    d.text((W / 2, 200), "Quanto paghi in più alla fine?", font=F("titolo", 74), fill=CARTA, anchor="mm")
    opz = [("A", "€ 900"), ("B", "€ 1.900"), ("C", "€ 2.847")]
    for i, (l, v) in enumerate(opz):
        cd = Image.new("RGBA", (400, 300), CARTA + (255,)); dc = ImageDraw.Draw(cd)
        dc.rectangle([0, 0, 399, 54], fill=INCH); dc.text((24, 8), l, font=F("mono", 34), fill=CARTA)
        for k in range(4): dc.line([24, 120 + k * 40, 376, 120 + k * 40], fill=(205, 222, 240), width=2)
        dc.line([60, 54, 60, 300], fill=(240, 170, 170), width=2)
        dc.text((210, 190), v, font=F("mono", 62), fill=INCH, anchor="mm")
        cd = grana_carta(cd, 10 + i); incolla(img, cd, (250 + i * 500, 380 + (i % 2) * 30), rot=(-4, 2, -2)[i])
    r = 92; cxy = (W / 2, 850)
    ring = Image.new("RGBA", (2 * r + 20, 2 * r + 20), (0, 0, 0, 0)); dr = ImageDraw.Draw(ring)
    dr.ellipse([10, 10, 2 * r + 10, 2 * r + 10], fill=NERO + (235,)); dr.arc([10, 10, 2 * r + 10, 2 * r + 10], -90, 150, fill=ROSSO, width=12)
    dr.text((r + 10, r + 10), "3", font=F("mono", 110), fill=CARTA, anchor="mm")
    img.alpha_composite(ring, (int(cxy[0] - r - 10), int(cxy[1] - r - 10)))
    d.text((W / 2 + 160, 850), "Scrivilo nei commenti prima della risposta", font=F("mano", 54), fill=GIALLO, anchor="lm")
    return img

# ---------- 5 VERDETTO ----------
def f5():
    img = scrivania(0.9)
    sw, sh_ = 560, 900; sc = Image.new("RGBA", (sw, sh_), (0, 0, 0, 0)); d = ImageDraw.Draw(sc)
    pts = [(0, 14)] + [(x, 14 if (x // 14) % 2 else 0) for x in range(0, sw + 1, 14)] + [(sw, sh_ - 14)] + \
          [(x, sh_ - 14 if (x // 14) % 2 else sh_) for x in range(sw, -1, -14)]
    d.polygon(pts, fill=(250, 250, 247, 255))
    m = F("mono2", 26); mb = F("mono", 28); y = 50
    d.text((sw / 2, y), "PRATICA N. 001", font=mb, fill=INCH, anchor="ma"); y += 44
    d.text((sw / 2, y), "FINANZIAMENTO AUTO", font=m, fill=INCH, anchor="ma"); y += 50
    d.text((40, y), "-" * 30, font=m, fill=GRIGIO); y += 46
    for k, v in [("Trappola 1  TAEG", "€   612"), ("Trappola 2  Maxirata", "€ 1.290"), ("Trappola 3  Polizze", "€   945")]:
        d.text((40, y), k, font=m, fill=INCH); d.text((sw - 40, y), v, font=mb, fill=INCH, anchor="ra"); y += 52
    d.text((40, y), "-" * 30, font=m, fill=GRIGIO); y += 50
    d.text((40, y), "TOTALE IN PIÙ", font=F("mono", 32), fill=ROSSO); d.text((sw - 40, y), "€ 2.847", font=F("mono", 32), fill=ROSSO, anchor="ra"); y += 70
    d.text((sw / 2, y), "Grazie per non aver firmato.", font=F("mano", 44), fill=(40, 40, 60), anchor="ma"); y += 80
    for i in range(46): d.rectangle([60 + i * 10, y, 60 + i * 10 + (3 if i % 3 else 6), y + 70], fill=INCH)   # codice a barre
    sc = grana_carta(sc, 12); incolla(img, sc, (250, 90), rot=3)
    t = timbro("NON CONVIENE", ROSSO, 70, 5).rotate(-12, expand=True); img.alpha_composite(t, (200, 640))
    c = contatore_rulli("€2.847", label="TOTALE PERSO", cell=(104, 156)); incolla(img, c, (1050, 170))
    pv = pillola("COME EVITARLO: 3 MOSSE  →", VERDE, 32); incolla(img, pv, (1080, 560), sh=False)
    sottotitolo(img, "Verdetto: con la maxirata, non conviene.")
    return img

if __name__ == "__main__":
    for i, f in enumerate([f1, f2, f3, f4, f5], 1):
        nome = ["gancio", "apertura-pratica", "trappola", "indovina", "verdetto"][i - 1]
        f().convert("RGB").save(os.path.join(BR, f"v2-{i}-{nome}.png")); print("ok", i)
