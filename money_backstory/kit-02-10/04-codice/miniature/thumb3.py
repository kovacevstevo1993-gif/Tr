from common import *
W2,H2=1280,720
im=Image.new('RGBA',(W2,H2),(0,0,0,255))
L=Image.new('RGBA',(W2,H2)); ld=ImageDraw.Draw(L)
for x in range(W2):
    t=x/W2
    ld.line([x,0,x,H2],fill=(int(150-60*t),20,30,255))
R=Image.new('RGBA',(W2,H2)); rd=ImageDraw.Draw(R)
for x in range(W2):
    t=x/W2
    rd.line([x,0,x,H2],fill=(10,int(90+60*t),50,255))
mask=Image.new('L',(W2,H2),0); ImageDraw.Draw(mask).polygon([(700,0),(W2,0),(W2,H2),(560,H2)],fill=255)
im=Image.composite(R,L,mask)
# vignette
v=Image.new('RGBA',(W2,H2),(0,0,0,0)); vd=ImageDraw.Draw(v); vd.rectangle([0,0,W2,H2],fill=(0,0,0,140)); vd.ellipse([-150,-120,W2+150,H2+120],fill=(0,0,0,0))
im=Image.alpha_composite(im,v.filter(ImageFilter.GaussianBlur(90)))
d=ImageDraw.Draw(im)
def T(s,f,x,y,col,anchor='l',stroke=8,sc=(0,0,0)):
    b=d.textbbox((0,0),s,font=f,stroke_width=stroke); w=b[2]-b[0]
    X=x-b[0] if anchor=='l' else (x-w/2-b[0] if anchor=='c' else x-w-b[0])
    d.text((X,y-b[1]),s,font=f,fill=col,stroke_width=stroke,stroke_fill=sc)
# glow behind numbers
G=Image.new('RGBA',(W2,H2),(0,0,0,0)); gd=ImageDraw.Draw(G)
gd.ellipse([40,60,560,520],fill=(255,70,70,120)); gd.ellipse([760,60,1260,520],fill=(80,255,140,110))
im=Image.alpha_composite(im,G.filter(ImageFilter.GaussianBlur(80))); d=ImageDraw.Draw(im)
T('62',BOLD(300),300,150,(255,255,255),'c',stroke=10)
T('70',BOLD(300),1000,150,(255,255,255),'c',stroke=10)
# arrows
d.rectangle([282,420,318,470],fill=(255,70,70),outline=(0,0,0),width=4); d.polygon([(245,468),(355,468),(300,530)],fill=(255,70,70),outline=(0,0,0),width=4)
d.rectangle([982,470,1018,530],fill=(90,255,140),outline=(0,0,0),width=4); d.polygon([(945,472),(1055,472),(1000,410)],fill=(90,255,140),outline=(0,0,0),width=4)
# question mark center
T('VS',BOLD(110),645,270,(255,214,70),'c',stroke=8)
# top banner
f0=BOLD(78); lab0='SOCIAL SECURITY'
b0=d.textbbox((0,0),lab0,font=f0); bw0=b0[2]-b0[0]+80; bx0=(W2-bw0)/2
d.rounded_rectangle([bx0,18,bx0+bw0,128],radius=20,fill=(255,255,255),outline=(0,0,0),width=7)
d.text((bx0+40-b0[0],73-(b0[3]-b0[1])/2-b0[1]),lab0,font=f0,fill=(20,40,90))
# bottom banner
f=BOLD(84); lab='$124,800 MISTAKE?'
b=d.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+90; bx=(W2-bw)/2; by=560
d.rounded_rectangle([bx,by,bx+bw,by+140],radius=28,fill=(255,214,70),outline=(0,0,0),width=8)
d.text((bx+45-b[0],by+70-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(10,10,10))
im.convert('RGB').save('/mnt/user-data/outputs/miniatura-video1-v3.png')
im.convert('RGB').resize((336,189)).save('/home/claude/t2small.png')
