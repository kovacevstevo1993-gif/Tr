import sys,subprocess,os
from playwright.sync_api import sync_playwright
D=[305,186,222,257,238,150]  # frame a 30 fps letti dalle 6 schermate CapCut (fine blocco, arrotondati per eccesso e sommati)
here=os.path.dirname(os.path.abspath(__file__))
def main(blocks,outdir):
    os.makedirs(outdir,exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']); pg=b.new_page(viewport={'width':1080,'height':1920})
        pg.on('pageerror',lambda e:print('ERR',e))
        pg.goto('file://'+here+'/index.html')
        for i in blocks:
            ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','medium','-movflags','+faststart',outdir+'/S4-blocco%02d.mp4'%(i+1)],stdin=subprocess.PIPE)
            for f in range(D[i]):
                pg.evaluate('draw(%d,%f)'%(i,f/30))
                ff.stdin.write(pg.screenshot(type='jpeg',quality=94))
            ff.stdin.close(); ff.wait()
        b.close()
main([int(a)-1 for a in sys.argv[2:]],sys.argv[1])
