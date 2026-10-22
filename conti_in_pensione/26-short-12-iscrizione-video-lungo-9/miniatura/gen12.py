# Miniatura short 12 (1080x1920): due pensionati affiancati, 10 EUR di differenza, bonus si'/no. Layout nuovo: cifra gigante sopra, due schede ritratto con pallina verde/rossa e disco "stessa pensione" al centro.
import os,sys
from playwright.sync_api import sync_playwright
def bust(shirt,hair):
    return f'''<path d="M-135 232 Q-135 92 0 92 Q135 92 135 232 Z" fill="{shirt}" stroke="#fff" stroke-width="7" stroke-linejoin="round"/>
<path d="M-38 98 L0 158 L38 98 Z" fill="#fff"/><path d="M-11 158 L0 226 L11 158 Z" fill="#0B3A3F"/>
<rect x="-26" y="48" width="52" height="56" rx="16" fill="#EDBE92"/><circle cx="0" cy="0" r="80" fill="#F7D3B0" stroke="#fff" stroke-width="6"/>
<path d="M-82 -8 Q-84 -96 0 -96 Q84 -96 82 -8 Q44 -52 -8 -50 Q-52 -48 -82 -8Z" fill="{hair}"/>
<circle cx="-27" cy="10" r="9" fill="#0B3A3F"/><circle cx="27" cy="10" r="9" fill="#0B3A3F"/>
<path d="M-28 40 Q0 66 28 40" fill="none" stroke="#B5523B" stroke-width="8" stroke-linecap="round"/>'''
def card(x,ok,shirt,hair,cid):
    col='url(#gr)' if ok else 'url(#rb)'
    lab='BONUS' if ok else 'ZERO'
    ball=('<path d="M-30 2 l20 22 l40 -44" fill="none" stroke="#fff" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>' if ok else '<path d="M-24 -24 L24 24 M24 -24 L-24 24" stroke="#fff" stroke-width="16" stroke-linecap="round"/>')
    return f'''<g transform="translate({x} 740)">
<g filter="url(#sh)"><rect width="440" height="550" rx="40" fill="#fff"/></g>
<clipPath id="{cid}"><rect width="440" height="550" rx="40"/></clipPath>
<g clip-path="url(#{cid})"><rect width="440" height="550" fill="#CBE8E2"/>
<g transform="translate(220 262) scale(1.22)">{bust(shirt,hair)}</g>
<rect y="448" width="440" height="102" fill="{col}"/>
<text class="t" id="lab{cid}" x="220" y="522" font-size="64" fill="#fff" text-anchor="middle" stroke="#06282C" stroke-width="8" stroke-linejoin="round" paint-order="stroke">{lab}</text></g>
<rect width="440" height="550" rx="40" fill="none" stroke="#fff" stroke-width="8"/>
<g transform="translate(372 70)"><circle r="64" fill="{col}" stroke="#fff" stroke-width="9" filter="url(#sh)"/>{ball}</g></g>'''
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;background:#000}}svg{{display:block}}.t{{font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900}}</style></head><body>
<svg id="svg" xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
<defs>
<radialGradient id="bg" cx="0.5" cy="0.45" r="1"><stop offset="0" stop-color="#25A9AE"/><stop offset="0.5" stop-color="#0D5158"/><stop offset="1" stop-color="#03181B"/></radialGradient>
<linearGradient id="rb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF5A43"/><stop offset="1" stop-color="#C0200F"/></linearGradient>
<linearGradient id="gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3FD6AB"/><stop offset="1" stop-color="#159078"/></linearGradient>
<filter id="sh" x="-30%" y="-30%" width="170%" height="170%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#021A1D" flood-opacity="0.75"/></filter>
<filter id="gl"><feGaussianBlur stdDeviation="30"/></filter>
</defs>
<rect width="1080" height="1920" fill="url(#bg)"/>
<g opacity="0.10" fill="#fff"><path d="M540 900 L-200 200 L0 0Z"/><path d="M540 900 L300 -100 L520 -100Z"/><path d="M540 900 L760 -100 L980 -100Z"/><path d="M540 900 L1300 300 L1300 600Z"/><path d="M540 900 L1300 1300 L1300 1500Z"/><path d="M540 900 L-200 1400 L0 1650Z"/></g>
<circle cx="540" cy="620" r="380" fill="#FFD43B" opacity="0.14" filter="url(#gl)"/>
<g class="t" text-anchor="middle" stroke="#06282C" stroke-linejoin="round" paint-order="stroke">
<text id="t1" x="540" y="215" font-size="176" fill="#fff" stroke-width="22">PENSIONI</text>
<text id="t2" x="540" y="345" font-size="112" fill="#FFD43B" stroke-width="18">DICEMBRE</text>
<text id="n1" x="540" y="585" font-size="232" fill="#3FE0A6" stroke-width="28">10 €</text>
<text id="n2" x="540" y="672" font-size="60" fill="#fff" stroke-width="12">AL MESE DI DIFFERENZA</text></g>
{card(50,True,'#1B9F81','#5A6E73','c1')}
{card(590,False,'#C98500','#9AA5A8','c2')}
<g transform="translate(540 1015)"><circle r="66" fill="#06303A" stroke="#FFD43B" stroke-width="8" filter="url(#sh)"/><text class="t" id="eq" y="26" font-size="86" fill="#FFD43B" text-anchor="middle">≈</text></g>
<g filter="url(#sh)"><rect x="150" y="1330" width="780" height="120" rx="60" fill="#FFD43B" stroke="#fff" stroke-width="8"/></g>
<text class="t" id="gp" x="540" y="1410" font-size="66" fill="#5A3A00" text-anchor="middle">BONUS 154,94 €</text>
<g filter="url(#sh)"><rect x="60" y="1510" width="960" height="270" rx="34" fill="#fff" stroke="#FFD43B" stroke-width="12"/></g>
<g class="t" text-anchor="middle"><text id="s1" x="540" y="1618" font-size="62" fill="#0D5158">PERCHÉ UNO LO PRENDE</text><text id="s2" x="540" y="1715" font-size="76" fill="#C0200F">E L'ALTRO ZERO?</text></g>
</svg></body></html>'''
here=os.path.dirname(os.path.abspath(__file__))
open(here+'/miniatura-short12.html','w',encoding='utf-8').write(html)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']);pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+here+'/miniatura-short12.html')
    for r in pg.evaluate("()=>[...document.querySelectorAll('text')].map(t=>{const r=t.getBoundingClientRect();return [t.id||t.textContent,Math.round(r.x),Math.round(r.y),Math.round(r.right),Math.round(r.bottom)]})"):
        print(r, 'FUORI' if r[1]<20 or r[3]>1060 else '')
    pg.screenshot(path=here+'/miniatura-short12.png');b.close()
