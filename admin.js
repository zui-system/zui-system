/* Pusat pengaturan pemilik (Firebase). Buka: #pengaturan di alamat, atau ketuk logo 5x. Hanya email pemilik (di aturan Firebase) yang bisa menyimpan. */
(()=>{
const CFG={apiKey:"AIzaSyC5SzHo8hf-nJoJogI3thTJKiulxvdkZ3E",authDomain:"web-zuisystem.firebaseapp.com",projectId:"web-zuisystem",storageBucket:"web-zuisystem.firebasestorage.app",messagingSenderId:"507512716156",appId:"1:507512716156:web:b9806f4db7704ecfdd42f9"};
const B='https://www.gstatic.com/firebasejs/13.0.0/firebase-',KC='zui-cfg',imp=m=>import(B+m+'.js');
const q=s=>document.querySelector(s),qa=s=>[...document.querySelectorAll(s)],cl=o=>JSON.parse(JSON.stringify(o)),esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const F=[['h1','Judul utama'],['.hero p.l','Teks pengantar'],['#aplikasi h2','Judul Aplikasi'],['#aplikasi .sub','Keterangan Aplikasi'],['#cara h2','Judul Cara pakai'],['#cara .w>p.sub','Keterangan Cara pakai'],['#kontrol h2','Judul Kontrol'],['#harga h2','Judul Harga'],['#harga .sub','Keterangan Harga'],['#mulai h2','Judul Mulai'],['.fin h2','Judul penutup'],['.fin p','Teks penutup']];
const orig=F.map(([s])=>{const e=q(s);return e?e.textContent:''}),mail0=(q('a[href^="mailto:"]:not([data-tetap])')||{}).textContent||'';
const D0={apps:cl(APPS),paket:cl(PAKET),faq:qa('.fq details').map(d=>({q:d.querySelector('summary').textContent,a:d.querySelector('p').textContent}))};
const FT=[{n:'Bawaan'},{n:'Modern',sf:'Inter',sn:'Inter',g:'Inter:wght@400;500;600;700'},{n:'Elegan',sf:'"Playfair Display"',sn:'"IBM Plex Sans"',g:'Playfair+Display:wght@500;600;700'},{n:'Hangat',sf:'Poppins',sn:'Poppins',g:'Poppins:wght@400;500;600'}];
const TH=[['ac','Warna aksen (tombol, garis)','#135E78'],['bg','Warna latar','#F5F6F4'],['ink','Warna teks','#0E2230'],['nv','Warna bagian penutup','#0E2230']];
const SEC=[['cara','Cara pakai'],['kontrol','Kontrol'],['harga','Harga'],['tanya','Pertanyaan'],['galeri','Galeri']];
const base=document.createElement('style'),sty=document.createElement('style');
base.textContent='.gg{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px;margin-top:32px}.gg figure{margin:0;background:var(--pn);border:1px solid var(--ln)}.gg img,.gg video{display:block;width:100%;max-height:360px;object-fit:cover;background:#0F2A3D}.gg figcaption{padding:10px 14px;color:var(--mu);font-size:14.5px}'+
'#adm{position:fixed;top:0;right:0;bottom:0;width:min(440px,100vw);z-index:400;background:#fff;color:#0E2230;border-left:1px solid #D3D9DE;box-shadow:-24px 0 50px -24px rgba(0,0,0,.45);display:flex;flex-direction:column;font:14.5px/1.5 system-ui,sans-serif}#adm[hidden]{display:none}#adm *{box-sizing:border-box}'+
'#adm header{background:#0E2230;color:#E6ECF0;padding:14px 16px;display:flex;justify-content:space-between;align-items:center}#adm header b{font-size:16px}#adm nav{display:flex;overflow-x:auto;border-bottom:1px solid #D3D9DE;flex:none}#adm nav button{flex:none;border:0;border-bottom:3px solid transparent;background:none;padding:11px 13px;font:500 14px system-ui;color:#4B5B68;cursor:pointer}#adm nav button[aria-selected=true]{color:#0E2230;border-color:#135E78}'+
'#adm .bd{flex:1;overflow:auto;padding:6px 16px 20px}#adm footer{border-top:1px solid #D3D9DE;padding:12px 16px;display:flex;gap:10px;align-items:center;flex:none}#adm h4{margin:20px 0 4px;font-size:14px}#adm label{display:block;font-size:12.5px;color:#4B5B68;margin:11px 0 3px}#adm .ck{display:flex;gap:8px;align-items:center;font-size:14px;color:#0E2230;margin:7px 0}'+
'#adm input[type=text],#adm input[type=number],#adm textarea,#adm select{width:100%;font:14.5px system-ui;padding:8px 10px;border:1px solid #C3CBD2;border-radius:6px;background:#fff;color:#0E2230}#adm textarea{min-height:64px;resize:vertical}#adm input[type=color]{width:100%;height:38px;border:1px solid #C3CBD2;border-radius:6px;padding:2px;background:#fff}'+
'#adm .rw{border:1px solid #D3D9DE;border-radius:8px;padding:4px 12px 12px;margin-top:14px;background:#F7F9FA}#adm .r{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}#adm .ab{border:1px solid #9AA8B3;background:#fff;color:#0E2230;border-radius:6px;padding:7px 12px;font:500 13.5px system-ui;cursor:pointer}#adm .ab.p{background:#135E78;border-color:#135E78;color:#fff}#adm .ab.x{color:#B3261E;border-color:#E3B0AB}#adm .ab:disabled{opacity:.4;cursor:default}#adm table{width:100%;margin-top:8px;font-size:13px}#adm td,#adm th{padding:2px 4px;text-align:left}#adm th{color:#4B5B68;font-weight:500}'+
'#adm .st{font-size:13px;color:#B3261E;flex:1}#adm .st.ok{color:#2E7D5B}#adm .mi2{display:grid;grid-template-columns:64px 1fr;gap:10px;padding:10px 0;border-bottom:1px solid #D3D9DE}#adm .mi2 img,#adm .mi2 video{width:64px;height:52px;object-fit:cover;background:#0F2A3D}'+
'@media(max-width:700px){#adm{top:auto;height:72vh;width:100%;border-left:0;border-top:1px solid #D3D9DE}}';
document.head.append(base,sty);

/* Firebase dimuat saat dibutuhkan */
let FB,AU,SG;
const core=async()=>FB||(FB=await(async()=>{const[a,f]=await Promise.all([imp('app'),imp('firestore')]),app=a.initializeApp(CFG);return{app,f,db:f.getFirestore(app)}})());
const auth=async()=>AU||(AU=await(async()=>{const c=await core(),m=await imp('auth');return{m,a:m.getAuth(c.app)}})());
const stor=async()=>SG||(SG=await(async()=>{const c=await core(),m=await imp('storage');return{m,s:m.getStorage(c.app)}})());
const msg=e=>/permission|insufficient/i.test(e&&(e.code+e.message))?'Akun ini bukan pemilik, atau aturan Firebase belum dipasang.':(e&&e.message)||'Gagal.';

/* menerapkan konfigurasi ke halaman */
const HD=h=>Object.assign({cara:true},h);
const hyd=c=>({t:c.t||{},apps:cl(c.apps||D0.apps),paket:cl(c.paket||D0.paket),faq:cl(c.faq||D0.faq),tema:cl(c.tema||{}),hide:HD(cl(c.hide||{})),mail:c.mail||''});
function apply(c){const t=c.t||{},m=c.tema||{},h=HD(c.hide),ft=FT[+m.f||0];
F.forEach(([s],i)=>{const e=q(s);if(e)e.textContent=t[i]||orig[i]});
let css='';if(m.ac)css+=`:root{--ac:${m.ac};--acs:color-mix(in srgb,${m.ac} 12%,var(--pn))}`;
const lt=[m.bg&&`--bg:${m.bg}`,m.ink&&`--ink:${m.ink}`,m.nv&&`--nv:${m.nv}`].filter(Boolean).join(';');if(lt)css+=`@media(prefers-color-scheme:light){:root{${lt}}}`;
if(ft.g){let l=document.getElementById('zfn');if(!l){l=document.createElement('link');l.id='zfn';l.rel='stylesheet';document.head.appendChild(l)}l.href='https://fonts.googleapis.com/css2?family='+ft.g+'&display=swap';css+=`:root{--sf:${ft.sf},Georgia,serif;--sn:${ft.sn},system-ui,sans-serif}`}
const hs=SEC.filter(([k])=>h[k]).map(([k])=>`#${k},a[href="#${k}"]`).join(',');if(hs)css+=hs+'{display:none!important}';sty.textContent=css;
APPS.length=0;APPS.push(...(c.apps||D0.apps));rA();PAKET.length=0;PAKET.push(...(c.paket||D0.paket));rp();
const fq=q('.fq');if(fq)fq.innerHTML=(c.faq||D0.faq).map(x=>`<details><summary>${esc(x.q)}</summary><p>${esc(x.a)}</p></details>`).join('');
const ml=c.mail||mail0;qa('a[href^="mailto:"]:not([data-tetap])').forEach(a=>{a.href='mailto:'+ml;a.textContent=ml})}
let cfg={},draft=hyd({}),dirty=0,GAL=[];
const gc=()=>{try{return JSON.parse(localStorage.getItem(KC)||'{}')}catch(e){return{}}};
function render(){let s=document.getElementById('galeri');
if(!GAL.length){if(s)s.remove();return}
if(!s){s=document.createElement('section');s.id='galeri';(document.getElementById('kontrol')||document.body).before(s)}
s.innerHTML='<div class="w"><h2>Galeri</h2><div class="gg">'+GAL.map(m=>'<figure>'+(m.k==='v'?`<video src="${esc(m.url)}" controls playsinline preload="metadata"></video>`:`<img src="${esc(m.url)}" alt="${esc(m.c)}" loading="lazy">`)+(m.c?`<figcaption>${esc(m.c)}</figcaption>`:'')+'</figure>').join('')+'</div></div>'}
async function muat(){try{const c=await core(),f=c.f,d=await f.getDoc(f.doc(c.db,'situs','config'));
cfg=d.exists()?JSON.parse(d.data().j||'{}'):{};localStorage.setItem(KC,JSON.stringify(cfg));if(!dirty){apply(cfg);draft=hyd(cfg)}
const g=await f.getDocs(f.query(f.collection(c.db,'galeri'),f.orderBy('o')));GAL=g.docs.map(x=>({id:x.id,...x.data()}));render()}catch(e){console.warn('Zui:',e)}}

/* panel */
const P=document.createElement('div');P.id='adm';P.hidden=true;document.body.appendChild(P);
let tab='t';
const setP=(p,v)=>{const k=p.split('.');let o=draft;k.slice(0,-1).forEach(x=>o=o[x]);o[k.pop()]=v};
const TB=[['t','Tampilan'],['x','Teks'],['a','Aplikasi'],['h','Harga'],['f','Tanya jawab'],['m','Media'],['k','Akun']];
const I=(p,v,l,n)=>`<label>${l}</label><input ${n?'type="number" data-n="1"':'type="text"'} data-p="${p}" value="${esc(v)}">`,T=(p,v,l)=>`<label>${l}</label><textarea data-p="${p}">${esc(v)}</textarea>`;
const bt=(k,i,n)=>`<div class="r"><button class="ab" data-a="up:${k}:${i}" ${i?'':'disabled'}>↑</button><button class="ab" data-a="dn:${k}:${i}" ${i<n-1?'':'disabled'}>↓</button><button class="ab x" data-a="del:${k}:${i}">Hapus</button></div>`;
const V={
t:()=>'<h4>Warna</h4>'+TH.map(([k,l,d])=>`<label>${l}</label><input type="color" data-p="tema.${k}" value="${draft.tema[k]||d}">`).join('')+`<label>Gaya huruf</label><select data-p="tema.f">${FT.map((f,i)=>`<option value="${i}" ${(+draft.tema.f||0)===i?'selected':''}>${f.n}</option>`).join('')}</select><h4>Bagian yang ditampilkan</h4>`+SEC.map(([k,l])=>`<label class="ck"><input type="checkbox" data-p="hide.${k}" data-inv="1" ${draft.hide[k]?'':'checked'}> ${l}</label>`).join('')+'<div class="r"><button class="ab" data-a="rst:tema:0">Kembalikan warna dan huruf asli</button></div>',
x:()=>F.map(([s,l],i)=>T('t.'+i,draft.t[i]||orig[i],l)).join('')+I('mail',draft.mail||mail0,'Email kontak'),
a:()=>draft.apps.map((a,i)=>`<div class="rw"><b>${i+1}. ${esc(a.n)}</b>`+I(`apps.${i}.n`,a.n,'Nama')+T(`apps.${i}.d`,a.d,'Deskripsi')+I(`apps.${i}.url`,a.url,'Alamat aplikasi (kosong = tampil "Segera")')+bt('apps',i,draft.apps.length)+'</div>').join('')+'<div class="r"><button class="ab p" data-a="add:apps:0">+ Tambah aplikasi</button></div>',
h:()=>draft.paket.map((p,i)=>`<div class="rw"><b>${esc(p.n)}</b>`+I(`paket.${i}.n`,p.n,'Nama paket')+I(`paket.${i}.b`,p.b,'Jumlah bulan',1)+I(`paket.${i}.ft`,p.ft||'','Label unggulan (opsional)')+'<table><tr><th></th><th>Normal</th><th>Promo</th></tr>'+['IDR','MYR','USD'].map(c=>`<tr><td>${c}</td><td><input type="number" data-n="1" data-p="paket.${i}.N.${c}" value="${p.N[c]||0}"></td><td><input type="number" data-n="1" data-p="paket.${i}.P.${c}" value="${p.P[c]||0}"></td></tr>`).join('')+'</table>'+bt('paket',i,draft.paket.length)+'</div>').join('')+'<div class="r"><button class="ab p" data-a="add:paket:0">+ Tambah paket</button></div>',
f:()=>draft.faq.map((x,i)=>`<div class="rw">`+I(`faq.${i}.q`,x.q,'Pertanyaan')+T(`faq.${i}.a`,x.a,'Jawaban')+bt('faq',i,draft.faq.length)+'</div>').join('')+'<div class="r"><button class="ab p" data-a="add:faq:0">+ Tambah pertanyaan</button></div>',
m:()=>'<label>Pilih gambar atau video (boleh banyak)</label><input type="file" id="afl" accept="image/*,video/*" multiple><label>Keterangan (opsional)</label><input type="text" id="acp" placeholder="Contoh: Gudang baru"><div class="r"><button class="ab p" id="aad">Unggah ke galeri</button></div><h4>Isi galeri (langsung tampil di situs)</h4>'+(GAL.length?GAL.map((m,i)=>`<div class="mi2">${m.k==='v'?`<video src="${esc(m.url)}" muted preload="metadata"></video>`:`<img src="${esc(m.url)}" alt="">`}<div><input type="text" data-mc="${i}" value="${esc(m.c)}" placeholder="Keterangan"><div class="r"><button class="ab" data-a="mu:0:${i}" ${i?'':'disabled'}>↑</button><button class="ab" data-a="md:0:${i}" ${i<GAL.length-1?'':'disabled'}>↓</button><button class="ab x" data-a="mx:0:${i}">Hapus</button></div></div></div>`).join(''):'<p>Belum ada isi.</p>'),
k:()=>`<h4>Akun</h4><p>Masuk sebagai ${esc(AU&&AU.a.currentUser&&AU.a.currentUser.email)}</p><div class="r"><button class="ab" data-a="out:0:0">Keluar</button><button class="ab x" data-a="all:0:0">Kembalikan seluruh situs ke bawaan</button></div>`};
const say=(m,ok)=>{const e=q('#adm .st');if(e){e.textContent=m;e.className='st'+(ok?' ok':'')}};
function show(t){tab=t||tab;P.innerHTML=`<header><b>Pengaturan situs</b><button class="ab" data-a="cls:0:0">Tutup</button></header><nav>${TB.map(([k,l])=>`<button data-t="${k}" aria-selected="${k===tab}">${l}</button>`).join('')}</nav><div class="bd">${V[tab]()}</div><footer><span class="st"></span><button class="ab p" data-a="sav:0:0">Simpan semua</button></footer>`;
if(tab==='m')q('#aad').onclick=upload}
function login(er){P.innerHTML=`<header><b>Pengaturan situs</b><button class="ab" data-a="cls:0:0">Tutup</button></header><div class="bd"><p>Masuk dengan akun Google pemilik.</p><p class="st">${esc(er)}</p><div class="r"><button class="ab p" id="aok">Masuk dengan Google</button></div></div>`;
q('#aok').onclick=async()=>{try{const A=await auth();await A.m.signInWithPopup(A.a,new A.m.GoogleAuthProvider());show()}catch(e){login(e.code==='auth/unauthorized-domain'?'Domain ini belum ditambahkan di Firebase: Authentication > Settings > Authorized domains.':msg(e))}}}
async function upload(){const fs=[...q('#afl').files].filter(f=>/^(image|video)\//.test(f.type)),c=q('#acp').value.trim();if(!fs.length){say('Pilih gambar atau video dulu.');return}
try{const k0=await core(),s=await stor();let n=0;
for(const f of fs){n++;const id='m'+Date.now()+Math.random().toString(36).slice(2,6),p='galeri/'+id,r=s.m.ref(s.s,p),task=s.m.uploadBytesResumable(r,f,{contentType:f.type});
await new Promise((ok,no)=>task.on('state_changed',sn=>say(`Mengunggah ${n}/${fs.length}: ${Math.round(sn.bytesTransferred/sn.totalBytes*100)}%`,1),no,ok));
await k0.f.setDoc(k0.f.doc(k0.db,'galeri',id),{k:f.type.startsWith('video')?'v':'i',url:await s.m.getDownloadURL(r),p,c,o:Date.now()+n})}
await muat();show();say('Selesai diunggah.',1)}catch(e){say(msg(e))}}
async function saveAll(c){const k=await core();await k.f.setDoc(k.f.doc(k.db,'situs','config'),{j:JSON.stringify(c)});cfg=c;localStorage.setItem(KC,JSON.stringify(c));dirty=0}
P.addEventListener('input',e=>{const t=e.target,p=t.dataset.p;if(!p)return;let v=t.type==='checkbox'?(t.dataset.inv?!t.checked:t.checked):t.value;if(t.dataset.n)v=Math.max(0,Number(v)||0)||(/\.b$/.test(p)?1:0);setP(p,v);dirty=1;apply(draft)});
P.addEventListener('change',async e=>{const i=e.target.dataset.mc;if(i==null)return;try{const c=await core(),m=GAL[+i];await c.f.updateDoc(c.f.doc(c.db,'galeri',m.id),{c:e.target.value});m.c=e.target.value;render()}catch(x){say(msg(x))}});
P.addEventListener('click',async e=>{const tb=e.target.closest('[data-t]');if(tb)return show(tb.dataset.t);
const b=e.target.closest('[data-a]');if(!b)return;const[a,k,i]=b.dataset.a.split(':'),n=+i,arr=draft[k];
try{if(a==='cls'){if(dirty&&!confirm('Ada perubahan belum disimpan. Tutup dan batalkan?'))return;if(dirty){apply(cfg);draft=hyd(cfg);dirty=0}P.hidden=true;return}
if(a==='sav'){say('Menyimpan…',1);await saveAll(cl(draft));say('Tersimpan dan tampil untuk semua pengunjung.',1);return}
if(a==='add')arr.push(k==='apps'?{n:'Aplikasi baru',d:'',url:'',repo:''}:k==='faq'?{q:'Pertanyaan baru',a:''}:{n:'Paket baru',b:1,N:{IDR:0,MYR:0,USD:0},P:{IDR:0,MYR:0,USD:0}});
else if(a==='del'){if(!confirm('Hapus item ini?'))return;arr.splice(n,1)}
else if(a==='up'||a==='dn'){const j=a==='up'?n-1:n+1;[arr[n],arr[j]]=[arr[j],arr[n]]}
else if(a==='rst')draft.tema={};
else if(a==='out'){await AU.m.signOut(AU.a);P.hidden=true;return}
else if(a==='all'){if(!confirm('Semua teks, tampilan, aplikasi, harga, dan tanya jawab kembali ke bawaan. Galeri tidak terhapus. Lanjutkan?'))return;await saveAll({});draft=hyd({});apply(draft)}
else{const c=await core(),f=c.f,m=GAL[n],d=x=>f.doc(c.db,'galeri',x.id);
if(a==='mx'){if(!confirm('Hapus item ini?'))return;await f.deleteDoc(d(m));try{const s=await stor();await s.m.deleteObject(s.m.ref(s.s,m.p))}catch(x){}}
else{const o=GAL[a==='mu'?n-1:n+1];await f.updateDoc(d(m),{o:o.o});await f.updateDoc(d(o),{o:m.o})}
await muat();show();return}
if(a!=='rst'&&a!=='all')dirty=1;apply(draft);show()}catch(x){say(msg(x))}});
async function buka(){P.hidden=false;P.innerHTML='<header><b>Pengaturan situs</b></header><div class="bd"><p>Memuat…</p></div>';
try{const A=await auth();await A.a.authStateReady();A.a.currentUser?show():login('')}catch(e){login(msg(e))}}
const chk=()=>{if(location.hash==='#pengaturan'){history.replaceState(null,'',location.pathname+location.search);buka()}};
addEventListener('hashchange',chk);
let tp=[];qa('.top .lg').forEach(a=>a.addEventListener('click',e=>{const n=Date.now();tp=tp.filter(x=>n-x<3000);tp.push(n);if(tp.length>=5){tp=[];e.preventDefault();buka()}}));
cfg=gc();draft=hyd(cfg);apply(cfg);muat();chk();
})();
