#!/usr/bin/env python3
"""Clip Wan 2.2 per 'Lavati le mani!' (coniglietto). Catena: start(n)=ultimo fotogramma clip(n-1). python3 mani_clips.py <n...> [SEED=..]"""
import os, shutil, subprocess, sys, time
from gradio_client import Client, handle_file
from PIL import Image, ImageDraw, ImageFilter
D = "assets/v/mani"
STYLE = " 3D Pixar animation for small children, smooth natural movement, locked static camera, one single rabbit, correct anatomy, bright colors."
NEG = "static, frozen, blurry, distorted face, extra limbs, duplicate characters, two rabbits, other animals, text, subtitles, watermark, camera shake, zoom, low quality, talking, moving lips"
CLIPS = {
 1: ("The little rabbit looks worried at its two front paws covered in brown mud and holds them up toward the camera, then shakes its head. Mouth closed, nobody talks.", 2.5),
 3: ("The little rabbit stands at the white sink, turns on the silver tap, and clear water runs from the tap over its front paws, washing the brown mud off. The rabbit looks happy, mouth closed, nobody talks.", 3.0),
 4: ("The little rabbit presses the soap dispenser and rubs its two front paws together, white soap foam and bubbles cover its paws. Happy face, mouth closed, nobody talks.", 3.0),
 5: ("The little rabbit holds its soapy front paws under the running water from the tap, the foam washes away and the paws become clean and white. Happy face, mouth closed, nobody talks.", 3.0),
 6: ("The little rabbit takes a fluffy white towel, dries its clean front paws and then shows its clean paws to the camera with a big happy smile and jumps with joy. Mouth closed, nobody talks.", 3.5),
 2: ("The little rabbit hops happily to the right, toward the white sink on the wooden stand, and stops in front of it. Mouth closed, nobody talks.", 3.0),
}
def start_mud():
    im = Image.open(f"{D}/R.png").convert("RGB"); mud = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(mud)
    for (cx, cy) in [(145, 398), (333, 380)]:                       # le due zampe anteriori
        d.ellipse((cx - 22, cy - 24, cx + 22, cy + 22), fill=(92, 58, 30, 255))
    mud = mud.filter(ImageFilter.GaussianBlur(2)); im.paste(mud, (0, 0), mud)
    im.crop((112, 0, 472, 640)).resize((720, 1280), Image.LANCZOS).save(f"{D}/start1.png")
def last_frame(n, dst):
    subprocess.check_call(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.1", "-i", f"{D}/clip{n}.mp4", "-frames:v", "1", dst])
def gen(n):
    start = f"{D}/start{n}.png"
    if n == 1: start_mud()
    else: last_frame(n - 1, start)
    c = Client("zerogpu-aoti/wan2-2-fp8da-aoti-faster"); t = time.time()
    r = c.predict(handle_file(start), CLIPS[n][0] + STYLE, 6, NEG, CLIPS[n][1], 1, 1, int(os.environ.get("SEED", 42)), False, api_name="/generate_video")
    v = r[0]["video"] if isinstance(r[0], dict) else r[0]; shutil.copy(v, f"{D}/clip{n}.mp4"); print(f"clip{n} ok {time.time()-t:.0f}s")
if __name__ == "__main__":
    for a in sys.argv[1:]: gen(int(a))
