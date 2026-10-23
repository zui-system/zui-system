
## Tampilan baru (gaya korporat)
Bilah atas, hero dengan demo alur interaktif, daftar aplikasi, bagian Kontrol, Harga (pilih IDR/MYR/USD), tiga langkah mulai, tanya jawab, dan footer. Edit `APPS` (alamat, repo, APK) dan `PAKET` (harga normal dan promo) di bagian skrip; samakan harga dengan Zui Admin. Tombol Masuk dan Coba gratis mengarah ke `SYS_URL`. Cache `zui-web-v2`.

## Menu aplikasi
Di komputer, menu **Aplikasi** membuka daftar bertingkat; di HP, ikon menu membuka layar penuh dengan daftar Aplikasi yang bisa dilipat. Isi menu dibuat dari daftar `APPS`, jadi aplikasi baru cukup ditambah satu baris di sana (n, d, url, repo). Aplikasi tanpa `url` tampil "Segera". Cache `zui-web-v4`.

- Logo kotak Z diganti tulisan ZUI bersusun (ZUI di atas, SYSTEM kecil). Ikon situs memakai tulisan ZUI. Cache `zui-web-v6`.

- Logo utama resmi (ZUI di atas, SYSTEM kecil; SVG garis dari huruf Inter) dipakai di atas, bawah, dan layar buka website (muncul sekali per sesi tab, CSS+skrip kecil). Cache `zui-web-v7`.

- Layar buka tampil 10 detik (garis menyala berdenyut), hilang lebih cepat jika disentuh/ditekan tombol. Cache dinaikkan.

- Bagian baru **Cara pakai** (video pengenalan 5 aplikasi: Zui System, Inventori, Manufaktur, Keuangan, Karyawan). Video tanpa suara, direkam dari aplikasi dengan data contoh "Zui Kosmetik", dengan teks keterangan di layar. File ada di folder `video/` (mp4 + webm cadangan + poster jpg). Unggah `index.html`, `sw.js`, dan seluruh folder `video/`. Cache `zui-web-v9` (video tidak ikut di-cache oleh service worker).

- Layar buka website kini memakai animasi yang sama dengan aplikasi (huruf ZUI naik satu per satu, SYSTEM muncul pelan, garis biru memanjang lalu berdenyut), ±7,6 detik, tampil setiap website dibuka, tidak bisa dilewati, tetap jalan walau perangkat memakai mode "kurangi gerakan". Cache `zui-web-v10`.

- Link aplikasi memakai satu domain: `https://zuisystem.com/inventori/`, `/manufaktur/`, `/keuangan/`, `/karyawan/` (sebelumnya subdomain terpisah). Cache `zui-web-v11`.

- **Pusat pengaturan** (`admin.js`, Firebase `web-zuisystem`): tersembunyi, buka dengan `#pengaturan` atau ketuk logo 5x; login Google pemilik. Panel samping dengan pratinjau langsung: Tampilan (warna, gaya huruf, tampil/sembunyi bagian), Teks, Aplikasi (tambah/ubah/urut/hapus), Harga (paket dan harga per mata uang), Tanya jawab, Media (galeri gambar/video), Akun. Semua disimpan di Firestore `situs/config` (satu dokumen), media di Storage `galeri/`. `index.html` kini membungkus daftar aplikasi dalam fungsi `rA()` agar bisa dirender ulang. Cache `zui-web-v14`.

- Isi web diperbarui untuk aplikasi Zui ERP, Zui Kontraktor, Zui Jurnal. Bagian "Cara pakai" disembunyikan secara bawaan karena video lama (Inventori, Manufaktur, dst.) tidak cocok lagi; aktifkan lewat panel > Tampilan setelah video baru ada. Alamat aplikasi diisi lewat panel > Aplikasi. Cache `zui-web-v15`.

- SEO: judul, canonical, Open Graph, data terstruktur (JSON-LD), `robots.txt`, `sitemap.xml`, `og-image.png`, dan daftar aplikasi cadangan tanpa JavaScript. Setelah aplikasi punya alamat sendiri, tambahkan ke `sitemap.xml`. Cache `zui-web-v16`.

- Halaman per aplikasi dan blog (SEO), semuanya berkas rata di root agar tidak saling menimpa `index.html`: `zui-erp.html`, `zui-kontraktor.html`, `zui-jurnal.html`, `blog.html`, dan artikel pertama `apa-itu-erp.html`. Gaya bersama `site.css`, skrip `site.js`, gambar OG `og-*.png`. Tiap halaman punya judul, deskripsi, canonical, Open Graph/Twitter, dan JSON-LD. Beranda menautkan ke halaman-halaman itu; daftar aplikasi ditulis statis di HTML. `sitemap.xml` diperbarui. Harga "Rp 79.000" di halaman aplikasi ditulis tetap, ubah juga di sana bila harga berubah. Cache `zui-web-v19`.

- Beranda disegarkan: judul baru ("Usaha tertata. Proyek terpantau. Rencana terjaga."), contoh interaktif bertab untuk tiga aplikasi (ERP, Kontraktor, Jurnal) di bagian atas, bagian baru **Masalah sehari-hari** (`#masalah`) dan **Dari blog** (`#blog`), kartu aplikasi dengan ikon dan poin singkat (diisi dari `IC` dan `BL` di skrip, berdasarkan nama aplikasi), dua tanya jawab baru, dan penutup baru. Semua `id` lama dipertahankan. Cache `zui-web-v20`.

- **Video cara pakai baru** (Zui ERP, Zui Kontraktor, Zui Jurnal), menggantikan video lama (Inventori, Manufaktur, dst.). Berupa animasi ilustrasi bergaya aplikasi dengan data contoh, bukan rekaman layar, tanpa suara dengan teks penjelasan di layar. Ukuran 600×1230 (cocok dengan pemutar HP di beranda), 45–54 detik, MP4 (H.264) + WebM cadangan + poster JPG di folder `video/` (`zui-erp`, `zui-kontraktor`, `zui-jurnal`). Daftar `V` di skrip beranda sudah diganti; tiap halaman aplikasi punya bagian video sendiri dengan data terstruktur VideoObject, dan `sitemap.xml` memuat entri video. Agar bagian **Cara pakai** muncul di beranda, aktifkan lewat panel > Tampilan. Unggah folder `video/` utuh (jangan diratakan). Cache `zui-web-v21`.

- Bagian baru **Aplikasi Kami** (`#aplikasi-kami`) di beranda: enam kartu (Zui ERP, Zui Kontraktor, Zui Jurnal, Zui Finance, Zui To-Do, Studi Kita), masing-masing dengan tombol **Buka Aplikasi** ke subdomainnya di tab baru. Ditulis statis di HTML, tidak diatur dari panel. Tautan "Aplikasi Kami"/"Aplikasi" ditambahkan ke menu semua halaman. Kontak di footer: WhatsApp, `info@zuisystem.com`, `support@zuisystem.com`, dan alamat. Video Zui ERP/Kontraktor/Jurnal dipindah ke folder `video/` (sebelumnya terunggah di root sehingga 404). Cache `zui-web-v22`.

## Tampilan baru: etalase aplikasi (Oktober 2026)
Situs kini berfungsi sebagai etalase dan pintu masuk ke aplikasi. **Setiap aplikasi berdiri sendiri** (akun, data, dan langganan terpisah); harga, login, dan uji coba ada di dalam tiap aplikasi, bukan di situs ini.

- **Tampilan gelap** untuk semua halaman, gaya bersama di `site.css` (huruf Inter).
- **Beranda** (`index.html`): ubin 6 aplikasi (buka di tab baru), Kenapa Zui System, Panduan aplikasi, tombol WhatsApp. Tombol Masuk, Coba gratis, harga, dan kalimat "satu akun" dihapus.
- **Panduan per aplikasi** (juga tampil di Blog): `zui-erp.html`, `zui-kontraktor.html`, `zui-finance.html`, `zui-jurnal.html`, `zui-todo.html`, `studi-kita.html`. Isinya diambil dari fitur nyata di repo tiap aplikasi. Artikel `apa-itu-erp.html` tetap ada. Artikel umum untuk SEO: `cara-membuat-rab.html` (Zui Kontraktor), `cara-membuat-laporan-laba-rugi.html` (Zui Finance), `tips-mengatur-jadwal-belajar.html` (Studi Kita), `cara-membuat-to-do-list.html` (Zui To-Do), `manfaat-menulis-jurnal-harian.html` (Zui Jurnal).
- **Legal**: `syarat.html` (Syarat Layanan), `privasi.html`, `pengembalian-dana.html`, `kontak.html`, disesuaikan dari dokumen legal ZUI Kontraktor untuk semua aplikasi. Zui System ditulis sebagai usaha perorangan; nama pemilik (opsional) diisi di panel Pengaturan → Kontak (`kontak.pemilik`).
- **SEO**: judul, deskripsi, canonical, Open Graph, gambar `og-*.png` per halaman, JSON-LD (Organization, Article, FAQPage, BreadcrumbList, SoftwareApplication, VideoObject), `sitemap.xml`.
- **WhatsApp** +62 882-0007-49699: tombol bulat di pojok kanan bawah setiap halaman, ikon di footer, dan tombol Chat WhatsApp.
- Video Zui Jurnal tidak dipakai lagi karena memuat adegan "Satu akun". Video Zui ERP dan Zui Kontraktor tetap dipakai di panduannya.
- Panel pengaturan (`admin.js`) tidak lagi dimuat di beranda karena bagian yang diaturnya (harga, tanya jawab, daftar aplikasi lama) sudah tidak ada. Berkasnya tetap disimpan.
- Alamat aplikasi Zui Finance memakai `finance.zuisystem.com`; repo Finance masih memakai CNAME `akuntansi.zuisystem.com`, samakan bila perlu.
- Cache `zui-web-v24`.

## Tentang, screenshot, dan video (Oktober 2026)
- Halaman **Tentang Zui System** (`tentang.html`), ditautkan dari footer.
- **Screenshot**: taruh di `img/<aplikasi>-<nomor>.jpg` (lihat `img/README.md`), otomatis tampil di bagian "Tampilan aplikasi" pada panduannya; gambar PC (mendatar) tampil lebar dan bisa diklik, gambar HP (tegak) berjajar.
- **Video**: taruh di `video/<halaman>.mp4` (dan/atau `.webm`, poster `.jpg`), misalnya `video/zui-todo.mp4` atau `video/studi-kita.mp4`. Judul, keterangan, durasi, dan orientasi opsional di `video/<halaman>.json` (`judul`, `keterangan`, `durasi` detik, `tanggal`, `orientasi`: `pc` atau `hp`, bawaan `pc`). Video PC tampil lebar 16:9; video HP tampil tegak di samping teks. Video otomatis tampil di panduan, masuk data terstruktur, dan masuk `sitemap.xml`. Untuk PC disarankan 1280×720 atau 1920×1080 (MP4 H.264).
- Video lama Zui Jurnal dipindah ke `video/arsip/` (tidak dipakai karena memuat "Satu akun").
- Halaman dibangun dari skrip di `_alat/` (lihat `_alat/README.md`). Setelah menambah gambar atau video, jalankan `python3 _alat/build.py`.

## Panel pengaturan (pemilik saja)
Alamat: `https://zuisystem.com/pengaturan.html` (tidak didaftarkan ke Google). Dari panel, pemilik bisa:
- **Aplikasi**: tambah, ubah (nama, alamat, keterangan, kategori, warna, ikon), urutkan, sembunyikan, hapus. Aplikasi baru otomatis tampil di halaman utama, footer, halaman Tentang, dan mendapat halaman sendiri `aplikasi-<kode>.html` (untuk gambar dan video). Panduan lengkap tetap ditulis di `_alat/articles.py`.
- **Gambar**: unggah screenshot per aplikasi (dikecilkan otomatis ke JPG), beri keterangan, urutkan, hapus. Disimpan di `img/`.
- **Video**: unggah MP4/WebM (maks. 95 MB, disimpan di `video/`, sampul dibuat otomatis) atau tempel tautan YouTube (diputar lewat youtube-nocookie, baru dimuat saat ditekan).
- **Kontak** dan **teks halaman utama**.
- **Tampilan**: tema (gelap, terang, otomatis), warna utama dan kedua, jenis huruf, ukuran huruf dan judul, ukuran kartu, sudut kartu, jarak antarbagian, dan tombol terang/gelap untuk pengunjung, dengan pratinjau langsung (PC/HP). Pilihan disimpan di `data/situs.json` (`tampilan`) dan diubah menjadi `tema.css` oleh `build.py`; angka setiap pilihan ada di `TAMPILAN_OPSI` (`_alat/common.py`), disalin ke `data/tampilan.json` untuk panel. Fungsi `tema_css` (Python) dan `temaCss` (panel) harus diubah bersamaan.
- **Terbitkan**: semua perubahan dikirim sebagai satu commit ke `main` lewat GitHub API. Workflow `.github/workflows/bangun-situs.yml` lalu menjalankan `_alat/build.py` dan menyimpan halaman hasilnya; GitHub Pages menayangkannya dalam beberapa menit. Riwayat setiap terbitan ada di GitHub dan bisa dikembalikan.

Semua data panel ada di `data/situs.json`; daftar ikon di `data/ikon.json` (dibuat oleh `build.py` dari `ICONS` di `_alat/common.py`).

### Unggah langsung ke repo (tanpa panel)
Foto `img/<kode>-<nomor>.jpg` dan video `video/<kode>.mp4` (sampul opsional `video/<kode>.jpg`) yang diunggah langsung ke repo dikenali otomatis oleh `build.py` dan tampil di panduan aplikasinya. Rinciannya di `img/README.md`. Unggahan ke `img/` atau `video/` di `main` menjalankan workflow **Bangun situs** sehingga halaman tersusun ulang sendiri.

### Masuk ke panel
Panel memakai **fine-grained personal access token** GitHub milik pemilik; tanpa token yang benar, panel tidak bisa mengubah apa pun. Token disimpan hanya di peramban perangkat itu.
1. GitHub → Settings → Developer settings → Fine-grained tokens → Generate new token.
2. Resource owner `zui-system`; Repository access: Only select repositories → `zui-system/zui-system`.
3. Repository permissions: **Contents: Read and write**, **Actions: Read-only**.
4. Salin token dan tempel di panel. Cabut token kapan saja dari halaman yang sama.

### Bila halaman tidak berubah setelah Terbitkan
- Buka tab **Actions** di repo dan lihat workflow **Bangun situs**.
- Bila gagal karena izin (403), buka Settings → Actions → General → Workflow permissions → pilih **Read and write permissions**.
- GitHub Pages harus menayangkan dari cabang `main` (Settings → Pages → Deploy from a branch).
