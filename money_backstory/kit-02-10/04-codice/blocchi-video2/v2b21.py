from common2 import *
import shutil, sys
S=["Let's make it real.","Imagine your withdrawals are taxed at an average of twenty percent.","Out of a one million dollar balance, about two hundred thousand dollars would go to taxes over time.","That's why many retirees look at strategies like spreading withdrawals across low income years, or converting part of their savings to a Roth account before required withdrawals begin.","A tax professional can help you find the right mix for your situation."]
TOTF=861
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0]+fs[1],fs[2],fs[3],fs[4]]; print(fs,durs,sum(durs))
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,"LET'S MAKE IT REAL",SER(70),110,goldL,255*ease(t/0.4))
    cx,cy,R=W/2,560,230; d.ellipse([cx-R,cy-R,cx+R,cy+R],outline=(40,62,92,255),width=50)
    s2=fs[0]/30
    if t>s2:
        p=ease((t-s2)/1.4); d.arc([cx-R,cy-R,cx+R,cy+R],start=-90,end=-90+72*p,fill=red+(255,),width=50)
        txt(L,f'{int(20*p)}%',BOLD(120),cy-80,red,255,x=cx); txt(L,'average tax',REG(36),cy+60,white,255*p,x=cx)
        txt(L,'on every withdrawal (example)',REG(34),850,grey,255*ease((t-s2-0.8)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'OUT OF $1,000,000...',SER(70),110,goldL,255*ease(t/0.4))
    X0,X1,y=240,1680,420
    p=ease((t-0.3)/1.2); d.rounded_rectangle([X0,y,X0+(X1-X0)*p,y+160],radius=30,fill=green+(255,))
    q=ease((t-1.6)/1.2)
    if q>0:
        xs=X0+(X1-X0)*0.8; d.rounded_rectangle([xs,y,xs+(X1-xs)*q,y+160],radius=30,fill=red+(255,))
    if p>0.9: txt(L,f'YOU KEEP ~${int(800000*min(1,q*1.2 if q>0 else 0)+0):,}' if False else 'YOU KEEP ~$800,000',BOLD(46),y+55,navy,255*ease((t-1.6)/0.4),x=X0+(X1-X0)*0.4)
    if q>0.9: txt(L,'TAXES',BOLD(40),y+55,(255,255,255),255,x=X0+(X1-X0)*0.9)
    if t>2.6:
        v=int(200000*ease((t-2.6)/1.0)); txt(L,f'~${v:,}',BOLD(120),640,red,255); txt(L,'GOES TO TAXES OVER TIME',BOLD(46),800,white,255*ease((t-2.6)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'STRATEGIES MANY RETIREES LOOK AT',SER(60),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    D=fs[3]/30
    for k,(title,sub,col,st) in enumerate([('SPREAD WITHDRAWALS','across low-income years',blue,0.4),('ROTH CONVERSION','before required withdrawals begin',green,D*0.5)]):
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=W/2+(k*2-1)*420; y=560+math.sin(t*2+k)*6
        cd.rounded_rectangle([x-380,y-280,x+380,y+280],radius=34,fill=card+(255,),outline=col+(255,),width=5)
        txt(C,title,BOLD(52),y-240,col,255,x=x); txt(C,sub,REG(34),y-170,white,255,x=x)
        if k==0:
            hs=[60,120,70,140,90,60]; hs2=[90,90,90,90,90,90]; pp=ease((t-st-0.6)/1.2)
            for i in range(6):
                h=hs[i]+(hs2[i]-hs[i])*pp; bx=x-270+i*95; cd.rounded_rectangle([bx,y+200-h*1.6,bx+70,y+200],radius=10,fill=col+(255,))
        else:
            cd.rounded_rectangle([x-330,y-60,x-90,y+120],radius=20,fill=(90,110,140,255)); txt(C,'TRADITIONAL',BOLD(30),y+10,(255,255,255),255,x=x-210)
            pp=ease((t-st-0.5)/0.8); cd.line([x-70,y+30,x-70+140*pp,y+30],fill=gold+(255,),width=12)
            if pp>0.9: cd.polygon([(x+70,y+5),(x+100,y+30),(x+70,y+55)],fill=gold+(255,))
            cd.rounded_rectangle([x+110,y-60,x+330,y+120],radius=20,fill=col+(255,)); txt(C,'ROTH',BOLD(44),y+2,navy,255,x=x+220)
        fr=pop(fr,C,(int(x-385),int(y-285),int(x+385),int(y+285)),back((t-st)/0.45))
    return frame(fr)
def drawD(t):
    fr=base(t); C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx,cy=W/2,440
    cd.ellipse([cx-70,cy-190,cx+70,cy-50],fill=gold+(255,)); cd.rounded_rectangle([cx-130,cy-40,cx+130,cy+160],radius=70,fill=gold+(255,))
    cd.rounded_rectangle([cx+90,cy+40,cx+210,cy+140],radius=12,fill=(120,80,40,255))
    fr=pop(fr,C,(int(cx-140),int(cy-200),int(cx+220),int(cy+170)),back(t/0.45))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'A TAX PROFESSIONAL CAN HELP',BOLD(60),680,white,255*ease((t-0.3)/0.4)); txt(L,'find the right mix for YOUR situation',REG(42),770,goldL,255*ease((t-0.6)/0.4))
    txt(L,'Educational content · not tax advice',REG(24),985,grey,200)
    fr=Image.alpha_composite(fr,L); return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3,4]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b21-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y21{i}.png')
