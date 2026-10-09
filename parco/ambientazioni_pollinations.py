#!/usr/bin/env python3
"""Genera nuove ambientazioni verticali 9:16 nello STESSO stile del parco (image-to-image, Pollinations).

Uso:
    python3 ambientazioni_pollinations.py             # tutte
    python3 ambientazioni_pollinations.py cucina      # una sola

Output: assets/amb/<nome>.png (768x1376, nessun personaggio, pavimento libero in basso).
Il riferimento di stile è assets/s/sfondo_src.png (il parco).
"""
import base64, io, os, sys, time
import requests
from PIL import Image

URL = "https://gen.pollinations.ai/v1/images/edits"
MODEL = "klein"
SIZE = (768, 1376)
HERE = os.path.dirname(os.path.abspath(__file__))
RIF = os.path.join(HERE, "assets", "s", "sfondo_src.png")
OUT = os.path.join(HERE, "assets", "amb")

AMB = {
    "cucina": "a cozy bright children's kitchen interior with a wooden table, cabinets, a window with sunlight, fruit bowl on the counter",
    "spiaggia": ("a sunny tropical beach with gentle turquoise sea waves, a distant sailboat, soft fluffy clouds, two palm trees at the far sides", "smooth flat golden sand, wet sand near the water, no wood, no planks, no tiles, free of objects and shells"),
    "asilo": "a colorful kindergarten classroom with small tables, shelves full of toys and books, big window, paintings on the wall",
    "giardino": ("a bright sunny garden meadow in the early morning with colorful flowers, a small wooden fence, a little vegetable patch, a big blue sky with soft fluffy clouds, a few round trees and hills in the distance", "short flat green grass lawn, free of objects"),
    "bosco": ("an enchanted magical forest clearing with tall friendly trees, soft golden sunbeams through the leaves, ferns, tiny glowing flowers and mossy rocks at the sides", "flat soft green grass and moss ground, free of objects"),
    "tramonto": ("a green hill meadow at sunset with an orange and pink sky, soft warm golden light, small wildflowers, far hills and a distant lake", "short flat green grass lawn, free of objects"),
    "spiaggia_baia": ("the same style beach but a different cozy cove in golden afternoon light: smooth big rocks on the left, a calm turquoise lagoon, a small wooden pier far away, two palm trees, fluffy clouds", "smooth flat golden sand, free of objects and shells, no wood, no tiles", "spiaggia"),
    "spiaggia_tramonto": ("the same beach at SUNSET: big orange and pink sky with a low glowing sun near the horizon, warm golden light, calm sea reflecting the sunset, silhouettes of palm trees at the sides, a distant sailboat", "smooth flat warm golden sand, free of objects and shells, no wood, no tiles", "spiaggia"),
    "camera_sera": "a child's bedroom in the evening with a small bed, a warm night lamp, a window showing a starry night sky and moon",
}


def chiedi(prompt, tentativi=6, rif=None):
    buf = io.BytesIO()
    Image.open(rif or RIF).convert("RGB").resize(SIZE).save(buf, "PNG")
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


def main():
    scelte = sys.argv[1:] or list(AMB)
    os.makedirs(OUT, exist_ok=True)
    for nome in scelte:
        print("🏞️ ", nome)
        v = AMB[nome] if isinstance(AMB[nome], tuple) else (AMB[nome], "a plain matte wooden parquet floor, flat and non-reflective, no glass, no rug, free of objects")
        scena, suolo = v[0], v[1]; rif = os.path.join(OUT, v[2] + ".png") if len(v) > 2 else None
        prompt = (
            "Keep the exact same 3D Pixar-style rendering, soft lighting and colors as the reference image, "
            "vertical 9:16. Change only the scene to: " + scena + ". "
            "The scene is EMPTY: no people, no animals, no characters. "
            "The lower third of the frame is " + suolo + ", "
            "so characters can be placed there. No text, no watermark."
        )
        chiedi(prompt, rif=rif).save(os.path.join(OUT, f"{nome}.png"))
    print("✅ fatto →", OUT)


if __name__ == "__main__":
    main()
