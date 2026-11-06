#!/usr/bin/env python3
"""Immagini gratis in locale (SD-Turbo CPU) per 'Lavati le mani'. python3 mani_gen.py A <seed...>"""
import sys, torch
from diffusers import AutoPipelineForText2Image
D = "assets/v/mani"
torch.set_num_threads(4)
PA = ("3D Pixar animation style render, medium shot, a cute fluffy white baby rabbit with big pink ears and big friendly eyes wearing a yellow t-shirt, standing at a white bathroom sink with a silver tap, "
      "the rabbit holds both front paws out toward the camera, both paws completely covered in thick dark brown mud, worried surprised face, bright clean bathroom with light blue tiles, soft light, one single character, centered, highly detailed, children cartoon")
p = AutoPipelineForText2Image.from_pretrained("stabilityai/sd-turbo")
for s in map(int, sys.argv[2:]):
    im = p(PA, num_inference_steps=4, guidance_scale=0.0, height=768, width=432, generator=torch.Generator().manual_seed(s)).images[0]
    im.save(f"{D}/B_{s}.png"); print("A", s, flush=True)
