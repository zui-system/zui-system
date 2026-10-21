import json,os,re,html as H
OUT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE='https://zuisystem.com/'
DATE='2026-10-21';DATE_ID='21 Oktober 2026'
LOGO=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'logo.svg')).read()
PT='PT. Zaor Utama Indonesia'
def ic(p,sw='1.7'):return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" aria-hidden="true">{p}</svg>'
WAI='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6a9.4 9.4 0 0 0-8.1 14.1L2.6 21.4l4.8-1.3A9.4 9.4 0 1 0 12 2.6z" fill="#fff"/><path d="M12 4.1a7.9 7.9 0 0 0-6.7 12.1l.2.3-.8 2.9 3-.8.3.2A7.9 7.9 0 1 0 12 4.1z" fill="#25D366"/><path d="M9.2 7.6c-.2-.4-.4-.4-.6-.4h-.5c-.2 0-.5.1-.7.3-.3.3-.9.9-.9 2.2s.9 2.6 1.1 2.8c.1.2 1.8 2.9 4.5 4 2.2.9 2.7.7 3.2.7.5-.1 1.6-.7 1.8-1.3.2-.6.2-1.2.2-1.3-.1-.1-.3-.2-.6-.3l-1.9-.9c-.3-.1-.5-.1-.7.1l-.9 1.1c-.2.2-.3.2-.6.1-.3-.1-1.2-.4-2.2-1.4-.8-.7-1.4-1.6-1.5-1.9-.2-.3 0-.4.1-.6l.4-.5.3-.5c.1-.2 0-.4 0-.5z" fill="#fff"/></svg>'
MAIL=ic('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/>')
PIN=ic('<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>')
EXT=ic('<path d="M14 4h6v6M20 4l-9 9M18 14v6H4V6h6"/>')

# Kumpulan ikon yang bisa dipilih di panel pengaturan (kunci → isi SVG 24×24)
ICONS={
 'grid':'<rect x="3" y="3" width="7.5" height="7.5" rx="1"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1"/><path d="M13.5 17.25h7.5M17.25 13.5V21"/>',
 'rumah':'<path d="M3 21h18M5 21V9l7-5 7 5v12M9 21v-6h6v6"/>',
 'grafik':'<path d="M4 20V10M10 20V4M16 20v-7M21 20H3"/>',
 'catatan':'<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 9l1.6 1.6L12.5 7.5M8 15l1.6 1.6 2.9-3.1M14.5 9.5H17M14.5 15.5H17"/>',
 'daftar':'<path d="M9 6h11M9 12h11M9 18h11"/><path d="M3.5 6l1.2 1.2L7 4.8M3.5 12l1.2 1.2L7 10.8M3.5 18l1.2 1.2L7 16.8"/>',
 'toga':'<path d="M2 7l10-4 10 4-10 4z"/><path d="M6 9v5c0 1.7 2.7 3 6 3s6-1.3 6-3V9M22 7v6"/>',
 'keranjang':'<path d="M3 4h2l2.4 11.2a1 1 0 0 0 1 .8h9.2a1 1 0 0 0 1-.8L20 8H6.2"/><circle cx="9.5" cy="19.5" r="1.3"/><circle cx="17" cy="19.5" r="1.3"/>',
 'dompet':'<path d="M4 7h15a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a2 2 0 0 1 2-2h11v3"/><path d="M16 13.5h4"/>',
 'kalender':'<rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
 'orang':'<circle cx="9" cy="8" r="3.2"/><path d="M3 20c.8-3.4 3.2-5.2 6-5.2s5.2 1.8 6 5.2"/><circle cx="17" cy="9" r="2.4"/><path d="M16 14.6c2.3.2 4 1.8 5 4.9"/>',
 'toko':'<path d="M4 10v10h16V10M3 10l1.5-6h15L21 10z"/><path d="M9.5 20v-5h5v5"/>',
 'truk':'<path d="M3 6h11v10H3zM14 9h4l3 3.5V16h-7"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17.5" cy="17.5" r="1.8"/>',
 'kotak':'<path d="M3.5 7.5L12 3l8.5 4.5v9L12 21l-8.5-4.5z"/><path d="M3.5 7.5L12 12l8.5-4.5M12 12v9"/>',
 'pesan':'<path d="M4 5h16v11H8l-4 4z"/><path d="M8 9.5h8M8 12.5h5"/>',
 'jam':'<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
 'kesehatan':'<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/><path d="M9 11h6M12 8v6"/>',
 'buku':'<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H20v3H6.5"/>',
 'bintang':'<path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9z"/>',
}
# Halaman panduan yang sudah ditulis (kunci aplikasi → berkas). Aplikasi baru dari panel tampil tanpa panduan.
PANDUAN={'erp':'zui-erp.html','kontraktor':'zui-kontraktor.html','finance':'zui-finance.html','jurnal':'zui-jurnal.html','todo':'zui-todo.html','studikita':'studi-kita.html'}

DATA=json.load(open(os.path.join(OUT,'data','situs.json'),encoding='utf-8'))
K=DATA['kontak']
WA_NUM=re.sub(r'\D','',K['wa']);WA='https://wa.me/'+WA_NUM;WA_TXT=K['wa_teks']
ADDR=K['alamat'];EMAIL_INFO=K['email_info'];EMAIL_HELP=K['email_bantuan'];JAM=K['jam']
def esc(s):return H.escape(str(s or ''),quote=True)
# Data aplikasi untuk halaman: hanya yang ditampilkan, sesuai urutan di data
APPS=[dict(k=a['k'],n=a['nama'],url=a['url'],pg=PANDUAN.get(a['k']) or 'aplikasi-'+a['k']+'.html',c=a.get('warna') or '#5BB4D2',g=a.get('kategori') or 'Usaha',
 i=ICONS.get(a.get('ikon'),ICONS['bintang']),d=a.get('ket',''),gambar=a.get('gambar') or [],video=a.get('video')) for a in DATA['aplikasi'] if a.get('tampil',True)]
A={a['k']:a for a in APPS}
def host(u):return u.split('//')[1]

NAV=[('Aplikasi','index.html#apl','apl'),('Blog','blog.html','blog'),('Syarat','syarat.html','legal'),('Kontak','kontak.html','kontak')]
def top(active):
    links=''.join(f'<a href="{h}"'+(' aria-current="page"' if k==active else '')+f'>{n}</a>' for n,h,k in NAV)
    return f'<a class="sk" href="#isi">Lewati ke isi</a><header class="top"><div class="w"><a class="lg" href="./" aria-label="Zui System, beranda">{LOGO}</a><nav class="nv" aria-label="Utama">{links}</nav></div></header>'

def footer():
    apps=''.join(f'<a href="{a["pg"]}">{esc(a["n"])}</a>' for a in APPS)
    return f'''<footer class="ft" id="kontak"><div class="w"><div class="fr">
<div class="fb"><a class="lg" href="./" aria-label="Zui System, beranda">{LOGO}</a><p>Aplikasi untuk usaha, proyek, dan belajar.</p></div>
<div><h2>Aplikasi</h2>{apps}</div>
<div><h2>Informasi</h2><a href="tentang.html">Tentang Zui System</a><a href="blog.html">Blog</a><a href="syarat.html">Syarat Layanan</a><a href="privasi.html">Kebijakan Privasi</a><a href="pengembalian-dana.html">Pengembalian Dana</a><a href="kontak.html">Kontak &amp; Alamat</a></div>
<div><h2>Kontak</h2><div class="ic"><a class="waw" href="{WA}" target="_blank" rel="noopener" aria-label="Chat WhatsApp {WA_TXT}" title="WhatsApp {WA_TXT}">{WAI}</a><a href="mailto:{EMAIL_INFO}" aria-label="Email {EMAIL_INFO}" title="{EMAIL_INFO}">{MAIL}</a></div>
<div class="ml"><a href="mailto:{EMAIL_INFO}">{MAIL}{EMAIL_INFO}</a><a href="mailto:{EMAIL_HELP}">{MAIL}{EMAIL_HELP}</a></div><address>{PIN}<span>{esc(ADDR)}</span></address></div>
</div><p class="cp">© <span id="yr">2026</span> Zui System</p></div></footer>
<a class="fab" href="{WA}" target="_blank" rel="noopener" aria-label="Chat WhatsApp Zui System" title="Chat WhatsApp">{WAI}</a>'''

ORG={"@type":"Organization","@id":SITE+"#org","name":"Zui System","url":SITE,"logo":SITE+"icon-512.png","email":EMAIL_INFO,"telephone":"+"+WA_NUM,
 "address":{"@type":"PostalAddress","streetAddress":ADDR,"addressCountry":"ID"},
 "contactPoint":[{"@type":"ContactPoint","contactType":"customer support","email":EMAIL_HELP,"telephone":"+"+WA_NUM,"availableLanguage":["id","en","ms"],"hoursAvailable":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"08:00","closes":"22:00"}}]}
def crumbs(items):
    return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":SITE+u} for i,(n,u) in enumerate(items)]}

def page(path,title,desc,body,active='',ld=None,og='og-image.png',ogtype='website',extra_head='',legal=False):
    url=SITE+('' if path=='index.html' else path)
    graph=[dict(ORG,legalName=PT) if legal else ORG]+(ld or [])
    t=H.escape(title,quote=True);d=H.escape(desc,quote=True)
    doc=f'''<!DOCTYPE html>
<html lang="id"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0A141B"><title>{t}</title>
<meta name="description" content="{d}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{ogtype}"><meta property="og:site_name" content="Zui System"><meta property="og:locale" content="id_ID">
<meta property="og:url" content="{url}"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}">
<meta property="og:image" content="{SITE}{og}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{SITE}{og}">
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False).replace("</","<\\/")}</script>
<link rel="icon" href="icon-192.png"><link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="site.css">{extra_head}
</head><body>
{top(active)}
<main id="isi">
{body}
</main>
{footer()}
<script>document.getElementById('yr').textContent=new Date().getFullYear();document.querySelectorAll('.yt').forEach(function(b){{b.addEventListener('click',function(){{var f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+b.dataset.yt+'?autoplay=1&rel=0';f.title=b.getAttribute('aria-label');f.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';f.allowFullscreen=true;b.replaceWith(f)}})}});if('serviceWorker' in navigator&&/^https?:/.test(location.protocol))navigator.serviceWorker.register('sw.js').catch(function(){{}})</script>
</body></html>
'''
    open(os.path.join(OUT,path),'w',encoding='utf-8').write(doc)
    return doc

def words(s):return len(re.sub(r'<[^>]+>',' ',s).split())
