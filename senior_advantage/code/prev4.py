import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib; L = importlib.import_module(os.environ.get("L4MOD", "long4_b01_10"))
from eng2 import background
from PIL import Image
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
b=int(sys.argv[2]); secs=[float(x) for x in sys.argv[3:]]
ims=[]
for s in secs:
    img=background(s); L.DRAW[b](img,s); ims.append(img.resize((640,360)))
cols=2; rows=(len(ims)+1)//2
sheet=Image.new("RGB",(640*cols,360*rows))
for i,im in enumerate(ims): sheet.paste(im,((i%cols)*640,(i//cols)*360))
sheet.save(f"{out}/b{b}.png")
