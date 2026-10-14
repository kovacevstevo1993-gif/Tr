#!/usr/bin/env python3
"""Asset dello Short 'Il pupazzo di neve' con il modello GRATUITO di Pollinations (flux-2-dev-free, 1024x1024).
Ambienti: quadrato -> scalato a 1376 di altezza e ritagliato al centro (768x1376). Oggetti: chiave verde/magenta come oggetti_pollinations.
Uso: python3 neve_free_pollinations.py [nome ...] [--rifai]"""
import base64, io, os, sys, time, requests
from PIL import Image
from oggetti_pollinations import ritaglia

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = "community/scriptsnsenses-sys/flux-2-dev-free"
AMB_ST = ("3D Pixar animation movie still, soft warm lighting, rich saturated colors, highly detailed, cute and magical, children's cartoon, "
          "the scene is EMPTY: no people, no animals, no characters, no snowman, no text, no watermark. ")
OBJ = "3D Pixar animation style, soft studio lighting, rich colors, highly detailed, front view, centered, plain flat pure {} background, no ground, no shadow, no text, no watermark"
G, M = OBJ.format("green #00FF00"), OBJ.format("magenta #FF00FF")
ITEMS = {
    "neve_collina": ("amb", AMB_ST + "A snowy winter hilltop meadow in bright morning sunshine, blue sky with a few fluffy clouds, snow-covered pine trees at the far left and far right, "
                     "a tiny wooden cottage with a snowy roof and smoke from the chimney far away in the middle distance, the whole lower half is a wide smooth flat soft white snow field, free of objects"),
    "neve_discesa": ("amb", AMB_ST + "A long snowy slope seen from the top going down into a valley, tall snow-covered pine trees on both sides of the slope, a frozen blue lake and a little village far below, "
                     "bright blue sky, sunny, the lower half is a smooth wide white snow slope, free of objects"),
    "neve_sera": ("amb", AMB_ST + "A cozy snowy village square at dusk, little wooden houses with warm glowing yellow windows and thick snowy roofs, colorful string lights, a deep blue and violet evening sky with a big moon and stars, "
                  "the lower half is a wide smooth flat soft white snow ground glowing blue, free of objects"),
    "snowball": ("obj", "one big round snowball made of soft packed sparkling white snow with a slightly bumpy texture and soft blue shading, " + G),
    "carrot": ("obj", "one small bright orange carrot lying horizontally pointing to the right, with a short green leafy top on the left, " + M),
    "sled": ("obj", "a long low wide wooden toboggan sled for three children, seen from the side, flat wooden plank deck close to the ground with a red painted side rail, long curved metal runners curling up high at the front right end, no backrest, not a chair, empty, " + G),
    "pine": ("obj", "one tall snow-covered pine tree, dark green branches with thick white snow on top, whole tree visible from the trunk to the top, " + M),
}


def chiedi(prompt):
    for n in range(6):
        try:
            r = requests.post("https://gen.pollinations.ai/v1/images/generations", json={"model": MODEL, "prompt": prompt, "size": "1024x1024", "n": 1}, timeout=300)
            if r.status_code == 200: return Image.open(io.BytesIO(base64.b64decode(r.json()["data"][0]["b64_json"]))).convert("RGB")
            print("   HTTP", r.status_code, r.text[:120])
        except requests.RequestException as e: print("   rete:", e)
        time.sleep(2 ** (n + 1))
    raise RuntimeError("Pollinations non risponde")


def main():
    for nome in [a for a in sys.argv[1:] if not a.startswith("--")] or list(ITEMS):
        kind, p = ITEMS[nome]
        f = os.path.join(HERE, "assets", kind, nome + ".png")
        if os.path.exists(f) and "--rifai" not in sys.argv: print("salto", nome); continue
        print("genero", nome); im = chiedi(p)
        im.save(os.path.join(HERE, "assets", "obj", "raw", nome + ".jpg"), quality=93)
        if kind == "amb":
            im = im.resize((1376, 1376), Image.LANCZOS).crop((304, 0, 304 + 768, 1376)); im.save(f)
        else:
            o = ritaglia(im, magenta=("FF00FF" in p)); o.crop(o.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox()).save(f)


if __name__ == "__main__":
    main()
