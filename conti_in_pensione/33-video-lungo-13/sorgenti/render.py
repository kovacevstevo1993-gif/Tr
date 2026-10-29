import sys,subprocess,os,json
from playwright.sync_api import sync_playwright
H=os.path.dirname(os.path.abspath(__file__))
# fotogrammi a 30 fps, fine blocco letta dalle timeline CapCut (DURATE.txt)
FR={int(k):v for k,v in json.load(open(os.path.join(H,"durate.json"))).items()}
b=int(sys.argv[1]);mode=sys.argv[2] if len(sys.argv)>2 else 'video'
subprocess.run(['python3',os.path.join(H,'build.py'),str(b)],check=True)
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox']);pg=br.new_page(viewport={'width':1920,'height':1080})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+H+'/blocco%02d.html'%b)
    if errs:print('ERRORE JS:',errs[:3]);sys.exit(1)
    if mode in ('video','check'):
        # ===== BLOCCO AUTOMATICO (regole N.15, N.18): se un controllo non passa, il render NON parte =====
        pg.evaluate('draw(0,0.1)');SC=pg.evaluate('window.__SC');IT=pg.evaluate('window.__IT')
        for (s0,e0),a_ in zip(SC,IT):
            L=e0-s0;a_=sorted(a_);last=a_[-1]+0.9
            gaps=[a_[i+1]-a_[i] for i in range(len(a_)-1)]
            if L<5.0 or last>0.8*L+0.02 or (L-last)<1.0 or (gaps and min(gaps)<0.44):
                print('ERRORE TEMPI: scena %.1f s, ultimo elemento completo a %.1f s (80%% = %.1f), distanza minima %.2f s: RENDER BLOCCATO'%(L,last,0.8*L,min(gaps) if gaps else 9));sys.exit(1)
        ov=pg.evaluate('window.__OVL()')
        if ov:
            for o in ov:print('ERRORE IMPAGINAZIONE:',o)
            print('RENDER BLOCCATO');sys.exit(1)
        if errs:print('ERRORE JS:',errs[:3]);sys.exit(1)
        q=subprocess.run(['python3',os.path.join(H,'..','..','qa','qa_slide.py'),os.path.join(H,'blocco%02d.html'%b),'0',str(FR[b])],capture_output=True,text=True)
        print(q.stdout.strip())
        if q.returncode!=0:
            print('ERRORE QA FOTOGRAMMI: RENDER BLOCCATO');sys.exit(1)
        print('CONTROLLI OK: tempi, impaginazione e fotogrammi')
    if mode=='check':
        br.close();sys.exit(0)
    if mode=='preview':
        os.makedirs(H+'/prev',exist_ok=True)
        for s in [float(x) for x in sys.argv[3:]]:
            pg.evaluate('draw(0,%f)'%s);pg.screenshot(path=H+'/prev/b%02d_t%05.2f.png'%(b,s))
    elif mode=='video':
        os.makedirs(H+'/../clip',exist_ok=True)
        ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','veryfast','-movflags','+faststart',H+'/../clip/CIP-V13-blocco%02d.mp4'%b],stdin=subprocess.PIPE)
        for f in range(FR[b]):
            pg.evaluate('draw(0,%f)'%(f/30));ff.stdin.write(pg.screenshot(type='jpeg',quality=94))
        ff.stdin.close();ff.wait()
    br.close()
