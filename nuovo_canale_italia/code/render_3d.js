// Uso: node render_3d.js pagina.html cartella_out primo ultimo | lista_t   (serve la cartella nuovo_canale_italia con un mini server, WebGL software)
const { chromium } = require('playwright'); const http = require('http'), fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..');
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.ttf': 'font/ttf', '.png': 'image/png', '.json': 'application/json' };
(async () => {
  const [html, out, a, b] = process.argv.slice(2); const W = process.env.W || '1080', H = process.env.H || '1920';
  const srv = http.createServer((q, r) => { const f = path.join(ROOT, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'Content-Type': MIME[path.extname(f)] || 'application/octet-stream' }); r.end(d); } }); });
  await new Promise(r => srv.listen(0, r)); const port = srv.address().port; fs.mkdirSync(out, { recursive: true });
  const br = await chromium.launch({ args: ['--use-angle=swiftshader', '--use-gl=angle', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const pg = await br.newPage({ viewport: { width: +W, height: +H } });
  pg.on('pageerror', e => console.log('ERRORE PAGINA', String(e).slice(0, 300)));
  await pg.goto(`http://localhost:${port}/code/${path.basename(html)}`); await pg.waitForFunction('window.pronto === true', null, { timeout: 60000 }); await pg.waitForTimeout(300);
  let frames = [];
  if (b === undefined) frames = a.split(',').map(x => ({ n: 't' + x, t: +x })); else for (let f = +a; f <= +b; f++) frames.push({ n: String(f).padStart(5, '0'), t: f / 30 });
  const bad = [];
  for (const fr of frames) { await pg.evaluate(t => draw(t), fr.t); const bo = await pg.evaluate(() => bounds()); if (bo.length) bad.push([fr.n, JSON.stringify(bo)]); await pg.screenshot({ path: path.join(out, fr.n + '.png') }); }
  console.log(bad.length ? 'FUORI_LIMITI ' + bad.length + ' ' + bad.slice(0, 3).map(x => x.join(' ')).join(' | ') : 'limiti ok ' + frames.length + ' fotogrammi');
  await br.close(); srv.close();
})();
