from common2 import *
import shutil, sys
S=["Here's the scary part.","Fidelity's research found that the average American expects to spend only about seventy five thousand dollars.","That's less than half of the real number.","Just the standard Medicare Part B premium is two hundred two dollars and ninety cents a month in 2026.","That's more than two thousand four hundred dollars a year, per person, before a single doctor visit, before dental, before vision, before prescriptions.","And if your income is higher, Medicare adds extra charges on top, called IRMAA, based on the tax return you filed two years earlier.","Many retirees only find out when the first bill arrives."]
TOTF=1241
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
G=[[0,1,2],[3],[4],[5,6]]; durs=[sum(fs[i] for i in g) for g in G]; print(fs,durs,sum(durs))
def rel(g): return [sum(fs[g[0]:k])/30 for k in g]
def drawA(t):
    r=rel(G[0]); fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,"HERE'S THE SCARY PART",SER(70),100,red,255*ease(t/0.35))
    cx,cy,R=W/2-330,560,230
    d.ellipse([cx-R,cy-R,cx+R,cy+R],outline=(40,62,92,255),width=50)
    if t>r[1]:
        p=ease((t-r[1])/1.6); frac=75000/185500
        d.arc([cx-R,cy-R,cx+R,cy+R],start=-90,end=-90+360*frac*p,fill=blue+(255,),width=50)
        txt(L,f'{int(frac*100*p)}%',BOLD(90),cy-60,blue,255,x=cx)
        txt(L,'what people expect',REG(30),cy+50,grey,255,x=cx)
        txt(L,f'EXPECTED: ${int(75000*p/100)*100:,}',BOLD(52),380,blue,255,x=W/2+120,anchor='l')
        txt(L,'REAL: $185,500',BOLD(52),480,red,255*ease((t-r[1]-0.8)/0.4),x=W/2+120,anchor='l')
        txt(L,'Source: Fidelity research',REG(26),985,grey,200)
    fr=Image.alpha_composite(fr,L)
    if t>r[2]:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(52); lab='LESS THAN HALF'; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+80; bx=W/2+120; y=620
        cd.rounded_rectangle([bx,y,bx+bw,y+100],radius=50,fill=red+(255,)); cd.text((bx+40-b[0],y+50-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(255,255,255,255))
        fr=pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,y+105),back((t-r[2])/0.4))
    return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'MEDICARE PART B · STANDARD PREMIUM 2026',SER(56),110,goldL,255*ease(t/0.4))
    # card
    C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x0,y0,x1,y1=W/2-480,260,W/2+480,820
    cd.rounded_rectangle([x0,y0,x1,y1],radius=36,fill=(236,240,245,255)); cd.rectangle([x0,y0+60,x1,y0+150],fill=blue+(255,))
    txt(C,'MEDICARE',BOLD(56),y0+72,(255,255,255),255,x=W/2)
    p=ease((t-0.5)/1.6); v=202.90*p
    txt(C,f'${v:,.2f}',BOLD(150),y0+220,navy,255,x=W/2); txt(C,'PER MONTH · PER PERSON',BOLD(40),y0+420,(90,100,120),255,x=W/2)
    fr=pop(fr,C,(int(x0)-5,y0-5,int(x1)+5,y1+5),back(t/0.45))
    L2=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L2,'Source: CMS (Centers for Medicare & Medicaid Services)',REG(26),985,grey,200)
    fr=Image.alpha_composite(fr,L); fr=Image.alpha_composite(fr,L2); return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'12 MONTHS × $202.90',SER(62),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    # calendar grid
    for m in range(12):
        st=0.2+m*0.12
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=260+(m%6)*150; y=240+(m//6)*150
        cd.rounded_rectangle([x,y,x+130,y+130],radius=16,fill=card+(255,),outline=blue+(255,),width=3)
        txt(C,['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'][m],BOLD(28),y+14,white,255,x=x+65); txt(C,'$203',BOLD(34),y+62,red,255,x=x+65)
        fr=pop(fr,C,(x-5,y-5,x+135,y+135),back((t-st)/0.35))
    p=ease((t-1.8)/1.2)
    if p>0:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,f'${2434.80*p:,.2f}',BOLD(96),290,red,255,x=1480); txt(L,'PER YEAR',BOLD(40),410,white,255*p,x=1480); txt(L,'per person',REG(32),470,grey,255*p,x=1480)
        fr=Image.alpha_composite(fr,L)
    items=['DOCTOR VISITS','DENTAL','VISION','PRESCRIPTIONS']
    for k,it in enumerate(items):
        st=4.0+k*0.9
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(36); lab='+ '+it; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+60; x=260+k*380; y=640
        cd.rounded_rectangle([x,y,x+bw,y+80],radius=40,fill=card+(255,),outline=red+(255,),width=3); cd.text((x+30-b[0],y+40-(b[3]-b[1])/2-b[1]),lab,font=f,fill=red+(255,))
        fr=pop(fr,C,(x-5,y-5,int(x+bw)+5,y+85),back((t-st)/0.4))
    if t>4.0:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'...and that is BEFORE all of these',BOLD(40),780,white,255*ease((t-4.0)/0.4)); fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawD(t):
    r=rel(G[3]); fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'HIGHER INCOME = EXTRA MEDICARE CHARGES',SER(54),95,goldL,255*ease(t/0.4))
    # staircase
    base_=760; x0=280
    for k in range(5):
        p=ease((t-0.4-k*0.35)/0.5)
        if p<=0: continue
        h=(80+k*80)*p; x=x0+k*150; col=tuple(int(gold[i]+(red[i]-gold[i])*k/4) for i in range(3))
        d.rounded_rectangle([x,base_-h,x+130,base_],radius=10,fill=col+(255,))
    d.line([x0-20,base_,x0+760,base_],fill=gold+(255,),width=3); txt(L,'YOUR INCOME →',BOLD(30),base_+16,grey,255,x=x0,anchor='l'); txt(L,'EXTRA PREMIUM',BOLD(30),base_-450,grey,255,x=x0,anchor='l')
    if t>1.6:
        txt(L,'IRMAA',BOLD(120),260,red,255*ease((t-1.6)/0.4),x=1400)
        txt(L,'based on your tax return',REG(38),420,white,255*ease((t-2.4)/0.4),x=1400)
        txt(L,'from 2 years earlier',BOLD(44),475,white,255*ease((t-2.4)/0.4),x=1400)
    fr=Image.alpha_composite(fr,L)
    if t>r[1]:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx,cy=1400,720
        cd.rectangle([cx-170,cy-100,cx+170,cy+100],fill=(236,240,245,255)); cd.polygon([(cx-170,cy-100),(cx,cy+10),(cx+170,cy-100)],outline=(160,170,190,255),width=5)
        cd.rounded_rectangle([cx-120,cy+20,cx+120,cy+80],radius=10,fill=red+(255,)); txt(C,'FIRST BILL',BOLD(34),cy+32,(255,255,255),255,x=cx)
        fr=pop(fr,C,(cx-175,cy-105,cx+175,cy+105),back((t-r[1])/0.45))
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3,4]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b9-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y9{i}.png')
