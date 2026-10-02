from common2 import *
import shutil, sys
S=["Meet Frank and Mary, two neighbors who retired at sixty five with the same savings.","Frank planned his money to last until eighty five.","Mary planned until ninety five.","At eighty six, Frank is healthy, happy, and suddenly out of savings.","Mary is fine.","The difference wasn't how much they saved.","It was how long they planned for.","So always plan for a long life.","The worst case isn't dying early.","It's living long with an empty account."]
TOTF=921
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
G=[[0],[1,2,3,4],[5,6],[7,8,9]]; durs=[sum(fs[i] for i in g) for g in G]; print(fs,durs,sum(durs))
def rel(g): return [sum(fs[g[0]:k])/30 for k in g]
def person(d,cx,cy,col,s=1.0):
    d.ellipse([cx-40*s,cy-120*s,cx+40*s,cy-40*s],fill=col); d.rounded_rectangle([cx-70*s,cy-25*s,cx+70*s,cy+100*s],radius=int(50*s),fill=col)
FX,MX=W/2-400,W/2+400
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'MEET FRANK AND MARY',SER(72),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    for i,(cx,n,col) in enumerate([(FX,'FRANK',red),(MX,'MARY',green)]):
        st=0.3+i*0.5
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(C); y=math.sin(t*2+i)*6
        d.rounded_rectangle([cx-300,220+y,cx+300,820+y],radius=34,fill=card+(255,),outline=col+(255,),width=5)
        person(d,cx,440+y,col+(255,),1.1); txt(C,n,BOLD(60),600+y,white,255,x=cx); txt(C,'retired at 65',REG(34),690+y,grey,255,x=cx)
        fr=pop(fr,C,(int(cx-305),int(215+y),int(cx+305),int(825+y)),back((t-st)/0.45))
    if t>1.6:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'SAME SAVINGS',900,alpha=255*ease((t-1.6)/0.4),size=44); fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawB(t):
    r=rel(G[1]); fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'SAVINGS BALANCE OVER TIME',SER(62),90,goldL,255*ease(t/0.4))
    X0,X1,Y0,Y1=260,1660,880,260
    def px(a): return X0+(a-65)/(95-65)*(X1-X0)
    d.line([X0,Y0,X1,Y0],fill=gold+(255,),width=3)
    for a in range(65,96,5): txt(L,str(a),REG(30),Y0+16,grey,255,x=px(a))
    txt(L,'AGE',BOLD(26),Y0+56,grey,255,x=X1,anchor='r')
    fr=Image.alpha_composite(fr,L)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    def bal(a,end): return max(0,1-((a-65)/(end-65)))**0.85
    # Frank line
    pF=ease((t-r[0]-0.1)/2.2); endF=65+21*pF
    ptsF=[(px(65+k*0.25),Y0-(Y0-Y1)*bal(65+k*0.25,85)) for k in range(int((endF-65)*4)+1)]
    if len(ptsF)>1: d.line(ptsF,fill=red+(255,),width=9)
    if pF>0.05: txt(L,'FRANK: plans to 85',BOLD(34),Y1-40,red,255,x=px(80),anchor='l')
    if t>r[1]:
        pM=ease((t-r[1])/2.4); endM=65+30*pM
        ptsM=[(px(65+k*0.25),Y0-(Y0-Y1)*bal(65+k*0.25,95)) for k in range(int((endM-65)*4)+1)]
        if len(ptsM)>1: d.line(ptsM,fill=green+(255,),width=9)
        txt(L,'MARY: plans to 95',BOLD(34),Y1+10,green,255,x=px(80),anchor='l')
    fr=Image.alpha_composite(fr,L)
    if t>r[2]:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=px(86); cd.ellipse([x-22,Y0-22,x+22,Y0+22],fill=red+(255,),outline=white+(255,),width=4)
        f=BOLD(40); lab='AGE 86: $0 LEFT'; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+60; bx=x-bw/2; by=Y0-150
        cd.rounded_rectangle([bx,by,bx+bw,by+80],radius=40,fill=red+(255,)); cd.text((bx+30-b[0],by+40-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(255,255,255,255))
        fr=pop(fr,C,(int(bx)-5,by-5,int(bx+bw)+5,Y0+30),back((t-r[2])/0.45))
    if t>r[3]:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); x=px(86); yM=Y0-(Y0-Y1)*bal(86,95)
        d.ellipse([x-18,yM-18,x+18,yM+18],fill=green+(255,),outline=white+(255,),width=4); txt(L,'MARY IS FINE',BOLD(38),yM-70,green,255*ease((t-r[3])/0.3),x=x+40,anchor='l')
        fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawC(t):
    r=rel(G[2]); fr=base(t)
    for i,(top,sub,col,st,ok) in enumerate([("NOT HOW MUCH","THEY SAVED",grey,0.2,False),("HOW LONG","THEY PLANNED FOR",gold,r[1],True)]):
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(C); cx=W/2+(i*2-1)*420; y=math.sin(t*2+i)*6
        d.rounded_rectangle([cx-360,280+y,cx+360,780+y],radius=34,fill=card+(255,),outline=col+(255,),width=5)
        txt(C,top,BOLD(64),340+y,col,255,x=cx); txt(C,sub,BOLD(50),430+y,white,255,x=cx)
        iy=620+y
        if ok:
            d.polygon([(cx-50,iy-70),(cx+50,iy-70),(cx,iy)],fill=gold+(255,)); d.polygon([(cx-50,iy+70),(cx+50,iy+70),(cx,iy)],outline=gold+(255,),width=5)
        else:
            txt(C,'$ = $',BOLD(90),iy-50,grey,255,x=cx); d.line([cx-150,iy+60,cx+150,iy-60],fill=red+(230,),width=14)
        fr=pop(fr,C,(int(cx-365),int(275+y),int(cx+365),int(785+y)),back((t-st)/0.45))
    return frame(fr)
def drawD(t):
    r=rel(G[3]); fr=base(t)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'ALWAYS PLAN FOR A LONG LIFE',SER(72),160,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    if t>r[1]:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,"THE WORST CASE ISN'T DYING EARLY",BOLD(48),330,white,255*ease((t-r[1])/0.4)); fr=Image.alpha_composite(fr,L)
    if t>r[2]:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(C); cx,cy=W/2-330,640
        d.rounded_rectangle([cx-150,cy-100,cx+150,cy+100],radius=24,fill=(120,80,40,255)); d.rounded_rectangle([cx+60,cy-40,cx+170,cy+40],radius=14,fill=(150,100,50,255)); d.ellipse([cx+100,cy-12,cx+124,cy+12],fill=gold+(255,))
        txt(C,'$0',BOLD(80),cy-45,white,255,x=cx-40)
        fr=pop(fr,C,(int(cx-160),int(cy-110),int(cx+180),int(cy+110)),back((t-r[2])/0.45))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,"IT'S LIVING LONG",BOLD(62),560,red,255*ease((t-r[2]-0.3)/0.4),x=W/2-90,anchor='l'); txt(L,'WITH AN EMPTY ACCOUNT',BOLD(52),650,red,255*ease((t-r[2]-0.5)/0.4),x=W/2-90,anchor='l')
        fr=Image.alpha_composite(fr,L)
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3,4]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b5-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y5{i}.png')
