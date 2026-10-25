const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
(async () => {
  const mode = process.argv[2] || 'preview';
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.resolve('index.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(500);
  if (mode === 'preview') {
    const ts = process.argv.slice(3).map(Number);
    for (const t of ts) { await p.evaluate(t => render(t), t); await p.screenshot({ path: `prev_${t}.png` }); }
  } else {
    const fps = 30, dur = await p.evaluate(() => DURATION);
    const ff = spawn('ffmpeg', ['-y','-f','image2pipe','-framerate',String(fps),'-i','-','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart','out.mp4'], { stdio: ['pipe','ignore','inherit'] });
    for (let i = 0; i < dur * fps; i++) {
      await p.evaluate(t => render(t), i / fps);
      const buf = await p.screenshot({ type: 'jpeg', quality: 95 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    }
    ff.stdin.end(); await new Promise(r => ff.on('close', r));
  }
  await b.close();
})();
