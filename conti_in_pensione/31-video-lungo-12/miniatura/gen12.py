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

# ---------------------------------------------------------------- A: LA SCALINATA CHE SCENDE (2023 -> 2025 -> 2027, la perdita resta "? EURO")
A=BASE+EXTRA+'<rect width="1280" height="720" fill="url(#bgA)"/>'+rays(640,430)+'<circle cx="900" cy="450" r="430" fill="url(#glow)"/>'
A+=T('a1',44,140,'PENSIONI <tspan fill="#FFD43B">2027</tspan>',126,'#fff',20,anchor='start',maxw=820)
A+='<g transform="rotate(7 1100 96)"><g filter="url(#sh)"><rect x="985" y="50" width="250" height="92" rx="16" fill="#fff" stroke="#E0402A" stroke-width="7"/></g>'+T('a2',1110,120,'DECRETO',52,'#E0402A',maxw=220)+'</g>'
A+=banner(44,168,980,88,-1.2,'#E0402A')
A+='<g transform="rotate(-1.2 534 212)">'+T('a3',534,236,'NUOVI COEFFICIENTI: <tspan fill="#FFD43B">QUANTO PERDI?</tspan>',54,'#fff',9,maxw=930)+'</g>'
steps=[(60,340,'2023-24','url(#lcard)',5),(440,440,'2025-26','url(#lcard)',4),(820,540,'2027','url(#re)',3)]
for k,(x,top,lab,fill,n) in enumerate(steps):
    A+=f'<g filter="url(#sh)"><rect x="{x}" y="{top}" width="360" height="{641-top}" rx="20" fill="{fill}" stroke="#fff" stroke-width="8"/></g>'
    A+=f'<rect x="{x+4}" y="{top+4}" width="352" height="{min(70,641-top-8)}" rx="16" fill="url(#gloss)" opacity="0.35"/>'
    A+=T(f's{k}',x+180,top+(92 if k<2 else 78),lab,52,'#fff',8,maxw=320)
    A+=stack(x+180,top-22,44,n)
# scheda rossa: perdita nascosta, sopra l'ultimo gradino
A+='<g filter="url(#sh)"><rect x="800" y="296" width="400" height="190" rx="28" fill="url(#pp)" stroke="#E0402A" stroke-width="12"/></g>'
A+=T('a4',1000,410,'− ? €',128,'#E0402A',14,maxw=360)
A+=T('a5',1000,468,'OGNI ANNO, A 67 ANNI',27,'#0D5158',maxw=370)
A+=coin(1190,300,34,14)
# freccia che scende dai gradini
A+='<g filter="url(#sh)"><path d="M440 292 H600 V262 L690 316 L600 370 V340 H440 Z" fill="url(#ye)" stroke="#fff" stroke-width="7" stroke-linejoin="round" transform="rotate(14 560 316)"/></g>'
A+='<g filter="url(#sh)"><rect x="140" y="654" width="1000" height="56" rx="28" fill="#06282C" fill-opacity="0.92" stroke="#FFD43B" stroke-width="6"/></g>'
A+=T('a6',640,693,'C\'È UN <tspan fill="#fff">CONTO PER RECUPERARE</tspan>: ALLA FINE',34,'#FFD43B',maxw=950)
A+='<rect width="1280" height="720" fill="url(#vig)"/>'+END
# ---------------------------------------------------------------- B: LA TABELLA CON LA COLONNA COPERTA (2026 visibile, 2027 nascosto)
B=BASE+EXTRA+'<rect width="1280" height="720" fill="url(#bgA)"/>'+'<g opacity="0.10" fill="#fff"><path d="M1000 380 L520 -200 L720 -200Z"/><path d="M1000 380 L920 -200 L1120 -200Z"/><path d="M1000 380 L1330 -120 L1330 120Z"/></g>'
B+='<circle cx="930" cy="330" r="420" fill="url(#glow)"/>'
B+=T('b1',40,150,'PENSIONI',134,'#fff',20,anchor='start',maxw=520)
B+=T('b2',40,322,'2027',160,'#FFD43B',22,anchor='start',maxw=520)
B+=banner(30,352,520,96,-3,'#E0402A')
B+='<g transform="rotate(-3 290 400)">'+T('b3',290,426,'QUANTO PERDI?',58,'#fff',9,maxw=470)+'</g>'
B+='<g filter="url(#sh)"><rect x="40" y="480" width="470" height="128" rx="26" fill="#06282C" fill-opacity="0.92" stroke="#FFD43B" stroke-width="6"/></g>'
B+=T('b4',275,532,'LA TUA ETÀ',44,'#FFD43B',maxw=420)
B+=T('b5',275,584,'È IN TABELLA?',44,'#fff',maxw=420)
# tabella a destra
B+='<g filter="url(#sh)"><rect x="590" y="46" width="650" height="560" rx="30" fill="url(#pp)" stroke="#fff" stroke-width="8"/></g>'
B+='<rect x="590" y="46" width="650" height="92" rx="30" fill="#0D5158"/><rect x="590" y="100" width="650" height="38" fill="#0D5158"/>'
B+=T('t0',668,106,'ETÀ',40,'#fff',maxw=130)
B+=T('t1',890,106,'OGGI',40,'#fff',maxw=190)
B+=T('t2',1112,106,'2027',40,'#FFD43B',maxw=190)
rows=[('62','4,795'),('65','5,250'),('67','5,608'),('70','6,258')]
for i,(e,v) in enumerate(rows):
    y=150+i*108
    hot=(e=='67')
    if hot:B+=f'<rect x="604" y="{y}" width="622" height="98" rx="18" fill="#FFF3B0" stroke="#FFD43B" stroke-width="6"/>'
    else:B+=f'<rect x="604" y="{y}" width="622" height="98" rx="18" fill="#E3EEF0"/>'
    B+=T(f'e{i}',668,y+68,e,58,'#0D5158',maxw=110)
    B+=T(f'v{i}',890,y+68,v+' %',58,'#0D5158',maxw=200)
    B+=f'<g filter="url(#sh)"><rect x="1010" y="{y+8}" width="206" height="82" rx="20" fill="#0A0A0A" stroke="#E0402A" stroke-width="5"/></g>'
    B+=T(f'q{i}',1113,y+68,'? , ? ? ?',54,'#fff',maxw=180)
B+='<g transform="rotate(-6 960 650)"><g filter="url(#sh)"><rect x="700" y="618" width="520" height="78" rx="14" fill="#fff" stroke="#E0402A" stroke-width="8"/></g>'+T('b6',960,674,'DECRETO 16 OTTOBRE',46,'#E0402A',maxw=470)+'</g>'
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
