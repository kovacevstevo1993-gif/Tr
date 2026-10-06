from common2 import *
import shutil, sys
S=["Here's the plan.","Mistake one: planning for the wrong number of years.","Mistake two: underestimating health care.","Mistake three: the safe move that isn't safe at all.","Mistake four: the bill Medicare will not pay.","And mistake five: forgetting who else owns part of your savings.","At the end, you'll get a simple five step checklist you can use today."]
TOTF=901
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[sum(fs[:6]),fs[6]]; st=[sum(fs[:i])/30 for i in range(7)]; print(fs,durs,sum(durs))
purple=(170,130,230)
rows=[('PLANNING FOR THE WRONG NUMBER OF YEARS',gold,'hour'),('UNDERESTIMATING HEALTH CARE',blue,'cross'),('THE "SAFE" MOVE THAT ISN\'T SAFE',red,'lock'),('THE BILL MEDICARE WON\'T PAY',purple,'bill'),('WHO ELSE OWNS YOUR SAVINGS',green,'pie')]
def icon(d,kind,cx,cy,col,t):
    c=col+(255,)
    if kind=='hour':
        d.polygon([(cx-26,cy-34),(cx+26,cy-34),(cx,cy)],fill=c); d.polygon([(cx-26,cy+34),(cx+26,cy+34),(cx,cy)],outline=c,width=4)
        f=(math.sin(t*2)+1)/2; d.polygon([(cx-26*f,cy+34-20*f),(cx+26*f,cy+34-20*f),(cx+26,cy+34),(cx-26,cy+34)],fill=c)
    elif kind=='cross':
        d.rounded_rectangle([cx-12,cy-34,cx+12,cy+34],radius=5,fill=c); d.rounded_rectangle([cx-34,cy-12,cx+34,cy+12],radius=5,fill=c)
    elif kind=='lock':
        d.rounded_rectangle([cx-30,cy-6,cx+30,cy+36],radius=8,fill=c); d.arc([cx-22,cy-38,cx+22,cy+8],180,360,fill=c,width=8)
        txt(IMG[0],'?',BOLD(34),cy+2,navy,255,x=cx)
    elif kind=='bill':
        d.rounded_rectangle([cx-26,cy-36,cx+26,cy+36],radius=6,fill=c)
        for k in range(3): d.line([cx-16,cy-18+k*14,cx+16,cy-18+k*14],fill=navy+(255,),width=4)
        txt(IMG[0],'$',BOLD(26),cy+10,navy,255,x=cx)
    elif kind=='pie':
        d.ellipse([cx-34,cy-34,cx+34,cy+34],fill=c); ang=-90+120*(0.8+0.2*math.sin(t*2)); d.pieslice([cx-34,cy-34,cx+34,cy+34],-90,ang,fill=red+(255,))
IMG=[None]
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); IMG[0]=L
    txt(L,"HERE'S THE PLAN",SER(76),95,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    cur=max([i for i in range(5) if t>=st[i+1]] or [-1])
    for i,(lab,col,kind) in enumerate(rows):
        s0=st[i+1]
        if t<s0: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); IMG[0]=C; d=ImageDraw.Draw(C); y=215+i*150; act=(i==cur)
        sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([210,y+10,W-190,y+130],radius=26,fill=(0,0,0,150)); C=Image.alpha_composite(C,sh.filter(ImageFilter.GaussianBlur(10))); IMG[0]=C; d=ImageDraw.Draw(C)
        d.rounded_rectangle([200,y,W-200,y+120],radius=26,fill=((30,54,86) if act else card)+(255,),outline=col+(255,),width=6 if act else 3)
        d.ellipse([235,y+18,319,y+102],fill=col+(255,)); txt(C,str(i+1),BOLD(52),y+30,navy,255,x=277)
        txt(C,'MISTAKE',BOLD(24),y+22,col,255,x=350,anchor='l'); txt(C,lab,BOLD(42),y+52,white,255,x=350,anchor='l')
        icon(d,kind,W-290,y+60,col,t)
        p=back((t-s0)/0.4); ox=int((1-min(1,p))*-120)
        C2=Image.new('RGBA',(W,H),(0,0,0,0)); C2.alpha_composite(C,(ox,0)) if ox else None
        fr=Image.alpha_composite(fr,C2 if ox else C) if p<1 else Image.alpha_composite(fr,C)
    return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'AT THE END: YOUR 5-STEP CHECKLIST',SER(62),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    # clipboard
    C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx=W/2; y0=230
    cd.rounded_rectangle([cx-330,y0,cx+330,y0+700],radius=30,fill=(236,240,245,255)); cd.rounded_rectangle([cx-110,y0-30,cx+110,y0+40],radius=16,fill=gold+(255,))
    for k in range(5):
        yy=y0+100+k*115; cd.rounded_rectangle([cx-270,yy,cx-200,yy+70],radius=12,outline=navy+(255,),width=5)
        cd.rounded_rectangle([cx-170,yy+22,cx+260,yy+48],radius=12,fill=(200,210,225,255))
        p=ease((t-0.6-k*0.45)/0.35)
        if p>0:
            pts=[(cx-258,yy+36),(cx-240,yy+56),(cx-208,yy+14)]
            cd.line(pts[:2] if p<0.5 else pts,fill=green+(255,),width=12,joint='curve')
    fr=pop(fr,C,(int(cx-335),y0-35,int(cx+335),y0+705),back(t/0.45))
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2]
for i,(fn,f) in enumerate(zip([drawA,drawB],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b2-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y2{i}.png')
