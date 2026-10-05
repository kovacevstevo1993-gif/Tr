from common import *
bg=make_bg(grid=True)
base=860; bw=230; gap=330
vals=[2000,2160,2320,2480]; ages=[67,68,69,70]; maxh=520
cols=[white,(170,215,180),(120,205,150),green]
bars=[bar(v/2480*maxh,c,bw) for v,c in zip(vals,cols)]
xs=[W/2+(i-1.5)*gap for i in range(4)]
def draw(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    a=ease(t/0.5); txt(L,'WAIT PAST 67:  +8% EVERY YEAR',SER(70),90,goldL,255*a)
    d.line([220,base,W-220,base],fill=gold+(255,),width=4); fr=Image.alpha_composite(fr,L)
    for i in range(4):
        st=0.5+i*1.2; p=ease((t-st)/0.8)
        if p<=0: continue
        if i==3 and t>6.0:
            pul=0.5+0.5*math.sin((t-6.0)*3)
            gl=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(gl).rounded_rectangle([xs[i]-bw/2-12,base-bars[i].height-12,xs[i]+bw/2+12,base],radius=26,fill=green+(int(80+80*pul),))
            fr=Image.alpha_composite(fr,gl.filter(ImageFilter.GaussianBlur(28)))
        im=bars[i].resize((bw,max(2,int(bars[i].height*p)))); fr.alpha_composite(im,(int(xs[i]-bw/2),base-im.height))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); top=base-im.height
        big = (i==3 and t>6.0)
        txt(L,f'${int(vals[i]*p/10)*10:,}',BOLD(96 if big else 70),top-(130 if big else 100),green if i==3 else white,255*min(1,p*2),x=xs[i])
        txt(L,f'AGE {ages[i]}',BOLD(40),base+25,white,255*p,x=xs[i])
        if i>0: txt(L,'+8%',BOLD(34),top+20,navy,255*p,x=xs[i])
        fr=Image.alpha_composite(fr,L)
    if t>6.6:
        s=back((t-6.6)/0.45); S=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(S)
        lab='AT 70: $2,480 A MONTH'; f=BOLD(46); b=sd.textbbox((0,0),lab,font=f); bw2=b[2]-b[0]+70; bh=92; bx=(W-bw2)/2; by=950
        sd.rounded_rectangle([bx,by,bx+bw2,by+bh],radius=46,fill=green+(255,)); sd.text((bx+35-b[0],by+bh/2-(b[3]-b[1])/2-b[1]),lab,font=f,fill=navy+(255,))
        fr=pop(fr,S,(int(bx)-5,by-5,int(bx+bw2)+5,by+bh+5),s)
    return fr
render(draw,11.79,'/mnt/user-data/outputs/v1-b3-03.mp4')
