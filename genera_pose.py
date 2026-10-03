#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera le pose del topolino con Pollinations (gen.pollinations.ai).

Ogni posa viene generata su sfondo verde piatto e poi ritagliata in un PNG
trasparente, pronto da sovrapporre al video. Output nella cartella `pose/`.

Uso:
    python genera_pose.py              # genera tutte le pose
    python genera_pose.py saluto gioia # solo alcune pose
"""

import io
import os
import sys
import time
import urllib.parse
from collections import deque

import requests
from PIL import Image

OUT_DIR = "pose"
SIZE = 768
MODEL = "flux"
SEED = 42  # stesso seed per tenere il personaggio il più coerente possibile
BASE_URL = "https://gen.pollinations.ai/image/"

# Descrizione fissa del personaggio: identica in tutte le pose
CHARACTER = (
    "cute original cartoon mouse character for toddlers, soft grey fur, big round "
    "light-grey ears with pink inside, big friendly eyes, small pink nose, "
    "blue dungarees over a yellow striped t-shirt, no gloves, bare paws, orange sneakers, "
    "flat vector illustration, thick clean outlines, bright colors, full body, centered"
)
BACKGROUND = (
    "isolated on a flat uniform bright neon chroma-key green background (#00FF00), "
    "no floor, no ground shadow, no gradient, no text"
)

POSE = {
    "saluto": "waving hello with one hand raised, big happy smile",
    "indica": "arm stretched out pointing to the right with the index finger, smiling, teaching",
    "conta": "holding up one open hand showing five fingers, cheerful, counting",
    "pollice": "giving a thumbs up with a big smile, proud",
    "gioia": "jumping in the air with both arms raised, celebrating, laughing",
    "pensa": "hand on chin, thinking, curious expression",
    "ciao": "waving goodbye with both hands, smiling warmly",
}


def scarica(prompt, seed, tentativi=4):
    url = BASE_URL + urllib.parse.quote(prompt)
    params = {"width": SIZE, "height": SIZE, "model": MODEL, "seed": seed, "nologo": "true"}
    for n in range(tentativi):
        try:
            r = requests.get(url, params=params, timeout=120)
            if r.status_code == 200 and r.headers.get("content-type", "").startswith("image"):
                return Image.open(io.BytesIO(r.content)).convert("RGB")
            print(f"    HTTP {r.status_code}, riprovo...")
        except requests.RequestException as e:
            print(f"    errore rete ({e}), riprovo...")
        time.sleep(2 ** (n + 1))
    raise RuntimeError("Pollinations non ha risposto")


def colore_sfondo(img):
    """Colore medio dei pixel di bordo (mediana per canale)."""
    w, h = img.size
    pix = img.load()
    bordo = [pix[x, 0] for x in range(w)] + [pix[x, h - 1] for x in range(w)]
    bordo += [pix[0, y] for y in range(h)] + [pix[w - 1, y] for y in range(h)]
    return tuple(sorted(p[c] for p in bordo)[len(bordo) // 2] for c in range(3))


def rimuovi_sfondo(img, tol=60):
    """Flood-fill dai bordi sui pixel simili al colore di sfondo campionato:
    il verde interno al personaggio resta intatto."""
    w, h = img.size
    pix = img.load()
    bg = colore_sfondo(img)

    def simile(p):
        return sum((p[c] - bg[c]) ** 2 for c in range(3)) ** 0.5 < tol

    sfondo = [[False] * w for _ in range(h)]
    coda = deque()
    for x in range(w):
        coda.extend([(x, 0), (x, h - 1)])
    for y in range(h):
        coda.extend([(0, y), (w - 1, y)])
    while coda:
        x, y = coda.popleft()
        if not (0 <= x < w and 0 <= y < h) or sfondo[y][x] or not simile(pix[x, y]):
            continue
        sfondo[y][x] = True
        coda.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

    out = img.convert("RGBA")
    op = out.load()
    for y in range(h):
        for x in range(w):
            if sfondo[y][x]:
                op[x, y] = (0, 0, 0, 0)
            else:
                # toglie la frangia verde sui bordi
                r, g, b, a = op[x, y]
                if g > r and g > b:
                    op[x, y] = (r, max(r, b), b, a)
    # ombra a terra: oliva scuro (r~g, blu più basso), colore assente nel personaggio
    for y in range(h):
        for x in range(w):
            r, g, b, a = op[x, y]
            if a and r < 170 and g >= r - 8 and b < g - 12:
                op[x, y] = (0, 0, 0, 0)
    togli_frammenti(out)
    bbox = out.getchannel("A").getbbox()
    return out.crop(bbox) if bbox else out


def togli_frammenti(img, min_px=2000):
    """Cancella le macchie isolate più piccole di min_px pixel (residui dell'ombra)."""
    w, h = img.size
    px = img.load()
    visto = [[False] * w for _ in range(h)]
    for y0 in range(h):
        for x0 in range(w):
            if visto[y0][x0] or not px[x0, y0][3]:
                continue
            comp, coda = [], deque([(x0, y0)])
            visto[y0][x0] = True
            while coda:
                x, y = coda.popleft()
                comp.append((x, y))
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < w and 0 <= ny < h and not visto[ny][nx] and px[nx, ny][3]:
                        visto[ny][nx] = True
                        coda.append((nx, ny))
            if len(comp) < min_px:
                for x, y in comp:
                    px[x, y] = (0, 0, 0, 0)


def main():
    scelte = sys.argv[1:] or list(POSE)
    os.makedirs(OUT_DIR, exist_ok=True)
    for nome in scelte:
        if nome not in POSE:
            print(f"Posa sconosciuta: {nome} (disponibili: {', '.join(POSE)})")
            continue
        print(f"🎨 {nome}...")
        prompt = f"{CHARACTER}, {POSE[nome]}, {BACKGROUND}"
        img = scarica(prompt, SEED)
        rimuovi_sfondo(img).save(os.path.join(OUT_DIR, f"{nome}.png"))
    print(f"✅ Pose salvate in '{OUT_DIR}/'")


if __name__ == "__main__":
    main()
