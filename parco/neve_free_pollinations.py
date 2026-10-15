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
    "notte_giardino": ("amb", AMB_ST + "A cozy backyard garden at night under a starry sky with a big crescent moon, a small wooden house with warm glowing windows on the left, a white picket fence, bushes and flowers lit by soft blue moonlight, fireflies, "
                       "the lower half is a wide flat short green grass lawn, free of objects"),
    "spazio": ("amb", AMB_ST + "Deep outer space full of colorful nebulas in purple, blue and pink, thousands of twinkling stars, a big ringed planet like Saturn in the upper right, a small red planet far away on the left, no ground, no rocket"),
    "luna": ("amb", AMB_ST + "On the surface of the Moon: smooth light grey moon ground with soft round craters, black starry sky with the blue and green planet Earth big and glowing in the upper part of the sky, "
             "the lower half is a wide flat smooth grey moon surface, free of objects"),
    "rocket": ("obj", "a cute cartoon toy rocket made from a cardboard box painted red and white, pointed red nose cone on top, one big round glass porthole window in the middle, three red fins at the bottom, standing upright, whole rocket visible, " + G),
    "saturn": ("obj", "a cute cartoon planet Saturn, orange and yellow striped ball with big tilted shiny rings, " + G),
    "bosco_autunno": ("amb", AMB_ST + "An autumn forest clearing in warm golden afternoon light, tall trees with orange, red and yellow leaves, a big thick old tree trunk on the right side, colorful fallen leaves everywhere, soft sunbeams, "
                      "the lower half is a wide flat ground covered with orange and yellow fallen leaves, free of objects"),
    "festa_buio": ("amb", AMB_ST + "A cozy children's living room decorated for a birthday party: colorful paper garlands and bunting on the walls, a sofa, a window with night sky, a low wooden table in the middle, "
                   "the lower half is a flat warm wooden floor with a round colorful rug, free of objects"),
    "leaves_pile": ("obj", "a big round fluffy pile of orange, red and yellow autumn leaves, " + M),
    "bush": ("obj", "a round fluffy green bush with a few small red berries, " + M),
    "cake": ("obj", "a big cute birthday cake with pink frosting, three layers, colorful sprinkles, strawberries on top and five lit candles, front view, " + G),
    "balloons": ("obj", "a bunch of five shiny party balloons in red, yellow, blue, pink and purple with curly strings, " + G),
    "gift": ("obj", "a cute wrapped gift box with blue paper with white polka dots and a big shiny red ribbon bow on top, front view, " + G),
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
