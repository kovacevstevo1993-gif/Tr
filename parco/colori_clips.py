#!/usr/bin/env python3
"""Clip Wan 2.2 (gratis) per 'Le porte dei colori'. Catena: start(n) = ultimo fotogramma di clip(n-1). python3 colori_clips.py <n...>  [SEED=..]"""
import os, shutil, subprocess, sys, time
from gradio_client import Client, handle_file
D = "assets/v/colori"
STYLE = " 3D Pixar animation for small children, smooth natural movement, locked static camera, the penguin stays in front, correct anatomy, bright colors."
NEG = "static, frozen, blurry, distorted face, extra limbs, duplicate characters, other penguins, text, subtitles, watermark, camera shake, zoom, low quality"
CLIPS = {
 1: ("The penguin waddles to the left, opens the solid red door on the left with its flipper, and behind the door there is a big shiny red apple. The penguin looks amazed, beak closed, nobody talks.", 3.0),
 2: ("The penguin waddles to the middle, opens the solid yellow door in the middle with its flipper, and behind the door there is a big yellow rubber duck. The penguin looks amazed, beak closed, nobody talks.", 3.0),
 3: ("The penguin waddles to the right, opens the solid blue door on the right with its flipper, and behind the door there is a big blue balloon. The penguin looks amazed, beak closed, nobody talks.", 3.0),
 4: ("The penguin jumps happily with joy between the three open doors, clapping its flippers, big smile.", 2.5),
}
def last_frame(n, dst):
    subprocess.check_call(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.1", "-i", f"{D}/clip{n}.mp4", "-frames:v", "1", dst])
def gen(n):
    start = f"{D}/start{n}.png"
    if n == 1: Image_up = __import__("PIL.Image", fromlist=["Image"]).open(f"{D}/R_0.45.png").resize((720, 1280)); Image_up.save(start)
    else: last_frame(n - 1, start)
    c = Client("zerogpu-aoti/wan2-2-fp8da-aoti-faster"); t = time.time()
    r = c.predict(handle_file(start), CLIPS[n][0] + STYLE, 6, NEG, CLIPS[n][1], 1, 1, int(os.environ.get("SEED", 42)), False, api_name="/generate_video")
    v = r[0]["video"] if isinstance(r[0], dict) else r[0]; shutil.copy(v, f"{D}/clip{n}.mp4"); print(f"clip{n} ok {time.time()-t:.0f}s")
if __name__ == "__main__":
    for a in sys.argv[1:]: gen(int(a))
