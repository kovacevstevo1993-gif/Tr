from common2 import *
import shutil, sys
S=["Now imagine keeping all your money in cash for twenty five years.","The number on your statement stays the same, so it feels safe.","But every year, it buys less food, less gas, less medicine.","You never see a loss on paper, but you lose purchasing power every single day.","That's why many retirees who played it too safe end up just as short as those who took too much risk."]
TOTF=760
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0]+fs[1],fs[2],fs[3],fs[4]]; print(fs,durs,sum(durs)); s2=fs[0]/30
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'25 YEARS IN CASH',SER(70),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x0,x1,y0=W/2-500,W/2+500,220
    cd.rounded_rectangle([x0,y0,x1,y0+680],radius=24,fill=(240,242,246,255)); cd.rectangle([x0,y0,x1,y0+90],fill=navy+(255,))
    txt(C,'SAVINGS ACCOUNT STATEMENT',BOLD(40),y0+25,(255,255,255),255,x=W/2)
    yr=min(25,int(1+t*25/(durs[0]/30*0.8)))
    txt(C,f'YEAR {yr}',BOLD(52),y0+150,(90,100,120),255,x=W/2)
    txt(C,'$100,000',BOLD(150),y0+240,navy,255,x=W/2)
    if t>s2: txt(C,'BALANCE: UNCHANGED  ✓' if False else 'BALANCE: UNCHANGED',BOLD(44),y0+470,green,255*ease((t-s2)/0.4),x=W/2)
    if t>s2+1.2: txt(C,'...so it feels safe',REG(40),y0+560,(90,100,120),255*ease((t-s2-1.2)/0.4),x=W/2)
    fr=pop(fr,C,(int(x0)-5,y0-5,int(x1)+5,y0+685),back(t/0.45))
    return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'EVERY YEAR IT BUYS LESS',SER(70),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    items=[('FOOD',gold),('GAS',blue),('MEDICINE',red)]
    for k,(lab,col) in enumerate(items):
        st=0.3+k*0.9
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=W/2+(k-1)*520; y=560
        cd.rounded_rectangle([x-220,y-260,x+220,y+260],radius=34,fill=card+(255,),outline=col+(255,),width=5)
        txt(C,'LESS',BOLD(40),y-230,grey,255,x=x); txt(C,lab,BOLD(60),y-170,col,255,x=x)
        sh=1-0.5*ease((t-st-0.3)/1.5)
        for r in range(5):
            wv=300*sh*(1-r*0.1); cd.rounded_rectangle([x-wv/2,y-40+r*55,x+wv/2,y-5+r*55],radius=10,fill=col+(255,))
        fr=pop(fr,C,(int(x-225),y-265,int(x+225),y+265),back((t-st)/0.45))
    return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'ON PAPER VS REAL BUYING POWER',SER(62),90,goldL,255*ease(t/0.4))
    X0,X1,Y0,Y1=300,1620,860,300
    def px(y): return X0+y/25*(X1-X0)
    def py(v): return Y0-(v/110000)*(Y0-Y1)
    d.line([X0,Y0,X1,Y0],fill=gold+(255,),width=3)
    for y in [0,5,10,15,20,25]: txt(L,f'YR {y}',REG(28),Y0+16,grey,255,x=px(y))
    fr=Image.alpha_composite(fr,L)
    p=ease((t-0.3)/2.2); n=int(p*100)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    pa=[(px(k/4),py(100000)) for k in range(n+1)]; pr=[(px(k/4),py(100000/1.03**(k/4))) for k in range(n+1)]
    if len(pa)>1:
        A=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(A).polygon(pa+pr[::-1],fill=red+(50,)); fr=Image.alpha_composite(fr,A)
        d.line(pa,fill=green+(255,),width=8); d.line(pr,fill=red+(255,),width=8)
    if p>0.98:
        txt(L,'ON PAPER: $100,000',BOLD(40),py(100000)-60,green,255,x=X1,anchor='r')
        txt(L,'BUYING POWER: ~$47,800',BOLD(40),py(47760)+20,red,255,x=X1,anchor='r')
    txt(L,'At 3% inflation per year',REG(26),985,grey,220)
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawD(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'TWO WAYS TO END UP SHORT',SER(66),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    for k,(lab,col,st) in enumerate([('TOO SAFE',blue,0.3),('TOO MUCH RISK',red,1.8)]):
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=W/2+(k*2-1)*420; y=520+math.sin(t*2+k)*6
        cd.rounded_rectangle([x-330,y-230,x+330,y+230],radius=34,fill=card+(255,),outline=col+(255,),width=5)
        txt(C,lab,BOLD(62),y-190,col,255,x=x)
        cd.rounded_rectangle([x-150,y-40,x+150,y+80],radius=18,fill=(120,80,40,255)); txt(C,'$0',BOLD(70),y-30,(255,255,255),255,x=x)
        txt(C,'SHORT OF MONEY',BOLD(38),y+130,white,255,x=x)
        fr=pop(fr,C,(int(x-335),int(y-235),int(x+335),int(y+235)),back((t-st)/0.45))
    if t>3.2:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'SAME RESULT',860,col=red,alpha=255*ease((t-3.2)/0.4),size=50); fr=Image.alpha_composite(fr,L)
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3,4]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b14-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y14{i}.png')
