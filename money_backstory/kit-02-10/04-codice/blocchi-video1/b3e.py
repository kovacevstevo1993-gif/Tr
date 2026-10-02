from common import *
bg=make_bg()
def cart(d,x,y,col,a):
    c=col+(int(255*a),)
    d.line([x-60,y-40,x-40,y-40],fill=c,width=8); d.line([x-40,y-40,x-20,y+20],fill=c,width=8)
    d.polygon([(x-30,y-20),(x+60,y-20),(x+45,y+20),(x-18,y+20)],outline=c,fill=None,width=8) if False else d.line([(x-30,y-20),(x+60,y-20),(x+45,y+20),(x-18,y+20),(x-30,y-20)],fill=c,width=8)
    d.ellipse([x-18,y+32,x+2,y+52],fill=c); d.ellipse([x+30,y+32,x+50,y+52],fill=c)
def medcard(d,x,y,col,a):
    c=col+(int(255*a),)
    d.rounded_rectangle([x-60,y-40,x+60,y+40],radius=12,outline=c,width=8)
    d.rectangle([x-8,y-26,x+8,y+26],fill=c); d.rectangle([x-26,y-8,x+26,y+8],fill=c)
def draw(t):
    fr=bg.copy()
    p=ease((t-0.3)/2.0); v=int(12960*p/10)*10
    s=f'+${v:,}'
    G=Image.new('RGBA',(W,H),(0,0,0,0)); txt(G,s,BOLD(210),250,green,200); fr=Image.alpha_composite(fr,G.filter(ImageFilter.GaussianBlur(28)))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    a=ease(t/0.4); txt(L,'THAT\'S ALMOST',BOLD(48),150,goldL,255*a)
    txt(L,s,BOLD(210),250,green,255)
    b=ease((t-2.3)/0.5); txt(L,'MORE EVERY YEAR',BOLD(56),520,white,255*b)
    fr=Image.alpha_composite(fr,L)
    for i,(lab,fn,st) in enumerate([('A FULL YEAR OF GROCERIES',cart,4.4),('+ MEDICARE PREMIUMS',medcard,6.6)]):
        q=back((t-st)/0.45)
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C)
        cx=W/2+(i*2-1)*440; y=700
        cd.rounded_rectangle([cx-400,y,cx+400,y+220],radius=30,fill=card+(255,),outline=gold+(255,),width=4)
        fn(cd,cx-270,y+110,gold,1)
        f=BOLD(40); bb=cd.textbbox((0,0),lab,font=f)
        cd.text((cx-170-bb[0],y+110-(bb[3]-bb[1])/2-bb[1]),lab,font=f,fill=white+(255,))
        fr=pop(fr,C,(int(cx-405),y-5,int(cx+405),y+225),q)
    return fr
render(draw,10.17,'/mnt/user-data/outputs/v1-b3-05.mp4')
