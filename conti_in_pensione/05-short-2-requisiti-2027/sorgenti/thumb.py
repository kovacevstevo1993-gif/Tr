import asyncio,os
from playwright.async_api import async_playwright
H=os.path.dirname(os.path.abspath(__file__))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']);pg=await b.new_page(viewport={'width':1080,'height':1920})
        pg.on('pageerror',lambda e:print('ERR',e))
        await pg.goto('file://'+H+'/thumb.html');await pg.screenshot(path=H+'/../miniature/miniatura-short2.png');await b.close()
asyncio.run(main())
