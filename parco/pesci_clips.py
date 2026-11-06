#!/usr/bin/env python3
"""Clip Wan 2.2 (gratis) per 'Contiamo i pesci'. Catena: start(n) = ultimo fotogramma di clip(n-1). python3 colori_clips.py <n...>  [SEED=..]"""
import os, shutil, subprocess, sys, time
from gradio_client import Client, handle_file
D = "assets/v/pesci"
STYLE = " 3D Pixar animation for small children, smooth natural movement, locked static camera, the penguin stays in front, correct anatomy, bright colors."
NEG = "static, frozen, blurry, distorted face, extra limbs, duplicate characters, other penguins, text, subtitles, watermark, camera shake, zoom, low quality"
CLIPS = {
 1: ("A realistic silver fish jumps out of the dark blue water hole on the right and lands flopping on the white ice. The penguin looks at it with joy and talks, saying the number one, then smiles. Beak closed when not talking.", 3.5),
 2: ("A second realistic silver fish jumps out of the water hole and lands flopping on the ice next to the first fish. The penguin looks at it with joy and talks, saying the number two, then smiles. Beak closed when not talking.", 3.5),
 3: ("A third realistic silver fish jumps out of the water hole and lands flopping on the ice next to the other fish. The penguin looks at it with joy and talks, saying the number three, then smiles. Beak closed when not talking.", 3.5),
 4: ("A fourth realistic silver fish jumps high out of the water hole and lands on top of the penguin's head. The penguin is surprised and talks, saying the number four, then laughs happily. The three other fish stay on the ice.", 3.5),
 5: ("The penguin smiles proudly and points with its flipper at the four silver fish lying on the ice, one by one, talking happily.", 5.0),
}
def last_frame(n, dst):
    subprocess.check_call(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.1", "-i", f"{D}/clip{n}.mp4", "-frames:v", "1", dst])
def gen(n):
    start = f"{D}/start{n}.png"
    if n == 1: Image_up = __import__("PIL.Image", fromlist=["Image"]).open(f"{D}/R.png").resize((720, 1280)); Image_up.save(start)
    else: last_frame(n - 1, start)
    c = Client("zerogpu-aoti/wan2-2-fp8da-aoti-faster"); t = time.time()
    r = c.predict(handle_file(start), CLIPS[n][0] + STYLE, 6, NEG, CLIPS[n][1], 1, 1, int(os.environ.get("SEED", 42)), False, api_name="/generate_video")
    v = r[0]["video"] if isinstance(r[0], dict) else r[0]; shutil.copy(v, f"{D}/clip{n}.mp4"); print(f"clip{n} ok {time.time()-t:.0f}s")
if __name__ == "__main__":
    for a in sys.argv[1:]: gen(int(a))
