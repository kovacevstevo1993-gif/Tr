#!/usr/bin/env python3
"""Motore video del canale: monta la voce dei blocchi e anima le scene sulla scrivania.
Veloce: 4 processi in parallelo, livelli fissi preparati una volta. Uso: render_pratica.py cartella_pratica"""
import os, sys, math, json, wave, random, subprocess
import numpy as np
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fotogrammi_v2 as G
import demo_gancio as D

W, H, FPS = 1920, 1080, 30
F = G.F; ROSSO, GIALLO, CARTA, NERO, GRIGIO, VERDE, INCH = G.ROSSO, G.GIALLO, G.CARTA, G.NERO, G.GRIGIO, G.VERDE, G.INCH
ease, lerp, ease_back = D.ease, D.lerp, D.ease_back
PR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else None
LEAD, GAP, CODA = 0.35, 0.45, 1.0

# ---------------- tempi ----------------
def durata(p): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]))
def prepara_audio():
    voce = sorted(f for f in os.listdir(os.path.join(PR, "voce")) if f.endswith(".mp3"))
    sr = 48000; pezzi = [np.zeros(int(LEAD * sr), np.float32)]; t = LEAD; blocchi = []
    for f in voce:
        wav = os.path.join(PR, "voce", f[:-4] + ".wav")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", os.path.join(PR, "voce", f), "-af",
                        "silenceremove=start_periods=1:start_threshold=-42dB,areverse,silenceremove=start_periods=1:start_threshold=-42dB,areverse",
                        "-ar", str(sr), "-ac", "1", wav], check=True)
        a = np.frombuffer(wave.open(wav).readframes(10 ** 9), np.int16).astype(np.float32) / 32768
        blocchi.append((t, t + len(a) / sr)); pezzi.append(a); t += len(a) / sr
        pezzi.append(np.zeros(int(GAP * sr), np.float32)); t += GAP
    pezzi.append(np.zeros(int(CODA * sr), np.float32)); voce_tot = np.concatenate(pezzi)
    return voce_tot, sr, blocchi

# ---------------- elementi riusabili ----------------
def foglio_righe(titolo, righe, evid=None, w=1000, testa="FINANZIAMENTO AUTO", n="001", nota=None):
    h = 230 + 80 * len(righe) + 90
    im = G.foglio(w, h); d = ImageDraw.Draw(im); L = 60
    d.text((L, 44), f"PRATICA N. {n}", font=F("mono", 26), fill=ROSSO)
    d.text((w - 60, 46), f"{testa}  ·  RISERVATO", font=F("mono2", 22), fill=GRIGIO, anchor="ra")
    d.line([L, 88, w - 60, 88], fill=INCH, width=3); d.text((L, 110), titolo, font=F("titolo", 44), fill=INCH)
    pos = []; y = 210
    for k, v in righe:
        pos.append(y)
        if k == evid: d.rectangle([L - 14, y - 8, w - 46, y + 52], fill=GIALLO)
        d.text((L, y), k, font=F("mono2", 32), fill=INCH); d.text((w - 60, y), v, font=F("mono", 32), fill=INCH, anchor="ra")
        d.line([L, y + 62, w - 60, y + 62], fill=(208, 203, 192), width=2); y += 80
    d.text((L, h - 50), nota or "Esempio: simulazione con calcoli nostri", font=F("corpoR", 21), fill=GRIGIO)
    return G.grana_carta(im, len(titolo)), pos

def con_ombra(im):
    s, p = G.ombra(im); return s, p

def card(testo, sotto, colore, w=600, h=300, fs=96):
    im = Image.new("RGBA", (w, h), CARTA + (255,)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, w, 14], fill=colore); d.text((w / 2, h * 0.47), testo, font=F("mono", fs), fill=colore, anchor="mm")
    d.text((w / 2, h - 46), sotto, font=F("corpo", 30), fill=INCH, anchor="mm"); return G.grana_carta(im, w)

def mossa(n, titolo, punti, w=1240):
    h = 170 + 86 * len(punti); im = Image.new("RGBA", (w, h), CARTA + (255,)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 18, h], fill=VERDE); d.ellipse([60, 40, 160, 140], fill=VERDE)
    d.text((110, 90), str(n), font=F("titolo", 64), fill=CARTA, anchor="mm"); d.text((200, 62), titolo, font=F("titolo", 52), fill=INCH)
    return G.grana_carta(im, n + 30), h

def incolla_a(img, ob, x, y, a=1.0, sc=1.0, rot=0):
    if a <= 0: return
    if sc != 1.0: ob = ob.resize((max(1, int(ob.width * sc)), max(1, int(ob.height * sc))), Image.BICUBIC)
    if rot: ob = ob.rotate(rot, expand=True, resample=Image.BICUBIC)
    if a < 1: ob = ob.copy(); ob.putalpha(ob.split()[3].point(lambda v: int(v * a)))
    img.alpha_composite(ob, (int(x), int(y)))

def entra(t, t0, dur=0.45): return ease_back((t - t0) / dur, 1.0) if t >= t0 else 0.0
def comp(t, t0, dur=0.3): return ease((t - t0) / dur) if t >= t0 else 0.0

# ---------------- contatore con rulli ----------------
class Cont:
    """valori del contatore nel tempo: lista (t_inizio, t_fine, da, a). Le cifre girano dal vecchio al nuovo valore."""
    def __init__(self, cambi): self.c = cambi
    def cifre(self, t):
        val_prec = None
        for (t0, t1, da, a) in self.c:
            if t < t0: return da, None, 0
            if t < t1: return da, a, (t - t0) / (t1 - t0)
            val_prec = a
        return val_prec, None, 0

class RulloFisso:
    def __init__(self, p, n=10, v=0): self.p, self.n, self.v = p, n, v
    def pos(self, t): return self.p
    def vel(self, t): return self.v

def rulli_valore(da, a, x):
    """4 rulli (migliaia, centinaia, decine, unita) che passano da 'da' ad 'a' con giri extra"""
    out = []
    for k, div in enumerate((1000, 100, 10, 1)):
        d0 = (da // div) % 10; d1 = (a // div) % 10 if a is not None else d0
        if a is None: out.append(RulloFisso(d0)); continue
        giri = 2 + k; tot = (d1 - d0) % 10 + 10 * giri
        xe = ease(min(1, max(0, (x - 0.06 * k) / (1 - 0.18))))
        out.append(RulloFisso(d0 + tot * xe, 10, v=tot * 3 * (1 - xe) + 0.01))
    return out

# ---------------- scene (una per blocco) ----------------
class Scene:
    def __init__(self, blocchi):
        self.b = blocchi
        self.desk = G.scrivania(0.92); self.desk_b = self.desk.filter(ImageFilter.GaussianBlur(7))
        self.grana = [Image.effect_noise((W // 2, H // 2), 22).resize((W, H)).convert("L") for _ in range(6)]
        # contratti / fogli
        self.f3, self.p3 = foglio_righe("Contratto di finanziamento", [("Prezzo auto", "€ 21.900"), ("Anticipo", "€ 3.000"), ("Da finanziare", "€ 18.900"), ("Rata mensile", "€ 199 x 35")])
        self.f5, self.p5 = foglio_righe("Costi dentro il TAEG", [("Spese di istruttoria", "€ 350"), ("Incasso rata 3,50 € x 35", "€ 122,50"), ("Imposta di bollo", "€ 16"), ("Totale nascosto", "€ 488")], evid="Totale nascosto")
        self.f7, self.p7 = foglio_righe("Contratto di finanziamento", [("Rata mensile", "€ 199 x 35"), ("Maxirata finale", "€ 15.957"), ("TAN fisso", "6,95%"), ("TAEG", "8,26%")], evid="Maxirata finale")
        self.f12, self.p12 = foglio_righe("Rifinanziamento maxirata", [("Importo", "€ 15.957"), ("Durata", "48 mesi"), ("Tasso (TAN)", "8,5%"), ("Interessi in più", "€ 2.922")], evid="Interessi in più", testa="NUOVO PRESTITO")
        self.secci, _ = foglio_righe("Modulo SECCI", [("Informazioni europee", "di base"), ("sul credito ai", "consumatori"), ("TAEG", "8,26%"), ("Costo totale", "€ 4.160")], evid="TAEG", testa="PRIMA DELLA FIRMA", nota="Va consegnato prima di firmare (Testo Unico Bancario)")
        self.c4a = card("6,95%", "TAN: solo interessi", GRIGIO); self.c4b = card("8,26%", "TAEG: tutto compreso", ROSSO)
        self.ind = [card(l, s, INCH if l != "C" else ROSSO, 440, 300, 120) for l, s in (("A", "la paga"), ("B", "restituisce l'auto"), ("C", "la rifinanzia"))]
        self.post1 = G.postit("chiedilo\nPRIMA!", 280); self.post_km = G.postit("limiti di\nchilometri", 290); self.post_d = G.postit("controlli\nsui danni", 290)
        self.post_auto = G.postit("auto di\n7 anni", 270)
        self.m1, _ = mossa(1, "Confronta il TAEG", ["Guarda il costo totale, non la rata", "Porta a casa il modulo SECCI", "Nessuna firma il giorno stesso"])
        self.m2, _ = mossa(2, "Decidi ora per la maxirata", ["Non avrai quella cifra? Niente maxirata", "Finanziamento classico: rata più alta", "…ma il debito scende ogni mese"])
        self.m3, _ = mossa(3, "Conosci i tuoi diritti", ["14 giorni per recedere", "Estinzione anticipata: meno interessi", "Polizze facoltative: puoi dire no"])
        self.t_nc = G.timbro("NON CONVIENE", ROSSO, 92, 5).rotate(-8, expand=True, resample=Image.BICUBIC)
        self.t_mx = G.timbro("NUOVO PRESTITO", ROSSO, 60, 6).rotate(6, expand=True, resample=Image.BICUBIC)
        self.chip = {k: G.pillola(f"TRAPPOLA {k} DI 3", ROSSO, 30) for k in (1, 2, 3)}
        self.pill_fine = G.pillola("LA CIFRA ESATTA ALLA FINE", ROSSO, 32); self.pill3 = G.pillola("3 TRAPPOLE", ROSSO, 34)
        self.pill_mosse = G.pillola("COME EVITARLE: 3 MOSSE", VERDE, 34)
        # cartelline
        self.cart1 = self.cartellina("001", "FINANZIAMENTO AUTO", "Rata: 199 € al mese… dove sta il trucco?")
        self.cart2 = self.cartellina("002", "BOLLETTA DELLA LUCE", "La voce che pochi controllano")
        auto = Image.open(os.path.join(G.AS, "auto_cc0.jpg")).convert("RGB"); s = min(auto.size); auto = auto.crop(((auto.width - s) // 2, (auto.height - s) // 2, (auto.width + s) // 2, (auto.height + s) // 2))
        pol = Image.new("RGBA", (380, 450), (250, 249, 245, 255)); pol.paste(auto.resize((344, 344)), (18, 18)); self.pol = pol
        self.scontrino9 = self.scontrino([("Anticipo", "3.000"), ("Rate 35 x 199", "6.965"), ("Incasso e bollo", "138,50"), ("Maxirata", "15.957")], ("TOTALE PAGATO", "26.060"), "Prezzo auto: 21.900 €")
        self.scontrino13 = self.scontrino([("1  Spese nascoste", "488"), ("2  Interessi", "3.672"), ("3  Rifinanziamento", "2.922")], ("TOTALE IN PIÙ", "7.082"), "Grazie per non aver firmato.")
        self.disc = self.disclaimer()
        b = blocchi; self.cont = Cont([(b[4][0] + 0.8 * (b[4][1] - b[4][0]), b[4][0] + 0.8 * (b[4][1] - b[4][0]) + 1.6, 0, 488),
                                      (b[8][0] + 0.8 * (b[8][1] - b[8][0]), b[8][0] + 0.8 * (b[8][1] - b[8][0]) + 1.6, 488, 4160),
                                      (b[11][0] + 0.45 * (b[11][1] - b[11][0]), b[11][0] + 0.45 * (b[11][1] - b[11][0]) + 1.6, 4160, 7082)])
        r = [D.Rullo(10 + 154 + 11 * k, 15 + 2 * k, 0.4 + 0.8 * (b[0][1] - b[0][0]) - 1.2 + 0.25 * k, 0.4 + 0.8 * (b[0][1] - b[0][0]) + 0.25 * k, 1.3 * k, facce=11) for k in range(4)]
        self.r_gancio = r

    def cartellina(self, n, tema, nota):
        c = Image.new("RGBA", (1100, 760), (0, 0, 0, 0)); d = ImageDraw.Draw(c)
        d.rounded_rectangle([0, 60, 1099, 759], radius=18, fill=(214, 196, 160, 255)); d.rounded_rectangle([40, 0, 420, 120], radius=18, fill=(214, 196, 160, 255))
        d.rectangle([60, 140, 900, 300], fill=CARTA + (255,)); d.rectangle([60, 140, 900, 300], outline=INCH, width=3)
        d.text((90, 160), f"PRATICA N. {n}", font=F("mono", 44), fill=ROSSO); d.text((90, 222), tema, font=F("titolo", 48), fill=INCH)
        d.text((70, 30), f"N. {n}", font=F("mono", 34), fill=(90, 70, 40))
        for i in range(3): d.line([60, 420 + i * 70, 1000, 420 + i * 70], fill=(176, 158, 122), width=3)
        d.text((60, 352), nota, font=F("mano", 58), fill=(40, 40, 60)); return G.grana_carta(c, int(n))

    def scontrino(self, righe, tot, firma):
        sw, sh = 620, 200 + 62 * len(righe) + 260; sc = Image.new("RGBA", (sw, sh), (0, 0, 0, 0)); d = ImageDraw.Draw(sc)
        pts = [(x, 14 if (x // 14) % 2 else 0) for x in range(0, sw + 1, 14)] + [(x, sh - 14 if (x // 14) % 2 else sh) for x in range(sw, -1, -14)]
        d.polygon(pts, fill=(250, 250, 247, 255)); m, mb = F("mono2", 28), F("mono", 30); y = 50
        d.text((sw / 2, y), "PRATICA N. 001", font=mb, fill=INCH, anchor="ma"); y += 60
        d.text((36, y), "-" * 32, font=m, fill=GRIGIO); y += 46; self._sc_y = []
        for k, v in righe:
            d.text((36, y), k, font=m, fill=INCH); d.text((sw - 36, y), "€ " + v, font=mb, fill=INCH, anchor="ra"); y += 62
        d.text((36, y), "-" * 32, font=m, fill=GRIGIO); y += 52
        d.text((36, y), tot[0], font=F("mono", 34), fill=ROSSO); d.text((sw - 36, y), "€ " + tot[1], font=F("mono", 34), fill=ROSSO, anchor="ra"); y += 80
        d.text((sw / 2, y), firma, font=F("mano", 46), fill=(40, 40, 60), anchor="ma")
        return G.grana_carta(sc, len(righe))

    def disclaimer(self):
        im = Image.new("RGBA", (1500, 600), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.rounded_rectangle([0, 0, 1499, 599], radius=26, fill=(14, 15, 18, 235), outline=(70, 72, 78, 255), width=3)
        d.text((70, 60), "PRIMA DI DECIDERE", font=F("mono", 34), fill=GIALLO); y = 140
        for r in ["Regole, tassi e condizioni cambiano e possono", "essere diversi da contratto a contratto.", "Controlla sempre il tuo modulo SECCI e la fonte", "ufficiale. I calcoli di questo video sono una", "simulazione. Informazione generale,", "non consulenza finanziaria."]:
            d.text((70, y), r, font=F("corpo", 46), fill=CARTA); y += 66
        return im

    # contatore: dove e quanto
    def disegna_cont(self, img, t, i, tl, dur):
        if i == 0:                                                                   # gancio: grande al centro, finisce su ?.???
            c = D.contatore_animato(self.r_gancio, t, label="QUANTO TI COSTA IN PIÙ")
            a = comp(t, self.b[0][0] + 0.9, 0.45); incolla_a(img, G.ombra(c)[0], (W - c.width) / 2 - 66, 400 + (1 - a) * 120 - 66, a); return
        da, a_, x = self.cont.cifre(t)
        rul = rulli_valore(da, a_, x)
        sc = 0.6; cx, cy = W - 546 - 60, 36
        if i == 12:                                                                  # verdetto del contatore: grande
            k = ease((tl) / 0.7); sc = lerp(0.6, 1.15, k); cxx = lerp(cx, (W - 910 * 1.15) / 2 + 380, k); cy = lerp(36, 330, k); cx = cxx
        if i >= 13:
            k = ease(tl / 0.6) if i == 13 else 1; sc = lerp(1.15, 0.6, k) if i == 13 else 0.6
            cx = lerp((W - 910 * 1.15) / 2 + 380, W - 546 - 60, k) if i == 13 else W - 546 - 60; cy = lerp(330, 36, k) if i == 13 else 36
        if i in (9, 17, 18): return
        c = D.contatore_animato(rul, t, label="TOTALE PERSO" if i >= 12 else "STAI PERDENDO")
        c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS); a = comp(t, self.b[1][0], 0.4) if i == 1 else 1
        incolla_a(img, G.ombra(c)[0], cx - 66, cy - 66, a)

    def frame(self, t):
        b = self.b; i = max([k for k, (s, e) in enumerate(b) if t >= s - 0.05] or [0])
        s, e = b[i]; dur = e - s; tl = t - s
        fine = (b[i + 1][0] if i + 1 < len(b) else e + CODA) - 0.05
        a_out = 1 - ease((t - (fine - 0.28)) / 0.28) if t > fine - 0.28 and i + 1 < len(b) else 1
        dof = 0.85 if i not in (0, 9, 18) else 0.0
        img = Image.blend(self.desk, self.desk_b, dof) if dof else self.desk.copy()
        if t < 0.5:
            img.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, int(255 * (1 - ease(t / 0.5)) * 0.95))))
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); self.scena(lay, i, tl, dur, t)
        if a_out < 1: lay.putalpha(lay.split()[3].point(lambda v: int(v * a_out)))
        img.alpha_composite(lay); self.disegna_cont(img, t, i, tl, dur)
        if i in (3, 4, 6, 7, 10, 11):
            k = {3: 1, 4: 1, 6: 2, 7: 2, 10: 3, 11: 3}[i]; incolla_a(img, self.chip[k], W - self.chip[k].width - 80, 255, comp(t, s, 0.3) if i in (3, 6, 10) else 1)
        z = 1.0 + 0.03 * min(1, tl / max(dur, 1)); cw, ch = W / z, H / z
        fr = img.convert("RGB").crop(((W - cw) / 2, (H - ch) / 2, (W + cw) / 2, (H + ch) / 2)).resize((W, H), Image.BICUBIC)
        g = (np.asarray(self.grana[int(t * FPS) % 6], np.int16) - 128) * 0.07
        return Image.fromarray(np.clip(np.asarray(fr, np.int16) + g[..., None], 0, 255).astype(np.uint8))

    def scena(self, L, i, tl, dur, t):
        p = lambda f: f * dur                                                       # momento dentro il blocco
        if i == 0:
            a = comp(tl, 0.0, 0.3); D.testo_ombra(L, (W / 2, 210 + 18 * (1 - a)), "199 € al mese.", F("titolo", 130), CARTA, alpha=255 * a)
            a2 = comp(tl, p(0.18)); D.testo_ombra(L, (W / 2, 315), "Per un'auto nuova.", F("corpo", 54), (210, 212, 218), alpha=255 * a2)
            a3 = comp(tl, p(0.8), 0.25); incolla_a(L, self.pill_fine, (W - self.pill_fine.width) / 2, 860, a3)
        elif i == 1:
            k = entra(tl, 0.0, 0.55); incolla_a(L, G.ombra(self.cart1)[0], 180 - 66, 200 + (1 - k) * 900 - 66, rot=-3)
            k2 = entra(tl, p(0.3)); incolla_a(L, G.ombra(self.pol)[0], 1300 - 66 + (1 - k2) * 700, 300 - 66, rot=6)
            if tl > p(0.3) + 0.3: incolla_a(L, G.graffetta(170), 1420, 250, rot=8)
            incolla_a(L, self.pill3, 1420, 880, comp(tl, p(0.8), 0.25))
        elif i == 2:
            k = entra(tl, 0.0, 0.5); x0, y0 = 300, 90 + (1 - k) * 1000
            fo = self.f3.copy(); dd = ImageDraw.Draw(fo); fr = [0, 0.2, 0.4, 0.6, 0.8]
            for r, yr in enumerate(self.p3):                                        # righe nascoste finche non arrivano
                if tl < p(fr[r + 1]): dd.rectangle([40, yr - 10, fo.width - 40, yr + 60], fill=CARTA)
            incolla_a(L, G.ombra(fo)[0], x0 - 66, y0 - 66, rot=-1.2)
        elif i == 3:
            incolla_a(L, G.ombra(self.c4a)[0], 280 - 66, 360 - 66 + (1 - entra(tl, p(0.35))) * 900, rot=-3)
            incolla_a(L, G.ombra(self.c4b)[0], 1040 - 66, 360 - 66 + (1 - entra(tl, p(0.55))) * 900, rot=2)
            a = comp(tl, p(0.8)); D.testo_ombra(L, (W / 2 + 10, 515), "≠", F("titolo", 150), GIALLO, alpha=255 * a)
        elif i == 4:
            fo = self.f5.copy(); dd = ImageDraw.Draw(fo); fr = [0.2, 0.4, 0.55, 0.8]
            for r, yr in enumerate(self.p5):
                if tl < p(fr[r]): dd.rectangle([40, yr - 10, fo.width - 30, yr + 60], fill=CARTA)
            k = entra(tl, 0.0, 0.5); incolla_a(L, G.ombra(fo)[0], 300 - 66, 120 - 66 + (1 - k) * 1000, rot=1.2)
        elif i == 5:
            k = entra(tl, 0.0, 0.5); incolla_a(L, G.ombra(self.secci)[0], 260 - 66, 100 - 66 + (1 - k) * 1000, rot=-1.5)
            incolla_a(L, G.ombra(self.post1)[0], 1330 - 66, 560 - 66 + (1 - entra(tl, p(0.8))) * 700, rot=-7)
        elif i == 6:
            k = entra(tl, 0.0, 0.5); fo = self.f7 if tl >= p(0.45) else foglio_cache(self, "f7n")
            incolla_a(L, G.ombra(fo)[0], 220 - 66, 110 - 66 + (1 - k) * 1000, rot=-1.5)
            if tl >= p(0.8):
                kk = ease((tl - p(0.8)) / 0.4); cx, cy = 220 + 820, 110 + self.p7[1] + 30
                le = G.lente(L.convert("RGB"), (cx, cy), r=165, zoom=1.5); incolla_a(L, G.ombra(le)[0], lerp(W + 200, cx - 185, kk) - 66, cy - 185 - 66)
        elif i == 7: self.grafico(L, tl, dur)
        elif i == 8:
            sc = self.scontrino9.copy(); dd = ImageDraw.Draw(sc); fr = [0.1, 0.3, 0.45, 0.6, 0.8]
            ys = [156 + 62 * k for k in range(4)] + [156 + 62 * 4 + 52]
            for r, yr in enumerate(ys):
                if tl < p(fr[r]): dd.rectangle([30, yr - 6, sc.width - 30, yr + 48], fill=(250, 250, 247))
            if tl < p(0.8): dd.rectangle([30, ys[-1] + 70, sc.width - 30, ys[-1] + 140], fill=(250, 250, 247))
            k = entra(tl, 0.0, 0.5); incolla_a(L, G.ombra(sc)[0], 640 - 66, 60 - 66 + (1 - k) * 1000, rot=2)
        elif i == 9:
            D.testo_ombra(L, (W / 2, 140), "INDOVINA", F("mono", 40), GIALLO, alpha=255 * comp(tl, 0))
            D.testo_ombra(L, (W / 2, 225), "Cosa fa la maggior parte delle persone?", F("titolo", 64), CARTA, alpha=255 * comp(tl, p(0.2)))
            for k, c in enumerate(self.ind):
                incolla_a(L, G.ombra(c)[0], 250 + k * 500 - 66, 360 - 66 + (1 - entra(tl, p(0.45 + 0.1 * k))) * 900, rot=(-3, 2, -2)[k])
            if tl >= p(0.75):
                n = 3 - min(2, int((tl - p(0.75)) / max(0.3, (dur - p(0.75)) / 3)))
                ring = Image.new("RGBA", (220, 220), (0, 0, 0, 0)); dr = ImageDraw.Draw(ring)
                dr.ellipse([10, 10, 210, 210], fill=NERO + (235,)); dr.arc([10, 10, 210, 210], -90, -90 + 120 * n, fill=ROSSO, width=12)
                dr.text((110, 110), str(n), font=F("mono", 110), fill=CARTA, anchor="mm"); incolla_a(L, ring, W / 2 - 110, 760)
                D.testo_ombra(L, (W / 2 + 150, 870), "Scrivilo nei commenti", F("mano", 60), GIALLO, anchor="lm")
        elif i == 10:
            c = self.ind[2]; k = ease(tl / 0.6); incolla_a(L, G.ombra(c)[0], lerp(1250, 300, k) - 66, lerp(360, 300, k) - 66, sc=lerp(1, 1.25, k), rot=-2)
            incolla_a(L, G.ombra(self.post_km)[0], 1000 - 66, 260 - 66 + (1 - entra(tl, p(0.45))) * 900, rot=-6)
            incolla_a(L, G.ombra(self.post_d)[0], 1380 - 66, 300 - 66 + (1 - entra(tl, p(0.6))) * 900, rot=5)
            if tl >= p(0.8): self.timbro_cade(L, self.t_mx, tl - p(0.8), 1050, 700)
        elif i == 11:
            fo = self.f12.copy() if tl >= p(0.45) else foglio_cache(self, "f12n")
            k = entra(tl, 0.0, 0.5); incolla_a(L, G.ombra(fo)[0], 220 - 66, 110 - 66 + (1 - k) * 1000, rot=1.2)
            incolla_a(L, G.ombra(self.post_auto)[0], 1400 - 66, 600 - 66 + (1 - entra(tl, p(0.8))) * 800, rot=-5)
        elif i == 12:
            sc = self.scontrino13; k = entra(tl, p(0.15), 0.5); incolla_a(L, G.ombra(sc)[0], 150 - 66, 60 - 66 + (1 - k) * 1000, rot=-2)
        elif i in (13, 14, 15):
            m = (self.m1, self.m2, self.m3)[i - 13]; k = entra(tl, 0.0, 0.5)
            incolla_a(L, self.pill_mosse, 340, 150, 1); incolla_a(L, G.ombra(m)[0], 340 - 66, 260 - 66 + (1 - k) * 900)
            punti = {13: ["Guarda il costo totale, non la rata", "Porta a casa il modulo SECCI", "Nessuna firma il giorno stesso"],
                     14: ["Non avrai quella cifra? Niente maxirata", "Finanziamento classico: rata più alta", "…ma il debito scende ogni mese"],
                     15: ["14 giorni per recedere dal contratto", "Estinzione anticipata: meno interessi", "Polizze facoltative: puoi dire no"]}[i]
            for r, txt in enumerate(punti):
                a = comp(tl, p((0.3, 0.55, 0.8)[r]), 0.25)
                if a > 0:
                    yy = 260 + 190 + r * 86 + (1 - k) * 900
                    D.testo_ombra(L, (340 + 200, yy), "✓  " + txt if False else "—  " + txt, F("corpo", 44), INCH, anchor="lm", alpha=255 * a, ombra=False)
        elif i == 16:
            D.testo_ombra(L, (W / 2, 170), "IL VERDETTO", F("mono", 44), GIALLO, alpha=255 * comp(tl, 0))
            a = comp(tl, p(0.25)); D.testo_ombra(L, (W / 2, 330), "Conviene se cambi auto ogni 3 anni", F("corpo", 56), (150, 220, 180), alpha=255 * a)
            a = comp(tl, p(0.5)); D.testo_ombra(L, (W / 2, 430), "Se vuoi tenerla e non hai la maxirata:", F("corpo", 56), CARTA, alpha=255 * a)
            if tl >= p(0.8): self.timbro_cade(L, self.t_nc, tl - p(0.8), W / 2, 680)
        elif i == 17:
            k = entra(tl, 0.0, 0.55); incolla_a(L, G.ombra(self.cart2)[0], 410 - 66, 180 + (1 - k) * 900 - 66, rot=2)
            D.testo_ombra(L, (W / 2, 110), "PROSSIMA PRATICA", F("mono", 44), GIALLO, alpha=255 * comp(tl, p(0.3)))
        elif i == 18:
            incolla_a(L, self.disc, (W - 1500) / 2, (H - 600) / 2, comp(tl, 0, 0.4))

    def timbro_cade(self, L, tb, dt, cx, cy):
        k = min(1, dt / 0.16); sc = lerp(1.7, 1.0, k * k)
        im = tb.resize((int(tb.width * sc), int(tb.height * sc)), Image.BICUBIC); incolla_a(L, im, cx - im.width / 2, cy - im.height / 2, 0.4 + 0.6 * k)

    def grafico(self, L, tl, dur):
        p = lambda f: f * dur; x0, y0, gw, gh = 300, 200, 1320, 640
        pan = Image.new("RGBA", (gw + 120, gh + 200), (0, 0, 0, 0)); d = ImageDraw.Draw(pan)
        d.rounded_rectangle([0, 0, gw + 119, gh + 199], radius=24, fill=(18, 19, 23, 235), outline=(70, 72, 78), width=3)
        d.text((40, 30), "DEBITO RESIDUO", font=F("mono", 30), fill=GRIGIO)
        ox, oy, aw, ah = 110, gh + 110, gw - 60, gh - 80
        d.line([ox, oy, ox + aw, oy], fill=(90, 92, 98), width=3); d.line([ox, oy, ox, oy - ah], fill=(90, 92, 98), width=3)
        for m in (0, 12, 24, 36): xx = ox + aw * m / 36; d.text((xx, oy + 16), f"{m}", font=F("mono2", 24), fill=GRIGIO, anchor="ma")
        d.text((ox + aw, oy + 50), "mesi", font=F("mono2", 24), fill=GRIGIO, anchor="ra")
        i_ = 0.0695 / 12; debito = 19250.0; R = 199; dm = [debito]; db = [debito]
        Rn = debito * i_ / (1 - (1 + i_) ** -36)
        for m in range(36):
            dm.append(dm[-1] * (1 + i_) - (R if m < 35 else dm[-1] * (1 + i_))); db.append(max(0, db[-1] * (1 + i_) - Rn))
        sy = lambda v: oy - ah * v / 20000
        def linea(serie, col, frac, w):
            n = int(36 * frac); pts = [(ox + aw * m / 36, sy(serie[m])) for m in range(n + 1)]
            if len(pts) > 1: d.line(pts, fill=col, width=w, joint="curve")
        k1 = comp(tl, p(0.35), 1.0); k2 = comp(tl, p(0.6), 1.0)
        linea(db, (150, 220, 180), k1, 7); linea(dm, ROSSO, k2, 9)
        if k1 >= 1: d.text((ox + aw * 0.45, sy(db[16]) + 30), "rata normale", font=F("corpo", 32), fill=(150, 220, 180))
        if k2 >= 1: d.text((ox + aw * 0.40, sy(dm[14]) - 60), "con maxirata", font=F("corpo", 32), fill=ROSSO)
        incolla_a(L, pan, x0, y0 + (1 - entra(tl, 0, 0.5)) * 900)

_cache = {}
def foglio_cache(S, k):
    if k not in _cache:
        if k == "f7n": _cache[k] = foglio_righe("Contratto di finanziamento", [("Rata mensile", "€ 199 x 35"), ("Maxirata finale", "€ 15.957"), ("TAN fisso", "6,95%"), ("TAEG", "8,26%")])[0]
        if k == "f12n": _cache[k] = foglio_righe("Rifinanziamento maxirata", [("Importo", "€ 15.957"), ("Durata", "48 mesi"), ("Tasso (TAN)", "8,5%"), ("Interessi in più", "€ 2.922")], testa="NUOVO PRESTITO")[0]
    return _cache[k]

# ---------------- lavoro parallelo ----------------
_S = None
def init(bl):
    global _S; _S = Scene(bl)
def lavora(arg):
    k, f0, f1 = arg; out = os.path.join(PR, "_tmp", f"parte{k:02d}.mp4"); os.makedirs(os.path.join(PR, "_tmp", "mini"), exist_ok=True)
    enc = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                            "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for fi in range(f0, f1):
        fr = _S.frame(fi / FPS); enc.stdin.write(fr.tobytes())
        if fi % 15 == 0: fr.resize((384, 216)).save(os.path.join(PR, "_tmp", "mini", f"{fi:05d}.jpg"), quality=80)
    enc.stdin.close(); enc.wait(); return out

def main():
    voce, sr, bl = prepara_audio(); dur = len(voce) / sr; NF = int(dur * FPS); dur = NF / FPS
    json.dump({"blocchi": bl, "durata": dur, "frames": NF}, open(os.path.join(PR, "tempi.json"), "w"), indent=1)
    # suoni: click lampada, tic dei rulli, fruscio all'entrata dei fogli, timbri
    ev = {"tic": [], "carta": 0, "lente": 0, "timbro": 0}
    fx = np.zeros(int(dur * sr), np.float32); base = D.sfx(dur, sr, bl, {"tic": [], "carta": bl[1][0], "lente": bl[6][0], "timbro": bl[16][0] + 0.8 * (bl[16][1] - bl[16][0])})
    fx += base
    S0 = Scene.__new__(Scene); S0.b = bl
    for (s, e) in bl[2:]:                                                            # fruscio all'entrata di ogni foglio
        fx += D.sfx(dur, sr, bl, {"tic": [], "carta": s + 0.02, "lente": dur - 0.01, "timbro": dur - 0.01}) * 0.5 - D.sfx(dur, sr, bl, {"tic": [], "carta": dur - 0.01, "lente": dur - 0.01, "timbro": dur - 0.01}) * 0.5
    tic = []
    cambi = [(bl[0][0] + 0.9, bl[0][0] + 0.8 * (bl[0][1] - bl[0][0]) + 0.75)]
    b = bl
    for kk in (4, 8, 11):
        f = 0.8 if kk != 11 else 0.45; t0 = b[kk][0] + f * (b[kk][1] - b[kk][0]); cambi.append((t0, t0 + 1.6))
    for t0, t1 in cambi:
        t = t0
        while t < t1: tic.append(t); t += 0.05 + 0.12 * ((t - t0) / (t1 - t0)) ** 2
    fx += D.sfx(dur, sr, bl, {"tic": tic, "carta": dur - 0.01, "lente": dur - 0.01, "timbro": dur - 0.01}) - D.sfx(dur, sr, bl, {"tic": [], "carta": dur - 0.01, "lente": dur - 0.01, "timbro": dur - 0.01})
    t_mx = b[10][0] + 0.8 * (b[10][1] - b[10][0])
    fx += D.sfx(dur, sr, bl, {"tic": [], "carta": dur - 0.01, "lente": dur - 0.01, "timbro": t_mx}) - D.sfx(dur, sr, bl, {"tic": [], "carta": dur - 0.01, "lente": dur - 0.01, "timbro": dur - 0.01})
    vv = np.zeros(len(fx), np.float32); vv[:min(len(voce), len(fx))] = voce[:len(fx)]
    for nome, arr in (("voce", vv), ("fx", fx)):
        w_ = wave.open(os.path.join(PR, f"_{nome}.wav"), "wb"); w_.setnchannels(1); w_.setsampwidth(2); w_.setframerate(sr)
        w_.writeframes((np.clip(arr, -1, 1) * 32767).astype(np.int16).tobytes()); w_.close()
    n = 4; passo = (NF + 4 * n - 1) // (4 * n); parti = [(k, k * passo, min(NF, (k + 1) * passo)) for k in range(4 * n) if k * passo < NF]
    with Pool(4, initializer=init, initargs=(bl,)) as pool: files = pool.map(lavora, parti)
    lst = os.path.join(PR, "_tmp", "lista.txt"); open(lst, "w").write("".join(f"file '{f}'\n" for f in files))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-i", os.path.join(PR, "_voce.wav"), "-i", os.path.join(PR, "_fx.wav"),
                    "-filter_complex", "[1:a]loudnorm=I=-15:TP=-1.5[v];[2:a]volume=0.9[f];[v][f]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", os.path.join(PR, "video.mp4")], check=True)
    print("frames", NF, "durata", round(dur, 1))

if __name__ == "__main__":
    main()
