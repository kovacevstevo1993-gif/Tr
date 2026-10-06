from common import *
import shutil
S=["And what if you already claimed, and now you regret it?","There are two little known escape doors.","First, if you claimed less than twelve months ago, you can withdraw your application.","You have to pay back what you received, but then it's as if you never claimed, and your future check can keep growing.","Second, once you reach full retirement age, you can ask Social Security to suspend your benefits.","Your check stops for a while, but it grows eight percent for every year of suspension, up to age 70."]
TOTF=1036
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
groups=[[0,1],[2],[3],[4],[5]]; durs=[sum(fs[i] for i in g) for g in groups]; print(fs,durs,sum(durs))
s2=fs[0]/30
bg=make_bg(); bgg=make_bg(grid=True)
def door(d,cx,cy,col,open_=0.0,s=1.0):
    w,h=150*s,260*s
    d.rounded_rectangle([cx-w/2-14,cy-h/2-14,cx+w/2+14,cy+h/2],radius=12,outline=col+(255,),width=10)
    dw=w*(1-0.6*open_); d.rectangle([cx-w/2,cy-h/2,cx-w/2+dw,cy+h/2],fill=col+(255,))
    d.ellipse([cx-w/2+dw-30,cy-6,cx-w/2+dw-14,cy+10],fill=navy+(255,))
def drawA(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'ALREADY CLAIMED?',SER(90),170,white,255*ease(t/0.4))
    txt(L,'AND NOW YOU REGRET IT?',BOLD(52),310,red,255*ease((t-1.2)/0.4)); fr=Image.alpha_composite(fr,L)
    if t>s2:
        for i in range(2):
            st=s2+i*0.4
            if t<st: continue
            C=Image.new('RGBA',(W,H),(0,0,0,0)); x=W/2+(i*2-1)*220; door(ImageDraw.Draw(C),x,620,gold,ease((t-st-0.4)/0.8))
            fr=pop(fr,C,(int(x-110),460,int(x+110),760),back((t-st)/0.45))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'2 LITTLE-KNOWN ESCAPE DOORS',BOLD(52),830,gold,255*ease((t-s2-0.3)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
def drawB(t):
    fr=bgg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'DOOR 1',BOLD(64),90,gold,255*ease(t/0.4)); txt(L,'WITHDRAW YOUR APPLICATION',SER(72),190,white,255*ease((t-0.3)/0.4))
    fr=Image.alpha_composite(fr,L)
    for m in range(12):
        st=0.6+m*0.12
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=W/2+((m%6)-2.5)*200; y=420+(m//6)*190
        cd.rounded_rectangle([x-80,y-70,x+80,y+70],radius=16,fill=card+(255,),outline=green+(255,),width=3); txt(C,str(m+1),BOLD(64),y-38,green,255,x=x)
        fr=pop(fr,C,(int(x-85),y-75,int(x+85),y+75),back((t-st)/0.35))
    if t>2.4:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'ONLY WITHIN 12 MONTHS OF CLAIMING',840,col=green,alpha=255*ease((t-2.4)/0.4),size=46); fr=Image.alpha_composite(fr,L)
    return fr
def drawC(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'PAY BACK WHAT YOU RECEIVED',BOLD(60),170,red,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    if t>1.8:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx,cy,r=W/2,500,120; p=ease((t-1.8)/1.0)
        cd.arc([cx-r,cy-r,cx+r,cy+r],start=90,end=90+300*p,fill=gold+(255,),width=24)
        if p>0.95:
            ang=math.radians(90+300); ex,ey=cx+r*math.cos(ang),cy+r*math.sin(ang); cd.polygon([(ex+30,ey+14),(ex-20,ey-30),(ex-14,ey+36)],fill=gold+(255,))
        txt(C,'RESET',BOLD(46),cy-26,gold); fr=Image.alpha_composite(fr,C)
    if t>2.6:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,"...AND IT'S AS IF YOU NEVER CLAIMED",SER(64),700,white,255*ease((t-2.6)/0.4)); fr=Image.alpha_composite(fr,L)
    if t>5.2:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'YOUR FUTURE CHECK KEEPS GROWING',840,col=green,alpha=255*ease((t-5.2)/0.4),size=46); fr=Image.alpha_composite(fr,L)
    return fr
def drawD(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0))
    txt(L,'DOOR 2',BOLD(64),90,gold,255*ease(t/0.4)); txt(L,'SUSPEND YOUR BENEFITS',SER(80),190,white,255*ease((t-0.3)/0.4)); fr=Image.alpha_composite(fr,L)
    if t>0.8:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx,cy=W/2,540; r=150
        cd.ellipse([cx-r,cy-r,cx+r,cy+r],fill=gold+(255,)); cd.rounded_rectangle([cx-60,cy-70,cx-18,cy+70],radius=8,fill=navy+(255,)); cd.rounded_rectangle([cx+18,cy-70,cx+60,cy+70],radius=8,fill=navy+(255,))
        fr=pop(fr,C,(int(cx-r-5),int(cy-r-5),int(cx+r+5),int(cy+r+5)),back((t-0.8)/0.45))
    if t>1.4:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'ONCE YOU REACH FULL RETIREMENT AGE',790,alpha=255*ease((t-1.4)/0.4),size=46); fr=Image.alpha_composite(fr,L)
    return fr
def drawE(t):
    fr=bgg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'+8% FOR EVERY YEAR OF SUSPENSION',SER(64),90,goldL,255*ease(t/0.4))
    base=860; d.line([260,base,W-260,base],fill=gold+(255,),width=4); fr=Image.alpha_composite(fr,L)
    vals=[2000,2160,2320,2480]
    for i,(age,v) in enumerate(zip([67,68,69,70],vals)):
        st=0.8+i*0.9; p=ease((t-st)/0.7)
        if p<=0: continue
        x=W/2+(i-1.5)*330; col=[white,(170,215,180),(120,205,150),green][i]; im=bar(v/2480*480*p,col,220); fr.alpha_composite(im,(int(x-110),base-im.height))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,f'${int(v*p/10)*10:,}',BOLD(62),base-im.height-90,green if i==3 else white,255*p,x=x); txt(L,f'AGE {age}',BOLD(38),base+22,white,255*p,x=x)
        fr=Image.alpha_composite(fr,L)
    if t>4.6:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'UP TO AGE 70',960,col=green,alpha=255*ease((t-4.6)/0.4),size=40); fr=Image.alpha_composite(fr,L)
    return fr
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD,drawE],durs),1):
    render(fn,f/30,f'/mnt/user-data/outputs/v1-b12-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/x12{i}.png')
