from common import *
import shutil
S=["And who should wait?","If you're healthy, if long life runs in your family, if you're married and you're the higher earner, or if you can live on savings or work income for a few more years, waiting is often the bigger payoff.","Remember, every year you wait after 67 adds eight percent to your check, for life.","Very few investments can promise that."]
TOTF=735
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1]); print(fs,sum(fs))
bg=make_bg()
def drawA(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'AND WHO SHOULD WAIT?',SER(100),420,green,255*ease(t/0.3)); fr=Image.alpha_composite(fr,L); return fr
def drawB(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'WAITING IS OFTEN THE BIGGER PAYOFF IF...',SER(60),80,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    D=fs[1]/30
    items=[("YOU'RE HEALTHY",0.2),('LONG LIFE RUNS IN YOUR FAMILY',D*0.12),("YOU'RE MARRIED AND THE HIGHER EARNER",D*0.3),('YOU CAN LIVE ON SAVINGS OR WORK A FEW MORE YEARS',D*0.52)]
    for i,(lab,st) in enumerate(items):
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); y=220+i*190
        cd.rounded_rectangle([160,y,W-160,y+150],radius=30,fill=card+(255,),outline=green+(255,),width=4)
        cx,cy=250,y+75; cd.ellipse([cx-45,cy-45,cx+45,cy+45],fill=green+(255,)); cd.line([(cx-22,cy),(cx-5,cy+18),(cx+24,cy-18)],fill=navy+(255,),width=12,joint='curve')
        txt(C,lab,BOLD(46),y+52,white,255,x=330,anchor='l')
        fr=pop(fr,C,(155,y-5,W-155,y+155),back((t-st)/0.45))
    return fr
def drawC(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'EVERY YEAR YOU WAIT AFTER 67',SER(70),120,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    s=back((t-0.5)/0.5)
    if t>0.5:
        S2=Image.new('RGBA',(W,H),(0,0,0,0)); txt(S2,'+8%',BOLD(300),290,green)
        fr=pop(fr,S2.filter(ImageFilter.GaussianBlur(28)),(560,270,1360,640),s); fr=pop(fr,S2,(560,270,1360,640),s)
    if t>2.2:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(64); lab='TO YOUR CHECK — FOR LIFE'; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+110; bx=(W-bw)/2; y=720
        cd.rounded_rectangle([bx,y,bx+bw,y+130],radius=65,fill=green+(255,)); cd.text((bx+55-b[0],y+65-(b[3]-b[1])/2-b[1]),lab,font=f,fill=navy+(255,))
        fr=pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,y+135),back((t-2.2)/0.45))
    return fr
def drawD(t):
    fr=bg.copy()
    S2=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(S2); cx,cy=W/2,420
    d.polygon([(cx,cy-190),(cx+170,cy-120),(cx+150,cy+80),(cx,cy+200),(cx-150,cy+80),(cx-170,cy-120)],fill=gold+(255,))
    txt(S2,'8%',BOLD(120),cy-70,navy)
    fr=pop(fr,S2,(int(cx-175),int(cy-195),int(cx+175),int(cy+205)),back(t/0.45))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'VERY FEW INVESTMENTS CAN PROMISE THAT',SER(72),720,white,255*ease((t-0.4)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD],fs),1):
    render(fn,f/30,f'/mnt/user-data/outputs/v1-b14-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/x14{i}.png')
