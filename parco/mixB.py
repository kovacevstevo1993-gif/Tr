import os, math; os.environ["SCENE"] = "sceneB"
import numpy as np, mixlib as M, engine as R, sceneB as S
N = int(S.DUR*M.SR); fol = np.zeros(N); voc = np.zeros(N)
mus = M.music(S.DUR, bpm=135); bird = M.birds(S.DUR)
for name, g in (("mouse", .9), ("chip", 1.0)):
    for te in R.walk_events(name): M.thud(fol, te, 0.5*g)
def drum(buf, t, g=0.9):
    n = int(.35*SR) if False else int(.35*M.SR); tt = np.arange(n)/M.SR
    f = 150*np.exp(-9*tt)+85; ph = 2*np.pi*np.cumsum(f)/M.SR
    M.put(buf, np.sin(ph)*np.exp(-9*tt)+0.5*M.lp(M.rng.normal(size=n), 2500)*np.exp(-70*tt), t, g)
for th in S.BEATS: drum(fol, th)
M.pop(fol, S.TP, 500, 0.6); M.shimmer(fol, 3.35, 0.8); M.shimmer(fol, 5.4, 1.0); M.shimmer(fol, 9.2, 1.1, (1318.5, 1568, 2093, 2637, 3136))
for i, (t0, t1, a, b) in enumerate(S.SHOTS):
    if i: M.whoosh(fol, t0-0.04, 0.22, 0.14)
dr = []
for k, t0, who, txt, d in S.VOICES: M.put(voc, M.load_voice(f"{S.AUDIO}/{k}.wav"), t0); dr.append((t0, t0+d+0.15))
print("picco dB", M.finish(np.zeros(N), "mixB.wav", voc, mus, fol, bird, dr, mg=0.14, fg=0.34))
