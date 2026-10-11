import sys,subprocess,os
from playwright.sync_api import sync_playwright
H=os.path.dirname(os.path.abspath(__file__))
# fotogrammi a 30 fps, fine blocco letta dalle timeline CapCut (DURATE.txt)
import json;FR={int(k):v for k,v in json.load(open(os.path.join(H,"durate.json"))).items()}
b=int(sys.argv[1]);mode=sys.argv[2] if len(sys.argv)>2 else 'video'
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']);pg=br.new_page(viewport={'width':1920,'height':1080})
    pg.on('pageerror',lambda e:print('ERR',e))
    pg.goto('file://'+H+'/blocco%02d.html'%b)
    if mode in ('video','check'):
        # ===== BLOCCO AUTOMATICO (regola N.18): se un controllo non passa, il render NON parte =====
        pg.evaluate('draw(0,0.1)');SC=pg.evaluate('window.__SC');IT=pg.evaluate('window.__IT')
        for (s0,e0),a_ in zip(SC,IT):
            L=e0-s0;a_=sorted(a_);last=a_[-1]+0.9
            if L<5.0 or last>0.8*L+0.02 or (L-last)<1.0:
                print('ERRORE TEMPI: scena %.1f s, ultimo elemento completo a %.1f s (80%% = %.1f): RENDER BLOCCATO'%(L,last,0.8*L));sys.exit(1)
        q=subprocess.run(['python3',os.path.join(H,'..','..','qa','qa_slide.py'),os.path.join(H,'blocco%02d.html'%b),'0',str(FR[b])],capture_output=True,text=True)
        print(q.stdout.strip())
        if q.returncode!=0:
            print('ERRORE QA FOTOGRAMMI: RENDER BLOCCATO');sys.exit(1)
        print('CONTROLLI OK: tempi e fotogrammi')
    if mode=='check':
        br.close();sys.exit(0)
    if mode=='preview':
        os.makedirs(H+'/prev',exist_ok=True)
        for s in [float(x) for x in sys.argv[3:]]:
            pg.evaluate('draw(0,%f)'%s);pg.screenshot(path=H+'/prev/b%02d_t%05.2f.png'%(b,s))
    else:
        os.makedirs(H+'/out',exist_ok=True)
        ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','veryfast','-movflags','+faststart',H+'/out/V5-blocco%02d.mp4'%b],stdin=subprocess.PIPE)
        for f in range(FR[b]):
            pg.evaluate('draw(0,%f)'%(f/30));ff.stdin.write(pg.screenshot(type='jpeg',quality=94))
        ff.stdin.close();ff.wait()
    br.close()
