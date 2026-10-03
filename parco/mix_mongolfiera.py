#!/usr/bin/env python3
"""Mix audio Short 'La mongolfiera dei quattro amici': voci italiane + musica + effetti sincronizzati -> mix_mongolfiera.wav"""
import numpy as np
import mixlib as M
import short_mongolfiera as R

N = int(R.DUR * M.SR)
voc = np.zeros(N); fol = np.zeros(N); mus = M.music(R.DUR, bpm=100); bird = M.birds(R.DUR)
rng = np.random.default_rng(8)

def boing(buf, t, g=0.5):
    n = int(.28 * M.SR); tt = np.arange(n) / M.SR; f = 260 + 700 * tt * 3 - 900 * tt ** 2 * 4
    M.put(buf, np.sin(2 * np.pi * np.cumsum(f) / M.SR) * np.exp(-9 * tt), t, g)
def noise_env(buf, t0, t1, lo, hi, g, a=0.3, r=0.4, shape=None):
    n = int((t1 - t0) * M.SR); x = M.bp(rng.normal(size=n), lo, hi); i = np.arange(n) / M.SR
    env = np.clip(np.minimum(1, np.minimum(i / a, (t1 - t0 - i) / r)), 0, 1)
    if shape is not None: env = env * shape(i / (t1 - t0))
    M.put(buf, x * env, t0, g)
def toot(buf, t, g=0.35, f0=420, up=1.5, dur=0.55):
    n = int(dur * M.SR); tt = np.arange(n) / M.SR; f = f0 * (1 + (up - 1) * np.minimum(1, tt / 0.12)) * (1 + 0.02 * np.sin(2 * np.pi * 22 * tt))
    ph = 2 * np.pi * np.cumsum(f) / M.SR; sig = (np.sin(ph) + 0.5 * np.sin(2 * ph) + 0.3 * np.sin(3 * ph)) * np.minimum(1, tt / 0.03) * np.exp(-3.5 * np.maximum(0, tt - dur * 0.45))
    M.put(buf, M.lp(sig, 3500), t, g)
def gullcry(buf, t, g=0.18):
    n = int(.45 * M.SR); tt = np.arange(n) / M.SR; f = 1500 + 500 * np.sin(2 * np.pi * 3 * tt) - 700 * tt
    M.put(buf, np.sin(2 * np.pi * np.cumsum(f) / M.SR) * np.sin(np.pi * tt / 0.45) ** 1.5, t, g)
def rise(buf, t, g=0.5, dur=0.9, f0=300, f1=1400):
    n = int(dur * M.SR); tt = np.arange(n) / M.SR; f = f0 + (f1 - f0) * (tt / dur) ** 1.4
    M.put(buf, np.sin(2 * np.pi * np.cumsum(f) / M.SR) * np.sin(np.pi * tt / dur) ** 1.2, t, g)
def fall(buf, t, g=0.4, dur=1.4, f0=1800, f1=250):
    n = int(dur * M.SR); tt = np.arange(n) / M.SR; f = f0 + (f1 - f0) * (tt / dur) ** 0.8
    M.put(buf, np.sin(2 * np.pi * np.cumsum(f) / M.SR) * np.sin(np.pi * tt / dur) ** 0.8, t, g)
def creak(buf, t, g=0.18):
    n = int(.22 * M.SR); tt = np.arange(n) / M.SR; f = 180 + 60 * np.sin(2 * np.pi * 14 * tt)
    M.put(buf, M.lp(np.sign(np.sin(2 * np.pi * np.cumsum(f) / M.SR)) * 0.4 + rng.normal(size=n) * 0.2, 1800) * np.exp(-9 * tt), t, g)

# vento di quota (basso, costante) + onde nella scena mare
for k in range(int(R.DUR / 5.0) + 1):
    t0 = k * 5.0; noise_env(fol, t0, min(R.DUR, t0 + 5.4), 250, 1600, 0.06, 1.5, 1.8)
for k in range(int((R.DUR - R.T_W2) / 3.0) + 1):
    t0 = R.T_W2 + 0.4 + k * 3.0
    if t0 < R.T_W3: noise_env(fol, t0, min(R.T_W3, t0 + 3.2), 500, 3600, 0.10, 1.0, 1.4)
# uccellini, gabbiani
for t0 in (R.V["c1"] + 0.3, R.V["n3"] + 0.8): gullcry(fol, t0, 0.14)
for t0 in (R.T_DIP + 2.0, R.T_CLIMB0 + 0.5, R.T_BLOW0 + 0.6): gullcry(fol, t0, 0.16); gullcry(fol, t0 + 1.4, 0.12)
M.whoosh(fol, 0.05, 0.5, 0.7)                                               # hook
# gonfiaggio: soffi dell'elefantino
t = 0.5
while t < R.T_FULL:
    noise_env(fol, t, t + 0.34, 600, 3200, 0.16 + 0.1 * (t / R.T_FULL), 0.05, 0.25); t += 0.46
M.shimmer(fol, R.T_FULL - 0.1, 0.5, (659.25, 783.99, 987.77, 1318.5, 1568))
# salti nel cesto
for n_, tb in R.T_BRD.items(): boing(fol, tb - 0.2, 0.28); M.thud(fol, tb + 0.55, 0.7); creak(fol, tb + 0.6, 0.25)
# decollo: fiamma del bruciatore, corde, nuvole
noise_env(fol, R.T_LIFT - 0.3, R.T_LIFT + 1.6, 200, 2000, 0.30, 0.15, 0.6)
rise(fol, R.T_LIFT, 0.35, 1.4, 260, 1100); creak(fol, R.T_LIFT + 0.1, 0.3); creak(fol, R.T_LIFT + 0.4, 0.25)
for tw in (R.T_W1, R.T_W3): M.whoosh(fol, tw - 0.7, 0.7, 1.2); M.shimmer(fol, tw - 0.1, 0.9, (784, 1046.5, 1318.5, 1568, 2093))
noise_env(fol, R.T_W3 - 1.0, R.T_W3 + 0.8, 200, 1800, 0.25, 0.4, 0.5)
M.shimmer(fol, R.V["c1"], 0.5, (1046.5, 1318.5, 1568, 2093, 2637))
# Spike salta -> Pop -> aria che esce
boing(fol, R.T_POP - 0.55, 0.35)
M.pop(fol, R.T_POP, 700, 0.9); M.thud(fol, R.T_POP, 0.5)
noise_env(fol, R.T_POP, R.T_PATCH, 3000, 10000, 0.20, 0.05, 1.5, lambda u: (1 - u) ** 0.6)
for j in range(8): M.bloop(fol, R.T_POP + 0.2 + j * 0.2, 500 + 90 * j, 0.15)
M.tonk(fol, R.V["s1"] + 0.1, 0.0)
# caduta
fall(fol, R.T_POP + 1.0, 0.30, 2.2, 1700, 260)
noise_env(fol, R.T_POP + 0.8, R.T_W2 + 0.5, 300, 4000, 0.22, 0.5, 0.4, lambda u: u ** 1.4)
M.whoosh(fol, R.T_W2 - 0.7, 0.8, 1.2)
# acqua: tuffo del cesto
M.thud(fol, R.T_DIP, 0.9); noise_env(fol, R.T_DIP - 0.1, R.T_DIP + 1.2, 500, 9000, 0.7, 0.03, 1.0)
for j in range(14): M.bloop(fol, R.T_DIP + 0.2 + j * 0.08, rng.uniform(400, 900), 0.22)
# Chip sale: passi sulla corda
tt_ = R.T_CLIMB0
while tt_ < R.T_CLIMB1: creak(fol, tt_, 0.2); M.thud(fol, tt_ + 0.08, 0.18); tt_ += 0.34
# toppa
M.pop(fol, R.T_PATCH, 420, 0.7); M.thud(fol, R.T_PATCH + 0.05, 0.6); M.shimmer(fol, R.T_PATCH + 0.05, 0.8)
# elefantino: trombetta e soffio forte
toot(fol, R.V["e1"] - 0.1, 0.34, 430, 1.5, 0.55)
noise_env(fol, R.T_BLOW0 - 0.1, R.T_BLOW1, 400, 4200, 0.55, 0.2, 0.5, lambda u: 0.6 + 0.4 * np.sin(u * 30))
rise(fol, R.T_BLOW0 + 0.2, 0.4, 2.4, 200, 900)
M.shimmer(fol, R.T_UP + 1.6, 0.8, (784, 987.77, 1318.5, 1568, 2093))
# tramonto
M.shimmer(fol, R.V["n7"], 0.7, (1046.5, 1318.5, 1568, 2093, 2637))
for j in range(10): M.shimmer(fol, R.V["n7"] + 0.5 + j * 0.6, 0.12, (1568, 2093, 2637))
boing(fol, R.V["s2"] - 0.1, 0.3)
M.shimmer(fol, R.V["end"] + 0.9, 0.9, (1568, 2093, 2637, 3136, 3951))
dr = []
for k, t0, who, txt, d in R.VOICES:
    sig = M.load_voice(f"audioH/{k}.wav"); M.put(voc, sig, t0, 0.95 if who != "narr" else 1.0); dr.append((t0, t0 + d + 0.15))
print("picco dB", M.finish(np.zeros(N), "mix_mongolfiera.wav", voc, mus, fol, bird, dr, mg=0.12, fg=0.36))
