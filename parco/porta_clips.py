#!/usr/bin/env python3
"""Clip Wan 2.2 (gratis, token HF) per lo short della porta. python3 porta_clips.py <n> [SEED=..]"""
import os, shutil, sys, time
from gradio_client import Client, handle_file
D = "assets/v/porta"
STYLE = " 3D Pixar animation for small children, smooth natural movement, locked static camera, correct anatomy, bright colors."
NEG = "static, frozen, blurry, distorted face, extra limbs, duplicate characters, text, subtitles, watermark, camera shake, zoom, low quality"
CLIPS = {
 1: ("The little penguin sits on the blue sofa giggling and swaying happily, mouth closed, nobody talks. The wooden door behind stays closed.", 3.0),
 3: ("The little penguin's big eyes open wide in surprise and it turns its head quickly to look at the side, then freezes frozen with surprise, mouth closed, nobody talks.", 2.5),
 4: ("The little penguin jumps up and down with joy on the sofa, flapping its flippers happily and clapping, big smile, mouth closed, nobody talks.", 2.5),
 2: ("The wooden door behind the sofa slowly creaks open and a huge fluffy brown teddy bear walks in smiling and waves. The little penguin turns and looks up in surprise.", 3.0),
}
def gen(n):
    out = f"{D}/clip{n}.mp4"
    c = Client("zerogpu-aoti/wan2-2-fp8da-aoti-faster")
    t = time.time()
    r = c.predict(handle_file(f"{D}/start{n}.png"), CLIPS[n][0] + STYLE, 6, NEG, CLIPS[n][1], 1, 1, int(os.environ.get("SEED", 42)), False, api_name="/generate_video")
    v = r[0]["video"] if isinstance(r[0], dict) else r[0]; shutil.copy(v, out); print(f"clip{n} ok {time.time()-t:.0f}s")
if __name__ == "__main__":
    for a in sys.argv[1:]: gen(int(a))
