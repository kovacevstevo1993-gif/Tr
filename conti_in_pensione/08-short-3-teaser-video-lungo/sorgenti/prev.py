from playwright.sync_api import sync_playwright
import os,sys
here=os.path.dirname(os.path.abspath(__file__))
T=[5.5,5.8,6.5,10.5,3.8,7.8,4.5] if len(sys.argv)<2 else [float(x) for x in sys.argv[1:]]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.on('pageerror',lambda e:print('ERR',e))
    pg.goto('file://'+here+'/index.html'); os.makedirs(here+'/prev',exist_ok=True)
    for i,t in enumerate(T):
        pg.evaluate('draw(%d,%f)'%(i,t)); pg.screenshot(path=here+'/prev/p%d.png'%(i+1))
    b.close()
