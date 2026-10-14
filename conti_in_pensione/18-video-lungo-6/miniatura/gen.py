import asyncio,os,re
from playwright.async_api import async_playwright
src=open('../../14-video-lungo-4-invalidita-2027/miniatura/vecchie-45cent/gen.py').read()
HEAD=re.search(r"HEAD='''(.*?)'''",src,re.S).group(1)
S='stroke="#06282C" stroke-linejoin="round" paint-order="stroke"'
END='</svg></body></html>'
STRIP=lambda txt:f'<g filter="url(#sh)"><rect x="30" y="630" width="1220" height="68" rx="20" fill="#fff"/><rect x="30" y="630" width="1220" height="68" rx="20" fill="none" stroke="#FFD43B" stroke-width="7"/></g><text x="640" y="681" class="t" font-size="44" fill="#C0200F" text-anchor="middle">{txt}</text>'
def blocco(x,y,w,h,txt,fs,fill="#FFD43B",col="#0D2A2F",rot=0):
    cx=x+w/2;cy=y+h/2
    return f'<g transform="rotate({rot} {cx} {cy})"><g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}"/></g><text x="{cx}" y="{y+h*0.72}" class="t" font-size="{fs}" fill="{col}" text-anchor="middle">{txt}</text></g>'
CHECK='<g filter="url(#sh)"><circle cx="0" cy="0" r="62" fill="url(#gr)" stroke="#fff" stroke-width="7"/></g><path d="M-30 2 L-8 26 L34 -24" fill="none" stroke="#fff" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>'
ARROW='<path d="M0 0 L-120 60" stroke="#E0402A" stroke-width="22" stroke-linecap="round"/><path d="M-150 75 L-100 20 L-80 80Z" fill="#E0402A" stroke="#fff" stroke-width="5" stroke-linejoin="round"/>'
def doc(x,y,r,sc):
    return f'''<g transform="translate({x} {y}) rotate({r}) scale({sc})" filter="url(#sh)"><rect x="-190" y="-215" width="380" height="430" rx="26" fill="url(#pp)" stroke="#fff" stroke-width="6"/>
<rect x="-190" y="-215" width="380" height="76" rx="26" fill="#1B9F81"/><rect x="-190" y="-185" width="380" height="46" fill="#1B9F81"/>
<text x="0" y="-160" class="t" font-size="36" fill="#fff" text-anchor="middle">CEDOLINO</text>
<text x="-150" y="-85" class="t" font-size="28" fill="#5B7A7E">LORDA</text><text x="150" y="-85" class="t" font-size="40" fill="#0B4A50" text-anchor="end">3.000€</text>
<rect x="-150" y="-55" width="300" height="8" rx="4" fill="#BFD0D3"/>
<text x="-150" y="-5" class="t" font-size="30" fill="#C0200F">IRPEF</text><text x="150" y="-5" class="t" font-size="40" fill="#C0200F" text-anchor="end">-990€</text>
<rect x="-150" y="40" width="300" height="130" rx="24" fill="#E3F6F1" stroke="#1B9F81" stroke-width="6"/>
<text x="0" y="88" class="t" font-size="30" fill="#1B9F81" text-anchor="middle">NETTO</text>
<text x="0" y="146" class="t" font-size="64" fill="#0B4A50" text-anchor="middle">2.010€</text></g>'''

# ===== VIDEO 6: PENSIONI NOVEMBRE (3 layout diversi dalle miniature del video 5) =====
def card(x,y,r,sc,amt_old,amt_new,tag):
    return f"""<g transform="translate({x} {y}) rotate({r}) scale({sc})" filter="url(#sh)"><rect x="-230" y="-215" width="460" height="430" rx="26" fill="url(#pp)" stroke="#fff" stroke-width="6"/>
<rect x="-230" y="-215" width="460" height="76" rx="26" fill="#1B9F81"/><rect x="-230" y="-185" width="460" height="46" fill="#1B9F81"/>
<text x="0" y="-162" class="t" font-size="32" fill="#fff" text-anchor="middle">CEDOLINO NOVEMBRE</text>
<text x="-190" y="-75" class="t" font-size="28" fill="#5B7A7E">OTTOBRE</text><text x="190" y="-75" class="t" font-size="40" fill="#0B4A50" text-anchor="end">{amt_old}</text>
<rect x="-190" y="-48" width="380" height="8" rx="4" fill="#BFD0D3"/>
<text x="-190" y="10" class="t" font-size="28" fill="#C0200F">ACCONTO</text><text x="190" y="10" class="t" font-size="40" fill="#C0200F" text-anchor="end">{tag}</text>
<rect x="-190" y="45" width="380" height="130" rx="24" fill="#FDE3DE" stroke="#E0402A" stroke-width="6"/>
<text x="0" y="92" class="t" font-size="30" fill="#C0200F" text-anchor="middle">NOVEMBRE</text>
<text x="0" y="150" class="t" font-size="64" fill="#C0200F" text-anchor="middle">{amt_new}</text></g>"""
def calendario(x,y,r,sc,mese,num,sub):
    return f"""<g transform="translate({x} {y}) rotate({r}) scale({sc})" filter="url(#sh)"><rect x="-190" y="-215" width="380" height="430" rx="30" fill="url(#pp)" stroke="#fff" stroke-width="6"/>
<rect x="-190" y="-215" width="380" height="110" rx="30" fill="#1B9F81"/><rect x="-190" y="-165" width="380" height="60" fill="#1B9F81"/>
<text x="0" y="-135" class="t" font-size="54" fill="#fff" text-anchor="middle">{mese}</text>
<text x="0" y="75" class="t" font-size="250" fill="#0B4A50" text-anchor="middle">{num}</text>
<text x="0" y="170" class="t" font-size="52" fill="#1B9F81" text-anchor="middle">{sub}</text></g>
<g filter="url(#sh)"><rect x="{x-110*sc}" y="{y-262*sc}" width="34" height="80" rx="17" fill="#C9D6D8" stroke="#fff" stroke-width="4" transform="rotate({r} {x} {y})"/><rect x="{x+76*sc}" y="{y-262*sc}" width="34" height="80" rx="17" fill="#C9D6D8" stroke="#fff" stroke-width="4" transform="rotate({r} {x} {y})"/></g>"""
FRECCIA_GIU='<g filter="url(#sh)"><path d="M-46 -90 H46 V0 H96 L0 100 L-96 0 H-46Z" fill="#E0402A" stroke="#fff" stroke-width="8" stroke-linejoin="round"/></g>'
FRECCIA_DX='<g filter="url(#sh)"><path d="M-80 -42 H0 V-90 L96 0 L0 90 V42 H-80Z" fill="#FFD43B" stroke="#fff" stroke-width="8" stroke-linejoin="round"/></g>'
# A: PENSIONI NOVEMBRE + cedolino con importo che scende + freccia rossa
A=HEAD+f"""<circle cx="360" cy="360" r="300" fill="#FFD43B" opacity="0.18" filter="url(#gl)"/>
<g class="t" {S} stroke-width="20"><text x="30" y="150" font-size="150" fill="#FFD43B">PENSIONI</text></g>
{blocco(30,175,720,125,"NOVEMBRE",104,"#fff","#E0402A")}
<g class="t" {S} stroke-width="16"><text x="30" y="395" font-size="92" fill="#FF5A43">PIÙ BASSA?</text></g>
{blocco(36,430,620,92,"IL CONTO VERO",58,"#FFD43B","#0D2A2F",-3)}
{card(1040,358,4,0.9,"1.400€","920€","-480€")}
<g transform="translate(745 500) scale(0.8)">{FRECCIA_GIU}</g>
{blocco(930,562,300,58,"ESEMPIO",38,"#E0402A","#fff",-4)}
"""+STRIP('ECCO <tspan fill="#0D5158">PERCHÉ ARRIVA MENO</tspan>')+END
# B: ULTIMA RATA -> POI PIÙ SOLDI (due palline rosso/verde) + calendario
B=HEAD+f"""<circle cx="640" cy="330" r="320" fill="#FFD43B" opacity="0.14" filter="url(#gl)"/>
<g class="t" text-anchor="middle" {S} stroke-width="20"><text x="640" y="140" font-size="140" fill="#fff">PENSIONI</text></g>
<g class="t" text-anchor="middle" {S} stroke-width="16"><text x="640" y="235" font-size="92" fill="#FFD43B">NOVEMBRE</text></g>
<g filter="url(#sh)"><circle cx="290" cy="405" r="135" fill="url(#re)" stroke="#fff" stroke-width="9"/><circle cx="990" cy="405" r="135" fill="url(#gr)" stroke="#fff" stroke-width="9"/></g>
<g class="t" text-anchor="middle" {S} stroke-width="12"><text x="290" y="385" font-size="48" fill="#fff">ULTIMA</text><text x="290" y="445" font-size="58" fill="#fff">RATA</text><text x="990" y="385" font-size="48" fill="#fff">DA</text><text x="990" y="445" font-size="54" fill="#fff">DICEMBRE</text></g>
<g transform="translate(640 405)">{FRECCIA_DX}</g>
<g class="t" text-anchor="middle" font-size="40" fill="#fff" {S} stroke-width="9"><text x="290" y="578">TRATTENUTE</text><text x="990" y="578">PIÙ SOLDI</text></g>
"""+STRIP('LE ADDIZIONALI <tspan fill="#0D5158">FINISCONO</tspan>')+END
# C: calendario 2 NOVEMBRE + PERCHE' ARRIVA MENO? + TUTTA LA VERITA'
C=HEAD+f"""<circle cx="900" cy="330" r="320" fill="#FF5A43" opacity="0.16" filter="url(#gl)"/>
<g class="t" {S} stroke-width="20"><text x="30" y="150" font-size="150" fill="#fff">PENSIONI</text></g>
<g class="t" {S} stroke-width="16"><text x="30" y="250" font-size="96" fill="#FFD43B">NOVEMBRE</text></g>
<g class="t" {S} stroke-width="16"><text x="30" y="360" font-size="104" fill="#FF5A43">PERCHÉ</text></g>
<g class="t" {S} stroke-width="16"><text x="30" y="470" font-size="104" fill="#FF5A43">MENO?</text></g>
{blocco(30,510,560,86,"TUTTA LA VERITÀ",56,"#FFD43B","#0D2A2F",-3)}
{calendario(960,350,4,0.85,"NOVEMBRE","2","LUNEDÌ")}
<g filter="url(#sh)"><circle cx="1140" cy="535" r="88" fill="url(#re)" stroke="#fff" stroke-width="8"/></g>
<g class="t" text-anchor="middle" {S} stroke-width="10"><text x="1140" y="562" font-size="80" fill="#fff">?€</text></g>
"""+STRIP('LA DATA VERA: <tspan fill="#0D5158">LUNEDÌ 2 NOVEMBRE</tspan>')+END
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg=await b.new_page(viewport={'width':1280,'height':720})
        for n,h in (('A',A),('B',B),('C',C)):
            open(f'miniatura-{n}.html','w').write(h)
            await pg.goto(f'file://{os.getcwd()}/miniatura-{n}.html'); await pg.screenshot(path=f'miniatura-{n}.png')
        await b.close()
asyncio.run(main())
