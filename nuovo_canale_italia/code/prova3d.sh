#!/bin/bash
# uso: prova3d.sh pagina.html "t1,t2,..." out.jpg   (fotogrammi a piena risoluzione + montaggio)
cd "$(dirname "$0")"; D=/tmp/claude-0/-home-user-Tr/83f1dbc3-8a8a-5736-8880-3dc7d5db45cd/scratchpad/prova_$$; rm -rf $D
node render_3d.js "$1" $D "$2" && python3 - "$D" "$3" <<'P'
import sys,glob
from PIL import Image
fs=sorted(glob.glob(sys.argv[1]+'/t*.png'),key=lambda f:float(f.split('/t')[-1][:-4]))
W,H=360,640;M=Image.new('RGB',(W*len(fs),H))
for i,f in enumerate(fs): M.paste(Image.open(f).convert('RGB').resize((W,H)),(i*W,0))
M.save(sys.argv[2],quality=85);print(len(fs))
P
