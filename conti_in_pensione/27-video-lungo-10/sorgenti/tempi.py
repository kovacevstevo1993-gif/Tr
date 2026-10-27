import sys,os,subprocess
from playwright.sync_api import sync_playwright
H=os.path.dirname(os.path.abspath(__file__))
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']);pg=br.new_page(viewport={'width':1920,'height':1080})
    for b in map(int,sys.argv[1:]):
        subprocess.run(['python3',os.path.join(H,'build.py'),str(b)],check=True)
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto('file://'+H+'/blocco%02d.html'%b)
        try:
            pg.evaluate('draw(0,0.1)');SC=pg.evaluate('window.__SC');IT=pg.evaluate('window.__IT')
            for (s,e),a in zip(SC,IT):
                a=sorted(a);L=e-s;print(b,'scena %.1f-%.1f (%.1f s) ultimo completo %.1f (80%%=%.1f) n=%d'%(s,e,L,a[-1]+0.9,0.8*L,len(a)),' '.join('%.1f'%x for x in a))
            ov=pg.evaluate('window.__OVL()')
            for o in ov:print(b,'IMPAGINAZIONE',o)
        except Exception as e: print(b,'ERR',e)
        if errs:print(b,errs[:3])
    br.close()
