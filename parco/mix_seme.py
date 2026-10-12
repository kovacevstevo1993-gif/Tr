#!/usr/bin/env python3
"""Mix audio Short 'Il seme magico': voci italiane + musica + effetti sincronizzati (passi, pioggia, crescita albero, mele, morsi...) -> mix_seme.wav"""
import numpy as np
import mixlib as M
import short_seme as R

N = int(R.DUR * M.SR)
voc = np.zeros(N); fol = np.zeros(N); mus = M.music(R.DUR, bpm=100); bird = M.birds(R.DUR)
rng = np.random.default_rng(4)

def boing(buf, t, g=0.5):
    n = int(.28 * M.SR); tt = np.arange(n) / M.SR; f = 260 + 700 * tt * 3 - 900 * tt ** 2 * 4
    M.put(buf, np.sin(2 * np.pi * np.cumsum(f) / M.SR) * np.exp(-9 * tt), t, g)
def crunch(buf, t, g=0.5):
    for j in range(3):
        n = int(.05 * M.SR); M.put(buf, M.bp(rng.normal(size=n), 1500, 6000) * np.exp(-np.arange(n) / M.SR * 60), t + j * 0.07, g)
def patter(buf, t, g=0.4):
    n = int(.05 * M.SR); M.put(buf, M.lp(rng.normal(size=n), 900) * np.exp(-np.arange(n) / M.SR * 70), t, g)
def rise(buf, t, g=0.5, dur=0.9, f0=300, f1=1400):
    n = int(dur * M.SR); tt = np.arange(n) / M.SR; f = f0 + (f1 - f0) * (tt / dur) ** 1.4
    M.put(buf, np.sin(2 * np.pi * np.cumsum(f) / M.SR) * np.sin(np.pi * tt / dur) ** 1.2, t, g)
def rain(buf, t0, t1, g=0.35):
    n = int((t1 - t0) * M.SR); env = np.minimum(1, np.minimum(np.arange(n) / (0.4 * M.SR), (n - np.arange(n)) / (0.4 * M.SR)))
    M.put(buf, M.bp(rng.normal(size=n), 2500, 9000) * env, t0, g)
    for k in range(int((t1 - t0) * 14)): M.bloop(buf, t0 + rng.uniform(0, t1 - t0), rng.uniform(900, 1700), 0.05)

for name, t0, t1, per, kind in R.GAIT:                                          # passi
    q = per / 2; k = 0
    while t0 + k * q < t1:
        (M.thud if kind == "walk" else patter)(fol, t0 + k * q, 0.2 if kind == "walk" else 0.4); k += 1
M.shimmer(fol, 0.25, 0.8)                                                      # il seme che brilla (hook)
M.shimmer(fol, R.T_PICK + 0.4, 0.8, (1318.5, 1568, 2093, 2637, 3136))          # lo raccoglie
for tb in (R.TB, R.TC):                                                        # cerchio magico
    M.whoosh(fol, tb, 0.6, 0.9); M.shimmer(fol, tb + 0.2, 0.9, (784, 1046.5, 1318.5, 1568, 2093))
M.thud(fol, R.T_SEED_IN, 0.6); M.bloop(fol, R.T_SEED_IN, 380, 0.5)             # il seme nella terra
M.whoosh(fol, R.CL0, 0.35, 1.4); rain(fol, R.RAIN0, R.RAIN1)                   # nuvoletta e pioggia
M.shimmer(fol, R.T_SPR, 0.9); M.pop(fol, R.T_SPR, 520, 0.9)                    # pop! germoglio
for k, tt in enumerate((R.G0 + 0.3, R.G0 + 1.4, R.G0 + 2.5)):                  # l'albero cresce a scatti
    rise(fol, tt, 0.45, 0.9, 260 + 120 * k, 1200 + 400 * k); M.thud(fol, tt + 0.55, 0.6)
M.shimmer(fol, R.G0 + 0.2, 0.9, (523, 659, 784, 1046.5, 1318.5)); M.shimmer(fol, R.G1 - 0.1, 1.0, (1046.5, 1318.5, 1568, 2093, 2637))
M.thud(fol, R.G1, 0.9)
for i, (dl, dx, dy) in enumerate(R.APPLES):                                    # mele che cadono e rimbalzano
    tf = R.FALL0 + dl; yg = (1690, 1720, 1700, 1740, 1660, 1650)[i]; y0 = R.P[1] - R.TREE_H * 0.78 + dy
    tl = tf + (2 * (yg - y0) / 2600) ** 0.5; M.thud(fol, tl, 0.35); M.bloop(fol, tl, 420, 0.35); M.thud(fol, tl + 0.3, 0.18)
for n, tl in R.LAND.items(): M.bloop(fol, tl, 560, 0.5); M.thud(fol, tl, 0.3)  # mela nelle mani
for n, et in R.EAT.items():
    for j in range(3): crunch(fol, et + 0.6 + j * 0.8, 0.45)                   # morsi
for name, ev in R.EV.items():                                                  # salti e scatti
    for (te, pose, dur) in ev:
        if pose == "salto": boing(fol, te, 0.3)
        if pose == "afferra": M.whoosh(fol, te - 0.05, 0.22, 0.2)
M.shimmer(fol, R.V["n10"], 0.7, (1046.5, 1318.5, 1568, 2093, 2637)); M.shimmer(fol, R.V["end"] + 0.9, 0.9, (1568, 2093, 2637, 3136, 3951))

dr = []
for k, t0, who, txt, d in R.VOICES:
    sig = M.load_voice(f"audioF/{k}.wav"); M.put(voc, sig, t0, 0.95 if who != "narr" else 1.0); dr.append((t0, t0 + d + 0.15))
print("picco dB", M.finish(np.zeros(N), "mix_seme.wav", voc, mus, fol, bird, dr, mg=0.12, fg=0.34))
