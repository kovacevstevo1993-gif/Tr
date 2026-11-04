# Miniatura short 16 (1080x1920): manovra 2027. Layout NUOVO (diverso da short 13-15 e dalle miniature del video 14):
# FACCIATA DI PALAZZO con frontone e TRE PORTE CHIUSE (BUONO, FONDO, IRPEF), ognuna con "?" dorato, luce che filtra da sotto;
# titolo in alto senza striscia; striscia bianca con bordo giallo "LE 3 NOVITA' DEL GOVERNO"; in basso la domanda "CHI CI GUADAGNA DAVVERO?". Nessuna cifra, nessuna risposta svelata.
import os
from playwright.sync_api import sync_playwright
CH=next((c for c in ('/opt/pw-browsers/chromium-1243/chrome-linux64/chrome','/opt/pw-browsers/chromium-1194/chrome-linux/chrome') if os.path.exists(c)),None)
def door(cx,name,fill_top='#12707A'):
    return f'''<g transform="translate({cx} 985)">
<ellipse cx="0" cy="238" rx="190" ry="46" fill="#FFE27A" opacity="0.55" filter="url(#gl2)"/>
<g filter="url(#sh)"><rect x="-140" y="-240" width="280" height="480" rx="20" fill="url(#dr)" stroke="#FFD43B" stroke-width="9"/></g>
<rect x="-112" y="-70" width="224" height="290" rx="12" fill="#06303A" opacity="0.35"/>
<rect x="-118" y="-212" width="236" height="62" rx="14" fill="#fff" stroke="#FFD43B" stroke-width="5"/>
<text class="t" id="n_{name}" x="0" y="-166" font-size="44" fill="#0B4A50" text-anchor="middle">{name}</text>
<circle cx="0" cy="20" r="84" fill="url(#gd)" stroke="#fff" stroke-width="7"/>
<text class="t" id="q_{name}" x="0" y="72" font-size="138" fill="#06303A" text-anchor="middle">?</text>
<circle cx="86" cy="176" r="15" fill="#FFD43B"/><rect x="82" y="176" width="8" height="26" rx="3" fill="#FFD43B"/>
<rect x="-140" y="228" width="280" height="12" fill="#FFF3B0"/></g>'''
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;background:#000}}svg{{display:block}}.t{{font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900}}</style></head><body>
<svg id="svg" xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
<defs>
<radialGradient id="bg" cx="0.5" cy="0.45" r="1"><stop offset="0" stop-color="#25A9AE"/><stop offset="0.5" stop-color="#0D5158"/><stop offset="1" stop-color="#03181B"/></radialGradient>
<linearGradient id="rb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A52"/><stop offset="1" stop-color="#B91E0E"/></linearGradient>
<linearGradient id="gd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE27A"/><stop offset="1" stop-color="#F0A800"/></linearGradient>
<linearGradient id="pp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#C9D9DD"/></linearGradient>
<linearGradient id="dr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1B8C93"/><stop offset="1" stop-color="#0A4047"/></linearGradient>
<linearGradient id="st" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C9D6D8"/><stop offset="1" stop-color="#8FA3A8"/></linearGradient>
<filter id="sh" x="-30%" y="-30%" width="170%" height="170%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#021A1D" flood-opacity="0.75"/></filter>
<filter id="gl"><feGaussianBlur stdDeviation="34"/></filter><filter id="gl2"><feGaussianBlur stdDeviation="18"/></filter>
</defs>
<rect width="1080" height="1920" fill="url(#bg)"/>
<g opacity="0.10" fill="#fff"><path d="M540 960 L-200 360 L0 160Z"/><path d="M540 960 L250 -140 L470 -140Z"/><path d="M540 960 L780 -140 L1000 -140Z"/><path d="M540 960 L1300 360 L1300 660Z"/><path d="M540 960 L1300 1360 L1300 1610Z"/><path d="M540 960 L-200 1460 L-200 1710Z"/></g>
<circle cx="540" cy="980" r="470" fill="#FFD43B" opacity="0.13" filter="url(#gl)"/>
<!-- etichetta in alto a destra -->
<g transform="translate(838 92) rotate(3)"><rect x="-190" y="-34" width="380" height="68" rx="34" fill="#06303A" stroke="#fff" stroke-width="5"/><text class="t" id="dl" x="0" y="11" font-size="31" fill="#fff" text-anchor="middle">DISEGNO DI LEGGE</text></g>
<!-- titolo -->
<g class="t" text-anchor="middle" stroke="#021A1D" stroke-linejoin="round" paint-order="stroke">
<text id="t1" x="540" y="300" font-size="168" fill="#fff" stroke-width="24">PENSIONI</text>
<text id="t2" x="540" y="424" font-size="104" fill="#FFD43B" stroke-width="20">MANOVRA 2027</text></g>
<!-- striscia bianca con bordo giallo -->
<g transform="translate(540 514) rotate(-1.5)"><g filter="url(#sh)"><rect x="-455" y="-52" width="910" height="104" rx="16" fill="#fff" stroke="#FFD43B" stroke-width="10"/></g>
<text class="t" id="s1" x="0" y="20" font-size="54" fill="#0B4A50" text-anchor="middle">LE 3 NOVITÀ DEL GOVERNO</text></g>
<!-- facciata: frontone, colonne, gradini -->
<g filter="url(#sh)"><path d="M60 700 L540 590 L1020 700Z" fill="url(#pp)" stroke="#fff" stroke-width="5" stroke-linejoin="round"/></g>
<circle cx="540" cy="672" r="30" fill="url(#gd)" stroke="#fff" stroke-width="5"/>
<rect x="50" y="700" width="980" height="34" fill="#DCE7EA"/>
<g fill="#F3F8F9" stroke="#C9D6D8" stroke-width="3"><rect x="62" y="734" width="40" height="520" rx="8"/><rect x="378" y="734" width="40" height="520" rx="8"/><rect x="662" y="734" width="40" height="520" rx="8"/><rect x="978" y="734" width="40" height="520" rx="8"/></g>
{door(240,'BUONO')}{door(540,'FONDO')}{door(840,'IRPEF')}
<rect x="40" y="1254" width="1000" height="30" fill="url(#st)"/><rect x="10" y="1284" width="1060" height="32" fill="#8FA3A8"/>
<!-- domanda in basso -->
<g transform="translate(540 1590) rotate(1)"><g filter="url(#sh)"><rect x="-490" y="-190" width="980" height="380" rx="44" fill="#06303A" stroke="#fff" stroke-width="9"/></g>
<rect x="-490" y="-190" width="980" height="18" rx="9" fill="#FFD43B"/>
<g class="t" text-anchor="middle" stroke="#021A1D" stroke-linejoin="round" paint-order="stroke">
<text id="d1" x="0" y="-30" font-size="86" fill="#fff" stroke-width="18">CHI CI GUADAGNA</text>
<text id="d2" x="0" y="120" font-size="138" fill="#FFD43B" stroke-width="22">DAVVERO?</text></g></g>
</svg></body></html>'''
here=os.path.dirname(os.path.abspath(__file__))
open(here+'/miniatura-short16.html','w',encoding='utf-8').write(html)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=CH,args=['--no-sandbox']);pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+here+'/miniatura-short16.html')
    for r in pg.evaluate("()=>[...document.querySelectorAll('text')].map(t=>{const r=t.getBoundingClientRect();return [t.id||t.textContent,Math.round(r.x),Math.round(r.y),Math.round(r.right),Math.round(r.bottom)]})"):
        print(r,'FUORI' if r[1]<24 or r[3]>1056 or r[2]<24 or r[4]>1896 else '')
    pg.screenshot(path=here+'/miniatura-short16.png');b.close()
