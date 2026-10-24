#!/usr/bin/env python3
"""Clip animate VERE e GRATIS per 'Chi ha mangiato il mela': Wan 2.2 immagine->video (Space HuggingFace, token HF nei segreti di rete).
Una clip alla volta, salta quelle già fatte. Uso: python3 palloncino_clips.py [n ...]"""
import os, shutil, sys, time
from gradio_client import Client, handle_file

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "assets", "v", "regalo")
SPACE = "zerogpu-aoti/wan2-2-fp8da-aoti-faster"
STYLE = " 3D Pixar animation for small children, smooth natural movement, locked static camera, same characters, no new characters, correct number of fingers, bright colors."
NEG = ("static, frozen, still image, blurry, distorted face, extra fingers, extra limbs, deformed hands, duplicate characters, clones, "
       "text, subtitles, watermark, camera shake, zoom, walking backwards, low quality")
CLIPS = {
    1: ("Wide shot at sunset: the little grey mouse and the squirrel stand holding a blue gift box with a red ribbon, the mouse talks excitedly and bounces a little, the squirrel nods.", 3.0, ""),
    2: ("Close-up of the squirrel, looking around nervously, he puts one paw over his mouth and whispers, eyes darting left and right.", 2.5, ""),
    3: ("Wide shot: the hedgehog peeks from behind the green bush, curious, and talks quietly, while the mouse and the squirrel hold the gift and look away innocently.", 3.0, ""),
    4: ("Close-up of the little grey mouse with a nervous smile, he shakes his head and whispers a secret, glancing aside.", 2.0, ""),
    5: ("The orange fox walks in from the right toward the group and waves hello and talks, the mouse, squirrel and hedgehog stand together hiding the gift behind them and smile innocently, mouths closed.", 3.0, ""),
    6: ("Everyone raises both arms and cheers together with big open mouths, bouncing with joy, the fox is surprised and delighted.", 2.5, ""),
    7: ("Close-up of the happy orange fox, laughing with joy, he holds the gift and talks thankfully, eyes sparkling.", 3.0, ""),
    8: ("The four friends hug each other and jump with joy together, laughing, no one talks.", 3.5, "talking, speaking"),
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
