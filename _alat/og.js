const {chromium}=require(process.env.PW);const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:630}});
for(const f of fs.readdirSync(__dirname).filter(x=>x.startsWith('og_')&&x.endsWith('.html'))){await p.goto('file://'+__dirname+'/'+f);await p.screenshot({path:require('path').resolve(__dirname,'..')+'/'+f.slice(3,-5)})}
await b.close()})();
