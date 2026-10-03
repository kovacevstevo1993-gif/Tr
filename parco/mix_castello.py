#!/usr/bin/env python3
"""Mix audio Short 'Il castello di sabbia': voci italiane + musica + effetti sincronizzati -> mix_castello.wav"""
import numpy as np
import mixlib as M
import short_castello as R

N = int(R.DUR * M.SR)
voc = np.zeros(N); fol = np.zeros(N); mus = M.music(R.DUR, bpm=104); bird = np.zeros(N)
rng = np.random.default_rng(6)

def boing(buf, t, g=0.5):
    n = int(.28 * M.SR); tt = np.arange(n) / M.SR; f = 260 + 700 * tt * 3 - 900 * tt ** 2 * 4
    M.put(buf, np.sin(2 * np.pi * np.cumsum(f) / M.SR) * np.exp(-9 * tt), t, g)
def patter(buf, t, g=0.4):
    n = int(.05 * M.SR); M.put(buf, M.lp(rng.normal(size=n), 900) * np.exp(-np.arange(n) / M.SR * 70), t, g)
def sandpat(buf, t, g=0.3):
    n = int(.07 * M.SR); M.put(buf, M.lp(rng.normal(size=n), 1400) * np.exp(-np.arange(n) / M.SR * 45), t, g); M.thud(buf, t, g * 0.5)
def rise(buf, t, g=0.5, dur=0.9, f0=300, f1=1400):
    n = int(dur * M.SR); tt = np.arange(n) / M.SR; f = f0 + (f1 - f0) * (tt / dur) ** 1.4
    M.put(buf, np.sin(2 * np.pi * np.cumsum(f) / M.SR) * np.sin(np.pi * tt / dur) ** 1.2, t, g)
def noise_env(buf, t0, t1, lo, hi, g, a=0.3, r=0.4, shape=None):
    n = int((t1 - t0) * M.SR); x = M.bp(rng.normal(size=n), lo, hi); i = np.arange(n) / M.SR
    env = np.minimum(1, np.minimum(i / a, (t1 - t0 - i) / r)); env = np.clip(env, 0, 1)
    if shape is not None: env = env * shape(i / (t1 - t0))
    M.put(buf, x * env, t0, g)
def toot(buf, t, g=0.35, f0=420, up=1.5, dur=0.55):
    """trombetta dell'elefantino: tono con vibrato che sale"""
    n = int(dur * M.SR); tt = np.arange(n) / M.SR; f = f0 * (1 + (up - 1) * np.minimum(1, tt / 0.12)) * (1 + 0.02 * np.sin(2 * np.pi * 22 * tt))
    ph = 2 * np.pi * np.cumsum(f) / M.SR; sig = (np.sin(ph) + 0.5 * np.sin(2 * ph) + 0.3 * np.sin(3 * ph)) * np.minimum(1, tt / 0.03) * np.exp(-3.5 * np.maximum(0, tt - dur * 0.45))
    M.put(buf, M.lp(sig, 3500), t, g)
def gullcry(buf, t, g=0.18):
    n = int(.45 * M.SR); tt = np.arange(n) / M.SR; f = 1500 + 500 * np.sin(2 * np.pi * 3 * tt) - 700 * tt
    M.put(buf, np.sin(2 * np.pi * np.cumsum(f) / M.SR) * np.sin(np.pi * tt / 0.45) ** 1.5, t, g)

# mare: sottofondo morbido a ondine
for k in range(int(R.DUR / 5.5) + 1):
    t0 = k * 5.5; noise_env(fol, t0, min(R.DUR, t0 + 5.0), 400, 2400, 0.07, 1.8, 2.2)
# gabbiani
for t0 in (1.0, 3.6, 12.0, R.TB + 4.0, R.TB + 9.0, R.TC + 1.0, R.TC + 3.0, R.TC + 7.0): gullcry(fol, t0 + 1.2); gullcry(fol, t0 + 2.4, 0.14)
M.whoosh(fol, 0.05, 0.5, 0.7)                                                      # hook
for t0, t1, per, kind in [(g[1], g[2], g[3], g[4]) for g in R.GAIT]:               # passi
    q = per / 2; k = 0
    while t0 + k * q < t1:
        (M.thud if kind == "walk" else patter)(fol, t0 + k * q, 0.16 if kind == "walk" else 0.4); k += 1
# castello 1: colpetti sulla sabbia mentre costruisce
tt_ = 0.2
while tt_ < R.V["t1"] - 0.3: sandpat(fol, tt_, 0.2); tt_ += 0.385
for kt in (0.9, 1.9, 2.9): M.pop(fol, kt, 420, 0.4); M.thud(fol, kt + 0.3, 0.3)
M.shimmer(fol, R.V["t1"] - 0.1, 0.6)
# onda: cresce, si schianta, si ritira
noise_env(fol, R.T_WS - 1.6, R.T_W, 150, 1800, 0.30, 1.4, 0.05, lambda u: u ** 1.8)
noise_env(fol, R.T_W - 0.05, R.T_W + 0.9, 300, 9000, 0.75, 0.02, 0.8)
M.thud(fol, R.T_W, 0.9); M.bloop(fol, R.T_W + 0.1, 300, 0.4)
noise_env(fol, R.T_W + 0.8, R.T_WE, 1000, 7000, 0.28, 0.4, 1.2)
boing(fol, R.T_W - 0.8, 0.35)
M.tonk(fol, R.V["t2"] + 0.1, 0.0)
# elefantino: trombetta all'arrivo, acqua, getto
toot(fol, R.V["e1"] - 0.4, 0.34)
noise_env(fol, R.T_FILL0 + 0.3, R.T_FILL1, 1800, 7500, 0.34, 0.15, 0.25)
for j in range(10): M.bloop(fol, R.T_FILL0 + 0.6 + j * 0.1, rng.uniform(500, 900), 0.22)
noise_env(fol, R.T_SPRAY0 + 0.25, R.T_SPRAY1, 2500, 9500, 0.40, 0.2, 0.3)
for j in range(14): M.bloop(fol, R.T_SPRAY0 + 0.8 + j * 0.12, rng.uniform(400, 800), 0.2)
M.whoosh(fol, R.T_SPRAY0 + 0.1, 0.25, 0.4)
M.shimmer(fol, R.T_SPRAY0 + 1.0, 0.5, (1318.5, 1568, 2093, 2637, 3136))
# cerchi magici
for tb in (R.TB, R.TC):
    M.whoosh(fol, tb, 0.6, 0.9); M.shimmer(fol, tb + 0.2, 0.9, (784, 1046.5, 1318.5, 1568, 2093))
# baia: costruzione a scatti
tt_ = R.max(R.V["n5"] - 0.1, R.TB + 1.05) if hasattr(R, "max") else R.V["n5"]
while tt_ < R.T_BUILD[3] + 0.4: sandpat(fol, tt_, 0.2); tt_ += 0.385
for k, tb_ in enumerate(R.T_BUILD):
    rise(fol, tb_ - 0.1, 0.4, 0.55, 260 + 90 * k, 900 + 350 * k); M.thud(fol, tb_ + 0.2, 0.55); M.pop(fol, tb_ + 0.1, 380 + 60 * k, 0.4)
M.shimmer(fol, R.T_BUILD[3] + 0.1, 1.0, (1046.5, 1318.5, 1568, 2093, 2637))
# Chip: corsa, lancio, bandiera
M.whoosh(fol, R.T_FLAG0, 0.5, 0.8); M.thud(fol, R.T_FLAG1, 0.8); M.bloop(fol, R.T_FLAG1, 700, 0.4); M.shimmer(fol, R.T_FLAG1 + 0.05, 0.8)
# getto grande e arcobaleno
toot(fol, R.T_FOUNT0 - 0.15, 0.4, 460, 1.6, 0.7)
noise_env(fol, R.T_FOUNT0, R.T_FOUNT1 + 0.8, 1500, 9000, 0.42, 0.15, 0.9)
M.shimmer(fol, R.T_RAIN, 1.1, (523, 659, 784, 1046.5, 1318.5, 1568)); M.shimmer(fol, R.T_RAIN + 0.5, 0.9, (1046.5, 1318.5, 1568, 2093, 2637))
# saltelli
for name, ev in R.EV.items():
    for (te, pose, dur) in ev:
        if pose in ("salto",): boing(fol, te, 0.28)
M.shimmer(fol, R.V["n7"], 0.7, (1046.5, 1318.5, 1568, 2093, 2637))
toot(fol, R.T_SPR3 - 0.1, 0.34, 440, 1.5, 0.6); noise_env(fol, R.T_SPR3, R.T_SPR3 + 1.8, 1500, 9000, 0.3, 0.15, 0.7)
M.shimmer(fol, R.V["end"] + 0.9, 0.9, (1568, 2093, 2637, 3136, 3951))
dr = []
for k, t0, who, txt, d in R.VOICES:
    sig = M.load_voice(f"audioG/{k}.wav"); M.put(voc, sig, t0, 0.95 if who != "narr" else 1.0); dr.append((t0, t0 + d + 0.15))
print("picco dB", M.finish(np.zeros(N), "mix_castello.wav", voc, mus, fol, bird, dr, mg=0.12, fg=0.34))
