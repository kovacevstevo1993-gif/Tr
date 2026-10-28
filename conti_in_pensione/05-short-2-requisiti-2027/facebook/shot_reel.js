const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/reel.html');
await p.screenshot({path:'copertina-reel.png'});
const r=await p.evaluate(()=>[...document.querySelectorAll('text')].map(t=>{const b=t.getBBox();const m=t.getCTM();return [t.textContent.slice(0,16),Math.round(b.x),Math.round(b.y),Math.round(b.x+b.width),Math.round(b.y+b.height)]}));
r.forEach(x=>console.log(JSON.stringify(x)));await b.close()})();
