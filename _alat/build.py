import os,re,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
from articles import ART
from general import GEN
GEN_BY_APP={v['app']:k for k,v in GEN.items()}
import legal as L

SCR=os.path.dirname(os.path.abspath(__file__))
ERP_BODY=open(os.path.join(SCR,'erp_body.html'),encoding='utf-8').read()

def ti(a,cls='ti'):return f'<span class="{cls}" style="--c:{a["c"]}">{ic(a["i"])}</span>'
GEN_I='<path d="M5 4h14v16H5zM8 8h8M8 12h8M8 16h5"/>'



def img_size(p):
    """Ukuran gambar (lebar, tinggi) tanpa pustaka tambahan; None bila tidak terbaca."""
    import struct
    try:
        with open(p,'rb') as f:d=f.read(65536)
        if d[:8]==b'\x89PNG\r\n\x1a\n':return struct.unpack('>II',d[16:24])
        if d[:4]==b'RIFF' and d[8:12]==b'WEBP':
            if d[12:16]==b'VP8X':return (int.from_bytes(d[24:27],'little')+1,int.from_bytes(d[27:30],'little')+1)
            if d[12:16]==b'VP8 ':return (struct.unpack('<H',d[26:28])[0]&0x3fff,struct.unpack('<H',d[28:30])[0]&0x3fff)
            if d[12:16]==b'VP8L':v=int.from_bytes(d[21:25],'little');return ((v&0x3fff)+1,((v>>14)&0x3fff)+1)
        if d[:2]==b'\xff\xd8':
            i=2
            while i<len(d)-9:
                if d[i]!=0xFF:i+=1;continue
                m=d[i+1]
                if m in (0xC0,0xC1,0xC2):h,w=struct.unpack('>HH',d[i+5:i+9]);return (w,h)
                i+=2+struct.unpack('>H',d[i+2:i+4])[0]
    except Exception:pass
    return None
def is_pc(p):
    s=img_size(p);return True if not s else s[0]>=s[1]
def find_video(slug,app_name):
    """Video panduan tampil otomatis bila ada video/<slug>.mp4 (atau .webm). Data opsional di video/<slug>.json."""
    import json as _j
    mp4=os.path.exists(os.path.join(OUT,'video',slug+'.mp4'));webm=os.path.exists(os.path.join(OUT,'video',slug+'.webm'))
    if not(mp4 or webm):return None
    meta={}
    p=os.path.join(OUT,'video',slug+'.json')
    if os.path.exists(p):meta=_j.load(open(p,encoding='utf-8'))
    return dict(slug=slug,mp4=mp4,webm=webm,poster=os.path.exists(os.path.join(OUT,'video',slug+'.jpg')),
        judul=meta.get('judul','Cara pakai '+app_name),ket=meta.get('keterangan','Video singkat cara memakai '+app_name+'.'),
        durasi=meta.get('durasi'),tanggal=meta.get('tanggal',DATE),pc=meta.get('orientasi','pc')!='hp')
# kartu panduan (dipakai di beranda, blog, dan bagian terkait)
ERP_ART=dict(pg='apa-itu-erp.html',n='Apa Itu ERP? Panduan untuk Pemilik Usaha',d='Pengertian ERP, modul yang umum, tanda usaha Anda membutuhkannya, dan cara memilih.')
def card(key):
    if key in GEN:
        g=GEN[key];a=A[g['app']]
        return f'<li><a href="{key}">{ti(a)}<span><b>{g["h1"][0].upper()+g["h1"][1:]}</b><small>{g["card"]}</small><em>Baca artikel ›</em></span></a></li>'
    if key=='erp-art':
        return f'<li><a href="{ERP_ART["pg"]}"><span class="ti gen">{ic(GEN_I)}</span><span><b>{ERP_ART["n"]}</b><small>{ERP_ART["d"]}</small><em>Baca artikel ›</em></span></a></li>'
    a=A[key];t=ART[key]
    return f'<li><a href="{a["pg"]}">{ti(a)}<span><b>Panduan {a["n"]}</b><small>{t["lede"].split(". ")[0].rstrip(".")}.</small><em>Baca panduan ›</em></span></a></li>'

# ---------- beranda ----------
tiles=''.join(f'<li><a href="{a["url"]}" target="_blank" rel="noopener" style="--c:{a["c"]}" aria-label="Buka {a["n"]} di tab baru">{ti(a)}<b>{a["n"]}</b><span>{a["d"]}</span><em>Buka ↗</em></a></li>' for a in APPS)
guides=''.join(card(a['k']) for a in APPS)
home=f'''<div class="w hero"><p class="ey">Zui System</p><h1>Aplikasi untuk <span class="gr">usaha, proyek, dan belajar</span></h1><p>Enam aplikasi yang masing-masing berdiri sendiri. Pilih yang Anda perlukan, lalu buka langsung di tab baru.</p><div class="cta"><a class="b" href="#apl">Jelajahi aplikasi</a></div></div>
<section class="sec" id="apl"><div class="w"><h2>Aplikasi Kami</h2><p class="sub">Setiap aplikasi punya akun dan datanya sendiri. Ketuk untuk membuka di tab baru.</p><ul class="bn">{tiles}</ul></div></section>
<section class="sec" id="kenapa"><div class="w"><h2>Kenapa Zui System</h2><p class="sub">Hal-hal yang membuatnya mudah dipakai.</p><div class="st"><div><b>6</b><span>aplikasi pilihan</span></div><div><b>Mandiri</b><span>akun dan data tiap aplikasi terpisah</span></div><div><b>HP</b><span>bisa dipasang di layar utama</span></div><div><b>1 ketuk</b><span>langsung terbuka di tab baru</span></div></div></div></section>
<section class="sec" id="panduan"><div class="w"><h2>Panduan aplikasi</h2><p class="sub">Kenali fungsi tiap aplikasi sebelum mencoba.</p><ul class="pg">{guides}</ul><a class="more" href="blog.html">Lihat semua tulisan di Blog ›</a>
</div></section>
<section class="sec" id="pasang"><div class="w"><h2>Pasang di layar utama HP</h2><p class="sub">Aplikasi Zui dibuka dari peramban dan bisa ditambahkan ke layar utama, tanpa toko aplikasi.</p>
<ol class="ps"><li><b>Android</b><span>Buka aplikasinya di Chrome, ketuk menu ⋮, lalu pilih <i>Instal aplikasi</i> atau <i>Tambahkan ke layar utama</i>.</span></li>
<li><b>iPhone dan iPad</b><span>Buka aplikasinya di Safari, ketuk tombol Bagikan, lalu pilih <i>Tambahkan ke Layar Utama</i>.</span></li>
<li><b>Komputer</b><span>Di Chrome atau Edge, klik ikon pasang di ujung kolom alamat bila tersedia, atau simpan sebagai bookmark.</span></li></ol></div></section>'''
page('index.html','Zui System: Aplikasi untuk Usaha, Proyek, dan Belajar',
 'Kumpulan aplikasi Zui System: Zui ERP, Zui Kontraktor, Zui Finance, Zui Jurnal, Zui To-Do, dan Studi Kita. Setiap aplikasi berdiri sendiri dan bisa dipasang di HP.',
 home,'',ld=[{"@type":"WebSite","@id":SITE+"#web","url":SITE,"name":"Zui System","inLanguage":"id","publisher":{"@id":SITE+"#org"}},
 {"@type":"ItemList","name":"Aplikasi Zui System","itemListElement":[{"@type":"ListItem","position":i+1,"item":{"@type":"SoftwareApplication","name":a["n"],"url":a["url"],"applicationCategory":"BusinessApplication" if a["g"]=="Usaha" else ("EducationalApplication" if a["g"]=="Pelajar" else "LifestyleApplication"),"operatingSystem":"Web, Android, iOS","description":a["d"],"publisher":{"@id":SITE+"#org"}}} for i,a in enumerate(APPS)]}])

# ---------- panduan per aplikasi ----------
def faq_html(fq):return '<div class="fq">'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in fq)+'</div>'
def article_page(path,title_seo,h1,desc,lede,sections,faq,rel,app=None,video=None,og='og-image.png',eyebrow='',kw='',section_name='Panduan',app_ld=True):
    toc=''.join(f'<a href="#{i}">{l}</a>' for i,l,_ in sections)+('<a href="#faq">Pertanyaan umum</a>' if faq else '')
    body_html=''.join(f'<h2 id="{i}">{l}</h2>{h}' for i,l,h in sections)
    if video:
        v=video;src=(f'<source src="video/{v["slug"]}.mp4" type="video/mp4">' if v['mp4'] else '')+(f'<source src="video/{v["slug"]}.webm" type="video/webm">' if v['webm'] else '')
        info=(f'Video tanpa suara, {v["durasi"]} detik.' if v['durasi'] else '')
        body_html=body_html.replace('<h2 id="'+sections[2][0]+'">',f'<div class="vid'+(' pc' if v['pc'] else '')+'"><video controls playsinline preload="none"'+(f' poster="video/{v["slug"]}.jpg"' if v['poster'] else '')+f'>{src}</video><div><h3 style="margin-top:0">{v["judul"]}</h3><p>{v["ket"]} {info}</p></div></div><h2 id="{sections[2][0]}">',1)
    if app and app_ld:
        import glob
        shots=sorted(glob.glob(os.path.join(OUT,'img',app['k']+'-*.*')),key=lambda p:int(re.sub(r'\D','',os.path.basename(p).split('-')[-1]) or 0))
        shots=[os.path.relpath(p,OUT) for p in shots if p.lower().endswith(('.jpg','.jpeg','.png','.webp'))]
        if shots:
            pcs=[s for s in shots if is_pc(os.path.join(OUT,s))];hps=[s for s in shots if s not in pcs]
            fig=lambda s,i:f'<figure><a href="{s}" target="_blank" rel="noopener" title="Buka ukuran penuh"><img src="{s}" alt="Tampilan {app["n"]} {i+1}" loading="lazy"></a></figure>'
            gal='<h2 id="tampilan">Tampilan aplikasi</h2>'+(('<div class="gal pc">'+''.join(fig(s,shots.index(s)) for s in pcs)+'</div>') if pcs else '')+(('<div class="gal">'+''.join(fig(s,shots.index(s)) for s in hps)+'</div>') if hps else '')
            body_html=body_html.replace('<h2 id="'+sections[1][0]+'">',gal+'<h2 id="'+sections[1][0]+'">',1)
            toc=toc.replace('<a href="#'+sections[1][0]+'">','<a href="#tampilan">Tampilan aplikasi</a><a href="#'+sections[1][0]+'">',1)
    if faq: body_html+='<h2 id="faq">Pertanyaan umum</h2>'+faq_html(faq)
    body_html+=f'<div class="rel"><h2>Baca juga</h2><ul class="pg">{"".join(card(k) for k in rel)}</ul></div>'
    mins=max(2,round(words(body_html+lede)/200))
    box=''
    if app:box=f'<div class="appbox">{ti(app)}<div><b>{app["n"]}</b><small>{(host(app["url"])+" · berdiri sendiri, akun terpisah") if app_ld else ("Aplikasi terkait · "+host(app["url"]))}</small></div><a class="b" href="{app["url"]}" target="_blank" rel="noopener">Buka Aplikasi {EXT}</a></div>'
    crumb_items=[('Beranda',''),('Blog','blog.html'),(h1.split(':')[0],path)]
    body=f'''<div class="w"><nav class="crumb" aria-label="Lokasi"><a href="./">Beranda</a><span aria-hidden="true">›</span><a href="blog.html">Blog</a><span aria-hidden="true">›</span><span>{crumb_items[2][0]}</span></nav>
<header class="ah"><p class="ey">{eyebrow}</p><h1>{h1}</h1><p class="lede">{lede}</p><p class="meta"><span>Oleh Tim Zui System</span><span>Diperbarui <time datetime="{DATE}">{DATE_ID}</time></span><span>±{mins} menit baca</span></p>{box}</header>
<div class="art"><nav class="toc" aria-label="Daftar isi"><b>Daftar isi</b>{toc}</nav><article class="pr">{body_html}</article></div></div>'''
    ld=[{"@type":"Article","headline":h1,"description":desc,"inLanguage":"id","datePublished":"2026-10-17" if path=='apa-itu-erp.html' else DATE,"dateModified":DATE,
         "author":{"@type":"Organization","name":"Tim Zui System","url":SITE},"publisher":{"@id":SITE+"#org"},"mainEntityOfPage":SITE+path,"image":SITE+og,"articleSection":section_name,**({"keywords":kw} if kw else {})},
        crumbs(crumb_items)]
    if faq: ld.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]})
    if app and app_ld: ld.append({"@type":"SoftwareApplication","name":app["n"],"url":app["url"],"operatingSystem":"Web, Android, iOS","applicationCategory":"BusinessApplication" if app["g"]=="Usaha" else ("EducationalApplication" if app["g"]=="Pelajar" else "LifestyleApplication"),"description":desc,"inLanguage":"id","publisher":{"@id":SITE+"#org"}})
    if video:
        v=video;vo={"@type":"VideoObject","name":v['judul'],"description":v['ket'],"contentUrl":SITE+f"video/{v['slug']}."+("mp4" if v['mp4'] else "webm"),"uploadDate":v['tanggal'],"inLanguage":"id","thumbnailUrl":SITE+(f"video/{v['slug']}.jpg" if v['poster'] else og)}
        if v['durasi']:vo["duration"]=f"PT{v['durasi']}S"
        ld.append(vo)
    page(path,title_seo,desc,body,'blog',ld=ld,og=og,ogtype='article')

OGS={}
for a in APPS:
    t=ART[a['k']];og='og-'+a['pg'].replace('.html','.png');OGS[og]=(a,t['seo'].split(': ',1)[1])
    rel=t['rel'][:2]+[GEN_BY_APP.get(a['k'],t['rel'][2])]
    article_page(a['pg'],t['seo'],t['h1'],t['desc'],t['lede'],t['sec'],t['faq'],rel,app=a,video=find_video(a['pg'][:-5],a['n']),og=og,eyebrow='Panduan · '+a['g'],kw=t['kw'])

# ---------- artikel Apa Itu ERP (isi lama, bagian Zui ERP diperbarui) ----------
erp_secs=[]
for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>(.*?)(?=<h2 id=|$)',ERP_BODY,re.S):
    erp_secs.append((m.group(1),re.sub(r'<[^>]+>','',m.group(2)),m.group(3).strip()))
LBL={'pengertian':'Pengertian ERP','perbandingan':'ERP dan spreadsheet','modul':'Modul yang umum','tanda':'Tanda butuh ERP','contoh':'Contoh alur pembelian','memilih':'Cara memilih','memulai':'Langkah memulai','kesalahan':'Kesalahan umum'}
erp_secs=[(i,LBL.get(i,l),h.replace(' Anda bisa mencoba alur serupa pada <a href="zui-erp.html">halaman Zui ERP</a>.',' Alur serupa dijelaskan di <a href="zui-erp.html">panduan Zui ERP</a>.')) for i,l,h in erp_secs]
# judul h2 asli dipakai di isi, label pendek di daftar isi
heads={m.group(1):m.group(2) for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>',ERP_BODY)}
erp_secs.append(('zui','Zui ERP','''<p><a href="zui-erp.html">Zui ERP</a> dibuat untuk usaha kecil dan menengah yang ingin menyatukan pembelian, stok, produksi, keuangan, dan data karyawan. Beberapa hal yang perlu Anda ketahui:</p>
<ul><li>Persetujuan antar divisi (Admin, Keuangan, Gudang) bisa dimatikan pemilik kapan saja bila terasa berat.</li>
<li>Setiap anggota hanya melihat bagian sesuai perannya, dan data tiap perusahaan terpisah.</li>
<li>Dipasang dari peramban di Android, iPhone, dan komputer.</li>
<li>Uji coba 14 hari sejak perusahaan dibuat, tanpa kartu kredit. Paket dan harga ditampilkan di aplikasi.</li></ul>
<p>Untuk usaha konstruksi, ada <a href="zui-kontraktor.html">Zui Kontraktor</a>. Untuk pembukuan dengan jurnal dan laporan keuangan, ada <a href="zui-finance.html">Zui Finance</a>. Setiap aplikasi Zui berdiri sendiri dengan akun masing-masing.</p>
<p><a class="b" href="https://erp.zuisystem.com" target="_blank" rel="noopener" style="text-decoration:none">Buka Zui ERP '''+EXT+'''</a></p>'''))
heads['zui']='Bagaimana Zui ERP membantu'
class S(list):pass
secs2=[(i,l,h) for i,l,h in erp_secs]
def article_erp():
    toc=''.join(f'<a href="#{i}">{l}</a>' for i,l,_ in secs2)+'<a href="#faq">Pertanyaan umum</a>'
    faq=[('Apakah ERP sama dengan aplikasi akuntansi?','Tidak. Akuntansi adalah salah satu bagian dari ERP. ERP juga mencakup pembelian, stok, produksi, dan data karyawan, yang menjadi sumber data bagi pembukuan.'),
         ('Apakah usaha kecil perlu ERP?','Tidak selalu. Jika transaksi masih sedikit dan catatan Anda rapi, spreadsheet bisa cukup. Gunakan daftar tanda di atas untuk menilai apakah sudah waktunya berpindah.'),
         ('Berapa lama sampai ERP siap dipakai?','Itu bergantung pada cakupan dan kebersihan data awal. Memulai dari satu alur, misalnya pembelian dan stok, hampir selalu lebih cepat daripada menyalakan semua modul sekaligus.')]
    sections=[(i,l,h) for i,l,h in secs2]
    # pakai judul h2 panjang di isi
    global article_page
    return sections,faq,heads
sections,faq,heads=article_erp()
def article_erp_page():
    body_sections=[(i,heads.get(i,l),h) for i,l,h in sections]
    toc_sections=sections
    # bangun manual agar daftar isi memakai label pendek
    path='apa-itu-erp.html';h1='Apa Itu ERP? Panduan untuk Pemilik Usaha Kecil dan Menengah'
    desc='Apa itu ERP? Pengertian, perbedaan dengan spreadsheet, modul yang umum, tanda usaha Anda membutuhkannya, contoh alur, dan cara memilih aplikasi ERP untuk UMKM.'
    lede='ERP sering dianggap urusan perusahaan besar. Padahal masalah yang diselesaikannya, yaitu data pembelian, stok, dan uang yang tidak saling nyambung, dialami usaha berkaryawan lima orang sama seperti usaha berkaryawan lima ratus.'
    article_page(path,'Apa Itu ERP? Pengertian dan Panduan untuk UMKM',h1,desc,lede,body_sections,faq,['erp','finance','kontraktor'],og='og-apa-itu-erp.png',eyebrow='Artikel · ERP',kw='apa itu ERP, pengertian ERP, ERP untuk UMKM, contoh ERP',section_name='Artikel')
    s=open(os.path.join(OUT,path),encoding='utf-8').read()
    toc_short=''.join(f'<a href="#{i}">{l}</a>' for i,l,_ in toc_sections)+'<a href="#faq">Pertanyaan umum</a>'
    s=re.sub(r'(<nav class="toc" aria-label="Daftar isi"><b>Daftar isi</b>).*?(</nav>)',lambda m:m.group(1)+toc_short+m.group(2),s,count=1,flags=re.S)
    s=s.replace('"datePublished": "2026-10-17"','"datePublished": "2026-10-17"')
    s=s.replace('<span>Diperbarui <time','<span>Diterbitkan <time datetime="2026-10-17">17 Oktober 2026</time></span><span>Diperbarui <time')
    open(os.path.join(OUT,path),'w',encoding='utf-8').write(s)
article_erp_page()
OGS['og-apa-itu-erp.png']=(None,'Apa Itu ERP? Panduan untuk Pemilik Usaha Kecil dan Menengah')


# ---------- artikel umum ----------
for k,g in GEN.items():
    a=A[g['app']];og='og-'+k.replace('.html','.png');OGS[og]=(a,g['h1'][0].upper()+g['h1'][1:])
    article_page(k,g['seo'],g['h1'][0].upper()+g['h1'][1:],g['desc'],g['lede'],g['sec'],g['faq'],g['rel'],app=a,og=og,eyebrow='Artikel · '+a['g'],kw=g['kw'],section_name='Artikel',app_ld=False)
# ---------- blog ----------
items=''.join(card(a['k']) for a in APPS)+card('erp-art')
blog=f'''<div class="w"><nav class="crumb" aria-label="Lokasi"><a href="./">Beranda</a><span aria-hidden="true">›</span><span>Blog</span></nav>
<header class="ah"><p class="ey">Blog Zui System</p><h1>Panduan aplikasi dan tulisan praktis</h1><p class="lede">Kenali fungsi setiap aplikasi Zui System, mulai dari usaha dan proyek sampai belajar, beserta cara memulainya.</p></header>
<section class="sec"><h2 class="h2">Panduan tiap aplikasi</h2><p class="sub">Satu panduan untuk setiap aplikasi.</p><ul class="pg">{''.join(card(a['k']) for a in APPS)}</ul></section>
<section class="sec"><h2 class="h2">Artikel</h2><p class="sub">Tips praktis untuk usaha, proyek, belajar, dan kegiatan sehari-hari.</p><ul class="pg">{card('erp-art')}{''.join(card(k) for k in GEN)}</ul></section></div>'''
page('blog.html','Blog Zui System: Panduan Aplikasi dan Tips Usaha',
 'Panduan Zui ERP, Zui Kontraktor, Zui Finance, Zui Jurnal, Zui To-Do, dan Studi Kita, serta artikel praktis untuk pemilik usaha kecil dan menengah.',
 blog,'blog',ld=[{"@type":"Blog","name":"Blog Zui System","url":SITE+"blog.html","inLanguage":"id","publisher":{"@id":SITE+"#org"},
 "blogPost":[{"@type":"BlogPosting","headline":ART[a['k']]['h1'],"url":SITE+a['pg'],"dateModified":DATE} for a in APPS]+[{"@type":"BlogPosting","headline":ERP_ART['n'],"url":SITE+ERP_ART['pg'],"datePublished":"2026-10-17","dateModified":DATE}]+[{"@type":"BlogPosting","headline":g['h1'],"url":SITE+k,"datePublished":DATE} for k,g in GEN.items()]},
 crumbs([('Beranda',''),('Blog','blog.html')])],og='og-blog.png')
OGS['og-blog.png']=(None,'Panduan aplikasi dan tulisan praktis')

# ---------- halaman legal ----------
LEG=[('syarat.html','Syarat Layanan'),('privasi.html','Kebijakan Privasi'),('pengembalian-dana.html','Pengembalian Dana'),('kontak.html','Kontak & Alamat')]
def legal_page(path,h1,intro,secs,desc,active='legal'):
    nav=''.join(f'<a href="{p}"'+(' aria-current="page"' if p==path else '')+f'>{n.replace("&","&amp;")}</a>' for p,n in LEG)
    toc=''.join(f'<a href="#{i}">{re.sub(r"^[0-9]+. ","",l)}</a>' for i,l,_ in secs)
    body_html=intro+''.join(f'<h2 id="{i}">{l}</h2>{h}' for i,l,h in secs)
    lay=f'<div class="art"><nav class="toc" aria-label="Isi halaman"><b>Isi halaman</b>{toc}</nav><article class="pr">{body_html}</article></div>' if secs else f'<div class="art"><div></div><article class="pr">{body_html}</article></div>'
    body=f'''<div class="w"><nav class="crumb" aria-label="Lokasi"><a href="./">Beranda</a><span aria-hidden="true">›</span><span>{h1.replace("&","&amp;")}</span></nav>
<header class="ah"><p class="ey">Zui System · {PT}</p><h1>{h1.replace("&","&amp;")}</h1><p class="meta"><span>Berlaku untuk situs zuisystem.com dan semua aplikasi Zui System</span><span>{L.VER}</span></p><nav class="legal-nav" aria-label="Dokumen legal">{nav}</nav></header>{lay}</div>'''
    page(path,f'{h1} Zui System',desc,body,active,ld=[{"@type":"WebPage","name":h1,"url":SITE+path,"inLanguage":"id","dateModified":DATE,"publisher":{"@id":SITE+"#org"}},crumbs([('Beranda',''),(h1,path)])],og='og-legal.png',legal=True)
legal_page('syarat.html','Syarat Layanan',L.SYARAT_INTRO,L.SYARAT,f'Syarat Layanan situs dan aplikasi Zui System, dikelola oleh {PT}: akun, langganan, data, penggunaan yang dilarang, dan hukum yang berlaku.')
legal_page('privasi.html','Kebijakan Privasi',L.PRIVASI_INTRO,L.PRIVASI,f'Kebijakan Privasi Zui System: data yang dikumpulkan tiap aplikasi, tempat penyimpanan, hak Anda, dan cara meminta penghapusan data. Dikelola oleh {PT}.')
legal_page('pengembalian-dana.html','Kebijakan Pengembalian Dana',L.REFUND_INTRO,L.REFUND,f'Kebijakan Pengembalian Dana langganan aplikasi Zui System: pengecualian kesalahan pembayaran, cara mengajukan, dan waktu proses.')
apps_kv=''.join(f'<div><small>{a["n"]}</small><a href="{a["url"]}" target="_blank" rel="noopener">{host(a["url"])}</a></div>' for a in APPS)
kontak=f'''<p>Situs dan aplikasi Zui System dikelola oleh Zui System, {PT}.</p>
<div class="kv"><div><small>Perusahaan</small><b>{PT}</b></div><div><small>Alamat</small><b>{ADDR}</b></div>
<div><small>WhatsApp</small><a href="{WA}" target="_blank" rel="noopener">{WA_TXT}</a></div><div><small>Jam layanan</small><b>Setiap hari, 08.00–22.00 WIB</b></div>
<div><small>Bantuan &amp; pengembalian dana</small><a href="mailto:support@zuisystem.com">support@zuisystem.com</a></div><div><small>Informasi umum &amp; kerja sama</small><a href="mailto:info@zuisystem.com">info@zuisystem.com</a></div></div>
<p><a class="wa" href="{WA}" target="_blank" rel="noopener" style="color:#073B1E;text-decoration:none">{WAI}Chat WhatsApp</a></p>
<h2 id="situs">Situs aplikasi</h2><div class="kv">{apps_kv}</div>'''
legal_page('kontak.html','Kontak & Alamat',kontak,[],f'Kontak Zui System, {PT}: WhatsApp {WA_TXT}, support@zuisystem.com, info@zuisystem.com, alamat di Pamekasan, Jawa Timur, dan jam layanan.',active='kontak')
OGS['og-legal.png']=(None,'Syarat, Privasi, dan Kontak')


# ---------- tentang ----------
ab_apps=''.join(f'<li><a href="{a["pg"]}"><strong>{a["n"]}</strong></a>: {a["d"][0].lower()+a["d"][1:]}</li>' for a in APPS)
tentang_body=f'''<div class="w"><nav class="crumb" aria-label="Lokasi"><a href="./">Beranda</a><span aria-hidden="true">›</span><span>Tentang Zui System</span></nav>
<header class="ah"><p class="ey">Tentang kami</p><h1>Tentang Zui System</h1><p class="lede">Zui System membuat aplikasi sederhana untuk usaha kecil dan menengah, kontraktor, pelajar, dan siapa saja yang ingin pekerjaannya lebih tertata.</p></header>
<div class="art"><nav class="toc" aria-label="Isi halaman"><b>Isi halaman</b><a href="#apa">Apa yang kami buat</a><a href="#prinsip">Cara kami membuat aplikasi</a><a href="#asal">Dari mana kami</a><a href="#hubungi">Hubungi kami</a></nav><article class="pr">
<h2 id="apa">Apa yang kami buat</h2><p>Kami membuat enam aplikasi yang masing-masing berdiri sendiri:</p><ul>{ab_apps}</ul>
<h2 id="prinsip">Cara kami membuat aplikasi</h2>
<ul><li><strong>Satu aplikasi, satu kebutuhan.</strong> Setiap aplikasi fokus pada satu pekerjaan dan punya akun, data, serta langganannya sendiri. Anda cukup memakai yang diperlukan.</li>
<li><strong>Bisa dipakai di HP.</strong> Aplikasi dibuka dari peramban dan bisa ditambahkan ke layar utama, sehingga tim kantor dan lapangan memakai alat yang sama.</li>
<li><strong>Data tetap milik Anda.</strong> Kami tidak menjual data dan tidak memakainya untuk iklan. Rinciannya ada di <a href="privasi.html">Kebijakan Privasi</a>.</li>
<li><strong>Coba dulu sebelum membayar.</strong> Aplikasi menyediakan masa uji coba atau paket gratis, dan langganan tidak diperpanjang otomatis.</li>
<li><strong>Bahasa sehari-hari.</strong> Tampilan memakai Bahasa Indonesia, dan sebagian aplikasi juga tersedia dalam Bahasa Melayu dan English.</li></ul>
<h2 id="asal">Dari mana kami</h2><p>Zui System dikelola dari Pamekasan, Jawa Timur, Indonesia. Pembayaran langganan bisa dilakukan lewat QRIS, dan sebagian aplikasi juga menerima DuitNow untuk pengguna di Malaysia.</p>
<h2 id="hubungi">Hubungi kami</h2><p>Tim kami melayani setiap hari pukul 08.00–22.00 WIB lewat <a href="{WA}" target="_blank" rel="noopener">WhatsApp {WA_TXT}</a>, email <a href="mailto:info@zuisystem.com">info@zuisystem.com</a> untuk informasi umum dan kerja sama, atau <a href="mailto:support@zuisystem.com">support@zuisystem.com</a> untuk bantuan. Alamat lengkap ada di <a href="kontak.html">Kontak &amp; Alamat</a>.</p>
<div class="rel"><h2>Kenali aplikasinya</h2><ul class="pg">{"".join(card(a["k"]) for a in APPS)}</ul></div>
</article></div></div>'''
page('tentang.html','Tentang Zui System','Tentang Zui System: siapa kami, aplikasi yang kami buat untuk usaha, proyek, dan belajar, cara kami membuatnya, dan cara menghubungi tim kami di Pamekasan, Jawa Timur.',
 tentang_body,'',ld=[{"@type":"AboutPage","name":"Tentang Zui System","url":SITE+"tentang.html","inLanguage":"id","about":{"@id":SITE+"#org"},"dateModified":DATE},crumbs([('Beranda',''),('Tentang Zui System','tentang.html')])],og='og-tentang.png')
OGS['og-tentang.png']=(None,'Tentang Zui System')
# ---------- sitemap ----------
urls=[('',1.0),('blog.html',.8)]+[(a['pg'],.9) for a in APPS]+[('apa-itu-erp.html',.7)]+[(k,.7) for k in GEN]+[('tentang.html',.5)]+[(p,.4) for p,_ in LEG]
VID={a['pg']:find_video(a['pg'][:-5],a['n']) for a in APPS if find_video(a['pg'][:-5],a['n'])}
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">\n'
for u,p in urls:
    sm+=f'  <url>\n    <loc>{SITE}{u}</loc>\n    <lastmod>{DATE}</lastmod>\n    <priority>{p:.1f}</priority>\n'
    if u in VID:
        v=VID[u];th=f"video/{v['slug']}.jpg" if v['poster'] else 'og-'+u.replace('.html','.png')
        sm+=f"    <video:video>\n      <video:thumbnail_loc>{SITE}{th}</video:thumbnail_loc>\n      <video:title>{v['judul']}</video:title>\n      <video:description>{v['ket']}</video:description>\n      <video:content_loc>{SITE}video/{v['slug']}.{'mp4' if v['mp4'] else 'webm'}</video:content_loc>\n"+(f"      <video:duration>{v['durasi']}</video:duration>\n" if v['durasi'] else '')+f"      <video:publication_date>{v['tanggal']}</video:publication_date>\n    </video:video>\n"
    sm+='  </url>\n'
open(os.path.join(OUT,'sitemap.xml'),'w').write(sm+'</urlset>\n')
OGS['og-image.png']=(None,'Aplikasi untuk usaha, proyek, dan belajar')
import json as J;J.dump({k:([v[0]['k'] if v[0] else None,v[1]]) for k,v in OGS.items()},open(os.path.join(SCR,'ogs.json'),'w'))
print('ok')
