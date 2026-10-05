import sys
sys.path.insert(0,'/home/claude/slides')
from scenes3 import *
pts=[(1,1.2),(1,3.6),(2,0.6),(2,4.9),(3,1.4),(3,3.4),(4,2.0),(4,3.7),(4,5.9),(5,1.9),(5,4.6),(5,6.5),(6,1.2),(6,3.5),(6,4.6),(6,6.1)]
if len(sys.argv)>1:
    keep=[int(x) for x in sys.argv[1:]]
    pts=[p for p in pts if p[0] in keep]
tiles=[]
for n,tt in pts:
    fn,nf=SCENES3[n]
    tt=min(tt,(nf-1)/FPS)
    img=background(tt); fn(img,tt); tiles.append(img.resize((270,480)))
cols=6; rows=(len(tiles)+cols-1)//cols
g=Image.new('RGB',(270*cols,480*rows))
for i,im in enumerate(tiles): g.paste(im,((i%cols)*270,(i//cols)*480))
g.save('/tmp/prev3.png'); print('ok',len(tiles))