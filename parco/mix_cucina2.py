#!/usr/bin/env python3
"""Mix audio Short v2: voci italiane + musica + effetti sincronizzati con l'animazione -> mix_cucina2.wav"""
import numpy as np
import mixlib as M
import short_cucina2 as R

N = int(R.DUR * M.SR)
voc = np.zeros(N); fol = np.zeros(N); mus = M.music(R.DUR, bpm=104); bird = np.zeros(N)
rng = np.random.default_rng(3)

def boing(buf, t, g=0.5):
    n = int(.28 * M.SR); tt = np.arange(n) / M.SR; f = 260 + 700 * tt * 3 - 900 * tt ** 2 * 4
    M.put(buf, np.sin(2 * np.pi * np.cumsum(f) / M.SR) * np.exp(-9 * tt), t, g)
def crunch(buf, t, g=0.5):
    for j in range(3):
        n = int(.05 * M.SR); M.put(buf, M.bp(rng.normal(size=n), 1500, 6000) * np.exp(-np.arange(n) / M.SR * 60), t + j * 0.07, g)
def patter(buf, t, g=0.4):
    n = int(.05 * M.SR); M.put(buf, M.lp(rng.normal(size=n), 900) * np.exp(-np.arange(n) / M.SR * 70), t, g)

# passi: un appoggio a ogni mezzo ciclo (camminata) / ogni passo (corsa)
for name, t0, t1, per, kind in R.GAIT:
    q = per / 2; k = 0
    while t0 + k * q < t1:
        tt = t0 + k * q
        (M.thud if kind == "walk" else patter)(fol, tt, 0.28 if kind == "walk" else 0.42)
        k += 1
for kt in R.KNOCKS: M.tonk(fol, kt, 0.55 if kt < R.V["n3"] else 0.3)            # toc toc
for name, ev in R.EV.items():                                                    # salti / bruschi cambi
    for (te, pose, dur) in ev:
        if pose == "salto": boing(fol, te, 0.35)
        if pose == "afferra": M.whoosh(fol, te - 0.05, 0.25, 0.2)
M.pop(fol, R.TP, 420, 0.9); M.shimmer(fol, R.TP + 0.05, 1.2); M.whoosh(fol, R.TP + 0.2, 0.5, 0.6)
for k, tt in enumerate((R.TP + 1.2, R.TP + 3.0, R.TP + 5.0, R.TP + 7.0)): M.shimmer(fol, tt, 0.45, (1568, 2093, 2637, 3136, 3951))
M.shimmer(fol, R.V["n6"] + 0.2, 0.9, (1318.5, 1568, 2093, 2637, 3136))
for k, n in enumerate(("spike", "chip", "mouse")): M.bloop(fol, R.V["n6"] + 1.4 + k * 0.32 + 0.8, 520 + 90 * k, 0.5)
for n, et in R.EAT.items(): crunch(fol, et + 0.55, 0.45); crunch(fol, et + 1.05, 0.45); crunch(fol, et + 1.55, 0.45)
M.shimmer(fol, R.V["n7"], 0.7, (1046.5, 1318.5, 1568, 2093, 2637)); M.shimmer(fol, R.V["end"] + 0.9, 0.9, (1568, 2093, 2637, 3136, 3951))
for (t0, ax, ay, az), (t1, bx, by, bz) in zip(R.CAM, R.CAM[1:]):
    if t0 > 0.5 and abs(bz - az) > 0.2 and t1 - t0 > 0.5: M.whoosh(fol, t0, 0.12, min(0.6, t1 - t0))

dr = []
for k, t0, who, txt, d in R.VOICES:
    sig = M.load_voice(f"audioD/{k}.wav"); M.put(voc, sig, t0, 0.95 if who != "narr" else 1.0); dr.append((t0, t0 + d + 0.15))
print("picco dB", M.finish(np.zeros(N), "mix_cucina2.wav", voc, mus, fol, bird, dr, mg=0.12, fg=0.34))
