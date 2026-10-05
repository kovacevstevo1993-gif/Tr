from common import *
import random
random.seed(7)
M=46  # frame margin
def _frame_layers():
    # outer gold glow
    glow=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
    gd.rounded_rectangle([M-6,M-6,W-M+6,H-M+6],radius=38,outline=(230,185,90,200),width=26)
    glow=glow.filter(ImageFilter.GaussianBlur(22))
    # bevel ring: vertical+horizontal gradient
    grad=Image.new('RGBA',(W,H)); g2=ImageDraw.Draw(grad)
    for y in range(H):
        t=y/H
        c=(int(255-95*t),int(226-100*t),int(150-95*t))
        g2.line([0,y,W,y],fill=c+(255,))
    ring=Image.new('L',(W,H),0); rd=ImageDraw.Draw(ring)
    rd.rounded_rectangle([M,M,W-M,H-M],radius=34,fill=255); rd.rounded_rectangle([M+16,M+16,W-M-16,H-M-16],radius=22,fill=0)
    bevel=Image.new('RGBA',(W,H),(0,0,0,0)); bevel.paste(grad,(0,0),ring)
    # highlight line + inner shadow
    hl=Image.new('RGBA',(W,H),(0,0,0,0)); hd=ImageDraw.Draw(hl)
    hd.rounded_rectangle([M+3,M+3,W-M-3,H-M-3],radius=32,outline=(255,245,200,160),width=2)
    hd.rounded_rectangle([M+16,M+16,W-M-16,H-M-16],radius=22,outline=(90,60,15,255),width=3)
    inner=Image.new('RGBA',(W,H),(0,0,0,0)); idd=ImageDraw.Draw(inner)
    idd.rounded_rectangle([M+16,M+16,W-M-16,H-M-16],radius=22,outline=(0,0,0,200),width=30)
    inner=inner.filter(ImageFilter.GaussianBlur(18))
    m=Image.new('L',(W,H),0); ImageDraw.Draw(m).rounded_rectangle([M+16,M+16,W-M-16,H-M-16],radius=22,fill=255)
    inner.putalpha(Image.composite(inner.split()[3],Image.new('L',(W,H),0),m))
    # outside dark
    out=Image.new('RGBA',(W,H),(4,10,18,255)); om=Image.new('L',(W,H),255); ImageDraw.Draw(om).rounded_rectangle([M,M,W-M,H-M],radius=34,fill=0)
    out.putalpha(om)
    return out,glow,bevel,hl,inner
_FR=_frame_layers()
_OV=Image.new('RGBA',(W,H),(0,0,0,0))
for _l in [_FR[4],_FR[0],_FR[1],_FR[2],_FR[3]]: _OV=Image.alpha_composite(_OV,_l)
_SW=Image.new('RGBA',(W+1400,H),(0,0,0,0)); ImageDraw.Draw(_SW).polygon([(700,0),(920,0),(520,H),(300,H)],fill=(255,230,160,18)); _SW=_SW.filter(ImageFilter.GaussianBlur(40))
BG=make_bg(grid=True)
parts=[(random.uniform(0,W),random.uniform(0,H),random.uniform(1.5,4),random.uniform(8,25),random.uniform(0,6.28)) for _ in range(55)]
def base(t):
    fr=BG.copy()
    off=int((t*140)%(W+800)); fr.alpha_composite(_SW.crop((1100-off+400, 0, 1100-off+400+W, H)) if False else _SW.crop((max(0,min(W+1400-W, 1100-off)),0,max(0,min(W+1400-W,1100-off))+W,H)))
    P=Image.new('RGBA',(W,H),(0,0,0,0)); pd=ImageDraw.Draw(P)
    for (px,py,r,sp,ph) in parts:
        y=(py-t*sp)%H; a=int(70+60*math.sin(t*1.5+ph))
        pd.ellipse([px-r,y-r,px+r,y+r],fill=(246,214,140,a))
    return Image.alpha_composite(fr,P)
def frame(fr):
    return Image.alpha_composite(fr,_OV)
