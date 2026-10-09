import asyncio,os,re
from playwright.async_api import async_playwright
src=open('vecchie-45cent/gen.py').read()
HEAD=re.search(r"HEAD='''(.*?)'''",src,re.S).group(1)
S='stroke="#06282C" stroke-linejoin="round" paint-order="stroke"'
END='</svg></body></html>'
STRIP=lambda txt:f'<g filter="url(#sh)"><rect x="30" y="630" width="1220" height="68" rx="20" fill="#fff"/><rect x="30" y="630" width="1220" height="68" rx="20" fill="none" stroke="#FFD43B" stroke-width="7"/></g><text x="640" y="681" class="t" font-size="44" fill="#C0200F" text-anchor="middle">{txt}</text>'
CARD='''<g transform="translate({x} {y}) rotate({r})" filter="url(#sh)"><rect x="-190" y="-215" width="380" height="430" rx="26" fill="url(#pp)" stroke="#fff" stroke-width="6"/>
<rect x="-190" y="-215" width="380" height="76" rx="26" fill="#1B9F81"/><rect x="-190" y="-185" width="380" height="46" fill="#1B9F81"/>
<text x="0" y="-160" class="t" font-size="38" fill="#fff" text-anchor="middle">INVALIDITÀ</text>
<rect x="-150" y="-110" width="250" height="18" rx="9" fill="#BFD0D3"/><rect x="-150" y="-72" width="170" height="18" rx="9" fill="#BFD0D3"/><rect x="-150" y="-34" width="290" height="18" rx="9" fill="#BFD0D3"/>
<rect x="-150" y="20" width="300" height="104" rx="24" fill="#E3F6F1" stroke="#1B9F81" stroke-width="6"/>
<text x="0" y="96" class="t" font-size="62" fill="#0B4A50" text-anchor="middle">340,71€</text>
<text x="0" y="176" class="t" font-size="38" fill="#1B9F81" text-anchor="middle">AL MESE (2026)</text></g>'''
# A: stile video 1
A=HEAD+f'''<circle cx="400" cy="380" r="300" fill="#FFD43B" opacity="0.2" filter="url(#gl)"/>
<g transform="rotate(-4 280 70)" filter="url(#sh)"><rect x="35" y="22" width="480" height="96" rx="12" fill="#E0402A" stroke="#fff" stroke-width="5"/></g>
<text x="275" y="92" class="t" font-size="54" fill="#fff" text-anchor="middle" transform="rotate(-4 280 70)">⚠ ATTENZIONE</text>
<g class="t" {S} stroke-width="22"><text x="30" y="530" font-size="250" fill="#FFD43B" letter-spacing="-8">2027</text></g>
<g class="t" {S} stroke-width="14"><text x="690" y="190" font-size="60" fill="#FFD43B">PENSIONI</text><text x="690" y="280" font-size="80" fill="#fff">INVALIDITÀ</text><text x="690" y="355" font-size="46" fill="#FF5A43">QUANTO AUMENTA?</text></g>
{CARD.format(x=1090,y=560,r=6).replace('translate(1090 560)','translate(1000 495) scale(0.55)')}
'''+STRIP('3 TRAPPOLE <tspan fill="#0D5158">CHE NESSUNO SPIEGA</tspan>')+END
# B: stile video 2
B=HEAD+f'''<circle cx="990" cy="330" r="300" fill="#FFD43B" opacity="0.2" filter="url(#gl)"/>
<g filter="url(#sh)"><circle cx="180" cy="130" r="108" fill="url(#re)" stroke="#fff" stroke-width="8"/><circle cx="560" cy="130" r="108" fill="url(#gr)" stroke="#fff" stroke-width="8"/><circle cx="370" cy="130" r="50" fill="url(#ye)" stroke="#fff" stroke-width="6"/></g>
<g class="t" text-anchor="middle" {S} stroke-width="9"><text x="180" y="152" font-size="38" fill="#fff">340,71€</text><text x="560" y="152" font-size="42" fill="#fff">≈351€</text></g>
<text x="370" y="148" class="t" font-size="44" fill="#7A3B00" text-anchor="middle">VS</text>
<g class="t" text-anchor="middle" font-size="34" fill="#fff" {S} stroke-width="8"><text x="180" y="278">OGGI 2026</text><text x="560" y="278">CON IL 3%</text></g>
<g class="t" {S} stroke-width="20"><text x="30" y="470" font-size="200" fill="#FF5A43" letter-spacing="-6">+10€</text><text x="36" y="595" font-size="130" fill="#FFD43B">AL MESE?</text></g>
{CARD.format(x=1020,y=330,r=6)}
'''+STRIP('ESEMPIO AL 3%: <tspan fill="#0D5158">IL CONTO VERO</tspan>')+END
# C: stile tabella video 3
rows=[("PENSIONE INABILITÀ","340,71€","+10€",0),("ASSEGNO MENSILE","340,71€","+10€",0),("ACCOMPAGNAMENTO","552,57€","?",1)]
tb='''<g filter="url(#sh)"><rect x="560" y="60" width="680" height="560" rx="32" fill="url(#pp)" stroke="#fff" stroke-width="6"/><rect x="560" y="60" width="680" height="100" rx="32" fill="#1B9F81"/><rect x="560" y="120" width="680" height="40" fill="#1B9F81"/></g>
<text x="600" y="125" class="t" font-size="40" fill="#fff">2026</text><text x="1200" y="125" class="t" font-size="40" fill="#fff" text-anchor="end">AUMENTO AL 3%</text>'''
for i,(a,b,c,h) in enumerate(rows):
    y=240+i*135
    if h: tb+=f'<rect x="575" y="{y-62}" width="650" height="120" rx="20" fill="#FDE3DE"/>'
    tb+=f'<text x="600" y="{y-8}" class="t" font-size="30" fill="#0B4A50">{a}</text><text x="600" y="{y+40}" class="t" font-size="48" fill="#0B4A50">{b}</text><text x="1200" y="{y+38}" class="t" font-size="{80 if h else 62}" fill="{"#C0200F" if h else "#1B9F81"}" text-anchor="end">{c}</text>'
    if i<2: tb+=f'<line x1="590" y1="{y+68}" x2="1210" y2="{y+68}" stroke="#C5D4D7" stroke-width="4"/>'
C=HEAD+f'''<g class="t" {S} stroke-width="16"><text x="30" y="100" font-size="72" fill="#fff">PENSIONI</text><text x="30" y="190" font-size="66" fill="#FFD43B">INVALIDITÀ</text><text x="30" y="300" font-size="110" fill="#FFD43B">2027:</text></g>
<g filter="url(#sh)"><rect x="30" y="350" width="470" height="100" rx="14" fill="#FFD43B"/></g><text x="265" y="423" class="t" font-size="70" fill="#0D2A2F" text-anchor="middle">QUANTO</text>
<g class="t" {S} stroke-width="16"><text x="30" y="560" font-size="76" fill="#FF5A43">DAVVERO?</text></g>
{tb}
'''+END
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg=await b.new_page(viewport={'width':1280,'height':720})
        for n,h in (('A',A),('B',B),('C',C)):
            open(f'miniatura-{n}.html','w').write(h)
            await pg.goto(f'file://{os.getcwd()}/miniatura-{n}.html'); await pg.screenshot(path=f'miniatura-{n}.png')
        await b.close()
asyncio.run(main())
