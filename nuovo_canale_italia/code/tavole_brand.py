#!/usr/bin/env python3
"""Tavole dell'identita del canale "Trappole e conti veri": colori/caratteri, fotogramma tipo, miniatura tipo.
Output: nuovo_canale_italia/brand/tavola-*.png"""
import os, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
BR = os.path.join(HERE, "..", "brand"); FD = os.path.join(BR, "fonts")
INTER = "/usr/share/fonts/opentype/inter/"

# --- PALETTE (fissa per tutto il canale) ---
SCRIVANIA = (16, 17, 20)      # fondo scuro
SCRIVANIA2 = (28, 30, 36)
CARTA = (243, 240, 232)       # fogli della pratica
INCHIOSTRO = (22, 24, 29)     # testo sui fogli
ROSSO = (227, 33, 25)         # trappole, contatore, timbro NON CONVIENE
GIALLO = (255, 225, 74)       # evidenziatore
VERDE = (25, 163, 91)         # timbro CONVIENE / risparmio
GRIGIO = (138, 143, 152)      # testi secondari

def F(nome, s):
    p = {"titolo": os.path.join(FD, "ArchivoBlack-Regular.ttf"), "mono": os.path.join(FD, "IBMPlexMono-Bold.ttf"),
         "mono2": os.path.join(FD, "IBMPlexMono-Medium.ttf"), "corpo": INTER + "Inter-SemiBold.otf",
         "corpoB": INTER + "Inter-Black.otf", "corpoR": INTER + "Inter-Regular.otf"}[nome]
    return ImageFont.truetype(p, s)

def scrivania(w, h, seed=1):
    """fondo scuro con vignetta e grana leggera (sempre uguale: e il 'tavolo' del canale)"""
    img = Image.new("RGB", (w, h), SCRIVANIA)
    g = Image.new("L", (w, h), 0); d = ImageDraw.Draw(g)
    for i in range(40):
        r = int(max(w, h) * (0.9 - i * 0.02)); a = int(2 + i * 0.9)
        d.ellipse([w * 0.45 - r, h * 0.42 - r, w * 0.45 + r, h * 0.42 + r], fill=min(255, a))
    g = g.filter(ImageFilter.GaussianBlur(60))
    img = Image.composite(Image.new("RGB", (w, h), SCRIVANIA2), img, g)
    random.seed(seed); px = img.load()
    for _ in range(w * h // 18):
        x, y = random.randrange(w), random.randrange(h); n = random.randint(-7, 7)
        c = px[x, y]; px[x, y] = tuple(max(0, min(255, v + n)) for v in c)
    return img

def foglio(w, h, rot=0):
    """foglio della pratica con ombra; ritorna immagine RGBA ruotata"""
    pad = 40; im = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rectangle([pad + 10, pad + 18, pad + w + 10, pad + h + 18], fill=(0, 0, 0, 170))
    sh = sh.filter(ImageFilter.GaussianBlur(18)); im.alpha_composite(sh)
    ImageDraw.Draw(im).rectangle([pad, pad, pad + w, pad + h], fill=CARTA + (255,))
    return im, pad

def timbro(testo, colore, size, rot):
    f = F("titolo", size); tw = int(f.getlength(testo)); th = int(size * 1.25)
    im = Image.new("RGBA", (tw + 80, th + 60), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([8, 8, tw + 72, th + 52], radius=14, outline=colore + (235,), width=9)
    d.text((40, 24), testo, font=f, fill=colore + (235,))
    random.seed(7); a = im.split()[3].load()                       # inchiostro irregolare
    for _ in range(im.size[0] * im.size[1] // 7):
        x, y = random.randrange(im.size[0]), random.randrange(im.size[1])
        if a[x, y] > 0: a[x, y] = int(a[x, y] * random.choice([0.35, 0.6, 1, 1, 1]))
    return im.rotate(rot, expand=True, resample=Image.BICUBIC)

def contatore(valore, label="STAI PERDENDO", scala=1.0):
    s = scala; f1 = F("mono", int(26 * s)); f2 = F("mono", int(78 * s))
    w = int(max(f2.getlength(valore), f1.getlength(label)) + 64 * s); h = int(150 * s)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=int(14 * s), fill=(8, 8, 10, 245), outline=ROSSO + (255,), width=int(4 * s))
    d.text((int(32 * s), int(16 * s)), label, font=f1, fill=GRIGIO)
    d.text((int(32 * s), int(48 * s)), valore, font=f2, fill=ROSSO)
    return im

# ---------------- TAVOLA 1: colori e caratteri ----------------
def tavola1():
    W, H = 1920, 1080; img = scrivania(W, H); d = ImageDraw.Draw(img)
    d.text((90, 70), "IDENTITÀ DEL CANALE", font=F("mono", 30), fill=GRIGIO)
    d.text((90, 110), "Colori e caratteri", font=F("titolo", 76), fill=CARTA)
    sw = [("SCRIVANIA", SCRIVANIA, "#101114", "fondo di ogni video"), ("CARTA", CARTA, "#F3F0E8", "fogli della pratica"),
          ("INCHIOSTRO", INCHIOSTRO, "#16181D", "testo sui fogli"), ("ROSSO TRAPPOLA", ROSSO, "#E32119", "contatore, trappole, NON CONVIENE"),
          ("EVIDENZIATORE", GIALLO, "#FFE14A", "la frase che conta"), ("VERDE CONVIENE", VERDE, "#19A35B", "risparmio, CONVIENE"),
          ("GRIGIO NOTA", GRIGIO, "#8A8F98", "etichette, fonti")]
    x0, y0, cw = 90, 270, 240
    for i, (n, c, hx, uso) in enumerate(sw):
        x = x0 + i * (cw + 18)
        d.rounded_rectangle([x, y0, x + cw, y0 + 200], radius=16, fill=c, outline=(70, 72, 80), width=2)
        d.text((x, y0 + 220), n, font=F("mono", 22), fill=CARTA)
        d.text((x, y0 + 252), hx, font=F("mono2", 22), fill=GRIGIO)
        y = y0 + 286
        righe, cur = [], ""
        for w_ in uso.split():
            if len(cur) + len(w_) + 1 > 22 and cur: righe.append(cur); cur = w_
            else: cur = (cur + " " + w_).strip()
        righe.append(cur)
        for riga in righe:
            d.text((x, y), riga, font=F("corpoR", 20), fill=GRIGIO); y += 26
    y = 690
    d.text((90, y), "TITOLI", font=F("mono", 22), fill=GRIGIO); d.text((90, y + 34), "Archivo Black", font=F("titolo", 64), fill=CARTA)
    d.text((720, y), "NUMERI E PRATICA", font=F("mono", 22), fill=GRIGIO); d.text((720, y + 40), "IBM Plex Mono", font=F("mono", 54), fill=ROSSO)
    d.text((1420, y), "TESTI", font=F("mono", 22), fill=GRIGIO); d.text((1420, y + 44), "Inter SemiBold", font=F("corpo", 54), fill=CARTA)
    d.text((90, 960), "Regola: massimo 3 colori per inquadratura + il rosso solo per soldi persi e trappole.", font=F("corpo", 30), fill=GIALLO)
    img.save(os.path.join(BR, "tavola-1-colori-caratteri.png"))

# ---------------- TAVOLA 2: fotogramma tipo ----------------
def tavola2():
    W, H = 1920, 1080; img = scrivania(W, H, 3).convert("RGBA")
    fw, fh = 1060, 840; fo, pad = foglio(fw, fh); d = ImageDraw.Draw(fo); L = pad + 70
    d.text((L, pad + 50), "PRATICA N. 001", font=F("mono", 30), fill=ROSSO)
    d.text((L + 330, pad + 50), "·  FINANZIAMENTO AUTO  ·  RISERVATO", font=F("mono2", 26), fill=GRIGIO)
    d.line([L, pad + 100, pad + fw - 70, pad + 100], fill=INCHIOSTRO, width=3)
    d.text((L, pad + 130), "Contratto di finanziamento", font=F("titolo", 50), fill=INCHIOSTRO)
    righe = [("Prezzo auto", "€ 21.900"), ("Anticipo", "€ 3.000"), ("Rata mensile", "€ 199 x 35"),
             ("Maxirata finale", "€ 14.782"), ("TAN fisso", "6,95%"), ("TAEG", "9,89%"), ("Totale dovuto", "€ 24.747")]
    y = pad + 240
    for i, (k, v) in enumerate(righe):
        if k == "Maxirata finale":
            d.rectangle([L - 12, y - 6, pad + fw - 58, y + 52], fill=GIALLO)
        d.text((L, y), k, font=F("mono2", 34), fill=INCHIOSTRO)
        d.text((pad + fw - 70 - F("mono", 34).getlength(v), y), v, font=F("mono", 34), fill=INCHIOSTRO)
        d.line([L, y + 62, pad + fw - 70, y + 62], fill=(205, 200, 190), width=2); y += 78
    tx = pad + fw - 70 - F("mono", 34).getlength("9,89%"); ty = pad + 240 + 5 * 78       # cerchio a penna sul TAEG
    for k in range(3):
        d.ellipse([tx - 26 + k, ty - 18 + k, tx + 130 - k, ty + 58 - k], outline=ROSSO, width=4)
    d.text((L, pad + fh - 42), "Fonte: simulazione su condizioni medie di mercato 2026", font=F("corpoR", 22), fill=GRIGIO)
    fo = fo.rotate(-2.2, expand=True, resample=Image.BICUBIC); img.alpha_composite(fo, (110, 40))
    c = contatore("−€ 2.847"); img.alpha_composite(c, (W - c.size[0] - 80, 70))
    ch = Image.new("RGBA", (330, 64), (0, 0, 0, 0)); dc = ImageDraw.Draw(ch)
    dc.rounded_rectangle([0, 0, 329, 63], radius=32, fill=ROSSO); dc.text((30, 13), "TRAPPOLA 2 DI 3", font=F("mono", 30), fill=CARTA)
    img.alpha_composite(ch, (W - 410, 260))
    t = timbro("NON CONVIENE", ROSSO, 64, 8); img.alpha_composite(t, (W - t.size[0] - 70, 470))
    sb = Image.new("RGBA", (W, 120), (0, 0, 0, 0)); ds = ImageDraw.Draw(sb)
    frase = "La rata è bassa perché il conto vero arriva alla fine."
    fwid = F("corpo", 44).getlength(frase); ds.rounded_rectangle([(W - fwid) / 2 - 30, 18, (W + fwid) / 2 + 30, 102], radius=14, fill=(8, 8, 10, 215))
    ds.text(((W - fwid) / 2, 32), frase, font=F("corpo", 44), fill=CARTA)
    img.alpha_composite(sb, (0, H - 135))
    img.convert("RGB").save(os.path.join(BR, "tavola-2-fotogramma-tipo.png"))

# ---------------- TAVOLA 3: miniatura tipo ----------------
def tavola3():
    W, H = 1280, 720; img = scrivania(W, H, 5).convert("RGBA")
    fo, pad = foglio(520, 600); d = ImageDraw.Draw(fo)
    d.text((pad + 40, pad + 40), "PRATICA N. 001", font=F("mono", 26), fill=ROSSO)
    for i in range(8):
        y = pad + 110 + i * 58; d.rectangle([pad + 40, y, pad + 40 + random.randint(260, 440), y + 18], fill=(200, 196, 186))
    d.rectangle([pad + 30, pad + 102 + 3 * 58, pad + 490, pad + 136 + 3 * 58], fill=GIALLO)
    fo = fo.rotate(6, expand=True, resample=Image.BICUBIC); img.alpha_composite(fo, (720, 30))
    d = ImageDraw.Draw(img)
    d.text((60, 70), "LA RATA BASSA", font=F("titolo", 84), fill=CARTA)
    d.text((60, 170), "TI COSTA", font=F("titolo", 84), fill=CARTA)
    c = contatore("€ 2.847", label="IN PIÙ", scala=1.7); img.alpha_composite(c, (50, 310))
    t = timbro("NON FIRMARE", ROSSO, 58, -8); img.alpha_composite(t, (W - t.size[0] - 20, H - t.size[1] - 30))
    img.convert("RGB").save(os.path.join(BR, "tavola-3-miniatura-tipo.png"))

if __name__ == "__main__":
    tavola1(); tavola2(); tavola3(); print("ok")
