#!/usr/bin/env python3
"""Clip animate VERE e GRATIS per 'Chi ha mangiato il mela': Wan 2.2 immagine->video (Space HuggingFace, token HF nei segreti di rete).
Una clip alla volta, salta quelle già fatte. Uso: python3 palloncino_clips.py [n ...]"""
import os, shutil, sys, time
from gradio_client import Client, handle_file

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "assets", "v", "torta")
SPACE = "zerogpu-aoti/wan2-2-fp8da-aoti-faster"
STYLE = " 3D Pixar animation for small children, smooth natural movement, locked static camera, same characters, no new characters, correct number of fingers, bright colors."
NEG = ("static, frozen, still image, blurry, distorted face, extra fingers, extra limbs, deformed hands, duplicate characters, clones, "
       "text, subtitles, watermark, camera shake, zoom, walking backwards, low quality")
CLIPS = {
    1: ("Wide shot of a picnic on a green hill: the little grey mouse and the squirrel cheer and bounce with joy around the birthday cake, a tiny blue bird flies in the far sky, mouths closed, nobody talks.", 2.5, "talking, speaking, moving lips"),
    2: ("Close-up of the little grey mouse: his eyes go wide and his jaw drops in shock, ears flick up, he quickly looks up at the sky, mouth open in shock without words.", 2.0, "talking, speaking"),
    3: ("The blue bird flies away across the sky carrying the cake, getting smaller, the mouse and the squirrel look up and shake their fists and jump up and down angrily, no words.", 3.0, "talking, speaking, moving lips"),
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
