# Miniature video 12 (coefficienti di trasformazione 2027, quanto perdi). Stile del canale (sfondo verde acqua a raggi, scritte con contorno scuro,
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


# ---------------------------------------------------------------- C: L'ASSEGNO STRAPPATO (un pezzo cade via: "- ? EURO")
C=BASE+EXTRA+'<rect width="1280" height="720" fill="url(#bgA)"/>'+rays(560,330,24,0.10)+'<circle cx="560" cy="330" r="420" fill="url(#glow)"/>'
C+=banner(300,26,680,88,1.2,'#0D5158')
C+='<g transform="rotate(1.2 640 70)">'+T('c1',640,92,'DAL <tspan fill="#FFD43B">1° GENNAIO 2027</tspan>',54,'#fff',8,maxw=640)+'</g>'
Z=[(620,0),(598,40),(634,80),(602,120),(636,160),(604,200),(632,240),(610,270)]
zp=' '.join(f'L{x} {y}' for x,y in Z)
zr=' '.join(f'L{x} {y}' for x,y in reversed(Z))
C+='<g transform="translate(110 150) rotate(-4 300 135)">'
C+=f'<g filter="url(#sh)"><path d="M0 0 {zp} L0 270 Z" fill="url(#pp)" stroke="#fff" stroke-width="6" stroke-linejoin="round"/></g>'
C+='<rect x="0" y="0" width="560" height="44" fill="#0D5158"/>'
C+=T('c2',24,32,'ASSEGNO DI PENSIONE',28,'#FFD43B',anchor='start',maxw=420)
C+=T('c3',34,148,'PENSIONI',108,'#0D5158',anchor='start',maxw=530)
C+=T('c4',34,252,'2027',96,'#E0402A',anchor='start',maxw=300)
C+='</g>'
C+='<g transform="translate(110 150) rotate(-4 300 135)"><g transform="translate(70 118) rotate(15 400 135)">'
C+=f'<g filter="url(#sh)"><path d="M{Z[0][0]} {Z[0][1]} L860 0 L860 270 L{Z[-1][0]} {Z[-1][1]} {zr} Z" fill="#fff" stroke="#E0402A" stroke-width="8" stroke-linejoin="round"/></g>'
C+=T('c5',768,172,'− ? €',104,'#E0402A',10,maxw=230)
C+='</g></g>'
C+=coin(95,500,30,-12)+coin(1210,200,26,10)
C+='<g filter="url(#sh)"><rect x="40" y="520" width="470" height="60" rx="30" fill="#06282C" fill-opacity="0.92" stroke="#FFD43B" stroke-width="5"/></g>'
C+=T('c6',275,562,'NUOVI COEFFICIENTI',36,'#FFD43B',maxw=430)
C+=banner(36,606,1208,100,-1,'#E0402A')
C+='<g transform="rotate(-1 640 656)">'+T('c7',640,684,'QUANTO TI <tspan fill="#FFD43B">TOGLIE</tspan> IL DECRETO?',70,'#fff',10,maxw=1130)+'</g>'
C+='<rect width="1280" height="720" fill="url(#vig)"/>'+END
# ---------------------------------------------------------------- D: IL TIMER (quanti mesi per recuperare: "? MESI")
D=BASE+EXTRA+'<rect width="1280" height="720" fill="url(#bgA)"/>'+rays(640,390,16,0.12)+'<circle cx="640" cy="390" r="460" fill="url(#glow)"/>'
D+=T('d1',640,138,'PENSIONI <tspan fill="#FFD43B">2027</tspan>',122,'#fff',20,maxw=1100)
cx,cy=640,392
D+=f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="232" fill="url(#go)" stroke="#fff" stroke-width="8"/></g>'
D+=f'<circle cx="{cx}" cy="{cy}" r="198" fill="url(#pp)" stroke="#B87800" stroke-width="8"/>'
for k in range(60):
    a=k*math.pi/30;big=(k%5==0);r1=198-(24 if big else 12);r2=190
    D+=f'<line x1="{cx+r1*math.sin(a):.1f}" y1="{cy-r1*math.cos(a):.1f}" x2="{cx+r2*math.sin(a):.1f}" y2="{cy-r2*math.cos(a):.1f}" stroke="#0D5158" stroke-width="{6 if big else 3}" stroke-linecap="round"/>'
a0=-math.pi/2;a1=a0+math.radians(62)
D+=f'<path d="M{cx+150*math.cos(a0):.1f} {cy+150*math.sin(a0):.1f} A150 150 0 0 1 {cx+150*math.cos(a1):.1f} {cy+150*math.sin(a1):.1f}" fill="none" stroke="#E0402A" stroke-width="18" stroke-linecap="round"/>'
D+=T('d2',cx,cy+22,'? MESI',100,'#E0402A',10,maxw=290)
D+=T('d3',cx,cy+90,'PER RECUPERARE',32,'#0D5158',maxw=290)
D+=f'<g filter="url(#sh)"><rect x="{cx-18}" y="{cy-262}" width="36" height="38" rx="8" fill="url(#go)" stroke="#fff" stroke-width="4"/></g>'
# sinistra: timbro decreto + data
D+='<g transform="rotate(-8 170 300)"><g filter="url(#sh)"><rect x="40" y="248" width="260" height="100" rx="14" fill="#fff" stroke="#E0402A" stroke-width="8"/></g>'+T('d4',170,312,'DECRETO',54,'#E0402A',maxw=230)+'</g>'
D+='<g filter="url(#sh)"><rect x="46" y="380" width="250" height="70" rx="35" fill="#06282C" fill-opacity="0.92" stroke="#FFD43B" stroke-width="5"/></g>'
D+=T('d5',171,428,'16 OTTOBRE',38,'#FFD43B',maxw=220)
# destra: perdita nascosta con monete
D+='<g filter="url(#sh)"><rect x="930" y="236" width="300" height="190" rx="26" fill="url(#pp)" stroke="#E0402A" stroke-width="10"/></g>'
D+=T('d6',1080,350,'− ? €',104,'#E0402A',10,maxw=270)
D+=T('d7',1080,404,'OGNI ANNO',30,'#0D5158',maxw=260)
D+=stack(1000,540,46,3)+stack(1120,560,46,2)+coin(1196,468,30,12)
D+=f'<g filter="url(#sh)"><path d="M1076 430 V470 H1050 L1080 510 L1110 470 H1084 V430 Z" fill="url(#re)" stroke="#fff" stroke-width="5" stroke-linejoin="round" opacity="0"/></g>'
D+='<g filter="url(#sh)"><rect x="110" y="640" width="1060" height="64" rx="32" fill="#06282C" fill-opacity="0.92" stroke="#FFD43B" stroke-width="6"/></g>'
D+=T('d8',640,686,'QUANTO TEMPO PER <tspan fill="#fff">RECUPERARE</tspan>?',40,'#FFD43B',maxw=1000)
D+='<rect width="1280" height="720" fill="url(#vig)"/>'+END
JS="""()=>{for(const t of document.querySelectorAll('text[data-w]')){const mw=parseFloat(t.getAttribute('data-w'));const fs=parseFloat(t.getAttribute('font-size'));const w=t.getBBox().width;if(w>mw)t.setAttribute('font-size',fs*mw/w);}
const o=[];for(const t of document.querySelectorAll('text')){const r=t.getBoundingClientRect();if(r.width<2)continue;o.push([t.id||'-',t.textContent.slice(0,24),Math.round(r.x),Math.round(r.y),Math.round(r.right),Math.round(r.bottom),+t.getAttribute('font-size')]);}return o;}"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1280,'height':720})
        for n,h in (('C',C),('D',D)):
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
