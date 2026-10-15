#!/usr/bin/env python3
"""Mix audio Short 'Il razzo per la luna' -> mix_razzo.wav"""
import numpy as np
import mixlib as M
import short_razzo as R

N = int(R.DUR * M.SR)
voc = np.zeros(N); fol = np.zeros(N); mus = M.music(R.DUR, bpm=110); bird = np.zeros(N)
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
for k in range(int(R.DUR / 4.0) + 1): noise_env(fol, k * 4.0, min(R.DUR, k * 4.0 + 4.4), 200, 900, 0.03, 1.2, 1.5)     # notte / spazio
M.whoosh(fol, 0.05, 0.5, 0.7); M.shimmer(fol, 0.1, 0.8)
tt_ = R.T_B1 - 0.2
while tt_ < R.T_B2 - 0.3: tap(fol, tt_, 0.35); tt_ += 0.18
M.thud(fol, R.T_B1, 0.6); M.whoosh(fol, R.T_B2, 0.4, 0.5); M.tonk(fol, R.T_B2L, 0.5); M.shimmer(fol, R.T_B3, 0.7)
for n_, ti in R.T_IN.items(): boing(fol, ti, 0.3); M.pop(fol, ti + 0.5, 500, 0.4)
for i, tc in enumerate(R.T_CNT): beep(fol, tc, 660 + 110 * i, 0.30)
noise_env(fol, R.T_CNT[0], R.T_LAUNCH, 60, 400, 0.4, 0.8, 0.05, lambda u: u ** 1.5)                          # rombo che cresce
noise_env(fol, R.T_LAUNCH, R.T_W1 + 0.5, 40, 900, 1.0, 0.05, 0.8)                                           # decollo
noise_env(fol, R.T_LAUNCH, R.T_W1 + 0.3, 1500, 7000, 0.35, 0.05, 0.6)
M.thud(fol, R.T_LAUNCH, 1.0)
for tw in R.WIPES: M.whoosh(fol, tw - 0.5, 0.8, 1.0); M.shimmer(fol, tw - 0.05, 0.7, (784, 1046.5, 1318.5, 1568, 2093))
noise_env(fol, R.T_W1, R.T_W2, 60, 600, 0.35, 0.4, 0.6)                                                     # motore nello spazio
M.shimmer(fol, R.T_SAT + 0.8, 0.6, (523, 659, 784, 1046.5))
noise_env(fol, R.T_W2, R.T_LAND + 0.2, 60, 700, 0.5, 0.2, 0.2); M.thud(fol, R.T_LAND, 0.9); noise_env(fol, R.T_LAND, R.T_LAND + 1.2, 300, 3000, 0.25, 0.02, 0.9)
for n_, to in R.T_OUT.items(): boing(fol, to, 0.25, 0.5, 2.0); M.thud(fol, to + 0.75, 0.3)
for n_, js in R.JUMPS.items():
    for (j0, jd, _) in js: boing(fol, j0, 0.22, 0.7, 2.6); M.thud(fol, j0 + jd, 0.35)
M.shimmer(fol, R.T_THINK, 0.6); M.pop(fol, R.T_BITE + 0.35, 300, 0.4); M.whoosh(fol, R.T_SPIT, 0.4, 0.5); M.thud(fol, R.T_SPIT + 1.25, 0.3)
M.whoosh(fol, R.T_FLAG0, 0.35, 0.6); M.thud(fol, R.T_FLAG1, 0.5); M.shimmer(fol, R.T_FLAG1, 0.6)
M.shimmer(fol, R.T_WAVE, 0.8, (1046.5, 1318.5, 1568, 2093, 2637))
M.shimmer(fol, R.V["end"] + 0.9, 0.9, (1568, 2093, 2637, 3136, 3951))
dr = []
for k, t0, who, d in R.VOICES:
    sig = M.load_voice(f"audioJ/{k}.wav"); M.put(voc, sig, t0, 0.95 if who != "narr" else 1.0); dr.append((t0, t0 + d + 0.15))
print("picco dB", M.finish(np.zeros(N), "/tmp/claude-0/prova/mix_razzo.wav", voc, mus, fol, bird, dr, mg=0.12, fg=0.34))
