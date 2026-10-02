import sys; sys.path.insert(0,'/home/claude')
from common import *
W2,H2=1280,720
im=Image.new('RGBA',(W2,H2),(0,0,0,255)); d=ImageDraw.Draw(im)
# background: dark red radial
bg=Image.new('RGBA',(W2,H2)); bd=ImageDraw.Draw(bg)
for y in range(H2):
    t=y/H2; bd.line([0,y,W2,y],fill=(int(150-70*t),int(18+8*t),int(30+10*t),255))
im=bg
G=Image.new('RGBA',(W2,H2),(0,0,0,0)); gd=ImageDraw.Draw(G)
gd.ellipse([40,120,760,640],fill=(255,90,70,150)); gd.ellipse([800,150,1260,600],fill=(255,210,70,90))
im=Image.alpha_composite(im,G.filter(ImageFilter.GaussianBlur(90)))
v=Image.new('RGBA',(W2,H2),(0,0,0,0)); vd=ImageDraw.Draw(v); vd.rectangle([0,0,W2,H2],fill=(0,0,0,150)); vd.ellipse([-200,-150,W2+200,H2+150],fill=(0,0,0,0))
im=Image.alpha_composite(im,v.filter(ImageFilter.GaussianBlur(100))); d=ImageDraw.Draw(im)
def T(s,f,x,y,col,anchor='l',stroke=8,sc=(0,0,0)):
    b=d.textbbox((0,0),s,font=f,stroke_width=stroke); w=b[2]-b[0]
    X=x-b[0] if anchor=='l' else (x-w/2-b[0] if anchor=='c' else x-w-b[0])
    d.text((X,y-b[1]),s,font=f,fill=col,stroke_width=stroke,stroke_fill=sc)
# top banner
f0=BOLD(70); lab0='5 THINGS CHANGE AT'
b0=d.textbbox((0,0),lab0,font=f0); bw0=b0[2]-b0[0]+80; bx0=(W2-bw0)/2
d.rounded_rectangle([bx0,18,bx0+bw0,122],radius=20,fill=(255,255,255),outline=(0,0,0),width=7)
d.text((bx0+40-b0[0],70-(b0[3]-b0[1])/2-b0[1]),lab0,font=f0,fill=(20,40,90))
# big 59 + fraction
T('59',BOLD(400),330,145,(255,255,255),'c',stroke=14)
# fraction 1/2 drawn by hand
fx,fy=700,200
T('1',BOLD(150),fx,fy,(255,214,70),'c',stroke=9)
d.line([fx-70,fy+190,fx+70,fy+120],fill=(0,0,0),width=24); d.line([fx-70,fy+190,fx+70,fy+120],fill=(255,214,70),width=13)
T('2',BOLD(150),fx+45,fy+205,(255,214,70),'c',stroke=9)
# padlock (right)
cx,cy=1055,365
d.arc([cx-105,cy-230,cx+105,cy-20],180,360,fill=(0,0,0),width=62); d.arc([cx-105,cy-230,cx+105,cy-20],180,360,fill=(200,205,215),width=42)
d.rectangle([cx-105,cy-130,cx-63,cy-20],fill=(0,0,0)); d.rectangle([cx+63,cy-130,cx+105,cy-20],fill=(0,0,0))
d.rectangle([cx-98,cy-130,cx-70,cy-20],fill=(200,205,215)); d.rectangle([cx+70,cy-130,cx+98,cy-20],fill=(200,205,215))
d.rounded_rectangle([cx-150,cy-40,cx+150,cy+170],radius=36,fill=(255,70,70),outline=(0,0,0),width=9)
d.ellipse([cx-30,cy+20,cx+30,cy+80],fill=(0,0,0)); d.polygon([(cx-16,cy+75),(cx+16,cy+75),(cx+26,cy+140),(cx-26,cy+140)],fill=(0,0,0))
# bottom banner
f=BOLD(80); lab='#4 TRAPS THOUSANDS'
b=d.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+90; bx=(W2-bw)/2; by=565
d.rounded_rectangle([bx,by,bx+bw,by+130],radius=28,fill=(255,214,70),outline=(0,0,0),width=8)
d.text((bx+45-b[0],by+65-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(10,10,10))
im.convert('RGB').save('/mnt/user-data/outputs/miniatura-video3.png')
