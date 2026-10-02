from common import *
W2,H2=1280,720
im=Image.new('RGBA',(W2,H2),(120,16,20,255))
L=Image.new('RGBA',(W2,H2)); ld=ImageDraw.Draw(L)
for y in range(H2):
    t=y/H2; ld.line([0,y,W2,y],fill=(int(150-70*t),int(22-8*t),int(28-10*t),255))
im=L
G=Image.new('RGBA',(W2,H2),(0,0,0,0)); ImageDraw.Draw(G).ellipse([120,-60,900,640],fill=(255,90,80,110))
im=Image.alpha_composite(im,G.filter(ImageFilter.GaussianBlur(130)))
d=ImageDraw.Draw(im)
def T(s,f,x,y,col,anchor='l',stroke=10,sc=(0,0,0)):
    b=d.textbbox((0,0),s,font=f,stroke_width=stroke); w=b[2]-b[0]
    X=x-b[0] if anchor=='l' else (x-w/2-b[0] if anchor=='c' else x-w-b[0])
    d.text((X,y-b[1]),s,font=f,fill=col,stroke_width=stroke,stroke_fill=sc)
# empty wallet big (right)
cx,cy=960,400
d.rounded_rectangle([cx-230,cy-130,cx+230,cy+170],radius=30,fill=(120,78,40),outline=(0,0,0),width=8)
d.rounded_rectangle([cx+60,cy-20,cx+250,cy+90],radius=20,fill=(150,100,52),outline=(0,0,0),width=8)
d.ellipse([cx+140,cy+18,cx+184,cy+62],fill=(255,214,70),outline=(0,0,0),width=6)
# money flying out
for k,(dx,dy,rot) in enumerate([(-40,-230,0),(70,-300,0),(180,-250,0)]):
    x,y=cx+dx,cy+dy
    d.rounded_rectangle([x-70,y-40,x+70,y+40],radius=8,fill=(90,190,120),outline=(0,0,0),width=6)
    d.ellipse([x-22,y-22,x+22,y+22],outline=(0,0,0),width=5)
T('$0',BOLD(120),cx-60,cy+10,(255,255,255),'l',stroke=10)
# left text
T('5',BOLD(300),55,40,(255,255,255),'l',stroke=14)
T('MISTAKES',BOLD(78),60,370,(255,214,70),'l',stroke=10)
T('THAT LEAVE YOU',BOLD(50),60,470,(255,255,255),'l',stroke=8)
T('BROKE AT 85',BOLD(74),60,535,(255,255,255),'l',stroke=9)
# badge bottom
f=BOLD(52); lab='#3 SHOCKS EVERYONE'
b=d.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+70; bx=50; by=630
d.rounded_rectangle([bx+8,by+8,bx+bw+8,by+86],radius=39,fill=(0,0,0,170))
d.rounded_rectangle([bx,by,bx+bw,by+78],radius=39,fill=(255,214,70),outline=(0,0,0),width=6)
d.text((bx+35-b[0],by+39-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(15,15,15))
im.convert('RGB').save('/mnt/user-data/outputs/miniatura-video2-clickbait2.png')
