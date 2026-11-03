const {chromium}=require('playwright');
const base='https://www.facebook.com/people/Conti-In-Pensione-A-Pillole/61572856361386/';
(async()=>{const b=await chromium.launch();const c=await b.newContext({locale:'it-IT',viewport:{width:1280,height:2000},userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'});
const p=await c.newPage();
await p.goto(base+'?sk=reels_tab',{waitUntil:'domcontentloaded',timeout:40000});await p.waitForTimeout(4000);
for(let i=0;i<10;i++){await p.mouse.wheel(0,2500);await p.waitForTimeout(1500);}
const links=await p.evaluate(()=>[...new Set([...document.querySelectorAll('a[href*="/reel/"],a[href*="/videos/"],a[href*="/posts/"]')].map(a=>a.href.split('?')[0]))]);
console.log(links.length);
const out=[];
for(const l of links){const q=await c.newPage();try{await q.goto(l,{waitUntil:'domcontentloaded',timeout:30000});await q.waitForTimeout(3500);
const t=await q.evaluate(()=>document.body.innerText);
const m=t.split('\n').filter(x=>x.trim()).slice(0,40).join(' | ');
console.log(l,'\n  ',m.slice(0,500));}catch(e){console.log(l,'ERR')}await q.close();}
await b.close()})();
