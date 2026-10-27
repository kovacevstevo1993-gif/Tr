import asyncio
from playwright.async_api import async_playwright
S='stroke="#08323A" paint-order="stroke" stroke-linejoin="round"'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920" style="font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900">
<defs><radialGradient id="g" cx="50%" cy="48%" r="70%"><stop offset="0" stop-color="#1E9A9A"/><stop offset="0.6" stop-color="#0F6670"/><stop offset="1" stop-color="#083B45"/></radialGradient>
<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#8FE3B0" stop-opacity=".5"/><stop offset="1" stop-color="#8FE3B0" stop-opacity="0"/></radialGradient></defs>
<rect width="1080" height="1920" fill="url(#g)"/>
<g opacity=".12" fill="#fff"><polygon points="540,960 0,300 220,0"/><polygon points="540,960 1080,200 1080,520"/><polygon points="540,960 1080,1500 800,1920"/><polygon points="540,960 0,1400 0,1700"/></g>
<ellipse cx="540" cy="960" rx="560" ry="360" fill="url(#glow)"/>
<text x="540" y="520" font-size="64" fill="#FFD43B" text-anchor="middle" {S} stroke-width="10">CONTI IN PENSIONE</text>
<!-- fascia centrale 16:9: y 656-1264 -->
<g transform="translate(150 742) rotate(-4)"><rect x="-120" y="-34" width="480" height="68" rx="12" fill="#D8281A" stroke="#fff" stroke-width="4"/><text x="120" y="17" font-size="40" fill="#fff" text-anchor="middle">⚠ ATTENZIONE</text></g>
<text x="30" y="1050" font-size="330" fill="#FFD43B" letter-spacing="-10" {S} stroke-width="20">64</text>
<text x="775" y="850" font-size="60" fill="#FFD43B" text-anchor="middle" {S} stroke-width="10">PENSIONE A</text>
<text x="775" y="985" font-size="130" fill="#fff" text-anchor="middle" {S} stroke-width="14">ANNI?</text>
<rect x="50" y="1085" width="980" height="130" rx="30" fill="#fff" stroke="#FFD43B" stroke-width="10"/>
<text x="540" y="1178" font-size="72" fill="#C0200F" text-anchor="middle" id="l1">LEGGE O <tspan fill="#0D5158">PROPOSTA?</tspan></text>
<text x="540" y="1480" font-size="60" fill="#fff" text-anchor="middle" {S} stroke-width="10">▶ GUARDA IL VIDEO</text>
</svg>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'); pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.set_content('<body style="margin:0">'+svg+'</body>')
        await pg.screenshot(path='copertina-fb-verticale.png')
        r=await pg.evaluate('''()=>[...document.querySelectorAll('text')].map(t=>{const b=t.getBBox();return [t.textContent.slice(0,22),Math.round(b.x),Math.round(b.y),Math.round(b.x+b.width),Math.round(b.y+b.height)]})''')
        for x in r: print(x)
        await b.close()
asyncio.run(main())
from PIL import Image
im=Image.open('copertina-fb-verticale.png'); print(im.size)
im.crop((0,656,1080,1264)).save('/tmp/crop169.png')
