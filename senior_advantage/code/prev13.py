import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenes13 as C
from scenes5 import zoomed
from PIL import Image
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
for b in [int(a) for a in sys.argv[2:]] or range(1, 8):
    C.S._cur["b"] = b
    n = C.DUR[b]
    frames = []
    for f in (0.28, 0.5, 0.78, 1.0):
        i = min(n - 1, int(n * f)) if f < 1 else n - 1
        img = C.background13(i / 30.0)
        zoomed(C.DRAW[b])(img, i / 30.0)
        frames.append(img.resize((540, 960), Image.LANCZOS))
    m = Image.new("RGB", (540 * 4, 960))
    for k, im in enumerate(frames):
        m.paste(im, (k * 540, 0))
    m.save(f"{out}/b{b}.png")
    print("ok", b)
