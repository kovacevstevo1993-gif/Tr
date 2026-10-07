import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenes7 as S
from eng2 import background
from PIL import Image
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
clip = int(sys.argv[2]); secs = [float(x) for x in sys.argv[3:]]
fn = S.zoomed(S.DRAW[clip])
ims = []
for s in secs:
    img = background(s); fn(img, s); ims.append(img.resize((540, 960)))
sheet = Image.new("RGB", (540 * len(ims), 960))
for i, im in enumerate(ims): sheet.paste(im, (540 * i, 0))
sheet.save(f"{out}/clip{clip}.png")
