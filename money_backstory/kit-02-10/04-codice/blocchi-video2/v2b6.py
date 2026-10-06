from common2 import *
import shutil, sys
S=["So how do you fix mistake number one?","First, plan for your money to last until at least ninety five.","Second, remember that Social Security is one of the few incomes that lasts as long as you do, and it grows every year you wait, up to age seventy.","That's why the claiming decision matters so much.","And third, don't spend like the first ten years are the only ones that count.","Your eighty year old self is counting on you."]
TOTF=919
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0]+fs[1],fs[2]+fs[3],fs[4]+fs[5]]; print(fs,durs,sum(durs))
def step(L,n,title,col,a,y=190):
    d=ImageDraw.Draw(L); d.ellipse([200,y,300,y+100],fill=col+(int(255*a),)); txt(L,str(n),BOLD(64),y+16,navy,255*a,x=250)
    txt(L,title,BOLD(54),y+22,white,255*a,x=330,anchor='l')
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'HOW TO FIX MISTAKE #1',SER(70),85,goldL,255*ease(t/0.4))
    s2=fs[0]/30
    if t>s2:
        a=ease((t-s2)/0.4); step(L,1,'PLAN TO AGE 95 OR BEYOND',gold,a)
        X0,X1=260,1660
        def ax(g): return X0+(g-65)/(100-65)*(X1-X0)
        d.line([X0,760,X1,760],fill=gold+(255,),width=3)
        for g in range(65,101,5): txt(L,str(g),REG(30),778,grey,255,x=ax(g))
        p=ease((t-s2-0.3)/1.4); d.rounded_rectangle([ax(65),520,ax(65)+(ax(95)-ax(65))*p,620],radius=50,fill=gold+(255,))
        if p>0.95: txt(L,'95+',BOLD(56),537,navy,255,x=ax(95)-80)
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    step(L,2,'SOCIAL SECURITY LASTS AS LONG AS YOU DO',blue,ease(t/0.4),y=120)
    base_=820; ages=[62,63,64,65,66,67,68,69,70]; vals=[70,75,80,86.7,93.3,100,108,116,124]
    xs=[380+i*140 for i in range(9)]
    d.line([300,base_,1640,base_],fill=gold+(255,),width=3); fr=Image.alpha_composite(fr,L)
    for i,(a,v) in enumerate(zip(ages,vals)):
        p=ease((t-0.5-i*0.22)/0.6)
        if p<=0: continue
        h=v/124*420*p; col=tuple(int(red[k]+(green[k]-red[k])*i/8) for k in range(3)); im=bar(h,col,100); fr.alpha_composite(im,(xs[i]-50,int(base_-im.height)))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,str(a),BOLD(32),base_+16,white,255,x=xs[i]); txt(L,f'{round(v)}%',BOLD(28),base_-im.height-40,col,255*p,x=xs[i]); fr=Image.alpha_composite(fr,L)
    s4=fs[2]/30
    if t>s4:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'WHEN YOU CLAIM MATTERS',920,col=gold,alpha=255*ease((t-s4)/0.4),size=44); fr=Image.alpha_composite(fr,L)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'% of full benefit by claiming age (full retirement age 67) · Source: SSA',REG(24),265,grey,220); fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    step(L,3,"DON'T SPEND IT ALL IN THE FIRST 10 YEARS",green,ease(t/0.4),y=120)
    fr=Image.alpha_composite(fr,L)
    decs=[('65-75',gold),('75-85',gold),('85-95',gold)]
    for i,(lab,col) in enumerate(decs):
        st=0.4+i*0.5
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=560+i*400; y=560+math.sin(t*2+i)*6
        cd.rounded_rectangle([x-170,y-170,x+170,y+170],radius=30,fill=card+(255,),outline=col+(255,),width=4)
        txt(C,'AGE '+lab,BOLD(40),y-130,white,255,x=x)
        # money stack
        for k in range(4): cd.rounded_rectangle([x-90,y+60-k*34,x+90,y+88-k*34],radius=6,fill=(60,170,90,255),outline=(20,70,35,255),width=3)
        fr=pop(fr,C,(int(x-175),int(y-175),int(x+175),int(y+175)),back((t-st)/0.45))
    s6=fs[4]/30
    if t>s6:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'YOUR 80-YEAR-OLD SELF IS COUNTING ON YOU',840,col=gold,alpha=255*ease((t-s6)/0.4),size=44); fr=Image.alpha_composite(fr,L)
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b6-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y6{i}.png')
