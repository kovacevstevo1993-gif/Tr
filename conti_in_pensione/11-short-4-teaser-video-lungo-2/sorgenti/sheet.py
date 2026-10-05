# anteprima: fotogrammi ogni 0,5 s di un blocco in un unico foglio
import sys,os
from playwright.sync_api import sync_playwright
D=[305,186,222,257,238,150]
here=os.path.dirname(os.path.abspath(__file__));blk=int(sys.argv[1])-1;out=sys.argv[2]
os.makedirs(out,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']);pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.on('pageerror',lambda e:print('ERR',e));pg.goto('file://'+here+'/index.html')
    f=0;k=0
    while f<D[blk]:
        pg.evaluate('draw(%d,%f)'%(blk,f/30));pg.screenshot(path=out+'/b%d_%03d.png'%(blk+1,k));k+=1;f+=15
    pg.evaluate('draw(%d,%f)'%(blk,(D[blk]-1)/30));pg.screenshot(path=out+'/b%d_%03d.png'%(blk+1,k))
