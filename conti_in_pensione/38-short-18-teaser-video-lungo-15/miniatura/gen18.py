# Miniatura short 18: 500 € gigante in alto, carta prepagata inclinata con nastro NON A TUTTI, pensionato (sagoma neutra) in cerchio con "?",
# PENSIONATI gigante + LA PRENDI? giallo, striscia bianca bassa. La risposta NON e' svelata. Layout nuovo (nessun assegno/forbici/tre schede come S17, nessun duello di carte come V15-A).
import os
from playwright.sync_api import sync_playwright
CH=next((c for c in ('/opt/pw-browsers/chromium-1243/chrome-linux64/chrome','/opt/pw-browsers/chromium-1194/chrome-linux/chrome') if os.path.exists(c)),None)
html='''<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#000}svg{display:block}.t{font-family:'Montserrat','DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900}</style></head><body>
<svg id="svg" xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
<defs>
<radialGradient id="bg" cx="0.5" cy="0.45" r="1"><stop offset="0" stop-color="#25A9AE"/><stop offset="0.5" stop-color="#0D5158"/><stop offset="1" stop-color="#03181B"/></radialGradient>
<linearGradient id="rb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A52"/><stop offset="1" stop-color="#B91E0E"/></linearGradient>
<linearGradient id="gd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE27A"/><stop offset="1" stop-color="#F0A800"/></linearGradient>
<linearGradient id="cd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2BCB9C"/><stop offset="1" stop-color="#0B6B58"/></linearGradient>
<filter id="sh" x="-30%" y="-30%" width="170%" height="170%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#021A1D" flood-opacity="0.75"/></filter>
<filter id="gl"><feGaussianBlur stdDeviation="34"/></filter>
</defs>
<rect width="1080" height="1920" fill="url(#bg)"/>
<g opacity="0.10" fill="#fff"><path d="M540 960 L-200 300 L0 100Z"/><path d="M540 960 L250 -140 L470 -140Z"/><path d="M540 960 L780 -140 L1000 -140Z"/><path d="M540 960 L1300 300 L1300 600Z"/><path d="M540 960 L1300 1300 L1300 1550Z"/><path d="M540 960 L-200 1300 L-200 1550Z"/><path d="M540 960 L300 2100 L520 2100Z"/><path d="M540 960 L800 2100 L1000 2100Z"/></g>
<circle cx="540" cy="760" r="420" fill="#FFD43B" opacity="0.13" filter="url(#gl)"/>
<!-- tag -->
<g transform="translate(230 312) rotate(-4)"><rect x="-190" y="-32" width="380" height="64" rx="32" fill="url(#rb)" stroke="#fff" stroke-width="5"/><text class="t" id="tag" x="0" y="12" font-size="36" fill="#fff" text-anchor="middle">DAL 4 NOVEMBRE</text></g>
<!-- 500 gigante -->
<text class="t" id="n500" x="540" y="560" font-size="250" fill="#FFD43B" stroke="#021A1D" stroke-width="26" stroke-linejoin="round" paint-order="stroke" text-anchor="middle" textLength="800" lengthAdjust="spacingAndGlyphs">500 €</text>
<!-- carta inclinata -->
<g transform="translate(470 860) rotate(-6)">
<g filter="url(#sh)"><rect x="-400" y="-230" width="800" height="460" rx="44" fill="url(#cd)" stroke="#fff" stroke-width="7"/></g>
<path d="M-356 -230 H356 Q400 -230 400 -186 V-130 Q0 -90 -400 -130 V-186 Q-400 -230 -356 -230Z" fill="#fff" opacity="0.14"/>
<rect x="-340" y="-70" width="120" height="92" rx="16" fill="#FFB020" stroke="#fff" stroke-width="4"/><path d="M-340 -24 H-220 M-280 -70 V22" stroke="#C98300" stroke-width="4" fill="none"/>
<g fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity="0.85"><path d="M-190 -42 q14 18 0 36"/><path d="M-170 -56 q22 32 0 64"/><path d="M-150 -70 q30 46 0 92"/></g>
<text class="t" id="cart" x="-340" y="-150" font-size="46" fill="#fff" textLength="640" lengthAdjust="spacingAndGlyphs">CARTA DEDICATA A TE</text>
<g transform="translate(-110 130) rotate(-3)"><rect x="-280" y="-46" width="560" height="92" rx="14" fill="url(#rb)" stroke="#fff" stroke-width="6"/><text class="t" id="nat" x="0" y="22" font-size="62" fill="#fff" text-anchor="middle" textLength="480" lengthAdjust="spacingAndGlyphs">NON A TUTTI</text></g>
</g>
<!-- pensionato in cerchio con ? -->
<g transform="translate(890 905)"><g filter="url(#sh)"><circle r="140" fill="#fff" stroke="#FFD43B" stroke-width="10"/></g>
<g fill="#06303A"><circle cx="-14" cy="-52" r="38"/><path d="M-84 80 Q-84 4 -14 4 Q56 4 56 80Z"/></g>
<path d="M82 80 V8 q0 -26 -26 -26" fill="none" stroke="#06303A" stroke-width="12" stroke-linecap="round"/>
<g transform="translate(96 -112)"><circle r="56" fill="url(#rb)" stroke="#fff" stroke-width="7"/><text class="t" id="qm" x="0" y="26" font-size="78" fill="#fff" text-anchor="middle">?</text></g></g>
<!-- parole giganti -->
<text class="t" id="pen" x="540" y="1250" font-size="180" fill="#fff" stroke="#021A1D" stroke-width="26" stroke-linejoin="round" paint-order="stroke" text-anchor="middle" textLength="940" lengthAdjust="spacingAndGlyphs">PENSIONATI</text>
<text class="t" id="pre" x="540" y="1420" font-size="150" fill="#FFD43B" stroke="#021A1D" stroke-width="24" stroke-linejoin="round" paint-order="stroke" text-anchor="middle" textLength="820" lengthAdjust="spacingAndGlyphs">LA PRENDI?</text>
<!-- striscia bassa -->
<g transform="translate(540 1566) rotate(-1)"><g filter="url(#sh)"><rect x="-480" y="-66" width="960" height="132" rx="18" fill="#fff" stroke="#FFD43B" stroke-width="10"/></g>
<text class="t" id="s1" x="0" y="-8" font-size="54" fill="#0B4A50" text-anchor="middle">IL DECRETO NON LO SCRIVE</text>
<text class="t" id="s2" x="0" y="40" font-size="34" fill="#C4200F" text-anchor="middle">LA RISPOSTA È ALTROVE</text></g>
</svg></body></html>'''
here=os.path.dirname(os.path.abspath(__file__))
open(here+'/miniatura-short18.html','w',encoding='utf-8').write(html)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=CH,args=['--no-sandbox']);pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+here+'/miniatura-short18.html')
    for r in pg.evaluate("()=>[...document.querySelectorAll('text')].map(t=>{const r=t.getBoundingClientRect();return [t.id||t.textContent,Math.round(r.x),Math.round(r.y),Math.round(r.right),Math.round(r.bottom)]})"):
        print(r,'FUORI' if r[1]<40 or r[3]>1040 or r[2]<250 or r[4]>1670 else '')
    pg.screenshot(path=here+'/miniatura-short18.png');b.close()
