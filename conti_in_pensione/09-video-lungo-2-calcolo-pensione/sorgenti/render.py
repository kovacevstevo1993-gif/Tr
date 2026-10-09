import sys,subprocess,os
from playwright.sync_api import sync_playwright
H=os.path.dirname(os.path.abspath(__file__))
# fotogrammi a 30 fps letti dalle timeline CapCut
FR={1:424,2:341,3:352,4:328,5:305,6:401,7:262,8:310,9:369,10:305,11:405,12:346,13:428,14:381,15:448,16:329,17:369,18:397,19:399,20:341,21:429,22:330,23:464,24:334,25:340,26:460,27:404,28:346,29:458,30:428,31:358,32:370,33:364,34:416,35:334,36:330,37:380,38:404,39:416,40:422,41:424,42:358,43:392,44:406,45:410,46:288,47:392,48:466,49:340,50:334,51:404,52:372,53:376,54:436,55:298,56:251,57:215}
b=int(sys.argv[1]);mode=sys.argv[2] if len(sys.argv)>2 else 'video'
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']);pg=br.new_page(viewport={'width':1920,'height':1080})
    pg.on('pageerror',lambda e:print('ERR',e))
    pg.goto('file://'+H+'/blocco%d.html'%b)
    if mode=='preview':
        os.makedirs(H+'/prev',exist_ok=True)
        for s in [float(x) for x in sys.argv[3:]]:
            pg.evaluate('draw(0,%f)'%s);pg.screenshot(path=H+'/prev/b%d_t%05.2f.png'%(b,s))
    else:
        os.makedirs(H+'/out',exist_ok=True)
        ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','veryfast','-movflags','+faststart',H+'/out/blocco%d.mp4'%b],stdin=subprocess.PIPE)
        for f in range(FR[b]):
            pg.evaluate('draw(0,%f)'%(f/30));ff.stdin.write(pg.screenshot(type='jpeg',quality=94))
        ff.stdin.close();ff.wait()
    br.close()
