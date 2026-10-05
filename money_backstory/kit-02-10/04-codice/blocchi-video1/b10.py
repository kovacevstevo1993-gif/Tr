from common import *
import shutil
S=["Trap number three: spousal benefits stop growing at full retirement age.","A spouse can receive up to half of the worker's full benefit.","But waiting past full retirement age adds nothing to a spousal benefit.","So a spouse who will only receive a spousal benefit usually has no reason to wait past full retirement age."]
TOTF=641
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1]); print(fs,sum(fs))
bg=make_bg(); bgg=make_bg(grid=True)
def person(d,cx,cy,col,s=1):
    d.ellipse([cx-40*s,cy-120*s,cx+40*s,cy-40*s],fill=col); d.rounded_rectangle([cx-70*s,cy-25*s,cx+70*s,cy+100*s],radius=int(50*s),fill=col)
def drawA(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); a=ease(t/0.4)
    txt(L,'TRAP #3',BOLD(140),170,red,255*a)
    fr=Image.alpha_composite(fr,L)
    if t>0.7:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cd.rounded_rectangle([W/2-600,450,W/2+600,650],radius=40,fill=card+(255,),outline=gold+(255,),width=4)
        txt(C,'SPOUSAL BENEFITS STOP GROWING',BOLD(60),480,white); txt(C,'AT FULL RETIREMENT AGE',BOLD(48),570,gold)
        fr=pop(fr,C,(int(W/2-605),445,int(W/2+605),655),back((t-0.7)/0.45))
    return fr
def drawB(t):
    fr=bgg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); a=ease(t/0.4)
    txt(L,'THE SPOUSAL BENEFIT',SER(72),110,goldL,255*a)
    person(d,W/2-420,470,white+(int(255*a),),1.3); txt(L,'WORKER',BOLD(44),640,white,255*a,x=W/2-420); txt(L,'$2,000',BOLD(90),710,white,255*a,x=W/2-420)
    fr=Image.alpha_composite(fr,L)
    if t>1.0:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); p=ease((t-1.0)/0.6); x0,x1=W/2-230,W/2+230
        d.line([x0,470,x0+(x1-x0)*p,470],fill=gold+(255,),width=12)
        if p>0.95: d.polygon([(x1,470),(x1-40,445),(x1-40,495)],fill=gold+(255,))
        txt(L,'UP TO 50%',BOLD(48),390,gold,255*p); fr=Image.alpha_composite(fr,L)
    if t>1.8:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); p=ease((t-1.8)/0.5)
        person(d,W/2+420,470,gold+(int(255*p),),1.3); txt(L,'SPOUSE',BOLD(44),640,gold,255*p,x=W/2+420)
        v=int(1000*ease((t-2.0)/1.2)); txt(L,f'${v:,}',BOLD(90),710,gold,255*p,x=W/2+420); fr=Image.alpha_composite(fr,L)
    return fr
def drawC(t):
    fr=bgg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'WAITING PAST 67 ADDS NOTHING',SER(66),90,goldL,255*ease(t/0.4))
    base=860; d.line([260,base,W-260,base],fill=gold+(255,),width=4)
    fr=Image.alpha_composite(fr,L)
    for i,age in enumerate([67,68,69,70]):
        st=0.4+i*0.35; p=ease((t-st)/0.5)
        if p<=0: continue
        x=W/2+(i-1.5)*330; im=bar(300*p,gold,220); fr.alpha_composite(im,(int(x-110),base-im.height))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'$1,000',BOLD(60),base-im.height-90,gold,255*p,x=x); txt(L,f'AGE {age}',BOLD(38),base+22,white,255*p,x=x)
        if i>0: txt(L,'+0%',BOLD(36),base-im.height+20,navy,255*p,x=x)
        fr=Image.alpha_composite(fr,L)
    return fr
def drawD(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); a=ease(t/0.4)
    txt(L,'ONLY GETTING A SPOUSAL BENEFIT?',SER(70),220,white,255*a); fr=Image.alpha_composite(fr,L)
    if t>1.2:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(64); lab='NO REASON TO WAIT PAST 67'; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+110; bx=(W-bw)/2; y=460
        cd.rounded_rectangle([bx,y,bx+bw,y+140],radius=70,fill=gold+(255,)); cd.text((bx+55-b[0],y+70-(b[3]-b[1])/2-b[1]),lab,font=f,fill=navy+(255,))
        fr=pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,y+145),back((t-1.2)/0.45))
    if t>2.4:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'(usually)',REG(44),660,grey,255*ease((t-2.4)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD],fs),1):
    render(fn,f/30,f'/mnt/user-data/outputs/v1-b10-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/x10{i}.png')
