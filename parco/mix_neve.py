#!/usr/bin/env python3
"""Mix audio Short 'Il pupazzo di neve': voci italiane + musica + effetti sincronizzati -> mix_neve.wav"""
import numpy as np
import mixlib as M
import short_neve as R

N = int(R.DUR * M.SR)
voc = np.zeros(N); fol = np.zeros(N); mus = M.music(R.DUR, bpm=104); bird = np.zeros(N)
rng = np.random.default_rng(8)

def noise_env(buf, t0, t1, lo, hi, g, a=0.3, r=0.4, shape=None):
    n = int((t1 - t0) * M.SR); x = M.bp(rng.normal(size=n), lo, hi); i = np.arange(n) / M.SR
    env = np.clip(np.minimum(1, np.minimum(i / a, (t1 - t0 - i) / r)), 0, 1)
    if shape is not None: env = env * shape(i / (t1 - t0))
    M.put(buf, x * env, t0, g)
def boing(buf, t, g=0.5):
    n = int(.28 * M.SR); tt = np.arange(n) / M.SR; f = 260 + 2100 * tt - 3600 * tt ** 2
    M.put(buf, np.sin(2 * np.pi * np.cumsum(f) / M.SR) * np.exp(-9 * tt), t, g)
def crunch(buf, t, g=0.3):                                   # passo / colpo sulla neve
    n = int(.12 * M.SR); M.put(buf, M.bp(rng.normal(size=n), 900, 5000) * np.exp(-np.arange(n) / M.SR * 30) * (0.6 + 0.4 * rng.random(n)), t, g)
def bells(buf, t0, t1, g=0.10, step=0.25):                   # sonagli della slitta
    t = t0
    while t < t1:
        for f in (2350, 3120, 4180):
            tt = np.arange(int(.18 * M.SR)) / M.SR; M.put(buf, np.sin(2 * np.pi * f * tt) * np.exp(-22 * tt), t + rng.uniform(0, 0.03), g * 0.6)
        t += step
def toot(buf, t, g=0.35, f0=420, up=1.5, dur=0.55):
    n = int(dur * M.SR); tt = np.arange(n) / M.SR; f = f0 * (1 + (up - 1) * np.minimum(1, tt / 0.12)) * (1 + 0.02 * np.sin(2 * np.pi * 22 * tt))
    ph = 2 * np.pi * np.cumsum(f) / M.SR; sig = (np.sin(ph) + 0.5 * np.sin(2 * ph) + 0.3 * np.sin(3 * ph)) * np.minimum(1, tt / 0.03) * np.exp(-3.5 * np.maximum(0, tt - dur * 0.45))
    M.put(buf, M.lp(sig, 3500), t, g)
def rolling(buf, t0, t1, g, grow=True):                      # palla che rotola (rombo morbido che cresce)
    n = int((t1 - t0) * M.SR); i = np.arange(n) / n
    x = M.lp(rng.normal(size=n), 260) * (0.3 + 0.7 * i if grow else 1) * np.minimum(1, np.minimum(i * n / M.SR / 0.2, (1 - i) * n / M.SR / 0.3))
    M.put(buf, x * 3, t0, g)

# vento leggero tutto il tempo
for k in range(int(R.DUR / 5.0) + 1):
    t0 = k * 5.0; noise_env(fol, t0, min(R.DUR, t0 + 5.4), 300, 1800, 0.05, 1.5, 1.8)
M.whoosh(fol, 0.05, 0.5, 0.7); M.shimmer(fol, 0.1, 0.8, (1568, 2093, 2637, 3136, 3951))          # hook
# S1: palla che rotola, passi
rolling(fol, R.T_R0, R.T_R1, 0.5); tt_ = R.T_R0
while tt_ < R.T_R1: crunch(fol, tt_, 0.22); tt_ += 0.30
M.shimmer(fol, R.V["t1"], 0.4)
boing(fol, R.T_THROW - 0.1, 0.25); M.whoosh(fol, R.T_THROW, 0.35, 0.6); M.thud(fol, R.T_HEAD, 0.55); crunch(fol, R.T_HEAD, 0.5); M.shimmer(fol, R.T_HEAD + 0.15, 0.4)
tt_ = R.T_E0
while tt_ < R.T_E1: crunch(fol, tt_, 0.2); tt_ += 0.15
toot(fol, R.T_CAR0 - 0.2, 0.25); M.whoosh(fol, R.T_CAR0, 0.3, 0.45); M.pop(fol, R.T_NOSE, 600, 0.6); M.shimmer(fol, R.T_NOSE + 0.05, 0.6)
noise_env(fol, R.T_SNZ - 0.05, R.T_SNZ + 0.45, 1500, 7000, 0.55, 0.02, 0.3)                       # starnuto
M.thud(fol, R.T_FALL + 0.4, 0.45); rolling(fol, R.T_FALL + 0.45, R.T_FALL + 2.2, 0.45); M.tonk(fol, R.T_FALL + 0.1, 0.25)
# S2: discesa
for tw in R.WIPES: M.whoosh(fol, tw - 0.6, 0.8, 1.2); M.shimmer(fol, tw - 0.1, 0.6, (784, 1046.5, 1318.5, 1568, 2093))
noise_env(fol, R.T_W1, R.T_W2, 400, 3500, 0.32, 0.4, 0.6)                                         # neve sotto i pattini
bells(fol, R.T_W1, R.T_W2, 0.11)
rolling(fol, R.T_W1, R.T_W2, 0.35)
boing(fol, R.T_BUMP - 0.05, 0.3); M.thud(fol, R.T_BUMP + 0.65, 0.5); crunch(fol, R.T_BUMP + 0.65, 0.5)
M.shimmer(fol, R.T_BIG, 0.5); toot(fol, R.V["e2"] - 0.15, 0.22, 470, 1.4, 0.4)
# S3: villaggio
rolling(fol, R.T_W2 - 0.3, R.T_STOP + 0.2, 0.5, False); M.thud(fol, R.T_STOP, 0.8); crunch(fol, R.T_STOP, 0.6)
boing(fol, R.T_THROW2 - 0.1, 0.25); M.whoosh(fol, R.T_THROW2, 0.35, 0.7); M.thud(fol, R.T_HEAD2, 0.55); crunch(fol, R.T_HEAD2, 0.4)
M.whoosh(fol, R.T_HAT0, 0.3, 0.6); M.tonk(fol, R.T_HAT1, 0.35); M.shimmer(fol, R.T_HAT1 + 0.05, 0.5)
toot(fol, R.T_CAR3 - 0.2, 0.22); M.pop(fol, R.T_NOSE3, 600, 0.6)
M.shimmer(fol, R.T_FACE, 0.9, (1046.5, 1318.5, 1568, 2093, 2637)); M.shimmer(fol, R.T_FACE + 0.4, 0.6)
M.bloop(fol, R.T_WINK, 1200, 0.35); M.shimmer(fol, R.T_WINK + 0.05, 0.7, (2093, 2637, 3136))
bells(fol, R.T_DANCE, R.V["end"] + 0.5, 0.07, 0.5)
M.shimmer(fol, R.V["end"] + 0.9, 0.9, (1568, 2093, 2637, 3136, 3951))
dr = []
for k, t0, who, txt, d in R.VOICES:
    sig = M.load_voice(f"audioI/{k}.wav"); M.put(voc, sig, t0, 0.95 if who != "narr" else 1.0); dr.append((t0, t0 + d + 0.15))
print("picco dB", M.finish(np.zeros(N), "mix_neve.wav", voc, mus, fol, bird, dr, mg=0.12, fg=0.36))
