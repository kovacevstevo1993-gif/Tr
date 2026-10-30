import sys, glob, re
from PIL import Image
b = int(sys.argv[1]); suf = sys.argv[2] if len(sys.argv) > 2 else '80'
fs = sorted(glob.glob(f'pv/pv{b}_*_{suf}.png'), key=lambda f: int(re.search(rf'pv{b}_(\d+)_', f).group(1)))
ims = [Image.open(f).convert('RGB') for f in fs]; n = len(ims); cols = 2; rows = (n + 1) // 2
sh = Image.new('RGB', (1920, 540 * rows))
for i, im in enumerate(ims): sh.paste(im, ((i % cols) * 960, (i // cols) * 540))
sh.save(f'pv/sheet{b}.png'); print(b, n)
