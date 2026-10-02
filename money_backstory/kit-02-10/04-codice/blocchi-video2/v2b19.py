from common2 import *
import shutil, sys
S=["So start planning for long term care in your fifties or early sixties, while you still have options.","That could mean long term care insurance, a hybrid policy, setting aside a separate fund, or simply talking with your family about a plan.","The worst plan is no plan, discovered in a hospital discharge office.","And don't count on Medicaid as a backup plan either.","It generally pays only after you've spent down most of your assets, and it can look back five years at any money you gave away."]
TOTF=977
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0],fs[1],fs[2],fs[3]+fs[4]]; print(fs,durs,sum(durs))
purple=(170,130,230)
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'WHEN TO START PLANNING',SER(66),100,goldL,255*ease(t/0.4))
    X0,X1,y=260,1660,560
    def ax(a): return X0+(a-45)/(85-45)*(X1-X0)
    d.line([X0,y,X1,y],fill=gold+(255,),width=4)
    for a in range(45,86,5): d.line([ax(a),y-10,ax(a),y+10],fill=gold+(255,),width=3); txt(L,str(a),REG(30),y+24,grey,255,x=ax(a))
    p=ease((t-0.5)/1.0)
    d.rounded_rectangle([ax(50),y-150,ax(50)+(ax(63)-ax(50))*p,y-40],radius=30,fill=green+(255,))
    if p>0.9: txt(L,'PLAN HERE',BOLD(44),y-122,navy,255,x=(ax(50)+ax(63))/2)
    if t>1.8:
        q=ease((t-1.8)/0.8); d.rounded_rectangle([ax(63),y-150,ax(63)+(ax(85)-ax(63))*q,y-40],radius=30,fill=(90,110,140,255))
        if q>0.9: txt(L,'FEWER OPTIONS, HIGHER COST',BOLD(34),y-118,white,255,x=(ax(63)+ax(85))/2)
    txt(L,'while you still have options',REG(40),y+110,white,255*ease((t-2.5)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'YOUR OPTIONS',SER(70),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    opts=[('LONG-TERM CARE','INSURANCE',purple),('HYBRID','POLICY',blue),('SEPARATE','FUND',gold),('FAMILY','PLAN',green)]
    D=fs[1]/30
    for k,(a,b,col) in enumerate(opts):
        st=0.2+k*(D*0.22)
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=W/2+(k-1.5)*400; y=540+math.sin(t*2+k)*6
        cd.rounded_rectangle([x-180,y-200,x+180,y+200],radius=30,fill=card+(255,),outline=col+(255,),width=5)
        cd.ellipse([x-60,y-160,x+60,y-40],fill=col+(255,)); txt(C,str(k+1),BOLD(70),y-150,navy,255,x=x)
        txt(C,a,BOLD(34 if len(a)>9 else 42),y+10,white,255,x=x); txt(C,b,BOLD(42),y+70,col,255,x=x)
        fr=pop(fr,C,(int(x-185),int(y-205),int(x+185),int(y+205)),back((t-st)/0.45))
    return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'THE WORST PLAN IS...',SER(70),120,goldL,255*ease(t/0.4))
    fr=Image.alpha_composite(fr,L)
    S2=Image.new('RGBA',(W,H),(0,0,0,0)); txt(S2,'NO PLAN',BOLD(200),250,red)
    fr=pop(fr,S2.filter(ImageFilter.GaussianBlur(24)),(400,230,1520,480),back((t-0.5)/0.45)); fr=pop(fr,S2,(400,230,1520,480),back((t-0.5)/0.45))
    if t>1.5:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx,cy=W/2,700
        cd.rounded_rectangle([cx-300,cy-90,cx+300,cy+90],radius=20,fill=(236,240,245,255)); cd.rectangle([cx-300,cy-90,cx-220,cy+90],fill=red+(255,))
        cd.rectangle([cx-270,cy-40,cx-250,cy+40],fill=(255,255,255,255)); cd.rectangle([cx-300,cy-10,cx-220,cy+10],fill=red+(255,))
        cd.rectangle([cx-280,cy-10,cx-240,cy+10],fill=(255,255,255,255))
        txt(C,'HOSPITAL',BOLD(40),cy-60,navy,255,x=cx+40); txt(C,'DISCHARGE OFFICE',BOLD(40),cy+5,navy,255,x=cx+40)
        fr=pop(fr,C,(int(cx-305),cy-95,int(cx+305),cy+95),back((t-1.5)/0.45))
    return frame(fr)
def drawD(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,"DON'T COUNT ON MEDICAID EITHER",SER(62),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    s5=fs[3]/30
    if t>s5:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
        txt(L,'1. SPEND DOWN YOUR ASSETS FIRST',BOLD(44),260,white,255*ease((t-s5)/0.4),x=240,anchor='l')
        p=ease((t-s5-0.4)/1.6); wv=1100*(1-0.85*p)
        d.rounded_rectangle([240,340,240+wv,430],radius=24,fill=gold+(255,)); txt(L,'YOUR SAVINGS',BOLD(36),362,white,255,x=260+wv,anchor='l')
        fr=Image.alpha_composite(fr,L)
    s6=s5+ (fs[4]/30)*0.45
    if t>s6:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
        txt(L,'2. 5-YEAR LOOK-BACK ON MONEY YOU GAVE AWAY',BOLD(44),520,white,255*ease((t-s6)/0.4),x=240,anchor='l')
        fr=Image.alpha_composite(fr,L)
        for k in range(5):
            st=s6+0.4+k*0.3
            if t<st: continue
            C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=320+k*260; y=620
            cd.rounded_rectangle([x-100,y,x+100,y+180],radius=20,fill=card+(255,),outline=red+(255,),width=4)
            txt(C,f'YEAR {5-k}',BOLD(30),y+20,red,255,x=x); txt(C,'BACK',BOLD(30),y+60,grey,255,x=x)
            cd.polygon([(x-30,y+150),(x,y+110),(x+30,y+150)],fill=gold+(255,))
            fr=pop(fr,C,(x-105,y-5,x+105,y+185),back((t-st)/0.35))
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3,4]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b19-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y19{i}.png')
