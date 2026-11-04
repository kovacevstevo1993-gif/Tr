#!/usr/bin/env python3
"""Clip animate VERE e GRATIS per 'Chi ha mangiato il mela': Wan 2.2 immagine->video (Space HuggingFace, token HF nei segreti di rete).
Una clip alla volta, salta quelle già fatte. Uso: python3 palloncino_clips.py [n ...]"""
import os, shutil, sys, time
from gradio_client import Client, handle_file

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "assets", "v", "mela2")
SPACE = "zerogpu-aoti/wan2-2-fp8da-aoti-faster"
STYLE = " 3D Pixar animation for small children, smooth natural movement, locked static camera, same characters, no new characters, correct number of fingers, bright colors."
NEG = ("static, frozen, still image, blurry, distorted face, extra fingers, extra limbs, deformed hands, duplicate characters, clones, "
       "text, subtitles, watermark, camera shake, zoom, walking backwards, low quality")
CLIPS = {
    1: ("The orange squirrel smiles with excitement, points to the side with one paw and talks happily, bouncing a little.", 2.5, ""),
    2: ("The hedgehog hugs the big red apple tightly against his chest, turns his body slightly away and talks grumpily, shaking his head.", 2.5, ""),
    3: ("The hedgehog smiles warmly, holds out the red apple on his open paw towards the camera, and talks kindly offering to share, nodding.", 3.0, ""),
    4: ("The three friends happily eat pieces of red apple, chewing with joy, eyes closed in delight, bouncing slightly, no one talks.", 3.5, "talking, speaking"),
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
