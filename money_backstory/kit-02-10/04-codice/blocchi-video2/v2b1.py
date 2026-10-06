from common2 import *
import shutil
S=["A sixty five year old retiring today may need one hundred eighty five thousand dollars just for health care.","Most Americans expect less than half of that.","And that's only one of five quiet mistakes that ruin retirements, not with one big disaster, but little by little, until it's too late to fix them.","Today, you'll see all five, with real numbers from Fidelity, Medicare and Social Security.","And pay close attention to mistake number three.","It's the one that feels the safest, and it surprises almost everyone."]
TOTF=1096
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0],fs[1],fs[2],fs[3],fs[4]+fs[5]]; print(fs,durs,sum(durs)); s6=fs[4]/30
def src(L,text,y=985):
    txt(L,text,REG(26),y,grey,200)
# A: big number + line chart of Fidelity estimates
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    a=ease(t/0.4); txt(L,'HEALTH CARE IN RETIREMENT',BOLD(40),110,goldL,255*a)
    p=ease((t-0.2)/1.8); v=int(185500*p/100)*100
    G=Image.new('RGBA',(W,H),(0,0,0,0)); txt(G,f'${v:,}',BOLD(170),170,red,200); fr=Image.alpha_composite(fr,L); fr=Image.alpha_composite(fr,G.filter(ImageFilter.GaussianBlur(26)))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); txt(L,f'${v:,}',BOLD(170),170,red); txt(L,'per person, age 65, after taxes',REG(34),370,white,255*a)
    # chart
    X0,X1,Y0,Y1=300,1620,900,470
    d.line([X0,Y0,X1,Y0],fill=gold+(255,),width=3)
    for gv in [50000,100000,150000,200000]:
        y=Y0-(gv/200000)*(Y0-Y1); d.line([X0,y,X1,y],fill=(255,255,255,18),width=2); txt(L,f'${gv//1000}K',REG(24),y-12,grey,220,x=X0-15,anchor='r')
    pts=[(2002,80000),(2024,165000),(2025,172500),(2026,185500)]
    def P(yr,val): return (X0+(yr-2002)/(2026-2002)*(X1-X0), Y0-(val/200000)*(Y0-Y1))
    q=ease((t-0.6)/2.2); seg=[P(*pts[0])]
    total=len(pts)-1; prog=q*total
    for k in range(1,len(pts)):
        if prog>=k: seg.append(P(*pts[k]))
        elif prog>k-1:
            f=prog-(k-1); a1=P(*pts[k-1]); b1=P(*pts[k]); seg.append((a1[0]+(b1[0]-a1[0])*f,a1[1]+(b1[1]-a1[1])*f)); break
    if len(seg)>1: d.line(seg,fill=red+(255,),width=8,joint='curve')
    for k,(yr,val) in enumerate(pts):
        if prog>=k:
            x,y=P(yr,val); d.ellipse([x-10,y-10,x+10,y+10],fill=goldL+(255,))
            if yr in (2002,2026):
                lab='$80,000' if yr==2002 else '$185,500'
                txt(L,lab,BOLD(34),y-60,white,255,x=x+(60 if yr==2002 else -40)); txt(L,str(yr),REG(28),Y0+14,grey,255,x=x)
    src(L,'Source: Fidelity Retiree Health Care Cost Estimate 2026')
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'EXPECTATION VS REALITY',SER(66),100,goldL,255*ease(t/0.4))
    base_=850; d.line([400,base_,1520,base_],fill=gold+(255,),width=4); fr=Image.alpha_composite(fr,L)
    for i,(lab,val,col,st) in enumerate([('WHAT AMERICANS EXPECT',75000,blue,0.2),('FIDELITY ESTIMATE',185500,red,0.6)]):
        p=ease((t-st)/1.0)
        if p<=0: continue
        x=W/2+(i*2-1)*280; h=val/185500*520*p; im=bar(h,col,260); fr.alpha_composite(im,(int(x-130),int(base_-im.height)))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,f'${int(val*p/100)*100:,}',BOLD(64),base_-im.height-85,col,255,x=x); txt(L,lab,BOLD(32),base_+20,white,255,x=x); fr=Image.alpha_composite(fr,L)
    if t>1.4:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(44); lab='LESS THAN HALF'; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+70; bx=W/2-bw/2-280; y=420
        cd.rounded_rectangle([bx,y,bx+bw,y+84],radius=42,fill=gold+(255,)); cd.text((bx+35-b[0],y+42-(b[3]-b[1])/2-b[1]),lab,font=f,fill=navy+(255,))
        fr=pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,y+89),back((t-1.4)/0.4))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); src(L,'Source: Fidelity research'); fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'5 QUIET MISTAKES',SER(72),100,goldL,255*ease(t/0.4)); txt(L,'not one big disaster... little by little',REG(36),200,white,255*ease((t-0.3)/0.4))
    X0,X1,Y0,Y1=260,1660,860,330
    d.line([X0,Y0,X1,Y0],fill=gold+(255,),width=3); txt(L,'YOUR SAVINGS',BOLD(28),Y1-95,grey,255,x=X0,anchor='l')
    fr=Image.alpha_composite(fr,L)
    q=ease((t-0.5)/(durs[2]/30-1.2))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    N=int(q*100); pts=[]
    for k in range(N+1):
        x=X0+(X1-X0)*k/100; y=Y1+(Y0-Y1-30)*(k/100)**1.6+math.sin(k*0.5)*6; pts.append((x,y))
    if len(pts)>1:
        poly=pts+[(pts[-1][0],Y0),(X0,Y0)]; A=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(A).polygon(poly,fill=red+(45,)); fr=Image.alpha_composite(fr,A)
        d.line(pts,fill=red+(255,),width=7)
    for m in range(5):
        k=12+m*20
        if N>=k:
            x,y=pts[k]; d.ellipse([x-18,y-18,x+18,y+18],fill=red+(255,),outline=white+(255,),width=3); txt(L,f'#{m+1}',BOLD(30),y-65,white,255,x=x)
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawD(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'REAL NUMBERS FROM',SER(70),160,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    names=['FIDELITY','MEDICARE','SOCIAL SECURITY']
    for i,n in enumerate(names):
        st=0.4+i*0.6
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=W/2+(i-1)*520; y=520+math.sin(t*2+i)*6
        cd.rounded_rectangle([x-230,y-150,x+230,y+150],radius=30,fill=card+(255,),outline=gold+(255,),width=4)
        cd.ellipse([x-45,y-110,x+45,y-20],fill=green+(255,)); cd.line([(x-22,y-65),(x-6,y-47),(x+24,y-82)],fill=navy+(255,),width=12,joint='curve')
        txt(C,n,BOLD(40 if len(n)<10 else 36),y+30,white,255,x=x); txt(C,'official data',REG(28),y+85,grey,255,x=x)
        fr=pop(fr,C,(int(x-235),int(y-155),int(x+235),int(y+155)),back((t-st)/0.45))
    return frame(fr)
def drawE(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'PAY CLOSE ATTENTION TO...',SER(66),130,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    for i in range(5):
        st=0.2+i*0.15
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=W/2+(i-2)*290
        big=(i==2 and t>0.9); sc=1.25 if big else 1.0; y=500+math.sin(t*2.2+i)*7
        r=110*sc; col=red if i==2 else (gold if not big else (120,110,90))
        cd.rounded_rectangle([x-r,y-r,x+r,y+r],radius=28,fill=card+(255,),outline=col+(255,),width=7 if i==2 else 4)
        txt(C,f'#{i+1}',BOLD(int(90*sc)),y-r*0.55,col,255 if (i==2 or not big) else 120,x=x)
        if i==2: 
            # lock icon
            cd.rounded_rectangle([x-30,y+55,x+30,y+100],radius=8,fill=gold+(255,)); cd.arc([x-22,y+25,x+22,y+65],180,360,fill=gold+(255,),width=8)
        fr=pop(fr,C,(int(x-r-10),int(y-r-10),int(x+r+10),int(y+r+10)),back((t-st)/0.4))
    if t>s6:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'IT FEELS THE SAFEST',760,col=gold,alpha=255*ease((t-s6)/0.4),size=46); fr=Image.alpha_composite(fr,L)
    if t>s6+1.8:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'...AND SURPRISES ALMOST EVERYONE',860,col=red,alpha=255*ease((t-s6-1.8)/0.4),size=42); fr=Image.alpha_composite(fr,L)
    return frame(fr)
import sys
sel=[int(x) for x in sys.argv[1:]] or [1,2,3,4,5]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD,drawE],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b1-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y1{i}.png')
