// Uso: node render_short.js pagina.html cartella_out primo ultimo [fps=30]   (o: ... lista t1,t2,t3 per fotogrammi di prova)
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const [html, out, a, b, fpsArg] = process.argv.slice(2);
  const fps = +(fpsArg || 30); fs.mkdirSync(out, { recursive: true });
  const br = await chromium.launch();
  const pg = await br.newPage({ viewport: { width: 1080, height: 1920 } });
  await pg.goto('file://' + path.resolve(html)); await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(400);
  let frames = [];
  if (b === undefined) frames = a.split(',').map(x => ({ n: 't' + x, t: +x }));
  else for (let f = +a; f <= +b; f++) frames.push({ n: String(f).padStart(5, '0'), t: f / fps });
  const bad = [];
  for (const fr of frames) {
    await pg.evaluate(t => draw(t), fr.t);
    const bo = await pg.evaluate(() => bounds());
    if (bo.length) bad.push([fr.n, JSON.stringify(bo)]);
    await pg.screenshot({ path: path.join(out, fr.n + '.png') });
  }
  if (bad.length) { console.log('FUORI_LIMITI', bad.length, 'fotogrammi; primi:', bad.slice(0, 3).map(x => x.join(' ')).join(' | ')); }
  else console.log('limiti ok', frames.length, 'fotogrammi');
  await br.close();
})();
