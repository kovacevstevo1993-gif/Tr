from common2 import *
import shutil, sys
S=["Mistake number one: planning for the wrong number of years.","Most people plan their retirement as if it will last fifteen or twenty years.","But according to the Social Security Administration, about one in four sixty five year olds today will live past ninety.","And about one in ten will live past ninety five.","That means your money may need to last thirty years or more.","And women, on average, live even longer than men, which makes this mistake even more dangerous for a surviving wife."]
TOTF=979
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0],fs[1],fs[2]+fs[3],fs[4],fs[5]]; print(fs,durs,sum(durs)); s4=fs[2]/30
pink=(230,140,190)
def person(d,cx,cy,col,s=1.0):
    d.ellipse([cx-18*s,cy-52*s,cx+18*s,cy-16*s],fill=col); d.rounded_rectangle([cx-30*s,cy-10*s,cx+30*s,cy+46*s],radius=int(22*s),fill=col)
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    a=ease(t/0.35); txt(L,'MISTAKE #1',BOLD(110),170,gold,255*a)
    cx,cy=W/2,520; f=(t*0.5)%1
    d.polygon([(cx-80,cy-110),(cx+80,cy-110),(cx,cy)],outline=gold+(255,),width=6); d.polygon([(cx-80,cy+110),(cx+80,cy+110),(cx,cy)],outline=gold+(255,),width=6)
    d.polygon([(cx-80*(1-f),cy-110+110*f),(cx+80*(1-f),cy-110+110*f),(cx,cy)],fill=gold+(255,))
    d.polygon([(cx-80*f,cy+110-60*f),(cx+80*f,cy+110-60*f),(cx+80,cy+110),(cx-80,cy+110)],fill=gold+(255,))
    d.line([cx,cy,cx,cy+110],fill=goldL+(200,),width=3)
    txt(L,'PLANNING FOR THE WRONG NUMBER OF YEARS',BOLD(50),720,white,255*ease((t-0.3)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
def timeline(d,L,y,a0,a1,col,label,p,x0=260,x1=1660,alpha=255):
    def ax(a): return x0+(a-65)/(100-65)*(x1-x0)
    xe=ax(a0)+(ax(a1)-ax(a0))*p
    d.rounded_rectangle([ax(a0),y,xe,y+70],radius=35,fill=col+(alpha,))
    if p>0.9: txt(L,label,BOLD(40),y+14,navy,255,x=(ax(a0)+xe)/2)
    return ax
def axis(d,L,y,x0=260,x1=1660):
    d.line([x0,y,x1,y],fill=gold+(255,),width=3)
    for a in range(65,101,5):
        x=x0+(a-65)/(35)*(x1-x0); d.line([x,y-8,x,y+8],fill=gold+(255,),width=3); txt(L,str(a),REG(30),y+18,grey,255,x=x)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'WHAT MOST PEOPLE PLAN FOR',SER(66),120,goldL,255*ease(t/0.4))
    axis(d,L,760)
    p=ease((t-0.4)/1.4); timeline(d,L,470,65,85,grey,'15-20 YEARS',p)
    txt(L,'retire at 65  →  money lasts until ~85',REG(36),600,white,255*ease((t-1.6)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'HOW LONG 65-YEAR-OLDS REALLY LIVE',SER(58),100,goldL,255*ease(t/0.4))
    # row 1: 1 in 4
    a=ease((t-0.3)/0.5)
    for k in range(4):
        col=gold if k==0 else (90,110,140); person(d,420+k*120,360,col+(int(255*a),),1.3)
    if t>1.2:
        txt(L,'1 IN 4',BOLD(80),300,gold,255*ease((t-1.2)/0.4),x=1100,anchor='l'); txt(L,'will live past 90',REG(40),395,white,255*ease((t-1.2)/0.4),x=1100,anchor='l')
    if t>s4:
        b=ease((t-s4)/0.5)
        for k in range(10):
            col=red if k==0 else (90,110,140); person(d,300+k*75,700,col+(int(255*b),),0.95)
        txt(L,'1 IN 10',BOLD(80),640,red,255*b,x=1100,anchor='l'); txt(L,'will live past 95',REG(40),735,white,255*b,x=1100,anchor='l')
    txt(L,'Source: Social Security Administration',REG(26),985,grey,200)
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawD(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'YOUR MONEY MAY NEED TO LAST',SER(66),110,goldL,255*ease(t/0.4))
    axis(d,L,800)
    timeline(d,L,400,65,85,grey,'WHAT YOU PLANNED',1.0,alpha=160)
    p=ease((t-0.4)/1.6); timeline(d,L,560,65,95,gold,'30+ YEARS',p)
    if p>0.95:
        x85=260+(85-65)/35*1400; x95=260+(95-65)/35*1400
        d.rounded_rectangle([x85,540,x95,650],radius=20,outline=red+(255,),width=5)
        txt(L,'UNFUNDED?',BOLD(40),670,red,255*ease((t-2.1)/0.4),x=(x85+x95)/2)
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawE(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'WOMEN LIVE LONGER ON AVERAGE',SER(64),110,goldL,255*ease(t/0.4))
    x0,x1=640,1640
    def ax(a): return x0+(a-65)/(95-65)*(x1-x0)
    for i,(lab,age,col,st) in enumerate([('MEN',84,blue,0.3),('WOMEN',87,pink,0.9)]):
        p=ease((t-st)/1.2)
        if p<=0: continue
        y=300+i*190; person(d,300,y+50,col+(255,),1.3); txt(L,lab,BOLD(44),y+28,col,255,x=390,anchor='l')
        xe=x0+(ax(age)-x0)*p; d.rounded_rectangle([x0,y,xe,y+100],radius=24,fill=col+(255,)); txt(L,f'~{int(65+(age-65)*p)}',BOLD(64),y+14,navy,255,x=max(x0+90,xe-90))
    if t>3.0:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(44); lab='THE BIGGEST RISK: A SURVIVING WIFE'; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+80; bx=(W-bw)/2; y=760
        cd.rounded_rectangle([bx,y,bx+bw,y+96],radius=48,fill=red+(255,)); cd.text((bx+40-b[0],y+48-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(255,255,255,255))
        fr=Image.alpha_composite(fr,L); L=Image.new('RGBA',(W,H),(0,0,0,0)); fr=pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,y+101),back((t-3.0)/0.45))
    txt(L,'Life expectancy at 65 · Source: Social Security Administration',REG(26),985,grey,200)
    fr=Image.alpha_composite(fr,L); return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3,4,5]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD,drawE],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b3-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y3{i}.png')
