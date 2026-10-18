#!/usr/bin/env python3
"""Mix audio Short 'La festa a sorpresa' -> mix_festa.wav"""
import numpy as np
import mixlib as M
import short_festa as R

N = int(R.DUR * M.SR)
voc = np.zeros(N); fol = np.zeros(N); mus = M.music(R.DUR, bpm=118); bird = np.zeros(N)
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
M.whoosh(fol, 0.05, 0.5, 0.7); M.shimmer(fol, 0.1, 0.8)
noise_env(fol, R.T_OFF - 0.05, R.T_OFF + 0.15, 200, 3000, 0.4, 0.01, 0.1)                     # click luce
tt_ = R.T_ENTER0
while tt_ < R.T_ENTER1: tap(fol, tt_, 0.3); tt_ += 0.31
M.thud(fol, R.T_ON, 0.8); M.shimmer(fol, R.T_ON, 1.0, (1046.5, 1318.5, 1568, 2093, 2637))
for k in range(12): M.pop(fol, R.T_ON + 0.05 + k * 0.07, 600 + 80 * k, 0.25)
for i, tc in enumerate(R.T_CNT[:3]): beep(fol, tc, 660 + 110 * i, 0.25)
noise_env(fol, R.T_PUFF, R.T_PUFF + 0.8, 500, 4000, 0.35, 0.05, 0.4)
M.bloop(fol, R.T_PUFF + 1.0, 300, 0.3); M.bloop(fol, R.T_PUFF + 1.2, 240, 0.3)
noise_env(fol, R.T_BLOW, R.T_SPLAT + 0.1, 200, 5000, 0.8, 0.1, 0.2, lambda u: 0.5 + 0.5 * u)
M.thud(fol, R.T_SPLAT, 0.8)
for k in range(10): M.bloop(fol, R.T_SPLAT + 0.02 + k * 0.05, 250 + 60 * k, 0.35)
M.pop(fol, R.T_GIFT, 400, 0.5); M.shimmer(fol, R.T_GIFT, 0.8)
for k in range(3): boing(fol, R.T_BALL + k * 0.15, 0.2)
M.shimmer(fol, R.T_DISCO, 1.0, (1046.5, 1318.5, 1568, 2093, 2637))
t = R.T_DISCO
while t < R.DUR - 0.3: M.thud(fol, t, 0.25); t += 60 / 118
M.shimmer(fol, R.V["end"] + 0.9, 0.9, (1568, 2093, 2637, 3136, 3951))
dr = []
for k, t0, who, d in R.VOICES:
    sig = M.load_voice(f"audioL/{k}.wav"); M.put(voc, sig, t0, 0.95 if who != "narr" else 1.0); dr.append((t0, t0 + d + 0.15))
print("picco dB", M.finish(np.zeros(N), "/tmp/claude-0/prova/mix_festa.wav", voc, mus, fol, bird, dr, mg=0.12, fg=0.34))
