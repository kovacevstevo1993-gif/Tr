from common import *
import shutil
S=["Trap number four: taxes.","Many retirees are shocked to learn that Social Security can be taxed.","If your combined income is above twenty five thousand dollars as a single filer, or thirty two thousand dollars as a married couple, part of your benefits becomes taxable.","Up to eighty five percent of your benefits can count as taxable income.","And here's the twist: those limits were set decades ago and have never been adjusted for inflation.","So every year, more retirees cross them without even noticing."]
TOTF=1062
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
groups=[[0,1],[2],[3],[4],[5]]; durs=[sum(fs[i] for i in g) for g in groups]; print(fs,durs,sum(durs))
s2=fs[0]/30
bg=make_bg(); bgg=make_bg(grid=True)
def drawA(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); a=ease(t/0.3)
    txt(L,'TRAP #4',BOLD(140),170,red,255*a); fr=Image.alpha_composite(fr,L)
    S2=Image.new('RGBA',(W,H),(0,0,0,0)); txt(S2,'TAXES',BOLD(220),360,gold); fr=pop(fr,S2,(560,340,1360,620),back((t-0.3)/0.45))
    if t>s2:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'YES — SOCIAL SECURITY CAN BE TAXED',BOLD(58),760,white,255*ease((t-s2)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
def drawB(t):
    fr=bgg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'IF YOUR COMBINED INCOME IS ABOVE...',SER(64),110,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    for i,(lab,v,st) in enumerate([('SINGLE',25000,0.6),('MARRIED COUPLE',32000,5.0)]):
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=W/2+(i*2-1)*420
        cd.rounded_rectangle([x-360,280,x+360,660],radius=34,fill=card+(255,),outline=gold+(255,),width=5)
        txt(C,lab,BOLD(48),330,white,255,x=x); p=ease((t-st-0.2)/1.2); txt(C,f'${int(v*p/100)*100:,}',BOLD(130),440,gold,255,x=x)
        fr=pop(fr,C,(int(x-365),275,int(x+365),665),back((t-st)/0.45))
    if t>8.2:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'PART OF YOUR BENEFITS BECOMES TAXABLE',800,col=red,alpha=255*ease((t-8.2)/0.4),size=46); fr=Image.alpha_composite(fr,L)
    return fr
def drawC(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'OF YOUR BENEFITS CAN BE TAXABLE',BOLD(54),880,white,255*ease((t-0.6)/0.4))
    txt(L,'UP TO',SER(64),110,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    p=ease((t-0.3)/1.8); cx,cy,r=W/2,530,260
    R=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(R)
    d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=(40,62,92,255),width=60)
    d.arc([cx-r,cy-r,cx+r,cy+r],start=-90,end=-90+360*0.85*p,fill=red+(255,),width=60)
    txt(R,f'{int(85*p)}%',BOLD(170),cy-100,red); fr=Image.alpha_composite(fr,R)
    return fr
def drawD(t):
    fr=bgg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,"HERE'S THE TWIST",SER(72),90,goldL,255*ease(t/0.4))
    x0,x1,y0=260,1660,820
    d.line([x0,y0,x1,y0],fill=gold+(255,),width=4)
    for k,yr in enumerate([1984,1995,2005,2015,2026]):
        x=x0+(x1-x0)*k/4; txt(L,str(yr),REG(32),y0+20,grey,255,x=x)
    fr=Image.alpha_composite(fr,L)
    p=ease((t-0.8)/3.0)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    xe=x0+(x1-x0)*p
    d.line([x0,640,xe,640],fill=gold+(255,),width=12)
    pts=[(x0+(x1-x0)*q/60, 640-(q/60)**1.3*360) for q in range(int(60*p)+1)]
    if len(pts)>1: d.line(pts,fill=red+(255,),width=12)
    txt(L,'LIMIT: $25,000 — NEVER CHANGED',BOLD(38),665,gold,255*ease((t-1.5)/0.5),x=x0+20,anchor='l')
    if p>0.9: txt(L,'PRICES & INCOMES',BOLD(38),230,red,255*ease((t-3.8)/0.5),x=x1,anchor='r')
    fr=Image.alpha_composite(fr,L)
    if t>4.5:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'NEVER ADJUSTED FOR INFLATION',940,col=red,alpha=255*ease((t-4.5)/0.4),size=44); fr=Image.alpha_composite(fr,L)
    return fr
def drawE(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'EVERY YEAR, MORE RETIREES CROSS THE LINE',SER(60),120,goldL,255*ease(t/0.4))
    d.line([200,560,W-200,560],fill=red+(255,),width=6); txt(L,'TAX LINE',BOLD(34),520,red,255,x=W-210,anchor='r')
    fr=Image.alpha_composite(fr,L)
    for i in range(7):
        st=0.3+i*0.35
        if t<st: continue
        p=ease((t-st)/0.8); x=330+i*210; y=760-(760-400)*p
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); col=white if y>560 else red
        d.ellipse([x-26,y-80,x+26,y-28],fill=col+(255,)); d.rounded_rectangle([x-45,y-20,x+45,y+60],radius=30,fill=col+(255,))
        fr=Image.alpha_composite(fr,L)
    if t>2.6:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'WITHOUT EVEN NOTICING',BOLD(56),880,white,255*ease((t-2.6)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
render(drawB,durs[1]/30,'/mnt/user-data/outputs/v1-b11-02.mp4')
