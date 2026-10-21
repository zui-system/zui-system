import json,os,sys
D=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,D);os.chdir(D)
from common import APPS,A,LOGO,ic
ogs=json.load(open('ogs.json'))
for f,(k,t) in ogs.items():
    a=A.get(k) if k else None
    icons=''.join(f'<span style="--c:{x["c"]}">{ic(x["i"],"1.8")}</span>' for x in APPS) if not a else f'<span class="big" style="--c:{a["c"]}">{ic(a["i"],"1.8")}</span>'
    guide=a and f=='og-'+a['pg'].replace('.html','.png')
    sub=('Panduan '+a['n']) if guide else ('Blog Zui System' if a else 'Zui System')
    url=(a['url'].split('//')[1]) if guide else 'zuisystem.com'
    h=f'''<!doctype html><meta charset=utf-8><style>*{{margin:0;box-sizing:border-box}}body{{width:1200px;height:630px;background:#0A141B;color:#E8EEF2;font-family:Inter,system-ui,sans-serif;position:relative;overflow:hidden;padding:70px 80px;display:flex;flex-direction:column}}
body:before{{content:"";position:absolute;right:-200px;top:-260px;width:900px;height:700px;background:radial-gradient(closest-side,rgba(91,180,210,.35),transparent)}}
.zl{{height:54px;width:auto;color:#E8EEF2;position:relative;align-self:flex-start}}
.k{{margin-top:auto;position:relative}}.s{{color:#7FD1B9;font-size:26px;font-weight:600;letter-spacing:.06em;text-transform:uppercase}}
h1{{font-size:{56 if len(t)<60 else 48}px;line-height:1.12;font-weight:700;letter-spacing:-.02em;max-width:880px;margin-top:14px}}
.u{{color:#93A3AF;font-size:24px;margin-top:22px}}
.ic{{position:absolute;right:80px;top:70px;display:flex;gap:14px}}.ic span{{width:64px;height:64px;border-radius:16px;display:grid;place-items:center;background:color-mix(in srgb,var(--c) 30%,#162733);color:color-mix(in srgb,var(--c) 40%,#fff)}}.ic svg{{width:34px;height:34px}}
.ic .big{{width:120px;height:120px;border-radius:28px}}.ic .big svg{{width:64px;height:64px}}</style>
{LOGO}<div class="ic">{icons}</div><div class="k"><p class="s">{sub}</p><h1>{t}</h1><p class="u">{url}</p></div>'''
    open('og_'+f+'.html','w').write(h)
print(len(ogs))
