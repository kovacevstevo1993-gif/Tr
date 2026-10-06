from common import *
bgg=make_bg(grid=True); bg=make_bg()
# chart geometry
X0,X1,Y0,Y1=230,1720,900,230  # ages 62..90, $0..$600k
def px(age): return X0+(age-62)/(90-62)*(X1-X0)
def py(v): return Y0-(v/600000)*(Y0-Y1)
def fr_cum(a): return max(0,(a-62))*16800
def ma_cum(a): return max(0,(a-70))*29760
keys=[(0,70.0),(5.83,72),(8.4,75),(12.97,80),(18.61,85),(22.18,90),(29.45,90)]
def cursor(t):
    for (t0,a0),(t1,a1) in zip(keys,keys[1:]):
        if t<=t1:
            dd=min(1.8,t1-t0); p=ease((t-(t1-dd))/dd) if t1>t0 else 1
            return a0+(a1-a0)*p
    return 90
def drawA(t):
    fr=bgg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'TOTAL COLLECTED OVER TIME',SER(64),70,goldL)
    d.line([X0,Y0,X1,Y0],fill=gold+(255,),width=4)
    for a in range(62,91,4): txt(L,str(a),REG(30),Y0+20,grey,255,x=px(a))
    for v in [200000,400000,600000]:
        d.line([X0,py(v),X1,py(v)],fill=(255,255,255,20),width=2); txt(L,f'${v//1000}k',REG(28),py(v)-16,grey,255,x=X0-20,anchor='r')
    cur=cursor(t)
    for fn,col,start in [(fr_cum,red,62),(ma_cum,green,70)]:
        pts=[(px(a/4),py(fn(a/4))) for a in range(int(start*4),int(cur*4)+1)]
        if len(pts)>1: d.line(pts,fill=col+(255,),width=10)
    # end dots + value labels
    for fn,col,name,dy in [(fr_cum,red,'FRANK',-60),(ma_cum,green,'MARY',40)]:
        x,y=px(cur),py(fn(cur)); d.ellipse([x-14,y-14,x+14,y+14],fill=col+(255,))
    fr=Image.alpha_composite(fr,L)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    fv,mv=fr_cum(cur),ma_cum(cur)
    txt(L,f'FRANK  ${int(fv/100)*100:,}',BOLD(40),190,red,255,x=X0+10,anchor='l')
    txt(L,f'MARY  ${int(mv/100)*100:,}',BOLD(40),245,green,255,x=X0+10,anchor='l')
    fr=Image.alpha_composite(fr,L)
    # callouts
    def callout(text,col,st,ax,fg=(255,255,255)):
        if t<st: return
        S=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(S); f=BOLD(42); b=sd.textbbox((0,0),text,font=f); bw=b[2]-b[0]+60; bh=84
        bx=min(max(ax-bw/2,X0),X1-bw); by=300
        sd.rounded_rectangle([bx,by,bx+bw,by+bh],radius=42,fill=col+(255,)); sd.text((bx+30-b[0],by+bh/2-(b[3]-b[1])/2-b[1]),text,font=f,fill=fg+(255,))
        nonlocal_fr[0]=pop(nonlocal_fr[0],S,(int(bx)-5,by-5,int(bx+bw)+5,by+bh+5),back((t-st)/0.4))
    nonlocal_fr=[fr]
    if 8.4<=t<12.97: callout('AGE 75: FRANK AHEAD BY $69,600',red,8.4,px(75))
    if 12.97<=t<18.61:
        callout('AGE 80: BREAK-EVEN',gold,12.97,px(80),navy)
    if 18.61<=t<22.18: callout('AGE 85: MARY AHEAD BY $60,000',green,18.61,px(85),navy)
    if t>=22.18: callout('AGE 90: MARY +$124,800',green,22.18,px(88),navy)
    fr=nonlocal_fr[0]
    if 12.97<=t:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); x=px(80.3); y=py(fr_cum(80.3))
        a=ease((t-12.97)/0.5); r=int(34*a)
        d.ellipse([x-r,y-r,x+r,y+r],outline=gold+(255,),width=6); fr=Image.alpha_composite(fr,L)
    return fr
def drawB(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0))
    a=ease(t/0.4); txt(L,'"WHAT IF I DIE AT 72?"',SER(96),230,white,255*a); fr=Image.alpha_composite(fr,L)
    if t>3.57:
        S=Image.new('RGBA',(W,H),(0,0,0,0)); txt(S,'THEN FRANK WINS.',BOLD(80),470,red); fr=pop(fr,S,(300,440,1620,580),back((t-3.57)/0.4))
    if t>6.26:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'A PERSONAL DECISION, NOT A RULE',720,alpha=255*ease((t-6.26)/0.5),size=52); fr=Image.alpha_composite(fr,L)
    return fr
def drawC(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); a=ease(t/0.4)
    txt(L,'YEARLY COST OF LIVING RAISE',SER(70),110,goldL,255*a)
    txt(L,'2026 raise: 2.8%',BOLD(44),220,white,255*ease((t-0.8)/0.5))
    fr=Image.alpha_composite(fr,L)
    for i,(lab,base_,col,x) in enumerate([('FRANK  ·  $1,400',1400,red,W/2-420),('MARY  ·  $2,480',2480,green,W/2+420)]):
        st=5.14+i*0.9
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C)
        cd.rounded_rectangle([x-360,360,x+360,820],radius=34,fill=card+(255,),outline=col+(255,),width=5)
        txt(C,lab,BOLD(44),410,white,255,x=x)
        inc=base_*0.028
        p=ease((t-st-0.4)/1.4); txt(C,f'+${inc*p:,.2f}',BOLD(120),520,col,255,x=x)
        txt(C,'more per month',REG(38),700,grey,255,x=x)
        fr=pop(fr,C,(int(x-365),355,int(x+365),825),back((t-st)/0.45))
    if t>9.0:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'BIGGER CHECK = BIGGER RAISES',900,alpha=255*ease((t-9.0)/0.5),size=46); fr=Image.alpha_composite(fr,L)
    return fr
render(drawA,29.45,'/mnt/user-data/outputs/v1-b5-01.mp4'); import shutil; shutil.copy('/home/claude/_fr/0870.png','/home/claude/c5a.png'); shutil.copy('/home/claude/_fr/0450.png','/home/claude/c5a2.png')
#render(drawB,10.59,'/mnt/user-data/outputs/v1-b5-02.mp4'); shutil.copy('/home/claude/_fr/0300.png','/home/claude/c5b.png')
#render(drawC,11.96,'/mnt/user-data/outputs/v1-b5-03.mp4'); shutil.copy('/home/claude/_fr/0340.png','/home/claude/c5c.png')
