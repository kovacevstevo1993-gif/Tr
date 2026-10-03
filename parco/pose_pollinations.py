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
from PIL import Image, ImageOps
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
    "ele": "assets/s/ele.png",
}

POSE = {
    # Passo con braccio opposto alla gamba avanti. cammina_sx NON si genera: è lo specchio di cammina_dx
    # (il personaggio è simmetrico), così i due passi sono sempre alternati e sincronizzati.
    "cammina_dx": "classic cartoon walk cycle CONTACT pose, front view, opposite arm and leg: the character's right leg steps far forward toward the camera, the character's left arm swings forward, the character's right arm swings backward, left leg stays behind with heel lifted, exaggerated clear walking pose",
    "china": "bending down and reaching to the ground with one hand to pick something up, knees bent, looking down",
    "tiene": "standing and holding both hands together in front of the belly at belly height, as if carrying a small object, smiling",
    "lancia": "throwing: one arm pulled far back over the shoulder about to throw, other arm forward for balance, determined smile",
    "saluta": "standing and waving hello with one hand raised high, big smile",
    "sorpreso": "surprised: mouth open in a round 'O', eyes wide, both hands raised near the cheeks",
    "neutro": "standing relaxed facing the camera, both arms hanging naturally at the sides, legs together, gentle smile",
    "corre": "running toward the camera, leaning forward, arms pumping, one knee high, big excited smile, mid-air",
    "sbircia": "sneaking forward on tiptoes, leaning in with curious wide eyes, one hand raised to the mouth in a 'shh' gesture",
    "indica": "excitedly pointing with one arm stretched out to the right, other hand on the hip, big open smile",
    "mangia": "holding a round chocolate chip cookie in both hands near the mouth, taking a bite, eyes closed with delight, happy chewing",
    "balla": "dancing happily, body leaning to the left, one arm up and one arm down, one leg lifted, joyful open smile",
    "salto": "jumping high in the air with arms and legs spread wide, joyful, mouth wide open, laughing",
    "afferra": "leaping forward with both arms stretched out in front trying to catch something, mouth open in excitement",
    "guarda_su": "looking up with an amazed open mouth and wide eyes, one hand raised pointing up",
    # --- pose con OGGETTO GIÀ NELLE MANI (gesti coerenti con gli oggetti) ---
    "orecchio": "head tilted to one side, leaning the body sideways, ONLY ONE hand raised and cupped behind one ear to listen, the other arm hanging down relaxed, eyes wide and curious, lips slightly parted",
    "riceve": "both arms stretched far out forward toward the viewer with elbows almost straight, hands wide open with palms facing up, leaning forward slightly, ready to catch something that is falling from above, looking up with a happy excited open mouth",
    "tiene_biscotto": "holding one round chocolate chip cookie with both hands in front of the chest, looking down at the cookie with delighted wide eyes and a big smile",
    "mangia2": "chewing happily with puffed cheeks and eyes closed with joy, holding a half-eaten chocolate chip cookie with a bite missing in both hands at chest height",
    "saluta2": "waving goodbye with both arms raised high and open hands, big warm smile, slightly leaning to one side",
    "indica_giu": "smiling at the camera and pointing downward with one index finger toward the ground in front, other hand on the hip",
    "parla_a": "exactly the same pose as the reference, only the mouth is wide open as if saying 'ah', nothing else changes",
    "parla_o": "exactly the same pose as the reference, only the mouth is a small round 'o' shape as if saying 'oh', nothing else changes",
    "tiene_mela": "holding one big shiny red apple with both hands in front of the chest, looking down at the apple with delighted wide eyes and a big smile",
    "mangia_mela": "holding a shiny red apple with both hands up near the mouth and taking a big bite, eyes closed with delight",
    "mangia_mela2": "chewing happily with puffed cheeks and eyes closed with joy, holding a red apple with a bite missing in both hands at chest height",
    "ride": "laughing happily with both arms raised up high, eyes closed with joy, mouth wide open",
    # --- storia 'castello di sabbia' ---
    "passa_dx": "classic cartoon walk cycle PASSING pose, front view: the character's left leg is lifted with the knee bent passing forward, the right leg is straight and supports the body, arms hanging close to the body swinging slightly, relaxed happy walking, small bounce",
    "batte_sabbia": "kneeling on both knees leaning forward with both hands pressed flat in front of the knees as if patting something on the ground, head up looking forward at the camera with a happy concentrated smile, ONLY the character, no sand, no ground, no objects",
    "triste": "sad: head tilted down, shoulders slumped, both arms hanging down, eyebrows raised in the middle, mouth turned down, big sad eyes",
    "fuggi": "jumping backward in fright, both arms thrown up in the air, eyes wide, mouth wide open in surprise, one leg lifted",
    "riempie": "leaning forward and bending down with the TRUNK pointing straight down, one hand on the knee, curious happy eyes looking down at the trunk tip, NO water, NO sand, NO ground, only the character",
    "spruzza": "head tilted back, the TRUNK RAISED STRAIGHT UP high above the head like a trumpet with the trunk tip open, both arms raised up in joy, eyes closed, big open smile, NO water, NO fountain, only the character",
    "spruzza_giu": "standing and the TRUNK stretched out forward and pointing down in front of the body, proud smile looking at the trunk tip, one hand on the hip, NO water, NO sand, NO ground, only the character",
    "tiene_bandiera": "holding a small wooden pole upright with both hands in front of the chest, excited wide smile, looking up",
}


def su_verde(path):
    """Ritaglio del personaggio su verde #00FF00, in 768x1376 SENZA stirarlo (proporzioni mantenute,
    centrato in orizzontale e appoggiato in basso)."""
    im = Image.open(path).convert("RGBA")
    a = np.array(im)
    a[..., 3] = np.where(a[..., 3] > 40, 255, 0)
    im = Image.fromarray(a, "RGBA")
    k = min(SIZE[0] * 0.9 / im.width, SIZE[1] * 0.9 / im.height)
    im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    bg = Image.new("RGBA", SIZE, (0, 255, 0, 255))
    bg.alpha_composite(im, ((SIZE[0] - im.width) // 2, SIZE[1] - im.height - round(SIZE[1] * 0.04)))
    return bg.convert("RGB")


def chiedi(ref_png, posa, tentativi=6):
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


SPECCHIO = {"cammina_sx": "cammina_dx"}   # posa -> posa da specchiare


def main():
    chi = sys.argv[1] if len(sys.argv) > 1 else "topo"
    if chi not in RIFERIMENTI:
        sys.exit(f"Personaggio sconosciuto: {chi} ({', '.join(RIFERIMENTI)})")
    scelte = [a for a in sys.argv[2:] if not a.startswith('--')] or (list(POSE) + list(SPECCHIO))
    os.makedirs(os.path.join(OUT, "raw"), exist_ok=True)
    ref = os.path.join(HERE, RIFERIMENTI[chi])
    for nome in scelte:
        if os.path.exists(os.path.join(OUT, f"{chi}_{nome}.png")) and "--rifai" not in sys.argv:
            print(f"⏭️  {chi} / {nome} già fatta (usa --rifai per rigenerarla)")
            continue
        print(f"🎨 {chi} / {nome}")
        if nome in SPECCHIO:
            src = os.path.join(OUT, "raw", f"{chi}_{SPECCHIO[nome]}.jpg")
            raw = ImageOps.mirror(Image.open(src).convert("RGB"))
        else:
            raw = chiedi(ref, POSE[nome])
        raw.save(os.path.join(OUT, "raw", f"{chi}_{nome}.jpg"), quality=93)
        ritaglia(raw).save(os.path.join(OUT, f"{chi}_{nome}.png"))
    print("✅ fatto →", OUT)


if __name__ == "__main__":
    main()
