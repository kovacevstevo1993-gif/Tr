import sys,subprocess,asyncio,os
from playwright.async_api import async_playwright
D=[139,298,162,246,108,185,192,143]
H=os.path.dirname(os.path.abspath(__file__))
async def main(i,mode):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']); pg=await b.new_page(viewport={'width':1080,'height':1920})
        pg.on('pageerror',lambda e:print('ERR',e))
        pg.on('console',lambda m:print('LOG',m.text) if m.type=='error' else None)
        await pg.goto('file://'+H+'/index.html')
        if mode=='preview':
            os.makedirs(H+'/prev',exist_ok=True)
            for s in [0.4,1.2,2.4,3.6,4.4,5.4,6.4,7.4,8.6,9.6]:
                f=int(s*30)
                if f>=D[i]: continue
                await pg.evaluate('draw(%d,%f)'%(i,f/30))
                await pg.screenshot(path=H+'/prev/s%d_%04.1f.png'%(i+1,s))
        else:
            os.makedirs(H+'/out',exist_ok=True)
            ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','medium','-movflags','+faststart',H+'/out/blocco%d.mp4'%(i+1)],stdin=subprocess.PIPE)
            for f in range(D[i]):
                await pg.evaluate('draw(%d,%f)'%(i,f/30))
                ff.stdin.write(await pg.screenshot(type='jpeg',quality=94))
            ff.stdin.close(); ff.wait()
        await b.close()
asyncio.run(main(int(sys.argv[1])-1,sys.argv[2] if len(sys.argv)>2 else 'video'))
