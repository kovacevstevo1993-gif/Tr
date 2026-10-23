#!/usr/bin/env python3
"""Clip animate VERE e GRATIS per 'Chi ha mangiato il mela': Wan 2.2 immagine->video (Space HuggingFace, token HF nei segreti di rete).
Una clip alla volta, salta quelle già fatte. Uso: python3 palloncino_clips.py [n ...]"""
import os, shutil, sys, time
from gradio_client import Client, handle_file

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "assets", "v", "mela")
SPACE = "zerogpu-aoti/wan2-2-fp8da-aoti-faster"
STYLE = " 3D Pixar animation for small children, smooth natural movement, locked static camera, same characters, no new characters, correct number of fingers, bright colors."
NEG = ("static, frozen, still image, blurry, distorted face, extra fingers, extra limbs, deformed hands, duplicate characters, clones, "
       "text, subtitles, watermark, camera shake, zoom, walking backwards, low quality")
CLIPS = {
    1: ("The little grey mouse holds out a big red apple with both hands towards the baby elephant, the hungry elephant looks at the apple with big excited eyes and opens his mouth wide, mouths closed otherwise, nobody talks.", 2.5, "talking, speaking, moving lips"),
    2: ("The baby elephant takes a huge bite of the red apple and chews it happily with puffed cheeks, eyes closed in delight, crunching.", 2.5, ""),
    3: ("The baby elephant raises his trunk and sprays a big fountain of water into the air, the little grey mouse in front covers his face with both hands in surprise, water splashes.", 2.5, "talking, speaking, moving lips"),
    4: ("The little grey mouse and the baby elephant laugh happily together, shaking with laughter, big smiles, mouths closed no words.", 2.0, "talking, speaking"),
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
