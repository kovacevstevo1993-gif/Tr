#!/usr/bin/env python3
"""Demo: i primi ~15 secondi del video (gancio) con voce A, animazione e suoni.
Uso: python3 demo_gancio.py  -> nuovo_canale_italia/demo/demo-gancio.mp4"""
import os, sys, math, json, random, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fotogrammi_v2 as G

HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "..", "demo")
W, H, FPS = 1920, 1080, 30
F = G.F; ROSSO, GIALLO, CARTA, NERO, GRIGIO = G.ROSSO, G.GIALLO, G.CARTA, G.NERO, G.GRIGIO

# ---------------- AUDIO: voce con pause regolate ----------------
SEG = [(0.293, 1.217), (1.711, 2.251), (2.772, 4.186), (4.659, 7.282), (7.719, 10.772),
       (11.320, 12.638), (13.037, 14.060), (14.653, 15.617)]                 # frasi in take1.mp3
LEAD, PAUSA_MAX, CODA = 0.35, 0.30, 0.70

def costruisci_voce():
    src = os.path.join(OUT, "take1.mp3"); wav = os.path.join(OUT, "take1.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-ar", "48000", "-ac", "1", wav], check=True)
    a = np.frombuffer(wave.open(wav).readframes(10 ** 9), dtype=np.int16).astype(np.float32) / 32768
    sr = 48000; out = [np.zeros(int(LEAD * sr), np.float32)]; t = LEAD; tempi = []
    for i, (s, e) in enumerate(SEG):
        s0, e0 = max(0, s - 0.04), e + 0.06
        pezzo = a[int(s0 * sr):int(e0 * sr)].copy(); f = int(0.01 * sr)
        pezzo[:f] *= np.linspace(0, 1, f); pezzo[-f:] *= np.linspace(1, 0, f)
        tempi.append((t + 0.04, t + 0.04 + (e - s))); out.append(pezzo); t += len(pezzo) / sr
        if i < len(SEG) - 1:
            p = min(SEG[i + 1][0] - e, PAUSA_MAX); out.append(np.zeros(int(p * sr), np.float32)); t += p
    out.append(np.zeros(int(CODA * sr), np.float32)); voce = np.concatenate(out)
    return voce, sr, tempi

def sfx(durata, sr, tempi, eventi):
    """suoni sintetici: click lampada, bordone basso, tic dei rulli, fruscio carta, timbro"""
    n = int(durata * sr); y = np.zeros(n, np.float32); rng = np.random.default_rng(3)
    t = np.arange(n) / sr
    drone = (0.5 * np.sin(2 * np.pi * 55 * t) + 0.3 * np.sin(2 * np.pi * 82.4 * t) + 0.2 * np.sin(2 * np.pi * 110 * t))
    drone *= (0.6 + 0.4 * np.sin(2 * np.pi * 0.25 * t)) * np.clip(t / 1.5, 0, 1) * np.clip((durata - t) / 0.6, 0, 1)
    y += 0.035 * drone
    def burst(t0, dur, amp, lp=None, hp=None, tono=None, dec=30):
        i0 = int(t0 * sr); m = int(dur * sr); k = np.arange(m) / sr
        s = rng.standard_normal(m).astype(np.float32) if tono is None else np.sin(2 * np.pi * tono * k * (1 - 0.35 * k / dur))
        if lp:
            a_ = math.exp(-2 * math.pi * lp / sr); s2 = np.zeros_like(s); acc = 0.0
            for j in range(m): acc = (1 - a_) * s[j] + a_ * acc; s2[j] = acc
            s = s2
        if hp: s = np.concatenate([[0], np.diff(s)])
        s = s * np.exp(-dec * k); s = s / (np.abs(s).max() + 1e-9) * amp
        e = min(n, i0 + m); y[i0:e] += s[:e - i0]
    burst(0.05, 0.05, 0.35, hp=True, dec=120)                                      # click lampada
    for tt in eventi["tic"]: burst(tt, 0.018, 0.12, hp=True, dec=260)               # rulli
    burst(eventi["carta"], 0.5, 0.18, lp=2500, dec=5)                               # fruscio carta
    burst(eventi["lente"], 0.35, 0.07, lp=1500, dec=7)
    burst(eventi["timbro"], 0.45, 0.65, tono=72, dec=9); burst(eventi["timbro"], 0.06, 0.4, lp=1200, dec=60)
    return y

# ---------------- TEMPI DELLE SCENE ----------------
def ease(x): x = min(1, max(0, x)); return 1 - (1 - x) ** 3
def ease_back(x, s=1.4):
    x = min(1, max(0, x)); x -= 1; return x * x * ((s + 1) * x + s) + 1
def lerp(a, b, x): return a + (b - a) * x

FACCE = [str(i) for i in range(10)] + ["?"]                                     # 11 facce: 0-9 e "?"
class Rullo:
    """posizione di un rullo (cifra float) nel tempo: gira a velocita v0 e si ferma sul bersaglio a t_stop (None = non si ferma)"""
    def __init__(self, target, v0, t_dec, t_stop, fase, v_finale=0.0, facce=10):
        self.t, self.v0, self.td, self.ts, self.f, self.vf, self.n = target, v0, t_dec, t_stop, fase, v_finale, facce
    def pos(self, t):
        if self.ts is None:                                                       # rallenta a vf ma continua a girare
            if t < self.td: return self.f + self.v0 * t
            T = 1.2; x = min(t - self.td, T); base = self.f + self.v0 * self.td
            d = self.v0 * x - (self.v0 - self.vf) * x * x / (2 * T)
            if t - self.td > T: d += self.vf * (t - self.td - T)
            return base + d
        T = self.ts - self.td
        if t >= self.ts: return float(self.t)
        if t >= self.td: return self.t - (self.v0 / (2 * T)) * (self.ts - t) ** 2
        return self.t - self.v0 * T / 2 - self.v0 * (self.td - t)
    def vel(self, t, dt=1 / 600): return abs(self.pos(t + dt) - self.pos(t)) / dt

# ---------------- DISEGNO ----------------
FIG_CELLA = (150, 226)
def contatore_animato(rulli, t, label="QUANTO TI COSTA IN PIÙ", cell=FIG_CELLA):
    cw, ch = cell; gap = 10; f = F("mono", int(ch * 0.62)); fl = F("mono", 26)
    celle = ["€"] + [r for r in rulli[:1]] + ["."] + rulli[1:]
    larg = cw * 5 + cw // 3 + gap * 5; w = max(larg + 60, int(fl.getlength(label)) + 110); h = ch + 110
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=22, fill=(24, 25, 29, 255), outline=(70, 72, 78, 255), width=3)
    d.rounded_rectangle([6, 6, w - 7, h - 7], radius=18, outline=(12, 12, 14, 255), width=3)
    d.text((30, 18), label, font=fl, fill=GRIGIO)
    if int(t * 2) % 2 == 0: d.ellipse([w - 44, 26, w - 28, 42], fill=ROSSO)          # spia che lampeggia
    else: d.ellipse([w - 44, 26, w - 28, 42], fill=(90, 20, 18))
    x = (w - larg) // 2; y = 70
    for c in celle:
        if c == ".":
            d.ellipse([x + cw // 6 - 8, y + ch - 34, x + cw // 6 + 8, y + ch - 18], fill=ROSSO); x += cw // 3 + gap; continue
        cel = Image.new("RGBA", (cw, ch), NERO + (255,)); dc = ImageDraw.Draw(cel)
        if c == "€": dc.text((cw / 2, ch / 2), "€", font=f, fill=ROSSO, anchor="mm"); blur = 0
        else:
            nf = c.n; p = c.pos(t) % nf; base = int(math.floor(p)); fr = p - base
            for k, oy in ((base, -fr * ch), ((base + 1) % nf, (1 - fr) * ch), ((base - 1) % nf, -(1 + fr) * ch)):
                fc = FACCE[k]; dc.text((cw / 2, ch / 2 + oy), fc, font=f, fill=(GRIGIO if fc == "?" else ROSSO), anchor="mm")
            v = c.vel(t); blur = min(7, v * 0.45)
        if blur > 0.4: cel = cel.resize((cw, max(8, int(ch / (1 + blur * 0.9)))), Image.BILINEAR).resize((cw, ch), Image.BILINEAR)   # mosso verticale
        sh = OMBRA_CELLA.get(cell)
        if sh is None:
            sh = Image.new("RGBA", (cw, ch), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
            for k in range(ch):
                q = abs(k - ch / 2) / (ch / 2); ds.line([0, k, cw, k], fill=(0, 0, 0, int(215 * q ** 2.2)))
            ds.line([0, ch * 0.5, cw, ch * 0.5], fill=(255, 255, 255, 18), width=2); OMBRA_CELLA[cell] = sh
        cel.alpha_composite(sh); im.alpha_composite(cel, (x, y))
        d.rectangle([x - 2, y - 2, x + cw + 1, y + ch + 1], outline=(55, 57, 63), width=2); x += cw + gap
    gl = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(gl).rounded_rectangle([14, 64, w - 14, 64 + ch * 0.35], radius=10, fill=(255, 255, 255, 14))
    im.alpha_composite(gl); return im
OMBRA_CELLA = {}

def testo_ombra(img, xy, txt, font, fill, anchor="mm", alpha=255, ombra=True):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    if ombra: d.text((xy[0] + 3, xy[1] + 4), txt, font=font, fill=(0, 0, 0, int(alpha * 0.7)), anchor=anchor)
    d.text(xy, txt, font=font, fill=fill + (int(alpha),), anchor=anchor); img.alpha_composite(lay)

def barra_sottotitolo(img, frase, alpha):
    if alpha <= 0: return
    f = F("corpo", 46); fw = f.getlength(frase); y = H - 132
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([(W - fw) / 2 - 32, y, (W + fw) / 2 + 32, y + 88], radius=14, fill=(8, 8, 10, int(215 * alpha)))
    d.text((W / 2, y + 44), frase, font=f, fill=CARTA + (int(255 * alpha),), anchor="mm"); img.alpha_composite(lay)

def particelle(n=70, seed=4):
    rng = random.Random(seed)
    return [(rng.uniform(80, 1100), rng.uniform(40, 760), rng.uniform(1.2, 3.4), rng.uniform(-9, 9), rng.uniform(-14, -3), rng.uniform(0, 6.28)) for _ in range(n)]

def main():
    voce, sr, tm = costruisci_voce(); durata = len(voce) / sr
    NF = int(round(durata * FPS)); durata_v = NF / FPS
    s = [a for a, b in tm]; e = [b for a, b in tm]
    T_B, T_C, T_D, T_R4, T_E = s[2], s[4], s[5], s[6], s[7]
    # rulli: cifre 2 8 4 7
    rul = [Rullo(2 + 110, 13, T_C + 0.15, T_C + 1.10, 0.3), Rullo(8 + 130, 15, T_C + 0.6, T_C + 1.9, 2.1),
           Rullo(10 + 154, 17, T_C + 1.5, T_C + 2.6, 5.5, facce=11), Rullo(10 + 176, 19, T_C + 1.7, T_C + 2.8, 7.7, facce=11)]
    T_TIMBRO = e[7] - 0.05; T_CONT = 0.55
    eventi = {"carta": T_D + 0.02, "lente": T_R4 + 0.15, "timbro": T_TIMBRO, "tic": []}
    last = [None] * 4; t_ult = -1
    for k in range(int(durata_v * 1000)):                                        # tic ogni volta che un rullo scatta
        tt = k / 1000
        if tt < T_CONT: continue
        for i, r in enumerate(rul):
            q = int(math.floor(r.pos(tt)))
            if last[i] is not None and q != last[i] and tt - t_ult > 0.045: eventi["tic"].append(tt); t_ult = tt
            last[i] = q
    fx = sfx(durata_v, sr, tm, eventi)
    vv = np.zeros(len(fx), np.float32); vv[:min(len(voce), len(fx))] = voce[:len(fx)]
    for nome, arr in (("voce", vv), ("fx", fx)):
        w_ = wave.open(os.path.join(OUT, f"_{nome}.wav"), "wb"); w_.setnchannels(1); w_.setsampwidth(2); w_.setframerate(sr)
        w_.writeframes((np.clip(arr, -1, 1) * 32767).astype(np.int16).tobytes()); w_.close()
    json.dump({"durata": durata_v, "frames": NF, "frasi": tm, "timbro": T_TIMBRO}, open(os.path.join(OUT, "tempi.json"), "w"), indent=1)

    # ---- livelli fissi ----
    desk = G.scrivania(0.92); desk_blur = desk.filter(ImageFilter.GaussianBlur(7))
    ct, _ = G.contratto(G.RIGHE, h=830); ct_hl, _ = G.contratto(G.RIGHE, evid="Maxirata finale", h=830)
    ROT = -1.5; ct_r = ct.rotate(ROT, expand=True, resample=Image.BICUBIC); ct_sh, pad = G.ombra(ct_r)
    PX, PY = 150, 52                                                             # posizione finale del foglio (angolo, con ombra)
    riga4_y = 222 + 3 * 76                                                        # nel foglio non ruotato
    grana = [Image.effect_noise((W // 2, H // 2), 22).resize((W, H)).convert("L") for _ in range(6)]
    parts = particelle()
    timbro = G.timbro("PRATICA N. 001", ROSSO, 44, 9).rotate(6, expand=True, resample=Image.BICUBIC)
    cart = Image.new("RGBA", (600, 230), CARTA + (255,)); dcart = ImageDraw.Draw(cart)
    dcart.text((28, 22), "FASCICOLO  ·  FINANZIAMENTO AUTO", font=F("mono", 22), fill=GRIGIO); dcart.line([28, 60, 572, 60], fill=(205, 200, 190), width=2)
    cart = G.grana_carta(cart, 21).rotate(-3, expand=True, resample=Image.BICUBIC); cart_s, cart_p = G.ombra(cart)
    CX_C, CY_C = 1590, 470
    pill = G.pillola("LA CIFRA ESATTA ALLA FINE DEL VIDEO", ROSSO, 30)
    ff = F("titolo", 128); sub = {2: "Questo video non ti serve…", 3: "…a meno che la rata non sia sotto i 200 €.",
                                  4: "Perché alla fine paghi quasi 3.000 € in più.", 5: "E non è scritto in piccolo.",
                                  6: "È alla riga 4.", 7: "Apriamo la pratica."}
    ff_sub_alpha = lambda t, i: min(ease((t - s[i] + 0.05) / 0.18), 1.0) if t >= s[i] - 0.05 else 0
    sh_cache = {}
    enc = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                            "-i", "-", "-c:v", "libx264", "-preset", "slow", "-crf", "15", "-pix_fmt", "yuv420p", os.path.join(OUT, "_video.mp4")],
                           stdin=subprocess.PIPE)
    os.makedirs(os.path.join(OUT, "frames"), exist_ok=True)
    for fi in range(NF):
        t = fi / FPS
        foglio_in = ease_back((t - T_D) / 0.55, 1.1) if t >= T_D else 0
        dof = ease((t - T_D) / 0.5) if t >= T_D else 0
        img = Image.blend(desk, desk_blur, dof * 0.85) if dof > 0 else desk.copy()
        # luce della lampada che si accende (con piccolo sfarfallio)
        luce = ease(t / 0.45) * (0.92 + 0.08 * math.sin(t * 37) * math.exp(-t * 3))
        if luce < 1:
            buio = Image.new("RGBA", (W, H), (0, 0, 0, int(255 * (1 - luce) * 0.95))); img.alpha_composite(buio)
        # pulviscolo nel fascio di luce
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for (x0, y0, r, vx, vy, ph) in parts:
            x = (x0 + vx * t + 6 * math.sin(t * 0.7 + ph)) % 1150; y = (y0 + vy * t) % 800
            a = int(55 * luce * (0.5 + 0.5 * math.sin(t * 1.3 + ph)) * max(0, 1 - math.hypot(x - 380, y - 260) / 620))
            if a > 2: d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 220, 170, a))
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(1.2)))
        # ---- titolo "Firma pure. Davvero."
        if t < T_C + 0.3:
            out_a = 1 - ease((t - T_C) / 0.3) if t >= T_C else 1
            a1 = ease((t - s[0] + 0.02) / 0.25) * out_a; a2 = ease((t - s[1] + 0.02) / 0.22) * out_a
            yt = 215
            w1, w2 = ff.getlength("Firma pure."), ff.getlength("Davvero."); gap = 40; x1 = (W - w1 - gap - w2) / 2
            if a1 > 0: testo_ombra(img, (x1, yt + 18 * (1 - a1)), "Firma pure.", ff, CARTA, anchor="lm", alpha=255 * a1)
            if a2 > 0: testo_ombra(img, (x1 + w1 + gap, yt + 18 * (1 - a2)), "Davvero.", ff, GIALLO, anchor="lm", alpha=255 * a2)
        # ---- foglio del contratto
        if foglio_in > 0:
            yy = PY + (1 - foglio_in) * 1150
            hl = ease((t - T_R4) / 0.35) if t >= T_R4 else 0
            if hl <= 0: base = ct_sh
            elif hl >= 1:
                if "hl" not in sh_cache: sh_cache["hl"] = G.ombra(ct_hl.rotate(ROT, expand=True, resample=Image.BICUBIC))[0]
                base = sh_cache["hl"]
            else:
                tmp = ct.copy(); wcut = int(hl * ct.width); tmp.paste(ct_hl.crop((0, 0, wcut, ct.height)), (0, 0))
                base = G.ombra(tmp.rotate(ROT, expand=True, resample=Image.BICUBIC))[0]
            img.alpha_composite(base, (int(PX - pad), int(yy - pad)))
            # lente sulla cifra della riga 4
            if t >= T_R4 + 0.1:
                k = ease((t - T_R4 - 0.1) / 0.45)
                cx_t, cy_t = PX + 902, PY + 486
                cx = lerp(W + 250, cx_t, k); cy = lerp(cy_t + 120, cy_t, k)
                le = G.lente(img.convert("RGB"), (cx_t, cy_t), r=165, zoom=1.55)
                le_s, lp = G.ombra(le); img.alpha_composite(le_s, (int(cx - 185 - lp), int(cy - 185 - lp)))
        # ---- timbro PRATICA N. 001
        if t >= T_E - 0.05:
            k = ease((t - T_E + 0.05) / 0.35); xx = lerp(W + 380, CX_C, k)
            img.alpha_composite(cart_s, (int(xx - cart.width / 2 - cart_p), int(CY_C - cart.height / 2 - cart_p)))
        if t >= T_TIMBRO:
            k = min(1, (t - T_TIMBRO) / 0.16); sc = lerp(1.7, 1.0, k * k)
            tb = timbro.resize((int(timbro.width * sc), int(timbro.height * sc)), Image.BICUBIC)
            if k < 1: tb.putalpha(tb.split()[3].point(lambda v: int(v * (0.4 + 0.6 * k))))
            img.alpha_composite(tb, (int(CX_C - tb.width / 2), int(CY_C + 8 - tb.height / 2)))
        # ---- contatore
        if t >= T_CONT:
            c = contatore_animato(rul, t)
            a_in = ease((t - T_CONT) / 0.45)
            big = 1.0 if t < T_C else lerp(1.0, 1.12, ease((t - T_C) / 0.6))
            if t >= T_D: big = lerp(1.12, 0.60, ease((t - T_D) / 0.55))
            cw_, chh = int(c.width * big), int(c.height * big); c = c.resize((cw_, chh), Image.LANCZOS)
            cx0, cy0 = (W - cw_) / 2, 430 + (1 - a_in) * 140
            if t >= T_C: cy0 = lerp(430, 330, ease((t - T_C) / 0.6))
            if t >= T_D:
                k = ease((t - T_D) / 0.55); cx0 = lerp((W - cw_) / 2, W - cw_ - 60, k); cy0 = lerp(330, 40, k)
            if a_in < 1: c.putalpha(c.split()[3].point(lambda v: int(v * a_in)))
            cs, cp = G.ombra(c); img.alpha_composite(cs, (int(cx0 - cp), int(cy0 - cp)))
        # pillola: compare all'80% della scena C, sparisce quando entra il foglio
        t_pill = T_C + 0.8 * (T_D - T_C)
        if t_pill <= t < T_D + 0.2:
            a = ease((t - t_pill) / 0.25) * (1 - ease((t - T_D) / 0.2) if t >= T_D else 1)
            p = pill.copy(); p.putalpha(p.split()[3].point(lambda v: int(v * a))); img.alpha_composite(p, (int((W - p.width) / 2), 870))
        # sottotitoli
        for i in range(2, 8):
            fine = s[i + 1] - 0.05 if i < 7 else durata_v + 1
            if s[i] - 0.05 <= t < fine: barra_sottotitolo(img, sub[i], ff_sub_alpha(t, i))
        # camera: spinta lenta + scossone del timbro
        zoom = 1.0 + 0.035 * (t / durata_v); dx = dy = 0
        if T_TIMBRO + 0.16 <= t < T_TIMBRO + 0.42:
            q = (t - T_TIMBRO - 0.16) / 0.26; dx = 9 * math.sin(q * 40) * (1 - q); dy = 7 * math.cos(q * 33) * (1 - q)
        cwz, chz = W / zoom, H / zoom; x0 = (W - cwz) / 2 + dx; y0 = (H - chz) / 2 + dy
        fr = img.convert("RGB").crop((x0, y0, x0 + cwz, y0 + chz)).resize((W, H), Image.BICUBIC)
        g = (np.asarray(grana[fi % len(grana)], np.int16) - 128) * 0.07
        fr = Image.fromarray(np.clip(np.asarray(fr, np.int16) + g[..., None], 0, 255).astype(np.uint8))
        enc.stdin.write(fr.tobytes())
        fr.resize((384, 216)).save(os.path.join(OUT, "frames", f"{fi:04d}.jpg"), quality=85)
        if fi in (0, 20, 60, 120, 200, 260, 300, 335, 360, 395, 430, 450, NF - 1): fr.save(os.path.join(OUT, "frames", f"full_{fi:04d}.png"))
    enc.stdin.close(); enc.wait()
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", os.path.join(OUT, "_video.mp4"), "-i", os.path.join(OUT, "_voce.wav"),
                    "-i", os.path.join(OUT, "_fx.wav"), "-filter_complex",
                    "[1:a]loudnorm=I=-15:TP=-1.5,volume=1.0[v];[2:a]volume=1.0[f];[v][f]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
                    os.path.join(OUT, "demo-gancio.mp4")], check=True)
    print("frames", NF, "durata", durata_v)

if __name__ == "__main__":
    main()
