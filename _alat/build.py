# Menyusun semua halaman situs dari data/situs.json dan isi tulisan di folder ini.
# Jalankan: python3 _alat/build.py
import os,re,sys,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
from articles import ART
from general import GEN
import legal as L

SCR=os.path.dirname(os.path.abspath(__file__))
ERP_BODY=open(os.path.join(SCR,'erp_body.html'),encoding='utf-8').read()
GEN_BY_APP={v['app']:k for k,v in GEN.items()}
GUIDES=[a for a in APPS if a['pg'] and a['k'] in ART]          # aplikasi yang punya panduan
ANGKA=['nol','satu','dua','tiga','empat','lima','enam','tujuh','delapan','sembilan','sepuluh']
def angka(n):return ANGKA[n] if n<len(ANGKA) else str(n)

def ti(a,cls='ti'):return f'<span class="{cls}" style="--c:{a["c"]}">{ic(a["i"])}</span>'
GEN_I='<path d="M5 4h14v16H5zM8 8h8M8 12h8M8 16h5"/>'
def cat(a):return "BusinessApplication" if a["g"]=="Usaha" else ("EducationalApplication" if a["g"]=="Pelajar" else "LifestyleApplication")

# ---------- gambar dan video ----------
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
def exists(p):return bool(p) and os.path.exists(os.path.join(OUT,p))
def yt_id(u):
    m=re.search(r'(?:youtu\.be/|v=|/embed/|/shorts/|/live/)([A-Za-z0-9_-]{11})',u or '')
    return m.group(1) if m else None
def app_video(a):
    """Video panduan dari data aplikasi: berkas di repo atau tautan YouTube. None bila tidak ada."""
    v=a.get('video') or {}
    yid=yt_id(v.get('youtube'));mp4=v.get('file') if exists(v.get('file')) else '';webm=v.get('webm') if exists(v.get('webm')) else ''
    if not(yid or mp4 or webm):return None
    return dict(yt=yid,mp4=mp4,webm=webm,poster=v.get('poster') if exists(v.get('poster')) else '',
        judul=v.get('judul') or 'Cara pakai '+a['n'],ket=v.get('ket') or 'Video singkat cara memakai '+a['n']+'.',
        durasi=v.get('durasi'),tanggal=v.get('tanggal') or DATE,pc=v.get('orientasi','pc')!='hp')
def mp4_info(path):
    """(lebar, tinggi, durasi detik) dari kotak tkhd/mvhd berkas MP4; None bila tidak terbaca."""
    import struct
    try:
        d=open(path,'rb').read()
        w=h=dur=None
        i=d.find(b'mvhd')
        if i>0:
            v=d[i+4];o=i+4+4
            if v==1:ts,du=struct.unpack('>IQ',d[o+16:o+28])
            else:ts,du=struct.unpack('>II',d[o+8:o+16])
            dur=round(du/ts) if ts else None
        j=0
        while True:
            j=d.find(b'tkhd',j+1)
            if j<0:break
            v=d[j+4];size=struct.unpack('>I',d[j-4:j])[0];end=j-4+size
            tw,th=struct.unpack('>II',d[end-8:end]);tw>>=16;th>>=16
            if tw and th:
                # perhitungkan rotasi (HP sering menyimpan video tegak sebagai mendatar + rotasi 90°)
                mat=struct.unpack('>9i',d[end-44:end-8]);
                if mat[0]==0 and abs(mat[1])==65536:tw,th=th,tw
                w,h=tw,th;break
        return (w,h,dur)
    except Exception:return None
def auto_media(a):
    """Gambar dan video yang diunggah langsung ke repo tanpa lewat panel:
    img/<kode>-<nomor>.(jpg|jpeg|png|webp) dan video/<kode>.(mp4|webm) dengan sampul opsional video/<kode>.jpg."""
    k=re.escape(a['k']);known={g.get('file') for g in a['gambar']}
    found=[]
    if os.path.isdir(os.path.join(OUT,'img')):
        for f in os.listdir(os.path.join(OUT,'img')):
            m=re.match(rf'^{k}-(\d+)\.(jpe?g|png|webp)$',f,re.I)
            if m and 'img/'+f not in known:found.append((int(m.group(1)),'img/'+f))
    a['gambar']=list(a['gambar'])+[dict(file=f,ket='') for _,f in sorted(found)]
    if app_video(a):return
    for ext in ('mp4','webm'):
        p=f'video/{a["k"]}.{ext}'
        if exists(p):
            info=mp4_info(os.path.join(OUT,p)) if ext=='mp4' else None
            w,h,dur=info if info else (None,None,None)
            a['video']=dict(file=p if ext=='mp4' else '',webm=p if ext=='webm' else '',poster=f'video/{a["k"]}.jpg' if exists(f'video/{a["k"]}.jpg') else '',
                youtube='',judul='Cara pakai '+a['n'],ket='',durasi=dur,orientasi='hp' if (w and h and h>w) else 'pc',tanggal=DATE)
            return
def video_html(v):
    info=f' Video tanpa suara, {v["durasi"]} detik.' if v['durasi'] and not v['yt'] else ''
    if v['yt']:
        player=f'<button type="button" class="yt" data-yt="{v["yt"]}" aria-label="Putar video: {esc(v["judul"])}"><img src="https://i.ytimg.com/vi/{v["yt"]}/hqdefault.jpg" alt="" loading="lazy"><span aria-hidden="true">▶</span></button>'
    else:
        src=(f'<source src="{v["mp4"]}" type="video/mp4">' if v['mp4'] else '')+(f'<source src="{v["webm"]}" type="video/webm">' if v['webm'] else '')
        player=f'<video controls playsinline preload="none"'+(f' poster="{v["poster"]}"' if v['poster'] else '')+f'>{src}</video>'
    return f'<div class="vid{" pc" if v["pc"] or v["yt"] else ""}">{player}<div><h3 style="margin-top:0">{esc(v["judul"])}</h3><p>{esc(v["ket"])}{info}</p></div></div>'
def video_ld(v,og):
    vo={"@type":"VideoObject","name":v['judul'],"description":v['ket'],"uploadDate":v['tanggal'],"inLanguage":"id"}
    if v['yt']:vo.update(embedUrl=f"https://www.youtube-nocookie.com/embed/{v['yt']}",thumbnailUrl=f"https://i.ytimg.com/vi/{v['yt']}/hqdefault.jpg")
    else:vo.update(contentUrl=SITE+(v['mp4'] or v['webm']),thumbnailUrl=SITE+(v['poster'] or og))
    if v['durasi']:vo["duration"]=f"PT{v['durasi']}S"
    return vo
def gallery_html(a):
    shots=[g for g in a['gambar'] if exists(g.get('file'))]
    if not shots:return ''
    def fig(g,i):
        cap=f'<figcaption>{esc(g["ket"])}</figcaption>' if g.get('ket') else ''
        return f'<figure><a href="{g["file"]}" target="_blank" rel="noopener" title="Buka ukuran penuh"><img src="{g["file"]}" alt="{esc(g.get("ket") or "Tampilan "+a["n"]+" "+str(i+1))}" loading="lazy"></a>{cap}</figure>'
    pcs=[(g,i) for i,g in enumerate(shots) if is_pc(os.path.join(OUT,g['file']))];hps=[(g,i) for i,g in enumerate(shots) if not is_pc(os.path.join(OUT,g['file']))]
    return ('<div class="gal pc">'+''.join(fig(g,i) for g,i in pcs)+'</div>' if pcs else '')+('<div class="gal">'+''.join(fig(g,i) for g,i in hps)+'</div>' if hps else '')

for _a in APPS:auto_media(_a)

# ---------- kartu panduan (beranda, blog, dan bagian terkait) ----------
ERP_ART=dict(pg='apa-itu-erp.html',n='Apa Itu ERP? Panduan untuk Pemilik Usaha',d='Pengertian ERP, modul yang umum, tanda usaha Anda membutuhkannya, dan cara memilih.')
def card(key):
    if key in GEN:
        g=GEN[key];a=A.get(g['app'])
        icon=ti(a) if a else f'<span class="ti gen">{ic(GEN_I)}</span>'
        return f'<li><a href="{key}">{icon}<span><b>{g["h1"][0].upper()+g["h1"][1:]}</b><small>{g["card"]}</small><em>Baca artikel ›</em></span></a></li>'
    if key=='erp-art':
        return f'<li><a href="{ERP_ART["pg"]}"><span class="ti gen">{ic(GEN_I)}</span><span><b>{ERP_ART["n"]}</b><small>{ERP_ART["d"]}</small><em>Baca artikel ›</em></span></a></li>'
    a=A.get(key)
    if not a or not a['pg'] or key not in ART:return ''
    return f'<li><a href="{a["pg"]}">{ti(a)}<span><b>Panduan {esc(a["n"])}</b><small>{ART[key]["lede"].split(". ")[0].rstrip(".")}.</small><em>Baca panduan ›</em></span></a></li>'
def names(apps):
    n=[a['n'] for a in apps]
    return (', '.join(n[:-1])+', dan '+n[-1]) if len(n)>1 else ''.join(n)

# ---------- beranda ----------
B=DATA['beranda']
def wide_slots(n):
    """Ubin lebar (2 kolom) agar baris selalu penuh di grid 4 kolom: pertama, terakhir, lalu di tengah."""
    w=(4-n%4)%4
    if n<=1:return set(range(n))
    order=[0,n-1]+[i for i in range(1,n-1) if i%2==1]
    return set(order[:w])
WIDE=wide_slots(len(APPS))
tiles=''.join(f'<li'+(' class="wd"' if i in WIDE else '')+f'><a href="{esc(a["url"])}" target="_blank" rel="noopener" style="--c:{a["c"]}" aria-label="Buka {esc(a["n"])} di tab baru">{ti(a)}<b>{esc(a["n"])}</b><span>{esc(a["d"])}</span><em>Buka ↗</em></a></li>' for i,a in enumerate(APPS))
guides=''.join(card(a['k']) for a in GUIDES)
home=f'''<div class="w hero"><p class="ey">Zui System</p><h1>{esc(B["judul"])} <span class="gr">{esc(B["judul_warna"])}</span></h1><p>{esc(B["pengantar"])}</p><div class="cta"><a class="b" href="#apl">Jelajahi aplikasi</a></div></div>
<section class="sec" id="apl"><div class="w"><h2>Aplikasi Kami</h2><p class="sub">Setiap aplikasi punya akun dan datanya sendiri. Ketuk untuk membuka di tab baru.</p><ul class="bn">{tiles}</ul></div></section>
<section class="sec" id="kenapa"><div class="w"><h2>Kenapa Zui System</h2><p class="sub">Hal-hal yang membuatnya mudah dipakai.</p><div class="st"><div><b>{len(APPS)}</b><span>aplikasi pilihan</span></div><div><b>Mandiri</b><span>akun dan data tiap aplikasi terpisah</span></div><div><b>HP</b><span>bisa dipasang di layar utama</span></div><div><b>1 ketuk</b><span>langsung terbuka di tab baru</span></div></div></div></section>
<section class="sec" id="panduan"><div class="w"><h2>Panduan aplikasi</h2><p class="sub">Kenali fungsi tiap aplikasi sebelum mencoba.</p><ul class="pg">{guides}</ul><a class="more" href="blog.html">Lihat semua tulisan di Blog ›</a>
</div></section>
<section class="sec" id="pasang"><div class="w"><h2>Pasang di layar utama HP</h2><p class="sub">Aplikasi Zui dibuka dari peramban dan bisa ditambahkan ke layar utama, tanpa toko aplikasi.</p>
<ol class="ps"><li><b>Android</b><span>Buka aplikasinya di Chrome, ketuk menu ⋮, lalu pilih <i>Instal aplikasi</i> atau <i>Tambahkan ke layar utama</i>.</span></li>
<li><b>iPhone dan iPad</b><span>Buka aplikasinya di Safari, ketuk tombol Bagikan, lalu pilih <i>Tambahkan ke Layar Utama</i>.</span></li>
<li><b>Komputer</b><span>Di Chrome atau Edge, klik ikon pasang di ujung kolom alamat bila tersedia, atau simpan sebagai bookmark.</span></li></ol></div></section>'''
page('index.html','Zui System: Aplikasi untuk Usaha, Proyek, dan Belajar',
 f'Kumpulan aplikasi Zui System: {names(APPS)}. Setiap aplikasi berdiri sendiri dan bisa dipasang di HP.',
 home,'',ld=[{"@type":"WebSite","@id":SITE+"#web","url":SITE,"name":"Zui System","inLanguage":"id","publisher":{"@id":SITE+"#org"}},
 {"@type":"ItemList","name":"Aplikasi Zui System","itemListElement":[{"@type":"ListItem","position":i+1,"item":{"@type":"SoftwareApplication","name":a["n"],"url":a["url"],"applicationCategory":cat(a),"operatingSystem":"Web, Android, iOS","description":a["d"],"publisher":{"@id":SITE+"#org"}}} for i,a in enumerate(APPS)]}])

# ---------- halaman artikel (panduan dan artikel umum) ----------
def faq_html(fq):return '<div class="fq">'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in fq)+'</div>'
def article_page(path,title_seo,h1,desc,lede,sections,faq,rel,app=None,og='og-image.png',eyebrow='',kw='',section_name='Panduan',app_ld=True,toc_labels=None):
    toc=''.join(f'<a href="#{i}">{(toc_labels or {}).get(i,l)}</a>' for i,l,_ in sections)
    body_html=''.join(f'<h2 id="{i}">{l}</h2>{h}' for i,l,h in sections)
    video=app_video(app) if app and app_ld else None
    if video:body_html=body_html.replace('<h2 id="'+sections[2][0]+'">',video_html(video)+'<h2 id="'+sections[2][0]+'">',1)
    gal=gallery_html(app) if app and app_ld else ''
    if gal:
        body_html=body_html.replace('<h2 id="'+sections[1][0]+'">','<h2 id="tampilan">Tampilan aplikasi</h2>'+gal+'<h2 id="'+sections[1][0]+'">',1)
        toc=toc.replace('<a href="#'+sections[1][0]+'">','<a href="#tampilan">Tampilan aplikasi</a><a href="#'+sections[1][0]+'">',1)
    if faq:
        toc+='<a href="#faq">Pertanyaan umum</a>';body_html+='<h2 id="faq">Pertanyaan umum</h2>'+faq_html(faq)
    rel_cards=''.join(card(k) for k in rel)
    if rel_cards:body_html+=f'<div class="rel"><h2>Baca juga</h2><ul class="pg">{rel_cards}</ul></div>'
    mins=max(2,round(words(body_html+lede)/200))
    box=''
    if app:box=f'<div class="appbox">{ti(app)}<div><b>{esc(app["n"])}</b><small>{(host(app["url"])+" · berdiri sendiri, akun terpisah") if app_ld else ("Aplikasi terkait · "+host(app["url"]))}</small></div><a class="b" href="{esc(app["url"])}" target="_blank" rel="noopener">Buka Aplikasi {EXT}</a></div>'
    mid=('Aplikasi','index.html#apl') if section_name=='Aplikasi' else ('Blog','blog.html')
    crumb_items=[('Beranda',''),mid,(h1.split(':')[0],path)]
    published='2026-10-17' if path=='apa-itu-erp.html' else DATE
    pub_meta='<span>Diterbitkan <time datetime="2026-10-17">17 Oktober 2026</time></span>' if path=='apa-itu-erp.html' else ''
    body=f'''<div class="w"><nav class="crumb" aria-label="Lokasi"><a href="./">Beranda</a><span aria-hidden="true">›</span><a href="{mid[1]}">{mid[0]}</a><span aria-hidden="true">›</span><span>{crumb_items[2][0]}</span></nav>
<header class="ah"><p class="ey">{eyebrow}</p><h1>{h1}</h1><p class="lede">{lede}</p><p class="meta"><span>Oleh Tim Zui System</span>{pub_meta}<span>Diperbarui <time datetime="{DATE}">{DATE_ID}</time></span><span>±{mins} menit baca</span></p>{box}</header>
<div class="art"><nav class="toc" aria-label="Daftar isi"><b>Daftar isi</b>{toc}</nav><article class="pr">{body_html}</article></div></div>'''
    ld=[{"@type":"Article","headline":h1,"description":desc,"inLanguage":"id","datePublished":published,"dateModified":DATE,
         "author":{"@type":"Organization","name":"Tim Zui System","url":SITE},"publisher":{"@id":SITE+"#org"},"mainEntityOfPage":SITE+path,"image":SITE+og,"articleSection":section_name,**({"keywords":kw} if kw else {})},
        crumbs(crumb_items)]
    if faq: ld.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]})
    if app and app_ld: ld.append({"@type":"SoftwareApplication","name":app["n"],"url":app["url"],"operatingSystem":"Web, Android, iOS","applicationCategory":cat(app),"description":desc,"inLanguage":"id","publisher":{"@id":SITE+"#org"}})
    if video: ld.append(video_ld(video,og))
    page(path,title_seo,desc,body,'apl' if section_name=='Aplikasi' else 'blog',ld=ld,og=og,ogtype='article')

OGS={}
for a in GUIDES:
    t=ART[a['k']];og='og-'+a['pg'].replace('.html','.png');OGS[og]=(a,t['seo'].split(': ',1)[1])
    rel=t['rel'][:2]+[GEN_BY_APP.get(a['k'],t['rel'][2])]
    article_page(a['pg'],t['seo'],t['h1'],t['desc'],t['lede'],t['sec'],t['faq'],rel,app=a,og=og,eyebrow='Panduan · '+a['g'],kw=t['kw'])

# ---------- halaman aplikasi tanpa panduan (aplikasi baru dari panel) ----------
SIMPLE=[a for a in APPS if a['k'] not in ART]
for a in SIMPLE:
    secs=[('tentang','Tentang '+esc(a['n']),f'<p><strong>{esc(a["n"])}</strong>: {esc(a["d"])}</p><p>{esc(a["n"])} dibuka dari <a href="{esc(a["url"])}" target="_blank" rel="noopener">{esc(host(a["url"]))}</a> dan berdiri sendiri, dengan akun dan data yang terpisah dari aplikasi Zui lainnya.</p>'),
          ('mulai','Cara mulai',f'<ol><li>Buka <a href="{esc(a["url"])}" target="_blank" rel="noopener">{esc(host(a["url"]))}</a>.</li><li>Daftar atau masuk, lalu ikuti petunjuk di dalam aplikasi.</li><li>Paket dan harga, bila ada, ditampilkan di dalam aplikasi.</li></ol>'),
          ('bantuan','Bantuan',f'<p>Ada pertanyaan tentang {esc(a["n"])}? Hubungi tim Zui System lewat <a href="{WA}" target="_blank" rel="noopener">WhatsApp {esc(WA_TXT)}</a> atau email <a href="mailto:{EMAIL_HELP}">{EMAIL_HELP}</a>.</p>')]
    desc=f'{a["n"]}: {a["d"]} Aplikasi dari Zui System yang berdiri sendiri, bisa dibuka dari peramban dan dipasang di HP.'
    article_page(a['pg'],f'{a["n"]}: {a["d"].rstrip(".")}',esc(a['n']),desc,esc(a['d']),secs,[],[g['k'] for g in GUIDES[:3]],app=a,og='og-image.png',eyebrow='Aplikasi · '+esc(a['g']),section_name='Aplikasi')

# ---------- artikel Apa Itu ERP (isi lama, bagian Zui ERP diperbarui) ----------
LBL={'pengertian':'Pengertian ERP','perbandingan':'ERP dan spreadsheet','modul':'Modul yang umum','tanda':'Tanda butuh ERP','contoh':'Contoh alur pembelian','memilih':'Cara memilih','memulai':'Langkah memulai','kesalahan':'Kesalahan umum','zui':'Zui ERP'}
erp_secs=[(m.group(1),m.group(2),m.group(3).strip()) for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>(.*?)(?=<h2 id=|$)',ERP_BODY,re.S)]
erp_secs=[(i,l,h.replace(' Anda bisa mencoba alur serupa pada <a href="zui-erp.html">halaman Zui ERP</a>.',' Alur serupa dijelaskan di <a href="zui-erp.html">panduan Zui ERP</a>.')) for i,l,h in erp_secs]
erp_secs.append(('zui','Bagaimana Zui ERP membantu','''<p><a href="zui-erp.html">Zui ERP</a> dibuat untuk usaha kecil dan menengah yang ingin menyatukan pembelian, stok, produksi, keuangan, dan data karyawan. Beberapa hal yang perlu Anda ketahui:</p>
<ul><li>Persetujuan antar divisi (Admin, Keuangan, Gudang) bisa dimatikan pemilik kapan saja bila terasa berat.</li>
<li>Setiap anggota hanya melihat bagian sesuai perannya, dan data tiap perusahaan terpisah.</li>
<li>Dipasang dari peramban di Android, iPhone, dan komputer.</li>
<li>Uji coba 14 hari sejak perusahaan dibuat, tanpa kartu kredit. Paket dan harga ditampilkan di aplikasi.</li></ul>
<p>Untuk usaha konstruksi, ada <a href="zui-kontraktor.html">Zui Kontraktor</a>. Untuk pembukuan dengan jurnal dan laporan keuangan, ada <a href="zui-finance.html">Zui Finance</a>. Setiap aplikasi Zui berdiri sendiri dengan akun masing-masing.</p>
<p><a class="b" href="https://erp.zuisystem.com" target="_blank" rel="noopener" style="text-decoration:none">Buka Zui ERP '''+EXT+'''</a></p>'''))
article_page('apa-itu-erp.html','Apa Itu ERP? Pengertian dan Panduan untuk UMKM','Apa Itu ERP? Panduan untuk Pemilik Usaha Kecil dan Menengah',
 'Apa itu ERP? Pengertian, perbedaan dengan spreadsheet, modul yang umum, tanda usaha Anda membutuhkannya, contoh alur, dan cara memilih aplikasi ERP untuk UMKM.',
 'ERP sering dianggap urusan perusahaan besar. Padahal masalah yang diselesaikannya, yaitu data pembelian, stok, dan uang yang tidak saling nyambung, dialami usaha berkaryawan lima orang sama seperti usaha berkaryawan lima ratus.',
 erp_secs,[('Apakah ERP sama dengan aplikasi akuntansi?','Tidak. Akuntansi adalah salah satu bagian dari ERP. ERP juga mencakup pembelian, stok, produksi, dan data karyawan, yang menjadi sumber data bagi pembukuan.'),
 ('Apakah usaha kecil perlu ERP?','Tidak selalu. Jika transaksi masih sedikit dan catatan Anda rapi, spreadsheet bisa cukup. Gunakan daftar tanda di atas untuk menilai apakah sudah waktunya berpindah.'),
 ('Berapa lama sampai ERP siap dipakai?','Itu bergantung pada cakupan dan kebersihan data awal. Memulai dari satu alur, misalnya pembelian dan stok, hampir selalu lebih cepat daripada menyalakan semua modul sekaligus.')],
 ['erp','finance','kontraktor'],og='og-apa-itu-erp.png',eyebrow='Artikel · ERP',kw='apa itu ERP, pengertian ERP, ERP untuk UMKM, contoh ERP',section_name='Artikel',toc_labels=LBL)
OGS['og-apa-itu-erp.png']=(None,'Apa Itu ERP? Panduan untuk Pemilik Usaha Kecil dan Menengah')

# ---------- artikel umum ----------
for k,g in GEN.items():
    a=A.get(g['app']);og='og-'+k.replace('.html','.png');OGS[og]=(a,g['h1'][0].upper()+g['h1'][1:])
    article_page(k,g['seo'],g['h1'][0].upper()+g['h1'][1:],g['desc'],g['lede'],g['sec'],g['faq'],g['rel'],app=a,og=og,eyebrow='Artikel · '+(a['g'] if a else 'Tips'),kw=g['kw'],section_name='Artikel',app_ld=False)

# ---------- blog ----------
blog=f'''<div class="w"><nav class="crumb" aria-label="Lokasi"><a href="./">Beranda</a><span aria-hidden="true">›</span><span>Blog</span></nav>
<header class="ah"><p class="ey">Blog Zui System</p><h1>Panduan aplikasi dan tulisan praktis</h1><p class="lede">Kenali fungsi setiap aplikasi Zui System, mulai dari usaha dan proyek sampai belajar, beserta cara memulainya.</p></header>
<section class="sec"><h2 class="h2">Panduan tiap aplikasi</h2><p class="sub">Satu panduan untuk setiap aplikasi.</p><ul class="pg">{''.join(card(a['k']) for a in GUIDES)}</ul></section>
<section class="sec"><h2 class="h2">Artikel</h2><p class="sub">Tips praktis untuk usaha, proyek, belajar, dan kegiatan sehari-hari.</p><ul class="pg">{card('erp-art')}{''.join(card(k) for k in GEN)}</ul></section></div>'''
page('blog.html','Blog Zui System: Panduan Aplikasi dan Tips Usaha',
 f'Panduan {names(GUIDES)}, serta artikel praktis untuk pemilik usaha kecil dan menengah.',
 blog,'blog',ld=[{"@type":"Blog","name":"Blog Zui System","url":SITE+"blog.html","inLanguage":"id","publisher":{"@id":SITE+"#org"},
 "blogPost":[{"@type":"BlogPosting","headline":ART[a['k']]['h1'],"url":SITE+a['pg'],"dateModified":DATE} for a in GUIDES]+[{"@type":"BlogPosting","headline":ERP_ART['n'],"url":SITE+ERP_ART['pg'],"datePublished":"2026-10-17","dateModified":DATE}]+[{"@type":"BlogPosting","headline":g['h1'],"url":SITE+k,"datePublished":DATE} for k,g in GEN.items()]},
 crumbs([('Beranda',''),('Blog','blog.html')])],og='og-blog.png')
OGS['og-blog.png']=(None,'Panduan aplikasi dan tulisan praktis')

# ---------- halaman legal ----------
LEG=[('syarat.html','Syarat Layanan'),('privasi.html','Kebijakan Privasi'),('pengembalian-dana.html','Pengembalian Dana'),('kontak.html','Kontak & Alamat')]
def mails(s):return s.replace('support@zuisystem.com',EMAIL_HELP).replace('info@zuisystem.com',EMAIL_INFO)
def legal_page(path,h1,intro,secs,desc,active='legal'):
    nav=''.join(f'<a href="{p}"'+(' aria-current="page"' if p==path else '')+f'>{n.replace("&","&amp;")}</a>' for p,n in LEG)
    toc=''.join(f'<a href="#{i}">{re.sub(r"^[0-9]+. ","",l)}</a>' for i,l,_ in secs)
    body_html=mails(intro+''.join(f'<h2 id="{i}">{l}</h2>{h}' for i,l,h in secs))
    lay=f'<div class="art"><nav class="toc" aria-label="Isi halaman"><b>Isi halaman</b>{toc}</nav><article class="pr">{body_html}</article></div>' if secs else f'<div class="art"><div></div><article class="pr">{body_html}</article></div>'
    body=f'''<div class="w"><nav class="crumb" aria-label="Lokasi"><a href="./">Beranda</a><span aria-hidden="true">›</span><span>{h1.replace("&","&amp;")}</span></nav>
<header class="ah"><p class="ey">Zui System · Dokumen legal</p><h1>{h1.replace("&","&amp;")}</h1><p class="meta"><span>Berlaku untuk situs zuisystem.com dan semua aplikasi Zui System</span><span>{L.VER}</span></p><nav class="legal-nav" aria-label="Dokumen legal">{nav}</nav></header>{lay}</div>'''
    page(path,f'{h1} Zui System',desc,body,active,ld=[{"@type":"WebPage","name":h1,"url":SITE+path,"inLanguage":"id","dateModified":DATE,"publisher":{"@id":SITE+"#org"}},crumbs([('Beranda',''),(h1,path)])],og='og-legal.png',legal=True)
legal_page('syarat.html','Syarat Layanan',L.SYARAT_INTRO,L.SYARAT,f'Syarat Layanan situs dan aplikasi Zui System: akun, langganan, data, penggunaan yang dilarang, dan hukum yang berlaku.')
legal_page('privasi.html','Kebijakan Privasi',L.PRIVASI_INTRO,L.PRIVASI,f'Kebijakan Privasi Zui System: data yang dikumpulkan tiap aplikasi, tempat penyimpanan, hak Anda, dan cara meminta penghapusan data.')
legal_page('pengembalian-dana.html','Kebijakan Pengembalian Dana',L.REFUND_INTRO,L.REFUND,f'Kebijakan Pengembalian Dana langganan aplikasi Zui System: pengecualian kesalahan pembayaran, cara mengajukan, dan waktu proses.')
apps_kv=''.join(f'<div><small>{esc(a["n"])}</small><a href="{esc(a["url"])}" target="_blank" rel="noopener">{esc(host(a["url"]))}</a></div>' for a in APPS)
kontak=f'''<p>Situs dan aplikasi Zui System dikelola oleh {esc(PENGELOLA)}.</p>
<div class="kv"><div><small>Pengelola</small><b>{esc(PENGELOLA)}</b></div><div><small>Alamat</small><b>{esc(ADDR)}</b></div>
<div><small>WhatsApp</small><a href="{WA}" target="_blank" rel="noopener">{esc(WA_TXT)}</a></div><div><small>Jam layanan</small><b>{esc(JAM)}</b></div>
<div><small>Bantuan &amp; pengembalian dana</small><a href="mailto:{EMAIL_HELP}">{EMAIL_HELP}</a></div><div><small>Informasi umum &amp; kerja sama</small><a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a></div></div>
<p><a class="wa" href="{WA}" target="_blank" rel="noopener" style="color:#073B1E;text-decoration:none">{WAI}Chat WhatsApp</a></p>
<h2 id="situs">Situs aplikasi</h2><div class="kv">{apps_kv}</div>'''
legal_page('kontak.html','Kontak & Alamat',kontak,[],f'Kontak Zui System: WhatsApp {WA_TXT}, {EMAIL_HELP}, {EMAIL_INFO}, alamat, dan jam layanan.',active='kontak')
OGS['og-legal.png']=(None,'Syarat, Privasi, dan Kontak')

# ---------- FAQ ----------
FAQ_GRUP=[('umum','Tentang Zui System',[
 ('Apa itu Zui System?',f'Zui System membuat aplikasi web untuk usaha, proyek konstruksi, pembukuan, perencanaan pribadi, dan belajar. Situs dan aplikasinya dikelola oleh {PENGELOLA}.'),
 ('Aplikasi apa saja yang tersedia?','Saat ini ada '+', '.join(esc(a['n'])+' ('+esc(host(a['url']))+')' for a in APPS)+'.'),
 ('Apakah satu akun bisa dipakai di semua aplikasi?','Tidak. Setiap aplikasi berdiri sendiri, dengan akun, data, dan langganannya masing-masing. Anda cukup mendaftar di aplikasi yang Anda perlukan.'),
 ('Apakah perlu memasang aplikasi dari Play Store atau App Store?','Tidak perlu. Aplikasi dibuka dari peramban di HP atau komputer, lalu bisa ditambahkan ke layar utama HP agar terasa seperti aplikasi biasa.')]),
('langganan','Uji coba, langganan, dan pembayaran',[
 ('Apakah bisa mencoba dulu sebelum membayar?','Bisa. Sebagian besar aplikasi menyediakan masa uji coba gratis atau paket gratis. Lama uji coba dan isi paket gratis bisa berbeda di tiap aplikasi.'),
 ('Di mana saya bisa melihat paket dan harga?','Paket dan harga ditampilkan di dalam masing-masing aplikasi, biasanya di menu langganan atau pengaturan. Harga bisa berbeda antar aplikasi.'),
 ('Bagaimana cara membayar langganan?','Pilih paket di dalam aplikasi, lalu bayar dengan metode yang ditampilkan di sana. Paket aktif setelah pembayaran terkonfirmasi.'),
 ('Apakah langganan diperpanjang otomatis?','Tidak. Langganan tidak diperpanjang otomatis, sehingga tidak ada tagihan berulang tanpa persetujuan Anda.'),
 ('Apa yang terjadi bila masa uji coba atau langganan habis?','Data Anda tetap tersimpan, tetapi bisa hanya dapat dilihat atau terkunci sampai langganan diperpanjang.')]),
('refund','Pengembalian dana',[
 ('Apakah langganan bisa dibatalkan dan uangnya dikembalikan?','Langganan yang sudah aktif bersifat final dan tidak dapat dikembalikan, kecuali karena kesalahan pembayaran: pembayaran ganda, kelebihan bayar, atau paket tidak diaktifkan dalam 3 × 24 jam setelah pembayaran.'),
 ('Bagaimana cara mengajukan pengembalian dana?',f'Kirim email ke {EMAIL_HELP} berisi nama aplikasi, email akun, tanggal dan jumlah pembayaran, nomor referensi, serta rekening bank atau e-wallet tujuan pengembalian.'),
 ('Berapa lama prosesnya?','Kami membalas paling lambat 2 hari kerja. Bila disetujui, dana dikirim dalam 7 sampai 14 hari kerja.')]),
('data','Akun dan data',[
 ('Apakah data saya aman?','Data setiap akun dan perusahaan dipisahkan, disimpan di layanan cloud tepercaya, dan dikirim lewat koneksi terenkripsi. Kami tidak menjual data dan tidak memakainya untuk iklan.'),
 ('Bagaimana cara menghapus akun atau data?',f'Gunakan menu hapus di pengaturan aplikasi bila tersedia, atau kirim email ke {EMAIL_HELP} dari email akun Anda dan sebutkan nama aplikasinya. Kami memprosesnya paling lambat 7 hari kerja.'),
 ('Saya lupa kata sandi. Apa yang harus dilakukan?','Pilih "Lupa kata sandi" di halaman masuk aplikasi, lalu ikuti tautan yang dikirim ke email Anda.')]),
('bantuan','Bantuan',[
 ('Bagaimana cara menghubungi Zui System?',f'Lewat WhatsApp {WA_TXT}, email {EMAIL_HELP} untuk bantuan, atau {EMAIL_INFO} untuk informasi umum dan kerja sama. Jam layanan: {JAM}.'),
 ('Di mana alamat Zui System?',f'{ADDR}.')])]
faq_link={'langganan':'<p>Ketentuan lengkap ada di <a href="syarat.html">Syarat Layanan</a>.</p>','refund':'<p>Rinciannya ada di <a href="pengembalian-dana.html">Kebijakan Pengembalian Dana</a>.</p>','data':'<p>Baca juga <a href="privasi.html">Kebijakan Privasi</a>.</p>','bantuan':'<p>Kontak lengkap ada di <a href="kontak.html">Kontak &amp; Alamat</a>.</p>'}
faq_apps=''.join(f'<li><a href="{a["pg"]}#faq">{esc(a["n"])}</a></li>' for a in GUIDES)
faq_toc=''.join(f'<a href="#{i}">{l}</a>' for i,l,_ in FAQ_GRUP)
faq_isi=''.join(f'<h2 id="{i}">{l}</h2>'+faq_html([(esc(q),esc(a)) for q,a in g])+faq_link.get(i,'') for i,l,g in FAQ_GRUP)
faq_body=f'''<div class="w"><nav class="crumb" aria-label="Lokasi"><a href="./">Beranda</a><span aria-hidden="true">›</span><span>FAQ</span></nav>
<header class="ah"><p class="ey">Bantuan</p><h1>Pertanyaan yang sering diajukan</h1><p class="lede">Jawaban singkat tentang aplikasi Zui System, uji coba, langganan, pembayaran, pengembalian dana, dan data Anda.</p></header>
<div class="art"><nav class="toc" aria-label="Isi halaman"><b>Isi halaman</b>{faq_toc}<a href="#aplikasi">Per aplikasi</a></nav><article class="pr">
{faq_isi}
<h2 id="aplikasi">Pertanyaan per aplikasi</h2><p>Pertanyaan khusus tiap aplikasi ada di panduannya:</p><ul>{faq_apps}</ul>
</article></div></div>'''
page('faq.html','FAQ Zui System: Pertanyaan yang Sering Diajukan','FAQ Zui System: uji coba, paket dan harga, cara membayar, pengembalian dana, keamanan data, hapus akun, dan cara menghubungi kami.',
 faq_body,'',ld=[{"@type":"FAQPage","name":"FAQ Zui System","url":SITE+"faq.html","inLanguage":"id","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for _,_,g in FAQ_GRUP for q,a in g]},crumbs([('Beranda',''),('FAQ','faq.html')])],og='og-legal.png')

# ---------- tentang ----------
ab_apps=''.join(f'<li><a href="{a["pg"] or esc(a["url"])}"'+('' if a['pg'] else ' target="_blank" rel="noopener"')+f'><strong>{esc(a["n"])}</strong></a>: {esc(a["d"][:1].lower()+a["d"][1:])}</li>' for a in APPS)
tentang_body=f'''<div class="w"><nav class="crumb" aria-label="Lokasi"><a href="./">Beranda</a><span aria-hidden="true">›</span><span>Tentang Zui System</span></nav>
<header class="ah"><p class="ey">Tentang kami</p><h1>Tentang Zui System</h1><p class="lede">Zui System membuat aplikasi sederhana untuk usaha kecil dan menengah, kontraktor, pelajar, dan siapa saja yang ingin pekerjaannya lebih tertata.</p></header>
<div class="art"><nav class="toc" aria-label="Isi halaman"><b>Isi halaman</b><a href="#apa">Apa yang kami buat</a><a href="#prinsip">Cara kami membuat aplikasi</a><a href="#asal">Dari mana kami</a><a href="#hubungi">Hubungi kami</a></nav><article class="pr">
<h2 id="apa">Apa yang kami buat</h2><p>Kami membuat {angka(len(APPS))} aplikasi yang masing-masing berdiri sendiri:</p><ul>{ab_apps}</ul>
<h2 id="prinsip">Cara kami membuat aplikasi</h2>
<ul><li><strong>Satu aplikasi, satu kebutuhan.</strong> Setiap aplikasi fokus pada satu pekerjaan dan punya akun, data, serta langganannya sendiri. Anda cukup memakai yang diperlukan.</li>
<li><strong>Bisa dipakai di HP.</strong> Aplikasi dibuka dari peramban dan bisa ditambahkan ke layar utama, sehingga tim kantor dan lapangan memakai alat yang sama.</li>
<li><strong>Data tetap milik Anda.</strong> Kami tidak menjual data dan tidak memakainya untuk iklan. Rinciannya ada di <a href="privasi.html">Kebijakan Privasi</a>.</li>
<li><strong>Coba dulu sebelum membayar.</strong> Aplikasi menyediakan masa uji coba atau paket gratis, dan langganan tidak diperpanjang otomatis.</li>
<li><strong>Bahasa sehari-hari.</strong> Tampilan memakai Bahasa Indonesia, dan sebagian aplikasi juga tersedia dalam Bahasa Melayu dan English.</li></ul>
<h2 id="asal">Dari mana kami</h2><p>Zui System dikelola dari Pamekasan, Jawa Timur, Indonesia. Pembayaran langganan bisa dilakukan lewat QRIS, dan sebagian aplikasi juga menerima DuitNow untuk pengguna di Malaysia.</p>
<h2 id="hubungi">Hubungi kami</h2><p>Hubungi kami lewat <a href="{WA}" target="_blank" rel="noopener">WhatsApp {esc(WA_TXT)}</a>, email <a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a> untuk informasi umum dan kerja sama, atau <a href="mailto:{EMAIL_HELP}">{EMAIL_HELP}</a> untuk bantuan. Jam layanan: {esc(JAM)}. Alamat lengkap ada di <a href="kontak.html">Kontak &amp; Alamat</a>.</p>
<div class="rel"><h2>Kenali aplikasinya</h2><ul class="pg">{"".join(card(a["k"]) for a in GUIDES)}</ul></div>
</article></div></div>'''
page('tentang.html','Tentang Zui System','Tentang Zui System: siapa kami, aplikasi yang kami buat untuk usaha, proyek, dan belajar, cara kami membuatnya, dan cara menghubungi tim kami di Pamekasan, Jawa Timur.',
 tentang_body,'',ld=[{"@type":"AboutPage","name":"Tentang Zui System","url":SITE+"tentang.html","inLanguage":"id","about":{"@id":SITE+"#org"},"dateModified":DATE},crumbs([('Beranda',''),('Tentang Zui System','tentang.html')])],og='og-tentang.png')
OGS['og-tentang.png']=(None,'Tentang Zui System')

# ---------- promo (tujuan tombol iklan media sosial) ----------
# Tautan tiap aplikasi diberi utm agar kunjungan dari iklan terlihat di statistik aplikasi
UTM='?utm_source=promo&utm_medium=iklan'
promo_apps=''.join(f'''<li style="--c:{a["c"]}">{ti(a)}<div><b>{esc(a["n"])}</b><span>{esc(a["d"])}</span></div><a class="b" href="{esc(a["url"])}{UTM}" target="_blank" rel="noopener">Daftar / Masuk</a></li>''' for a in APPS)
promo_css='''<style>
.pm{display:grid;grid-template-columns:1fr 300px;gap:28px;align-items:start;padding:22px 0 30px}
.pm h1{font:700 calc(clamp(26px,4.4vw,38px)*var(--hs))/1.12 var(--font);letter-spacing:-.03em;margin:6px 0 10px}
.pm video{width:100%;aspect-ratio:9/16;border-radius:16px;border:1px solid var(--ln);background:var(--pn);display:block}
.pa{list-style:none;padding:0;display:flex;flex-direction:column;gap:10px;margin-top:18px}
.pa li{display:flex;align-items:center;gap:12px;padding:12px;border:1px solid color-mix(in srgb,var(--c) 45%,var(--ln));border-radius:12px;background:var(--pn)}
.pa .ti{flex:none;display:grid;place-items:center;width:42px;height:42px;border-radius:10px;background:color-mix(in srgb,var(--c) 22%,var(--pn2));color:color-mix(in srgb,var(--c) 45%,var(--tif))}.pa .ti svg{width:22px;height:22px}
.pa div{flex:1;min-width:0}.pa b{display:block;font-size:calc(15px*var(--fs))}.pa span{display:block;color:var(--mu);font-size:calc(12.5px*var(--fs));line-height:1.4}
.pa .b{flex:none;padding:11px 16px;font-size:calc(13.5px*var(--fs))}
.pw{margin-top:18px;display:flex;flex-wrap:wrap;gap:10px;align-items:center;color:var(--mu);font-size:calc(13px*var(--fs))}
@media (max-width:760px){.pm{grid-template-columns:1fr}.pm video{max-width:300px;margin:0 auto}.pa li{flex-wrap:wrap}.pa .b{width:100%;justify-content:center}}
</style>'''
promo_body=f'''<div class="w"><div class="pm"><div>
<p class="ey">{angka(len(APPS)).capitalize()} aplikasi Zui System</p>
<h1>Pilih aplikasinya, <span class="gr">langsung mulai.</span></h1>
<p class="lede">Setiap aplikasi punya akun dan datanya sendiri. Tekan <strong>Daftar / Masuk</strong> pada aplikasi yang Anda butuhkan untuk membuat akun dan mencobanya.</p>
<ul class="pa">{promo_apps}</ul>
<div class="pw"><span>Masih ragu? Tanya dulu:</span><a class="wa" href="{WA}?text={__import__('urllib.parse').parse.quote('Halo Zui System, saya lihat iklannya dan ingin bertanya.')}" target="_blank" rel="noopener">{WAI}Chat WhatsApp</a></div>
</div>
<video src="video/promo.mp4" poster="video/promo.jpg" autoplay muted loop playsinline preload="metadata" aria-label="Video pengenalan enam aplikasi Zui System"></video>
</div></div>'''
page('promo.html','Mulai Pakai Aplikasi Zui System','Pilih aplikasi Zui System yang Anda butuhkan, lalu daftar dan coba langsung: Zui ERP, Zui Kontraktor, Zui Finance, Zui Jurnal, Zui To-Do, dan Studi Kita.',
 promo_body,'',ld=[crumbs([('Beranda',''),('Mulai pakai','promo.html')])],extra_head=promo_css)

# ---------- sitemap ----------
urls=[('',1.0),('blog.html',.8)]+[(a['pg'],.9) for a in GUIDES]+[(a['pg'],.6) for a in SIMPLE]+[('apa-itu-erp.html',.7)]+[(k,.7) for k in GEN]+[('tentang.html',.5),('faq.html',.5)]+[(p,.4) for p,_ in LEG]
VID={a['pg']:app_video(a) for a in APPS if app_video(a)}
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">\n'
for u,p in urls:
    sm+=f'  <url>\n    <loc>{SITE}{u}</loc>\n    <lastmod>{DATE}</lastmod>\n    <priority>{p:.1f}</priority>\n'
    if u in VID:
        v=VID[u]
        th=f"https://i.ytimg.com/vi/{v['yt']}/hqdefault.jpg" if v['yt'] else SITE+(v['poster'] or 'og-'+u.replace('.html','.png'))
        loc=f"      <video:player_loc>https://www.youtube-nocookie.com/embed/{v['yt']}</video:player_loc>\n" if v['yt'] else f"      <video:content_loc>{SITE}{v['mp4'] or v['webm']}</video:content_loc>\n"
        sm+=f"    <video:video>\n      <video:thumbnail_loc>{th}</video:thumbnail_loc>\n      <video:title>{esc(v['judul'])}</video:title>\n      <video:description>{esc(v['ket'])}</video:description>\n"+loc+(f"      <video:duration>{v['durasi']}</video:duration>\n" if v['durasi'] else '')+f"      <video:publication_date>{v['tanggal']}</video:publication_date>\n    </video:video>\n"
    sm+='  </url>\n'
open(os.path.join(OUT,'sitemap.xml'),'w').write(sm+'</urlset>\n')

# ---------- data untuk panel pengaturan ----------
open(os.path.join(OUT,'tema.css'),'w').write(TEMA_CSS)
open(os.path.join(OUT,'data','tampilan.json'),'w').write(json.dumps(dict(opsi=TAMPILAN_OPSI,palet=PALET,bawaan=TAMPILAN_BAWAAN),ensure_ascii=False,indent=1)+'\n')
open(os.path.join(OUT,'data','ikon.json'),'w').write(json.dumps(ICONS,ensure_ascii=False,indent=1)+'\n')
OGS['og-image.png']=(None,'Aplikasi untuk usaha, proyek, dan belajar')
json.dump({k:([v[0]['k'] if v[0] else None,v[1]]) for k,v in OGS.items()},open(os.path.join(SCR,'ogs.json'),'w'))
print('ok')
