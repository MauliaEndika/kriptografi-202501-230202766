# Laporan Praktikum Kriptografi
Minggu ke-: 12  
Topik: Aplikasi TLS & E-commerce 
Nama: Maulia Endika Putri 
NIM: 230202766
Kelas: 5IKRA  

---

## 1. Tujuan
1. Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
2. Menjelaskan enkripsi dalam transaksi e-commerce.
3. Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.

---

## 2. Dasar Teori
    TLS adalah protokol keamanan yang digunakan untuk melindungi komunikasi data melalui jaringan internet. TLS memiliki mekanisme enkripsi, autentikasi, dan integritas data untuk memastikan bahwa orang yang tidak berwenang tidak dapat mengakses atau mengubah data yang dikirimkan antara klien dan server.
    TLS sangat penting untuk aplikasi e-commerce karena transaksi online melibatkan data sensitif seperti informasi akun, kata sandi, dan detail pembayaran. Dengan menggunakan TLS, seluruh data transaksi dienkripsi, sehingga mengurangi kemungkinan penyadapan dan pencurian data.Protokol HTTPS menunjukkan implementasi TLS dalam e-commerce, meningkatkan kepercayaan pengguna. Selain melindungi kepentingan pelanggan dan penyedia layanan, keamanan komunikasi yang terjamin membuat transaksi menjadi lebih aman dan andal.
---

## 3. Hasil dan Pembahasan
Langkah 1
Website : Tokopedia
Menggunakan HTTPS (TLS aktif)
Sertifikat digital valid dan masih berlaku
Diterbitkan oleh Certificate Authority (CA) tepercaya
Menggunakan algoritma kriptografi yang kuat (RSA/AES, SHA-256)

Langkah 2.
    bagaimana enkripsi digunakan untuk melindungi transaksi online (misalnya saat login atau melakukan pembayaran). dalam website tokopedia?
Pada website Tokopedia, enkripsi digunakan untuk melindungi transaksi online melalui     penerapan protokol TLS (HTTPS). Saat pengguna melakukan login, data seperti email dan kata sandi dienkripsi selama proses transmisi sehingga tidak dapat dibaca oleh pihak lain di jaringan. Pada saat pembayaran, informasi sensitif seperti detail transaksi dan metode pembayaran juga dienkripsi menggunakan kunci sesi yang aman, sehingga hanya server Tokopedia yang dapat mendekripsi dan memproses data tersebut. Dengan mekanisme ini, risiko penyadapan, pencurian data, dan manipulasi transaksi dapat diminimalkan.
    Potensi ancaman jika TLS tidak digunakan
Jika TLS tidak digunakan, data yang dikirimkan antara pengguna dan server akan dikirim dalam bentuk plaintext, sehingga sangat rentan terhadap berbagai ancaman keamanan. Salah satu ancaman utama adalah serangan Man-in-the-Middle (MITM), di mana penyerang dapat menyadap, membaca, bahkan mengubah data yang sedang ditransmisikan tanpa sepengetahuan pengguna. Selain itu, tanpa TLS dapat terjadi pencurian akun, pemalsuan transaksi, serta kebocoran data pribadi dan finansial, yang berpotensi merugikan pengguna dan menurunkan tingkat kepercayaan terhadap layanan online.

Langkah 3.
    Identifikasi isu privasi dalam penggunaan email terenkripsi (PGP, S/MIME).
Meskipun penggunaan protokol email terenkripsi seperti PGP dan S/MIME melindungi isi pesan, ada beberapa masalah yang terkait dengan privasi. Metadata email, yang mencakup informasi seperti alamat pengirim, penerima, dan waktu pengiriman, yang biasanya tidak dienkripsi dan masih dapat dianalisis, merupakan masalah besar. Selain itu, mengelola kunci kriptografi membawa risiko, seperti penyimpanan kunci privat yang tidak aman atau akses oleh pihak lain. Organisasi yang memiliki akses ke sertifikat atau kunci dapat mengakses komunikasi pengguna tanpa sepengetahuan mereka, yang menimbulkan masalah privasi.
    
Ketika persyaratan keamanan bertentangan dengan hak privasi, muncul masalah etika terkait penggunaan komunikasi terenkripsi. Untuk melakukan dekripsi email karyawan untuk audit, perusahaan hanya dapat melakukannya secara terbatas, transparan, dan berdasarkan kebijakan resmi yang telah disetujui oleh karyawan, seperti untuk keamanan sistem atau kepatuhan hukum. Tindakan tersebut dapat melanggar privasi individu jika tidak ada kejelasan kebijakan. Sementara itu, dasar hukum yang jelas dan prosedur perizinan yang ketat diperlukan untuk mengatur pengawasan pemerintah terhadap komunikasi terenkripsi. Tanpa melemahkan sistem enkripsi yang dapat membahayakan keamanan data secara luas, pemerintah harus menyeimbangkan keamanan nasional dengan perlindungan privasi masyarakat.

---

## 4. Jawaban Pertanyaan
1. Salah satu perbedaan utama antara HTTP dan HTTPS adalah keamanannya. HTTP mengirimkan data tanpa enkripsi, sehingga orang lain dapat membacanya. Sebaliknya, HTTPS menggunakan protokol TLS untuk mengenkripsi data, yang membuat komunikasi lebih aman dan melindungi data dari penyadapan dan manipulasi.
2. Dalam komunikasi TLS, sertifikat digital sangat penting karena berfungsi untuk memverifikasi identitas server yang diakses pengguna. Sertifikat yang dikeluarkan oleh otoritas sertifikat (CA) yang dapat diandalkan membantu mencegah pemalsuan identitas dan memastikan bahwa koneksi benar-benar terhubung ke server yang sah
3. Dengan mengenkripsi data sehingga hanya pihak yang berwenang yang dapat mengaksesnya, kriptografi mendukung privasi dalam komunikasi digital. Namun, di sisi lain, kriptografi juga menimbulkan tantangan hukum dan etika karena dapat membatasi pengawasan perusahaan atau pemerintah. Akibatnya, diperlukan keseimbangan antara perlindungan privasi, keamanan, dan kepentingan hukum.
---

## 8. Kesimpulan
Dalam komunikasi digital, penggunaan TLS dan kriptografi sangat penting untuk menjaga keamanan dan privasi data, terutama pada layanan berbasis internet seperti e-commerce dan email. Perbedaan antara HTTP dan HTTPS menunjukkan bahwa enkripsi adalah komponen utama dalam melindungi data dari penyadapan dan manipulasi. Sertifikat digital sangat penting untuk menjamin keaslian identitas server, sehingga komunikasi dapat berlangsung secara aman dan tepercaya. Dibutuhkan kebijakan yang seimbang antara keamanan, privasi, dan kepatuhan hukum karena kriptografi, meskipun memberikan perlindungan privasi yang kuat, menimbulkan tantangan hukum dan etika terkait pengawasan dan akses data.

---

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
