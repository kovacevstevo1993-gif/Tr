# Miniatura short 15 (1080x1920): coefficienti 2027. Layout NUOVO (diverso da short 11-14 e dalle miniature del video 12):
# TEST A 3 DOMANDE su un blocco note con clip e spirale, ognuna con la RISPOSTA NASCOSTA ("- ? EURO", "?", "? MESI"); titolo su striscia scura inclinata in alto;
# in basso la domanda "RIENTRI ANCHE TU?" su pannello scuro. Nessuna cifra svelata.
import os
from playwright.sync_api import sync_playwright
CH=next((c for c in ('/opt/pw-browsers/chromium-1243/chrome-linux64/chrome','/opt/pw-browsers/chromium-1194/chrome-linux/chrome') if os.path.exists(c)),None)
def row(y,n,l1,l2,box,fs=62):
    return f'''<g transform="translate(0 {y})">
<circle cx="-380" cy="0" r="44" fill="#0B4A50" stroke="#fff" stroke-width="6"/><text class="t" x="-380" y="25" font-size="66" fill="#FFD43B" text-anchor="middle">{n}</text>
<text class="t" id="r{n}a" x="-318" y="{-6 if fs==62 else -2}" font-size="{fs}" fill="#0B4A50">{l1}</text>
<text class="t" id="r{n}b" x="-318" y="{64 if fs==62 else 58}" font-size="{fs}" fill="#0B4A50">{l2}</text>
{box}</g>'''
b1='<g transform="translate(275 28)"><rect x="-150" y="-92" width="300" height="184" rx="34" fill="url(#rb)" stroke="#fff" stroke-width="8"/><text class="t" id="b1" x="0" y="34" font-size="92" fill="#fff" text-anchor="middle">− ? €</text></g>'
b2='<g transform="translate(275 28)"><rect x="-150" y="-92" width="300" height="184" rx="34" fill="#0B4A50" stroke="#FFD43B" stroke-width="8"/><text class="t" id="b2" x="0" y="52" font-size="150" fill="#FFD43B" text-anchor="middle">?</text></g>'
b3='<g transform="translate(275 28)"><rect x="-150" y="-92" width="300" height="184" rx="34" fill="url(#gd)" stroke="#fff" stroke-width="8"/><text class="t" id="b3" x="0" y="16" font-size="124" fill="#5A3A00" text-anchor="middle">?</text><text class="t" id="b3b" x="0" y="74" font-size="52" fill="#5A3A00" text-anchor="middle">MESI</text></g>'
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;background:#000}}svg{{display:block}}.t{{font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900}}</style></head><body>
<svg id="svg" xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
<defs>
<radialGradient id="bg" cx="0.5" cy="0.5" r="1"><stop offset="0" stop-color="#25A9AE"/><stop offset="0.5" stop-color="#0D5158"/><stop offset="1" stop-color="#03181B"/></radialGradient>
<linearGradient id="rb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A52"/><stop offset="1" stop-color="#B91E0E"/></linearGradient>
<linearGradient id="gd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE27A"/><stop offset="1" stop-color="#F0A800"/></linearGradient>
<linearGradient id="pp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#DCE7EA"/></linearGradient>
<linearGradient id="mt" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8FA3A8"/><stop offset="0.5" stop-color="#F4F8F9"/><stop offset="1" stop-color="#7F9398"/></linearGradient>
<filter id="sh" x="-30%" y="-30%" width="170%" height="170%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#021A1D" flood-opacity="0.75"/></filter>
<filter id="gl"><feGaussianBlur stdDeviation="34"/></filter>
</defs>
<rect width="1080" height="1920" fill="url(#bg)"/>
<g opacity="0.10" fill="#fff"><path d="M540 1000 L-200 400 L0 200Z"/><path d="M540 1000 L250 -100 L470 -100Z"/><path d="M540 1000 L780 -100 L1000 -100Z"/><path d="M540 1000 L1300 400 L1300 700Z"/><path d="M540 1000 L1300 1400 L1300 1650Z"/><path d="M540 1000 L-200 1500 L-200 1750Z"/></g>
<circle cx="540" cy="1000" r="460" fill="#FFD43B" opacity="0.14" filter="url(#gl)"/>
<!-- striscia scura inclinata con il titolo -->
<g transform="translate(540 235) rotate(-4)"><g filter="url(#sh)"><rect x="-640" y="-175" width="1280" height="350" fill="#06303A" stroke="#fff" stroke-width="9"/></g>
<rect x="-640" y="-175" width="1280" height="18" fill="#FFD43B"/>
<g class="t" text-anchor="middle" stroke="#021A1D" stroke-linejoin="round" paint-order="stroke">
<text id="t1" x="0" y="-10" font-size="172" fill="#fff" stroke-width="22">PENSIONI</text>
<text id="t2" x="0" y="140" font-size="150" fill="#FFD43B" stroke-width="22">2027</text></g></g>
<!-- nastro rosso -->
<g transform="translate(540 500) rotate(2)"><g filter="url(#sh)"><rect x="-420" y="-52" width="840" height="104" rx="18" fill="url(#rb)" stroke="#fff" stroke-width="8"/></g>
<text class="t" id="n1" x="0" y="24" font-size="62" fill="#fff" text-anchor="middle">NUOVI COEFFICIENTI</text></g>
<!-- blocco note con clip -->
<g transform="translate(540 1050) rotate(-2)">
<g filter="url(#sh)"><rect x="-470" y="-440" width="940" height="900" rx="40" fill="#0B4A50" stroke="#fff" stroke-width="8"/></g>
<rect x="-440" y="-410" width="880" height="840" rx="26" fill="url(#pp)"/>
<g filter="url(#sh)"><rect x="-150" y="-478" width="300" height="86" rx="26" fill="url(#mt)" stroke="#5B7378" stroke-width="5"/></g><rect x="-86" y="-452" width="172" height="34" rx="17" fill="#0A3F45"/>
<text class="t" id="h1" x="0" y="-335" font-size="40" fill="#13805F" text-anchor="middle">3 DOMANDE · UN SOLO DECRETO</text>
<g stroke="#9FB4B9" stroke-width="4" stroke-dasharray="14 12"><line x1="-410" y1="-60" x2="410" y2="-60"/><line x1="-410" y1="170" x2="410" y2="170"/></g>
{row(-205,1,'QUANTO','PERDI?',b1)}
{row(25,2,'CHI','RIENTRA?',b2)}
{row(265,3,'MESI PER','RECUPERARE?',b3,48)}
</g>
<!-- domanda in basso -->
<g transform="translate(540 1740) rotate(1.5)"><g filter="url(#sh)"><rect x="-480" y="-135" width="960" height="270" rx="44" fill="#06303A" stroke="#fff" stroke-width="9"/></g>
<rect x="-480" y="-135" width="960" height="16" rx="8" fill="#FFD43B"/>
<g class="t" text-anchor="middle" stroke="#021A1D" stroke-linejoin="round" paint-order="stroke">
<text id="d1" x="0" y="-6" font-size="112" fill="#FFD43B" stroke-width="20">RIENTRI</text>
<text id="d2" x="0" y="100" font-size="112" fill="#fff" stroke-width="20">ANCHE TU?</text></g></g>
</svg></body></html>'''
here=os.path.dirname(os.path.abspath(__file__))
open(here+'/miniatura-short15.html','w',encoding='utf-8').write(html)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=CH,args=['--no-sandbox']);pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+here+'/miniatura-short15.html')
    for r in pg.evaluate("()=>[...document.querySelectorAll('text')].map(t=>{const r=t.getBoundingClientRect();return [t.id||t.textContent,Math.round(r.x),Math.round(r.y),Math.round(r.right),Math.round(r.bottom)]})"):
        print(r,'FUORI' if r[1]<20 or r[3]>1060 and r[0] not in ('d1','d2') or r[4]>1900 or r[2]<20 else '')
    pg.screenshot(path=here+'/miniatura-short15.png');b.close()
