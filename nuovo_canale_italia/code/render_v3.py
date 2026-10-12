#!/usr/bin/env python3
"""Motore video v3 (12/10/2026): stile "virale" - foto a tutto schermo con camera in movimento, cambio scena ogni 2-5 s,
testo gigante solo sulle parole chiave, grafici animati, whoosh/pop/thud ad ogni stacco, musica originale bassa.
Voce NON rifatta: usa pratica001/voce (render_pratica.prepara_audio). Uso: render_v3.py cartella_pratica [solo_frame_fotogrammi]"""
import os, sys, re, json, math, wave, bisect, subprocess, random
import numpy as np
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render_pratica as R
import fotogrammi_v2 as G
import demo_gancio as D

W, H, FPS = 1920, 1080, 30
F = G.F; ROSSO, GIALLO, CARTA, NERO, GRIGIO, VERDE, INCH = G.ROSSO, G.GIALLO, G.CARTA, G.NERO, G.GRIGIO, G.VERDE, G.INCH
ease, lerp, ease_back = D.ease, D.lerp, D.ease_back
PR = R.PR
SC0 = R.Scene
AI = os.path.join(G.AS, "ai")
COP = json.load(open(os.path.join(PR, "copione.json"), encoding="utf-8"))
BLU = (70, 130, 255); AZZ = (120, 190, 255); VERDEC = (150, 220, 180)

def A(tl, t0, d=0.3): return ease((tl - t0) / d) if tl >= t0 else 0.0
def E(tl, t0, d=0.45): return ease_back((tl - t0) / d, 1.5) if tl >= t0 else 0.0
def fmt(v): return f"{int(round(v)):,}".replace(",", ".")

class Q(str): pass                                                                   # cue: frase detta a voce -> secondi dall'inizio della scena

# ============================================================ sprite (cache per processo)
_C = {}
def tx(s, fs, col=CARTA, font="titolo", sw=None, sh=True):
    k = ("tx", s, fs, col, font)
    if k in _C: return _C[k]
    f = F(font, fs); ls = int(fs * 1.12); lines = s.split("\n"); pad = fs // 3 + 8
    w = int(max(f.getlength(l) for l in lines)) + 2 * pad; h = ls * len(lines) + 2 * pad
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); sw = fs // 15 if sw is None else sw
    if sh:
        s2 = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d2 = ImageDraw.Draw(s2)
        for i, l in enumerate(lines): d2.text((w / 2 + 3, pad + i * ls + fs // 2 + 7), l, font=f, fill=(0, 0, 0, 170), anchor="mm", stroke_width=sw, stroke_fill=(0, 0, 0, 170))
        im.alpha_composite(s2.filter(ImageFilter.GaussianBlur(max(3, fs // 14))))
    d = ImageDraw.Draw(im)
    for i, l in enumerate(lines): d.text((w / 2, pad + i * ls + fs // 2), l, font=f, fill=col + (255,), anchor="mm", stroke_width=sw, stroke_fill=(8, 8, 10, 255))
    _C[k] = im; return im

def chip(s, fs, fg=CARTA, bg=ROSSO, font="mono", px=34):
    k = ("chip", s, fs, fg, bg, font)
    if k in _C: return _C[k]
    f = F(font, fs); w = int(f.getlength(s)) + 2 * px; h = int(fs * 2.2)
    im = Image.new("RGBA", (w + 24, h + 24), (0, 0, 0, 0)); sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([12, 18, w + 12, h + 18], radius=h // 2, fill=(0, 0, 0, 160)); im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)))
    d = ImageDraw.Draw(im); d.rounded_rectangle([12, 12, w + 11, h + 11], radius=h // 2, fill=bg); d.text((12 + w / 2, 12 + h / 2), s, font=f, fill=fg, anchor="mm")
    _C[k] = im; return im

def ico(nome, s, col=CARTA):
    k = ("ico", nome, s, col)
    if k in _C: return _C[k]
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0)); d = ImageDraw.Draw(im); w = max(6, s // 9); c = col + (255,)
    if nome == "check": d.line([s * .16, s * .55, s * .40, s * .78, s * .86, s * .24], fill=c, width=w * 2, joint="curve")
    elif nome == "cross": d.line([s * .2, s * .2, s * .8, s * .8], fill=c, width=w * 2); d.line([s * .8, s * .2, s * .2, s * .8], fill=c, width=w * 2)
    elif nome == "arrow_down": d.polygon([(s * .38, s * .1), (s * .62, s * .1), (s * .62, s * .55), (s * .85, s * .55), (s * .5, s * .92), (s * .15, s * .55), (s * .38, s * .55)], fill=c)
    elif nome == "arrow_up": d.polygon([(s * .38, s * .9), (s * .62, s * .9), (s * .62, s * .45), (s * .85, s * .45), (s * .5, s * .08), (s * .15, s * .45), (s * .38, s * .45)], fill=c)
    elif nome == "lock":
        d.rounded_rectangle([s * .2, s * .42, s * .8, s * .9], radius=s // 12, fill=c); d.arc([s * .28, s * .1, s * .72, s * .7], 180, 360, fill=c, width=w)
        d.ellipse([s * .43, s * .58, s * .57, s * .72], fill=(20, 20, 24, 255))
    elif nome == "doc":
        d.rounded_rectangle([s * .18, s * .06, s * .82, s * .94], radius=s // 14, fill=c)
        for i in range(5): d.line([s * .3, s * (.26 + .15 * i), s * (.7 if i % 2 == 0 else .58), s * (.26 + .15 * i)], fill=(30, 30, 36, 255), width=max(3, s // 24))
    elif nome == "home":
        d.polygon([(s * .5, s * .08), (s * .94, s * .5), (s * .82, s * .5), (s * .82, s * .9), (s * .18, s * .9), (s * .18, s * .5), (s * .06, s * .5)], fill=c)
        d.rectangle([s * .42, s * .58, s * .58, s * .9], fill=(20, 20, 24, 255))
    elif nome == "pen":
        d.polygon([(s * .12, s * .88), (s * .2, s * .62), (s * .72, s * .1), (s * .9, s * .28), (s * .38, s * .8)], fill=c); d.polygon([(s * .12, s * .88), (s * .2, s * .62), (s * .38, s * .8)], fill=(40, 40, 46, 255))
    elif nome == "coin":
        d.ellipse([s * .06, s * .06, s * .94, s * .94], fill=c); d.ellipse([s * .16, s * .16, s * .84, s * .84], outline=(30, 30, 36, 255), width=max(3, s // 24))
        d.text((s / 2, s / 2), "€", font=F("titolo", int(s * .5)), fill=(30, 30, 36, 255), anchor="mm")
    elif nome == "warn":
        d.polygon([(s * .5, s * .06), (s * .96, s * .9), (s * .04, s * .9)], fill=c); d.text((s / 2, s * .66), "!", font=F("titolo", int(s * .5)), fill=(20, 20, 24, 255), anchor="mm")
    elif nome == "shield":
        d.polygon([(s * .5, s * .04), (s * .9, s * .18), (s * .9, s * .5), (s * .5, s * .96), (s * .1, s * .5), (s * .1, s * .18)], fill=c)
        d.line([s * .3, s * .48, s * .46, s * .64, s * .72, s * .32], fill=(20, 20, 24, 255), width=w * 2, joint="curve")
    elif nome == "car":
        d.polygon([(s * .06, s * .62), (s * .12, s * .46), (s * .3, s * .44), (s * .4, s * .26), (s * .68, s * .26), (s * .8, s * .44), (s * .94, s * .5), (s * .96, s * .66)], fill=c)
        for cx in (.28, .74): d.ellipse([s * (cx - .11), s * .56, s * (cx + .11), s * .78], fill=(20, 20, 24, 255)); d.ellipse([s * (cx - .05), s * .62, s * (cx + .05), s * .72], fill=c)
    _C[k] = im; return im

def put(L, im, cx, cy, a=1.0, sc=1.0, rot=0):
    if a <= 0 or sc <= 0.01: return
    if sc != 1.0: im = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))), Image.BICUBIC)
    if rot: im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
    if a < 1: im = im.copy(); im.putalpha(im.split()[3].point(lambda v: int(v * a)))
    L.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))

def pop(L, im, cx, cy, tl, t0, d=0.4, rot=0, sc=1.0):
    if tl < t0: return
    k = E(tl, t0, d); put(L, im, cx, cy, a=min(1, (tl - t0) / 0.12), sc=k * sc, rot=rot)

def panel(w, h, fill=(18, 19, 23, 235), outline=(70, 72, 78), r=26):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); ImageDraw.Draw(im).rounded_rectangle([0, 0, w - 1, h - 1], radius=r, fill=fill, outline=outline, width=3); return im

def sombra(im): return G.ombra(im)[0]

# ============================================================ sfondi
def vignetta(im, forza=0.55):
    yy, xx = np.mgrid[0:H, 0:W]; r = np.sqrt(((xx - W / 2) / (W * 0.62)) ** 2 + ((yy - H / 2) / (H * 0.62)) ** 2)
    v = Image.fromarray((np.clip(r - 0.45, 0, 1) * 255 * forza * 1.6).clip(0, 220).astype("uint8")); nero = Image.new("RGBA", (W, H), (0, 0, 0, 0)); nero.putalpha(v); im.alpha_composite(nero); return im

def sfondo_scuro(tinta):
    base = np.zeros((H, W, 3), np.float32); yy = np.linspace(0, 1, H)[:, None]
    c0 = {"n": (26, 28, 34), "r": (58, 14, 14), "g": (10, 40, 28), "b": (14, 24, 52), "y": (44, 36, 8)}[tinta]
    base[:] = np.array(c0, np.float32) * (1.15 - 0.75 * yy)[..., None]
    g = Image.fromarray(np.clip(base, 0, 255).astype("uint8")).convert("RGBA"); d = ImageDraw.Draw(g)
    for x in range(0, W, 80): d.line([x, 0, x, H], fill=(255, 255, 255, 9), width=1)
    for y in range(0, H, 80): d.line([0, y, W, y], fill=(255, 255, 255, 9), width=1)
    return vignetta(g, 0.7)

def sfondo_foto(nome, dim=0.62, tinta=(10, 14, 30)):
    im = Image.open(os.path.join(AI, nome + ".jpg")).convert("RGB").crop((32, 0, 992, 540)).resize((2400, 1350), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 60, 3))
    im = ImageEnhance.Contrast(im).enhance(1.12); im = ImageEnhance.Brightness(im).enhance(dim)
    t = Image.new("RGB", im.size, tinta); im = Image.blend(im, t, 0.18)
    return im

# ============================================================ tempi: parole -> secondi
def parole(b): return COP[b].split()
def norm(w): return re.sub(r"[^a-z0-9àèéìòù]", "", w.lower().replace("'", ""))
def tempi_parole(b, s, e):
    ws = parole(b); wt = []
    for w in ws:
        p = 0
        if w.endswith((",", ";", ":")): p = 4
        if w.endswith((".", "?", "!")): p = 9
        wt.append((max(2, len(norm(w))), p))
    tot = sum(a + p for a, p in wt); t = s; out = []
    for a, p in wt:
        out.append(t); t += (a + p) / tot * (e - s)
    return out

# ============================================================ i beat (scene). bg: ("d",tinta) | ("f",foto,dim) | ("desk",) | ("deskf",)
def B(b, cue, x, bg, dur_min=0, **kw): return dict(b=b, cue=cue, x=x, bg=bg, **kw)
def it(*a): return a                                                              # voce di elenco elementi

BEATS = [
    # ---- 0 gancio
    B(0, None, "std", ("f", "piazzale", .72), flash=1, items=[
        ("t", "199 € al mese", 150, GIALLO, 960, 480, 0.15, "titolo"), ("t", "per un'auto nuova", 66, CARTA, 960, 640, Q("Per un'auto nuova"), "corpo")]),
    B(0, "Sembra il prezzo giusto", "std", ("f", "chiavi", .7), items=[
        ("ico", "check", 190, 960, 410, 0.1, VERDE), ("t", "SEMBRA GIUSTO", 120, CARTA, 960, 640, 0.35, "titolo")]),
    B(0, "Ma in questo contratto", "std", ("f", "lente", .6), shake=0.0, items=[
        ("t", "UNA RIGA", 190, ROSSO, 960, 330, 0.2, "titolo"), ("t", "può costarti migliaia di euro", 66, CARTA, 960, 860, Q("può costarti migliaia"), "corpo")]),
    B(0, "Il contatore qui sopra", "hero0", ("d", "r"), flash=1),
    # ---- 1 apertura
    B(1, None, "cart", ("deskf",), flash=1),
    B(1, "È il contratto che oggi", "std", ("f", "firma", .66), items=[
        ("t", "IL CONTRATTO PIÙ FIRMATO", 96, CARTA, 960, 420, 0.2, "titolo"), ("t", "in concessionaria", 76, GIALLO, 960, 560, Q("in concessionaria"), "corpo")]),
    B(1, "Dentro ci sono tre trappole", "tre", ("d", "n"), cues=dict(a=Q("Dentro ci sono tre"), b=Q("trappole"), c=Q("E la terza"))),
    # ---- 2 numeri
    B(2, None, "std", ("f", "strada", .66), items=[
        ("t", "L'AUTO COSTA", 70, CARTA, 960, 340, 0.1, "corpo"), ("num", 21900, 190, GIALLO, 960, 520, 0.25, 1.1)]),
    B(2, "Versi tremila euro", "barsplit", ("d", "b"), cues=dict(a=Q("Versi tremila"), b=Q("Restano"))),
    B(2, "Il venditore ti propone", "rate35", ("d", "n"), n=35, step=0.07),
    B(2, "Fin qui, tutto chiaro", "std", ("f", "coppia", .66), items=[
        ("t", "FIN QUI TUTTO CHIARO?", 120, GIALLO, 960, 300, 0.1, "titolo"), ("ico", "warn", 150, 960, 760, 0.7, GIALLO)]),
    # ---- 3 trappola 1
    B(3, None, "titlecard", ("d", "r"), num="1", flash=1, thud=0.05),
    B(3, "Il prezzo che vedi non è", "versus", ("d", "n"), cues=dict(a=Q("Il prezzo che vedi non è il prezzo"), b=Q("che paghi"))),
    B(3, "Sul foglio trovi", "sheet", ("desk",), foglio="tan", reveal=[0.3, 0.6, 0.9, 1.1], circ=[(0, Q("Il TAN")), (1, Q("E il TAEG"))]),
    B(3, "Il TAN, sei virgola", "gauge2", ("d", "n"), cues=dict(l=Q("Il TAN"), r=Q("E il TAEG"))),
    B(3, "Sembrano simili", "noteq", ("d", "r"), cues=dict(q=Q("Non lo sono")), thud=Q("Non lo sono")),
    # ---- 4 TAN/TAEG
    B(4, None, "iceberg", ("d", "b"), cues=dict(pan=Q("Il TAEG invece"), a=Q("Le spese di istruttoria")), flash=1),
    B(4, "Le spese di incasso", "std", ("f", "calcolatrice", .62), items=[
        ("t", "INCASSO RATA", 76, CARTA, 960, 300, 0.1, "corpo"), ("t", "3,50 € × 35 rate", 120, GIALLO, 960, 470, 0.25, "titolo"),
        ("t", "= 122,50 €", 150, ROSSO, 960, 680, Q("L'imposta di bollo") if False else 1.4, "titolo"), ("t", "+ imposta di bollo", 70, CARTA, 960, 860, Q("L'imposta di bollo"), "corpo")]),
    B(4, "In questo esempio sono", "tot488", ("d", "r"), cues=dict(a=Q("In questo esempio")), cont=(0, 488, Q("In questo esempio"))),
    # ---- 5 regola
    B(5, None, "regola", ("d", "g"), cues=dict(x=Q("Mai il TAN"))),
    B(5, "E chiedi il modulo SECCI", "secci", ("desk",)),
    B(5, "Per legge te lo devono", "timeline", ("d", "g")),
    # ---- 6 trappola 2
    B(6, None, "titlecard", ("d", "r"), num="2", flash=1, thud=0.05),
    B(6, "La rata è bassa per", "rate35", ("d", "n"), n=35, step=0.045, ghost=Q("Dopo le trentacinque")),
    B(6, "La maxirata", "torre", ("d", "r"), cues=dict(a=Q("Quindicimilanovecentocinquantasette")), thud=Q("Quindicimilanovecentocinquantasette"), shake_at=Q("Quindicimilanovecentocinquantasette")),
    # ---- 7 debito
    B(7, None, "std", ("f", "clessidra", .7), items=[("t", "3 ANNI", 230, GIALLO, 960, 380, 0.1, "titolo"), ("t", "quasi 16.000 € di debito", 80, CARTA, 960, 640, Q("quei quasi sedicimila"), "corpo")]),
    B(7, "E per tre anni, su quel", "coins", ("f", "preoccupato", .6)),
    B(7, "Con una rata normale", "chart", ("d", "n"), cues=dict(g=Q("Con una rata normale"), r=Q("Con la maxirata"), z=Q("non scende mai"))),
    # ---- 8 conto finale
    B(8, None, "somma", ("d", "n"), cues=dict(a=Q("Tremila di anticipo"), b=Q("più trentacinque rate"), c=Q("più le spese"), d=Q("più la maxirata"), t=Q("Totale"))),
    B(8, "Per un'auto che ne costava", "barscmp", ("d", "b"), cues=dict(a=Q("Per un'auto che ne costava"), b=Q("Sono quattromila")), cont=(488, 4160, Q("Sono quattromila"))),
    B(8, "Sono quattromilacento", "std", ("f", "banconote", .55), items=[("t", "+ 4.160 €", 260, ROSSO, 960, 470, 0.1, "titolo"), ("t", "IN PIÙ", 100, CARTA, 960, 700, 0.5, "titolo")], cont=(488, 4160, 0.2), shake=0.1),
    # ---- 9 indovina
    B(9, None, "std", ("f", "stretta", .62), items=[("t", "ORA TOCCA A TE", 170, GIALLO, 960, 400, 0.1, "titolo"), ("t", "?", 400, ROSSO, 960, 700, 0.5, "titolo")], flash=1),
    B(9, "Ti do tre possibilità", "cards3", ("d", "y"), cues=dict(a=Q("A: la paga"), b=Q("B: restituisce"), c=Q("C: la rifinanzia"))),
    B(9, "Scrivi la tua risposta", "comment", ("d", "n")),
    # ---- 10 trappola 3
    B(10, None, "titlecard", ("d", "r"), num="3", flash=1, thud=0.05),
    B(10, "Quando arriva la maxirata", "conto", ("d", "n"), cues=dict(a=Q("molti non hanno"))),
    B(10, "Restituire l'auto non", "std", ("f", "auto_vecchia", .6), items=[
        ("chip", "LIMITI DI CHILOMETRI", 44, CARTA, ROSSO, 960, 330, Q("limiti di chilometri")), ("chip", "CONTROLLI SUI DANNI", 44, INCH, GIALLO, 960, 470, Q("controlli sui danni"))]),
    B(10, "Così si firma un nuovo", "std", ("f", "firma", .6), items=[("stamp", "NUOVO PRESTITO", ROSSO, 120, 960, 520, Q("solo per pagare"), -6)], thud=Q("solo per pagare")),
    # ---- 11 rifinanziamento
    B(11, None, "sheet", ("desk",), foglio="f12", reveal=[0.3, 0.9, 1.5, 2.0], circ=[(3, Q("Altri duemila"))]),
    B(11, "Altri duemila", "std", ("d", "r"), items=[("t", "+ 2.922 €", 250, ROSSO, 960, 450, 0.1, "titolo"), ("t", "DI INTERESSI IN PIÙ", 80, CARTA, 960, 680, 0.45, "titolo")], cont=(4160, 7082, 0.2), thud=0.1),
    B(11, "E intanto l'auto ha sette", "valore", ("f", "rottamaio", .55), cues=dict(a=Q("vale molto meno"))),
    # ---- 12 contatore finale
    B(12, None, "hero12", ("d", "r"), cues=dict(a=Q("Spese nascoste"), b=Q("Interessi del"), c=Q("Rifinanziamento della"), t=Q("Totale")), thud=Q("Totale"), flash=1),
    B(12, "Per un'auto da", "receipt", ("deskf",)),
    # ---- 13-15 mosse
    B(13, None, "std", ("d", "g"), flash=1, items=[("t", "COME EVITARLE", 140, CARTA, 960, 380, 0.1, "titolo"), ("t", "3 MOSSE", 230, VERDEC, 960, 620, 0.3, "titolo"),
                                                      ("ico", "shield", 150, 520, 860, 0.5, VERDE), ("ico", "shield", 150, 960, 860, 0.7, VERDE), ("ico", "shield", 150, 1400, 860, 0.9, VERDE)]),
    B(13, "Prima mossa", "check", ("d", "g"), mossa=1, righe=[("Confronta il TAEG e il costo totale", Q("confronta sempre")), ("Chiedi il modulo SECCI e portalo a casa", Q("Chiedi il modulo")), ("Nessuna firma il giorno stesso", Q("Nessuna firma"))]),
    B(14, None, "std", ("f", "calendario", .6), items=[("t", "MOSSA 2", 120, VERDEC, 960, 330, 0.1, "titolo"), ("t", "DECIDI OGGI", 190, CARTA, 960, 560, 0.3, "titolo"), ("t", "cosa farai con la maxirata", 66, GIALLO, 960, 770, Q("cosa farai"), "corpo")]),
    B(14, "Se sai già che", "fork", ("d", "n"), cues=dict(r=Q("chiedi un finanziamento classico"))),
    B(14, "La rata è più alta", "chart", ("d", "g"), cues=dict(g=Q("ma il debito scende")), solo_verde=True),
    B(15, None, "std", ("d", "g"), flash=1, items=[("t", "MOSSA 3", 120, VERDEC, 960, 300, 0.1, "titolo"), ("ico", "shield", 260, 960, 560, 0.3, VERDE), ("t", "I TUOI DIRITTI", 150, CARTA, 960, 860, 0.5, "titolo")]),
    B(15, "Hai quattordici giorni", "cal14", ("d", "n")),
    B(15, "E puoi estinguere", "loan", ("d", "b"), cues=dict(a=Q("con la riduzione")), thud=Q("con la riduzione")),
    B(15, "Le polizze facoltative", "toggle", ("d", "n"), cues=dict(a=Q("puoi rifiutarle"))),
    # ---- 16 verdetto
    B(16, None, "scales", ("d", "n"), cues=dict(a=Q("Conviene a chi"), b=Q("Ma per chi vuole")), flash=1),
    B(16, "Ma per chi vuole tenerla", "std", ("f", "preoccupato", .5), items=[("t", "SE VUOI TENERLA", 120, CARTA, 960, 330, 0.1, "titolo"), ("t", "e non hai la maxirata", 66, GIALLO, 960, 450, Q("e non ha la maxirata"), "corpo"),
                                                                         ("stamp", "NON CONVIENE", ROSSO, 150, 960, 700, Q("non conviene"), -7)], thud=Q("non conviene")),
    # ---- 17-18
    B(17, None, "cartella2", ("f", "bolletta", .62), flash=1),
    B(17, "E lì c'è una voce", "std", ("f", "lente", .55), items=[("t", "UNA VOCE", 200, ROSSO, 960, 380, 0.1, "titolo"), ("t", "che pochi controllano", 80, CARTA, 960, 620, 0.5, "corpo")]),
    B(18, None, "disc", ("d", "n")),
]

# ============================================================ scena
class V3:
    def __init__(self, bl):
        self.bl = bl; self.beats = self.risolvi(bl)
        self.starts = [b["t0"] for b in self.beats]
        self.desk = G.scrivania(0.92); self.desk_b = self.desk.filter(ImageFilter.GaussianBlur(7))
        self.dark = {k: sfondo_scuro(k) for k in "nrgby"}
        self.foto = {}
        self.grana = [Image.effect_noise((W // 2, H // 2), 22).resize((W, H)).convert("L") for _ in range(6)]
        S = SC0.__new__(SC0); S.b = bl
        self.f = {"tan": R.foglio_righe("Contratto di finanziamento", [("Tasso (TAN)", "6,95%"), ("TAEG", "8,26%"), ("Rate", "35 x 199 €"), ("Maxirata", "€ 15.957")])[:2],
                  "f12": R.foglio_righe("Rifinanziamento maxirata", [("Importo", "€ 15.957"), ("Durata", "48 mesi"), ("Tasso (TAN)", "8,5%"), ("Interessi in più", "€ 2.922")], testa="NUOVO PRESTITO")[:2]}
        self.secci, _ = R.foglio_righe("Modulo SECCI", [("Informazioni europee", "di base"), ("sul credito ai", "consumatori"), ("TAEG", "8,26%"), ("Costo totale", "€ 4.160")], evid="TAEG", testa="PRIMA DELLA FIRMA", nota="Va consegnato prima di firmare (Testo Unico Bancario)")
        S.cartellina = SC0.cartellina.__get__(S); S.scontrino = SC0.scontrino.__get__(S)
        self.cart1 = S.cartellina("001", "FINANZIAMENTO AUTO", "Rata: 199 € al mese… dove sta il trucco?")
        self.cart2 = S.cartellina("002", "BOLLETTA DELLA LUCE", "La voce che pochi controllano")
        self.scontrino13 = S.scontrino([("1  Spese nascoste", "488"), ("2  Interessi", "3.672"), ("3  Rifinanziamento", "2.922")], ("TOTALE IN PIÙ", "7.082"), "Grazie per non aver firmato.")
        self.post1 = G.postit("chiedilo\nPRIMA!", 290)
        self.ind = [R.card(l, s, INCH if l != "C" else ROSSO, 440, 300, 120) for l, s in (("A", "la paga"), ("B", "restituisce l'auto"), ("C", "la rifinanzia"))]
        self.disc = SC0.disclaimer(S)
        self.rulli = {}

    # ---------- tempi
    def risolvi(self, bl):
        wt = [tempi_parole(b, *bl[b]) for b in range(len(bl))]; out = []
        for b0 in BEATS:
            b = b0["b"]; s, e = bl[b]
            if b0["cue"] is None: t0 = s
            else:
                t0 = self.cerca(wt[b], b, b0["cue"], s) - 0.12
                t0 = min(max(t0, s + 1.0), e - 0.8)
            out.append(dict(b0, t0=t0, wt=wt[b], s=s, e=e))
        for i, x in enumerate(out):
            nxt = out[i + 1]["t0"] if i + 1 < len(out) else None
            same = i + 1 < len(out) and out[i + 1]["b"] == x["b"]
            x["t1"] = nxt - 0.0 if nxt is not None else x["e"] + 1.2
            if not same and nxt is not None: x["t1"] = nxt - 0.05
        for x in out:
            P = self.q(x, x); x.update(P); x["P"] = P
        return out

    def cerca(self, wt, b, cue, s):
        ws = [norm(w) for w in parole(b)]; c = [norm(w) for w in cue.split()]
        for i in range(len(ws) - len(c) + 1):
            if ws[i:i + len(c) - 1] == c[:-1] and ws[i + len(c) - 1].startswith(c[-1]): return wt[i]
        raise SystemExit(f"cue non trovata nel blocco {b+1}: {cue!r}")
    def q(self, x, _):
        def r(v):
            if isinstance(v, Q): return max(0.0, self.cerca(x["wt"], x["b"], str(v), x["s"]) - 0.1 - x["t0"])
            if isinstance(v, dict): return {k: r(w) for k, w in v.items()}
            if isinstance(v, (list, tuple)): return type(v)(r(w) for w in v)
            return v
        return {k: r(v) for k, v in x.items() if k not in ("wt",)}

    def eventi_audio(self):
        ev = []
        for x in self.beats:
            if x["t0"] > 0.5: ev.append(("whoosh", x["t0"] - 0.03, 1.0))
            P = x["P"]
            def raccogli(v, k=""):
                if isinstance(v, dict):
                    for kk, w in v.items(): raccogli(w, kk)
                elif isinstance(v, (list, tuple)):
                    for w in v: raccogli(w, k)
                elif isinstance(v, float) and k in ("a", "b", "c", "d", "l", "r", "g", "t", "q", "x", "pan", "z") and v > 0.05: ev.append(("pop", x["t0"] + v, 0.8))
            raccogli(P.get("cues", {}))
            for key in ("thud", "shake_at"):
                v = P.get(key)
                if isinstance(v, float) and v > 0: ev.append(("thud", x["t0"] + v, 1.0)) if key == "thud" else None
            if P.get("x") == "titlecard": ev.append(("thud", x["t0"] + 0.1, 1.0))
            for item in P.get("items", []):
                tt = item[6] if item[0] == "t" else None
                if item[0] == "stamp": ev.append(("stamp", x["t0"] + item[5] if False else x["t0"] + item[-2], 1.0))
            if P.get("cont"):
                c = P["cont"]; t0 = x["t0"] + (c[2] if isinstance(c[2], float) else 0.2)
                for k in range(14): ev.append(("tic", t0 + k * (0.05 + 0.011 * k), 0.8))
        return ev

    # ---------- sfondo
    def bg(self, b, tl, dur, i):
        k = b["bg"]
        if k[0] == "d": return self.dark[k[1]].copy()
        if k[0] == "desk": return Image.blend(self.desk, self.desk_b, .85)
        if k[0] == "deskf": return self.desk.copy()
        nome, dim = k[1], k[2]
        if nome not in self.foto: self.foto[nome] = sfondo_foto(nome, dim)
        im = self.foto[nome]; rnd = random.Random(i * 7 + 3); z0 = rnd.choice([1.25, 1.42]); z1 = 1.67 - z0 + 0.0 if z0 > 1.3 else 1.45
        z0, z1 = (1.25, 1.42) if rnd.random() < .5 else (1.42, 1.25)
        u = tl / max(dur, 0.5); z = lerp(z0, z1, u); vw = 2400 / z; vh = vw * 9 / 16
        px = rnd.choice([-1, 1]) * 90 * (u - 0.5); py = rnd.choice([-1, 1]) * 40 * (u - 0.5)
        cx = 1200 + px; cy = 675 + py
        fr = im.crop((int(cx - vw / 2), int(cy - vh / 2), int(cx + vw / 2), int(cy + vh / 2))).resize((W, H), Image.BILINEAR).convert("RGBA")
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sh.putalpha(self.grad_basso()); fr.alpha_composite(sh); return vignetta(fr, .5)
    def grad_basso(self):
        if "gb" not in _C: _C["gb"] = Image.fromarray((np.linspace(0, 1, H)[:, None] ** 2.2 * 150 * np.ones((1, W))).astype("uint8"))
        return _C["gb"]

    # ---------- frame
    def frame(self, t):
        i = max(0, bisect.bisect_right(self.starts, t) - 1); b = self.beats[i]; tl = t - b["t0"]; dur = b["t1"] - b["t0"]
        P = b
        img = self.bg(b, tl, dur, i); L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        getattr(self, "x_" + b["x"])(L, tl, dur, P)
        for item in b.get("items", []): self.item(L, tl, item)
        if b.get("cont"): self.cont_small(L, tl, dur, b)
        sl = A(tl, 0, 0.28)
        if i > 0 and b["b"] != self.beats[i - 1]["b"] or i == 0: pass
        img.alpha_composite(L)
        # fine scena: dissolvenza veloce verso la prossima
        # camera
        punch = 0.075 * (1 - ease(tl / 0.30)) if tl < 0.3 else 0.0
        z = 1.0 + punch + 0.035 * min(1, tl / max(dur, 1))
        sx = sy = 0.0
        sa = b.get("shake_at")
        if isinstance(sa, float) and tl >= sa and tl < sa + 0.55:
            k = (1 - (tl - sa) / 0.55); sx = math.sin(tl * 90) * 16 * k; sy = math.cos(tl * 77) * 12 * k
        th = b.get("thud")
        if isinstance(th, float) and tl >= th and tl < th + 0.4:
            k = (1 - (tl - th) / 0.4); sx += math.sin(tl * 80) * 12 * k; sy += math.cos(tl * 70) * 10 * k
        cw, ch = W / z, H / z
        fr = img.convert("RGB").crop(((W - cw) / 2 + sx, (H - ch) / 2 + sy, (W + cw) / 2 + sx, (H + ch) / 2 + sy)).resize((W, H), Image.BICUBIC)
        arr = np.asarray(fr, np.int16)
        fl = 0.0
        if b.get("flash") and tl < 0.16: fl = 0.35 * (1 - tl / 0.16)
        if isinstance(th, float) and 0 <= tl - th < 0.12: fl = max(fl, 0.25 * (1 - (tl - th) / 0.12))
        if t < 0.5: arr = (arr * ease(t / 0.5)).astype(np.int16)
        if fl: arr = arr + (255 - arr) * fl
        g = (np.asarray(self.grana[int(t * FPS) % 6], np.int16) - 128) * 0.06
        return Image.fromarray(np.clip(arr + g[..., None], 0, 255).astype(np.uint8))

    # ---------- elementi
    def item(self, L, tl, it_):
        k = it_[0]
        if k == "t":
            _, s, fs, col, x, y, t0, font = it_; pop(L, tx(s, fs, col, font), x, y, tl, t0)
        elif k == "chip":
            _, s, fs, fg, bg, x, y, t0 = it_; pop(L, chip(s, fs, fg, bg), x, y, tl, t0)
        elif k == "ico":
            _, n, s, x, y, t0, col = it_; pop(L, ico(n, s, col), x, y, tl, t0)
        elif k == "num":
            _, v, fs, col, x, y, t0, dd = it_
            if tl >= t0: pop(L, tx(fmt(v * ease((tl - t0) / dd)) + " €", fs, col), x, y, tl, t0, 0.2)
        elif k == "stamp":
            _, s, col, fs, x, y, t0, rot = it_
            if tl >= t0:
                kk = min(1, (tl - t0) / 0.16); sc = lerp(1.8, 1.0, kk * kk); put(L, G.timbro(s, col, fs, 5), x, y, a=0.4 + 0.6 * kk, sc=sc, rot=rot)

    def cont_small(self, L, tl, dur, b):
        da, a_, cue = b["cont"]; t0 = cue if isinstance(cue, float) else 0.2
        x = ease((tl - t0) / 1.6) if tl >= t0 else 0.0
        rul = R.rulli_valore(int(da), int(a_), x)
        c = D.contatore_animato(rul, tl + b["t0"], label="STAI PERDENDO")
        c = c.resize((int(c.width * .6), int(c.height * .6)), Image.LANCZOS); a = A(tl, 0.0, 0.3) * (1 - A(tl, dur - 0.25, 0.25))
        put(L, sombra(c), W - c.width / 2 - 60, 36 + c.height / 2, a)

    # =================== scene speciali
    def x_std(self, L, tl, dur, P): pass

    def x_cart(self, L, tl, dur, P):
        k = E(tl, 0.0, 0.6); put(L, sombra(self.cart1), 960, 520 + (1 - k) * 900, rot=-2)
        pop(L, tx("PRATICA N. 001", 120, GIALLO), 960, 140, tl, 0.7); pop(L, chip("FINANZIAMENTO AUTO + MAXIRATA", 40), 960, 960, tl, 1.4)
        if tl > 1.0: put(L, G.graffetta(170), 1330, 300, rot=8)

    def x_hero0(self, L, tl, dur, P):
        r = [D.Rullo(164 + 11 * k, 15 + 2 * k, 0.6 + 0.2 * k, max(2.0, dur - 2.2) + 0.25 * k, 1.3 * k, facce=11) for k in range(4)]
        c = D.contatore_animato(r, tl)
        a = A(tl, 0.0, 0.5); put(L, sombra(c), 960, 520 + (1 - a) * 140, a)
        pop(L, tx("QUANTO TI COSTA IN PIÙ?", 70, CARTA, "corpo"), 960, 200, tl, 0.2); pop(L, G.pillola("LA CIFRA ESATTA ALLA FINE", ROSSO, 40), 960, 870, tl, max(0.9, dur - 2.2))
    def rull_h(self, key, dur):
        return None
    def x_tre(self, L, tl, dur, P):
        cu = P["cues"]
        for n, (cx, t0) in enumerate(((420, cu["a"]), (960, cu["b"]), (1500, cu["c"]))):
            if tl < t0 - 0.3 and n: pass
            k = E(tl, (0.2 if n == 0 else t0 - 0.2) if True else 0, 0.5); col = ROSSO if n == 2 else GRIGIO
            if tl < (0.2 if n == 0 else max(0.4, t0 - 0.3)): continue
            c = panel(430, 560, (22, 24, 29, 240), col if n == 2 and tl > cu["c"] else (90, 92, 98), 30); d = ImageDraw.Draw(c)
            d.text((215, 90), f"TRAPPOLA {n+1}", font=F("mono", 40), fill=col if n == 2 else GRIGIO, anchor="mm"); d.text((215, 330), "?", font=F("titolo", 260), fill=col if n == 2 else (96, 98, 104), anchor="mm")
            c.alpha_composite(ico("lock", 90, col if n == 2 else GRIGIO), (170, 440)); pul = 1 + (0.05 * math.sin(tl * 9) if n == 2 and tl > cu["c"] else 0)
            put(L, sombra(c), cx, 540 + (1 - k) * 600, sc=pul * k if k < 1 else pul, rot=(-3, 0, 3)[n])
        pop(L, tx("DENTRO CI SONO 3 TRAPPOLE", 70, CARTA, "titolo"), 960, 150, tl, 0.0)

    def x_barsplit(self, L, tl, dur, P):
        cu = P["cues"]; x0, wb = 210, 1500; y = 520; h = 170
        g = A(tl, 0.1, 0.8); total = max(wb * g, 40)
        d = ImageDraw.Draw(L); pop(L, tx("PREZZO AUTO  21.900 €", 70, CARTA), 960, 260, tl, 0.2)
        ant = wb * 3000 / 21900; sp = ease((tl - cu["a"]) / 0.6) if tl >= cu["a"] else 0
        if not sp: d.rounded_rectangle([x0, y, x0 + total, y + h], radius=14, fill=(120, 126, 140, 255))
        else:
            d.rounded_rectangle([x0 + ant, y, max(x0 + ant + 4, x0 + total), y + h], radius=14, fill=GIALLO)
            d.rounded_rectangle([x0, y + 300 * sp, x0 + ant, y + h + 300 * sp], radius=14, fill=VERDE)
            put(L, tx("ANTICIPO 3.000 €", 56, VERDEC, "titolo"), x0 + 260, y + 470, A(tl, cu["a"] + .4))
        if tl >= cu["b"]: pop(L, tx("DA FINANZIARE", 60, CARTA, "corpo"), 1100, y - 70, tl, cu["b"]); pop(L, tx("18.900 €", 190, GIALLO), 1100, y + 420, tl, cu["b"] + .15)

    def x_rate35(self, L, tl, dur, P):
        n = P["n"]; step = P["step"]; ghost = P.get("ghost")
        pop(L, tx("35 RATE × 199 €", 100, CARTA), 960, 130, tl, 0.1)
        cols = 7; tw, th, gx, gy = 190, 110, 20, 18; x0 = (W - (cols * tw + (cols - 1) * gx)) / 2; y0 = 250
        for i in range(n):
            t0 = 0.3 + i * step
            if tl < t0: break
            c = chip("199 €", 40, CARTA, (40, 110, 80) if i < n - 1 else VERDE, "mono", 26) if False else None
            r, cc = divmod(i, cols); tile = _C.get("tile") or self._tile(); put(L, tile, x0 + cc * (tw + gx) + tw / 2, y0 + r * (th + gy) + th / 2, a=min(1, (tl - t0) / 0.1), sc=E(tl, t0, 0.2))
        if ghost is not None and tl >= ghost:
            r, cc = divmod(35, cols); pulse = 0.5 + 0.5 * math.sin((tl - ghost) * 8)
            gh = Image.new("RGBA", (tw, th), (0, 0, 0, 0)); ImageDraw.Draw(gh).rounded_rectangle([0, 0, tw - 1, th - 1], radius=16, outline=ROSSO + (int(120 + 135 * pulse),), width=6)
            ImageDraw.Draw(gh).text((tw / 2, th / 2), "?", font=F("titolo", 70), fill=ROSSO + (255,), anchor="mm"); put(L, gh, 960, 250 + 5 * (th + gy) + th / 2 + 6, 1.0)
    def _tile(self):
        t = Image.new("RGBA", (190, 110), (0, 0, 0, 0)); d = ImageDraw.Draw(t); d.rounded_rectangle([0, 0, 189, 109], radius=16, fill=(30, 100, 74, 255), outline=(70, 190, 140), width=3)
        d.text((95, 55), "199 €", font=F("mono", 44), fill=CARTA, anchor="mm"); _C["tile"] = t; return t

    def x_torre(self, L, tl, dur, P):
        a = P["cues"]["a"]; d = ImageDraw.Draw(L)
        for i in range(35): d.rounded_rectangle([88 + i * 49, 880, 88 + i * 49 + 42, 950], radius=6, fill=(30, 100, 74, 255), outline=(70, 190, 140), width=2)
        pop(L, tx("35 RATE BASSE", 64, VERDEC, "corpo"), 960, 1010, tl, 0.2)
        if tl < a: pop(L, tx("poi arriva l'ultima…", 90, CARTA, "corpo"), 960, 380, tl, 0.3); return
        u = tl - a; y = lerp(-500, 560, min(1, (u / 0.28) ** 2)) + (abs(math.sin(max(0, u - 0.28) * 14)) * -50 * math.exp(-(max(0, u - 0.28)) * 5) if u > 0.28 else 0)
        b = Image.new("RGBA", (1100, 560), (0, 0, 0, 0)); bd = ImageDraw.Draw(b); bd.rounded_rectangle([0, 0, 1099, 559], radius=22, fill=ROSSO + (255,), outline=(255, 120, 110), width=8)
        bd.text((550, 190), "MAXIRATA", font=F("mono", 70), fill=CARTA, anchor="mm"); bd.text((550, 340), "15.957 €", font=F("titolo", 190), fill=CARTA, anchor="mm"); bd.text((550, 480), "tutta in una volta sola", font=F("corpo", 48), fill=(255, 220, 215), anchor="mm")
        put(L, sombra(b), 960, y + 240)

    def x_titlecard(self, L, tl, dur, P):
        n = P["num"]; k = ease(tl / 0.5)
        put(L, tx(n, 1100, (120, 24, 24), "titolo", sw=0, sh=False), 1300, 540, 0.9 * k)
        pop(L, tx("TRAPPOLA", 150, CARTA), 700, 400, tl, 0.1, 0.35); pop(L, tx(f"{n} DI 3", 230, GIALLO), 700, 640, tl, 0.3, 0.35)
        put(L, ico("warn", 170, GIALLO), 1560, 300, A(tl, 0.5, .3) * (0.7 + 0.3 * math.sin(tl * 10)))

    def x_versus(self, L, tl, dur, P):
        cu = P["cues"]; d = ImageDraw.Draw(L); k = ease(tl / 0.4)
        d.rectangle([0, 0, 960 * k, H], fill=(14, 60, 40, 200)); d.rectangle([W - 960 * k, 0, W, H], fill=(70, 14, 14, 215)); d.line([960, 0, 960, H], fill=GIALLO + (255,), width=6)
        pop(L, tx("IL PREZZO\nCHE VEDI", 90, CARTA), 480, 280, tl, 0.2); pop(L, tx("199 €", 220, VERDEC), 480, 640, tl, 0.5); pop(L, tx("al mese", 66, CARTA, "corpo"), 480, 830, tl, 0.7)
        if tl >= cu["b"] - 0.1:
            pop(L, tx("IL PREZZO\nCHE PAGHI", 90, CARTA), 1440, 280, tl, cu["b"] - 0.1)
            r = random.Random(int(tl * 14)); txt = "".join(r.choice("0123456789") for _ in range(2)) + "." + "".join(r.choice("0123456789") for _ in range(3)) + " €" if tl < cu["b"] + 1.4 else "???"
            pop(L, tx(txt, 200, ROSSO), 1440, 650, tl, cu["b"] + 0.1)

    def x_sheet(self, L, tl, dur, P):
        im, pos = self.f[P["foglio"]]; fo = im.copy(); dd = ImageDraw.Draw(fo); rv = P["reveal"]
        for r, yr in enumerate(pos):
            if tl < rv[r]: dd.rectangle([40, yr - 10, fo.width - 40, yr + 60], fill=CARTA)
        k = E(tl, 0.0, 0.55); x0, y0 = 460, 90
        put(L, sombra(fo), x0 + fo.width / 2, y0 + fo.height / 2 + (1 - k) * 1000, rot=-1.2)
        for (row, t0) in P.get("circ", []):
            if tl >= t0:
                lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); yr = y0 + pos[row] + 30
                u = min(1, (tl - t0) / 0.5); n = int(40 * u)
                import math as m
                pts = [(x0 + 530 + 460 * m.cos(a / 40 * 6.5) * 0.98 + 0, yr + 52 * m.sin(a / 40 * 6.5)) for a in range(n + 1)]
                if len(pts) > 1: dl.line(pts, fill=ROSSO + (255,), width=9, joint="curve")
                L.alpha_composite(lay)
        if P["foglio"] == "tan":
            pop(L, tx("DUE PERCENTUALI", 70, CARTA, "titolo"), 960, 990, tl, 0.4)

    def x_gauge2(self, L, tl, dur, P):
        cu = P["cues"]
        for (cx, key, nome, val, col, lab) in ((520, "l", "TAN", 6.95, GRIGIO, "solo interessi"), (1400, "r", "TAEG", 8.26, ROSSO, "tutto compreso")):
            t0 = cu[key] - 0.1; im = Image.new("RGBA", (700, 560), (0, 0, 0, 0)); d = ImageDraw.Draw(im); u = ease((tl - t0) / 1.4) if tl >= t0 else 0
            d.arc([60, 60, 640, 640], 180, 360, fill=(48, 50, 56, 255), width=46); d.arc([60, 60, 640, 640], 180, 180 + 180 * (val / 10) * u, fill=col, width=46)
            ang = math.radians(180 + 180 * (val / 10) * u); d.line([350, 350, 350 + 230 * math.cos(ang), 350 + 230 * math.sin(ang)], fill=CARTA, width=10); d.ellipse([330, 330, 370, 370], fill=CARTA)
            d.text((350, 460), f"{(val * u):.2f}".replace(".", ",") + "%", font=F("titolo", 130), fill=col if key == "r" else CARTA, anchor="mm")
            if tl >= t0: put(L, im, cx, 520, A(tl, t0, 0.2)); pop(L, tx(nome, 120, CARTA), cx, 230, tl, t0); pop(L, tx(lab, 54, GIALLO if key == "r" else GRIGIO, "corpo"), cx, 830, tl, t0 + 0.5)

    def x_noteq(self, L, tl, dur, P):
        q = P["cues"]["q"]; pop(L, tx("6,95%", 190, CARTA), 480, 520, tl, 0.1); pop(L, tx("8,26%", 190, ROSSO), 1440, 520, tl, 0.3)
        if tl < q: pop(L, tx("≈", 220, GRIGIO), 960, 520, tl, 0.6); pop(L, tx("sembrano simili…", 70, CARTA, "corpo"), 960, 800, tl, 0.7)
        else: pop(L, tx("≠", 360, GIALLO), 960, 520, tl, q, 0.25); pop(L, tx("NON LO SONO", 110, CARTA), 960, 850, tl, q + 0.2)

    def x_iceberg(self, L, tl, dur, P):
        cu = P["cues"]
        if "ice" not in _C:
            w = Image.new("RGB", (W, 2200)); a = np.zeros((2200, W, 3), np.float32); yy = np.linspace(0, 1, 2200)[:, None]
            a[:, :, 0] = 20 + 14 * (1 - yy); a[:, :, 1] = 40 + 30 * (1 - yy) ; a[:, :, 2] = 90 + 40 * (1 - yy)
            a[:700] = np.array([(24, 30, 52)]) * 1.0 + (np.linspace(0, 1, 700)[:, None, None] * np.array([(26, 40, 40)]))
            im = Image.fromarray(a.astype("uint8")).convert("RGBA"); d = ImageDraw.Draw(im)
            d.polygon([(690, 700), (800, 470), (900, 520), (990, 380), (1080, 500), (1170, 460), (1260, 700)], fill=(224, 238, 248, 255))
            d.polygon([(990, 380), (1080, 500), (1020, 700), (940, 700), (900, 520)], fill=(190, 214, 235, 255))
            d.polygon([(690, 700), (1260, 700), (1500, 1000), (1420, 1500), (1180, 1850), (900, 1900), (560, 1620), (470, 1150), (560, 880)], fill=(70, 130, 190, 255))
            d.polygon([(900, 1900), (1180, 1850), (1420, 1500), (1100, 1300), (800, 1500)], fill=(40, 90, 150, 255))
            d.rectangle([0, 700, W, 701], fill=(180, 220, 255, 255)); _C["ice"] = vignetta(im, 0.5)
        pan = ease((tl - cu["pan"]) / 1.0) if tl >= cu["pan"] else 0
        cam = lerp(150, 1050, pan); L.alpha_composite(_C["ice"].crop((0, int(cam), W, int(cam) + H)))
        wy = lambda y: y - cam
        pop(L, tx("TAN", 130, CARTA), 480, wy(430), tl, 0.2); pop(L, tx("solo interessi", 60, GIALLO, "corpo"), 480, wy(550), tl, 0.5)
        if pan > 0:
            pop(L, tx("TAEG: TUTTO", 130, CARTA), 960, wy(1120), tl, cu["pan"] + 0.5)
        for j, (s, y) in enumerate((("ISTRUTTORIA  350 €", 1250), ("INCASSO RATE", 1360), ("IMPOSTA DI BOLLO", 1470))):
            t0 = (cu["a"] if j == 0 else cu["a"] + 3.1 * j)
            if j == 0 and tl >= t0: pop(L, chip(s, 40, INCH, GIALLO), 960, wy(y), tl, t0)
            elif j > 0 and tl >= min(t0, dur - 1.0): pop(L, chip(s, 40, INCH, GIALLO), 960, wy(y), tl, min(t0, dur - 1.0))
        pop(L, tx("NELLA RATA NON LI VEDI", 54, ROSSO, "corpo"), 960, wy(1620), tl, max(cu["pan"] + 1.0, cu["a"] + 1.5))

    def x_tot488(self, L, tl, dur, P):
        a = P["cues"]["a"]
        for j, (s, v, x) in enumerate((("ISTRUTTORIA", "350 €", 360), ("INCASSO", "122,50 €", 960), ("BOLLO", "16 €", 1560))):
            c = panel(430, 230, (22, 24, 29, 240), (90, 92, 98)); d = ImageDraw.Draw(c); d.text((215, 70), s, font=F("mono", 42), fill=GRIGIO, anchor="mm"); d.text((215, 150), v, font=F("titolo", 74), fill=CARTA, anchor="mm")
            k = ease((tl - a - 0.0) / 0.9) if tl >= a else 0
            put(L, sombra(c), lerp(x, 960, k), lerp(330, 620, k), a=1 - 0.9 * k if k > .9 else 1, sc=1 - .15 * k)
        if tl >= a + 0.9: pop(L, tx("488 €", 330, ROSSO), 960, 600, tl, a + 0.9, 0.3); pop(L, tx("che nella rata non vedi", 72, CARTA, "corpo"), 960, 820, tl, a + 1.2)

    def x_regola(self, L, tl, dur, P):
        x = P["cues"]["x"]; pop(L, chip("LA REGOLA", 54, CARTA, VERDE), 960, 150, tl, 0.1)
        pop(L, tx("GUARDA SEMPRE", 120, CARTA), 960, 330, tl, 0.3); pop(L, tx("IL TAEG", 330, VERDEC), 960, 600, tl, 0.6); put(L, ico("check", 180, VERDE), 1560, 640, A(tl, 1.0, .2), E(tl, 1.0, .4))
        if tl >= x:
            c = tx("TAN", 150, GRIGIO); put(L, c, 360, 700, 1.0); k = ease((tl - x) / .25); put(L, ico("cross", 260, ROSSO), 360, 700, k)
            pop(L, tx("mai da solo", 54, GIALLO, "corpo"), 360, 860, tl, x + .2)

    def x_secci(self, L, tl, dur, P):
        k = E(tl, 0.0, 0.55); put(L, sombra(self.secci), 760, 530 + (1 - k) * 1000, rot=-1.5)
        pop(L, sombra(self.post1), 1560, 640, tl, 0.9, 0.4, rot=-7); pop(L, chip("MODULO SECCI", 56), 1500, 190, tl, 0.3)

    def x_timeline(self, L, tl, dur, P):
        d = ImageDraw.Draw(L); xs = (400, 960, 1520); y = 560; u = ease(tl / (dur - 1.2))
        d.line([xs[0], y, xs[2], y], fill=(70, 72, 78, 255), width=14); d.line([xs[0], y, lerp(xs[0], xs[2], u), y], fill=VERDE + (255,), width=14)
        for j, (n, lab) in enumerate((("doc", "MODULO SECCI"), ("home", "PORTALO A CASA"), ("pen", "FIRMA"))):
            t0 = 0.2 + j * dur * 0.3; col = VERDEC if (j < 2) else ROSSO
            pop(L, ico(n, 190, col), xs[j], y - 40, tl, t0); pop(L, tx(lab, 54, CARTA, "corpo"), xs[j], y + 170, tl, t0 + .15)
        pop(L, chip("PER LEGGE, PRIMA DELLA FIRMA", 46, INCH, GIALLO), 960, 190, tl, 0.1)

    def x_coins(self, L, tl, dur, P):
        rnd = random.Random(5)
        for i in range(34):
            x = rnd.uniform(160, 1760); t0 = rnd.uniform(0.2, max(0.4, dur - 1.0)); v = rnd.uniform(500, 900); s = rnd.uniform(80, 140)
            if tl >= t0: put(L, ico("coin", int(s), GIALLO), x, -100 + (tl - t0) * v, 0.95, rot=(tl - t0) * 120)
        pop(L, tx("INTERESSI", 210, ROSSO), 960, 400, tl, 0.1); pop(L, tx("per tre anni", 90, CARTA, "corpo"), 960, 620, tl, 0.5)

    def x_chart(self, L, tl, dur, P):
        cu = P["cues"]; solo = P.get("solo_verde"); pan = panel(1500, 800, (18, 19, 23, 238)); d = ImageDraw.Draw(pan); gw, gh = 1500, 800
        d.text((50, 36), "DEBITO RESIDUO", font=F("mono", 34), fill=GRIGIO); ox, oy, aw, ah = 120, 700, 1320, 560
        d.line([ox, oy, ox + aw, oy], fill=(90, 92, 98), width=3); d.line([ox, oy, ox, oy - ah], fill=(90, 92, 98), width=3)
        for m in (0, 12, 24, 36): d.text((ox + aw * m / 36, oy + 16), str(m), font=F("mono2", 26), fill=GRIGIO, anchor="ma")
        d.text((ox + aw, oy + 54), "mesi", font=F("mono2", 26), fill=GRIGIO, anchor="ra")
        i_ = 0.0695 / 12; de = 19250.0; R_ = 199; dm = [de]; db = [de]; Rn = de * i_ / (1 - (1 + i_) ** -36)
        for m in range(36): dm.append(dm[-1] * (1 + i_) - (R_ if m < 35 else dm[-1] * (1 + i_))); db.append(max(0, db[-1] * (1 + i_) - Rn))
        sy = lambda v: oy - ah * v / 20000
        def linea(serie, col, frac, w):
            n = int(36 * min(1, frac)); pts = [(ox + aw * m / 36, sy(serie[m])) for m in range(n + 1)]
            if len(pts) > 1: d.line(pts, fill=col, width=w, joint="curve")
        k1 = ease((tl - cu["g"]) / 1.8) if tl >= cu["g"] else 0
        linea(db, VERDEC, k1, 10)
        if not solo:
            k2 = ease((tl - cu["r"]) / 1.8) if tl >= cu["r"] else 0; linea(dm, ROSSO, k2, 12)
            if k1 >= 1: d.text((ox + aw * 0.42, sy(db[16]) + 34), "rata normale: scende", font=F("corpo", 40), fill=VERDEC)
            if k2 >= 1: d.text((ox + aw * 0.30, sy(dm[14]) - 90), "con maxirata: NON scende", font=F("corpo", 40), fill=ROSSO)
        else:
            if k1 >= 1: d.text((ox + aw * 0.42, sy(db[16]) + 34), "finanziamento classico", font=F("corpo", 40), fill=VERDEC)
        put(L, sombra(pan), 960, 560 + (1 - E(tl, 0, 0.5)) * 900)
        if not solo and tl >= cu["z"]: pop(L, chip("NON SCENDE MAI", 56), 1300, 190, tl, cu["z"])
        if solo: pop(L, chip("DEBITO CHE SCENDE DAVVERO", 52, CARTA, VERDE), 960, 130, tl, 0.3); put(L, ico("arrow_up", 100, GIALLO), 400, 140, A(tl, .6) * .0 + A(tl, .6))

    def x_somma(self, L, tl, dur, P):
        cu = P["cues"]; pan = panel(1180, 800, (243, 240, 232, 255), (200, 196, 186), 18); d = ImageDraw.Draw(pan)
        d.text((60, 56), "CONTO FINALE", font=F("mono", 44), fill=INCH); y = 150
        for (lab, v, key) in (("Anticipo", "3.000", "a"), ("35 rate × 199", "6.965", "b"), ("Spese e bollo", "138,50", "c"), ("Maxirata", "15.957", "d")):
            if tl >= cu[key] - 0.1: d.text((60, y), lab, font=F("mono2", 46), fill=INCH); d.text((1120, y), v + " €", font=F("mono", 52), fill=INCH, anchor="ra")
            y += 100
        if tl >= cu["t"] - 0.1: d.line([60, 566, 1120, 566], fill=INCH, width=5); d.text((60, 620), "TOTALE", font=F("mono", 60), fill=ROSSO); d.text((1120, 620), "26.060 €", font=F("titolo", 84), fill=ROSSO, anchor="ra")
        put(L, sombra(pan), 960, 540 + (1 - E(tl, 0.0, .5)) * 900, rot=-1)
        if tl >= cu["t"]: pop(L, tx("quasi 26.000 €", 76, GIALLO, "corpo"), 960, 1000, tl, cu["t"] + 0.5)

    def x_barscmp(self, L, tl, dur, P):
        cu = P["cues"]; d = ImageDraw.Draw(L); base = 940; sc = 21.9 / 430; k1 = ease(tl / 0.8)
        d.rounded_rectangle([420, base - 21.9 / sc * k1 * 1.0 * 1, 760, base], radius=10, fill=(150, 156, 170, 255)); pop(L, tx("PREZZO AUTO\n21.900 €", 56, CARTA, "corpo"), 590, base + 0 - 21.9 / sc - 90, tl, 0.6)
        if tl >= cu["a"]:
            k = ease((tl - cu["a"]) / 0.9); h = 26.06 / sc * k; d.rounded_rectangle([1160, base - h, 1500, base], radius=10, fill=(150, 40, 40, 255))
            hh = 21.9 / sc * k; d.rectangle([1160, base - hh, 1500, base], fill=(150, 156, 170, 255)); d.rectangle([1160, base - h, 1500, base - hh], fill=ROSSO)
            pop(L, tx("TOTALE PAGATO\n26.060 €", 56, CARTA, "corpo"), 1330, base - h - 90, tl, cu["a"] + 0.7)
        if tl >= cu["a"] + 1.0: d.line([420, base - 21.9 / sc, 1500, base - 21.9 / sc], fill=GIALLO + (255,), width=5)
        if tl >= cu["b"]: pop(L, tx("+ 4.160 €", 170, ROSSO), 960, 300, tl, cu["b"], 0.3)

    def x_cards3(self, L, tl, dur, P):
        cu = P["cues"]; pop(L, tx("COSA FA LA MAGGIOR PARTE\nDELLE PERSONE?", 78, CARTA), 960, 190, tl, 0.1)
        for j, key in enumerate("abc"):
            pop(L, sombra(self.ind[j]), 330 + j * 630, 600, tl, cu[key] - 0.15, 0.45, rot=(-3, 2, -2)[j])
        if tl >= cu["c"] + 1.2: put(L, ico("lock", 10, CARTA), 0, 0, 0)

    def x_comment(self, L, tl, dur, P):
        pan = panel(1500, 260, (30, 32, 38, 255), (90, 92, 98), 30); d = ImageDraw.Draw(pan); d.ellipse([40, 60, 160, 180], fill=(90, 94, 110)); d.text((100, 120), "Tu", font=F("corpo", 44), fill=CARTA, anchor="mm")
        s = "La risposta è... "; n = int(max(0, tl - 0.5) * 14); d.text((200, 130), (s + "C")[:n], font=F("corpo", 64), fill=CARTA, anchor="lm")
        if int(tl * 2) % 2 == 0: d.rectangle([200 + F("corpo", 64).getlength((s + "C")[:n]) + 6, 90, 200 + F("corpo", 64).getlength((s + "C")[:n]) + 12, 170], fill=GIALLO)
        put(L, sombra(pan), 960, 520, A(tl, 0.0, 0.3), E(tl, 0, 0.45)); pop(L, tx("SCRIVILO NEI COMMENTI", 110, GIALLO), 960, 250, tl, 0.1)
        pop(L, tx("prima della soluzione", 66, CARTA, "corpo"), 960, 780, tl, 0.8)

    def x_conto(self, L, tl, dur, P):
        a = P["cues"]["a"]; c = panel(620, 380, (30, 60, 110, 255), (120, 160, 220), 34); d = ImageDraw.Draw(c)
        d.rounded_rectangle([50, 70, 140, 130], radius=10, fill=(230, 200, 120)); d.text((50, 190), "SALDO CONTO", font=F("mono", 36), fill=(200, 220, 255));
        wid = 520 * (0.14 + 0.02 * math.sin(tl * 3)); d.rounded_rectangle([50, 250, 570, 290], radius=18, fill=(20, 40, 80)); d.rounded_rectangle([50, 250, 50 + wid, 290], radius=18, fill=ROSSO)
        d.text((310, 335), "poco…", font=F("mano", 54), fill=CARTA, anchor="mm")
        put(L, sombra(c), 540, 560, A(tl, 0, .3), E(tl, 0.0, 0.5), rot=-3)
        if tl >= 0.8:
            m = Image.new("RGBA", (640, 400), (0, 0, 0, 0)); md = ImageDraw.Draw(m); md.rounded_rectangle([0, 0, 639, 399], radius=26, fill=ROSSO + (255,), outline=(255, 130, 120), width=6)
            md.text((320, 120), "MAXIRATA", font=F("mono", 60), fill=CARTA, anchor="mm"); md.text((320, 270), "15.957 €", font=F("titolo", 112), fill=CARTA, anchor="mm")
            put(L, sombra(m), lerp(2200, 1380, ease((tl - 0.8) / 0.5)), 540, rot=3)
        if tl >= a: pop(L, ico("cross", 190, ROSSO), 960, 540, tl, a); pop(L, tx("NON BASTA", 100, CARTA), 960, 900, tl, a + 0.2)

    def x_valore(self, L, tl, dur, P):
        a = P["cues"]["a"]; pop(L, chip("L'AUTO HA 7 ANNI", 56, CARTA, (40, 40, 48)), 960, 160, tl, 0.2)
        u = ease((tl - a) / 1.3) if tl >= a else 0; k = tl >= a
        pop(L, tx("VALE\nMOLTO MENO", 190, CARTA), 960, 520 + 40 * u, tl, a - 0.1)
        put(L, ico("arrow_down", 220 + int(40 * math.sin(tl * 7)), ROSSO), 1560, 330 + 260 * u, A(tl, a))
        pop(L, tx("rifinanziata: 4 anni in più", 62, GIALLO, "corpo"), 960, 900, tl, 0.7)

    def x_hero12(self, L, tl, dur, P):
        cu = P["cues"]; rul = R.rulli_valore(7082, None, 0); c = D.contatore_animato(rul, tl + 5.0, label="TOTALE PERSO"); c = c.resize((int(c.width * 1.0), int(c.height * 1.0)), Image.LANCZOS)
        pul = 1 + (0.08 * math.exp(-(tl - cu["t"]) * 6) if tl >= cu["t"] else 0)
        pop(L, tx("ADESSO IL CONTATORE SI FERMA", 74, CARTA, "corpo"), 960, 150, tl, 0.1)
        put(L, sombra(c), 960, 470, A(tl, 0, .3), pul)
        for (key, s, v, x) in (("a", "SPESE NASCOSTE", "488 €", 400), ("b", "INTERESSI", "3.672 €", 960), ("c", "RIFINANZIAMENTO", "2.922 €", 1520)):
            c2 = panel(470, 200, (22, 24, 29, 240), (90, 92, 98)); d = ImageDraw.Draw(c2); d.text((235, 60), s, font=F("mono", 36), fill=GRIGIO, anchor="mm"); d.text((235, 134), v, font=F("titolo", 70), fill=CARTA, anchor="mm")
            pop(L, sombra(c2), x, 860, tl, cu[key] - 0.1, 0.4)
        if tl >= cu["t"]: pop(L, tx("7.082 €", 200, ROSSO), 960, 700, tl, cu["t"], 0.3) if False else None

    def x_receipt(self, L, tl, dur, P):
        k = E(tl, 0.0, 0.55); put(L, sombra(self.scontrino13), 960, 560 + (1 - k) * 1000, rot=-1.5)
        pop(L, tx("per un'auto da 21.900 €", 66, GIALLO, "corpo"), 960, 120, tl, 0.6)

    def x_check(self, L, tl, dur, P):
        pop(L, tx(f"MOSSA {P['mossa']}", 150, VERDEC), 520, 200, tl, 0.1)
        for j, (s, t0) in enumerate(P["righe"]):
            y = 420 + j * 190; k = E(tl, max(0.4, t0 - 0.15), 0.4)
            if tl < max(0.4, t0 - 0.15): box = panel(150, 150, (20, 22, 26, 255), (110, 112, 118), 22); put(L, box, 300, y)
            else:
                box = panel(150, 150, (20, 22, 26, 255), VERDE, 22); put(L, box, 300, y); put(L, ico("check", 130, VERDE), 300, y, A(tl, t0 - 0.1, .2), E(tl, t0 - 0.1, .35))
            pop(L, tx(s, 62, CARTA, "corpo", sh=True), 1060 if len(s) < 40 else 1080, y, tl, max(0.4, t0 - 0.15))

    def x_fork(self, L, tl, dur, P):
        r = P["cues"]["r"]; d = ImageDraw.Draw(L); verde = tl >= r
        d.line([960, 1100, 960, 760, 560, 440, 480, 200], fill=(150, 40, 40, 255) if True else None, width=70, joint="curve")
        d.line([960, 760, 1360, 440, 1440, 200], fill=(40, 130, 90, 255) if verde else (80, 82, 88, 255), width=70, joint="curve")
        pop(L, chip("CON MAXIRATA", 52), 520, 150, tl, 0.2); pop(L, chip("CLASSICO", 52, CARTA, VERDE if verde else (80, 82, 88)), 1400, 150, tl, 0.5)
        pop(L, tx("DECIDI ORA", 110, CARTA), 960, 900, tl, 0.1)
        if verde: put(L, ico("check", 150, VERDEC), 1400, 340, A(tl, r), E(tl, r))
        pop(L, ico("warn", 150, GIALLO), 520, 340, tl, 0.8)

    def x_cal14(self, L, tl, dur, P):
        pop(L, tx("14 GIORNI", 220, CARTA), 960, 180, tl, 0.1); pop(L, tx("per recedere dal contratto", 70, GIALLO, "corpo"), 960, 350, tl, 0.4)
        for i in range(14):
            r, c = divmod(i, 7); x = 330 + c * 210; y = 560 + r * 200; t0 = 0.8 + i * 0.12
            box = panel(180, 160, (24, 26, 31, 255), (90, 92, 98) if tl < t0 else VERDE, 18); d = ImageDraw.Draw(box); d.text((90, 80), str(i + 1), font=F("titolo", 80), fill=CARTA if tl >= t0 else (110, 112, 118), anchor="mm")
            put(L, box, x, y, A(tl, 0, .2))

    def x_loan(self, L, tl, dur, P):
        a = P["cues"]["a"]; d = ImageDraw.Draw(L); pop(L, tx("ESTINZIONE ANTICIPATA", 100, CARTA), 960, 200, tl, 0.1)
        k = ease((tl - a) / 1.0) if tl >= a else 0
        d.rounded_rectangle([260, 440, 1100, 640], radius=22, fill=BLU + (255,)); d.text((680, 540), "DEBITO", font=F("mono", 60), fill=CARTA, anchor="mm")
        x0 = 1100; d.rounded_rectangle([x0, 440 + k * 260, x0 + 560 * (1 - 0.0), 640 + k * 260], radius=22, fill=ROSSO + (int(255 * (1 - 0.6 * k)),)); d.text((x0 + 280, 540 + k * 260), "INTERESSI FUTURI", font=F("mono", 40), fill=CARTA, anchor="mm")
        if tl >= a: pop(L, tx("MENO INTERESSI!", 120, VERDEC), 1380, 330, tl, a + 0.2)
        put(L, ico("arrow_down", 120, VERDEC), 1380, 520 + k * 60, A(tl, a))

    def x_toggle(self, L, tl, dur, P):
        a = P["cues"]["a"]; u = ease((tl - a) / 0.35) if tl >= a else 0
        pop(L, tx("POLIZZE FACOLTATIVE", 100, CARTA), 960, 250, tl, 0.1)
        sw = Image.new("RGBA", (560, 280), (0, 0, 0, 0)); d = ImageDraw.Draw(sw); col = tuple(int(lerp(VERDE[k], (90, 92, 98)[k], u)) for k in range(3))
        d.rounded_rectangle([0, 0, 559, 279], radius=140, fill=col + (255,)); d.ellipse([lerp(300, 20, u), 20, lerp(300, 20, u) + 240, 260], fill=CARTA)
        put(L, sombra(sw), 960, 560, A(tl, 0, .3), E(tl, 0, .5)); pop(L, tx("SÌ" if u < .5 else "NO", 130, CARTA if u < .5 else ROSSO), 960, 780, tl, 0.4)
        if tl >= a: pop(L, tx("PUOI RIFIUTARLE", 80, GIALLO), 960, 950, tl, a + 0.3)

    def x_scales(self, L, tl, dur, P):
        cu = P["cues"]; b = cu["b"]; ang = 0.0
        if tl >= cu["a"]: ang = -10 * ease((tl - cu["a"]) / 0.5) * (1 if tl < b else 0) + (12 * ease((tl - b) / 0.5) if tl >= b else 0) + (0 if tl < b else 10 * ease((tl - b) / 0.5)) * 0
        if tl >= b: ang = lerp(-10, 12, ease((tl - b) / 0.6))
        pop(L, tx("IL VERDETTO", 120, GIALLO), 960, 140, tl, 0.1)
        d = ImageDraw.Draw(L); d.polygon([(930, 900), (990, 900), (975, 360), (945, 360)], fill=(170, 174, 184, 255)); d.rectangle([800, 900, 1120, 930], fill=(170, 174, 184, 255))
        beam = Image.new("RGBA", (1500, 40), (0, 0, 0, 0)); ImageDraw.Draw(beam).rounded_rectangle([0, 0, 1499, 39], radius=18, fill=(200, 204, 214, 255))
        br = beam.rotate(ang, expand=True, resample=Image.BICUBIC); L.alpha_composite(br, (int(960 - br.width / 2), int(360 - br.height / 2)))
        import math as m; hx = 750 * m.cos(m.radians(ang)); hy = -750 * m.sin(m.radians(ang))
        for sgn, lab, col, key in ((-1, "CAMBI AUTO\nOGNI 3 ANNI", VERDE, "a"), (1, "VUOI TENERLA", ROSSO, "b")):
            cx = 960 + sgn * hx; cy = 360 + sgn * hy
            d.line([cx, cy, cx, cy + 220], fill=(170, 174, 184, 255), width=6)
            pan = Image.new("RGBA", (560, 150), (0, 0, 0, 0)); pd = ImageDraw.Draw(pan); pd.rounded_rectangle([0, 0, 559, 149], radius=26, fill=col + (255,)); pd.text((280, 75), lab, font=F("mono", 42), fill=CARTA, anchor="mm")
            if tl >= cu[key] - 0.1: put(L, pan, cx, cy + 300, A(tl, cu[key] - .1, .3))

    def x_cartella2(self, L, tl, dur, P):
        k = E(tl, 0.2, 0.6); put(L, sombra(self.cart2), 960, 600 + (1 - k) * 900, rot=2); pop(L, chip("PROSSIMA PRATICA", 54, INCH, GIALLO), 960, 160, tl, 0.5)

    def x_disc(self, L, tl, dur, P):
        put(L, self.disc, 960, 540, A(tl, 0, .4))

# ============================================================ audio
def audio_fx(dur, sr, ev):
    n = int(dur * sr); y = np.zeros(n, np.float32); rng = np.random.default_rng(5); t = np.arange(n) / sr
    drone = 0.5 * np.sin(2 * np.pi * 55 * t) + 0.3 * np.sin(2 * np.pi * 82.4 * t) + 0.18 * np.sin(2 * np.pi * 110 * t + np.sin(t * 0.3))
    pulse = (0.55 + 0.45 * np.sin(2 * np.pi * (1 / 1.6) * t)) ** 2
    y += 0.05 * drone * (0.6 + 0.4 * pulse) * np.clip(t / 2, 0, 1) * np.clip((dur - t) / 1.5, 0, 1)
    pad = 0.5 * np.sin(2 * np.pi * 220 * t) * np.sin(2 * np.pi * 0.07 * t) ** 2 + 0.4 * np.sin(2 * np.pi * 261.6 * t) * np.sin(2 * np.pi * 0.05 * t + 1) ** 2
    y += 0.012 * pad
    def add(t0, s):
        i0 = int(t0 * sr)
        if i0 < 0 or i0 >= n: return
        e = min(n, i0 + len(s)); y[i0:e] += s[:e - i0]
    for kind, t0, amp in ev:
        if kind == "whoosh":
            m = int(0.42 * sr); k = np.arange(m) / m; ns = rng.standard_normal(m).astype(np.float32)
            F_ = np.fft.rfft(ns); fr = np.fft.rfftfreq(m, 1 / sr); c = 500 + 4500 * k.mean(); F_ *= np.exp(-((fr - 1800) / 1500) ** 2); s = np.fft.irfft(F_, m)
            s = s / (np.abs(s).max() + 1e-9) * np.sin(np.pi * k) ** 2 * 0.28 * amp; add(t0 - 0.12, s.astype(np.float32))
        elif kind == "pop":
            m = int(0.09 * sr); k = np.arange(m) / sr; s = np.sin(2 * np.pi * (520 - 2400 * k) * k) * np.exp(-k * 45) * 0.16 * amp; add(t0, s.astype(np.float32))
        elif kind in ("thud", "stamp"):
            m = int(0.55 * sr); k = np.arange(m) / sr; s = np.sin(2 * np.pi * (78 - 40 * k) * k * 1.0 + 0) * np.exp(-k * 7) * 0.7
            nz = rng.standard_normal(m).astype(np.float32) * np.exp(-k * 38) * 0.22; add(t0, (s + nz).astype(np.float32))
        elif kind == "tic":
            m = int(0.02 * sr); s = np.diff(np.concatenate([[0], rng.standard_normal(m)])) * np.exp(-np.arange(m) / sr * 260) * 0.1; add(t0, s.astype(np.float32))
    return np.clip(y, -1, 1)

def main():
    voce, sr, bl = R.prepara_audio(); dur = len(voce) / sr; NF = int(dur * FPS); dur = NF / FPS
    S = V3(bl); ev = S.eventi_audio()
    json.dump({"blocchi": bl, "durata": dur, "frames": NF, "scene": [(round(b["t0"], 2), b["b"] + 1, b["x"]) for b in S.beats]}, open(os.path.join(PR, "tempi.json"), "w"), indent=1)
    fx = audio_fx(dur, sr, ev); vv = np.zeros(len(fx), np.float32); vv[:min(len(voce), len(fx))] = voce[:len(fx)]
    for nome, arr in (("voce", vv), ("fx", fx)):
        w_ = wave.open(os.path.join(PR, f"_{nome}.wav"), "wb"); w_.setnchannels(1); w_.setsampwidth(2); w_.setframerate(sr)
        w_.writeframes((np.clip(arr, -1, 1) * 32767).astype(np.int16).tobytes()); w_.close()
    if len(sys.argv) > 2 and sys.argv[2] == "solo_audio": return
    R.Scene = V3
    n = 4; passo = (NF + 4 * n - 1) // (4 * n); parti = [(k, k * passo, min(NF, (k + 1) * passo)) for k in range(4 * n) if k * passo < NF]
    with Pool(4, initializer=R.init, initargs=(bl,)) as pool: files = pool.map(R.lavora, parti)
    lst = os.path.join(PR, "_tmp", "lista.txt"); open(lst, "w").write("".join(f"file '{f}'\n" for f in files))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-i", os.path.join(PR, "_voce.wav"), "-i", os.path.join(PR, "_fx.wav"),
                    "-filter_complex", "[1:a]loudnorm=I=-15:TP=-1.5[v];[2:a]volume=1.0[f];[v][f]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", os.path.join(PR, "video.mp4")], check=True)
    print("frames", NF, "durata", round(dur, 1))

if __name__ == "__main__":
    main()
