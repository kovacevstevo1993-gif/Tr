from common import *
import shutil
s=["So far, waiting looks like a clear winner.","But before you decide, you need to know the traps.","Because some of them can wipe out the advantage of waiting, and one of them can quietly hurt your spouse for decades."]
w=[len(x)+10 for x in s]; T=sum(w); D=15.0; d=[x/T*D for x in w]; st=[sum(d[:i]) for i in range(3)]
DA=d[0]; DB=d[1]+d[2]; s3=d[1]
print(round(DA,2),round(DB,2))
bg=make_bg()
def drawA(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); dd=ImageDraw.Draw(L)
    a=ease(t/0.4); txt(L,'SO FAR...',SER(70),200,goldL,255*a)
    fr=Image.alpha_composite(fr,L)
    if t>0.5:
        S=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(S); cx,cy=W/2,560; r=150
        sd.ellipse([cx-r,cy-r,cx+r,cy+r],fill=green+(255,)); sd.line([(cx-70,cy),(cx-15,cy+60),(cx+80,cy-60)],fill=navy+(255,),width=34,joint='curve')
        fr=pop(fr,S,(int(cx-r-5),int(cy-r-5),int(cx+r+5),int(cy+r+5)),back((t-0.5)/0.45))
    if t>1.0:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'WAITING LOOKS LIKE THE WINNER',BOLD(60),790,white,255*ease((t-1.0)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
def warn(d,cx,cy,s,col):
    d.polygon([(cx,cy-130*s),(cx+150*s,cy+120*s),(cx-150*s,cy+120*s)],fill=col+(255,))
    d.rounded_rectangle([cx-14*s,cy-50*s,cx+14*s,cy+50*s],radius=int(10*s),fill=navy+(255,)); d.ellipse([cx-16*s,cy+68*s,cx+16*s,cy+100*s],fill=navy+(255,))
def drawB(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0))
    a=ease(t/0.4); txt(L,'03',BOLD(120),90,red,255*a); txt(L,'THE HIDDEN TRAPS',BOLD(64),230,white,255*a); fr=Image.alpha_composite(fr,L)
    S=Image.new('RGBA',(W,H),(0,0,0,0)); warn(ImageDraw.Draw(S),W/2,480,1.0,red); fr=pop(fr,S,(W//2-160,340,W//2+160,610),back((t-0.4)/0.45))
    for i,(lab,col,stt) in enumerate([('SOME CAN WIPE OUT THE ADVANTAGE OF WAITING',gold,s3+0.2),('ONE CAN HURT YOUR SPOUSE FOR DECADES',red,s3+4.2)]):
        if t<stt: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); y=690+i*140
        f=BOLD(46); b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+90; bx=(W-bw)/2
        cd.rounded_rectangle([bx,y,bx+bw,y+100],radius=50,fill=card+(255,),outline=col+(255,),width=4)
        cd.text((bx+45-b[0],y+50-(b[3]-b[1])/2-b[1]),lab,font=f,fill=white+(255,))
        fr=pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,y+105),back((t-stt)/0.45))
    return fr
render(drawA,DA,'/mnt/user-data/outputs/v1-b7-01.mp4'); shutil.copy(f'/home/claude/_fr/{int(DA*30)-3:04d}.png','/home/claude/x7a.png')
render(drawB,DB,'/mnt/user-data/outputs/v1-b7-02.mp4'); shutil.copy(f'/home/claude/_fr/{int(DB*30)-3:04d}.png','/home/claude/x7b.png')
