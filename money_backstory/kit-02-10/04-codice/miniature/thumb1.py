from common import *
W2,H2=1280,720
im=Image.new('RGBA',(W2,H2),navy+(255,))
g=Image.new('RGBA',(W2,H2),(0,0,0,0)); ImageDraw.Draw(g).ellipse([140,-100,1140,820],fill=(34,66,104,255)); im=Image.alpha_composite(im,g.filter(ImageFilter.GaussianBlur(160)))
d=ImageDraw.Draw(im)
def t(s,f,x,y,col,anchor='l',stroke=0):
    b=d.textbbox((0,0),s,font=f); w=b[2]-b[0]
    X=x-b[0] if anchor=='l' else (x-w/2-b[0] if anchor=='c' else x-w-b[0])
    d.text((X,y-b[1]),s,font=f,fill=col,stroke_width=stroke,stroke_fill=(0,0,0))
    return b[3]-b[1]
# top label
t('WHEN TO CLAIM?',BOLD(64),W2/2,40,goldL,'c',stroke=3)
# big 62 vs 70
t('62',BOLD(300),80,150,red,stroke=6)
t('vs',SER(110),W2/2,330,white,'c')
t('70',BOLD(300),W2-80,150,green,'r',stroke=6)
# arrows
d.polygon([(495,280),(565,280),(530,350)],fill=red); d.rectangle([515,180,545,282],fill=red)
d.polygon([(W2-495,250),(W2-565,250),(W2-530,180)],fill=green); d.rectangle([W2-545,248,W2-515,350],fill=green)
# money badge
f=BOLD(70); lab='$124,800 DIFFERENCE'; b=d.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+80; bx=(W2-bw)/2; by=540
d.rounded_rectangle([bx+8,by+10,bx+bw+8,by+130],radius=40,fill=(0,0,0,160))
d.rounded_rectangle([bx,by,bx+bw,by+120],radius=40,fill=gold)
d.text((bx+40-b[0],by+60-(b[3]-b[1])/2-b[1]),lab,font=f,fill=navy)
im.convert('RGB').save('/mnt/user-data/outputs/miniatura-video1.png')
im.convert('RGB').resize((320,180)).save('/home/claude/thumb_small.png')
