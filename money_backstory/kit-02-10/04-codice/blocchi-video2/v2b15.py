from common2 import *
import shutil, sys
S=["The goal isn't to avoid risk completely.","It's to balance it.","Keep enough safe money for the next few years of spending, and let the rest keep growing, so your savings can keep up with rising prices."]
TOTF=410
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0]+fs[1],fs[2]]; print(fs,durs,sum(durs)); s2=fs[0]/30
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,"THE GOAL: DON'T AVOID RISK...",SER(60),100,goldL,255*ease(t/0.4))
    cx,cy=W/2,560
    ang=math.radians(-14*(1-ease((t-s2)/1.0))) if t>s2 else math.radians(-14)
    d.polygon([(cx-60,cy+260),(cx+60,cy+260),(cx,cy+40)],fill=gold+(255,))
    dx,dy=math.cos(ang)*420,math.sin(ang)*420
    d.line([cx-dx,cy-dy,cx+dx,cy+dy],fill=gold+(255,),width=14); d.ellipse([cx-18,cy-18,cx+18,cy+18],fill=goldL+(255,))
    for sgn,lab,col in [(-1,'SAFETY',blue),(1,'GROWTH',green)]:
        px_,py_=cx+sgn*dx,cy+sgn*dy
        d.line([px_,py_,px_-70,py_+150],fill=gold+(255,),width=5); d.line([px_,py_,px_+70,py_+150],fill=gold+(255,),width=5)
        d.pieslice([px_-120,py_+90,px_+120,py_+260],0,180,fill=col+(255,)); txt(L,lab,BOLD(36),py_+190,navy,255,x=px_)
    if t>s2: txt(L,'BALANCE IT.',BOLD(80),850,white,255*ease((t-s2)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'A SIMPLE WAY TO BALANCE',SER(64),100,goldL,255*ease(t/0.4))
    cx,cy,R=560,560,250
    p=ease((t-0.3)/1.2)
    d.pieslice([cx-R,cy-R,cx+R,cy+R],-90,-90+110*p,fill=blue+(255,))
    q=ease((t-2.0)/1.4)
    d.pieslice([cx-R,cy-R,cx+R,cy+R],20,20+250*q,fill=green+(255,))
    d.ellipse([cx-140,cy-140,cx+140,cy+140],fill=(16,32,54,255))
    txt(L,'YOUR',BOLD(40),cy-50,white,255,x=cx); txt(L,'SAVINGS',BOLD(40),cy+5,white,255,x=cx)
    fr=Image.alpha_composite(fr,L)
    for k,(t0,col,title,sub) in enumerate([(0.6,blue,'SAFE MONEY','next few years of spending'),(2.3,green,'KEEPS GROWING','the rest of your savings')]):
        if t<t0: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); y=330+k*230
        cd.rounded_rectangle([960,y,1640,y+180],radius=30,fill=card+(255,),outline=col+(255,),width=5); cd.ellipse([990,y+60,1050,y+120],fill=col+(255,))
        txt(C,title,BOLD(52),y+35,col,255,x=1080,anchor='l'); txt(C,sub,REG(36),y+110,white,255,x=1080,anchor='l')
        fr=pop(fr,C,(955,y-5,1645,y+185),back((t-t0)/0.4))
    if t>fs[2]/30-4.0:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'SO YOUR SAVINGS KEEP UP WITH RISING PRICES',880,col=gold,alpha=255*ease((t-(fs[2]/30-4.0))/0.4),size=40); fr=Image.alpha_composite(fr,L)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'Example for illustration only · not personal advice',REG(24),985,grey,200); fr=Image.alpha_composite(fr,L)
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2]
for i,(fn,f) in enumerate(zip([drawA,drawB],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b15-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y15{i}.png')
