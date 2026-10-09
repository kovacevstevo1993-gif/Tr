import sys,os
from playwright.sync_api import sync_playwright
H=os.path.dirname(os.path.abspath(__file__))
b=int(sys.argv[1]);ts=[float(x) for x in sys.argv[2:]]
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']);pg=br.new_page(viewport={'width':1920,'height':1080})
    pg.on('pageerror',lambda e:print('ERR',e));pg.on('console',lambda m:print('LOG',m.text) if m.type=='warning' else None)
    pg.goto('file://'+H+'/blocco%02d.html'%b)
    sc=pg.evaluate('window.__SC')
    print('scene',[(round(a,2),round(c,2)) for a,c in sc])
    os.makedirs(H+'/prev',exist_ok=True)
    if not ts: ts=[c-0.7 for a,c in sc]
    for s in ts:
        pg.evaluate('draw(0,%f)'%s);pg.screenshot(path=H+'/prev/b%02d_t%05.2f.png'%(b,s))
    br.close()
