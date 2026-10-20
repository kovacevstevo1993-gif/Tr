#!/usr/bin/env python3
"""Clip animate VERE e GRATIS per 'Il palloncino rosso': Wan 2.2 immagine->video (Space HuggingFace, token HF nei segreti di rete).
Una clip alla volta, salta quelle già fatte. Uso: python3 palloncino_clips.py [n ...]"""
import os, shutil, sys, time
from gradio_client import Client, handle_file

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "assets", "v", "palloncino")
SPACE = "zerogpu-aoti/wan2-2-fp8da-aoti-faster"
STYLE = " 3D Pixar animation for small children, smooth natural movement, locked static camera, same characters, no new characters, correct number of fingers, bright colors."
NEG = ("static, frozen, still image, blurry, distorted face, extra fingers, extra limbs, deformed hands, duplicate characters, clones, "
       "text, subtitles, watermark, camera shake, zoom, walking backwards, low quality")
CLIPS = {
    1: "The little grey mouse happily holds the string of his red balloon up high, the balloon bobs gently in the breeze, he smiles and sways his body, ears wiggle.",
    2: "The red balloon floats slowly up into the sky with its string dangling, the little mouse looks up at it with a surprised open mouth and reaches up with one hand.",
    3: "The red balloon is stuck in the branches of the round tree on the right, it sways a little; the little mouse looks up at it, points with his finger and looks sad.",
    4: "The orange squirrel jumps up high and grabs the red balloon string with his paw, then lands on the ground holding the balloon, smiling.",
    5: "The orange squirrel smiles and holds the red balloon string out toward the little grey mouse, the mouse reaches out and takes it, both smile.",
    6: "The little grey mouse and the orange squirrel dance happily together in the garden, jumping and waving their arms, the red balloon bobs above them.",
    7: "The little grey mouse and the orange squirrel wave hello to the viewer with big smiles, the red balloon bobs gently.",
}


def gen(c, n):
    out = os.path.join(D, f"clip{n}.mp4")
    if os.path.exists(out): print("salto", n); return
    for k in range(6):
        try:
            t0 = time.time()
            r = c.predict(handle_file(os.path.join(D, f"start{n}.png")), CLIPS[n] + STYLE, 6, NEG, float(os.environ.get("DUR", 5.0)), 1, 1, 42, False, api_name="/generate_video")
            v = r[0]["video"] if isinstance(r[0], dict) else r[0]; shutil.copy(v, out)
            print(f"clip{n} ok in {time.time() - t0:.0f}s", flush=True); return
        except Exception as e:
            print(f"clip{n} errore: {str(e)[:200]}", flush=True)
            if "quota" in str(e).lower() or "limit" in str(e).lower(): raise
            time.sleep(20)


if __name__ == "__main__":
    c = Client(SPACE)
    for n in [int(a) for a in sys.argv[1:]] or list(CLIPS): gen(c, n)
