#!/usr/bin/env python3
"""Marionetta digitale (cutout rig): da UNA sola immagine di un personaggio ricava i pezzi (testa, busto, braccia, gambe, coda)
e li anima con le articolazioni -> movimento continuo e naturale (niente 'foto di passaggio').
Ogni pezzo: poligono nell'immagine sorgente, perno (articolazione), genitore, ordine di disegno.
Il busto/genitore copre le giunture; i pezzi hanno bordi morbidi.
    rig = Rig(CONF["volpe"]); img = rig.render(pose)   # pose = {pezzo: angolo_gradi, '_x','_y','_rot','_sq'...}
"""
import math, os
import numpy as np, cv2
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))


def _mask_poly(shape, poly, feather=3):
    m = Image.new("L", (shape[1], shape[0]), 0); ImageDraw.Draw(m).polygon([tuple(p) for p in poly], fill=255)
    m = np.asarray(m).astype(np.float32) / 255
    return cv2.GaussianBlur(m, (0, 0), feather) if feather else m


class Rig:
    def __init__(self, conf):
        self.c = conf
        src = np.asarray(Image.open(os.path.join(HERE, conf["img"])).convert("RGBA")).astype(np.float32)
        self.H, self.W = src.shape[:2]
        self.parts = {}
        for name, p in conf["parts"].items():
            m = _mask_poly(src.shape, p["poly"], p.get("feather", 2.5))
            lay = src.copy(); lay[..., 3] = lay[..., 3] * m
            ys, xs = np.nonzero(lay[..., 3] > 4)
            x0, x1, y0, y1 = max(0, xs.min() - 4), min(self.W, xs.max() + 5), max(0, ys.min() - 4), min(self.H, ys.max() + 5)
            sh = p.get("shift", (0, 0)); x0s, y0s = x0 + sh[0], y0 + sh[1]
            self.parts[name] = dict(img=lay[y0:y1, x0:x1].copy(), off=(x0s, y0s), pivot=p["pivot"], parent=p.get("parent"), z=p["z"])
        self.order = sorted(self.parts, key=lambda n: self.parts[n]["z"])

    def _world(self, name, pose, cache):
        """matrice 2x3 (sorgente -> mondo-sorgente) del pezzo, componendo i genitori"""
        if name in cache: return cache[name]
        p = self.parts[name]; a = math.radians(pose.get(name, 0.0)); px, py = p["pivot"]
        ca, sa = math.cos(a), math.sin(a)
        R = np.array([[ca, -sa, px - ca * px + sa * py], [sa, ca, py - sa * px - ca * py], [0, 0, 1]], np.float64)
        if name == self.c.get("root"):                                      # radice: estensione 'respiro' verticale del busto
            sy = pose.get("_breath", 1.0); S = np.array([[1, 0, 0], [0, sy, py - sy * py], [0, 0, 1]], np.float64); R = R @ S
        M = R if p["parent"] is None else self._world(p["parent"], pose, cache) @ R
        cache[name] = M; return M

    def render(self, pose, scale=1.0):
        """-> immagine RGBA (H*scale x W*scale) del personaggio in posa, con ancora ai piedi (anchor) fissa"""
        cache = {}
        g = pose.get("_rot", 0.0); ax, ay = self.c["anchor"]
        ga = math.radians(g); cg, sg = math.cos(ga), math.sin(ga)
        sq = pose.get("_sq", 1.0)
        G = np.array([[cg / math.sqrt(sq), -sg, 0], [sg / math.sqrt(sq) * 0, cg * sq, 0], [0, 0, 1]], np.float64)
        G = np.array([[cg, -sg, 0], [sg, cg, 0], [0, 0, 1]]) @ np.diag([1 / math.sqrt(sq), sq, 1.0])
        T1 = np.array([[1, 0, -ax], [0, 1, -ay], [0, 0, 1]], np.float64)
        T2 = np.array([[scale, 0, ax * scale], [0, scale, ay * scale], [0, 0, 1]], np.float64)
        GW = T2 @ G @ T1
        Wd, Hd = int(self.W * scale), int(self.H * scale)
        acc = np.zeros((Hd, Wd, 4), np.float32)
        for name in self.order:
            if pose.get("_hide_" + name): continue
            p = self.parts[name]; ox, oy = p["off"]
            M = GW @ self._world(name, pose, cache) @ np.array([[1, 0, ox], [0, 1, oy], [0, 0, 1]], np.float64)
            w = cv2.warpAffine(p["img"], M[:2], (Wd, Hd), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
            a = w[..., 3:4] / 255.0
            acc[..., :3] = w[..., :3] * a + acc[..., :3] * (1 - a)
            acc[..., 3:4] = a * 255 + acc[..., 3:4] * (1 - a)
        return acc.clip(0, 255).astype(np.uint8)


# ------------------------------------------------------------------ configurazioni dei personaggi
CONF = {
    "volpe": dict(
        img="assets/s/volpe_full.png", anchor=(520, 940), root="busto",
        parts={
            "coda": dict(poly=[(180, 500), (350, 590), (345, 640), (240, 640), (170, 560)], pivot=(458, 640), shift=(120, 25), parent="busto", z=0),
            "gamba_s": dict(poly=[(470, 630), (520, 640), (520, 700), (330, 860), (300, 960), (90, 960), (90, 840), (240, 760), (380, 650)], pivot=(470, 650), parent="busto", z=1),
            "gamba_d": dict(poly=[(530, 630), (650, 620), (720, 660), (800, 680), (920, 700), (920, 860), (740, 860), (700, 760), (540, 700)], pivot=(640, 650), parent="busto", z=1),
            "busto": dict(poly=[(355, 360), (760, 350), (765, 450), (660, 470), (650, 600), (660, 660), (600, 690), (450, 690), (440, 620), (455, 470), (350, 460)], pivot=(550, 650), z=2, feather=1.5),
            "braccio_s": dict(poly=[(100, 160), (270, 170), (300, 300), (348, 350), (348, 448), (320, 445), (210, 340), (100, 330)], pivot=(352, 415), parent="busto", z=5),
            "braccio_d": dict(poly=[(820, 170), (990, 180), (990, 320), (880, 330), (800, 440), (768, 445), (768, 360), (790, 340)], pivot=(765, 405), parent="busto", z=5),
            "testa": dict(poly=[(340, 30), (740, 30), (760, 260), (720, 360), (640, 400), (480, 410), (400, 360), (330, 260)], pivot=(560, 395), parent="busto", z=4, feather=2),
        }),
}
