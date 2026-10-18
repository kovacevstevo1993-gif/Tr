#!/usr/bin/env python3
"""Attori con TANTE pose vere (pose_free.py) + transizioni morph + 'corpo vivo' (testa, respiro, peso) -> movimento naturale.
Uso: a = Attore("volpe", [(t0, posa, durata_transizione), ...], salti=[(t0, durata, altezza)], sq=[(t0,)])
     a.draw(img, t, x, y_piedi, scala, ...)
"""
import math
import numpy as np, cv2
from PIL import Image
import morph as MO
from short_razzo import lerp, clamp, ease, alive_warp


class Attore:
    def __init__(self, name, ev, jumps=(), talk=None, height=900):
        self.n = name; self.ev = sorted(ev, key=lambda e: e[0]); self.jumps = list(jumps); self.talk = talk or (lambda t: 0.0); self.h = height

    def pairs(self):
        s = set()
        for a, b in zip(self.ev, self.ev[1:]):
            if a[1] != b[1]: s.add((self.n, a[1], b[1]))
        return s

    def state(self, t):
        idx = 0
        for i, e in enumerate(self.ev):
            if e[0] <= t: idx = i
        t0, pose, dur = self.ev[idx]; prev = self.ev[idx - 1][1] if idx > 0 else pose
        if prev != pose and t < t0 + dur: return prev, pose, (t - t0) / dur
        return pose, pose, 1.0

    def canvas(self, t):
        A, B, u = self.state(t)
        if A == B: return MO.aligned(self.n, A), A, B
        fr = MO.transition(self.n, A, B); idx = int(ease(u) * (MO.K + 1))
        if idx <= 0: return MO.aligned(self.n, A), A, B
        if idx >= MO.K + 1: return MO.aligned(self.n, B), A, B
        return fr[idx - 1], A, B

    def hop(self, t):
        for (j0, jd, hg) in self.jumps:
            if j0 <= t < j0 + jd:
                p = (t - j0) / jd; return 4 * p * (1 - p) * hg, p
        return 0.0, None

    def draw(self, img, t, x, y, scale=1.0, rot=0.0, flip=False, extra_hop=0.0, rim=((255, 190, 130), 0.45), tint=(1.0, 1.0, 1.0), shadow=True, alpha=1.0):
        cv, A, B = self.canvas(t)
        hop, jp = self.hop(t); hop += extra_hop
        sq = 1.0
        if jp is not None:
            if jp < 0.12: sq = 1 - 0.08 * math.sin(math.pi * jp / 0.12)
            elif jp > 0.88: sq = 1 - 0.10 * math.sin(math.pi * (jp - 0.88) / 0.12)
            else: sq = 1 + 0.05 * math.sin(math.pi * (jp - 0.12) / 0.76)
        tk = self.talk(t); ph = len(self.n) * 1.3
        head = 3.0 * math.sin(t * 1.4 + ph) + 1.5 * math.sin(t * 3.1 + ph) + 6 * tk * math.sin(t * 12 + ph)
        sway = 5 * math.sin(t * 1.2 + ph); breath = 0.010 * math.sin(t * 2.5 + ph)
        lean = -14 * math.sin(math.pi * jp) if jp is not None else 0.0
        f = scale * self.h / MO.TARGET_H.get(self.n, 900)
        nw, nh = max(2, int(MO.CW * f / math.sqrt(sq))), max(2, int(MO.CH * f * sq))
        small = cv2.resize(np.ascontiguousarray(cv), (nw, nh), interpolation=cv2.INTER_AREA if f < 1 else cv2.INTER_CUBIC)
        small = alive_warp(small, t, self.n, head, sway * f, breath, lean * f)
        if flip: small = small[:, ::-1].copy()
        im = Image.fromarray(small, "RGBA")
        if rot: im = im.rotate(rot, resample=Image.BILINEAR, center=(MO.AX * nw / MO.CW, MO.AY * nh / MO.CH))
        px, py = x - MO.AX * nw / MO.CW, y - hop - MO.AY * nh / MO.CH
        if shadow:
            from PIL import ImageDraw, ImageFilter
            sw = 230 * f * clamp(1 - hop / 700, 0.35, 1) + 30
            sh = Image.new("RGBA", (int(sw * 2.2), 90), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([10, 15, sw * 2.2 - 10, 75], fill=(20, 10, 30, int(120 * clamp(1 - hop / 800, 0.3, 1) * alpha)))
            sh = sh.filter(ImageFilter.GaussianBlur(10)); img.paste(sh, (int(x - sh.width / 2), int(y - 45)), sh)
        a = np.asarray(im).astype(np.float32); al = a[..., 3] / 255.0
        Lb = cv2.GaussianBlur(al, (0, 0), max(3, 7 * f)); Ls = cv2.warpAffine(Lb, np.float32([[1, 0, 8 * f], [0, 1, 7 * f]]), (im.width, im.height))
        r = np.clip(al * (1 - Ls * 1.25), 0, 1) ** 1.3
        a[..., :3] = np.clip(a[..., :3] * np.array(tint) + r[..., None] * np.array(rim[0]) * rim[1], 0, 255)
        gy = np.linspace(0, 1, im.height, dtype=np.float32)[:, None, None]; a[..., :3] *= (1.03 - 0.10 * gy)
        a[..., 3] *= alpha
        out = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGBA")
        img.paste(out, (int(px), int(py)), out)
        return py
