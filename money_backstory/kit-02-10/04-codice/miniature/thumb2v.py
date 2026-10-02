from common import *
W2,H2=1280,720
im=Image.new('RGBA',(W2,H2),(0,0,0,255))
L=Image.new('RGBA',(W2,H2)); ld=ImageDraw.Draw(L)
for x in range(W2):
    t=x/W2; ld.line([x,0,x,H2],fill=(int(120-40*t),18,26,255))
R=Image.new('RGBA',(W2,H2)); rd=ImageDraw.Draw(R)
for x in range(W2):
    t=x/W2; rd.line([x,0,x,H2],fill=(int(12+10*t),int(70+40*t),40,255))
mask=Image.new('L',(W2,H2),0); ImageDraw.Draw(mask).polygon([(690,0),(W2,0),(W2,H2),(550,H2)],fill=255)
im=Image.composite(R,L,mask)
G=Image.new('RGBA',(W2,H2),(0,0,0,0)); gd=ImageDraw.Draw(G); gd.ellipse([80,-40,620,520],fill=(255,80,80,110))
im=Image.alpha_composite(im,G.filter(ImageFilter.GaussianBlur(90)))
d=ImageDraw.Draw(im)
def T(s,f,x,y,col,anchor='l',stroke=8):
    b=d.textbbox((0,0),s,font=f,stroke_width=stroke); w=b[2]-b[0]
    X=x-b[0] if anchor=='l' else (x-w/2-b[0] if anchor=='c' else x-w-b[0])
    d.text((X,y-b[1]),s,font=f,fill=col,stroke_width=stroke,stroke_fill=(0,0,0))
# top banner
f0=BOLD(70); lab0='RETIREMENT MISTAKES'
b0=d.textbbox((0,0),lab0,font=f0); bw0=b0[2]-b0[0]+80; bx0=(W2-bw0)/2
d.rounded_rectangle([bx0,16,bx0+bw0,120],radius=20,fill=(255,255,255),outline=(0,0,0),width=7)
d.text((bx0+40-b0[0],68-(b0[3]-b0[1])/2-b0[1]),lab0,font=f0,fill=(20,40,90))
# big 5
T('5',BOLD(300),300,150,(255,255,255),'c',stroke=12)
T('THAT QUIETLY',BOLD(62),620,210,(255,255,255),'l',stroke=7)
T('RUIN YOUR',BOLD(62),620,285,(255,255,255),'l',stroke=7)
T('RETIREMENT',BOLD(62),620,360,(255,214,70),'l',stroke=7)
# warning triangle
cx,cy=300,455
d.polygon([(cx,cy-60),(cx+110,cy+120),(cx-110,cy+120)],fill=(255,214,70),outline=(0,0,0))
d.line([(cx,cy-60),(cx+110,cy+120),(cx-110,cy+120),(cx,cy-60)],fill=(0,0,0),width=7)
d.rounded_rectangle([cx-13,cy+5,cx+13,cy+70],radius=6,fill=(10,10,10)); d.ellipse([cx-15,cy+82,cx+15,cy+112],fill=(10,10,10))
# bottom banner
f=BOLD(72); lab='#3 SHOCKS EVERYONE'
b=d.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+90; bx=(W2-bw)/2; by=580
d.rounded_rectangle([bx,by,bx+bw,by+120],radius=26,fill=(232,60,60),outline=(0,0,0),width=8)
d.text((bx+45-b[0],by+60-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(255,255,255))
im.convert('RGB').save('/mnt/user-data/outputs/miniatura-video2.png')
