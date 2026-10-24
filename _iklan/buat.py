# Membuat materi iklan media sosial dari template.html: gambar PNG, video MP4, dan kartu carousel.
# Jalankan: python3 _iklan/buat.py   (perlu Playwright + Chromium dan ffmpeg)
import json,os,subprocess,sys
D=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(D,'..','_alat'))
from common import ICONS,LOGO,WAI
ik={k:ICONS[k] for k in ['grid','rumah','grafik','catatan','daftar','toga']}
h=open(os.path.join(D,'template.html'),encoding='utf-8').read()
h=h.replace('{{LOGO}}',LOGO).replace('{{ICONS}}',json.dumps(ik)).replace('{{WA}}',WAI)
os.makedirs(os.path.join(D,'hasil'),exist_ok=True)
open(os.path.join(D,'.iklan.html'),'w',encoding='utf-8').write(h)
subprocess.run(['node',os.path.join(D,'render.js')]+sys.argv[1:],check=True)
