from common import *
import shutil
S=["So who should claim early?","It can make sense if your health is poor, if you're single and no one depends on your benefit, or if you truly need the income now and have no other savings.","Claiming early is not a failure.","For some people, it's the smartest choice they can make."]
TOTF=523
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0],fs[1],fs[2]+fs[3]]; print(fs,durs,sum(durs))
s4=fs[2]/30
bg=make_bg()
def drawA(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); a=ease(t/0.3)
    txt(L,'04',BOLD(140),200,blue,255*a); txt(L,'EARLY OR WAIT?',BOLD(64),370,white,255*a)
    txt(L,'WHO SHOULD CLAIM EARLY?',SER(80),600,goldL,255*ease((t-0.5)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
def drawB(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'CLAIMING EARLY CAN MAKE SENSE IF...',SER(64),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    D=fs[1]/30
    items=[('YOUR HEALTH IS POOR',0.3),("YOU'RE SINGLE — NO ONE DEPENDS ON YOUR BENEFIT",D*0.2),('YOU NEED THE INCOME NOW — NO OTHER SAVINGS',D*0.55)]
    for i,(lab,st) in enumerate(items):
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); y=280+i*210
        cd.rounded_rectangle([200,y,W-200,y+160],radius=30,fill=card+(255,),outline=blue+(255,),width=4)
        cd.ellipse([250,y+35,340,y+125],fill=blue+(255,)); txt(C,str(i+1),BOLD(56),y+50,navy,255,x=295)
        txt(C,lab,BOLD(48),y+55,white,255,x=390,anchor='l')
        fr=pop(fr,C,(195,y-5,W-195,y+165),back((t-st)/0.45))
    return fr
def drawC(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'CLAIMING EARLY IS NOT A FAILURE.',SER(84),260,white,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    if t>s4:
        S2=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(S2); cx,cy,r=W/2,560,110
        sd.ellipse([cx-r,cy-r,cx+r,cy+r],fill=green+(255,)); sd.line([(cx-50,cy),(cx-10,cy+42),(cx+58,cy-44)],fill=navy+(255,),width=26,joint='curve')
        fr=pop(fr,S2,(int(cx-r-5),int(cy-r-5),int(cx+r+5),int(cy+r+5)),back((t-s4)/0.45))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,"FOR SOME, IT'S THE SMARTEST CHOICE",BOLD(58),760,green,255*ease((t-s4-0.3)/0.4)); fr=Image.alpha_composite(fr,L)
    return fr
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],durs),1):
    render(fn,f/30,f'/mnt/user-data/outputs/v1-b13-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/x13{i}.png')
