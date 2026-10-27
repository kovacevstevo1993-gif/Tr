import asyncio
from playwright.async_api import async_playwright
svg='''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920" style="font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900">
<defs><radialGradient id="g" cx="50%" cy="48%" r="70%"><stop offset="0" stop-color="#1E9A9A"/><stop offset="0.6" stop-color="#0F6670"/><stop offset="1" stop-color="#083B45"/></radialGradient>
<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#8FE3B0" stop-opacity=".55"/><stop offset="1" stop-color="#8FE3B0" stop-opacity="0"/></radialGradient></defs>
<rect width="1080" height="1920" fill="url(#g)"/>
<g opacity=".12" fill="#fff"><polygon points="540,960 0,300 220,0"/><polygon points="540,960 1080,200 1080,520"/><polygon points="540,960 1080,1500 800,1920"/><polygon points="540,960 0,1400 0,1700"/></g>
<ellipse cx="540" cy="900" rx="520" ry="420" fill="url(#glow)"/>
<g transform="translate(540 470) rotate(-3)"><rect x="-330" y="-60" width="660" height="120" rx="18" fill="#D8281A" stroke="#fff" stroke-width="6"/>
<text x="0" y="28" font-size="68" fill="#fff" text-anchor="middle">⚠ ATTENZIONE</text></g>
<text x="540" y="665" font-size="82" fill="#FFD43B" text-anchor="middle" stroke="#08323A" stroke-width="14" paint-order="stroke" stroke-linejoin="round">PENSIONE A</text>
<text x="520" y="1050" font-size="470" fill="#FFD43B" text-anchor="middle" letter-spacing="-14" stroke="#08323A" stroke-width="26" paint-order="stroke" stroke-linejoin="round">64</text>
<text x="540" y="1290" font-size="190" fill="#fff" text-anchor="middle" stroke="#08323A" stroke-width="20" paint-order="stroke" stroke-linejoin="round">ANNI?</text>
<rect x="110" y="1345" width="860" height="190" rx="36" fill="#fff" stroke="#FFD43B" stroke-width="12"/>
<text x="540" y="1437" font-size="84" fill="#C0200F" text-anchor="middle">LEGGE O</text>
<text x="540" y="1505" font-size="60" fill="#0D5158" text-anchor="middle" opacity="0">.</text>
</svg>'''
# riga 2 dentro il riquadro
svg=svg.replace('<text x="540" y="1437" font-size="84" fill="#C0200F" text-anchor="middle">LEGGE O</text>','<text x="540" y="1432" font-size="92" fill="#C0200F" text-anchor="middle">LEGGE O</text><text x="540" y="1530" font-size="92" fill="#0D5158" text-anchor="middle">PROPOSTA?</text>').replace('<text x="540" y="1505" font-size="60" fill="#0D5158" text-anchor="middle" opacity="0">.</text>','')
svg=svg.replace('height="190" rx="36"','height="250" rx="36"')
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'); pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.set_content('<body style="margin:0">'+svg+'</body>')
        await pg.screenshot(path='copertina-fb-verticale.png')
        # verifica: misura testi
        r=await pg.evaluate('''()=>[...document.querySelectorAll('text')].map(t=>{const b=t.getBBox();return [t.textContent,Math.round(b.x),Math.round(b.y),Math.round(b.x+b.width),Math.round(b.y+b.height)]})''')
        for x in r: print(x)
        await b.close()
asyncio.run(main())
# simulazione ritaglio 4:5 (1080x1350, centrato) e 3:4
from PIL import Image
im=Image.open('copertina-fb-verticale.png')
im.crop((0,285,1080,1635)).save('/tmp/crop45.png')
