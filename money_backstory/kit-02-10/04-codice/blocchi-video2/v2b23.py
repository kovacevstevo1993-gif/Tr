from common2 import *
import shutil, sys
S=["So let's go back to Frank and Mary one last time.","Frank planned for twenty years, ignored health care, kept everything in cash, counted on Medicare for long term care, and never thought about taxes.","Mary planned for thirty years, gave health care its own budget, kept a balanced mix, made a long term care plan, and spread out her withdrawals.","Same income.","Same savings.","Completely different retirement."]
TOTF=913
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0],fs[1]+fs[2],fs[3]+fs[4]+fs[5]]; print(fs,durs,sum(durs))
def person(d,cx,cy,col,s=1.0):
    d.ellipse([cx-40*s,cy-120*s,cx+40*s,cy-40*s],fill=col); d.rounded_rectangle([cx-70*s,cy-25*s,cx+70*s,cy+100*s],radius=int(50*s),fill=col)
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'FRANK AND MARY',SER(80),150,goldL,255*ease(t/0.4)); txt(L,'one last time',REG(44),260,white,255*ease((t-0.3)/0.4))
    a=ease((t-0.4)/0.5); person(d,W/2-250,560,red+(int(255*a),),1.5); person(d,W/2+250,560,green+(int(255*a),),1.5)
    txt(L,'FRANK',BOLD(50),740,red,255*a,x=W/2-250); txt(L,'MARY',BOLD(50),740,green,255*a,x=W/2+250)
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    d.rounded_rectangle([90,120,W/2-20,960],radius=30,fill=(60,20,30,120),outline=red+(255,),width=4)
    d.rounded_rectangle([W/2+20,120,W-90,960],radius=30,fill=(20,60,40,120),outline=green+(255,),width=4)
    txt(L,'FRANK',BOLD(64),150,red,255,x=W/2-460); txt(L,'MARY',BOLD(64),150,green,255,x=W/2+460)
    fr=Image.alpha_composite(fr,L)
    fi=['Planned for 20 years','Ignored health care','Kept everything in cash','Counted on Medicare for care','Never thought about taxes']
    mi=['Planned for 30 years','Health care in the budget','Kept a balanced mix','Made a long-term care plan','Spread out withdrawals']
    D1=fs[1]/30; D2=fs[2]/30
    for side,items,col,t0,D in [(0,fi,red,0.0,D1),(1,mi,green,D1,D2)]:
        for k,it in enumerate(items):
            st=t0+0.3+k*(D*0.85/5)
            if t<st: continue
            C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x0=140 if side==0 else W/2+70; y=290+k*130
            cx,cy=x0+30,y+30
            if side==0:
                cd.ellipse([cx-28,cy-28,cx+28,cy+28],fill=red+(255,)); cd.line([cx-12,cy-12,cx+12,cy+12],fill=(255,255,255,255),width=7); cd.line([cx-12,cy+12,cx+12,cy-12],fill=(255,255,255,255),width=7)
            else:
                cd.ellipse([cx-28,cy-28,cx+28,cy+28],fill=green+(255,)); cd.line([(cx-13,cy),(cx-3,cy+11),(cx+14,cy-11)],fill=navy+(255,),width=7,joint='curve')
            txt(C,it,BOLD(38),y+10,white,255,x=x0+80,anchor='l')
            fr=pop(fr,C,(int(x0)-5,y-10,int(x0)+780,y+75),back((t-st)/0.35))
    return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    s5=fs[3]/30; s6=(fs[3]+fs[4])/30
    txt(L,'SAME INCOME.',BOLD(60),130,white,255*ease(t/0.3),x=W/2-300)
    if t>s5: txt(L,'SAME SAVINGS.',BOLD(60),130,white,255*ease((t-s5)/0.3),x=W/2+300)
    fr=Image.alpha_composite(fr,L)
    if t>s6:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); p=ease((t-s6)/1.2)
        txt(L,'COMPLETELY DIFFERENT RETIREMENT',SER(64),250,goldL,255*ease((t-s6)/0.4))
        X0,X1=380,1620
        for k,(lab,col,frac,end) in enumerate([('FRANK',red,0.35,'OUT OF MONEY'),('MARY',green,1.0,'SECURE UNTIL 95+')]):
            y=450+k*220; txt(L,lab,BOLD(48),y+25,col,255,x=X0-40,anchor='r')
            xe=X0+(X1-X0)*frac*p; d.rounded_rectangle([X0,y,xe,y+110],radius=30,fill=col+(255,))
            if p>0.9: txt(L,end,BOLD(40),y+32,(255,255,255) if k==0 else navy,255,x=(X0+xe)/2 if k==1 else xe+30,anchor='c' if k==1 else 'l')
        fr=Image.alpha_composite(fr,L)
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b23-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y23{i}.png')
