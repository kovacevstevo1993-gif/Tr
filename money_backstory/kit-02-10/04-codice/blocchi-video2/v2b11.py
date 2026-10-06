from common2 import *
import shutil, sys
S=["So when you plan your retirement budget, give health care its own line.","Don't hide it inside everyday expenses.","Because health care costs have historically grown faster than general inflation.","And that leads us to the mistake that surprises almost everyone."]
TOTF=484
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0]+fs[1],fs[2],fs[3]]; print(fs,durs,sum(durs)); s2=fs[0]/30
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'YOUR RETIREMENT BUDGET',SER(66),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x0,x1,y0=W/2-520,W/2+520,220
    cd.rounded_rectangle([x0,y0,x1,y0+700],radius=24,fill=(240,236,225,255))
    rows=['Housing','Food','Transportation','Travel & fun']
    for k,r in enumerate(rows):
        yy=y0+50+k*95; txt(C,r,REG(40),yy,navy,255,x=x0+60,anchor='l'); cd.line([x0+60,yy+70,x1-60,yy+70],fill=(190,185,170,255),width=2)
    fr=Image.alpha_composite(fr,C)
    if t>0.8:
        p=back((t-0.8)/0.45); C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); yy=y0+50+4*95
        cd.rounded_rectangle([x0+40,yy-15,x1-40,yy+95],radius=20,fill=blue+(255,)); txt(C,'HEALTH CARE — ITS OWN LINE',BOLD(44),yy+14,(255,255,255),255,x=W/2)
        G=C.filter(ImageFilter.GaussianBlur(18)); fr=pop(fr,G,(int(x0)+30,yy-30,int(x1)-30,yy+110),p); fr=pop(fr,C,(int(x0)+30,yy-30,int(x1)-30,yy+110),p)
    if t>s2:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(42); lab="DON'T HIDE IT IN EVERYDAY EXPENSES"; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+80; bx=(W-bw)/2; y=y0+610
        cd.rounded_rectangle([bx,y,bx+bw,y+84],radius=42,fill=red+(255,)); cd.text((bx+40-b[0],y+42-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(255,255,255,255))
        fr=pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,y+89),back((t-s2)/0.4))
    return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'HEALTH CARE COSTS VS GENERAL INFLATION',SER(56),100,goldL,255*ease(t/0.4))
    X0,X1,Y0,Y1=300,1620,860,260
    d.line([X0,Y0,X1,Y0],fill=gold+(255,),width=3); d.line([X0,Y0,X0,Y1],fill=gold+(255,),width=3)
    txt(L,'TIME →',BOLD(28),Y0+18,grey,255,x=X1,anchor='r'); txt(L,'COST',BOLD(28),Y1-40,grey,255,x=X0,anchor='l')
    p=ease((t-0.3)/2.4); n=int(p*100)
    ptsI=[(X0+(X1-X0)*k/100, Y0-(Y0-Y1)*0.45*(k/100)**1.2) for k in range(n+1)]
    ptsH=[(X0+(X1-X0)*k/100, Y0-(Y0-Y1)*0.95*(k/100)**1.35) for k in range(n+1)]
    if len(ptsI)>1:
        d.line(ptsI,fill=grey+(255,),width=7); d.line(ptsH,fill=red+(255,),width=9)
    if p>0.95:
        txt(L,'HEALTH CARE',BOLD(38),ptsH[-1][1]-20,red,255,x=X1-20,anchor='r'); txt(L,'GENERAL INFLATION',BOLD(34),ptsI[-1][1]-60,grey,255,x=X1-20,anchor='r')
    txt(L,'Illustration of the historical trend',REG(26),985,grey,200)
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'NEXT: THE MISTAKE THAT',BOLD(46),230,white,255*ease(t/0.35)); txt(L,'SURPRISES ALMOST EVERYONE',BOLD(58),300,red,255*ease((t-0.3)/0.35)); fr=Image.alpha_composite(fr,L)
    C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx,cy=W/2,640; s=1+0.04*math.sin(t*5)
    cd.rounded_rectangle([cx-180*s,cy-180*s,cx+180*s,cy+180*s],radius=40,fill=card+(255,),outline=red+(255,),width=8)
    txt(C,'#3',BOLD(int(170*s)),cy-150*s,red,255,x=cx)
    cd.rounded_rectangle([cx-40,cy+70,cx+40,cy+140],radius=10,fill=gold+(255,)); cd.arc([cx-30,cy+30,cx+30,cy+90],180,360,fill=gold+(255,),width=10)
    fr=pop(fr,C,(int(cx-200),int(cy-200),int(cx+200),int(cy+200)),back((t-0.2)/0.45))
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b11-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y11{i}.png')
