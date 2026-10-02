from common2 import *
import shutil, sys
S=["Mistake number five: forgetting who else owns part of your savings.","If most of your money is in a traditional 401k or IRA, it's not all yours.","Every dollar you take out is taxed as ordinary income.","So a one million dollar balance is not one million dollars you can spend.","Depending on your tax bracket, a big slice of it belongs to the IRS."]
TOTF=787
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0],fs[1]+fs[2],fs[3]+fs[4]]; print(fs,durs,sum(durs))
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'MISTAKE #5',BOLD(120),150,green,255*ease(t/0.35))
    cx,cy,R=W/2,520,140; d.ellipse([cx-R,cy-R,cx+R,cy+R],fill=green+(255,))
    a=-90+80*(0.8+0.2*math.sin(t*3)); d.pieslice([cx-R,cy-R,cx+R,cy+R],-90,a,fill=red+(255,))
    txt(L,'?',BOLD(70),cy-R-30,red,255,x=cx+R*0.6)
    txt(L,'WHO ELSE OWNS PART OF YOUR SAVINGS?',BOLD(52),730,white,255*ease((t-0.3)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'TRADITIONAL 401(K) OR IRA',SER(66),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x0,y0=260,280
    cd.rounded_rectangle([x0,y0,x0+560,y0+420],radius=30,fill=card+(255,),outline=gold+(255,),width=5)
    txt(C,'YOUR ACCOUNT',BOLD(42),y0+40,gold,255,x=x0+280); txt(C,'$$$',BOLD(130),y0+130,green,255,x=x0+280)
    txt(C,"it's not all yours",REG(36),y0+320,white,255*ease((t-1.5)/0.4),x=x0+280)
    fr=pop(fr,C,(x0-5,y0-5,x0+565,y0+425),back(t/0.45))
    s3=fs[1]/30
    if t>s3:
        p=ease((t-s3)/0.8); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
        d.line([860,490,860+300*p,490],fill=gold+(255,),width=14)
        if p>0.9: d.polygon([(1170,460),(1210,490),(1170,520)],fill=gold+(255,))
        txt(L,'EVERY WITHDRAWAL',BOLD(34),420,white,255*p,x=1010)
        fr=Image.alpha_composite(fr,L)
        if t>s3+0.8:
            C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx,cy=1450,490
            cd.rounded_rectangle([cx-220,cy-150,cx+220,cy+150],radius=30,fill=red+(255,))
            txt(C,'TAXED AS',BOLD(52),cy-100,(255,255,255),255,x=cx); txt(C,'ORDINARY',BOLD(52),cy-35,(255,255,255),255,x=cx); txt(C,'INCOME',BOLD(52),cy+30,(255,255,255),255,x=cx)
            fr=pop(fr,C,(cx-225,cy-155,cx+225,cy+155),back((t-s3-0.8)/0.4))
    return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'$1,000,000 IN A 401(K)...',SER(66),100,goldL,255*ease(t/0.4))
    cx,cy,R=620,560,280
    d.ellipse([cx-R,cy-R,cx+R,cy+R],fill=green+(255,))
    txt(L,'$1,000,000',BOLD(60),cy-30,navy,255,x=cx)
    fr=Image.alpha_composite(fr,L)
    s5=fs[3]/30
    if t>1.2:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'IS NOT $1,000,000',BOLD(70),330,white,255*ease((t-1.2)/0.4),x=1300); txt(L,'YOU CAN SPEND',BOLD(70),420,white,255*ease((t-1.4)/0.4),x=1300); fr=Image.alpha_composite(fr,L)
    if t>s5:
        p=ease((t-s5)/1.0); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
        off=30*p; a1=-90; a2=-90+80*p; mid=math.radians((a1+a2)/2)
        ox,oy=math.cos(mid)*off,math.sin(mid)*off
        d.pieslice([cx-R+ox,cy-R+oy,cx+R+ox,cy+R+oy],a1,a2,fill=red+(255,))
        if p>0.8:
            txt(L,'IRS',BOLD(60),cy-R*0.62+oy-30,(255,255,255),255,x=cx+R*0.42+ox)
        fr=Image.alpha_composite(fr,L)
        if t>s5+1.2:
            L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'THE IRS SHARE DEPENDS ON YOUR TAX BRACKET',880,col=red,alpha=255*ease((t-s5-1.2)/0.4),size=40)
            fr=Image.alpha_composite(fr,L)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'Illustration only',REG(24),985,grey,200); fr=Image.alpha_composite(fr,L)
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b20-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y20{i}.png')
