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
# A: PENSIONI / TREDICESIMA / DETASSATA? + cedolino + spunta + freccia
A=HEAD+f'''<circle cx="360" cy="380" r="300" fill="#FFD43B" opacity="0.18" filter="url(#gl)"/>
<g class="t" {S} stroke-width="20"><text x="30" y="150" font-size="150" fill="#fff">PENSIONI</text></g>
{blocco(30,180,780,110,"TREDICESIMA",88)}
<g class="t" {S} stroke-width="20"><text x="30" y="430" font-size="114" fill="#FF5A43">DETASSATA?</text></g>
{blocco(36,468,560,92,"SOLO UNA PROPOSTA",44,"#E0402A","#fff",-4)}
{doc(1050,300,5,0.95)}
<g transform="translate(880 520) scale(0.9)">{CHECK}</g>
'''+STRIP('ECCO IL TUO <tspan fill="#0D5158">IMPORTO NETTO</tspan>')+END
# B: PENSIONI + tabella importi
rows=[("1.000€","770€",0),("1.500€","1.155€",0),("2.000€","1.540€",0),("3.000€","2.010€",1)]
tb='''<g filter="url(#sh)"><rect x="790" y="30" width="460" height="580" rx="30" fill="url(#pp)" stroke="#fff" stroke-width="6"/><rect x="790" y="30" width="460" height="86" rx="30" fill="#1B9F81"/><rect x="790" y="80" width="460" height="36" fill="#1B9F81"/></g>
<text x="830" y="90" class="t" font-size="34" fill="#fff">LORDA</text><text x="1210" y="90" class="t" font-size="34" fill="#fff" text-anchor="end">NETTA</text><text x="1020" y="92" class="t" font-size="44" fill="#FFD43B" text-anchor="middle">➜</text>'''
for i,(a,b,h) in enumerate(rows):
    y=200+i*122
    if h: tb+=f'<rect x="802" y="{y-62}" width="436" height="100" rx="18" fill="#FDE3DE"/>'
    tb+=f'<text x="830" y="{y}" class="t" font-size="42" fill="#0B4A50">{a}</text><text x="1210" y="{y}" class="t" font-size="{46 if h else 42}" fill="{"#C0200F" if h else "#1B9F81"}" text-anchor="end">{b}</text>'
    if i<3: tb+=f'<line x1="810" y1="{y+22}" x2="1230" y2="{y+22}" stroke="#C5D4D7" stroke-width="4"/>'
B=HEAD+f'''<circle cx="400" cy="330" r="300" fill="#FFD43B" opacity="0.16" filter="url(#gl)"/>
<g class="t" {S} stroke-width="20"><text x="30" y="150" font-size="140" fill="#FFD43B">PENSIONI</text></g>
<g class="t" {S} stroke-width="16"><text x="30" y="250" font-size="84" fill="#fff">TREDICESIMA</text></g>
<g class="t" {S} stroke-width="14"><text x="30" y="345" font-size="64" fill="#FF5A43">QUANTO AUMENTA?</text></g>
{blocco(30,385,700,100,"TABELLA IMPORTI",66)}
{blocco(30,515,520,80,"⚠ ATTENZIONE",50,"#E0402A","#fff",-3)}
{tb}
'''+STRIP('TUTTI GLI IMPORTI <tspan fill="#0D5158">NETTI DI DICEMBRE</tspan>')+END
# C: -990 gigante
C=HEAD+f'''<circle cx="640" cy="360" r="330" fill="#FF5A43" opacity="0.18" filter="url(#gl)"/>
<g filter="url(#sh)"><circle cx="135" cy="150" r="108" fill="url(#re)" stroke="#fff" stroke-width="8"/><circle cx="1145" cy="150" r="108" fill="url(#gr)" stroke="#fff" stroke-width="8"/></g>
<g class="t" text-anchor="middle" {S} stroke-width="10"><text x="135" y="168" font-size="46" fill="#fff">3.000€</text><text x="1145" y="168" font-size="46" fill="#fff">2.010€</text></g>
<g class="t" text-anchor="middle" font-size="34" fill="#fff" {S} stroke-width="8"><text x="135" y="285">LORDA</text><text x="1145" y="285">NETTA</text></g>
<g class="t" text-anchor="middle" {S} stroke-width="18"><text x="640" y="135" font-size="132" fill="#fff">PENSIONI</text></g>
<g class="t" text-anchor="middle" {S} stroke-width="14"><text x="640" y="225" font-size="80" fill="#FFD43B">TREDICESIMA</text></g>
<g class="t" text-anchor="middle" {S} stroke-width="26"><text x="640" y="470" font-size="240" fill="#FF5A43" letter-spacing="-8">-990€</text></g>
<g class="t" text-anchor="middle" {S} stroke-width="12"><text x="640" y="580" font-size="62" fill="#FFD43B">QUASI MILLE EURO IN MENO</text></g>
'''+STRIP('PENSIONE DA 3.000€: <tspan fill="#0D5158">IL CONTO VERO</tspan>')+END
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg=await b.new_page(viewport={'width':1280,'height':720})
        for n,h in (('A',A),('B',B),('C',C)):
            open(f'miniatura-{n}.html','w').write(h)
            await pg.goto(f'file://{os.getcwd()}/miniatura-{n}.html'); await pg.screenshot(path=f'miniatura-{n}.png')
        await b.close()
asyncio.run(main())
