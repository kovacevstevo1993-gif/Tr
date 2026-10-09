import os, math; os.environ["SCENE"] = "sceneA"
import numpy as np, mixlib as M, engine as R, sceneA as S
N = int(S.DUR*M.SR); fol = np.zeros(N); voc = np.zeros(N)
mus = M.music(S.DUR); bird = M.birds(S.DUR)
for name, g in (("mouse", .9), ("chip", 1.0), ("spike", 1.05)):
    for te in R.walk_events(name): M.thud(fol, te, 0.5*g)
for kind, ix, iy, who, tp, tl, b in S.ITEMS:
    M.pop(fol, tp, 500, 0.55); M.whoosh(fol, tl-0.12, 0.9); M.tonk(fol, tl+R.FLY, 0.9); M.shimmer(fol, tl+R.FLY+0.02, 1.0)
for i, (t0, t1, a, b) in enumerate(S.SHOTS):                       # fruscio a ogni taglio di inquadratura
    if i: M.whoosh(fol, t0-0.04, 0.22, 0.14)
for j, f in enumerate((523, 659, 784, 988, 1175, 1319, 1568)): M.put(fol, M.tone(f, .8, 4), 4.9+j*0.17, 0.35)     # arpa dell'arcobaleno
for k in range(6): M.put(fol, M.bp(M.rng.normal(size=int(.5*M.SR)), 2000, 5000)*np.abs(np.sin(np.arange(int(.5*M.SR))/M.SR*50))*np.sin(np.pi*np.arange(int(.5*M.SR))/(.5*M.SR)), 11.5+k*0.28, 0.10)  # frullii
for k, (x, y, col, sz) in enumerate(S.FLOWERS):                    # bloop dei fiori
    M.bloop(fol, 19.1+math.hypot(x-810, y-1340)/1000+0.2, 380+ (k % 7)*90, 0.30)
M.put(fol, M.bp(M.rng.normal(size=int(.3*M.SR)), 800, 6000)*np.exp(-np.arange(int(.3*M.SR))/M.SR*14), 19.0, 0.8)
M.shimmer(fol, 19.0, 1.2, (1318.5, 1568, 2093, 2637, 3136))
dr = []
for k, t0, who, txt, d in S.VOICES:
    M.put(voc, M.load_voice(f"{S.AUDIO}/{k}.wav"), t0); dr.append((t0, t0+d+0.15))
print("picco dB", M.finish(np.zeros(N), "mixA.wav", voc, mus, fol, bird, dr))
