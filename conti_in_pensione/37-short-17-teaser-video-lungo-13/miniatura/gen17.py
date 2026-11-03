# Miniatura short 17: ASSEGNO DELLA PENSIONE inclinato con forbice che taglia l'angolo (lembo "- ? EURO"), PENSIONE gigante sotto l'assegno,
# 3 sagome (coniuge, figli, genitori) con "?", pallina QUANDO?, striscia bianca bassa con domanda. Nessuna cifra svelata.
import os
from playwright.sync_api import sync_playwright
CH=next((c for c in ('/opt/pw-browsers/chromium-1243/chrome-linux64/chrome','/opt/pw-browsers/chromium-1194/chrome-linux/chrome') if os.path.exists(c)),None)
def chip(cx,label,icon):
    return f'''<g transform="translate({cx} 1418)"><g filter="url(#sh)"><rect x="-150" y="-92" width="300" height="184" rx="26" fill="#06303A" stroke="#fff" stroke-width="7"/></g>
<rect x="-150" y="-100" width="300" height="14" rx="7" fill="#FFD43B"/>
{icon}
<circle cx="88" cy="-52" r="34" fill="url(#gd)" stroke="#fff" stroke-width="5"/><text class="t" x="88" y="-36" font-size="48" fill="#06303A" text-anchor="middle">?</text>
<text class="t" id="c_{label}" x="0" y="78" font-size="32" fill="#fff" text-anchor="middle">{label}</text></g>'''
def person(x,y,s,col):
    return f'<g transform="translate({x} {y}) scale({s})" fill="{col}"><circle cx="0" cy="-26" r="17"/><path d="M-30 30 Q-30 -4 0 -4 Q30 -4 30 30Z"/></g>'
ic1=person(-34,-6,1.15,'#FFFFFF')+person(26,-6,1.15,'#FFD43B')
ic2=person(-44,6,0.8,'#FFFFFF')+person(0,6,0.8,'#FFD43B')+person(44,6,0.8,'#FFFFFF')
ic3=person(-34,-6,1.15,'#C9D9DD')+person(26,-6,1.15,'#C9D9DD')
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;background:#000}}svg{{display:block}}.t{{font-family:'Montserrat','DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900}}</style></head><body>
<svg id="svg" xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
<defs>
<radialGradient id="bg" cx="0.5" cy="0.5" r="1"><stop offset="0" stop-color="#25A9AE"/><stop offset="0.5" stop-color="#0D5158"/><stop offset="1" stop-color="#03181B"/></radialGradient>
<linearGradient id="rb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A52"/><stop offset="1" stop-color="#B91E0E"/></linearGradient>
<linearGradient id="gd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE27A"/><stop offset="1" stop-color="#F0A800"/></linearGradient>
<linearGradient id="pp" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#D5E3E6"/></linearGradient>
<linearGradient id="bl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#F4F8F9"/><stop offset="1" stop-color="#8FA3A8"/></linearGradient>
<filter id="sh" x="-30%" y="-30%" width="170%" height="170%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#021A1D" flood-opacity="0.75"/></filter>
<filter id="gl"><feGaussianBlur stdDeviation="34"/></filter>
</defs>
<rect width="1080" height="1920" fill="url(#bg)"/>
<g opacity="0.10" fill="#fff"><path d="M540 900 L-200 300 L0 100Z"/><path d="M540 900 L250 -140 L470 -140Z"/><path d="M540 900 L780 -140 L1000 -140Z"/><path d="M540 900 L1300 300 L1300 600Z"/><path d="M540 900 L1300 1300 L1300 1550Z"/><path d="M540 900 L-200 1400 L-200 1650Z"/></g>
<circle cx="540" cy="760" r="430" fill="#FFD43B" opacity="0.13" filter="url(#gl)"/>
<!-- tag + titolo reversibilita' -->
<g transform="translate(205 296) rotate(-4)"><rect x="-150" y="-30" width="300" height="60" rx="30" fill="url(#rb)" stroke="#fff" stroke-width="5"/><text class="t" id="tag" x="0" y="11" font-size="34" fill="#fff" text-anchor="middle">ATTENZIONE</text></g>
<text class="t" id="rev" x="540" y="440" font-size="100" fill="#FFD43B" stroke="#021A1D" stroke-width="20" stroke-linejoin="round" paint-order="stroke" text-anchor="middle" textLength="940" lengthAdjust="spacingAndGlyphs">REVERSIBILITÀ</text>
<!-- assegno inclinato -->
<g transform="translate(540 800) rotate(-5)">
<g filter="url(#sh)"><path d="M-430 -190 L250 -190 L250 -110 L170 -190 Z" fill="none"/>
<path d="M-430 -190 L270 -190 L430 -30 L430 190 L-430 190 Z" fill="url(#pp)" stroke="#fff" stroke-width="6" stroke-linejoin="round"/></g>
<rect x="-430" y="-190" width="700" height="52" fill="#0D5158"/>
<text class="t" id="hd" x="-400" y="-152" font-size="30" fill="#fff" textLength="330" lengthAdjust="spacingAndGlyphs">ASSEGNO MENSILE</text>
<g fill="#C3D3D7"><rect x="-400" y="-100" width="330" height="18" rx="9"/><rect x="-400" y="-62" width="250" height="18" rx="9"/><rect x="-400" y="150" width="520" height="16" rx="8"/></g>
<rect x="-110" y="-110" width="500" height="210" rx="22" fill="#fff" stroke="#0D5158" stroke-width="6"/>
<text class="t" id="amt" x="140" y="62" font-size="140" fill="#0D5158" stroke="#fff" stroke-width="6" paint-order="stroke" text-anchor="middle" >? €</text>
<!-- linea di taglio -->
<path d="M270 -190 L430 -30" stroke="#E5301E" stroke-width="8" stroke-dasharray="16 12" fill="none"/>
</g>
<!-- lembo che si stacca -->
<g transform="translate(985 880) rotate(35)"><g filter="url(#sh)"><path d="M-58 -58 L58 -58 L58 58 Z" fill="url(#pp)" stroke="#fff" stroke-width="5" stroke-linejoin="round"/></g></g>
<g transform="translate(850 1003) rotate(7)"><rect x="-120" y="-40" width="240" height="80" rx="18" fill="url(#rb)" stroke="#fff" stroke-width="6"/><text class="t" id="cut" x="0" y="17" font-size="54" fill="#fff" text-anchor="middle">− ? €</text></g>
<!-- forbice -->
<g transform="translate(915 690) rotate(-140) scale(0.95)" filter="url(#sh)">
<path d="M0 0 L190 -34 L190 -8 Z" fill="url(#bl)" stroke="#5E7378" stroke-width="3"/><path d="M0 0 L190 34 L190 8 Z" fill="url(#bl)" stroke="#5E7378" stroke-width="3"/>
<circle cx="0" cy="0" r="9" fill="#5E7378"/>
<ellipse cx="-62" cy="-40" rx="46" ry="30" fill="none" stroke="#E5301E" stroke-width="16" transform="rotate(35 -62 -40)"/><ellipse cx="-62" cy="40" rx="46" ry="30" fill="none" stroke="#E5301E" stroke-width="16" transform="rotate(-35 -62 40)"/>
<path d="M-28 -12 L0 0 L-28 12" fill="none" stroke="#E5301E" stroke-width="14" stroke-linejoin="round"/></g>
<!-- pallina QUANDO -->
<g transform="translate(150 985) rotate(-8)"><circle r="96" fill="url(#rb)" stroke="#fff" stroke-width="9" filter="url(#sh)"/><text class="t" id="q" x="0" y="14" font-size="36" fill="#fff" text-anchor="middle" textLength="150" lengthAdjust="spacingAndGlyphs" stroke="#6A0F05" stroke-width="7" paint-order="stroke">QUANDO?</text></g>
<!-- PENSIONE gigante -->
<text class="t" id="pen" x="540" y="1222" font-size="190" fill="#fff" stroke="#021A1D" stroke-width="26" stroke-linejoin="round" paint-order="stroke" text-anchor="middle" textLength="940" lengthAdjust="spacingAndGlyphs">PENSIONE</text>
<!-- chi ha diritto -->
<g transform="translate(540 1296)"><text class="t" id="chi" x="0" y="0" font-size="38" fill="#FFD43B" stroke="#021A1D" stroke-width="10" paint-order="stroke" text-anchor="middle" textLength="520" lengthAdjust="spacingAndGlyphs">CHI HA DIRITTO?</text></g>
{chip(190,'CONIUGE',ic1)}{chip(540,'FIGLI',ic2)}{chip(890,'GENITORI',ic3)}
<!-- striscia bassa -->
<g transform="translate(540 1604) rotate(-1)"><g filter="url(#sh)"><rect x="-480" y="-66" width="960" height="132" rx="18" fill="#fff" stroke="#FFD43B" stroke-width="10"/></g>
<text class="t" id="s1" x="0" y="-8" font-size="56" fill="#0B4A50" text-anchor="middle">L'INPS PUÒ TAGLIARLA?</text>
<text class="t" id="s2" x="0" y="40" font-size="34" fill="#C4200F" text-anchor="middle">C'È UN CASO IN CUI NON LA TAGLIA</text></g>
</svg></body></html>'''
here=os.path.dirname(os.path.abspath(__file__))
open(here+'/miniatura-short17.html','w',encoding='utf-8').write(html)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=CH,args=['--no-sandbox']);pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+here+'/miniatura-short17.html')
    for r in pg.evaluate("()=>[...document.querySelectorAll('text')].map(t=>{const r=t.getBoundingClientRect();return [t.id||t.textContent,Math.round(r.x),Math.round(r.y),Math.round(r.right),Math.round(r.bottom)]})"):
        print(r,'FUORI' if r[1]<60 or r[3]>1020 or r[2]<250 or r[4]>1670 else '')
    pg.screenshot(path=here+'/miniatura-short17.png');b.close()
from PIL import Image
im=Image.open(here+'/miniatura-short17.png');print(im.size);im.resize((270,480)).save('/tmp/claude-0/-home-user-Tr/23ff82fb-02ca-53af-8113-e12cc83d6c26/scratchpad/small17.png')
