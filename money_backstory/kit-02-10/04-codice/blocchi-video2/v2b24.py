from common2 import *
import shutil, sys
S=["Here's your five step checklist.","One: plan for your money to last until at least ninety five.","Two: give health care its own line in your budget.","Three: keep a few years of spending safe, and let the rest grow.","Four: make a long term care plan before you need it.","Five: plan your withdrawals and taxes years in advance.","Write these five down, and check them once a year.","And do it together with your spouse, because every one of these mistakes hits a couple twice as hard."]
TOTF=1081
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[sum(fs[:6]),fs[6]+fs[7]]; st=[sum(fs[:i])/30 for i in range(8)]; print(fs,durs,sum(durs))
purple=(170,130,230)
rows=[('PLAN FOR YOUR MONEY TO LAST UNTIL 95+',gold),('GIVE HEALTH CARE ITS OWN BUDGET LINE',blue),('KEEP A FEW YEARS SAFE, LET THE REST GROW',red),('MAKE A LONG-TERM CARE PLAN EARLY',purple),('PLAN WITHDRAWALS & TAXES IN ADVANCE',green)]
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'YOUR 5-STEP CHECKLIST',SER(72),85,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    for i,(lab,col) in enumerate(rows):
        s0=st[i+1]
        if t<s0: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); y=210+i*150
        cd.rounded_rectangle([190,y,W-190,y+125],radius=30,fill=card+(255,),outline=col+(255,),width=4)
        cd.rounded_rectangle([225,y+22,305,y+102],radius=16,outline=col+(255,),width=6)
        p=ease((t-s0-0.5)/0.4)
        if p>0: 
            pts=[(240,y+62),(262,y+86),(292,y+36)]; cd.line(pts[:2] if p<0.5 else pts,fill=green+(255,),width=12,joint='curve')
        txt(C,str(i+1),BOLD(56),y+30,col,255,x=360)
        txt(C,lab,BOLD(40),y+42,white,255,x=420,anchor='l')
        fr=pop(fr,C,(185,y-5,W-185,y+130),back((t-s0)/0.4))
    return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    # calendar
    cx,cy=W/2-420,420; a=ease(t/0.4)
    d.rounded_rectangle([cx-170,cy-150,cx+170,cy+170],radius=26,fill=(236,240,245,int(255*a))); d.rounded_rectangle([cx-170,cy-150,cx+170,cy-70],radius=26,fill=red+(int(255*a),)); d.rectangle([cx-170,cy-100,cx+170,cy-70],fill=red+(int(255*a),))
    txt(L,'1x',BOLD(100),cy-40,navy,255*a,x=cx); txt(L,'PER YEAR',BOLD(34),cy+90,navy,255*a,x=cx)
    txt(L,'WRITE THEM DOWN.',BOLD(56),330,white,255*a,x=W/2-150,anchor='l'); txt(L,'CHECK THEM ONCE A YEAR.',BOLD(56),420,goldL,255*ease((t-0.8)/0.4),x=W/2-150,anchor='l')
    fr=Image.alpha_composite(fr,L)
    s8=fs[6]/30
    if t>s8:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); b=ease((t-s8)/0.5)
        for k,col in enumerate([(236,240,245),(230,140,190)]):
            x=W/2-420+(k*2-1)*80; y=780
            d.ellipse([x-38,y-110,x+38,y-34],fill=col+(int(255*b),)); d.rounded_rectangle([x-62,y-24,x+62,y+90],radius=45,fill=col+(int(255*b),))
        txt(L,'DO IT TOGETHER',BOLD(58),700,white,255*b,x=W/2-150,anchor='l')
        txt(L,'every mistake hits a couple',REG(40),790,grey,255*ease((t-s8-0.6)/0.4),x=W/2-150,anchor='l')
        fr=Image.alpha_composite(fr,L)
        if t>s8+2.2:
            S2=Image.new('RGBA',(W,H),(0,0,0,0)); txt(S2,'TWICE AS HARD',BOLD(66),860,red,x=W/2-150,anchor='l')
            fr=Image.alpha_composite(fr,S2) if False else pop(fr,S2,(int(W/2-160),840,1760,960),back((t-s8-2.2)/0.4))
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2]
for i,(fn,f) in enumerate(zip([drawA,drawB],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b24-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y24{i}.png')
