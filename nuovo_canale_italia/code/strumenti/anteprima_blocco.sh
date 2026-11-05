#!/bin/bash
# Uso: anteprima_blocco.sh pagina.html durata_s out.jpg   -> un fotogramma ogni 1,5 s, dall'inizio ALLA FINE del blocco, in un unico montaggio (circa 1 minuto). OBBLIGATORIO per ogni blocco PRIMA del render.
cd "$(dirname "$0")/.."; D=$(mktemp -d); T=$(python3 -c "
d=float('$2');t=[0.05];x=1.5
while x<d-.2: t.append(round(x,2)); x+=1.5
t.append(round(d-.1,2));print(','.join(map(str,t)))")
node render_3d.js "$1" $D "$T" >/dev/null && python3 - "$D" "$3" <<'P'
import sys,glob
from PIL import Image
fs=sorted(glob.glob(sys.argv[1]+'/t*.png'),key=lambda f:float(f.split('/t')[-1][:-4]))
W,H=270,480;c=8;r=(len(fs)+c-1)//c;M=Image.new('RGB',(W*c,H*r))
for i,f in enumerate(fs):M.paste(Image.open(f).convert('RGB').resize((W,H)),((i%c)*W,(i//c)*H))
M.save(sys.argv[2],quality=80);print(len(fs),'fotogrammi nel montaggio')
P
