#!/usr/bin/env python3
"""Clip Wan 2.2 per 'Contiamo i pesci' v2: start = fkK.png (K pesci GIA' sul ghiaccio, composti). python3 pesci2_clips.py <k...>  [SEED=..]
Il pinguino guarda i K pesci e dice il numero; i pesci non cambiano di numero dentro la clip. Clip salvata come assets/v/pesci/ckK.mp4"""
import os, shutil, sys, time
from gradio_client import Client, handle_file
D = "assets/v/pesci"
NUM = {1: "one", 2: "two", 3: "three", 4: "four"}
DUR = {1: 2.5, 2: 2.5, 3: 2.5, 4: 2.5}
STYLE = " 3D Pixar animation for small children, smooth natural movement, locked static camera, the penguin stays in the same place, the fish stay exactly where they are, correct anatomy, bright colors."
NEG = "static, frozen, blurry, distorted face, extra limbs, more fish, fewer fish, moving fish away, duplicate characters, other penguins, text, subtitles, watermark, camera shake, zoom, low quality"
def prompt(k):
    return (f"The penguin looks down happily at the {NUM[k]} silver fish lying on the ice in front of it and talks, saying the number {NUM[k]}, then smiles at the camera. "
            "The fish stay on the ice and flop slightly. Beak closed when not talking.")
def gen(k):
    c = Client("zerogpu-aoti/wan2-2-fp8da-aoti-faster"); t = time.time()
    r = c.predict(handle_file(f"{D}/fk{k}.png"), prompt(k) + STYLE, 6, NEG, DUR[k], 1, 1, int(os.environ.get("SEED", 42)), False, api_name="/generate_video")
    v = r[0]["video"] if isinstance(r[0], dict) else r[0]; shutil.copy(v, f"{D}/ck{k}.mp4"); print(f"ck{k} ok {time.time()-t:.0f}s")
if __name__ == "__main__":
    for a in sys.argv[1:]: gen(int(a))
