import asyncio,os,re
from playwright.async_api import async_playwright
src=open('vecchie-45cent/gen.py').read()
HEAD=re.search(r"HEAD='''(.*?)'''",src,re.S).group(1)
def T(x,y,s,fs,fill,sx=0.78,anc='start',sw=14,stroke='#06282C'):
    # testo stretto (condensed) con contorno
    return f'<g transform="translate({x} {y}) scale({sx} 1)"><text class="t" x="0" y="0" font-size="{fs}" fill="{fill}" text-anchor="{anc}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" paint-order="stroke">{s}</text></g>'
def STRIP(x,y,w,h,fill,rot=0):
    return f'<g transform="rotate({rot} {x+w/2} {y+h/2})" filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}"/></g>'
def DOC(x,y,w,h,rows,rot=0):
    g=f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#sh)"><rect width="{w}" height="{h}" rx="14" fill="url(#pp)" stroke="#fff" stroke-width="5"/>'
    g+=f'<rect width="{w}" height="64" rx="14" fill="#1B6FB5"/><rect y="40" width="{w}" height="24" fill="#1B6FB5"/><text x="20" y="45" class="t" font-size="38" fill="#fff">INPS</text><text x="{w-20}" y="44" class="t" font-size="26" fill="#fff" text-anchor="end">PENSIONI 2026</text>'
    for i,(a,b,hl) in enumerate(rows):
        yy=110+i*62
        if hl: g+=f'<rect x="10" y="{yy-40}" width="{w-20}" height="56" rx="10" fill="#FFF3A8"/>'
        g+=f'<text x="22" y="{yy}" class="t" font-size="30" fill="#0B4A50">{a}</text><text x="{w-22}" y="{yy}" class="t" font-size="34" fill="{"#C0200F" if hl else "#0B4A50"}" text-anchor="end">{b}</text>'
    g+=f'<ellipse cx="{w-105}" cy="96" rx="100" ry="36" fill="none" stroke="#E0201A" stroke-width="8"/>'
    return g+'</g>'
def ARROW(x1,y1,x2,y2):
    return f'<g filter="url(#sh)"><path d="M{x1} {y1} H{x2-40} V{y1-40} L{x2} {y1} L{x2-40} {y1+40} V{y1} Z" fill="#E0201A" stroke="#fff" stroke-width="5" stroke-linejoin="round"/></g>'
END='</svg></body></html>'
# A: INVALIDITA' 2027 / QUANTO AUMENTA? / documento con importi cerchiati
A=HEAD+STRIP(0,0,1280,150,'#2B2D8C')+T(30,122,"INVALIDITÀ",128,'#fff',0.8)+T(700,122,"2027",128,'#FFD43B',0.8)
A+=STRIP(20,190,640,120,'#FFE600',-2)+T(50,288,"QUANTO",112,'#0B0B0B',0.78,sw=0)
A+=T(30,450,"AUMENTA",135,'#fff',0.78)+T(30,585,"DAVVERO?",125,'#FF5A43',0.78)
A+=DOC(730,190,520,440,[("Pensione inabilità","340,71€",1),("Assegno mensile","340,71€",0),("Accompagnamento","552,57€",0),("Limite reddito","20.029€",0),("Età massima","67 anni",0)],4)
A+=STRIP(20,630,660,70,'#fff')+T(40,684,"NUMERI UFFICIALI INPS",52,'#C0200F',0.8,sw=0)+END
# B: COSA NON TI DICONO + 3 trappole
B=HEAD+STRIP(0,0,1280,125,'#2B2D8C')+T(30,100,"INVALIDI 2027:",104,'#fff',0.8)
B+=STRIP(20,150,1010,120,'#FFE600',-1)+T(45,245,"COSA NON TI DICONO",100,'#0B0B0B',0.78,sw=0)
rows=[("1","ACCOMPAGNAMENTO","ALTRO INDICE"),("2","LIMITI DI REDDITO","PUOI PERDERLA"),("3","67 ANNI","CAMBIA TUTTO")]
for i,(n,a,b) in enumerate(rows):
    y=310+i*130
    B+=f'<g filter="url(#sh)"><rect x="30" y="{y}" width="1220" height="110" rx="16" fill="#fff"/><rect x="30" y="{y}" width="130" height="110" rx="16" fill="#E0402A"/></g>'
    B+=T(95,y+88,n,100,'#fff',0.9,'middle',sw=0)+T(185,y+55,a,50,'#0B4A50',0.8,sw=0)+T(185,y+98,b,42,'#C0200F',0.8,sw=0)
    B+=f'<circle cx="1180" cy="{y+55}" r="38" fill="#FFD43B" stroke="#fff" stroke-width="5"/>'+T(1180,y+75,"!",64,'#8A1F10',1,'middle',sw=0)
B+=END
# C: importi grandi con freccia rossa (340,71 -> ~351) + accompagnamento
C=HEAD+STRIP(0,0,1280,150,'#2B2D8C')+T(30,122,"INVALIDITÀ",128,'#fff',0.8)+T(700,122,"2027",128,'#FFD43B',0.8)
C+=STRIP(20,180,1240,110,'#FFE600',-1)+T(50,272,"NUOVI IMPORTI: IL CONTO VERO",84,'#0B0B0B',0.78,sw=0)
C+='<g filter="url(#sh)"><rect x="30" y="330" width="560" height="270" rx="26" fill="url(#pp)" stroke="#fff" stroke-width="6"/><rect x="690" y="330" width="560" height="270" rx="26" fill="url(#pp)" stroke="#fff" stroke-width="6"/></g>'
C+=T(310,395,"OGGI (2026)",52,'#0B4A50',0.85,'middle',sw=0)+T(310,520,"340,71€",132,'#0B4A50',0.78,'middle',sw=0)+T(310,580,"al mese",44,'#1B9F81',0.85,'middle',sw=0)
C+=T(970,395,"CON IL 3%",52,'#C0200F',0.85,'middle',sw=0)+T(970,520,"≈ 351€",132,'#1B9F81',0.78,'middle',sw=0)+T(970,580,"esempio, non ufficiale",44,'#0B4A50',0.85,'middle',sw=0)
C+=ARROW(595,465,685,465)
C+=STRIP(20,630,1240,72,'#fff')+T(640,686,"MA L'ACCOMPAGNAMENTO NON SEGUE IL 3%!",58,'#C0200F',0.8,'middle',sw=0)+END
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg=await b.new_page(viewport={'width':1280,'height':720})
        for n,h in (('A',A),('B',B),('C',C)):
            open(f'miniatura-{n}.html','w').write(h)
            await pg.goto(f'file://{os.getcwd()}/miniatura-{n}.html'); await pg.screenshot(path=f'miniatura-{n}.png')
        await b.close()
asyncio.run(main())
