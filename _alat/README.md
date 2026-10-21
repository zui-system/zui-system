# Pembangun halaman situs

Semua halaman HTML, `sitemap.xml`, dan isi blog dibuat dari skrip di folder ini. Jangan ubah berkas `.html` di root secara langsung; ubah isinya di sini lalu bangun ulang.

- `common.py`: kepala halaman, bilah atas, footer, data aplikasi (`APPS`), kontak.
- `articles.py`: isi panduan tiap aplikasi.
- `general.py`: artikel umum blog.
- `legal.py`: Syarat Layanan, Kebijakan Privasi, Pengembalian Dana.
- `build.py`: menyusun semua halaman (beranda, blog, panduan, artikel, legal, tentang, sitemap).

## Bangun ulang
```
python3 _alat/build.py
```
Gambar pratinjau (`og-*.png`) dibuat dengan `python3 _alat/og.py` lalu `node _alat/og.js` (butuh Playwright). Hanya perlu bila judul halaman berubah atau ada halaman baru.

Screenshot dan video: lihat `img/README.md` dan README utama.
