#!/usr/bin/env python3
"""Mix audio Short 'Balla con la volpe' -> mix_balla.wav"""
import numpy as np
import mixlib as M
import short_balla2 as R

N = int(R.DUR * M.SR)
voc = np.zeros(N); fol = np.zeros(N); mus = M.music(R.DUR, bpm=120); bird = np.zeros(N)
rng = np.random.default_rng(5)
def noise_env(buf, t0, t1, lo, hi, g, a=0.3, r=0.4, shape=None):
    n = int((t1 - t0) * M.SR); x = M.bp(rng.normal(size=n), lo, hi); i = np.arange(n) / M.SR
    env = np.clip(np.minimum(1, np.minimum(i / a, (t1 - t0 - i) / r)), 0, 1)
    if shape is not None: env = env * shape(i / (t1 - t0))
    M.put(buf, x * env, t0, g)
def boing(buf, t, g=0.5, dur=0.28, slow=1.0):
    n = int(dur * M.SR); tt = np.arange(n) / M.SR / slow; f = 260 + 2100 * tt - 3600 * tt ** 2
    M.put(buf, np.sin(2 * np.pi * np.cumsum(f) / M.SR / slow) * np.exp(-9 * tt), t, g)
def beep(buf, t, f=880, g=0.3, d=0.18):
    tt = np.arange(int(d * M.SR)) / M.SR; M.put(buf, np.sign(np.sin(2 * np.pi * f * tt)) * 0.4 * np.exp(-6 * tt), t, g)
def tap(buf, t, g=0.25):
    n = int(.08 * M.SR); M.put(buf, M.lp(rng.normal(size=n), 1200) * np.exp(-np.arange(n) / M.SR * 50), t, g)
def clap(buf, t, g=0.5):
    n = int(.09 * M.SR); M.put(buf, M.bp(rng.normal(size=n), 900, 6000) * np.exp(-np.arange(n) / M.SR * 45), t, g)
M.whoosh(fol, 0.05, 0.5, 0.7); M.shimmer(fol, 0.1, 0.8)
t = 0.0
while t < R.DUR - 0.3: M.thud(fol, t, 0.30 if int(round(t / 0.5)) % 2 == 0 else 0.15); t += 0.5          # cassa a tempo
for t0, pz, d in R.EV:
    if pz == "mani": clap(fol, t0 + 0.08, 0.7)
for (j0, jd, hg) in R.JUMPS:
    if hg > 100: boing(fol, j0, 0.3); M.thud(fol, j0 + jd, 0.45)
for t0, pz, d in R.EV:
    if pz == "lato": M.whoosh(fol, t0, 0.4, 0.6)
tt = 0.0
while tt < 2.0: M.thud(fol, tt, 0.12); tt += 0.32                                  # passi d'entrata
M.shimmer(fol, R.V["v6"], 1.0, (1046.5, 1318.5, 1568, 2093, 2637))
for k in range(12): M.pop(fol, R.V["v6"] + 0.4 + k * 0.06, 600 + 70 * k, 0.25)
M.shimmer(fol, R.V["end"] + 0.9, 0.9, (1568, 2093, 2637, 3136, 3951))
dr = []
for k, t0, who, d in R.VOICES:
    sig = M.load_voice(f"audioM/{k}.wav"); M.put(voc, sig, t0, 1.0); dr.append((t0, t0 + d + 0.15))
print("picco dB", M.finish(np.zeros(N), "/tmp/claude-0/prova/mix_balla2.wav", voc, mus, fol, bird, dr, mg=0.16, fg=0.34))
