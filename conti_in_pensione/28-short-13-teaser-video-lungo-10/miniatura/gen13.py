# Miniatura short 13 (1080x1920): pensione alle casalinghe. Layout NUOVO (diverso da short 10-12 e dalle miniature A/B/C del video 10):
# grafico a barre in ALTO (quanto arriva a lei: fino a 546 euro, poi scende a 0) con la cifra del marito NASCOSTA ("? €" con lucchetto),
# parola PENSIONE al CENTRO con nastro rosso CASALINGHE, domanda in basso allineata a sinistra con pallina rossa, nessuna striscia bianca.
import os
from playwright.sync_api import sync_playwright
CH=next((c for c in ('/opt/pw-browsers/chromium-1194/chrome-linux/chrome','/opt/pw-browsers/chromium-1243/chrome-linux64/chrome') if os.path.exists(c)),None)
bars=''
H=[430,430,335,240,145,52]
for k,h in enumerate(H):
    x=150+k*108;col='url(#gr)' if k<2 else ('url(#yl)' if k<4 else 'url(#rb)')
    bars+=f'<rect x="{x}" y="{760-h}" width="90" height="{h}" rx="14" fill="{col}" stroke="#fff" stroke-width="5"/>'
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;background:#000}}svg{{display:block}}.t{{font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900}}</style></head><body>
<svg id="svg" xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
<defs>
<radialGradient id="bg" cx="0.5" cy="0.58" r="1"><stop offset="0" stop-color="#25A9AE"/><stop offset="0.5" stop-color="#0D5158"/><stop offset="1" stop-color="#03181B"/></radialGradient>
<linearGradient id="rb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF5A43"/><stop offset="1" stop-color="#C0200F"/></linearGradient>
<linearGradient id="gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3FD6AB"/><stop offset="1" stop-color="#159078"/></linearGradient>
<linearGradient id="yl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE27A"/><stop offset="1" stop-color="#F0B400"/></linearGradient>
<filter id="sh" x="-30%" y="-30%" width="170%" height="170%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#021A1D" flood-opacity="0.75"/></filter>
<filter id="gl"><feGaussianBlur stdDeviation="30"/></filter>
</defs>
<rect width="1080" height="1920" fill="url(#bg)"/>
<g opacity="0.10" fill="#fff"><path d="M540 1150 L-200 500 L0 300Z"/><path d="M540 1150 L250 -100 L470 -100Z"/><path d="M540 1150 L780 -100 L1000 -100Z"/><path d="M540 1150 L1300 500 L1300 800Z"/><path d="M540 1150 L1300 1500 L1300 1750Z"/><path d="M540 1150 L-200 1650 L0 1900Z"/><path d="M540 1150 L420 1920 L660 1920Z"/></g>
<circle cx="540" cy="1150" r="420" fill="#FFD43B" opacity="0.13" filter="url(#gl)"/>
<!-- grafico -->
<g filter="url(#sh)"><rect x="50" y="90" width="980" height="790" rx="44" fill="#fff"/></g>
<path d="M50 200 V134 a44 44 0 0 1 44 -44 H986 a44 44 0 0 1 44 44 V200Z" fill="#0B4A50"/>
<text class="t" id="h1" x="94" y="165" font-size="48" fill="#fff" letter-spacing="2">QUANTO ARRIVA A TE AL MESE</text>
<text class="t" id="v1" x="150" y="305" font-size="74" fill="#13805F">FINO A 546 €</text>
{bars}
<line x1="800" y1="372" x2="800" y2="770" stroke="#E8503A" stroke-width="9" stroke-dasharray="20 13" stroke-linecap="round"/>
<g transform="translate(800 300) scale(.78)"><g filter="url(#sh)">
<path d="M-46 -20 V-64 a46 46 0 0 1 92 0 V-20" fill="none" stroke="#7A5A00" stroke-width="18" stroke-linecap="round"/>
<rect x="-70" y="-24" width="140" height="112" rx="24" fill="#FFD43B" stroke="#fff" stroke-width="7"/></g><circle cx="0" cy="26" r="14" fill="#7A2A00"/></g>
<g filter="url(#sh)"><rect x="712" y="790" width="176" height="80" rx="40" fill="url(#rb)" stroke="#fff" stroke-width="6"/></g>
<text class="t" id="q1" x="800" y="851" font-size="56" fill="#fff" text-anchor="middle">? €</text>
<text class="t" id="z1" x="912" y="745" font-size="64" fill="#C0200F" text-anchor="middle">0 €</text>
<line x1="120" y1="770" x2="975" y2="770" stroke="#0B4A50" stroke-width="8" stroke-linecap="round"/>
<path d="M972 752 L1004 770 L972 788Z" fill="#0B4A50"/>
<text class="t" id="x1" x="110" y="844" font-size="38" fill="#0B4A50">PENSIONE DI TUO MARITO</text>
<!-- parola PENSIONE al centro + nastro -->
<g class="t" text-anchor="middle" stroke="#06282C" stroke-linejoin="round" paint-order="stroke">
<text id="t1" x="540" y="1120" font-size="176" fill="#fff" stroke-width="24">PENSIONE</text></g>
<g transform="translate(540 1245) rotate(-3)"><g filter="url(#sh)"><rect x="-430" y="-78" width="860" height="156" rx="26" fill="url(#rb)" stroke="#fff" stroke-width="8"/></g>
<text class="t" id="t2" x="0" y="38" font-size="104" fill="#fff" text-anchor="middle">CASALINGHE</text></g>
<!-- domanda in basso, a sinistra -->
<g class="t" stroke="#06282C" stroke-linejoin="round" paint-order="stroke">
<text id="d1" x="60" y="1490" font-size="112" fill="#FFD43B" stroke-width="20">TUO MARITO</text>
<text id="d2" x="60" y="1612" font-size="92" fill="#fff" stroke-width="18">PRENDE TROPPO?</text></g>
<g transform="translate(860 1770)"><circle r="118" fill="url(#rb)" stroke="#fff" stroke-width="10" filter="url(#sh)"/>
<text class="t" id="p1" y="-22" font-size="44" fill="#fff" text-anchor="middle">A TE</text>
<text class="t" id="p2" y="52" font-size="72" fill="#fff" text-anchor="middle">0 €?</text></g>
</svg></body></html>'''
here=os.path.dirname(os.path.abspath(__file__))
open(here+'/miniatura-short13.html','w',encoding='utf-8').write(html)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=CH,args=['--no-sandbox']);pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+here+'/miniatura-short13.html')
    for r in pg.evaluate("()=>[...document.querySelectorAll('text')].map(t=>{const r=t.getBoundingClientRect();return [t.id||t.textContent,Math.round(r.x),Math.round(r.y),Math.round(r.right),Math.round(r.bottom)]})"):
        print(r, 'FUORI' if r[1]<20 or r[3]>1060 else '')
    pg.screenshot(path=here+'/miniatura-short13.png');b.close()
