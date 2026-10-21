# Gambar dan video aplikasi

Ada dua cara menambah gambar atau video:

## 1. Lewat panel pengaturan (disarankan)
Buka `https://zuisystem.com/pengaturan.html`, pilih aplikasi, unggah, lalu tekan **Terbitkan**. Gambar dikecilkan otomatis dan bisa diberi keterangan.

## 2. Unggah langsung ke repo
Di GitHub: buka folder, tekan **Add file → Upload files**, lalu **Commit changes**. Halaman disusun ulang otomatis dalam beberapa menit.

| Jenis | Folder | Nama berkas | Contoh |
|---|---|---|---|
| Foto | `img/` | `<kode>-<nomor>.jpg` (atau .png, .webp) | `erp-1.jpg`, `erp-2.jpg` |
| Video | `video/` | `<kode>.mp4` (atau .webm) | `todo.mp4` |
| Sampul video (opsional) | `video/` | `<kode>.jpg` | `todo.jpg` |

Kode aplikasi: `erp`, `kontraktor`, `finance`, `jurnal`, `todo`, `studikita` (aplikasi baru dari panel: lihat kodenya di `data/situs.json`).

- Foto tampil di bagian "Tampilan aplikasi" pada panduan aplikasinya, urut sesuai nomor. Foto PC (mendatar) tampil lebar, foto HP (tegak) berjajar.
- Video tampil di panduan aplikasinya bila aplikasi itu belum punya video dari panel. Durasi dan bentuk (PC/HP) dibaca otomatis dari MP4.
- Batas unggah lewat halaman GitHub 25 MB per berkas; lewat panel 95 MB. Video yang lebih besar sebaiknya di YouTube lalu ditempel di panel.
- Berkas yang diunggah langsung tidak muncul di daftar panel, tetapi tetap tampil di situs. Untuk menghapusnya, hapus berkasnya dari repo.
- Pakai data contoh, bukan data pelanggan.
