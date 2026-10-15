#!/usr/bin/env python3
"""Mix audio Short 'Nascondino nel bosco' -> mix_nascondino.wav"""
import numpy as np
import mixlib as M
import short_nascondino as R

N = int(R.DUR * M.SR)
voc = np.zeros(N); fol = np.zeros(N); mus = M.music(R.DUR, bpm=100); bird = np.zeros(N)
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
def rustle(buf, t, d=0.5, g=0.35):
    noise_env(buf, t, t + d, 1500, 8000, g, 0.03, d * 0.6, lambda u: 0.5 + 0.5 * np.abs(np.sin(u * 40)))
for k in range(int(R.DUR / 4.0) + 1): noise_env(fol, k * 4.0, min(R.DUR, k * 4.0 + 4.4), 300, 1800, 0.04, 1.2, 1.5)          # vento nel bosco
M.whoosh(fol, 0.05, 0.5, 0.7); M.shimmer(fol, 0.1, 0.8)
bird = M.birds(R.DUR)
for i in range(3): beep(fol, R.word("v1", ["Uno", "due", "tre"][i]), 520 + 130 * i, 0.12)
boing(fol, R.T_HIDE_S, 0.3); rustle(fol, R.T_HIDE_S + 0.5, 0.6, 0.5)
tt_ = R.T_HIDE_E0
while tt_ < R.T_HIDE_E1: tap(fol, tt_, 0.25); rustle(fol, tt_, 0.12, 0.08); tt_ += 0.3
rustle(fol, R.T_HIDE_E1 - 0.2, 0.6, 0.4)
for k in range(5): rustle(fol, R.T_LOOK1 + 0.4 + k * 0.62, 0.25, 0.28)
M.shimmer(fol, R.T_LOOK1 + 0.6, 0.4, (784, 988, 1175))
rustle(fol, R.T_FOUND1, 0.9, 0.7); M.pop(fol, R.T_FOUND1, 500, 0.6); M.shimmer(fol, R.T_FOUND1 + 0.05, 0.7)
for k in range(5): rustle(fol, R.T_LOOK2 + 0.4 + k * 0.66, 0.25, 0.28)
M.shimmer(fol, R.T_LOOK2 + 0.6, 0.4, (784, 988, 1175))
rustle(fol, R.T_FOUND2, 0.8, 0.6); M.pop(fol, R.T_FOUND2, 450, 0.5); M.shimmer(fol, R.T_FOUND2 + 0.05, 0.6)
for d_ in (0.0, 0.1, 0.25): boing(fol, R.T_JUMP + d_, 0.22)
M.thud(fol, R.T_BOOM, 0.9); rustle(fol, R.T_BOOM, 2.2, 1.0); M.shimmer(fol, R.T_BOOM + 0.05, 0.9, (1046.5, 1318.5, 1568, 2093, 2637))
for k in range(4): rustle(fol, R.T_MOUSE - 1.6 + k * 0.4, 0.2, 0.3)
rustle(fol, R.T_MOUSE, 1.2, 0.8); boing(fol, R.T_MOUSE, 0.35); M.shimmer(fol, R.T_MOUSE + 0.1, 0.9)
M.shimmer(fol, R.V["end"] + 0.9, 0.9, (1568, 2093, 2637, 3136, 3951))
dr = []
for k, t0, who, d in R.VOICES:
    sig = M.load_voice(f"audioK/{k}.wav"); M.put(voc, sig, t0, 0.95 if who != "narr" else 1.0); dr.append((t0, t0 + d + 0.15))
print("picco dB", M.finish(np.zeros(N), "/tmp/claude-0/prova/mix_nascondino.wav", voc, mus, fol, bird, dr, mg=0.12, fg=0.34))
