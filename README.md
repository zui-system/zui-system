
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
