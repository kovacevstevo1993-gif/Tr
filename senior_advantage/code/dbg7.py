import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenes7 as S, scenes5, eng2
from PIL import Image
for m in (S, scenes5): m.ambient_food = lambda *a, **k: None
b=int(sys.argv[1]); fr=[int(x) for x in sys.argv[2:]]
for i in fr:
    img = Image.new("RGB", (1080,1920), (0,0,0)); S.zoomed(S.DRAW[b])(img, i/30)
    a=np.asarray(img).max(axis=2)>45
    ys,xs=np.where(a)
    print(i, xs.min(), 1079-xs.max(), ys.min(), 1919-ys.max())
    edge=np.where(a[:,0]|a[:,-1])[0]; edge2=np.where(a[0,:]|a[-1,:])[0]
    print("  rows on side edges:", edge[:6], edge[-3:], " cols on top/bottom:", edge2[:6])
