import sys
sys.path.insert(0,'/home/claude/slides')
from scenes2 import *
pts=[(1,1.4),(2,1.0),(2,3.3),(3,2.6),(3,5.9),(4,1.9),(4,3.6),(5,3.0),(6,1.5),(6,3.4),(5,5.3),(1,2.9)]
tiles=[]
for n,tt in pts:
    fn,nf=SCENES[n]
    img=background(tt); fn(img,tt); tiles.append(img.resize((300,533)))
cols=6; rows=2
g=Image.new('RGB',(300*cols,533*rows))
for i,im in enumerate(tiles): g.paste(im,((i%cols)*300,(i//cols)*533))
g.save('/tmp/prev_mid.png'); print('ok')