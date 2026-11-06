"""contact sheet: ultimo fotogramma (97%) di tutte le slide di un blocco, 2 per riga. Uso: python3 sheets.py 1,2,3"""
import sys, os, glob
from PIL import Image
for b in sys.argv[1].split(','):
    fs = sorted(glob.glob(f'../pv/pv{b}_*_97.png'), key=lambda f: int(f.split('_')[1]))
    if not fs: continue
    ims = [Image.open(f).resize((800, 450)) for f in fs]; rows = (len(ims) + 1) // 2
    sh = Image.new('RGB', (1600, 450 * rows), (0, 0, 0))
    for i, im in enumerate(ims): sh.paste(im, ((i % 2) * 800, (i // 2) * 450))
    sh.save(f'../pv/sheet{b}.png')
