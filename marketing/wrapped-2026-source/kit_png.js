const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const KIT = process.argv[2], FONTS = process.argv[3];
(async () => {
  const b = await chromium.launch();
  const svgDir = path.join(KIT, 'assets/svg');
  // stickers from SVG
  let p = await b.newPage({ viewport: { width: 2048, height: 2048 }, deviceScaleFactor: 2 });
  for (const f of fs.readdirSync(svgDir).filter(f => f.endsWith('.svg'))) {
    const inner = fs.readFileSync(path.join(svgDir, f), 'utf8').replace(/<svg[^>]*>/, '').replace('</svg>', '');
    const name = f.replace('.svg', '');
    for (const [dir, vb, filt] of [['sans-contour', '-4 -4 108 108', ''], ['autocollant', '-10 -10 120 120', 'filter="url(#stk)"']]) {
      await p.setContent(`<html><body style="margin:0;background:transparent"><svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}" width="2048" height="2048"><defs><filter id="stk" x="-30%" y="-30%" width="160%" height="160%"><feMorphology in="SourceAlpha" operator="dilate" radius="5" result="d"/><feFlood flood-color="#FFFDF8"/><feComposite in2="d" operator="in" result="o"/><feMerge><feMergeNode in="o"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><g ${filt}>${inner}</g></svg></body></html>`);
      await p.screenshot({ path: path.join(KIT, 'assets/png', dir, name + '.png'), omitBackground: true });
    }
  }
  await p.close();
  // chips + rank badges (HTML, fonts as in the video)
  p = await b.newPage({ viewport: { width: 900, height: 400 }, deviceScaleFactor: 4 });
  const chips = [['bilan-2026','sage','BILAN 2026'],['credit-impot-50','brown',"CRÉDIT D'IMPÔT -50 %"],['record','sage','RECORD'],['22-juin-creation-appli','sage',"22 JUIN<br>CRÉATION DE L'APPLI"],
    ['plus-71-vs-septembre','sage','+71 % VS SEPTEMBRE'],['n1-des-ventes-2026','brown','N°1 DES VENTES EN 2026'],['en-cabinet-ou-en-visio','brown','EN CABINET<br>OU EN VISIO'],
    ['du-22-juin-a-fin-octobre','sage','DU 22 JUIN À FIN OCTOBRE 2026'],['octobre-au-top','brown','OCTOBRE AU TOP'],['app-nous-fr','sage','APP-NOUS.FR'],['credit-impot-50-blanc','white',"CRÉDIT D'IMPÔT -50 %"]];
  const css = `@font-face{font-family:Nunito;font-weight:900;src:url(data:font/ttf;base64,${fs.readFileSync(FONTS + '/Nunito-Black.ttf').toString('base64')})}
  body{margin:0;background:transparent;padding:20px 20px 30px}
  .chip{display:inline-block;font-family:Nunito;font-weight:900;letter-spacing:.08em;font-size:40px;line-height:1.2;text-align:center;color:#4A2A21;padding:16px 34px;border-radius:999px;border:4px solid #4A2A21;box-shadow:0 10px 0 #4A2A21}
  .sage{background:#CFDAC2}.brown{background:#D7B596}.white{background:#FFFDF8}
  .n{width:120px;height:120px;border-radius:50%;background:#4A2A21;color:#F7F0E5;font-family:Nunito;font-weight:900;font-size:68px;display:flex;align-items:center;justify-content:center}`;
  for (const [n, c, t] of chips) {
    await p.setContent(`<html><head><style>${css}</style></head><body><span class="chip ${c}">${t}</span></body></html>`);
    await p.evaluate(() => document.fonts.ready);
    const el = await p.$('body');
    const box = await p.$eval('.chip', e => { const r = e.getBoundingClientRect(); return { x: 0, y: 0, width: r.right + 20, height: r.bottom + 30 }; });
    await p.screenshot({ path: path.join(KIT, 'assets/png/pastilles', 'pastille-' + n + '.png'), omitBackground: true, clip: box });
  }
  await p.close(); p = await b.newPage({ viewport: { width: 300, height: 300 }, deviceScaleFactor: 8 });
  for (let i = 1; i <= 4; i++) {
    await p.setContent(`<html><head><style>${css}</style></head><body><div class="n">${i}</div></body></html>`);
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(KIT, 'assets/png/pastilles', `numero-${i}.png`), omitBackground: true, clip: { x: 0, y: 0, width: 160, height: 170 }, scale: 'device' });
  }
  await b.close();
})();
