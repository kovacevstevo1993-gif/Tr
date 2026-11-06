#!/usr/bin/env python3
"""Immagini gratis in locale (SD-Turbo CPU) per 'Le porte dei colori'. python3 colori_gen.py A <seed...>"""
import sys, torch
from diffusers import AutoPipelineForText2Image
torch.set_num_threads(4)
P = ("3D Pixar animation style render, bright playful hallway with a white wall, three big closed doors side by side: the left door is solid red, the middle door is solid yellow, the right door is solid blue, "
     "one single cute baby penguin standing in front of the doors in the center, full body visible, wide shot, bright colors, soft light, highly detailed, children cartoon")
p = AutoPipelineForText2Image.from_pretrained("stabilityai/sd-turbo")
for s in map(int, sys.argv[2:]):
    im = p(P, num_inference_steps=4, guidance_scale=0.0, height=768, width=432, generator=torch.Generator().manual_seed(s)).images[0]
    im.save(f"assets/v/colori/A_{s}.png"); print("A", s, flush=True)
