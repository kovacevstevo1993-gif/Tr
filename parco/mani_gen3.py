import sys, torch
from diffusers import AutoPipelineForImage2Image
from PIL import Image
D="assets/v/mani"; torch.set_num_threads(4)
BASE="3D Pixar animation style render, the same cute fluffy white baby rabbit with big pink ears, pink collar and yellow knitted sweater, bright blue tiled bathroom, one single rabbit, highly detailed, children cartoon, "
S={
 "1":"front paws held up covered in thick brown mud, worried face, standing in the bathroom",
 "2":"standing on a small wooden step stool at a white sink, the silver tap is running water over its front paws, happy face, close shot",
 "3":"at the white sink, front paws covered in white soap foam bubbles, happy face, close shot",
 "4":"at the white sink, rubbing front paws together full of soap bubbles, foam, smiling, close shot",
 "5":"at the white sink, clean paws under running water from the silver tap, splashing drops, happy face, close shot",
 "6":"holding a fluffy white towel drying clean paws, very happy smiling, bright bathroom",
}
p=AutoPipelineForImage2Image.from_pretrained("stabilityai/sd-turbo")
src=Image.open(f"{D}/R.png").convert("RGB")
st=float(sys.argv[1])
for k in sys.argv[2:]:
    for s in (1,2):
        p(BASE+S[k],image=src,strength=st,num_inference_steps=4,guidance_scale=0.0,generator=torch.Generator().manual_seed(s)).images[0].save(f"{D}/S{k}_{s}.png"); print(k,s,flush=True)
