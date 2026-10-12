#!/usr/bin/env python3
"""Mix audio dello Short 'Il barattolo misterioso': voci + musica dolce + passi + effetti. -> mix_cucina.wav"""
import numpy as np
import mixlib as M
import short_cucina as R

N = int(R.DUR * M.SR)
voc = np.zeros(N); fol = np.zeros(N)
mus = M.music(R.DUR, bpm=100); bird = np.zeros(N)

# passi dei tre personaggi (stessa regola dell'animazione: un appoggio ogni 70 px)
for name, g in (("mouse", .8), ("chip", .9), ("spike", .75)):
    prev = None
    for i in range(int(R.DUR * 240)):
        t = i / 240; x, y, mv, d, cum = R.seg(name, t); ph = int(cum / 70) if mv else prev
        if prev is not None and mv and ph != prev: M.thud(fol, t, 0.35 * g)
        prev = ph if mv else prev

# barattolo che si agita: toc toc sommessi prima dell'apertura
t = 0.0
while t < R.TP - 0.3:
    if (t % 1.6) < 1.0: M.tonk(fol, t, 0.10 + 0.25 * t / R.TP)
    t += 0.28
M.whoosh(fol, R.V["n2"] - 0.1, 0.25, 0.3)                      # entrano di corsa
M.pop(fol, R.TP, 420, 0.8); M.shimmer(fol, R.TP + 0.05, 1.1)   # coperchio che salta + magia
M.shimmer(fol, R.V["t2"], 0.9, (1318.5, 1568, 2093, 2637, 3136))
for k in range(3): M.bloop(fol, R.V["n4"] + 0.25 + k * 0.28 + 0.7, 520 + 90 * k, 0.5)   # i biscotti arrivano
M.shimmer(fol, R.V["end"] + 0.7, 0.9, (1568, 2093, 2637, 3136, 3951))                   # pulsante iscriviti
for (t0, t1, a, b) in R.SHOTS[1:]:
    if t0 < R.DUR: M.whoosh(fol, t0 - 0.04, 0.18, 0.14)

dr = []
for k, t0, who, txt, d in R.VOICES:
    sig = M.load_voice(f"audioC/{k}.wav"); M.put(voc, sig, t0, 0.95); dr.append((t0, t0 + d + 0.15))
print("picco dB", M.finish(np.zeros(N), "mix_cucina.wav", voc, mus, fol, bird, dr, mg=0.13, fg=0.34))
