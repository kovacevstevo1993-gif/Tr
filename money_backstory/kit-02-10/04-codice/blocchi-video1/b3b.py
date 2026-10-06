from common import *
bg=make_bg(grid=True)
base=860; bw=300
B67=bar(460,white,bw); B62=bar(460*0.7,red,bw)
x67=W/2+300; x62=W/2-300
def draw(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    a=ease(t/0.5); txt(L,'YOUR FULL BENEFIT AT 67',SER(70),90,goldL,255*a)
    d.line([220,base,W-220,base],fill=gold+(255,),width=4)
    fr=Image.alpha_composite(fr,L)
    p=ease((t-0.6)/1.6)
    if p>0:
        h=int(B67.height*p); im=B67.resize((bw,max(2,h))); fr.alpha_composite(im,(int(x67-bw/2),base-im.height))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); v=int(2000*p/10)*10
        txt(L,f'${v:,}',BOLD(100),base-im.height-150,white,255,x=x67); txt(L,'per month',REG(34),base-im.height-40,grey,255,x=x67)
        txt(L,'CLAIM AT 67',BOLD(42),base+25,white,255,x=x67); fr=Image.alpha_composite(fr,L)
    q=ease((t-4.95)/1.4)
    if q>0:
        h=int(B62.height*q); im=B62.resize((bw,max(2,h))); fr.alpha_composite(im,(int(x62-bw/2),base-im.height))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pc=int(70*q)
        top=base-im.height
        if t<9.55:
            txt(L,f'{pc}%',BOLD(100),top-150,red,255,x=x62); txt(L,'of your benefit',REG(34),top-40,grey,255,x=x62)
        else:
            k=ease((t-9.55)/1.0); v=int(1400*k/10)*10
            txt(L,f'${v:,}',BOLD(100),top-150,red,255,x=x62); txt(L,'per month',REG(34),top-40,grey,255,x=x62)
        txt(L,'CLAIM AT 62',BOLD(42),base+25,white,255,x=x62); fr=Image.alpha_composite(fr,L)
    if t>11.0:
        s=back((t-11.0)/0.45)
        S=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(S)
        lab='−30% FOR THE REST OF YOUR LIFE'; f=BOLD(44); b=sd.textbbox((0,0),lab,font=f); bw2=b[2]-b[0]+70; bh=90; bx=(W-bw2)/2; by=950
        sd.rounded_rectangle([bx,by,bx+bw2,by+bh],radius=45,fill=red+(255,))
        sd.text((bx+35-b[0],by+bh/2-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(255,255,255,255))
        fr=pop(fr,S,(int(bx)-5,by-5,int(bx+bw2)+5,by+bh+5),s)
    return fr
render(draw,14.64,'/mnt/user-data/outputs/v1-b3-02.mp4')
