from PIL import Image, ImageDraw, ImageFont, ImageFilter
import subprocess, os, shutil, math
W,H=1920,1080; F='/mnt/skills/examples/canvas-design/canvas-fonts/'
navy=(10,24,40); gold=(212,172,82); goldL=(246,214,140); white=(236,240,245); red=(232,84,84); green=(84,200,124); grey=(150,165,185); blue=(110,160,230); card=(22,40,64)
FPS=30
def font(n,s): return ImageFont.truetype(F+n,s)
SER=lambda s: font('Gloock-Regular.ttf',s); BOLD=lambda s: font('InstrumentSans-Bold.ttf',s); REG=lambda s: font('InstrumentSans-Regular.ttf',s)
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
def back(t):
    t=max(0,min(1,t)); c1=1.70158; c3=c1+1; return 1+c3*(t-1)**3+c1*(t-1)**2
def make_bg(grid=False):
    bg=Image.new('RGBA',(W,H),navy+(255,))
    g=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W/2-950,H/2-520,W/2+950,H/2+520],fill=(32,62,98,255))
    bg=Image.alpha_composite(bg,g.filter(ImageFilter.GaussianBlur(230)))
    v=Image.new('RGBA',(W,H),(0,0,0,0)); vd=ImageDraw.Draw(v); vd.rectangle([0,0,W,H],fill=(0,0,0,120)); vd.ellipse([-200,-150,W+200,H+150],fill=(0,0,0,0))
    bg=Image.alpha_composite(bg,v.filter(ImageFilter.GaussianBlur(120)))
    if grid:
        gr=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(gr)
        for y in range(0,H,60): gd.line([0,y,W,y],fill=(255,255,255,8),width=1)
        for x in range(0,W,60): gd.line([x,0,x,H],fill=(255,255,255,8),width=1)
        bg=Image.alpha_composite(bg,gr)
    return bg
def txt(L,t,f,y,col,alpha=255,x=None,anchor='c'):
    d=ImageDraw.Draw(L); b=d.textbbox((0,0),t,font=f); w=b[2]-b[0]
    X=(W-w)/2-b[0] if x is None else (x-w/2-b[0] if anchor=='c' else (x-b[0] if anchor=='l' else x-w-b[0]))
    d.text((X,y-b[1]),t,font=f,fill=col+(int(max(0,min(255,alpha))),)); return w
def pop(fr,layer,box,s):
    s=max(0.01,s); piece=layer.crop(box); pw,ph=piece.size
    piece=piece.resize((max(1,int(pw*s)),max(1,int(ph*s))))
    fr.alpha_composite(piece,(int((box[0]+box[2])/2-piece.width/2),int((box[1]+box[3])/2-piece.height/2))); return fr
def render(draw,dur,out):
    d='/home/claude/_fr'; shutil.rmtree(d,ignore_errors=True); os.makedirs(d)
    N=int(round(FPS*dur))
    for fn in range(N):
        draw(fn/FPS).convert('RGB').save(f'{d}/{fn:04d}.png')
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',f'{d}/%04d.png','-c:v','libx264','-pix_fmt','yuv420p','-crf','18',out],check=True)
def pill(L,text,y,col=gold,alpha=255,size=32,fill=(38,48,52)):
    d=ImageDraw.Draw(L); f=BOLD(size); b=d.textbbox((0,0),text,font=f); pw=b[2]-b[0]+60; ph=b[3]-b[1]+30
    d.rounded_rectangle([(W-pw)/2,y,(W+pw)/2,y+ph],radius=ph/2,fill=fill+(int(alpha),),outline=col+(int(alpha),),width=3)
    d.text(((W-(b[2]-b[0]))/2-b[0],y+15-b[1]),text,font=f,fill=col+(int(alpha),))
def bar(h,col,bw=280):
    im=Image.new('RGBA',(bw,max(2,int(h))),(0,0,0,0)); d=ImageDraw.Draw(im)
    for y in range(im.height):
        t=y/im.height; cc=tuple(int(col[k]*(1-0.38*t)) for k in range(3)); d.line([0,y,bw,y],fill=cc+(255,))
    m=Image.new('L',im.size,0); ImageDraw.Draw(m).rounded_rectangle([0,0,bw-1,im.height-1],radius=min(20,im.height//2),fill=255); im.putalpha(m); return im
