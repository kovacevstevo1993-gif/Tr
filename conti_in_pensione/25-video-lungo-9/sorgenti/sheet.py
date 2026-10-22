import sys,os,json
from playwright.sync_api import sync_playwright
from PIL import Image
H=os.path.dirname(os.path.abspath(__file__));bl=[int(x) for x in sys.argv[1:]]
ims=[]
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']);pg=br.new_page(viewport={'width':1920,'height':1080})
    for b in bl:
        pg.goto('file://'+H+'/blocco%02d.html'%b);pg.evaluate('draw(0,0.1)');SC=pg.evaluate('window.__SC')
        for s,e in SC:
            pg.evaluate('draw(0,%f)'%(e-0.4));pg.screenshot(path='/tmp/_s9.png');ims.append(Image.open('/tmp/_s9.png').resize((960,540)))
    br.close()
W=Image.new('RGB',(1920,540*((len(ims)+1)//2)))
for i,im in enumerate(ims):W.paste(im,((i%2)*960,(i//2)*540))
os.makedirs(H+'/prev',exist_ok=True);W.save(H+'/prev/sheet_'+'_'.join(map(str,bl))+'.png')
