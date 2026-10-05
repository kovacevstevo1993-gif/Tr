from common2 import *
import shutil, sys
S=["There is one tool that can really help here, if you're still working and have a qualifying high deductible health plan: a health savings account, or HSA.","In 2026, you can put in up to four thousand four hundred dollars for yourself, or eight thousand seven hundred fifty for a family, plus an extra thousand dollars if you're fifty five or older.","The money goes in tax free, grows tax free, and comes out tax free for medical expenses."]
TOTF=898
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1]); print(fs,sum(fs))
def check(d,cx,cy,col):
    d.ellipse([cx-30,cy-30,cx+30,cy+30],fill=col+(255,)); d.line([(cx-14,cy),(cx-3,cy+12),(cx+16,cy-12)],fill=navy+(255,),width=8,joint='curve')
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'ONE TOOL THAT CAN REALLY HELP',SER(64),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    D=fs[0]/30
    # conditions (first half of sentence)
    for k,lab in enumerate(["YOU'RE STILL WORKING","YOU HAVE A QUALIFYING HIGH-DEDUCTIBLE HEALTH PLAN"]):
        st=0.6+k*1.6
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); y=250+k*120
        cd.rounded_rectangle([250,y,W-250,y+95],radius=46,fill=card+(255,),outline=gold+(255,),width=3); check(cd,305,y+47,green)
        txt(C,'IF '+lab,BOLD(38),y+28,white,255,x=360,anchor='l')
        fr=pop(fr,C,(245,y-5,W-245,y+100),back((t-st)/0.4))
    if t>D*0.6:
        p=back((t-D*0.6)/0.5); C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx,cy=W/2,700
        cd.rounded_rectangle([cx-420,cy-120,cx+420,cy+140],radius=40,fill=green+(255,))
        txt(C,'HSA',BOLD(130),cy-110,navy,255,x=cx); txt(C,'HEALTH SAVINGS ACCOUNT',BOLD(40),cy+60,navy,255,x=cx)
        fr=pop(fr,C,(int(cx-425),cy-125,int(cx+425),cy+145),p)
    return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'2026 HSA CONTRIBUTION LIMITS',SER(64),100,goldL,255*ease(t/0.4))
    base_=840; d.line([380,base_,1540,base_],fill=gold+(255,),width=4); fr=Image.alpha_composite(fr,L)
    D=fs[1]/30
    bars=[('YOURSELF',4400,blue,0.3,W/2-300),('FAMILY',8750,green,D*0.35,W/2+300)]
    for lab,val,col,st,x in bars:
        p=ease((t-st)/1.2)
        if p<=0: continue
        h=val/9750*520*p; im=bar(h,col,260); fr.alpha_composite(im,(int(x-130),int(base_-im.height)))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,f'${int(val*p/10)*10:,}',BOLD(66),base_-(val+1000)/9750*520-100,col,255,x=x); txt(L,lab,BOLD(36),base_+20,white,255,x=x); fr=Image.alpha_composite(fr,L)
    if t>D*0.72:
        p=ease((t-D*0.72)/0.8)
        for x in [W/2-300,W/2+300]:
            val=4400 if x<W/2 else 8750; h0=val/9750*520; hh=1000/9750*520*p
            C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cd.rounded_rectangle([x-130,base_-h0-hh,x+130,base_-h0],radius=10,fill=gold+(255,),outline=goldL+(255,),width=3); fr=Image.alpha_composite(fr,C)
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'+ $1,000 EXTRA IF YOU ARE 55 OR OLDER',895,col=gold,alpha=255*p,size=40); fr=Image.alpha_composite(fr,L)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'Source: IRS',REG(26),975,grey,200); fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'THE TRIPLE TAX ADVANTAGE',SER(66),110,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    steps=[('GOES IN','TAX FREE'),('GROWS','TAX FREE'),('COMES OUT','TAX FREE*')]
    for k,(a,b) in enumerate(steps):
        st=0.3+k*1.3
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=W/2+(k-1)*520; y=520+math.sin(t*2+k)*6
        cd.rounded_rectangle([x-210,y-190,x+210,y+190],radius=34,fill=card+(255,),outline=green+(255,),width=5)
        txt(C,str(k+1),BOLD(80),y-170,green,255,x=x); txt(C,a,BOLD(50),y-50,white,255,x=x); txt(C,b,BOLD(52),y+40,green,255,x=x)
        fr=pop(fr,C,(int(x-215),int(y-195),int(x+215),int(y+195)),back((t-st)/0.45))
        if k<2 and t>st+0.4:
            A=Image.new('RGBA',(W,H),(0,0,0,0)); ad=ImageDraw.Draw(A); ax=x+230; ad.polygon([(ax,520-25),(ax+50,520),(ax,520+25)],fill=gold+(255,)); fr=Image.alpha_composite(fr,A)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'*when used for qualified medical expenses',REG(28),800,grey,255*ease((t-3.2)/0.4)); fr=Image.alpha_composite(fr,L)
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],fs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b10-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y10{i}.png')
