from common2 import *
import shutil, sys
S=["Mistake number four: counting on Medicare for long term care.","According to the Department of Health and Human Services, someone turning sixty five today has almost a seventy percent chance of needing some type of long term care.","That means help with daily activities, like bathing, dressing, or eating."]
TOTF=616
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1]); print(fs,sum(fs))
purple=(170,130,230)
def person(d,cx,cy,col,s=1.0):
    d.ellipse([cx-18*s,cy-52*s,cx+18*s,cy-16*s],fill=col); d.rounded_rectangle([cx-30*s,cy-10*s,cx+30*s,cy+46*s],radius=int(22*s),fill=col)
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'MISTAKE #4',BOLD(120),170,purple,255*ease(t/0.35))
    cx,cy=W/2,520; s=1+0.04*math.sin(t*4)
    d.rounded_rectangle([cx-110*s,cy-50*s,cx+110*s,cy+50*s],radius=14,fill=blue+(255,)); txt(L,'MEDICARE',BOLD(34),cy-20,(255,255,255),255,x=cx)
    d.line([cx-150,cy-90,cx+150,cy+90],fill=red+(230,),width=14)
    txt(L,'COUNTING ON MEDICARE FOR LONG-TERM CARE',BOLD(52),700,white,255*ease((t-0.3)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'TURNING 65 TODAY?',SER(70),110,goldL,255*ease(t/0.4))
    for k in range(10):
        st=0.4+k*0.18; a=ease((t-st)/0.3)
        if a<=0: continue
        on=k<7 and t>st+0.6+0.1*k
        col=purple if on else (90,110,140)
        person(d,370+k*130,470,col+(int(255*a),),1.6)
    fr=Image.alpha_composite(fr,L)
    if t>3.2:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); p=ease((t-3.2)/1.0)
        txt(L,f'~{int(70*p)}%',BOLD(130),600,purple,255,x=W/2-300); txt(L,'will need some type of',REG(40),640,white,255*p,x=W/2-60,anchor='l'); txt(L,'LONG-TERM CARE',BOLD(56),695,white,255*p,x=W/2-60,anchor='l')
        txt(L,'Source: U.S. Department of Health and Human Services',REG(26),985,grey,200)
        fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'HELP WITH DAILY ACTIVITIES',SER(66),110,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    items=[('BATHING',blue),('DRESSING',gold),('EATING',green)]
    for k,(lab,col) in enumerate(items):
        st=0.5+k*0.9
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=W/2+(k-1)*520; y=540+math.sin(t*2+k)*6
        cd.rounded_rectangle([x-220,y-230,x+220,y+230],radius=34,fill=card+(255,),outline=col+(255,),width=5)
        c=col+(255,)
        if k==0:
            cd.polygon([(x,y-150),(x-70,y-20),(x+70,y-20)],fill=c); cd.ellipse([x-70,y-90,x+70,y+50],fill=c)
        elif k==1:
            cd.polygon([(x-110,y-120),(x-40,y-150),(x,y-110),(x+40,y-150),(x+110,y-120),(x+80,y-60),(x+55,y-75),(x+55,y+50),(x-55,y+50),(x-55,y-75),(x-80,y-60)],fill=c)
        else:
            cd.ellipse([x-100,y-130,x+100,y+70],outline=c,width=12)
            cd.rounded_rectangle([x-150,y-130,x-135,y+60],radius=6,fill=c); cd.rounded_rectangle([x+135,y-130,x+150,y+60],radius=6,fill=c)
        txt(C,lab,BOLD(56),y+120,white,255,x=x)
        fr=pop(fr,C,(int(x-225),int(y-235),int(x+225),int(y+235)),back((t-st)/0.45))
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],fs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b17-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y17{i}.png')
