from common import *
import shutil
S=["Trap number one: claiming early while you're still working.","In 2026, if you're under full retirement age and you earn more than twenty four thousand four hundred eighty dollars a year, Social Security holds back one dollar of benefits for every two dollars you earn above that limit.","Earn forty thousand dollars, and about seven thousand seven hundred sixty dollars of your checks are withheld.","The good news: that money isn't lost forever.","Your benefit is recalculated when you reach full retirement age.","But many people panic when their checks suddenly stop."]
TOTF=1047  # 34.9 s at 30 fps
w=[len(x)+10 for x in S]; T=sum(w)
fr_s=[round(x/T*TOTF) for x in w]; fr_s[-1]=TOTF-sum(fr_s[:-1])
groups=[[0],[1],[2],[3,4],[5]]
durs=[sum(fr_s[i] for i in g) for g in groups]
print(durs,sum(durs))
sub4=fr_s[3]/30
bg=make_bg(); bgg=make_bg(grid=True)
def banner_pop(fr,text,y,col,fg,t,st,size=46):
    if t<st: return fr
    C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(size); b=cd.textbbox((0,0),text,font=f); bw=b[2]-b[0]+90; bh=b[3]-b[1]+50; bx=(W-bw)/2
    cd.rounded_rectangle([bx,y,bx+bw,y+bh],radius=bh/2,fill=col+(255,)); cd.text((bx+45-b[0],y+25-b[1]),text,font=f,fill=fg+(255,))
    return pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,int(y+bh)+5),back((t-st)/0.45))
def drawA(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); a=ease(t/0.4)
    txt(L,'TRAP #1',BOLD(150),250,red,255*a); fr=Image.alpha_composite(fr,L)
    # briefcase icon
    if t>0.8:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(C); cx,cy=W/2,560
        d.rounded_rectangle([cx-120,cy-70,cx+120,cy+90],radius=20,fill=gold+(255,)); d.rounded_rectangle([cx-50,cy-110,cx+50,cy-60],radius=14,outline=gold+(255,),width=16)
        d.rectangle([cx-120,cy-5,cx+120,cy+5],fill=navy+(255,))
        fr=pop(fr,C,(int(cx-125),int(cy-125),int(cx+125),int(cy+95)),back((t-0.8)/0.45))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'CLAIMING EARLY WHILE STILL WORKING',BOLD(56),760,white,255*ease((t-1.2)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
def drawB(t):
    fr=bgg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); a=ease(t/0.4)
    txt(L,'2026 EARNINGS LIMIT',SER(72),150,goldL,255*a); txt(L,'(under full retirement age)',REG(38),255,grey,255*a); fr=Image.alpha_composite(fr,L)
    p=ease((t-1.5)/2.0); v=int(24480*p/10)*10
    G=Image.new('RGBA',(W,H),(0,0,0,0)); txt(G,f'${v:,}',BOLD(200),360,gold,200); fr=Image.alpha_composite(fr,G.filter(ImageFilter.GaussianBlur(26)))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,f'${v:,}',BOLD(200),360,gold); txt(L,'a year',REG(40),600,white,255*p); fr=Image.alpha_composite(fr,L)
    # $1 per $2
    D=durs[1]/30
    fr=banner_pop(fr,'ABOVE IT:  $1 WITHHELD FOR EVERY $2 YOU EARN',780,red,(255,255,255),t,D*0.62,size=48)
    return fr
def drawC(t):
    fr=bgg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); a=ease(t/0.4)
    txt(L,'EXAMPLE: YOU EARN $40,000',SER(70),110,goldL,255*a); fr=Image.alpha_composite(fr,L)
    rows=[('$40,000','you earn',white,0.5),('− $24,480','the limit',grey,1.4),('= $15,520','over the limit',white,2.3),('÷ 2','',grey,3.2)]
    for i,(v,lab,col,st) in enumerate(rows):
        if t<st: continue
        L=Image.new('RGBA',(W,H),(0,0,0,0)); al=255*ease((t-st)/0.35); y=260+i*120
        txt(L,v,BOLD(80),y,col,al,x=W/2+120,anchor='r'); txt(L,lab,REG(38),y+22,grey,al,x=W/2+170,anchor='l')
        fr=Image.alpha_composite(fr,L)
    if t>4.1:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(L).line([W/2-420,760,W/2+420,760],fill=gold+(255,),width=4); fr=Image.alpha_composite(fr,L)
        p=ease((t-4.1)/1.3); v=int(7760*p/10)*10
        S2=Image.new('RGBA',(W,H),(0,0,0,0)); txt(S2,f'${v:,} WITHHELD',BOLD(96),800,red); fr=Image.alpha_composite(fr,S2)
    return fr
def drawD(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0))
    txt(L,'THE GOOD NEWS',SER(80),160,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    fr=banner_pop(fr,'NOT LOST FOREVER',380,green,navy,t,0.9,size=90)
    if t>sub4:
        # recalculation arrow loop
        C=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(C); cx,cy=W/2,700; r=110
        p=ease((t-sub4)/1.2); d.arc([cx-r,cy-r,cx+r,cy+r],start=-90,end=-90+320*p,fill=gold+(255,),width=22)
        if p>0.95:
            ang=math.radians(-90+320); ex,ey=cx+r*math.cos(ang),cy+r*math.sin(ang)
            d.polygon([(ex+30,ey-10),(ex-25,ey-25),(ex-5,ey+30)],fill=gold+(255,))
        fr=Image.alpha_composite(fr,C)
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'YOUR BENEFIT IS RECALCULATED AT FULL RETIREMENT AGE',BOLD(44),880,white,255*ease((t-sub4-0.3)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
def drawE(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0))
    txt(L,'BUT MANY PEOPLE PANIC',SER(84),140,white,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    months=['JAN','FEB','MAR','APR','MAY','JUN']
    for i,m in enumerate(months):
        st=0.4+i*0.25
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(C); x=W/2+(i-2.5)*250; y=520
        d.rounded_rectangle([x-100,y-110,x+100,y+110],radius=20,fill=card+(255,),outline=grey+(255,),width=3)
        txt(C,m,BOLD(40),y-85,white,255,x=x); txt(C,'$0',BOLD(64),y-10,red,255,x=x)
        fr=pop(fr,C,(int(x-105),y-115,int(x+105),y+115),back((t-st)/0.4))
    if t>2.2:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'WHEN THEIR CHECKS SUDDENLY STOP',BOLD(52),780,red,255*ease((t-2.2)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
def renderF(fn,frames,out):
    render(fn,frames/30,out)
for i,(fn,fr_) in enumerate(zip([drawA,drawB,drawC,drawD,drawE],durs),1):
    renderF(fn,fr_,f'/mnt/user-data/outputs/v1-b8-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{fr_-3:04d}.png',f'/home/claude/x8{i}.png')
