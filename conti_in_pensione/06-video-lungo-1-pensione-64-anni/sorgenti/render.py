import sys,subprocess,asyncio,os
from playwright.async_api import async_playwright
H=os.path.dirname(os.path.abspath(__file__))
async def main(name,frames,mode):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']);pg=await b.new_page(viewport={'width':1920,'height':1080})
        pg.on('pageerror',lambda e:print('ERR',e))
        await pg.goto('file://'+H+'/'+name+'.html')
        if mode=='preview':
            os.makedirs(H+'/prev',exist_ok=True)
            for s in [0.5,1.3,2.4,3.0,3.8,4.6,5.6,6.8,8.0,9.5,10.5,11.9,13.0,14.0,15.2,16.0,17.2,18.2]:
                if int(s*30)>=frames: continue
                await pg.evaluate('draw(0,%f)'%s);await pg.screenshot(path=H+'/prev/%s_%05.2f.png'%(name,s))
        else:
            os.makedirs(H+'/out',exist_ok=True)
            ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','medium','-movflags','+faststart',H+'/out/%s.mp4'%name],stdin=subprocess.PIPE)
            for f in range(frames):
                await pg.evaluate('draw(0,%f)'%(f/30));ff.stdin.write(await pg.screenshot(type='jpeg',quality=94))
            ff.stdin.close();ff.wait()
        await b.close()
asyncio.run(main(sys.argv[1],int(sys.argv[2]),sys.argv[3] if len(sys.argv)>3 else 'video'))
