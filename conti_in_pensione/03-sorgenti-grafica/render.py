
import sys,subprocess,asyncio
from playwright.async_api import async_playwright
D=[150,103,192,115,162,175,162]
async def main(i):
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
        pg.on('pageerror',lambda e:print('ERR',e))
        await pg.goto('file://'+__file__.rsplit('/',1)[0]+'/index.html')
        ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','medium','-movflags','+faststart',__file__.rsplit('/',1)[0]+'/out/blocco%d.mp4'%(i+1)],stdin=subprocess.PIPE)
        for f in range(D[i]):
            await pg.evaluate('draw(%d,%f)'%(i,f/30))
            ff.stdin.write(await pg.screenshot(type='jpeg',quality=94))
        ff.stdin.close(); ff.wait(); await b.close()
asyncio.run(main(int(sys.argv[1])))
