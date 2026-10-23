# Miniature video 10 (pensione alle casalinghe). Stile del canale: sfondo verde acqua a raggi, scritte giganti con contorno scuro,
# palline rosso/verde, striscia bianca con bordo giallo. Layout NUOVI rispetto ai video 8-9: A = casa con lei dentro + importo;
# B = coppia con la cifra del marito chiusa a lucchetto. La risposta (la cifra) resta nascosta: la dice il video.
import asyncio,os,re,sys
from playwright.async_api import async_playwright
sys.path.insert(0,'../../25-video-lungo-9/miniatura')
src=open('../../14-video-lungo-4-invalidita-2027/miniatura/vecchie-45cent/gen.py').read()
HEAD=re.search(r"HEAD='''(.*?)'''",src,re.S).group(1)
g9=open('../../25-video-lungo-9/miniatura/gen9.py').read()
exec(g9[g9.index("S='stroke"):g9.index("# A: LA BUSTA")])
def house(cx,gy,w,h,rh):
    return (f'<g filter="url(#sh)"><rect x="{cx+w*0.2}" y="{gy-h-rh*0.85}" width="{w*0.1}" height="{rh*0.75}" rx="4" fill="#C9503C" stroke="#fff" stroke-width="5"/>'
     f'<rect x="{cx-w/2}" y="{gy-h}" width="{w}" height="{h}" rx="14" fill="url(#pp)" stroke="#fff" stroke-width="6"/>'
     f'<path d="M{cx-w/2-30} {gy-h+8} L{cx} {gy-h-rh} L{cx+w/2+30} {gy-h+8} Z" fill="url(#re)" stroke="#fff" stroke-width="7" stroke-linejoin="round"/></g>')
def lock(cx,cy,s):
    return (f'<g transform="translate({cx} {cy}) scale({s})" filter="url(#sh)"><path d="M-30 -8 V-30 Q-30 -60 0 -60 Q30 -60 30 -30 V-8" fill="none" stroke="#FFD43B" stroke-width="13"/>'
     f'<rect x="-46" y="-12" width="92" height="70" rx="12" fill="#FFD43B" stroke="#fff" stroke-width="5"/><circle cx="0" cy="16" r="10" fill="#5A3300"/><rect x="-4" y="18" width="8" height="22" rx="4" fill="#5A3300"/></g>')
# A: CASA con LEI dentro, "MAI LAVORATO?", fino a 546 € al mese, pallina rossa "IL MARITO?"
A=HEAD+f"""<circle cx="980" cy="360" r="300" fill="#FFD43B" opacity="0.14" filter="url(#gl)"/>
<g class="t" {S} stroke-width="20"><text id="a1" x="30" y="122" font-size="120" fill="#fff">PENSIONE</text></g>
{blocco(36,150,560,90,"CASALINGHE",72,"#FFD43B","#0D2A2F",-2,'a2')}
<g class="t" {S} stroke-width="16"><text id="a3" x="38" y="338" font-size="78" fill="#fff">MAI LAVORATO?</text><text id="a4" x="38" y="424" font-size="62" fill="#3BE39A">TI SPETTA FINO A</text></g>
<g class="t" {S} stroke-width="22"><text id="a5" x="30" y="590" font-size="170" fill="#3BE39A">546 €</text></g>
<text id="a6" x="560" y="590" class="t" font-size="46" fill="#fff" {S} stroke-width="9">AL MESE</text>
{house(1000,600,380,300,150)}
{person(1000,440,105,'L','#1B9F81')}
<g filter="url(#sh)"><circle cx="1160" cy="205" r="88" fill="url(#re)" stroke="#fff" stroke-width="8"/></g>
<text x="1160" y="196" class="t" font-size="30" fill="#fff" text-anchor="middle" {S} stroke-width="5">E IL</text><text x="1160" y="232" class="t" font-size="28" fill="#fff" text-anchor="middle" {S} stroke-width="5">MARITO?</text>
"""+STRIP('MA C\'È UNA CIFRA CHE <tspan fill="#0D5158">DECIDE TUTTO</tspan>')+END
# B: COPPIA: la pensione di LUI chiusa a lucchetto ("? €"), LEI con "0 €?" ; numero gigante nascosto
B=HEAD+f"""<circle cx="640" cy="330" r="330" fill="#25D08C" opacity="0.13" filter="url(#gl)"/>
<g class="t" text-anchor="middle" {S} stroke-width="18"><text id="b1" x="640" y="108" font-size="92" fill="#fff">PENSIONE <tspan fill="#FFD43B">CASALINGHE</tspan></text></g>
{blocco(200,132,880,72,"SE TUO MARITO PRENDE PIÙ DI...",44,"#E0402A","#fff",-1,'b2')}
<g filter="url(#sh)"><rect x="440" y="230" width="420" height="250" rx="26" fill="url(#pp)" stroke="#FFD43B" stroke-width="10"/></g>
{lock(530,350,1.15)}
<g class="t" text-anchor="middle" {S} stroke-width="14"><text id="b3" x="720" y="390" font-size="140" fill="#0D2A2F" stroke="#fff">? €</text></g>
<text id="b4" x="650" y="462" class="t" font-size="30" fill="#0D5158" text-anchor="middle">AL MESE, NETTI</text>
{person(215,370,105,'F','#2B6F8F')}
{blocco(115,500,200,56,"LUI",38,"#0D5158","#fff",0,'b5')}
{person(1065,370,105,'L','#1B9F81')}
{blocco(965,500,200,56,"LEI",38,"#0D5158","#fff",0,'b6')}
<g filter="url(#sh)"><circle cx="1190" cy="250" r="66" fill="url(#re)" stroke="#fff" stroke-width="8"/></g><text x="1190" y="270" class="t" font-size="54" fill="#fff" text-anchor="middle" {S} stroke-width="7">0 €?</text>
{blocco(440,500,400,64,"IL CONTO VERO",40,"#FFD43B","#0D2A2F",0,'b7')}
"""+STRIP('A LEI <tspan fill="#0D5158">NON ARRIVA NIENTE?</tspan>')+END
# C (rifatta 23/10): impaginazione DIVERSA da A e B: bilancia gigante in alto, scritta PENSIONE CASALINGHE in BASSO, niente striscia bianca.
def slots(x,y,n,w,h):
    o=''
    for i in range(n):o+=f'<g filter="url(#sh)"><rect x="{x+i*(w+10)}" y="{y}" width="{w}" height="{h}" rx="10" fill="url(#re)" stroke="#fff" stroke-width="5"/></g><text x="{x+i*(w+10)+w/2}" y="{y+h*0.78}" class="t" font-size="{h*0.78}" fill="#fff" text-anchor="middle" {S} stroke-width="6">?</text>'
    return o
C=HEAD+f"""<rect x="0" y="0" width="640" height="720" fill="#7A1A10" opacity="0.28"/>
<circle cx="640" cy="80" r="40" fill="#FFD43B" stroke="#fff" stroke-width="7"/>
<rect x="628" y="80" width="24" height="330" rx="8" fill="#FFD43B" stroke="#fff" stroke-width="5"/>
<path d="M560 420 H720 L690 380 H590 Z" fill="#FFD43B" stroke="#fff" stroke-width="5"/>
<g transform="rotate(-12 640 110)"><rect x="200" y="100" width="880" height="22" rx="11" fill="#FFD43B" stroke="#fff" stroke-width="5"/>
<path d="M250 122 L130 300 M250 122 L370 300 M1030 122 L950 300 M1030 122 L1110 300" stroke="#fff" stroke-width="5"/></g>
<g filter="url(#sh)"><path d="M90 420 Q270 500 450 420 Z" fill="#FFD43B" stroke="#fff" stroke-width="6"/><path d="M900 210 Q1020 284 1140 210 Z" fill="#FFD43B" stroke="#fff" stroke-width="6"/></g>
<g filter="url(#sh)"><rect x="80" y="222" width="380" height="196" rx="22" fill="url(#pp)" stroke="#fff" stroke-width="6"/></g>
<text x="270" y="270" class="t" font-size="36" fill="#0D5158" text-anchor="middle">LUI: MILLE E...</text>
<text id="c3" x="100" y="390" class="t" font-size="94" fill="#0D2A2F">1.0</text>{slots(280,300,2,58,96)}<text x="452" y="390" class="t" font-size="60" fill="#0D2A2F" text-anchor="end">€</text>
{person(1020,140,62,'L','#1B9F81')}
<g filter="url(#sh)"><circle cx="1150" cy="70" r="56" fill="url(#re)" stroke="#fff" stroke-width="7"/></g><text x="1150" y="88" class="t" font-size="44" fill="#fff" text-anchor="middle" {S} stroke-width="6">0 €</text>
{blocco(830,250,380,70,"E A LEI ZERO?",44,"#E0402A","#fff",-3,'c4')}
<g class="t" text-anchor="middle" {S} stroke-width="22"><text id="c1" x="640" y="556" font-size="122" fill="#fff">PENSIONE</text><text id="c2" x="640" y="676" font-size="112" fill="#FFD43B">CASALINGHE</text></g>
"""+END
JS="""()=>{const o=[];for(const t of document.querySelectorAll('text')){const r=t.getBoundingClientRect();if(r.width<2)continue;o.push([t.textContent.slice(0,22),Math.round(r.x),Math.round(r.y),Math.round(r.right),Math.round(r.bottom)]);}return o;}"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg=await b.new_page(viewport={'width':1280,'height':720})
        for n,h in (('A',A),('B',B),('C',C)):
            open(f'miniatura-{n}.html','w').write(h)
            await pg.goto(f'file://{os.getcwd()}/miniatura-{n}.html')
            for r in await pg.evaluate(JS):
                flag='' if r[1]>=8 and r[3]<=1272 and r[2]>=0 and r[4]<=716 else '  <<< FUORI'
                print(n,r,flag)
            await pg.screenshot(path=f'miniatura-{n}.png')
        await b.close()
asyncio.run(main())
