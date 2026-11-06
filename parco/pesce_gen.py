#!/usr/bin/env python3
"""Immagini gratis in locale (SD-Turbo CPU) per 'Il pesce rubato'. python3 pesce_gen.py A <seed...>"""
import sys, torch
from diffusers import AutoPipelineForText2Image
torch.set_num_threads(4)
P = ("3D Pixar animation style render, bright sunny arctic ice field with blue sky and distant icebergs, a round dark hole in the ice in the foreground, "
     "one single cute baby penguin walking proudly on the ice holding a huge silver fish above its head with both flippers, full body visible, wide shot, bright colors, highly detailed, children cartoon")
p = AutoPipelineForText2Image.from_pretrained("stabilityai/sd-turbo")
for s in map(int, sys.argv[2:]):
    im = p(P, num_inference_steps=4, guidance_scale=0.0, height=768, width=432, generator=torch.Generator().manual_seed(s)).images[0]
    im.save(f"assets/v/pesce/A_{s}.png"); print("A", s, flush=True)
