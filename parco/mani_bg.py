import sys, torch
from diffusers import AutoPipelineForText2Image
torch.set_num_threads(4)
P=("3D Pixar animation style render, empty bright children bathroom with light blue tiles, a big white sink with a wide basin and a silver tap seen from the front, white soap dispenser and a fluffy white towel on the side, "
   "nobody in the room, no animals, highly detailed, children cartoon")
p=AutoPipelineForText2Image.from_pretrained("stabilityai/sd-turbo")
for s in map(int,sys.argv[1:]):
    p(P,num_inference_steps=4,guidance_scale=0.0,height=640,width=512,generator=torch.Generator().manual_seed(s)).images[0].save(f"assets/v/mani/BG_{s}.png"); print(s,flush=True)
