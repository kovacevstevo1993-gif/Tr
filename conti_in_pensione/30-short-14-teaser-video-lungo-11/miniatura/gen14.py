# Miniatura short 14 (1080x1920): aumento pensioni gennaio 2027. Layout NUOVO (diverso da short 7-13): IMBUTO delle tasse al centro,
# a sinistra 1.000 euro lordi, a destra +29 euro (stima), sotto il portafoglio con la risposta NASCOSTA ("? €"); AUMENTO PENSIONI in alto, domanda in basso.
import os
from playwright.sync_api import sync_playwright
CH=next((c for c in ('/opt/pw-browsers/chromium-1243/chrome-linux64/chrome','/opt/pw-browsers/chromium-1194/chrome-linux/chrome') if os.path.exists(c)),None)
html='''<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#000}svg{display:block}.t{font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900}</style></head><body>
<svg id="svg" xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
<defs>
<radialGradient id="bg" cx="0.5" cy="0.5" r="1"><stop offset="0" stop-color="#25A9AE"/><stop offset="0.5" stop-color="#0D5158"/><stop offset="1" stop-color="#03181B"/></radialGradient>
<linearGradient id="rb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A52"/><stop offset="1" stop-color="#B91E0E"/></linearGradient>
<linearGradient id="gd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE27A"/><stop offset="1" stop-color="#F0A800"/></linearGradient>
<linearGradient id="fn" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#C21F0F"/><stop offset="0.45" stop-color="#FF6A52"/><stop offset="1" stop-color="#B01A0C"/></linearGradient>
<filter id="sh" x="-30%" y="-30%" width="170%" height="170%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#021A1D" flood-opacity="0.75"/></filter>
<filter id="gl"><feGaussianBlur stdDeviation="34"/></filter>
</defs>
<rect width="1080" height="1920" fill="url(#bg)"/>
<g opacity="0.10" fill="#fff"><path d="M540 1000 L-200 400 L0 200Z"/><path d="M540 1000 L250 -100 L470 -100Z"/><path d="M540 1000 L780 -100 L1000 -100Z"/><path d="M540 1000 L1300 400 L1300 700Z"/><path d="M540 1000 L1300 1400 L1300 1650Z"/><path d="M540 1000 L-200 1500 L-200 1750Z"/></g>
<circle cx="540" cy="1050" r="430" fill="#FFD43B" opacity="0.14" filter="url(#gl)"/>
<!-- adesivi in alto -->
<g transform="translate(262 190) rotate(-5)"><g filter="url(#sh)"><rect x="-215" y="-48" width="430" height="96" rx="48" fill="url(#gd)" stroke="#fff" stroke-width="7"/></g><text class="t" id="a1" x="0" y="20" font-size="42" fill="#5A3A00" text-anchor="middle">GENNAIO 2027</text></g>
<g transform="translate(860 190) rotate(6)"><g filter="url(#sh)"><rect x="-150" y="-48" width="300" height="96" rx="22" fill="url(#rb)" stroke="#fff" stroke-width="7"/></g><text class="t" id="a2" x="0" y="20" font-size="54" fill="#fff" text-anchor="middle">⚠ STIME</text></g>
<!-- titolo -->
<g class="t" text-anchor="middle" stroke="#06282C" stroke-linejoin="round" paint-order="stroke">
<text id="t1" x="540" y="440" font-size="152" fill="#fff" stroke-width="26">AUMENTO</text>
<text id="t2" x="540" y="635" font-size="168" fill="#FFD43B" stroke-width="28">PENSIONI</text></g>
<g transform="translate(0 -40)">
<!-- sinistra: 1.000 euro lordi -->
<g transform="translate(215 905) rotate(-5)"><g filter="url(#sh)"><rect x="-185" y="-105" width="370" height="210" rx="30" fill="#fff"/></g>
<text class="t" id="l1" x="0" y="8" font-size="66" fill="#0D5158" text-anchor="middle">1.000 €</text>
<rect x="-110" y="34" width="220" height="52" rx="26" fill="#0B4A50"/><text class="t" id="l2" x="0" y="73" font-size="38" fill="#fff" text-anchor="middle">LORDI</text></g>
<!-- destra: +29 -->
<g transform="translate(875 905) rotate(5)"><g filter="url(#sh)"><circle r="140" fill="url(#gd)" stroke="#fff" stroke-width="9"/></g>
<circle r="116" fill="none" stroke="#fff" stroke-opacity=".7" stroke-width="5" stroke-dasharray="10 12"/>
<text class="t" id="r1" x="0" y="22" font-size="62" fill="#5A3A00" text-anchor="middle">+29 €</text></g>
<!-- imbuto -->
<g filter="url(#sh)"><path d="M150 1010 H930 Q960 1010 940 1040 L650 1330 V1450 Q650 1470 630 1470 H450 Q430 1470 430 1450 V1330 L140 1040 Q120 1010 150 1010Z" fill="url(#fn)" stroke="#fff" stroke-width="9" stroke-linejoin="round"/></g>
<ellipse cx="540" cy="1022" rx="388" ry="26" fill="#7A1208" opacity=".55"/>
<text class="t" id="f1" x="540" y="1200" font-size="150" fill="#fff" text-anchor="middle" stroke="#5A0F06" stroke-width="16" stroke-linejoin="round" paint-order="stroke">TASSE</text>
<!-- frecce verso l'imbuto -->
<path d="M335 960 H395 V928 L455 990 L395 1052 V1020 H335Z" fill="#FFD43B" stroke="#fff" stroke-width="5" stroke-linejoin="round" opacity="0"/>
<!-- portafoglio con risposta nascosta -->
<g transform="translate(540 1590)"><g filter="url(#sh)"><rect x="-230" y="-95" width="460" height="190" rx="40" fill="#0B4A50" stroke="#fff" stroke-width="8"/></g>
<path d="M-230 -35 H230" stroke="#FFD43B" stroke-width="10"/>
<g filter="url(#sh)"><circle cx="0" cy="-10" r="128" fill="url(#rb)" stroke="#fff" stroke-width="10"/></g>
<text class="t" id="q1" x="0" y="34" font-size="108" fill="#fff" text-anchor="middle">? €</text></g>
</g>
<!-- domanda -->
<g class="t" text-anchor="middle" stroke="#06282C" stroke-linejoin="round" paint-order="stroke">
<text id="d1" x="540" y="1763" font-size="98" fill="#FFD43B" stroke-width="20">QUANTO ARRIVA</text>
<text id="d2" x="540" y="1872" font-size="110" fill="#fff" stroke-width="20">DAVVERO?</text></g>
</svg></body></html>'''
here=os.path.dirname(os.path.abspath(__file__))
open(here+'/miniatura-short14.html','w',encoding='utf-8').write(html)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=CH,args=['--no-sandbox']);pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+here+'/miniatura-short14.html')
    for r in pg.evaluate("()=>[...document.querySelectorAll('text')].map(t=>{const r=t.getBoundingClientRect();return [t.id||t.textContent,Math.round(r.x),Math.round(r.y),Math.round(r.right),Math.round(r.bottom)]})"):
        print(r,'FUORI' if r[1]<20 or r[3]>1900 or r[4]>1900 or r[2]<20 else '')
    pg.screenshot(path=here+'/miniatura-short14.png');b.close()
