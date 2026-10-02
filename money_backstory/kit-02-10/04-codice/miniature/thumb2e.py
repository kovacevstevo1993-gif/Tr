from common import *
W2,H2=1280,720
# clean light-to-dark bg like competitors
im=Image.new('RGBA',(W2,H2),(245,243,238,255))
L=Image.new('RGBA',(W2,H2)); ld=ImageDraw.Draw(L)
for y in range(H2):
    t=y/H2; ld.line([0,y,W2,y],fill=(int(240-30*t),int(238-32*t),int(232-30*t),255))
im=L
d=ImageDraw.Draw(im)
def T(s,f,x,y,col,anchor='l',stroke=0,sc=(0,0,0)):
    b=d.textbbox((0,0),s,font=f,stroke_width=stroke); w=b[2]-b[0]
    X=x-b[0] if anchor=='l' else (x-w/2-b[0] if anchor=='c' else x-w-b[0])
    d.text((X,y-b[1]),s,font=f,fill=col,stroke_width=stroke,stroke_fill=sc); return b[2]-b[0]
# big stack of cash right, shrinking
base=630
for i,(w,h,c) in enumerate([(360,58,(92,178,120)),(330,56,(92,178,120)),(290,54,(92,178,120)),(240,52,(92,178,120)),(180,50,(92,178,120))]):
    y=base-i*62; x=980
    d.rounded_rectangle([x-w/2,y-h,x+w/2,y],radius=10,fill=c,outline=(20,60,35),width=5)
    d.ellipse([x-26,y-h/2-22,x+26,y-h/2+22],outline=(20,60,35),width=5)
# red arrow down over stack
ax=980
d.polygon([(ax-55,190),(ax+55,190),(ax+55,250),(ax+110,250),(ax,360),(ax-110,250),(ax-55,250)],fill=(224,40,40),outline=(0,0,0))
d.line([(ax-55,190),(ax+55,190),(ax+55,250),(ax+110,250),(ax,360),(ax-110,250),(ax-55,250),(ax-55,190)],fill=(0,0,0),width=7)
# left text block
T('5 RETIREMENT',BOLD(74),60,80,(22,32,60),'l')
T('MISTAKES',BOLD(116),60,170,(224,40,40),'l')
f=BOLD(62); lab='THAT LEAVE YOU'
T(lab,BOLD(56),60,300,(22,32,60),'l')
# yellow highlight for BROKE AT 85
f2=BOLD(86); lab2='BROKE AT 85'
b2=d.textbbox((0,0),lab2,font=f2); bw2=b2[2]-b2[0]+40
d.rounded_rectangle([50,370,50+bw2,370+130],radius=12,fill=(255,214,60))
T(lab2,f2,70,398,(15,15,15),'l')
# bottom red banner
f3=BOLD(54); lab3='#3 SHOCKS EVERYONE'
b3=d.textbbox((0,0),lab3,font=f3); bw3=b3[2]-b3[0]+70
d.rounded_rectangle([50,556,50+bw3,556+92],radius=18,fill=(224,40,40),outline=(0,0,0),width=6)
d.text((50+35-b3[0],556+46-(b3[3]-b3[1])/2-b3[1]),lab3,font=f3,fill=(255,255,255))
im.convert('RGB').save('/mnt/user-data/outputs/miniatura-video2-stile-usa.png')
