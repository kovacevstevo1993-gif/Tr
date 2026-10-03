#!/usr/bin/env python3
"""Genera nuove pose di un personaggio PARTENDO DALLA SUA IMMAGINE (image-to-image) con Pollinations.

Uso:
    python3 pose_pollinations.py topo                 # tutte le pose del topolino
    python3 pose_pollinations.py topo cammina_sx      # una sola posa
    python3 pose_pollinations.py chip | spike

Output: assets/pose/<personaggio>_<posa>.png (RGBA, sfondo trasparente, 768x1376)
        assets/pose/raw/<personaggio>_<posa>.jpg (originale su verde, per ricontrollare il ritaglio)
Il riferimento è il ritaglio già in assets/ (stesso volto, pelo, vestiti, stile 3D).
La chiave Pollinations è iniettata dal proxy della sessione: non serve scriverla qui.
"""
import base64, io, os, sys, time
import numpy as np
import requests
from PIL import Image
from scipy.ndimage import binary_dilation, label

URL = "https://gen.pollinations.ai/v1/images/edits"
MODEL = "klein"          # flux.2-klein: 0.005 pollen a immagine
SIZE = (768, 1376)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "pose")

RIFERIMENTI = {
    "topo": "assets/topo/neutro_full.png",
    "chip": "assets/s/chip.png",
    "spike": "assets/s/spike.png",
}

POSE = {
    "cammina_sx": "walking, left foot stepping forward, arms swinging naturally, mid-step, looking forward",
    "cammina_dx": "walking, right foot stepping forward, arms swinging naturally, mid-step, looking forward",
    "china": "bending down and reaching to the ground with one hand to pick something up, knees bent, looking down",
    "tiene": "standing and holding both hands together in front of the belly at belly height, as if carrying a small object, smiling",
    "lancia": "throwing: one arm pulled far back over the shoulder about to throw, other arm forward for balance, determined smile",
    "saluta": "standing and waving hello with one hand raised high, big smile",
    "sorpreso": "surprised: mouth open in a round 'O', eyes wide, both hands raised near the cheeks",
    "ride": "laughing happily with both arms raised up high, eyes closed with joy, mouth wide open",
}


def su_verde(path):
    im = Image.open(path).convert("RGBA")
    im.putalpha(Image.fromarray(np.where(np.array(im)[..., 3] > 40, 255, 0).astype("uint8")))  # alpha netto
    bg = Image.new("RGBA", im.size, (0, 255, 0, 255))
    bg.alpha_composite(im)
    return bg.convert("RGB").resize(SIZE)


def chiedi(ref_png, posa, tentativi=4):
    buf = io.BytesIO()
    su_verde(ref_png).save(buf, "PNG")
    prompt = (
        "Use the attached character exactly as it is (same face, fur, clothes, colors, proportions, "
        "3D Pixar style, same camera angle and same size in the frame). Only change the pose: " + posa +
        ". Plain flat pure green #00FF00 background, no ground, no shadow, no text, no watermark, "
        "full body visible, feet near the bottom of the frame."
    )
    for n in range(tentativi):
        try:
            r = requests.post(
                URL,
                data={"model": MODEL, "size": f"{SIZE[0]}x{SIZE[1]}", "prompt": prompt},
                files={"image": ("ref.png", buf.getvalue(), "image/png")},
                timeout=240,
            )
            if r.status_code == 200:
                b = r.json()["data"][0]["b64_json"]
                return Image.open(io.BytesIO(base64.b64decode(b))).convert("RGB").resize(SIZE)
            print(f"   HTTP {r.status_code}: {r.text[:120]}")
        except requests.RequestException as e:
            print("   errore rete:", e)
        time.sleep(2 ** (n + 1))
    raise RuntimeError("Pollinations non ha risposto")


def ritaglia(img):
    """Chiave verde morbida + despill. Tiene solo la figura più grande (via ombre e macchie)."""
    a = np.asarray(img).astype(float)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    verde = g - np.maximum(r, b)                      # quanto "verde puro" è il pixel
    alpha = np.clip(1 - (verde - 40) / 120, 0, 1)     # 0 su verde pieno, 1 sul personaggio
    alpha[verde > 160] = 0
    solido = alpha > 0.5
    lab, n = label(solido)
    if n:
        dim = np.bincount(lab.ravel())[1:]
        solido = lab == (1 + int(np.argmax(dim)))
        alpha = np.where(binary_dilation(solido, iterations=4), alpha, 0)
    # despill: dove il verde sborda sul bordo lo riporta al massimo tra rosso e blu
    sp = g > np.maximum(r, b)
    a[..., 1] = np.where(sp, np.maximum(r, b), g)
    out = np.dstack([a, alpha * 255]).astype("uint8")
    im = Image.fromarray(out, "RGBA")
    return im


def main():
    chi = sys.argv[1] if len(sys.argv) > 1 else "topo"
    if chi not in RIFERIMENTI:
        sys.exit(f"Personaggio sconosciuto: {chi} ({', '.join(RIFERIMENTI)})")
    scelte = sys.argv[2:] or list(POSE)
    os.makedirs(os.path.join(OUT, "raw"), exist_ok=True)
    ref = os.path.join(HERE, RIFERIMENTI[chi])
    for nome in scelte:
        print(f"🎨 {chi} / {nome}")
        raw = chiedi(ref, POSE[nome])
        raw.save(os.path.join(OUT, "raw", f"{chi}_{nome}.jpg"), quality=93)
        ritaglia(raw).save(os.path.join(OUT, f"{chi}_{nome}.png"))
    print("✅ fatto →", OUT)


if __name__ == "__main__":
    main()
