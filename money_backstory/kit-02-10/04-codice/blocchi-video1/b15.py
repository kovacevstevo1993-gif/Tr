from common import *
import shutil
S=["Here's what to do today.","Go to ssa.gov and open your free my Social Security account.","It shows your personal estimate at every age from 62 to 70.","Look at your numbers, think about your health and your spouse, and then make this decision with your eyes wide open."]
TOTF=571
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0]+fs[1],fs[2],fs[3]]; print(fs,durs,sum(durs)); s2=fs[0]/30
bg=make_bg(); bgg=make_bg(grid=True)
def drawA(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,"HERE'S WHAT TO DO TODAY",SER(80),110,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    if t>s2:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(C); x0,y0,x1,y1=W/2-620,280,W/2+620,860
        d.rounded_rectangle([x0,y0,x1,y1],radius=26,fill=(236,240,245,255)); d.rounded_rectangle([x0,y0,x1,y0+80],radius=26,fill=(200,208,220,255)); d.rectangle([x0,y0+50,x1,y0+80],fill=(200,208,220,255))
        for k,c in enumerate([(232,84,84),(230,180,70),(84,200,124)]): d.ellipse([x0+30+k*40,y0+28,x0+54+k*40,y0+52],fill=c+(255,))
        d.rounded_rectangle([x0+180,y0+18,x1-40,y0+62],radius=22,fill=(255,255,255,255))
        typed='ssa.gov'[:int(len('ssa.gov')*ease((t-s2-0.2)/0.8))]; txt(C,typed,BOLD(34),y0+24,navy,255,x=x0+210,anchor='l')
        txt(C,'my Social Security',BOLD(80),y0+180,navy,255*ease((t-s2-1.0)/0.4))
        if t>s2+1.4:
            f=BOLD(50); lab='OPEN YOUR FREE ACCOUNT'; b=d.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+90; bx=(W-bw)/2; by=y0+340
            d.rounded_rectangle([bx,by,bx+bw,by+110],radius=55,fill=green+(255,)); d.text((bx+45-b[0],by+55-(b[3]-b[1])/2-b[1]),lab,font=f,fill=navy+(255,))
        fr=pop(fr,C,(int(x0)-5,y0-5,int(x1)+5,y1+5),back((t-s2)/0.45))
    return fr
def drawB(t):
    fr=bgg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'YOUR PERSONAL ESTIMATE AT EVERY AGE',SER(60),80,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    for i,age in enumerate(range(62,71)):
        st=0.3+i*0.28
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(C); x=W/2+(i-4)*190; h=200+i*55; base=880
        col=tuple(int(red[k]+(green[k]-red[k])*i/8) for k in range(3))
        d.rounded_rectangle([x-70,base-h,x+70,base],radius=16,fill=col+(255,))
        txt(C,'$?',BOLD(44),base-h-60,white,255,x=x); txt(C,str(age),BOLD(40),base+20,white,255,x=x)
        fr=pop(fr,C,(int(x-75),base-h-70,int(x+75),base+70),back((t-st)/0.4))
    return fr
def drawC(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'BEFORE YOU DECIDE, CHECK:',SER(66),110,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    D=fs[3]/30
    for i,(lab,st) in enumerate([('YOUR NUMBERS',0.2),('YOUR HEALTH',D*0.18),('YOUR SPOUSE',D*0.33)]):
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(C); x=W/2+(i-1)*520; y=300
        d.rounded_rectangle([x-230,y,x+230,y+260],radius=30,fill=card+(255,),outline=gold+(255,),width=4)
        cx,cy=x,y+95; d.ellipse([cx-50,cy-50,cx+50,cy+50],fill=green+(255,)); d.line([(cx-24,cy),(cx-6,cy+20),(cx+26,cy-20)],fill=navy+(255,),width=13,joint='curve')
        txt(C,lab,BOLD(44),y+180,white,255,x=x)
        fr=pop(fr,C,(int(x-235),y-5,int(x+235),y+265),back((t-st)/0.45))
    if t>D*0.55:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(C); f=BOLD(58); lab='DECIDE WITH YOUR EYES WIDE OPEN'; b=d.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+100; bx=(W-bw)/2; y=720
        d.rounded_rectangle([bx,y,bx+bw,y+130],radius=65,fill=gold+(255,)); d.text((bx+50-b[0],y+65-(b[3]-b[1])/2-b[1]),lab,font=f,fill=navy+(255,))
        fr=pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,y+135),back((t-D*0.55)/0.45))
    return fr
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],durs),1):
    render(fn,f/30,f'/mnt/user-data/outputs/v1-b15-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/x15{i}.png')
