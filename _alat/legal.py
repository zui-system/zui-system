# Dokumen legal situs, disesuaikan dari dokumen legal ZUI Kontraktor untuk semua aplikasi Zui System.
from common import PT,ADDR,WA,WA_TXT,APPS
APPLIST=', '.join(a['n'] for a in APPS[:-1])+', dan '+APPS[-1]['n']
VER='Berlaku sejak 21 Oktober 2026'

SYARAT=[
('layanan','1. Layanan kami',f'''<p>Zui System menyediakan beberapa aplikasi yang masing-masing berdiri sendiri:</p>
<ul>{''.join(f'<li><strong>{a["n"]}</strong> ({a["url"].split("//")[1]}): {a["d"][0].lower()+a["d"][1:]}</li>' for a in APPS)}</ul>
<p>Setiap aplikasi punya akun, data, dan langganannya sendiri. Akun di satu aplikasi tidak otomatis berlaku di aplikasi lain. Kami bisa menambah, mengubah, atau menghentikan fitur dari waktu ke waktu.</p>'''),
('akun','2. Akun dan keamanan','''<ul><li>Anda wajib memberi nama dan email yang benar, dan memverifikasi email bila aplikasi memintanya.</li>
<li>Jaga kerahasiaan kata sandi. Semua kegiatan di akun Anda menjadi tanggung jawab Anda.</li>
<li>Segera hubungi kami bila Anda menduga akun Anda dipakai orang lain.</li></ul>'''),
('tim','3. Perusahaan, anggota tim, dan peran','''<p>Di aplikasi yang memakai perusahaan atau grup, pemilik bisa mengundang anggota dan mengatur perannya. Pemilik bertanggung jawab atas siapa saja yang diundang dan data yang bisa mereka lihat atau ubah.</p>
<p>Tautan yang bisa dibagikan, misalnya halaman klien dan halaman pekerja di Zui Kontraktor, atau kode grup keluarga dan kelas di Studi Kita, bisa dipakai oleh siapa saja yang menerimanya. Bagikan hanya kepada orang yang tepat.</p>'''),
('langganan','4. Masa uji coba dan langganan','''<ul><li>Masa uji coba, paket gratis, paket berbayar, dan harga bisa berbeda di setiap aplikasi. Rinciannya ditampilkan di dalam aplikasi masing-masing.</li>
<li>Pembayaran dilakukan lewat metode yang ditampilkan di aplikasi, misalnya QRIS atau DuitNow. Paket aktif setelah pembayaran diperiksa.</li>
<li>Langganan tidak diperpanjang otomatis.</li>
<li>Jika masa uji coba atau langganan habis, data tetap tersimpan, tetapi bisa hanya dapat dilihat atau terkunci sampai langganan diperpanjang.</li>
<li>Langganan yang sudah aktif tidak dapat dibatalkan dan pembayarannya tidak dapat dikembalikan, kecuali karena kesalahan pembayaran sesuai <a href="pengembalian-dana.html">Kebijakan Pengembalian Dana</a>.</li></ul>'''),
('data','5. Data milik Anda','''<p>Data yang Anda masukkan tetap milik Anda. Kami hanya memakainya untuk menjalankan layanan sesuai <a href="privasi.html">Kebijakan Privasi</a>. Anda bertanggung jawab atas kebenaran data, termasuk data karyawan, pekerja, klien, atau siswa yang Anda catat, serta memastikan Anda berhak memasukkannya. Kami menyarankan Anda mencadangkan data secara berkala bila aplikasi menyediakan fiturnya.</p>'''),
('larangan','6. Penggunaan yang dilarang','''<ul><li>Memakai aplikasi untuk kegiatan yang melanggar hukum atau menipu.</li>
<li>Mencoba membuka data pengguna atau perusahaan lain, membobol keamanan, atau mengganggu kerja aplikasi.</li>
<li>Menjual kembali atau menyalin aplikasi tanpa izin tertulis dari kami.</li></ul>'''),
('ketersediaan','7. Ketersediaan layanan','''<p>Kami berusaha agar aplikasi selalu bisa dipakai, tetapi tidak menjamin layanan bebas gangguan. Pemeliharaan, gangguan jaringan, atau gangguan penyedia infrastruktur bisa membuat aplikasi sementara tidak tersedia.</p>'''),
('tanggung','8. Batas tanggung jawab','''<p>Dokumen dan angka yang dibuat aplikasi, seperti RAB, penawaran, tagihan, faktur, slip upah, harga jual, dan laporan keuangan, dihitung dari data yang Anda masukkan. Periksa kembali sebelum dikirim ke pihak lain atau dipakai untuk pajak. Sejauh diizinkan hukum, kami tidak bertanggung jawab atas kerugian tidak langsung, kehilangan keuntungan, atau kerugian akibat data yang salah.</p>'''),
('penghentian','9. Penghentian','''<p>Anda bisa berhenti memakai aplikasi kapan saja, menghapus data lewat menu Pengaturan bila tersedia, atau meminta penghapusan akun lewat email. Kami bisa menangguhkan atau menutup akun yang melanggar syarat ini, dengan pemberitahuan bila memungkinkan.</p>'''),
('perubahan','10. Perubahan syarat','''<p>Kami bisa memperbarui syarat ini. Perubahan penting akan kami umumkan di aplikasi, di situs ini, atau lewat email. Tanggal berlaku di atas menunjukkan versi terbaru.</p>'''),
('hukum','11. Hukum yang berlaku','''<p>Syarat ini tunduk pada hukum Republik Indonesia. Perselisihan diselesaikan lebih dulu secara musyawarah, dan bila tidak tercapai, melalui Pengadilan Negeri Pamekasan.</p>'''),
('hubungi','12. Hubungi kami','''<p>Lihat <a href="kontak.html">Kontak &amp; Alamat</a>.</p>'''),
]
SYARAT_INTRO=f'''<p>Syarat ini mengatur penggunaan situs zuisystem.com dan aplikasi {APPLIST} (“aplikasi”) yang dikelola oleh Zui System, {PT} (“kami”). Dengan membuat akun atau memakai aplikasi, Anda menyetujui syarat ini.</p>
<p>Aplikasi tertentu bisa menampilkan ketentuan tambahan di dalamnya. Bila ada perbedaan, ketentuan di dalam aplikasi itulah yang berlaku untuk aplikasi tersebut.</p>'''

PRIVASI=[
('kumpul','1. Data yang kami kumpulkan','''<ul><li><strong>Data akun:</strong> nama, email, dan kata sandi. Kata sandi dikelola oleh layanan login (Firebase Authentication, atau Supabase untuk Studi Kita) dan tidak bisa kami lihat. Bila Anda masuk dengan Google, kami menerima nama dan email akun Google Anda.</li>
<li><strong>Data yang Anda masukkan di aplikasi</strong>, sesuai aplikasi yang dipakai (lihat tabel di bawah).</li>
<li><strong>Data pembayaran:</strong> nomor referensi dan bukti bayar yang Anda kirim untuk mengaktifkan paket. Kami tidak menerima data kartu pembayaran Anda.</li>
<li><strong>Pesan bantuan:</strong> isi chat atau email yang Anda kirim ke kami, termasuk foto yang Anda lampirkan.</li>
<li><strong>Pengaturan perangkat:</strong> bahasa, tema, dan pilihan serupa yang disimpan di peramban perangkat Anda.</li></ul>
<div class="tw"><table><thead><tr><th>Aplikasi</th><th>Data yang Anda masukkan</th></tr></thead><tbody>
<tr><td>Zui ERP</td><td>Profil dan logo perusahaan, anggota dan peran, barang, pembelian, penjualan, pemasok dan pelanggan, produksi, kas dan pembayaran, data karyawan, kehadiran, cuti, dan jejak aktivitas.</td></tr>
<tr><td>Zui Kontraktor</td><td>Profil perusahaan, proyek, survei, RAB, penawaran, tagihan, transaksi, vendor, material, data klien, data pekerja (nama, nomor telepon, upah, kasbon), foto progres, laporan harian, foto absensi, serta lokasi proyek dan lokasi pekerja saat absen. Lokasi hanya diambil saat tombol absen atau atur lokasi ditekan dan izin diberikan.</td></tr>
<tr><td>Zui Finance</td><td>Profil usaha (nama, alamat, telepon, nomor pajak, logo), akun, jurnal, faktur, kurs, dan anggota tim.</td></tr>
<tr><td>Zui Jurnal</td><td>Rencana, proyek, tugas, target, catatan, suasana hati dan energi, kebiasaan, manifestasi, catatan ibadah, serta lokasi yang Anda pilih untuk menghitung waktu ibadah.</td></tr>
<tr><td>Zui To-Do</td><td>Tugas, kategori, target, dan pilihan tema.</td></tr>
<tr><td>Studi Kita</td><td>Jadwal, kegiatan, catatan, rencana, statistik fokus, nama panggilan, kelas, serta nama dan alamat sekolah. Tanpa akun, data hanya tersimpan di perangkat Anda.</td></tr>
</tbody></table></div>'''),
('pakai','2. Untuk apa data dipakai','''<ul><li>Menjalankan fitur aplikasi, seperti menyimpan data, membuat dokumen, dan mencatat absensi.</li>
<li>Memverifikasi email, mengirim undangan tim, dan membantu atur ulang kata sandi.</li>
<li>Mengelola masa uji coba dan langganan.</li>
<li>Menjawab pertanyaan dan permintaan bantuan dari Anda.</li></ul>
<p>Kami tidak menjual data pribadi dan tidak memakainya untuk iklan.</p>'''),
('simpan','3. Tempat penyimpanan dan keamanan','''<p>Data disimpan di layanan Google Firebase (Authentication dan Cloud Firestore) untuk Zui ERP, Zui Kontraktor, Zui Finance, Zui Jurnal, dan Zui To-Do, serta di Supabase untuk Studi Kita. Server penyimpanannya bisa berada di luar Indonesia. Data perusahaan hanya bisa dibuka oleh anggota yang diundang, sesuai perannya. Koneksi ke aplikasi dan situs ini dienkripsi dengan HTTPS.</p>'''),
('bagi','4. Berbagi data','''<p>Kami hanya berbagi data dengan:</p>
<ul><li>Google dan Supabase, sebagai penyedia infrastruktur penyimpanan dan login.</li>
<li>Layanan terjemahan MyMemory, hanya untuk teks yang Anda terjemahkan lewat fitur terjemahan di Studi Kita.</li>
<li>Orang yang Anda beri akses, seperti anggota tim, orang tua dalam grup keluarga, atau penerima tautan halaman klien dan halaman pekerja.</li>
<li>Pihak berwenang, bila diwajibkan oleh hukum.</li></ul>'''),
('situs','5. Situs zuisystem.com','''<p>Situs ini tidak memakai formulir pendaftaran, iklan, atau alat pelacak. Situs memuat huruf dari Google Fonts, sehingga alamat IP Anda diterima Google saat huruf diunduh. Peramban Anda bisa menyimpan salinan halaman agar situs lebih cepat dibuka.</p>'''),
('hak','6. Hak Anda','''<p>Anda berhak meminta salinan data pribadi Anda, memperbaiki data yang salah, menghapus data, dan menarik persetujuan. Sebagian besar bisa Anda lakukan sendiri di aplikasi. Untuk permintaan lain, kirim email ke alamat di bawah. Kami akan menanggapi paling lambat 3 × 24 jam sejak permintaan diterima.</p>'''),
('hapus','7. Lama penyimpanan dan penghapusan','''<p>Data disimpan selama akun atau perusahaan Anda aktif. Bila aplikasi menyediakan menu hapus perusahaan atau hapus akun, data yang dihapus lewat menu itu langsung dihapus dari server. Untuk permintaan penghapusan lain, kirim email ke support@zuisystem.com dari email akun Anda dan sebutkan nama aplikasinya; kami memprosesnya paling lambat 7 hari kerja. Salinan cadangan di penyedia infrastruktur, bila ada, terhapus permanen paling lambat 30 hari setelah penghapusan.</p>'''),
('pihak','8. Data karyawan, pekerja, klien, dan siswa','''<p>Bila Anda mencatat data orang lain, seperti karyawan, pekerja, klien, atau siswa, Anda yang menentukan data tersebut dan bertanggung jawab memberi tahu mereka. Kami memproses data itu atas nama Anda dan hanya untuk menjalankan aplikasi.</p>'''),
('anak','9. Pengguna di bawah umur','''<p>Zui ERP, Zui Kontraktor, dan Zui Finance ditujukan untuk usaha dan tidak ditujukan bagi anak di bawah 18 tahun. Studi Kita dibuat untuk pelajar; pengguna di bawah 18 tahun sebaiknya memakainya dengan sepengetahuan orang tua atau wali. Orang tua dapat meminta data anak dihapus lewat email di bawah.</p>'''),
('ubah','10. Perubahan kebijakan','''<p>Bila kebijakan ini berubah, kami akan memperbarui tanggal berlaku dan memberi tahu perubahan penting di aplikasi, di situs ini, atau lewat email.</p>'''),
('kontak','11. Hubungi kami','''<p>Pertanyaan atau permintaan soal data pribadi bisa dikirim ke <a href="mailto:support@zuisystem.com"><strong>support@zuisystem.com</strong></a>. Alamat lengkap ada di <a href="kontak.html">Kontak &amp; Alamat</a>.</p>'''),
]
PRIVASI_INTRO=f'''<p>Kebijakan ini menjelaskan data apa yang dikumpulkan situs zuisystem.com dan aplikasi {APPLIST}, untuk apa, dan bagaimana Anda bisa mengaturnya. Semua aplikasi dikelola oleh Zui System, {PT}. Kami mengikuti Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi.</p>'''

REFUND=[
('coba','1. Coba dulu sebelum membayar','''<p>Sebagian besar aplikasi Zui menyediakan masa uji coba gratis atau paket gratis. Kami menyarankan Anda memakai masa itu untuk memastikan aplikasi sesuai kebutuhan sebelum berlangganan.</p>'''),
('harga','2. Paket dan harga','''<p>Paket dan harga ditampilkan di dalam masing-masing aplikasi dan bisa berbeda antar aplikasi. Langganan tidak diperpanjang otomatis, jadi tidak ada tagihan berulang tanpa persetujuan Anda.</p>'''),
('kecuali','3. Pengecualian: kesalahan pembayaran','''<p>Pengembalian dana hanya berlaku untuk kesalahan pembayaran berikut:</p>
<ul><li><strong>Pembayaran ganda:</strong> Anda membayar dua kali untuk tagihan yang sama. Kelebihannya dikembalikan penuh.</li>
<li><strong>Kelebihan bayar:</strong> jumlah yang dibayar lebih besar dari harga paket. Selisihnya dikembalikan.</li>
<li><strong>Paket tidak diaktifkan:</strong> paket belum aktif dalam 3 × 24 jam setelah Anda mengirim bukti bayar yang benar, dan Anda memilih membatalkan. Pembayaran dikembalikan penuh.</li></ul>'''),
('tidak','4. Pembayaran yang tidak bisa dikembalikan','''<ul><li>Langganan yang sudah aktif, termasuk perpanjangan, dengan alasan apa pun, misalnya berubah pikiran atau tidak lagi memakai aplikasi.</li>
<li>Sisa masa langganan bila Anda berhenti memakai aplikasi di tengah periode.</li>
<li>Pembatalan paket atau penurunan ke paket yang lebih murah selama masa langganan.</li>
<li>Akun atau perusahaan yang ditutup karena melanggar <a href="syarat.html">Syarat Layanan</a>.</li>
<li>Pembayaran yang dikirim ke tujuan selain QRIS atau DuitNow resmi yang ditampilkan di aplikasi Zui.</li></ul>'''),
('cara','5. Cara mengajukan','''<p>Kirim email ke <a href="mailto:support@zuisystem.com"><strong>support@zuisystem.com</strong></a> dengan judul “Pengembalian Dana” dan sertakan:</p>
<ul><li>nama aplikasi, nama perusahaan (bila ada), dan email akun,</li>
<li>nomor referensi dan tanggal pembayaran, serta jumlah yang dibayar,</li>
<li>alasan pengajuan,</li>
<li>nama bank atau e-wallet, nomor rekening, dan nama pemilik rekening untuk menerima dana.</li></ul>'''),
('proses','6. Proses dan waktu','''<ul><li>Kami membalas pengajuan paling lambat 2 hari kerja.</li>
<li>Bila disetujui, dana dikirim dalam 7 sampai 14 hari kerja ke rekening bank atau e-wallet yang Anda berikan.</li>
<li>Pengembalian karena pembayaran ganda atau kelebihan bayar tidak mengubah paket yang sudah aktif. Untuk paket yang belum diaktifkan, pesanannya dibatalkan dan data Anda tetap aman.</li></ul>'''),
]
REFUND_INTRO='''<p>Kebijakan ini menjelaskan aturan pengembalian dana untuk pembayaran langganan aplikasi Zui System.</p>
<div class="nt warn"><strong>Langganan yang sudah aktif bersifat final.</strong> Langganan tidak dapat dibatalkan dan pembayarannya tidak dapat dikembalikan, kecuali karena kesalahan pembayaran pada bagian 3.</div>'''
