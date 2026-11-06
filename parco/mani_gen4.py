import sys, torch
from diffusers import AutoPipelineForText2Image
D="assets/v/mani"; torch.set_num_threads(4)
BASE="3D Pixar animation style render, a cute fluffy white baby rabbit with big pink ears, pink collar and yellow knitted sweater, bright blue tiled bathroom with a white sink and silver tap, one single rabbit, highly detailed, children cartoon, "
S={
 "2":"standing on a small wooden step stool at the sink, the silver tap is running water over its front paws, happy face",
 "3":"standing at the sink, front paws full of white soap foam, bubbles, happy face",
 "4":"standing at the sink rubbing its front paws together full of soap bubbles and foam, smiling",
 "5":"standing at the sink, front paws under running water from the tap, water splashes, happy face",
 "6":"holding a fluffy white towel, drying clean front paws, very happy smiling",
}
p=AutoPipelineForText2Image.from_pretrained("stabilityai/sd-turbo")
for k in sys.argv[1:]:
    for s in (31,32,33):
        p(BASE+S[k],num_inference_steps=4,guidance_scale=0.0,height=640,width=512,generator=torch.Generator().manual_seed(s)).images[0].save(f"{D}/T{k}_{s}.png"); print(k,s,flush=True)
