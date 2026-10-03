import sys,subprocess,os
from playwright.sync_api import sync_playwright
H=os.path.dirname(os.path.abspath(__file__))
FR=424  # 14,13 s a 30 fps, letti dalla timeline CapCut
mode=sys.argv[1] if len(sys.argv)>1 else 'video'
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']);pg=br.new_page(viewport={'width':1920,'height':1080})
    pg.on('pageerror',lambda e:print('ERR',e))
    pg.goto('file://'+H+'/blocco1.html')
    if mode=='preview':
        os.makedirs(H+'/prev',exist_ok=True)
        for s in [float(x) for x in sys.argv[2:]]:
            pg.evaluate('draw(0,%f)'%s);pg.screenshot(path=H+'/prev/t%05.2f.png'%s)
    else:
        os.makedirs(H+'/out',exist_ok=True)
        ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','medium','-movflags','+faststart',H+'/out/blocco1.mp4'],stdin=subprocess.PIPE)
        for f in range(FR):
            pg.evaluate('draw(0,%f)'%(f/30));ff.stdin.write(pg.screenshot(type='jpeg',quality=94))
        ff.stdin.close();ff.wait()
    br.close()
