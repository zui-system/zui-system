# Isi panduan per aplikasi. Fakta diambil dari kode dan catatan tiap repo aplikasi.
# Format bagian: (id, label daftar isi, html)
ART={}

ART['erp']=dict(
 seo='Zui ERP: Aplikasi ERP untuk Usaha Kecil dan Menengah',
 h1='Zui ERP: aplikasi ERP untuk pembelian, stok, produksi, keuangan, dan karyawan',
 desc='Panduan Zui ERP: modul Inventori, Manufaktur, Keuangan, dan Karyawan, peran tim, alur persetujuan, harga jual otomatis, dan cara mulai uji coba 14 hari.',
 lede='Zui ERP menyatukan pekerjaan harian usaha dagang dan produksi dalam satu tempat. Data diketik sekali, lalu dipakai oleh gudang, kasir, keuangan, dan pemilik tanpa diketik ulang.',
 kw='aplikasi ERP, ERP UMKM, aplikasi stok barang, aplikasi inventori, aplikasi pembelian',
 sec=[
('apa','Apa itu Zui ERP','''<p><strong>Zui ERP</strong> adalah aplikasi ERP (perencanaan sumber daya perusahaan) untuk usaha kecil dan menengah. Di dalamnya ada satu pusat dan empat modul yang saling terhubung. Pusatnya mengurus perusahaan, anggota tim, peran, dan jejak aktivitas. Modulnya mengurus barang, produksi, uang, dan karyawan.</p>
<p>Zui ERP dibuka dari <a href="https://erp.zuisystem.com" target="_blank" rel="noopener">erp.zuisystem.com</a> dan berdiri sendiri. Akun, data, dan langganannya terpisah dari aplikasi Zui lainnya.</p>'''),
('modul','Modul di dalamnya','''<div class="tw"><table><thead><tr><th>Modul</th><th>Yang dikelola</th></tr></thead><tbody>
<tr><td><strong>Inventori</strong></td><td>Daftar barang, batch dan tanggal kedaluwarsa, pembelian dari pemasok, penjualan, riwayat keluar-masuk stok, serta daftar pemasok dan pelanggan.</td></tr>
<tr><td><strong>Manufaktur</strong></td><td>Resep produksi (<em>bill of materials</em>) dengan biaya lain per batch, permintaan bahan ke gudang, uji mutu, dan penerimaan hasil produksi.</td></tr>
<tr><td><strong>Keuangan</strong></td><td>Akun kas dan bank, transaksi kas, utang dan piutang, pembayaran, serta pengeluaran yang menunggu persetujuan.</td></tr>
<tr><td><strong>Karyawan</strong></td><td>Data karyawan, kehadiran, dan pengajuan cuti beserta persetujuannya.</td></tr>
</tbody></table></div>
<p>Pemilik dan Admin juga punya tab <strong>Pantauan</strong>: ringkasan semua divisi dalam satu layar, mulai dari nilai stok, barang menipis, pembelian yang menunggu, saldo, utang dan piutang, produksi berjalan, sampai karyawan yang cuti hari ini. Setiap anggota juga melihat daftar <strong>Menunggu tindakan</strong> berisi pekerjaan yang sedang menunggu perannya.</p>'''),
('peran','Peran dan hak akses','''<p>Setiap anggota diundang lewat email dengan satu peran. Peran menentukan bagian yang bisa dilihat dan diubah.</p>
<ul><li><strong>Pemilik dan Admin</strong>: semua modul, pengaturan, dan data.</li>
<li><strong>Gudang</strong>: barang dan pembelian.</li>
<li><strong>Kasir</strong>: penjualan dan kontak pelanggan. Harga pokok (HPP) tidak ditampilkan di layar Kasir.</li>
<li><strong>Keuangan</strong>: pembayaran pembelian dan penjualan, kas, dan laporan.</li>
<li><strong>Produksi dan Mutu</strong>: kegiatan produksi dan uji mutu.</li></ul>
<p>Perubahan penting tercatat sebagai jejak aktivitas yang hanya bisa ditambah, tidak bisa diubah atau dihapus.</p>'''),
('alur','Contoh alur: satu pembelian','''<p>Misalnya sebuah usaha memesan 200 botol dari pemasok seharga Rp 12.400.000 (angka contoh).</p>
<ol><li>Staf pembelian membuat pesanan pembelian (PO). Statusnya menunggu persetujuan Admin.</li>
<li>Admin menyetujui, lalu Keuangan mengonfirmasi. Langkah berikutnya terkunci sampai langkah sebelumnya selesai.</li>
<li>Gudang menerima barang. Stok bertambah 200 botol dan utang ke pemasok tercatat di Keuangan, tanpa diketik ulang.</li></ol>
<p>Untuk tim kecil, pemilik bisa mematikan kewajiban persetujuan dan serah-terima antar divisi di Pengaturan.</p>
<p>Uang dari penjualan juga bisa langsung masuk kas. Bila penjualan dicatat Kasir, uangnya menjadi setoran yang menunggu diterima Keuangan.</p>'''),
('harga-jual','Harga jual otomatis','''<p>Pemilik bisa menyalakan harga jual otomatis: harga dihitung dari HPP ditambah persentase keuntungan, lalu dibulatkan. Keuntungan bisa diatur untuk semua barang, per kategori, atau per barang. Saat HPP naik karena pembelian atau hasil produksi, harga jual ikut naik. Saat HPP turun, aplikasi hanya memberi saran harga.</p>'''),
('bahasa','Bahasa, mata uang, dan perangkat','''<ul><li>Bahasa Indonesia, English, dan Bahasa Melayu. Tiap anggota boleh memilih bahasanya sendiri.</li>
<li>Mata uang Rupiah, Ringgit Malaysia, atau Dolar AS, dipilih per perusahaan. Pilihan ini hanya mengubah simbol dan format angka; nilai tidak dikonversi.</li>
<li>Dipasang dari peramban di Android, iPhone, atau komputer, sehingga ikonnya muncul di layar utama.</li></ul>'''),
('mulai','Cara mulai','''<ol><li>Buka <a href="https://erp.zuisystem.com" target="_blank" rel="noopener">erp.zuisystem.com</a>, lalu daftar dengan email (diverifikasi) atau masuk dengan Google.</li>
<li>Buat perusahaan. Anda menjadi Pemilik dan uji coba 14 hari langsung berjalan.</li>
<li>Undang anggota tim lewat email beserta perannya.</li>
<li>Mulai dari satu alur, misalnya pembelian sampai stok masuk, lalu tambah modul lain bertahap.</li></ol>
<p>Setelah uji coba berakhir, aplikasi terkunci sampai langganan aktif. Data tetap tersimpan. Paket dan harga ditampilkan di dalam aplikasi.</p>'''),
 ],
 faq=[('Apakah Zui ERP cocok untuk usaha kecil?','Cocok bila pembelian, stok, dan kas mulai dicatat di banyak tempat. Persetujuan antar divisi bisa dimatikan, sehingga alurnya bisa disederhanakan untuk tim kecil.'),
('Apakah akun Zui ERP bisa dipakai di aplikasi Zui lain?','Tidak. Setiap aplikasi Zui berdiri sendiri, dengan akun, data, dan langganannya masing-masing.'),
('Apakah Zui ERP sama dengan aplikasi akuntansi?','Tidak. Zui ERP mencakup pembelian, stok, produksi, dan karyawan selain kas. Untuk pembukuan dengan jurnal dan laporan keuangan lengkap, lihat Zui Finance.'),
('Berapa lama uji cobanya?','14 hari sejak perusahaan dibuat, tanpa kartu kredit.')],
 rel=['finance','kontraktor','erp-art'],video=('zui-erp',49,'Cara pakai Zui ERP','Ikuti satu pembelian dari PO sampai stok masuk, lewat persetujuan Admin dan Keuangan.'))

ART['kontraktor']=dict(
 seo='Zui Kontraktor: Aplikasi Kontraktor untuk Proyek, RAB, dan Tagihan',
 h1='Zui Kontraktor: aplikasi untuk proyek, RAB, tagihan, pekerja, dan material',
 desc='Panduan Zui Kontraktor: kelola proyek, survei, RAB, penawaran, tagihan, keuangan proyek, absensi dan upah pekerja, material, serta halaman progres untuk klien.',
 lede='Zui Kontraktor dibuat untuk usaha jasa konstruksi dan renovasi. Kantor dan lapangan memakai data yang sama, dari survei pertama sampai tagihan terakhir.',
 kw='aplikasi kontraktor, aplikasi RAB, aplikasi proyek konstruksi, absensi pekerja proyek',
 sec=[
('apa','Apa itu Zui Kontraktor','''<p><strong>Zui Kontraktor</strong> adalah aplikasi untuk mengelola usaha kontraktor: proyek, survei, RAB, penawaran, tagihan, keuangan, pekerja, absensi, upah, dan material. Aplikasi ini dibuka dari <a href="https://kontraktor.zuisystem.com" target="_blank" rel="noopener">kontraktor.zuisystem.com</a> dan berdiri sendiri, dengan akun dan data yang terpisah dari aplikasi Zui lainnya.</p>'''),
('fitur','Yang dikelola','''<div class="tw"><table><thead><tr><th>Bagian</th><th>Isi</th></tr></thead><tbody>
<tr><td><strong>Proyek</strong></td><td>Daftar proyek, lokasi, progres, foto progres, dan laporan harian.</td></tr>
<tr><td><strong>Survei dan RAB</strong></td><td>Catatan survei lalu rencana anggaran biaya yang menjadi dasar penawaran.</td></tr>
<tr><td><strong>Penawaran dan tagihan</strong></td><td>Dokumen penawaran untuk klien dan tagihan sesuai termin pembayaran.</td></tr>
<tr><td><strong>Keuangan</strong></td><td>Transaksi masuk dan keluar per proyek, serta vendor.</td></tr>
<tr><td><strong>Pekerja</strong></td><td>Data pekerja, absensi dengan foto dan lokasi, upah, dan kasbon.</td></tr>
<tr><td><strong>Material</strong></td><td>Kebutuhan dan pemakaian material per proyek.</td></tr>
</tbody></table></div>'''),
('lapangan','Halaman pekerja dan halaman klien','''<p>Zui Kontraktor punya dua halaman yang bisa dibagikan lewat tautan:</p>
<ul><li><strong>Halaman pekerja</strong>: pekerja absen dari HP. Foto dan titik lokasi diambil hanya saat tombol absen ditekan dan izin diberikan.</li>
<li><strong>Halaman klien</strong>: klien melihat progres proyeknya tanpa perlu membuat akun.</li></ul>
<div class="nt warn">Siapa pun yang menerima tautan halaman pekerja atau halaman klien bisa membukanya. Bagikan hanya kepada orang yang tepat.</div>'''),
('tim','Tim dan peran','''<p>Pemilik perusahaan mengundang anggota tim dan mengatur perannya. Pemilik bertanggung jawab atas siapa yang diundang dan data yang bisa mereka lihat atau ubah.</p>'''),
('paket','Uji coba dan paket','''<ul><li>Perusahaan baru mendapat uji coba gratis 14 hari dengan fitur lengkap.</li>
<li>Setelah itu tersedia paket Starter, Pro, dan Bisnis untuk 1, 6, atau 12 bulan. Harga berlaku per perusahaan dan ditampilkan di aplikasi.</li>
<li>Pembayaran lewat QRIS dan paket aktif setelah pembayaran diperiksa. Langganan tidak diperpanjang otomatis.</li>
<li>Bila masa langganan habis, data tetap aman dan bisa dilihat, tetapi tidak bisa diubah sampai diperpanjang.</li></ul>'''),
('mulai','Cara mulai','''<ol><li>Buka <a href="https://kontraktor.zuisystem.com" target="_blank" rel="noopener">kontraktor.zuisystem.com</a>, daftar dengan email atau masuk dengan Google.</li>
<li>Buat perusahaan dan isi profil serta logonya. Uji coba 14 hari langsung berjalan.</li>
<li>Tambahkan proyek pertama, lalu undang tim dan bagikan halaman pekerja.</li></ol>
<p>Dokumen seperti RAB, penawaran, tagihan, dan slip upah dihitung dari data yang Anda masukkan. Periksa kembali angkanya sebelum dikirim ke klien.</p>'''),
 ],
 faq=[('Apakah pekerja harus punya akun?','Tidak. Pekerja absen lewat tautan halaman pekerja yang Anda bagikan.'),
('Apakah klien bisa melihat progres proyek?','Bisa, lewat tautan halaman klien. Klien tidak perlu membuat akun.'),
('Apakah Zui Kontraktor sama dengan Zui ERP?','Tidak. Zui ERP untuk usaha dagang dan produksi. Zui Kontraktor khusus untuk proyek konstruksi. Keduanya berdiri sendiri dengan akun masing-masing.'),
('Bagaimana cara membayar langganan?','Lewat QRIS dari dalam aplikasi. Paket aktif setelah admin memeriksa pembayaran.')],
 rel=['erp','finance','todo'],video=('zui-kontraktor',54,'Cara pakai Zui Kontraktor','Ikuti satu proyek renovasi: anggaran, progres lapangan, material, dan termin pembayaran.'))

ART['finance']=dict(
 seo='Zui Finance: Aplikasi Pembukuan dan Faktur untuk UMKM',
 h1='Zui Finance: aplikasi pembukuan, faktur, dan laporan keuangan',
 desc='Panduan Zui Finance: jurnal dan buku besar, faktur dengan pajak dan logo, laporan laba rugi, neraca, dan arus kas, multi mata uang, rekonsiliasi bank, dan tim.',
 lede='Zui Finance membantu usaha kecil dan menengah mencatat transaksi dengan cara akuntansi yang benar, lalu menghasilkan faktur dan laporan keuangan kapan saja.',
 kw='aplikasi pembukuan, aplikasi akuntansi UMKM, aplikasi faktur, laporan laba rugi',
 sec=[
('apa','Apa itu Zui Finance','''<p><strong>Zui Finance</strong> adalah aplikasi pembukuan untuk usaha kecil dan menengah. Anda mencatat jurnal, membuat faktur, dan memantau laporan dalam Rupiah, Ringgit, atau Dolar AS. Aplikasi ini dibuka dari <a href="https://finance.zuisystem.com" target="_blank" rel="noopener">finance.zuisystem.com</a> dan berdiri sendiri dari aplikasi Zui lainnya.</p>'''),
('fitur','Fitur utama','''<ul><li><strong>Jurnal dan buku besar.</strong> Jurnal multi-baris yang tidak bisa diubah setelah dicatat. Koreksi dilakukan lewat jurnal balik, dan setiap akun punya buku besarnya sendiri.</li>
<li><strong>Faktur.</strong> Banyak item, pajak, nomor otomatis, logo usaha, lalu dicetak atau disimpan sebagai PDF.</li>
<li><strong>Laporan.</strong> Neraca saldo, laba rugi, posisi keuangan (neraca), dan arus kas, bisa dicetak atau diekspor.</li>
<li><strong>Multi mata uang.</strong> Rupiah, Ringgit Malaysia, dan Dolar AS dengan kurs yang Anda atur sendiri.</li>
<li><strong>Jurnal berulang.</strong> Transaksi rutin seperti sewa atau gaji tercatat sendiri saat jatuh tempo.</li>
<li><strong>Rekonsiliasi bank.</strong> Cocokkan mutasi bank dengan catatan kas untuk menemukan selisih.</li>
<li><strong>Tim dan peran.</strong> Undang anggota sebagai owner, editor, atau viewer.</li>
<li><strong>Keamanan.</strong> Masuk dengan Google atau email terverifikasi, dan setiap jurnal punya rantai audit.</li></ul>'''),
('profil','Profil usaha di faktur','''<p>Nama, alamat, telepon, nomor pajak (NPWP atau SSM), dan logo usaha diisi sekali di profil usaha, lalu tampil di faktur dan laporan.</p>'''),
('beda','Zui Finance dan Zui ERP','''<p>Keduanya mencatat uang, tetapi untuk kebutuhan yang berbeda. Zui ERP mencatat kas sebagai bagian dari pembelian, stok, dan produksi. Zui Finance fokus pada pembukuan: jurnal berpasangan, buku besar, faktur, dan laporan keuangan. Keduanya aplikasi terpisah dengan akun masing-masing.</p>'''),
('paket','Paket','''<p>Zui Finance punya paket Gratis untuk mulai (satu buku usaha, satu anggota, sampai 50 transaksi per bulan) dan paket berbayar dengan anggota lebih banyak dan transaksi tanpa batas, termasuk uji coba gratis 14 hari. Rincian paket dan harga terbaru ada di dalam aplikasi.</p>'''),
('mulai','Cara mulai','''<ol><li>Buka <a href="https://finance.zuisystem.com" target="_blank" rel="noopener">finance.zuisystem.com</a>, lalu daftar gratis.</li>
<li>Isi profil usaha dan pilih mata uang.</li>
<li>Catat transaksi pertama, lalu lihat buku besar dan laporannya.</li></ol>
<p>Aplikasi tersedia dalam Bahasa Indonesia, English, dan Bahasa Melayu, dengan tema terang atau gelap.</p>'''),
 ],
 faq=[('Apakah Zui Finance bisa dipakai gratis?','Bisa, dengan paket Gratis: satu buku usaha, satu anggota, dan sampai 50 transaksi per bulan.'),
('Bagaimana memperbaiki jurnal yang salah?','Jurnal yang sudah dicatat tidak bisa diubah. Koreksi dilakukan dengan jurnal balik, sehingga riwayatnya tetap utuh.'),
('Mata uang apa yang didukung?','Rupiah, Ringgit Malaysia, dan Dolar AS. Kurs diatur secara manual.'),
('Apakah faktur bisa disimpan sebagai PDF?','Bisa. Faktur bisa dicetak atau disimpan sebagai PDF lengkap dengan logo usaha.')],
 rel=['erp','kontraktor','erp-art'])

ART['jurnal']=dict(
 seo='Zui Jurnal: Aplikasi Jurnal Pribadi, Rencana, dan Kebiasaan',
 h1='Zui Jurnal: rencana, proyek, tugas, catatan, dan kebiasaan pribadi',
 desc='Panduan Zui Jurnal: susun rencana dan proyek pribadi, pecah jadi tugas, catat suasana hati dan energi, bangun kebiasaan, manifestasi, dan pengingat ibadah harian.',
 lede='Zui Jurnal adalah ruang pribadi untuk mengatur diri: dari rencana besar sampai tugas hari ini, dari catatan perasaan sampai kebiasaan yang ingin dibangun.',
 kw='aplikasi jurnal pribadi, aplikasi rencana, habit tracker, jurnal suasana hati',
 sec=[
('apa','Apa itu Zui Jurnal','''<p><strong>Zui Jurnal</strong> adalah aplikasi jurnal dan perencanaan pribadi. Aplikasi ini dibuka dari <a href="https://jurnal.zuisystem.com" target="_blank" rel="noopener">jurnal.zuisystem.com</a> dan berdiri sendiri, dengan akun dan data yang terpisah dari aplikasi Zui lainnya.</p>
<div class="nt">Zui Jurnal bukan jurnal akuntansi. Untuk pembukuan usaha, lihat <a href="zui-finance.html">Zui Finance</a>.</div>'''),
('bagian','Bagian-bagiannya','''<div class="tw"><table><thead><tr><th>Bagian</th><th>Fungsi</th></tr></thead><tbody>
<tr><td><strong>Rencana</strong></td><td>Hal yang ingin dicapai, supaya pekerjaan harian punya arah.</td></tr>
<tr><td><strong>Proyek dan Tugas</strong></td><td>Kelompokkan tugas yang saling berkaitan, lalu tandai yang sudah selesai.</td></tr>
<tr><td><strong>Progres</strong></td><td>Target yang ingin Anda capai sedikit demi sedikit, dengan kemajuannya tercatat.</td></tr>
<tr><td><strong>Manifestasi</strong></td><td>Afirmasi, catatan syukur, bukti kecil yang menandakan niat bergerak, latihan 369, visualisasi, dan papan visi.</td></tr>
<tr><td><strong>Catatan</strong></td><td>Refleksi bebas atau pola pemicu dan respons, lengkap dengan suasana hati dan energi untuk melihat trennya.</td></tr>
<tr><td><strong>Hari ini</strong></td><td>Ringkasan fokus hari ini: tugas, kebiasaan, dan sesi yang perlu diselesaikan.</td></tr>
<tr><td><strong>Kewajiban</strong></td><td>Daftar ibadah harian. Untuk shalat, waktu dihitung dari lokasi dan metode perhitungan yang Anda pilih, dengan rekap 30 hari.</td></tr>
</tbody></table></div>'''),
('privat','Privasi dan pengingat','''<ul><li>Pasang <strong>PIN pengunci</strong> 4 sampai 6 angka agar isi jurnal tidak dibuka orang lain di perangkat Anda.</li>
<li>Atur <strong>pengingat harian</strong> pada jam yang Anda pilih.</li>
<li>Tersedia dalam Bahasa Indonesia dan English.</li></ul>'''),
('cocok','Cocok untuk siapa','''<ul><li>Pemilik usaha yang ingin memisahkan rencana pribadi dari data perusahaan.</li>
<li>Pekerja mandiri yang mengatur beberapa proyek dan tenggat sekaligus.</li>
<li>Siapa saja yang ingin membangun kebiasaan dan mencatat perkembangan diri.</li></ul>'''),
('paket','Uji coba dan paket','''<p>Akun baru mendapat masa percobaan 14 hari dengan semua fitur. Setelah masa percobaan atau masa paket berakhir ada tenggang 3 hari. Setelah itu data tetap tersimpan, tetapi hanya bisa dibaca sampai Anda berlangganan. Paket Starter, Pro, dan Bisnis diaktifkan setelah pembayaran dikonfirmasi, dengan harga yang ditampilkan di aplikasi.</p>'''),
('mulai','Cara mulai','''<ol><li>Buka <a href="https://jurnal.zuisystem.com" target="_blank" rel="noopener">jurnal.zuisystem.com</a> dan buat akun.</li>
<li>Tulis satu rencana, lalu buat proyek dan tugas pertamanya.</li>
<li>Buka tab Hari ini setiap pagi untuk melihat fokus Anda.</li></ol>'''),
 ],
 faq=[('Apakah Zui Jurnal sama dengan jurnal akuntansi?','Bukan. Zui Jurnal untuk rencana dan catatan pribadi. Untuk pembukuan usaha, gunakan Zui Finance.'),
('Apakah isi jurnal bisa dikunci?','Bisa. Pasang PIN pengunci 4 sampai 6 angka di Pengaturan.'),
('Apakah akun Zui Jurnal bisa dipakai di Zui ERP?','Tidak. Setiap aplikasi Zui punya akun sendiri.'),
('Apa yang terjadi setelah masa percobaan?','Ada tenggang 3 hari. Setelah itu data tetap tersimpan dan bisa dibaca, tetapi tidak bisa diubah sampai Anda berlangganan.')],
 rel=['todo','studikita','finance'])

ART['todo']=dict(
 seo='Zui To-Do: Aplikasi Daftar Tugas Harian dengan Papan dan Kalender',
 h1='Zui To-Do: daftar tugas harian dengan papan, kalender, dan target',
 desc='Panduan Zui To-Do: atur tugas di tampilan Hari ini, Papan, Kalender, dan Ringkasan, pakai kategori dan target, 8 tema, tiga bahasa, serta paket Starter, Pro, dan Bisnis.',
 lede='Zui To-Do membantu Anda menyelesaikan pekerjaan satu per satu. Lihat tugas hari ini, geser tugas di papan, dan pantau semuanya di kalender.',
 kw='aplikasi to do list, aplikasi daftar tugas, aplikasi kalender tugas, to-do list bahasa Indonesia',
 sec=[
('apa','Apa itu Zui To-Do','''<p><strong>Zui To-Do</strong> adalah aplikasi daftar tugas. Aplikasi ini dibuka dari <a href="https://todo.zuisystem.com" target="_blank" rel="noopener">todo.zuisystem.com</a> dan berdiri sendiri, dengan akun dan data yang terpisah dari aplikasi Zui lainnya.</p>'''),
('tampilan','Empat tampilan','''<ul><li><strong>Hari ini</strong>: tugas yang perlu diselesaikan hari ini.</li>
<li><strong>Papan</strong>: alur kerja berbentuk kolom. Seret kartu tugas ke kolom lain, atau pakai tombol panah.</li>
<li><strong>Kalender</strong>: tugas dilihat per tanggal.</li>
<li><strong>Ringkasan</strong>: gambaran kemajuan dan target.</li></ul>
<p>Tugas bisa diberi kategori, dan Anda bisa memasang target harian sampai tahunan. Semua menu, nama hari, dan nama bulan mengikuti bahasa pilihan Anda: Indonesia, Melayu, atau English.</p>'''),
('tema','Tema','''<p>Ada 8 tema siap pakai untuk semua paket: Zui, Laut, Hutan, Senja, Mawar, Lavender, Kopi, dan Grafit. Di paket Pro dan Bisnis, Anda bisa meracik tema sendiri: warna utama, warna penanda hari ini, latar, huruf, ukuran teks, dan sudut. Tema tersimpan di akun Anda.</p>'''),
('paket','Paket','''<div class="tw"><table><thead><tr><th>Paket</th><th>Isi</th></tr></thead><tbody>
<tr><td><strong>Starter</strong></td><td>Semua tampilan, target, sinkron antarperangkat, 8 tema, sampai 5 kategori.</td></tr>
<tr><td><strong>Pro</strong></td><td>Semua isi Starter, sampai 50 kategori, racik tema sendiri, dan ekspor CSV.</td></tr>
<tr><td><strong>Bisnis</strong></td><td>Semua isi Pro, cadangkan dan pulihkan data (JSON), dan prioritas chat.</td></tr>
</tbody></table></div>
<p>Akun baru mendapat uji coba 14 hari dengan semua fitur Bisnis, lalu tenggang 3 hari. Setelah itu tugas hanya bisa dibaca sampai Anda berlangganan. Pembayaran lewat QRIS (Rupiah) atau DuitNow (Ringgit). Harga ditampilkan di aplikasi.</p>'''),
('bantuan','Bantuan di dalam aplikasi','''<p>Zui To-Do punya halaman pertanyaan umum, syarat, kebijakan privasi, kelola langganan, dan chat dengan admin. Anda juga bisa membagikan tautan aplikasi ke teman lewat WhatsApp, Telegram, Facebook, X, LinkedIn, email, atau SMS.</p>'''),
('mulai','Cara mulai','''<ol><li>Buka <a href="https://todo.zuisystem.com" target="_blank" rel="noopener">todo.zuisystem.com</a> dan buat akun.</li>
<li>Buat beberapa kategori, misalnya Kerja, Rumah, dan Belajar.</li>
<li>Tambahkan tugas hari ini, lalu tandai selesai satu per satu.</li></ol>'''),
 ],
 faq=[('Apakah Zui To-Do bisa dipakai di HP?','Bisa. Zui To-Do dipasang dari peramban dan ikonnya muncul di layar utama HP.'),
('Bagaimana cara membayar langganan?','Pilih paket di Kelola langganan, bayar lewat QRIS atau DuitNow, lalu kirim nomor referensi. Paket aktif setelah pembayaran diperiksa.'),
('Bisakah data diekspor?','Bisa. Paket Pro bisa ekspor CSV, dan paket Bisnis bisa mencadangkan serta memulihkan data dalam format JSON.'),
('Apa bedanya dengan Zui Jurnal?','Zui To-Do fokus pada daftar tugas. Zui Jurnal mencakup rencana, catatan perasaan, kebiasaan, dan manifestasi.')],
 rel=['jurnal','studikita','erp'])

ART['studikita']=dict(
 seo='Studi Kita: Aplikasi Belajar untuk Jadwal, Catatan, dan Fokus',
 h1='Studi Kita: jadwal pelajaran, catatan, rencana ujian, dan waktu fokus',
 desc='Panduan Studi Kita: atur jadwal pelajaran, catat tugas dan materi, susun rencana ujian, dan belajar fokus dengan timer. Ada paket Gratis, Pelajar, Keluarga, dan Sekolah.',
 lede='Studi Kita membantu pelajar belajar lebih teratur. Jadwal, tugas, catatan, dan waktu fokus ada di satu aplikasi yang bisa dipakai di HP maupun komputer.',
 kw='aplikasi belajar, aplikasi jadwal pelajaran, aplikasi catatan pelajar, timer belajar',
 sec=[
('apa','Apa itu Studi Kita','''<p><strong>Studi Kita</strong> adalah aplikasi belajar untuk pelajar. Aplikasi ini dibuka dari <a href="https://studikita.zuisystem.com" target="_blank" rel="noopener">studikita.zuisystem.com</a> dan berdiri sendiri, dengan akun dan data yang terpisah dari aplikasi Zui lainnya.</p>'''),
('fitur','Fitur','''<ul><li><strong>Jadwal</strong>: jadwal pelajaran mingguan yang berulang otomatis.</li>
<li><strong>Kegiatan</strong>: catat tugas, ujian, dan ekskul dengan hitungan hari menuju tenggat.</li>
<li><strong>Catatan</strong>: simpan isi pelajaran per mata pelajaran dan cari dengan cepat.</li>
<li><strong>Rencana</strong>: susun target ke depan dan pantau tenggatnya.</li>
<li><strong>Fokus</strong>: timer belajar dan istirahat dengan target sesi harian.</li>
<li><strong>Alat bantu</strong>: kalkulator, dan terjemahan teks langsung di aplikasi.</li></ul>'''),
('akun','Dengan atau tanpa akun','''<p>Studi Kita bisa dipakai tanpa akun; datanya tersimpan di perangkat itu saja. Buat akun bila ingin data tersinkron di semua perangkat.</p>'''),
('paket','Paket','''<div class="tw"><table><thead><tr><th>Paket</th><th>Isi</th></tr></thead><tbody>
<tr><td><strong>Gratis</strong></td><td>Jadwal, kegiatan, rencana, timer fokus, kalkulator, terjemahan, dan sampai 30 catatan.</td></tr>
<tr><td><strong>Pelajar</strong></td><td>Catatan tanpa batas, ekspor catatan ke PDF, statistik fokus mingguan, dan warna tema eksklusif.</td></tr>
<tr><td><strong>Keluarga</strong></td><td>Sampai 3 anak. Orang tua memantau jadwal dan tugas, dan anak mendapat semua fitur Premium.</td></tr>
<tr><td><strong>Sekolah dan bimbel</strong></td><td>Guru membuat kelas, membagikan kode, lalu menambah tugas dan jadwal kelas.</td></tr>
</tbody></table></div>
<p>Harga terbaru tercantum di halaman Studi Kita.</p>'''),
('keluarga','Untuk orang tua dan guru','''<ul><li>Orang tua membuat grup di tab Grup dan membagikan kodenya ke anak. Orang tua hanya melihat jadwal, kegiatan, rencana, dan statistik fokus anak, <strong>bukan</strong> catatan pelajarannya.</li>
<li>Guru membuat kelas dan membagikan kode ke siswa. Guru mengirim tugas dan jadwal kelas, tetapi tidak bisa melihat data pribadi siswa.</li>
<li>Pengguna di bawah 18 tahun sebaiknya memakai aplikasi dengan sepengetahuan orang tua atau wali.</li></ul>'''),
('mulai','Cara mulai','''<ol><li>Buka <a href="https://studikita.zuisystem.com" target="_blank" rel="noopener">studikita.zuisystem.com</a>.</li>
<li>Isi jadwal pelajaran mingguan.</li>
<li>Catat tugas dan ujian terdekat, lalu mulai satu sesi fokus.</li></ol>'''),
 ],
 faq=[('Apakah Studi Kita gratis?','Ada paket Gratis dengan jadwal, kegiatan, rencana, timer fokus, dan sampai 30 catatan. Paket berbayar menambah catatan tanpa batas dan fitur lain.'),
('Apakah orang tua bisa membaca catatan anak?','Tidak. Orang tua hanya melihat jadwal, kegiatan, rencana, dan statistik fokus anak.'),
('Bisakah dipakai tanpa akun?','Bisa. Datanya tersimpan di perangkat itu saja. Buat akun agar data tersinkron di semua perangkat.'),
('Apakah guru bisa melihat data pribadi siswa?','Tidak. Guru hanya mengirim tugas dan jadwal kelas.')],
 rel=['todo','jurnal','erp-art'])
