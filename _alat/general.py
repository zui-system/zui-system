# Artikel umum (topik yang dicari di Google), masing-masing mengarah ke satu aplikasi.
GEN={}

GEN['cara-membuat-rab.html']=dict(app='kontraktor',
 seo='Cara Membuat RAB Proyek Bangunan: Langkah dan Contoh',
 h1='Cara membuat RAB proyek bangunan, langkah demi langkah',
 card='Komponen RAB, cara menghitung volume dan harga satuan, contoh perhitungan, dan kesalahan yang sering terjadi.',
 desc='Panduan membuat RAB (rencana anggaran biaya) proyek bangunan: komponen, cara menghitung volume dan harga satuan, contoh perhitungan, dan kesalahan yang sering terjadi.',
 lede='RAB yang rapi membuat penawaran lebih meyakinkan dan proyek lebih terkendali. Panduan ini menjelaskan cara menyusunnya dari nol, lengkap dengan contoh perhitungan.',
 kw='cara membuat RAB, contoh RAB bangunan, rencana anggaran biaya, RAB renovasi',
 sec=[
('pengertian','Apa itu RAB','''<p>RAB adalah singkatan dari <strong>rencana anggaran biaya</strong>: perkiraan seluruh biaya yang dibutuhkan untuk menyelesaikan sebuah pekerjaan konstruksi, dari persiapan sampai pembersihan akhir. RAB dipakai untuk menyusun penawaran ke klien, mengendalikan pengeluaran selama proyek, dan menjadi dasar tagihan per termin.</p>'''),
('komponen','Komponen RAB','''<ul><li><strong>Uraian pekerjaan</strong>: daftar pekerjaan yang dikelompokkan, misalnya persiapan, tanah dan pondasi, struktur, dinding, atap, lantai, pengecatan, dan instalasi.</li>
<li><strong>Volume</strong>: jumlah setiap pekerjaan dalam satuannya, misalnya m², m³, m', atau unit.</li>
<li><strong>Harga satuan</strong>: biaya untuk satu satuan pekerjaan, terdiri dari bahan, upah, dan alat.</li>
<li><strong>Jumlah harga</strong>: volume dikali harga satuan.</li>
<li><strong>Biaya umum dan keuntungan</strong>: biaya kantor, transportasi, dan margin usaha.</li>
<li><strong>Pajak</strong>: sesuai ketentuan yang berlaku dan kesepakatan dengan klien.</li></ul>'''),
('langkah','Langkah menyusun RAB','''<ol><li><strong>Pelajari gambar dan lakukan survei.</strong> Ukur lokasi, catat kondisi lapangan, dan pastikan lingkup pekerjaan yang diminta klien.</li>
<li><strong>Susun daftar pekerjaan.</strong> Urutkan sesuai tahap pengerjaan agar tidak ada yang terlewat.</li>
<li><strong>Hitung volume.</strong> Hitung dari gambar atau hasil ukur, lalu tulis cara hitungnya agar mudah diperiksa ulang.</li>
<li><strong>Tentukan harga satuan.</strong> Gunakan harga bahan dan upah terbaru di daerah proyek. Analisa harga satuan menghitung kebutuhan bahan, upah, dan alat untuk satu satuan pekerjaan.</li>
<li><strong>Kalikan dan jumlahkan.</strong> Volume × harga satuan untuk setiap baris, lalu jumlahkan per kelompok pekerjaan.</li>
<li><strong>Tambahkan biaya umum, keuntungan, dan pajak.</strong></li>
<li><strong>Periksa ulang.</strong> Bandingkan dengan proyek serupa yang pernah Anda kerjakan.</li></ol>'''),
('contoh','Contoh perhitungan','''<p>Contoh sederhana untuk pekerjaan dinding (semua angka hanya contoh):</p>
<div class="tw"><table><thead><tr><th>Pekerjaan</th><th>Volume</th><th>Harga satuan</th><th>Jumlah</th></tr></thead><tbody>
<tr><td>Pasangan dinding bata</td><td>50 m²</td><td>Rp 150.000</td><td>Rp 7.500.000</td></tr>
<tr><td>Plesteran dan acian</td><td>100 m²</td><td>Rp 70.000</td><td>Rp 7.000.000</td></tr>
<tr><td>Pengecatan</td><td>100 m²</td><td>Rp 35.000</td><td>Rp 3.500.000</td></tr>
<tr><td colspan="3"><strong>Subtotal</strong></td><td><strong>Rp 18.000.000</strong></td></tr>
</tbody></table></div>
<p>Plesteran dan pengecatan dihitung dua sisi dinding, sehingga volumenya 100 m². Detail kecil seperti ini yang paling sering terlewat.</p>'''),
('kesalahan','Kesalahan yang sering terjadi','''<ul><li>Memakai harga bahan lama, padahal harga sudah naik.</li>
<li>Lupa pekerjaan persiapan dan pembersihan akhir.</li>
<li>Tidak memperhitungkan material yang terbuang di lapangan.</li>
<li>Menghitung volume tanpa catatan cara hitung, sehingga sulit diperiksa.</li>
<li>Tidak memisahkan pekerjaan tambah dan kurang dari RAB awal.</li></ul>'''),
('aplikasi','Menyusun RAB di aplikasi','''<p>Menyusun RAB di spreadsheet bisa saja, tetapi RAB sering harus disambungkan ke penawaran, tagihan, dan pengeluaran proyek. <a href="zui-kontraktor.html">Zui Kontraktor</a> menyimpan survei, RAB, penawaran, dan tagihan dalam satu proyek, sehingga angka yang sama tidak diketik berulang. Angka tetap dihitung dari data yang Anda masukkan, jadi periksa kembali sebelum dikirim ke klien.</p>'''),
 ],
 faq=[('Apa bedanya RAB dan penawaran?','RAB adalah perhitungan biaya untuk kebutuhan internal. Penawaran adalah dokumen yang dikirim ke klien, biasanya disusun dari RAB.'),
('Dari mana mendapatkan harga satuan?','Dari harga bahan dan upah terbaru di daerah proyek, analisa harga satuan, dan catatan proyek sebelumnya.'),
('Apakah RAB bisa berubah saat proyek berjalan?','Bisa, misalnya karena pekerjaan tambah atau kurang. Catat perubahannya terpisah dan sepakati dengan klien.')],
 rel=['kontraktor','cara-membuat-laporan-laba-rugi.html','erp-art'])

GEN['cara-membuat-laporan-laba-rugi.html']=dict(app='finance',
 seo='Cara Membuat Laporan Laba Rugi Sederhana untuk UMKM',
 h1='Cara membuat laporan laba rugi sederhana untuk usaha kecil',
 card='Susunan laporan laba rugi, rumus laba kotor sampai laba bersih, contoh angka, dan tips agar datanya benar.',
 desc='Panduan membuat laporan laba rugi sederhana untuk UMKM: susunan laporan, rumus laba kotor dan laba bersih, contoh perhitungan, dan kesalahan yang perlu dihindari.',
 lede='Laporan laba rugi menjawab pertanyaan paling penting dalam usaha: bulan ini untung atau rugi, dan berapa besarnya. Berikut cara menyusunnya dengan sederhana.',
 kw='laporan laba rugi, cara membuat laporan laba rugi, contoh laporan laba rugi UMKM, laba bersih',
 sec=[
('pengertian','Apa itu laporan laba rugi','''<p>Laporan laba rugi merangkum <strong>pendapatan</strong> dan <strong>beban</strong> usaha dalam satu periode, misalnya satu bulan atau satu tahun. Selisihnya adalah laba (bila pendapatan lebih besar) atau rugi (bila beban lebih besar).</p>
<p>Laporan ini berbeda dari arus kas. Penjualan yang belum dibayar pelanggan sudah dihitung sebagai pendapatan, meskipun uangnya belum masuk.</p>'''),
('susunan','Susunan laporan','''<ol><li><strong>Pendapatan</strong>: hasil penjualan barang atau jasa.</li>
<li><strong>Harga pokok penjualan (HPP)</strong>: biaya barang yang terjual, misalnya harga beli barang dagangan atau bahan baku.</li>
<li><strong>Laba kotor</strong> = pendapatan − HPP.</li>
<li><strong>Beban operasional</strong>: gaji, sewa, listrik, transportasi, pemasaran.</li>
<li><strong>Laba operasional</strong> = laba kotor − beban operasional.</li>
<li><strong>Pendapatan dan beban lain</strong>: misalnya bunga bank.</li>
<li><strong>Laba bersih</strong>: hasil akhir setelah semua pos di atas, dan pajak bila ada.</li></ol>'''),
('contoh','Contoh perhitungan','''<p>Contoh usaha kecil dalam satu bulan (angka contoh):</p>
<div class="tw"><table><tbody>
<tr><td>Pendapatan penjualan</td><td>Rp 50.000.000</td></tr>
<tr><td>HPP</td><td>(Rp 30.000.000)</td></tr>
<tr><td><strong>Laba kotor</strong></td><td><strong>Rp 20.000.000</strong></td></tr>
<tr><td>Gaji karyawan</td><td>(Rp 8.000.000)</td></tr>
<tr><td>Sewa tempat</td><td>(Rp 3.000.000)</td></tr>
<tr><td>Listrik, air, internet</td><td>(Rp 1.000.000)</td></tr>
<tr><td><strong>Laba operasional</strong></td><td><strong>Rp 8.000.000</strong></td></tr>
</tbody></table></div>
<p>Dari contoh ini terlihat bahwa margin laba kotor 40%, tetapi setelah beban operasional, yang tersisa 16% dari penjualan.</p>'''),
('langkah','Langkah menyusunnya','''<ol><li>Catat semua transaksi selama periode itu, jangan hanya yang lewat rekening bank.</li>
<li>Kelompokkan transaksi ke akun: pendapatan, HPP, dan jenis-jenis beban.</li>
<li>Pisahkan uang pribadi dan uang usaha.</li>
<li>Jumlahkan per kelompok, lalu hitung laba kotor, laba operasional, dan laba bersih.</li>
<li>Bandingkan dengan bulan sebelumnya untuk melihat tren.</li></ol>'''),
('kesalahan','Kesalahan yang sering terjadi','''<ul><li>Mencampur pengeluaran pribadi dengan pengeluaran usaha.</li>
<li>Menghitung pembelian stok sebagai beban, padahal yang menjadi HPP hanya barang yang sudah terjual.</li>
<li>Lupa mencatat beban rutin kecil yang jumlahnya besar bila dikumpulkan.</li>
<li>Menganggap saldo kas sama dengan laba.</li></ul>'''),
('aplikasi','Membuat laporan otomatis','''<p>Bila setiap transaksi dicatat sebagai jurnal, laporan laba rugi bisa dibuat otomatis. <a href="zui-finance.html">Zui Finance</a> menyusun neraca saldo, laba rugi, posisi keuangan, dan arus kas dari jurnal yang Anda catat, dan bisa dimulai dengan paket Gratis.</p>'''),
 ],
 faq=[('Seberapa sering laporan laba rugi dibuat?','Paling tidak setiap bulan, agar masalah cepat terlihat. Laporan tahunan dibutuhkan untuk pajak dan pengajuan pinjaman.'),
('Apa bedanya laba kotor dan laba bersih?','Laba kotor adalah pendapatan dikurangi HPP. Laba bersih adalah sisa setelah semua beban, pendapatan dan beban lain, serta pajak.'),
('Apakah usaha kecil perlu laporan laba rugi?','Perlu. Tanpa laporan ini, sulit tahu apakah usaha benar-benar untung atau hanya uangnya berputar.')],
 rel=['finance','erp-art','cara-membuat-rab.html'])

GEN['tips-mengatur-jadwal-belajar.html']=dict(app='studikita',
 seo='Tips Mengatur Jadwal Belajar agar Konsisten dan Tidak Mudah Lelah',
 h1='Tips mengatur jadwal belajar agar konsisten',
 card='Cara menyusun jadwal belajar mingguan, membagi waktu tugas dan ujian, belajar fokus dengan sesi pendek, dan menjaga istirahat.',
 desc='Tips mengatur jadwal belajar untuk pelajar: susun jadwal mingguan, catat tenggat tugas dan ujian, belajar dengan sesi fokus pendek, ulangi materi berkala, dan jaga waktu istirahat.',
 lede='Belajar banyak tidak selalu berarti belajar lama. Jadwal yang teratur membantu materi masuk sedikit demi sedikit, tanpa menumpuk menjelang ujian.',
 kw='tips mengatur jadwal belajar, jadwal belajar efektif, cara belajar fokus, jadwal belajar pelajar',
 sec=[
('mingguan','1. Mulai dari jadwal mingguan','''<p>Tulis dulu kegiatan tetap: jam sekolah, les, ekskul, dan waktu bersama keluarga. Ruang kosong di antaranya adalah waktu belajar yang realistis. Jadwal yang berulang setiap minggu lebih mudah dijalankan daripada jadwal yang berubah setiap hari.</p>'''),
('tenggat','2. Catat tugas dan ujian beserta tenggatnya','''<p>Catat setiap tugas dan jadwal ujian begitu diumumkan. Hitung mundur dari tanggal tenggat: tugas besar dipecah menjadi beberapa bagian kecil, dan setiap bagian diberi hari sendiri.</p>'''),
('fokus','3. Belajar dalam sesi pendek','''<p>Banyak pelajar terbantu dengan sesi fokus pendek, misalnya 25 menit belajar lalu 5 menit istirahat. Saat sesi berjalan, jauhkan HP dari jangkauan atau matikan notifikasinya. Tentukan target jumlah sesi per hari, misalnya empat sesi.</p>'''),
('ulang','4. Ulangi materi secara berkala','''<p>Membaca ulang catatan beberapa hari setelah pelajaran membantu materi lebih melekat dibanding membaca semuanya sekaligus sehari sebelum ujian. Sisihkan waktu singkat setiap minggu untuk mengulang materi minggu itu.</p>'''),
('catatan','5. Simpan catatan per mata pelajaran','''<p>Catatan yang dikelompokkan per mata pelajaran lebih mudah dicari saat belajar untuk ujian. Tulis dengan kalimat sendiri, bukan sekadar menyalin.</p>'''),
('istirahat','6. Jaga waktu istirahat','''<p>Tidur yang cukup, makan teratur, dan waktu bermain tetap penting. Jadwal yang terlalu padat biasanya tidak bertahan lama.</p>'''),
('aplikasi','Membantu dengan aplikasi','''<p><a href="studi-kita.html">Studi Kita</a> menyediakan jadwal pelajaran mingguan yang berulang otomatis, catatan per mata pelajaran, daftar kegiatan dengan hitungan hari menuju tenggat, rencana ke depan, dan timer fokus dengan target sesi harian. Paket Gratis sudah bisa dipakai untuk memulai.</p>'''),
 ],
 faq=[('Berapa lama sebaiknya belajar setiap hari?','Tidak ada angka yang sama untuk semua orang. Mulai dari sesi pendek yang bisa dijalankan setiap hari, lalu tambah perlahan.'),
('Bagaimana kalau jadwal sering berantakan?','Kurangi target dan buat jadwal lebih longgar. Jadwal yang sederhana tetapi dijalankan lebih baik daripada jadwal sempurna yang ditinggalkan.'),
('Apakah belajar sambil mendengarkan musik boleh?','Sebagian orang terbantu, sebagian terganggu. Coba keduanya dan bandingkan hasilnya.')],
 rel=['studikita','cara-membuat-to-do-list.html','manfaat-menulis-jurnal-harian.html'])

GEN['cara-membuat-to-do-list.html']=dict(app='todo',
 seo='Cara Membuat To-Do List yang Efektif dan Benar-Benar Selesai',
 h1='Cara membuat to-do list yang efektif',
 card='Cara menulis tugas yang jelas, memecah pekerjaan besar, menentukan prioritas, dan meninjau daftar setiap hari.',
 desc='Cara membuat to-do list yang efektif: tulis tugas yang jelas, pecah pekerjaan besar, tentukan prioritas, batasi tugas utama harian, pakai papan alur kerja, dan tinjau setiap hari.',
 lede='Daftar tugas yang terlalu panjang justru membuat kewalahan. To-do list yang efektif pendek, jelas, dan diperbarui setiap hari.',
 kw='cara membuat to do list, to do list efektif, daftar tugas harian, tips produktif',
 sec=[
('jelas','1. Tulis tugas yang jelas','''<p>Tulis tugas sebagai tindakan yang bisa langsung dikerjakan. "Kirim penawaran ke Bu Rina" lebih jelas daripada "urusan penawaran".</p>'''),
('pecah','2. Pecah pekerjaan besar','''<p>Pekerjaan besar seperti "siapkan acara kantor" sulit dimulai. Pecah menjadi langkah kecil: pesan tempat, susun daftar tamu, kirim undangan. Setiap langkah bisa diselesaikan dalam sekali duduk.</p>'''),
('prioritas','3. Tentukan prioritas','''<p>Bedakan tugas yang penting dan yang mendesak. Kerjakan yang penting dan mendesak lebih dulu, jadwalkan yang penting tetapi tidak mendesak, dan pertimbangkan untuk mendelegasikan atau menghapus sisanya.</p>'''),
('tiga','4. Pilih tiga tugas utama setiap hari','''<p>Dari seluruh daftar, pilih tiga tugas yang paling berarti hari ini. Bila ketiganya selesai, hari itu sudah produktif meskipun daftar lain belum habis.</p>'''),
('papan','5. Pakai papan alur kerja','''<p>Untuk pekerjaan yang bertahap, bagi tugas ke kolom seperti "Belum", "Sedang", dan "Selesai". Menggeser kartu dari kolom ke kolom membuat kemajuan terlihat jelas.</p>'''),
('tinjau','6. Tinjau setiap hari','''<p>Luangkan lima menit di pagi atau malam hari untuk mencoret yang selesai, memindahkan yang tertunda, dan menyiapkan daftar besok.</p>'''),
('aplikasi','Membantu dengan aplikasi','''<p><a href="zui-todo.html">Zui To-Do</a> punya tampilan Hari ini, Papan untuk alur kerja, Kalender, dan Ringkasan, lengkap dengan kategori dan target harian sampai tahunan. Bisa dipakai dalam Bahasa Indonesia, Melayu, atau English.</p>'''),
 ],
 faq=[('Berapa banyak tugas yang ideal dalam satu hari?','Tergantung besarnya tugas. Mulailah dengan tiga tugas utama, lalu tambahkan tugas kecil bila masih ada waktu.'),
('Lebih baik di kertas atau aplikasi?','Keduanya bisa. Aplikasi memudahkan tugas berulang, pengingat tanggal, dan melihat kemajuan dari waktu ke waktu.'),
('Bagaimana kalau tugas terus tertunda?','Pecah tugas itu menjadi langkah yang lebih kecil, atau tanyakan apakah tugas itu memang perlu dikerjakan.')],
 rel=['todo','manfaat-menulis-jurnal-harian.html','tips-mengatur-jadwal-belajar.html'])

GEN['manfaat-menulis-jurnal-harian.html']=dict(app='jurnal',
 seo='Manfaat Menulis Jurnal Harian dan Cara Memulainya',
 h1='Manfaat menulis jurnal harian dan cara memulainya',
 card='Mengapa banyak orang menulis jurnal, apa saja yang bisa ditulis, dan cara memulai dalam lima menit sehari.',
 desc='Manfaat menulis jurnal harian: mengenali pola suasana hati, merapikan pikiran, mencatat rasa syukur, dan menjaga tujuan. Lengkap dengan cara memulai dan contoh pertanyaan.',
 lede='Menulis jurnal tidak harus panjang. Beberapa kalimat setiap hari sudah cukup untuk mengenal diri lebih baik dan menjaga arah tujuan.',
 kw='manfaat menulis jurnal, jurnal harian, cara menulis jurnal, journaling',
 sec=[
('manfaat','Manfaat yang sering dirasakan','''<ul><li><strong>Merapikan pikiran.</strong> Menuliskan hal yang mengganjal membantu melihatnya lebih jernih.</li>
<li><strong>Mengenali pola.</strong> Dengan mencatat suasana hati dan energi, Anda bisa melihat hari atau kegiatan apa yang membuat Anda lebih baik.</li>
<li><strong>Melatih rasa syukur.</strong> Mencatat beberapa hal baik setiap hari membantu memperhatikan sisi positif.</li>
<li><strong>Menjaga tujuan.</strong> Menulis rencana dan kemajuannya membuat tujuan tetap terlihat.</li>
<li><strong>Membangun kebiasaan.</strong> Mencatat kebiasaan harian membuat Anda tahu apakah sudah konsisten.</li></ul>
<p>Jurnal bukan pengganti bantuan profesional. Bila Anda merasa sangat tertekan dalam waktu lama, bicarakan dengan orang yang Anda percaya atau tenaga kesehatan.</p>'''),
('isi','Apa yang bisa ditulis','''<ul><li>Apa yang terjadi hari ini dan bagaimana perasaan Anda.</li>
<li>Satu sampai tiga hal yang Anda syukuri.</li>
<li>Pemicu yang membuat Anda kesal, dan bagaimana Anda meresponsnya.</li>
<li>Rencana besok dan satu hal yang paling ingin diselesaikan.</li></ul>'''),
('mulai','Cara memulai dalam lima menit','''<ol><li>Pilih waktu tetap, misalnya sebelum tidur.</li>
<li>Mulai dengan satu pertanyaan saja, misalnya "Apa yang berjalan baik hari ini?"</li>
<li>Tulis tanpa memikirkan tata bahasa.</li>
<li>Seminggu sekali, baca ulang catatan minggu itu.</li></ol>'''),
('privasi','Menjaga privasi jurnal','''<p>Jurnal berisi hal pribadi. Simpan di tempat yang hanya bisa Anda buka, misalnya buku yang disimpan sendiri atau aplikasi yang bisa dikunci.</p>'''),
('aplikasi','Menulis jurnal di aplikasi','''<p><a href="zui-jurnal.html">Zui Jurnal</a> menyediakan catatan refleksi bebas atau pemicu dan respons, pencatatan suasana hati dan energi beserta trennya, catatan syukur, kebiasaan, rencana, dan tugas. Isi jurnal bisa dikunci dengan PIN, dan pengingat harian bisa diatur pada jam yang Anda pilih.</p>'''),
 ],
 faq=[('Berapa lama sebaiknya menulis jurnal setiap hari?','Lima menit sudah cukup untuk memulai. Yang penting rutin, bukan panjang.'),
('Bagaimana kalau tidak tahu harus menulis apa?','Mulai dengan satu pertanyaan tetap, misalnya hal yang disyukuri hari ini.'),
('Apakah jurnal harus ditulis setiap hari?','Tidak harus. Beberapa kali seminggu pun bermanfaat, asalkan dilakukan dengan teratur.')],
 rel=['jurnal','cara-membuat-to-do-list.html','tips-mengatur-jadwal-belajar.html'])
