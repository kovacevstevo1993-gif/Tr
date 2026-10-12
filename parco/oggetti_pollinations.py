#!/usr/bin/env python3
"""Oggetti 3D (stile Pixar, come i personaggi) per lo Short: barattolo, coperchio, biscotto, farfalla magica.
Parte da testo (barattolo, biscotto, farfalla ali aperte) e poi deriva le varianti in image-to-image dallo stesso oggetto
(così coperchio/barattolo aperto/farfalla chiusa sono identici). Output: assets/obj/<nome>.png (RGBA).
Uso: python3 oggetti_pollinations.py [nome ...] [--rifai]"""
import base64, io, os, sys, time
import requests
from PIL import Image
import numpy as np
from scipy.ndimage import binary_dilation, label
import colorsys


def ritaglia(img, lo=10, span=45, vetro=False, magenta=False):
    """chiave verde più severa di quella dei personaggi (via ombre a terra); con vetro=True corregge la tinta verde vista attraverso il vetro"""
    a = np.asarray(img).astype(float); r, g, b = a[..., 0], a[..., 1], a[..., 2]
    verde = (np.minimum(r, b) - g) if magenta else (g - np.maximum(r, b))
    alpha = np.clip(1 - (verde - lo) / span, 0, 1); alpha[verde > lo + span] = 0
    solido = alpha > 0.5; lab, n = label(solido)
    if n:
        dim = np.bincount(lab.ravel())[1:]; solido = lab == (1 + int(np.argmax(dim)))
        alpha = np.where(binary_dilation(solido, iterations=3), alpha, 0)
    if magenta:                                                                        # despill magenta sul bordo
        m = np.clip(np.minimum(r, b) - g, 0, None) * (alpha < 0.999); a[..., 0] = r - m; a[..., 2] = b - m
    else:
        sp = g > np.maximum(r, b); a[..., 1] = np.where(sp, np.maximum(r, b), g)          # despill del bordo
    if vetro:                                                                          # biscotti visti attraverso il vetro: via il verde-oliva
        h = np.zeros(r.shape); 
        mx = np.maximum(np.maximum(r, g), b); mn = np.minimum(np.minimum(r, g), b)
        olive = (g >= r * 0.92) & (g > b * 1.25) & (mx > 60)
        a[..., 1] = np.where(olive, np.minimum(g, r * 0.80 + b * 0.2), a[..., 1])
    return Image.fromarray(np.dstack([a, alpha * 255]).astype("uint8"), "RGBA")

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "obj"); os.makedirs(os.path.join(OUT, "raw"), exist_ok=True)
GEN = "https://gen.pollinations.ai/v1/images/generations"
EDIT = "https://gen.pollinations.ai/v1/images/edits"
STILE = ("3D Pixar animation style, soft studio lighting, rich colors, highly detailed, front view, centered, "
         "plain flat pure green #00FF00 background, no ground, no shadow, no text, no watermark")

STILE_M = STILE.replace("pure green #00FF00", "pure magenta #FF00FF")
OGG = {
    "tree": (None, "a giant magical apple tree with a thick friendly trunk, big roots at the base and a huge round lush green crown full of shiny red apples, whole tree visible from roots to top, " + STILE_M, (768, 1376)),
    "seed": (None, "one tiny glowing golden magic seed with sparkles around it, " + STILE_M, (768, 768)),
    "sprout": (None, "a small cute green sprout with two round leaves growing from a little mound of brown soil, " + STILE_M, (768, 768)),
    "apple": (None, "one shiny juicy red apple with a small green leaf on its stem, " + STILE_M, (768, 768)),
    "cloud": (None, "a cute fluffy white rain cloud with a tiny smiling face and a light grey-blue underside, " + STILE_M, (768, 768)),
    "bird": (None, "a cute small blue bird with big shiny eyes flying with its wings open, " + STILE_M, (768, 768)),
    "bucket": (None, "a cute bright blue plastic sand bucket with a yellow handle, seen from a slightly high front 3/4 view, empty and clean, " + STILE, (768, 768)),
    "shovel": (None, "a small red plastic toy beach shovel with a yellow handle, seen from the front, " + STILE, (768, 1024)),
    "castle_small": (None, "a small cute sand castle made of golden wet sand with three little round towers, a small arched door and tiny windows, simple, " + STILE, (768, 768)),
    "castle_big": (None, "a very tall, grand and detailed golden sand castle with many towers of different heights, arched door, windows, crenellated walls and stairs, perfectly built, no flag, " + STILE, (768, 1024)),
    "sand_heap": (None, "a messy collapsed wet sand pile with a few small broken tower pieces, flat low heap, " + STILE, (768, 768)),
    "seagull": (None, "a cute white seagull with big friendly eyes and an orange beak flying with its wings wide open, " + STILE, (1024, 768)),
    "balloon": (None, "a big round hot air balloon envelope with bright smooth glossy vertical stripes in red, yellow, orange and blue ONLY (absolutely no green and no pink), a golden band at the bottom with a small round opening, whole balloon seen from the front, NO ropes, NO basket, " + STILE, (768, 1024)),
    "basket": (None, "a cute wide low wicker basket of a hot air balloon seen exactly from the front at eye level, rectangular woven light-brown wicker with a thick braided rope rim on top and four small wooden corner posts, empty, " + STILE, (1024, 768)),
    "nuvola_a": (None, "one big soft fluffy white cumulus cloud with gentle blue-grey shading underneath and a warm light on top, long flat bottom, NO face, " + STILE, (1024, 768)),
    "nuvola_b": (None, "one small round puffy white cloud with a gentle blue-grey shaded underside, NO face, " + STILE, (1024, 768)),
    "toppa": (None, "one big round colorful patchwork repair patch made of yellow fabric with a red star in the middle and visible stitched edges, seen from the front, " + STILE_M, (768, 768)),
    "jar": (None, "a big transparent glass cookie jar with a cute round red plastic lid with a small yellow knob, filled to the top with many chocolate chip cookies, " + STILE, (768, 1024)),
    "jar_open": ("jar", "the exact same glass cookie jar, but WITHOUT the lid: open top, no lid at all, cookies visible inside up to the rim; everything else identical", (768, 1024)),
    "lid": ("jar", "only the red round lid with the yellow knob of this jar, alone, floating, slightly seen from above, nothing else in the picture", (768, 768)),
    "cookie": (None, "one single round chocolate chip cookie, golden brown with dark chocolate chips, " + STILE, (768, 768)),
    "bf_open": (None, "a magical cute butterfly with glowing golden-orange wings with sparkles and a tiny smiling face, wings fully open seen from the front, " + STILE, (1024, 1024)),
    "bf_closed": ("bf_open", "the exact same butterfly but with its wings folded up closed together above its body, seen from the front, thin profile; everything else identical", (1024, 1024)),
}


def verde(im, size):
    from pose_pollinations import SIZE
    im = im.convert("RGBA"); bg = Image.new("RGBA", size, (0, 255, 0, 255))
    k = min(size[0] * 0.9 / im.width, size[1] * 0.9 / im.height); im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    bg.alpha_composite(im, ((size[0] - im.width) // 2, (size[1] - im.height) // 2)); return bg.convert("RGB")


def chiedi(prompt, size, ref=None, tentativi=6):
    for n in range(tentativi):
        try:
            if ref is None:
                r = requests.post(GEN, json={"model": "klein", "prompt": prompt, "size": f"{size[0]}x{size[1]}", "n": 1}, timeout=240)
            else:
                buf = io.BytesIO(); verde(ref, size).save(buf, "PNG")
                full = ("Use the attached object exactly as it is (same style, colors, proportions, camera angle). " + prompt +
                        ". Plain flat pure green #00FF00 background, no ground, no shadow, no text, no watermark.")
                r = requests.post(EDIT, data={"model": "klein", "size": f"{size[0]}x{size[1]}", "prompt": full},
                                  files={"image": ("ref.png", buf.getvalue(), "image/png")}, timeout=240)
            if r.status_code == 200:
                return Image.open(io.BytesIO(base64.b64decode(r.json()["data"][0]["b64_json"]))).convert("RGB")
            print(f"   HTTP {r.status_code}: {r.text[:120]}")
        except requests.RequestException as e:
            print("   errore rete:", e)
        time.sleep(2 ** (n + 1))
    raise RuntimeError("Pollinations non ha risposto")


def main():
    scelte = [a for a in sys.argv[1:] if not a.startswith("--")] or list(OGG)
    for nome in scelte:
        f = os.path.join(OUT, f"{nome}.png")
        if os.path.exists(f) and "--rifai" not in sys.argv: print("⏭️ ", nome); continue
        da, prompt, size = OGG[nome]
        print("🎨", nome)
        ref = None
        if da:
            ref = Image.open(os.path.join(OUT, f"{da}.png"))
        raw = chiedi(prompt, size, ref)
        raw.save(os.path.join(OUT, "raw", f"{nome}.jpg"), quality=93)
        im = ritaglia(raw, vetro=(nome in ('jar', 'jar_open')), magenta=('FF00FF' in prompt))
        bb = im.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox()
        im.crop(bb).save(f)
    print("✅ fatto")


if __name__ == "__main__":
    main()
