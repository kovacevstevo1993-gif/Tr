S='stroke="#06242B" paint-order="stroke" stroke-linejoin="round"'
def bar(y,w,black=False):
    return f'<rect x="50" y="{y}" width="{w}" height="26" rx="6" fill="{"#0B1A1F" if black else "#CBD7D9"}"/>'
lines=''
ys=[190,240,290,340,420,470,520,640,690,740,790]
ws=[500,430,520,360,520,470,400,520,440,500,300]
blk={1,2,5,8}
for i,(y,w) in enumerate(zip(ys,ws)): lines+=bar(y,w,i in blk)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" style="font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0E7C86"/><stop offset=".5" stop-color="#0A5360"/><stop offset="1" stop-color="#041E27"/></linearGradient>
<radialGradient id="spot" cx="75%" cy="50%" r="45%"><stop offset="0" stop-color="#7DE8C4" stop-opacity=".55"/><stop offset="1" stop-color="#7DE8C4" stop-opacity="0"/></radialGradient>
<linearGradient id="y" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE777"/><stop offset="1" stop-color="#FFB400"/></linearGradient>
<linearGradient id="r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A55"/><stop offset="1" stop-color="#C21808"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#010d11" flood-opacity=".7"/></filter>
<pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M60 0H0V60" fill="none" stroke="#fff" stroke-opacity=".06" stroke-width="2"/></pattern>
</defs>
<rect width="1920" height="1080" fill="url(#bg)"/><rect width="1920" height="1080" fill="url(#grid)"/>
<ellipse cx="1480" cy="540" rx="620" ry="620" fill="url(#spot)"/>
<g transform="translate(50 44) rotate(-2)" filter="url(#sh)"><rect width="500" height="84" rx="14" fill="url(#r)" stroke="#fff" stroke-width="5"/><text x="250" y="60" font-size="50" fill="#fff" text-anchor="middle">⚠ ATTENZIONE</text></g>
<text x="56" y="350" font-size="170" fill="url(#y)" {S} stroke-width="22" id="a1">PENSIONE</text>
<text x="56" y="540" font-size="170" fill="#fff" {S} stroke-width="22" id="a2">A <tspan fill="url(#y)">64</tspan> ANNI?</text>
<g transform="translate(56 640) rotate(-1.5)" filter="url(#sh)"><rect width="1020" height="150" rx="22" fill="#08171C" stroke="#FFD43B" stroke-width="8"/>
<text x="510" y="100" font-size="80" fill="#FFD43B" text-anchor="middle" id="b1">LEGGE O PROPOSTA?</text></g>
<g filter="url(#sh)"><rect x="56" y="850" width="1020" height="130" rx="28" fill="#fff"/>
<text x="566" y="935" font-size="52" fill="#C0200F" text-anchor="middle" id="c1">LA VERITÀ <tspan fill="#0D5158">CHE NON TI DICONO</tspan></text></g>
<g transform="translate(1210 90) rotate(5)" filter="url(#sh)">
<rect width="620" height="880" rx="26" fill="#FBFDFD"/>
<rect width="620" height="120" rx="26" fill="#0D5158"/><rect y="90" width="620" height="30" fill="#0D5158"/>
<text x="310" y="82" font-size="56" fill="#FFD43B" text-anchor="middle" id="d1">MANOVRA 2027</text>
{lines}
<rect x="40" y="560" width="540" height="56" rx="8" fill="#FFE777"/>
<text x="310" y="602" font-size="40" fill="#08323A" text-anchor="middle" id="d2">USCITA A 64 ANNI</text>
<ellipse cx="310" cy="588" rx="282" ry="50" fill="none" stroke="#E0200F" stroke-width="10" transform="rotate(-2 310 588)"/>
<g transform="translate(430 780) rotate(-14)"><circle r="92" fill="#E0200F" stroke="#fff" stroke-width="10"/><text y="42" font-size="130" fill="#fff" text-anchor="middle">?</text></g>
</g>
<g transform="translate(1135 800) rotate(-9)" filter="url(#sh)"><rect width="230" height="230" rx="20" fill="#fff"/><rect width="230" height="66" rx="20" fill="#D8281A"/><rect y="38" width="230" height="28" fill="#D8281A"/><text x="115" y="50" font-size="36" fill="#fff" text-anchor="middle">ANNO</text><text x="115" y="176" font-size="72" fill="#0D5158" text-anchor="middle" id="y">2027</text></g>
</svg>'''
open('orizz2.html','w').write('<body style="margin:0">'+svg+'</body>')
