from common import *
bg=make_bg()
def draw(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    # opener chip (0-2.5) moves up
    a=ease(t/0.5); up=ease((t-2.3)/0.6)
    y0=430-int(up*300)
    sc=1-0.35*up
    f1=BOLD(int(130*sc)); f2=BOLD(int(64*sc))
    txt(L,'01',f1,y0,gold,255*a)
    txt(L,'WHAT YOU REALLY GET',f2,y0+int(170*sc),white,255*a)
    fr=Image.alpha_composite(fr,L)
    if t>2.6:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
        b1=ease((t-2.6)/0.5); txt(L,'FULL RETIREMENT AGE',BOLD(52),420,goldL,255*b1)
        fr=Image.alpha_composite(fr,L)
        s=back((t-3.0)/0.5)
        N2=Image.new('RGBA',(W,H),(0,0,0,0)); txt(N2,'67',BOLD(300),500,gold)
        G=N2.filter(ImageFilter.GaussianBlur(26)); fr=pop(fr,G,(W//2-300,480,W//2+300,860),s); fr=pop(fr,N2,(W//2-300,480,W//2+300,860),s)
        c=ease((t-4.0)/0.5)
        if c>0:
            L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'IF YOU WERE BORN IN 1960 OR LATER',900,alpha=255*c,size=34); fr=Image.alpha_composite(fr,L)
    return fr
render(draw,7.06,'/mnt/user-data/outputs/v1-b3-01.mp4')
