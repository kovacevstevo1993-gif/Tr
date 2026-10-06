from common import *
import shutil
S=["Trap number two is the one most married couples miss.","When one spouse dies, the survivor doesn't keep both checks.","They keep only the larger one.","So if the higher earner claims at 62, that reduced check can shrink what the surviving spouse receives for the rest of their life.","By waiting, the higher earner isn't just raising their own check.","They're protecting the person they love."]
TOTF=774
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
groups=[[0],[1,2],[3],[4,5]]; durs=[sum(fs[i] for i in g) for g in groups]; print(fs,durs,sum(durs))
s3=fs[1]/30; s6=fs[4]/30
bg=make_bg()
def person(d,cx,cy,col,s=1):
    d.ellipse([cx-40*s,cy-120*s,cx+40*s,cy-40*s],fill=col); d.rounded_rectangle([cx-70*s,cy-25*s,cx+70*s,cy+100*s],radius=int(50*s),fill=col)
def drawA(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); a=ease(t/0.4)
    txt(L,'TRAP #2',BOLD(140),110,red,255*a)
    person(d,W/2-120,460,white+(int(255*a),)); person(d,W/2+120,460,gold+(int(255*a),))
    fr=Image.alpha_composite(fr,L)
    # unlocked card
    if t>0.6:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C)
        cd.rounded_rectangle([W/2-560,660,W/2+560,820],radius=30,fill=card+(255,),outline=gold+(255,),width=4)
        txt(C,'THE SURVIVOR CHECK RULE',BOLD(58),710,white)
        lx,ly=W/2+500,745; cd.rounded_rectangle([lx-34,ly-10,lx+34,ly+42],radius=8,fill=gold+(255,)); cd.arc([lx-24,ly-70,lx+24,ly-14],180,300,fill=gold+(255,),width=9)
        fr=pop(fr,C,(int(W/2-565),655,int(W/2+565),825),back((t-0.6)/0.45))
    if t>1.3:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'MOST MARRIED COUPLES MISS THIS',BOLD(44),890,gold,255*ease((t-1.3)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
def check(C,cx,cy,lab,val,col,alpha=255):
    d=ImageDraw.Draw(C); d.rounded_rectangle([cx-300,cy-150,cx+300,cy+150],radius=26,fill=card+(int(alpha),),outline=col+(int(alpha),),width=5)
    txt(C,lab,BOLD(40),cy-110,white,alpha,x=cx); txt(C,val,BOLD(110),cy-40,col,alpha,x=cx); txt(C,'per month',REG(32),cy+95,grey,alpha,x=cx)
def drawB(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'WHEN ONE SPOUSE DIES...',SER(72),110,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    fade=1-ease((t-s3+0.2)/0.6)
    C=Image.new('RGBA',(W,H),(0,0,0,0)); check(C,W/2-360,520,'CHECK 1',"$2,480",green)
    check(C,W/2+360,520,'CHECK 2',"$1,200",blue,255*max(fade,0.25)); fr=Image.alpha_composite(fr,C)
    if t>s3-0.2:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); p=ease((t-s3+0.2)/0.4); x=W/2+360; r=200*p
        d.line([x-r,520-r*0.7,x+r,520+r*0.7],fill=red+(230,),width=22); d.line([x-r,520+r*0.7,x+r,520-r*0.7],fill=red+(230,),width=22); fr=Image.alpha_composite(fr,L)
        fr_=fr
    if t>1.0:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'THE SURVIVOR DOESN\'T KEEP BOTH',BOLD(48),760,white,255*ease((t-1.0)/0.4)); fr=Image.alpha_composite(fr,L)
    if t>s3:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); dd=ImageDraw.Draw(C); f=BOLD(50); lab='ONLY THE LARGER ONE'; b=dd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+90; bx=(W-bw)/2; y=860
        dd.rounded_rectangle([bx,y,bx+bw,y+100],radius=50,fill=green+(255,)); dd.text((bx+45-b[0],y+50-(b[3]-b[1])/2-b[1]),lab,font=f,fill=navy+(255,))
        fr=pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,y+105),back((t-s3)/0.45))
    return fr
def drawC(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'IF THE HIGHER EARNER CLAIMS AT 62',SER(64),110,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    C=Image.new('RGBA',(W,H),(0,0,0,0))
    if t>0.6:
        check(C,W/2-400,500,'CLAIMED AT 70','$2,480',green,255*ease((t-0.6)/0.4))
    if t>1.6:
        check(C,W/2+400,500,'CLAIMED AT 62','REDUCED',red,255*ease((t-1.6)/0.4))
    fr=Image.alpha_composite(fr,C)
    if t>2.6:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); x=W/2+400; p=ease((t-2.6)/0.6)
        d.line([x,690,x,690+110*p],fill=red+(255,),width=14)
        if p>0.9: d.polygon([(x-30,780),(x+30,780),(x,830)],fill=red+(255,))
        fr=Image.alpha_composite(fr,L)
    if t>3.6:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'SMALLER SURVIVOR CHECK — FOR LIFE',BOLD(52),880,red,255*ease((t-3.6)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
def drawD(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'WAITING ISN\'T JUST ABOUT YOUR CHECK',SER(62),130,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    if t>0.5:
        S2=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(S2); cx,cy=W/2,520
        d.polygon([(cx,cy-190),(cx+170,cy-120),(cx+150,cy+80),(cx,cy+200),(cx-150,cy+80),(cx-170,cy-120)],fill=gold+(255,))
        # heart
        r=48; d.ellipse([cx-2*r+5,cy-70,cx+5,cy-70+2*r],fill=navy+(255,)); d.ellipse([cx-5,cy-70,cx+2*r-5,cy-70+2*r],fill=navy+(255,)); d.polygon([(cx-2*r+8,cy-10),(cx+2*r-8,cy-10),(cx,cy+100)],fill=navy+(255,))
        fr=pop(fr,S2,(int(cx-175),int(cy-195),int(cx+175),int(cy+205)),back((t-0.5)/0.5))
    if t>s6:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'IT PROTECTS THE PERSON YOU LOVE',BOLD(60),800,white,255*ease((t-s6)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD],durs),1):
    render(fn,f/30,f'/mnt/user-data/outputs/v1-b9-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/x9{i}.png')
