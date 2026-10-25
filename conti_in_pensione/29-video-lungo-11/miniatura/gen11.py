# Miniature video 11 (aumento pensioni gennaio 2027, tabella netta). Stile del canale (sfondo verde acqua a raggi, scritte con contorno scuro,
# giallo/rosso/verde, schede con ombra, font del canale) con IMPAGINAZIONE NUOVA rispetto ai video 1-10:
# A = duello "+29 € LORDI" contro "? € NETTI" (paradosso, la risposta resta nascosta), niente tabella a destra, niente striscia bianca;
# B = scala di 5 schede da 600 a 3.000 € con "? €" in ognuna + freccia che sale + tab LE MINIME (la tabella del video).
# Numeri solo quelli detti dal video: 29 € ogni 1.000 € lordi (stima 2,9%), 600-3.000 €, minime. Il netto e' sempre "? €".
# Uso: python3 gen11.py (dalla cartella miniatura). Controlla ogni testo (dentro il quadro, niente sovrapposizioni tra testi).
import asyncio,os,re,sys,math
from playwright.async_api import async_playwright
src=open('../../14-video-lungo-4-invalidita-2027/miniatura/vecchie-45cent/gen.py').read()
HEAD0=re.search(r"HEAD='''(.*?)'''",src,re.S).group(1)
g9=open('../../25-video-lungo-9/miniatura/gen9.py').read()
exec(g9[g9.index("S='stroke"):g9.index("# A: LA BUSTA")])
BASE=HEAD0[:HEAD0.index('<g opacity="0.10"')]
EXTRA='''<defs>
<radialGradient id="bgA" cx="0.5" cy="0.58" r="0.95"><stop offset="0" stop-color="#2DB8BC"/><stop offset="0.5" stop-color="#0D5158"/><stop offset="1" stop-color="#03181B"/></radialGradient>
<linearGradient id="lcard" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#22C48A"/><stop offset="1" stop-color="#0A5F44"/></linearGradient>
<linearGradient id="go" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFF6B8"/><stop offset="0.35" stop-color="#FFD43B"/><stop offset="0.7" stop-color="#E5A100"/><stop offset="1" stop-color="#9A6400"/></linearGradient>
<linearGradient id="goS" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#A36B00"/><stop offset="0.45" stop-color="#FFD43B"/><stop offset="1" stop-color="#8A5A00"/></linearGradient>
<linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0.5"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<radialGradient id="vig" cx="0.5" cy="0.5" r="0.78"><stop offset="0.6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.45"/></radialGradient>
<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FFF3A8" stop-opacity="0.55"/><stop offset="1" stop-color="#FFF3A8" stop-opacity="0"/></radialGradient>
</defs>'''
def rays(cx,cy,n=20,op=0.11):
    o=f'<g opacity="{op}" fill="#fff">'
    for k in range(n):
        a=k*2*math.pi/n;b=a+math.pi/n*0.9;R=1700
        o+=f'<path d="M{cx} {cy} L{cx+R*math.cos(a):.0f} {cy+R*math.sin(a):.0f} L{cx+R*math.cos(b):.0f} {cy+R*math.sin(b):.0f}Z"/>'
    return o+'</g>'
def stack(cx,by,r,n):
    o='';h=r*0.30
    for i in range(n):
        y=by-i*h
        o+=(f'<ellipse cx="{cx}" cy="{y+h}" rx="{r}" ry="{r*0.36}" fill="#7A4D00"/><rect x="{cx-r}" y="{y}" width="{2*r}" height="{h}" fill="url(#goS)"/>'
            f'<ellipse cx="{cx}" cy="{y}" rx="{r}" ry="{r*0.36}" fill="url(#go)" stroke="#B87800" stroke-width="2"/>')
    return f'<g filter="url(#sh)">{o}</g>'
def coin(cx,cy,r,rot=0):
    return (f'<g transform="translate({cx} {cy}) rotate({rot})" filter="url(#sh)"><circle r="{r}" fill="url(#go)" stroke="#fff" stroke-width="{r*0.08}"/>'
            f'<circle r="{r*0.72}" fill="none" stroke="#B87800" stroke-width="{r*0.07}"/>'
            f'<text y="{r*0.3}" class="t" font-size="{r*0.95}" fill="#B87800" text-anchor="middle">€</text></g>')
def T(i,x,y,txt,fs,fill,sw=0,anchor='middle',maxw=None,extra=''):
    st=f'{S} stroke-width="{sw}"' if sw else ''
    mw=f' data-w="{maxw}"' if maxw else ''
    return f'<text id="{i}" x="{x}" y="{y}" class="t" font-size="{fs}" fill="{fill}" text-anchor="{anchor}" {st}{mw} {extra}>{txt}</text>'
def banner(x,y,w,h,rot,fill):
    return f'<g transform="rotate({rot} {x+w/2} {y+h/2})"><g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="#fff" stroke-width="6"/></g></g>'
# ---------------------------------------------------------------- A: IL CONTO CHE NON TORNA (duello lordo / netto)
A=BASE+EXTRA+'<rect width="1280" height="720" fill="url(#bgA)"/>'+rays(640,440)+'<circle cx="640" cy="450" r="470" fill="url(#glow)"/>'
A+=T('a1',640,128,'PENSIONI <tspan fill="#FFD43B">2027</tspan>',122,'#fff',20,maxw=1150)
A+=banner(150,150,980,92,-1.4,'#E0402A')
A+=f'<g transform="rotate(-1.4 640 196)">'+T('a2',640,222,'QUANTI EURO NETTI IN PIÙ?',62,'#fff',9,maxw=920)+'</g>'
# scheda sinistra: +29 € LORDI
A+='<g filter="url(#sh)"><rect x="40" y="292" width="530" height="318" rx="30" fill="url(#lcard)" stroke="#fff" stroke-width="8"/></g>'
A+='<rect x="44" y="296" width="522" height="130" rx="26" fill="url(#gloss)" opacity="0.35"/>'
A+='<g transform="rotate(-4 160 298)"><g filter="url(#sh)"><rect x="70" y="266" width="190" height="62" rx="12" fill="#FFD43B"/></g>'+T('a3',165,312,'LORDI',42,'#0D2A2F')+'</g>'
A+=T('a4',305,478,'+29 €',156,'#FFD43B',26,maxw=480)
A+=T('a5',305,540,'OGNI 1.000 € DI PENSIONE',31,'#fff',8,maxw=480)
A+='<g filter="url(#sh)"><rect x="205" y="560" width="200" height="40" rx="20" fill="#fff"/></g>'+T('a6',305,589,'STIMA 2,9%',24,'#0D5158',maxw=180)
A+=coin(540,300,30,14)
# scheda destra: ? € NETTI
A+='<g filter="url(#sh)"><rect x="710" y="292" width="530" height="318" rx="30" fill="url(#pp)" stroke="#E0402A" stroke-width="12"/></g>'
A+='<g transform="rotate(4 1105 298)"><g filter="url(#sh)"><rect x="1000" y="266" width="200" height="62" rx="12" fill="#E0402A" stroke="#fff" stroke-width="5"/></g>'+T('a7',1100,312,'NETTI',42,'#fff')+'</g>'
A+=T('a8',975,508,'? €',214,'#E0402A',18,maxw=400)
A+=T('a9',975,578,'IN TASCA A GENNAIO',33,'#0D5158',maxw=470)
# freccia centrale
A+='<g filter="url(#sh)"><path d="M582 408 H632 V372 L712 450 L632 528 V492 H582 Z" fill="url(#ye)" stroke="#fff" stroke-width="8" stroke-linejoin="round"/></g>'
# promessa in basso
A+='<g filter="url(#sh)"><rect x="95" y="638" width="1030" height="62" rx="31" fill="#06282C" fill-opacity="0.92" stroke="#FFD43B" stroke-width="6"/></g>'
A+=T('a10',610,682,'TABELLA DA 600 A 3.000 € <tspan fill="#fff">+ LE MINIME</tspan>',38,'#FFD43B',maxw=960)
A+='<rect width="1280" height="720" fill="url(#vig)"/>'+END
# ---------------------------------------------------------------- B: LA SCALA DA 600 A 3.000 € (5 schede con "? €")
B=BASE+EXTRA+'<rect width="1280" height="720" fill="url(#vig)" opacity="0"/>'+'<g opacity="0.10" fill="#fff"><path d="M980 330 L500 -200 L700 -200Z"/><path d="M980 330 L900 -200 L1100 -200Z"/><path d="M980 330 L1300 -200 L1500 0Z"/><path d="M980 330 L1500 300 L1500 520Z"/><path d="M980 330 L1300 900 L1100 900Z"/><path d="M980 330 L700 900 L500 900Z"/><path d="M980 330 L-100 500 L-100 300Z"/></g>'
B+='<circle cx="900" cy="330" r="420" fill="url(#glow)"/>'
B+=T('b1',44,138,'PENSIONI <tspan fill="#FFD43B">2027</tspan>',120,'#fff',20,anchor='start',maxw=800)
B+='<g transform="rotate(8 1120 98)"><g filter="url(#sh)"><rect x="1010" y="52" width="230" height="92" rx="16" fill="#fff" stroke="#E0402A" stroke-width="7"/></g>'+T('b2',1125,122,'STIME',58,'#E0402A',maxw=200)+'</g>'
B+=banner(44,170,900,88,-1.2,'#E0402A')
B+='<g transform="rotate(-1.2 494 214)">'+T('b3',494,238,'AUMENTO NETTO: <tspan fill="#FFD43B">QUANTO?</tspan>',56,'#fff',9,maxw=840)+'</g>'
# freccia che sale lungo la scala (dietro le schede)
x0,y0,x1,y1=50,431,1130,257
dx,dy=x1-x0,y1-y0;L=math.hypot(dx,dy);ux,uy=dx/L,dy/L;nx,ny=-uy,ux
tip=(x1+ux*95,y1+uy*95);b1=(x1+nx*62,y1+ny*62);b2=(x1-nx*62,y1-ny*62)
B+=(f'<g filter="url(#sh)"><line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="#fff" stroke-width="56" stroke-linecap="round"/>'
    f'<polygon points="{tip[0]:.0f},{tip[1]:.0f} {b1[0]:.0f},{b1[1]:.0f} {b2[0]:.0f},{b2[1]:.0f}" fill="#fff" stroke="#fff" stroke-width="14" stroke-linejoin="round"/>'
    f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="#FFD43B" stroke-width="40" stroke-linecap="round"/>'
    f'<polygon points="{tip[0]:.0f},{tip[1]:.0f} {b1[0]:.0f},{b1[1]:.0f} {b2[0]:.0f},{b2[1]:.0f}" fill="#FFD43B" stroke="#FFD43B" stroke-width="4" stroke-linejoin="round"/></g>')
def pcard(i,x,top,w,bottom,label,hot=False):
    h=bottom-top
    s=f'<g filter="url(#sh)"><rect x="{x}" y="{top}" width="{w}" height="{h}" rx="22" fill="url(#pp)" stroke="{"#FFD43B" if hot else "#fff"}" stroke-width="{10 if hot else 6}"/></g>'
    s+=T(f'p{i}',x+w/2,top+60,label,46,'#0D5158',maxw=w-30)
    s+=f'<g filter="url(#sh)"><rect x="{x+20}" y="{top+78}" width="{w-40}" height="76" rx="30" fill="url(#re)" stroke="#fff" stroke-width="5"/></g>'
    s+=T(f'q{i}',x+w/2,top+78+55,'? €',56,'#fff',7,maxw=w-80)
    s+=stack(x+w/2,bottom-30,40,i) if i else ''
    return s
bottom=641
for i,lab in enumerate(['600 €','1.000 €','1.500 €','2.000 €','3.000 €']):
    B+=pcard(i,38+i*244,456-i*38,228,bottom,lab,hot=(i==0))
# tab LE MINIME sotto la prima scheda
B+='<g filter="url(#sh)"><path d="M70 650 L100 626 L130 650 H300 a14 14 0 0 1 14 14 V684 a14 14 0 0 1 -14 14 H84 a14 14 0 0 1 -14 -14 Z" fill="#E0402A" stroke="#fff" stroke-width="5" stroke-linejoin="round"/></g>'
B+=T('b4',192,686,'LE MINIME!',32,'#fff',maxw=200)
B+='<rect width="1280" height="720" fill="url(#vig)"/>'+END
JS="""()=>{for(const t of document.querySelectorAll('text[data-w]')){const mw=parseFloat(t.getAttribute('data-w'));const fs=parseFloat(t.getAttribute('font-size'));const w=t.getBBox().width;if(w>mw)t.setAttribute('font-size',fs*mw/w);}
const o=[];for(const t of document.querySelectorAll('text')){const r=t.getBoundingClientRect();if(r.width<2)continue;o.push([t.id||'-',t.textContent.slice(0,24),Math.round(r.x),Math.round(r.y),Math.round(r.right),Math.round(r.bottom),+t.getAttribute('font-size')]);}return o;}"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1280,'height':720})
        for n,h in (('A',A),('B',B)):
            open(f'miniatura-{n}.html','w').write(h)
            await pg.goto(f'file://{os.getcwd()}/miniatura-{n}.html')
            boxes=await pg.evaluate(JS)
            for r in boxes:
                flag='' if r[2]>=8 and r[4]<=1272 and r[3]>=0 and r[5]<=716 else '  <<< FUORI'
                print(n,r,flag)
            ids=[r for r in boxes if r[0]!='-']
            for i in range(len(ids)):
                for j in range(i+1,len(ids)):
                    a,c=ids[i],ids[j]
                    ox=min(a[4],c[4])-max(a[2],c[2]);oy=min(a[5],c[5])-max(a[3],c[3])
                    if ox>2 and oy>2: print(n,'SOVRAPPOSTI',a[0],a[1],'<->',c[0],c[1],ox,oy)
            await pg.screenshot(path=f'miniatura-{n}.png')
        await b.close()
asyncio.run(main())
