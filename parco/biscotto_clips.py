#!/usr/bin/env python3
"""Clip animate VERE e GRATIS per 'Chi ha mangiato il biscotto': Wan 2.2 immagine->video (Space HuggingFace, token HF nei segreti di rete).
Una clip alla volta, salta quelle già fatte. Uso: python3 palloncino_clips.py [n ...]"""
import os, shutil, sys, time
from gradio_client import Client, handle_file

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "assets", "v", "biscotto")
SPACE = "zerogpu-aoti/wan2-2-fp8da-aoti-faster"
STYLE = " 3D Pixar animation for small children, smooth natural movement, locked static camera, same characters, no new characters, correct number of fingers, bright colors."
NEG = ("static, frozen, still image, blurry, distorted face, extra fingers, extra limbs, deformed hands, duplicate characters, clones, "
       "text, subtitles, watermark, camera shake, zoom, walking backwards, low quality")
CLIPS = {
    1: ("Three friends, a little grey mouse, an orange fox and a green frog, look at the empty plate on the table, gasp in surprise with open mouths and look at each other.", 3.0, ""),
    2: ("The little grey mouse shakes his head and talks, raising both hands in a gesture of innocence, saying it was not me.", 2.5, ""),
    3: ("The orange fox talks with a sly innocent smile, shrugs his shoulders and looks away while his tail swishes.", 2.5, ""),
    4: ("The green frog talks, shakes his head no, then smiles innocently and blinks his big eyes.", 2.0, ""),
    5: ("The three friends look down at the cookie crumbs on the floor and point at them, mouths closed, nobody talks, curious eyes.", 3.0, "talking, speaking, moving lips"),
    6: ("The hedgehog takes a bite of the cookie and chews happily, then eyes wide he notices he was caught and covers his mouth with both paws, embarrassed.", 2.9, ""),
    7: ("All four friends laugh happily together and bounce a little with joy, big smiles.", 4.0, ""),
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
