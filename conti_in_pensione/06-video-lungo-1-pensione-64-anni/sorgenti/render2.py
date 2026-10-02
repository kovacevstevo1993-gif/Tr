import sys,subprocess,asyncio,os
from playwright.async_api import async_playwright
H=os.path.dirname(os.path.abspath(__file__))
D={2:17.47,3:18.67,4:19.43,5:10.17}
async def main(b,mode):
    frames=round(D[b]*30)
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']);pg=await br.new_page(viewport={'width':1920,'height':1080})
        pg.on('pageerror',lambda e:print('ERR',e))
        await pg.goto('file://'+H+'/blocchi.html')
        if mode=='preview':
            os.makedirs(H+'/prev',exist_ok=True)
            n=0
            for s in [x*0.5 for x in range(1,int(D[b]*2))]:
                if int(s*30)>=frames: continue
                await pg.evaluate('draw(%d,%f)'%(b,s));await pg.screenshot(path=H+'/prev/b%d_%05.2f.png'%(b,s))
        else:
            os.makedirs(H+'/out',exist_ok=True)
            ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','medium','-movflags','+faststart',H+'/out/blocco%d.mp4'%b],stdin=subprocess.PIPE)
            for f in range(frames):
                await pg.evaluate('draw(%d,%f)'%(b,f/30));ff.stdin.write(await pg.screenshot(type='jpeg',quality=94))
            ff.stdin.close();ff.wait()
        await br.close()
asyncio.run(main(int(sys.argv[1]),sys.argv[2] if len(sys.argv)>2 else 'video'))
