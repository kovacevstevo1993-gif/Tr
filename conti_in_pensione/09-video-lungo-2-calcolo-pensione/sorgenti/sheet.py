import sys,os,subprocess
from playwright.sync_api import sync_playwright
# anteprima: un fotogramma ogni 0,5 s di un blocco -> fogli 4x3 (per guardare ogni slide prima del render)
H=os.path.dirname(os.path.abspath(__file__))
FR={1:424,2:341,3:352,4:328,5:305,6:401,7:262,8:310,9:369,10:305,11:405,12:346,13:428,14:381,15:448,16:329,17:369,18:397,19:399,20:341,21:429,22:330,23:464,24:334,25:340,26:460,27:404,28:346,29:458,30:428,31:358,32:370,33:364,34:416,35:334,36:330,37:380,38:404,39:416,40:422,41:424,42:358,43:392,44:406,45:410,46:288,47:392,48:466,49:340,50:334,51:404,52:372,53:376,54:436,55:298,56:251,57:215}
b=int(sys.argv[1]);os.makedirs(H+'/qa',exist_ok=True)
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']);pg=br.new_page(viewport={'width':1920,'height':1080})
    pg.on('pageerror',lambda e:print('ERR',e));pg.goto('file://'+H+'/blocco%d.html'%b)
    n=0;t=0.25
    while t<FR[b]/30:
        pg.evaluate('draw(0,%f)'%t);pg.screenshot(path=H+'/qa/f%03d.png'%n);n+=1;t+=0.5
    br.close()
subprocess.run('ffmpeg -y -loglevel error -framerate 1 -i %s/qa/f%%03d.png -vf "scale=480:-1,tile=4x3" %s/qa/sh%d_%%d.png'%(H,H,b),shell=True)
subprocess.run('rm -f %s/qa/f*.png'%H,shell=True)
