import sys,os,subprocess
from playwright.sync_api import sync_playwright
H=os.path.dirname(os.path.abspath(__file__));os.makedirs(H+'/prev',exist_ok=True)
# uso: shot.py <blocco> t1 t2 ...  (salva prev/b%02d_t%05.2f.png a piena risoluzione)
b=int(sys.argv[1])
subprocess.run(['python3',os.path.join(H,'build.py'),str(b)],check=True)
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox']);pg=br.new_page(viewport={'width':1920,'height':1080})
    pg.goto('file://'+H+'/blocco%02d.html'%b)
    for s in [float(x) for x in sys.argv[2:]]:
        pg.evaluate('draw(0,%f)'%s);pg.screenshot(path=H+'/prev/b%02d_t%05.2f.png'%(b,s))
    br.close()
