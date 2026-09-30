import sys
sys.path.insert(0,'/home/claude/slides')
from scenes2 import *
which = [int(x) for x in sys.argv[1:]] or [1,2,3,4,5,6]
tiles=[]
for n in which:
    fn, nf = SCENES[n]
    t = (nf-1)/FPS
    img = background(t); fn(img, t)
    tiles.append(img.resize((360,640)))
cols=3; rows=(len(tiles)+cols-1)//cols
g=Image.new('RGB',(360*cols,640*rows))
for i,im in enumerate(tiles): g.paste(im,((i%cols)*360,(i//cols)*640))
g.save('/tmp/prev2.png')
print('ok')