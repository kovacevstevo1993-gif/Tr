import sys, torch
from diffusers import AutoPipelineForText2Image
D="assets/v/mani"; torch.set_num_threads(4)
P=("3D Pixar animation style render, a cute fluffy white baby rabbit with big pink ears wearing a yellow t-shirt standing on a blue step stool at a white bathroom sink with a silver tap, "
   "front paws held out covered in brown mud, worried face, bright bathroom with light blue tiles, one single rabbit, full body, highly detailed, children cartoon")
p=AutoPipelineForText2Image.from_pretrained("stabilityai/sd-turbo")
W,H=int(sys.argv[1]),int(sys.argv[2])
for s in map(int,sys.argv[3:]):
    p(P,num_inference_steps=4,guidance_scale=0.0,height=H,width=W,generator=torch.Generator().manual_seed(s)).images[0].save(f"{D}/C_{W}x{H}_{s}.png"); print(s,flush=True)
