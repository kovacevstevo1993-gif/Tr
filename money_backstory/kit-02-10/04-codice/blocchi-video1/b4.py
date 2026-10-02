from common import *
bg=make_bg(); bgg=make_bg(grid=True)
def avatar(d,cx,cy,col,s=1.0,a=1.0):
    c=col+(int(255*a),)
    d.ellipse([cx-60*s,cy-170*s,cx+60*s,cy-50*s],fill=c)
    d.rounded_rectangle([cx-110*s,cy-30*s,cx+110*s,cy+140*s],radius=int(80*s),fill=c)
FX,MX=W/2-430,W/2+430
def cards(t,fr,lab62=None,lab70=None,pl=0):
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    for cx,name,col in [(FX,'FRANK',red),(MX,'MARY',green)]:
        d.rounded_rectangle([cx-330,230,cx+330,860],radius=36,fill=card+(255,),outline=col+(255,),width=5)
        avatar(d,cx,480,col,1.0); txt(L,name,BOLD(64),650,white,255,x=cx)
    fr=Image.alpha_composite(fr,L); return fr
# A: meet frank & mary, same benefit
def drawA(t):
    fr=bg.copy()
    L=Image.new('RGBA',(W,H),(0,0,0,0)); a=ease(t/0.5); txt(L,'MEET YOUR NEIGHBORS',SER(72),90,goldL,255*a); fr=Image.alpha_composite(fr,L)
    for i,(cx,name,col) in enumerate([(FX,'FRANK',red),(MX,'MARY',green)]):
        st=0.4+i*0.8
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(C)
        d.rounded_rectangle([cx-330,230,cx+330,860],radius=36,fill=card+(255,),outline=col+(255,),width=5)
        avatar(d,cx,480,col); txt(C,name,BOLD(64),650,white,255,x=cx)
        fr=pop(fr,C,(int(cx-335),225,int(cx+335),865),back((t-st)/0.5))
    for i,cx in enumerate([FX,MX]):
        st=4.9+i*0.3
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); txt(C,'$2,000 / month',BOLD(56),760,goldL,255,x=cx)
        fr=pop(fr,C,(int(cx-320),740,int(cx+320),840),back((t-st)/0.45))
    if t>6.0:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'SAME FULL BENEFIT',930,alpha=255*ease((t-6.0)/0.5),size=40); fr=Image.alpha_composite(fr,L)
    return fr
# B: claims
def stamp(fr,cx,text,col,s):
    S=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(S); f=BOLD(50); b=sd.textbbox((0,0),text,font=f); bw=b[2]-b[0]+60; bh=96; bx=cx-bw/2; by=735
    sd.rounded_rectangle([bx,by,bx+bw,by+bh],radius=48,fill=col+(255,)); sd.text((bx+30-b[0],by+bh/2-(b[3]-b[1])/2-b[1]),text,font=f,fill=(255,255,255,255) if col==red else navy+(255,))
    return pop(fr,S,(int(bx)-5,by-5,int(bx+bw)+5,by+bh+5),s)
def drawB(t):
    fr=cards(t,bg.copy())
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'TWO DIFFERENT CHOICES',SER(72),90,goldL); fr=Image.alpha_composite(fr,L)
    fr=stamp(fr,FX,'CLAIMS AT 62',red,back((t-0.1)/0.4))
    if t>1.85: fr=stamp(fr,MX,'WAITS UNTIL 70',green,back((t-1.85)/0.4))
    return fr
# C: 8 years timeline
def drawC(t):
    fr=bgg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'8 YEARS: AGE 62 → 70',SER(72),80,goldL,255*ease(t/0.5))
    x0,x1=260,W-260
    for row,(name,col,y) in enumerate([('FRANK',red,330),('MARY',green,640)]):
        txt(L,name,BOLD(48),y-90,col,255,x=x0,anchor='l')
        d.line([x0,y+60,x1,y+60],fill=(255,255,255,60),width=3)
        for k in range(9):
            xx=x0+(x1-x0)*k/8; d.line([xx,y+50,xx,y+70],fill=(255,255,255,90),width=3)
            txt(L,str(62+k),REG(28),y+85,grey,255,x=xx)
    fr=Image.alpha_composite(fr,L)
    p=ease((t-0.5)/5.4)
    # Frank checks stacking along row
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    n=int(p*96)
    for m in range(n):
        xx=x0+(x1-x0)*(m/96); d.rounded_rectangle([xx,300,xx+(x1-x0)/96-3,380],radius=4,fill=red+(230,))
    txt(L,'$0 — nothing yet',BOLD(44),610,grey,255*ease((t-2.0)/0.6),x=W/2)
    fr=Image.alpha_composite(fr,L)
    q=ease((t-5.93)/2.6)
    if t>5.93:
        v=int(134400*q/100)*100
        G=Image.new('RGBA',(W,H),(0,0,0,0)); txt(G,f'${v:,}',BOLD(150),800,red,200); fr=Image.alpha_composite(fr,G.filter(ImageFilter.GaussianBlur(24)))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,f'${v:,}',BOLD(150),800,red); txt(L,'FRANK HAS ALREADY COLLECTED',BOLD(38),750-10,white,255*ease((t-5.93)/0.5))
        fr=Image.alpha_composite(fr,L)
    return fr
# D: Frank wins? not so fast
def drawD(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0))
    a=ease(t/0.4); txt(L,'SO FRANK WINS?',SER(120),330,white,255*a)
    fr=Image.alpha_composite(fr,L)
    if t>1.98:
        s=back((t-1.98)/0.35); S=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(S); f=BOLD(110); b=sd.textbbox((0,0),'NOT SO FAST.',font=f)
        bw=b[2]-b[0]+100; bh=b[3]-b[1]+70; bx=(W-bw)/2; by=560
        sd.rounded_rectangle([bx,by,bx+bw,by+bh],radius=30,fill=gold+(255,)); sd.text((bx+50-b[0],by+35-b[1]),'NOT SO FAST.',font=f,fill=navy+(255,))
        fr=pop(fr,S,(int(bx)-5,by-5,int(bx+bw)+5,by+bh+5),s)
    return fr
for fn,dur,name in [(drawA,9.44,1),(drawB,4.4,2),(drawC,13.27,3),(drawD,3.38,4)]:
    render(fn,dur,f'/mnt/user-data/outputs/v1-b4-0{name}.mp4')
    import shutil; shutil.copy(f'/home/claude/_fr/{int(dur*30)-5:04d}.png',f'/home/claude/b4_{name}.png')
