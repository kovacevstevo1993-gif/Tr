#!/usr/bin/env python3
"""Clip animate VERE e GRATIS per 'Tanti auguri!': Wan 2.2 immagine->video (Space HuggingFace, token HF nei segreti di rete).
Una clip alla volta, salta quelle gia' fatte. Uso: python3 auguri_clips.py [n ...]"""
import os, shutil, sys, time
from gradio_client import Client, handle_file

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "assets", "v", "auguri")
SPACE = "zerogpu-aoti/wan2-2-fp8da-aoti-faster"
STYLE = " 3D Pixar animation for small children, smooth natural movement, locked static camera, same characters, no new characters, correct number of fingers, bright colors."
NEG = ("static, frozen, still image, blurry, distorted face, extra fingers, extra limbs, deformed hands, duplicate characters, clones, "
       "text, subtitles, watermark, camera shake, zoom, walking backwards, low quality")
CLIPS = {
    1: ("The little grey mouse runs happily and fast to the right along the green hill path, big happy smile, arms swinging, the blue gift box with a red ribbon stays on the ground and bounces along behind him, never leaving the ground, mouth closed, nobody talks.", 3.4, "talking, speaking, moving lips"),
    2: ("Close-up of the little grey mouse: he laughs with pure joy, bounces up and down on his feet and claps his hands near his chest, eyes closed with happiness, ears wiggle, mouth closed, no words.", 3.4, "talking, speaking"),
    3: ("The orange fox waves his arm and then spreads his arms wide proudly presenting the birthday cake with lit candles, the little grey mouse claps his hands and bounces with joy, both smile, no words.", 4.1, "talking, speaking, moving lips"),
}


def gen(c, n):
    out = os.path.join(D, f"clip{n}.mp4")
    if os.path.exists(out): print("salto", n); return
    for k in range(6):
        try:
            t0 = time.time()
            r = c.predict(handle_file(os.path.join(D, f"start{n}.png")), CLIPS[n][0] + STYLE, 6, NEG + (", " + CLIPS[n][2] if CLIPS[n][2] else ""), CLIPS[n][1], 1, 1, int(os.environ.get("SEED", 42)), False, api_name="/generate_video")
            v = r[0]["video"] if isinstance(r[0], dict) else r[0]; shutil.copy(v, out)
            print(f"clip{n} ok in {time.time() - t0:.0f}s", flush=True); return
        except Exception as e:
            print(f"clip{n} errore: {str(e)[:200]}", flush=True)
            if "quota" in str(e).lower() or "limit" in str(e).lower(): raise
            time.sleep(20)


if __name__ == "__main__":
    c = Client(SPACE)
    for n in [int(a) for a in sys.argv[1:]] or list(CLIPS): gen(c, n)
