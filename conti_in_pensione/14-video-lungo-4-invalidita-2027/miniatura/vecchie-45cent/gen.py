import asyncio
from playwright.async_api import async_playwright
HEAD='''<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#000}svg{display:block}.t{font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900}</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">
<defs>
<radialGradient id="bg" cx="0.7" cy="0.45" r="1"><stop offset="0" stop-color="#25A9AE"/><stop offset="0.5" stop-color="#0D5158"/><stop offset="1" stop-color="#03181B"/></radialGradient>
<radialGradient id="gr" cx="0.4" cy="0.3" r="0.8"><stop offset="0" stop-color="#9CFFD9"/><stop offset="0.5" stop-color="#25D08C"/><stop offset="1" stop-color="#0B7C54"/></radialGradient>
<radialGradient id="re" cx="0.4" cy="0.3" r="0.8"><stop offset="0" stop-color="#FFB3A3"/><stop offset="0.5" stop-color="#F0503A"/><stop offset="1" stop-color="#9E2112"/></radialGradient>
<radialGradient id="ye" cx="0.4" cy="0.3" r="0.8"><stop offset="0" stop-color="#FFF3A8"/><stop offset="0.5" stop-color="#FFD43B"/><stop offset="1" stop-color="#C08A00"/></radialGradient>
<linearGradient id="pp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#D6E4E7"/></linearGradient>
<filter id="sh" x="-30%" y="-30%" width="170%" height="170%"><feDropShadow dx="0" dy="12" stdDeviation="12" flood-color="#021A1D" flood-opacity="0.75"/></filter>
<filter id="gl"><feGaussianBlur stdDeviation="24"/></filter>
</defs>
<rect width="1280" height="720" fill="url(#bg)"/>
<g opacity="0.10" fill="#fff"><path d="M980 330 L500 -200 L700 -200Z"/><path d="M980 330 L900 -200 L1100 -200Z"/><path d="M980 330 L1300 -200 L1500 0Z"/><path d="M980 330 L1500 300 L1500 520Z"/><path d="M980 330 L1300 900 L1100 900Z"/><path d="M980 330 L700 900 L500 900Z"/><path d="M980 330 L-100 500 L-100 300Z"/></g>
'''
S='stroke="#06282C" stroke-linejoin="round" paint-order="stroke"'
A=HEAD+f'''<circle cx="900" cy="330" r="300" fill="#FFD43B" opacity="0.22" filter="url(#gl)"/>
<g class="t" {S} stroke-width="20">
<text x="30" y="120" font-size="92" fill="#fff">INVALIDITÀ 2027:</text>
<text x="30" y="300" font-size="170" fill="#FFD43B" letter-spacing="-5">SOLO</text>
<text x="30" y="480" font-size="150" fill="#FF5A43" letter-spacing="-4">45 CENT!</text></g>
<g transform="translate(1030 400) rotate(5) scale(0.74)" filter="url(#sh)">
<rect x="-290" y="-215" width="580" height="430" rx="28" fill="url(#pp)" stroke="#fff" stroke-width="6"/>
<rect x="-290" y="-215" width="580" height="82" rx="28" fill="#1B9F81"/><rect x="-290" y="-180" width="580" height="47" fill="#1B9F81"/>
<text x="0" y="-155" class="t" font-size="44" fill="#fff" text-anchor="middle">PENSIONE INVALIDITÀ</text>
<text x="-250" y="-60" class="t" font-size="42" fill="#0B4A50">2025</text><text x="250" y="-60" class="t" font-size="52" fill="#0B4A50" text-anchor="end">747,84€</text>
<line x1="-250" y1="-30" x2="250" y2="-30" stroke="#BFD0D3" stroke-width="5"/>
<text x="-250" y="45" class="t" font-size="42" fill="#0B4A50">2026</text><text x="250" y="45" class="t" font-size="52" fill="#0B4A50" text-anchor="end">748,29€</text>
<rect x="-250" y="85" width="500" height="100" rx="24" fill="#FDE3DE" stroke="#E0402A" stroke-width="6"/>
<text x="0" y="158" class="t" font-size="70" fill="#C0200F" text-anchor="middle">+0,45€</text></g>
<g filter="url(#sh)"><rect x="30" y="600" width="800" height="90" rx="22" fill="#fff"/><rect x="30" y="600" width="800" height="90" rx="22" fill="none" stroke="#FFD43B" stroke-width="7"/></g>
<text x="430" y="662" class="t" font-size="46" fill="#0D5158" text-anchor="middle">TOTALE AL MESE: <tspan fill="#C0200F">PERCHÉ?</tspan></text>
</svg></body></html>'''
B=HEAD+f'''<g class="t" {S} stroke-width="16">
<text x="30" y="105" font-size="86" fill="#fff">INVALIDITÀ</text>
<text x="30" y="205" font-size="86" fill="#FFD43B">2027:</text></g>
<g class="t" {S} stroke-width="16"><text x="30" y="300" font-size="58" fill="#fff">L'AUMENTO NON</text><text x="30" y="365" font-size="58" fill="#FF5A43">ARRIVA A TUTTI</text></g>
<g filter="url(#sh)"><rect x="30" y="400" width="600" height="280" rx="26" fill="url(#pp)" stroke="#fff" stroke-width="6"/></g>
<g class="t" font-size="42">
<text x="60" y="470" fill="#0B4A50">PENSIONE</text><text x="600" y="470" fill="#1B9F81" text-anchor="end">+4,71€</text>
<line x1="60" y1="492" x2="600" y2="492" stroke="#BFD0D3" stroke-width="4"/>
<text x="60" y="552" fill="#0B4A50">INCREMENTO</text><text x="600" y="552" fill="#E0402A" text-anchor="end">−4,26€</text>
<line x1="60" y1="574" x2="600" y2="574" stroke="#BFD0D3" stroke-width="4"/></g>
<rect x="50" y="590" width="560" height="74" rx="16" fill="#FDE3DE"/>
<text x="60" y="645" class="t" font-size="46" fill="#0B4A50">TOTALE</text><text x="600" y="647" class="t" font-size="54" fill="#C0200F" text-anchor="end">+0,45€</text>
<g transform="translate(965 340)" filter="url(#sh)"><circle r="270" fill="url(#ye)" stroke="#fff" stroke-width="12"/><circle r="236" fill="none" stroke="#C08A00" stroke-width="7"/>
<text x="0" y="-90" class="t" font-size="50" fill="#7A3B00" text-anchor="middle">PRIMA</text>
<text x="0" y="-30" class="t" font-size="50" fill="#7A3B00" text-anchor="middle">DEL TEST</text>
<text x="0" y="125" class="t" font-size="140" fill="#8A1F10" text-anchor="middle">?!</text>
<text x="0" y="190" class="t" font-size="42" fill="#7A3B00" text-anchor="middle">DATI INPS</text></g>
</svg></body></html>'''
C=HEAD+f'''<circle cx="640" cy="330" r="420" fill="#FFD43B" opacity="0.14" filter="url(#gl)"/>
<g class="t" {S} stroke-width="18" text-anchor="middle">
<text x="640" y="110" font-size="78" fill="#fff">PENSIONI INVALIDITÀ 2027</text>
<text x="640" y="205" font-size="64" fill="#FFD43B">QUANTO AUMENTA DAVVERO?</text></g>
<g filter="url(#sh)">
<rect x="60" y="260" width="520" height="300" rx="30" fill="url(#pp)" stroke="#fff" stroke-width="6"/>
<rect x="700" y="260" width="520" height="300" rx="30" fill="url(#pp)" stroke="#fff" stroke-width="6"/></g>
<g class="t" text-anchor="middle">
<text x="320" y="325" font-size="38" fill="#1B9F81">COSA SPERI</text>
<text x="320" y="450" font-size="100" fill="#1B9F81">+10€</text>
<text x="320" y="520" font-size="36" fill="#0B4A50">sul totale</text>
<text x="960" y="325" font-size="38" fill="#E0402A">COSA SUCCEDE</text>
<text x="960" y="450" font-size="100" fill="#C0200F">+0,45€</text>
<text x="960" y="520" font-size="36" fill="#0B4A50">nel 2026, dati Inps</text></g>
<g filter="url(#sh)"><circle cx="640" cy="410" r="62" fill="url(#ye)" stroke="#fff" stroke-width="7"/></g>
<text x="640" y="432" class="t" font-size="56" fill="#7A3B00" text-anchor="middle">VS</text>
<g filter="url(#sh)"><rect x="150" y="605" width="980" height="86" rx="22" fill="#fff"/><rect x="150" y="605" width="980" height="86" rx="22" fill="none" stroke="#FFD43B" stroke-width="7"/></g>
<text x="640" y="665" class="t" font-size="46" fill="#C0200F" text-anchor="middle">LA TRAPPOLA <tspan fill="#0D5158">CHE NESSUNO SPIEGA</tspan></text>
</svg></body></html>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg=await b.new_page(viewport={'width':1280,'height':720})
        for n,h in (('A',A),('B',B),('C',C)):
            open(f'miniatura-{n}.html','w').write(h)
            await pg.goto(f'file://{__import__("os").getcwd()}/miniatura-{n}.html')
            await pg.screenshot(path=f'miniatura-{n}.png')
        await b.close()
asyncio.run(main())
