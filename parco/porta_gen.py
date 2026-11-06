#!/usr/bin/env python3
"""Immagini gratis in locale (SD-Turbo, CPU). python3 porta_gen.py A <seed...>  |  B <seed...> (img2img da A)"""
import sys, torch
from diffusers import AutoPipelineForText2Image, AutoPipelineForImage2Image
from PIL import Image
D = "assets/v/porta"
torch.set_num_threads(4)
PA = ("3D Pixar animation style render, cozy living room at night with warm lamp light, one single cute baby penguin sitting alone on a big blue sofa, a closed plain wooden door on the wall behind the sofa, "
      "only one character in the room, full body of the penguin visible, wide shot, bright colors, soft light, highly detailed, children cartoon")
PB = ("3D Pixar animation style render, cozy living room at night with warm lamp light, a cute fluffy baby penguin on a big blue sofa, the wooden door at the back is wide open "
      "and a huge friendly smiling brown teddy bear stands in the doorway holding a big birthday cake with candles, wide shot, bright colors, highly detailed, children cartoon")
mode = sys.argv[1]
if mode == "A":
    p = AutoPipelineForText2Image.from_pretrained("stabilityai/sd-turbo")
    for s in map(int, sys.argv[2:]):
        im = p(PA, num_inference_steps=4, guidance_scale=0.0, height=768, width=432, generator=torch.Generator().manual_seed(s)).images[0]
        im.save(f"{D}/A_{s}.png"); print("A", s, flush=True)
else:
    p = AutoPipelineForImage2Image.from_pretrained("stabilityai/sd-turbo")
    src = Image.open(f"{D}/A.png").convert("RGB").resize((432, 768))
    for s in map(int, sys.argv[2:]):
        im = p(PB, image=src, strength=0.6, num_inference_steps=4, guidance_scale=0.0, generator=torch.Generator().manual_seed(s)).images[0]
        im.save(f"{D}/B_{s}.png"); print("B", s, flush=True)
