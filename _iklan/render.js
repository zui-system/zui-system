const {chromium}=require('playwright'),fs=require('fs'),path=require('path'),{execFileSync}=require('child_process');
const D=__dirname,O=path.join(D,'hasil'),SRC='file://'+path.join(D,'.iklan.html'),FPS=30;
const only=process.argv[2];
async function page(b,w,h){const p=await b.newPage({viewport:{width:w,height:h}});await p.goto(`${SRC}?w=${w}&h=${h}`);await p.evaluate(()=>document.fonts.ready);return p}
(async()=>{const b=await chromium.launch();
 if(!only||only==='gambar'){
  for(const [n,w,h] of [['feed-1080x1080',1080,1080],['portrait-1080x1350',1080,1350],['story-1080x1920',1080,1920],['landscape-1200x628',1200,628]]){
   const p=await page(b,w,h);await p.evaluate(()=>R.poster());await p.screenshot({path:`${O}/poster-${n}.png`});await p.close()}
  const p=await page(b,1080,1080);
  await p.evaluate(()=>R.render(4.6));await p.screenshot({path:`${O}/carousel-1-sampul.png`});
  for(let k=0;k<6;k++){await p.evaluate(k=>R.appCard(k),k);await p.screenshot({path:`${O}/carousel-${k+2}-aplikasi.png`})}
  await p.evaluate(()=>R.render(22));await p.screenshot({path:`${O}/carousel-8-penutup.png`});await p.close()}
 if(!only||only==='video'){
  for(const [n,w,h] of [['reels-tiktok-1080x1920',1080,1920],['feed-1080x1080',1080,1080]]){
   const p=await page(b,w,h),dur=await p.evaluate(()=>R.DUR),fr=path.join(D,'.frame');fs.rmSync(fr,{recursive:true,force:true});fs.mkdirSync(fr);
   for(let i=0;i<Math.round(dur*FPS);i++){await p.evaluate(t=>R.render(t),i/FPS);await p.screenshot({path:`${fr}/${String(i).padStart(5,'0')}.png`})}
   await p.close();
   execFileSync('ffmpeg',['-y','-loglevel','error','-framerate',''+FPS,'-i',`${fr}/%05d.png`,'-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','slow','-movflags','+faststart',`${O}/video-${n}.mp4`]);
   fs.rmSync(fr,{recursive:true,force:true})}}
 await b.close()})();
