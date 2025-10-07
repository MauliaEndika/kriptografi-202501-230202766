# Laporan Praktikum Kriptografi
Minggu ke-: 1
Topik: [Intro CIA]  
Nama: [Maulia Endika Putri]  
NIM: [230202766]  
Kelas: [5IKRA]  

---
**Sejarah Kriptografi**
1. Era Kriptografi Klasik
Kriptografi klasik adalah tahap awal dalam pengembangan metode penyandian yang bertujuan untuk menjaga kerahasiaan informasi, terutama dalam konteks militer dan diplomasi. Salah satu teknik yang paling awal dikenal adalah Caesar Cipher, yang diperkenalkan oleh Julius Caesar. Metode ini mengganti huruf dalam abjad untuk mengenkripsi pesan–misalnya, huruf A akan menjadi D jika terjadi pergeseran tiga huruf. Teknik ini mudah dipahami dan diterapkan, tetapi juga rentan terhadap analisis pola huruf yang dapat mengungkap isi pesan. Metode lain yang lebih rumit adalah Vigenère Cipher, yakni sistem substitusi polialfabetik yang menggunakan kata kunci untuk mengacak konten pesan. Teknik ini memberikan tingkat keamanan yang lebih baik dibandingkan Caesar Cipher, tetapi masih dapat diserang dengan analisis frekuensi. Meskipun sederhana, periode kriptografi klasik berfungsi sebagai fondasi penting bagi pengembangan prinsip-prinsip enkripsi, kunci rahasia, serta keamanan komunikasi di masa mendatang.

3. Perkembangan Kriptografi Modern
Dengan perkembangan teknologi komputer dan digitalisasi data, kriptografi telah mengalami transformasi signifikan menuju sistem yang lebih aman dan efektif. Kriptografi modern ditandai dengan munculnya algoritma kunci simetris dan asimetris yang menjadi acuan keamanan secara global. Salah satu algoritma simetris yang banyak diterapkan adalah Advanced Encryption Standard (AES), yang mengolah blok data berukuran 128 bit dengan kunci 128 hingga 256 bit. AES sering digunakan dalam komunikasi, penyimpanan data, serta perlindungan informasi sensitif berkat efisiensi dan tingkat keamanan yang tinggi. Sementara itu, algoritma Rivest–Shamir–Adleman (RSA) menjadi contoh utama dari kriptografi kunci publik, yang memungkinkan proses enkripsi dan tanda tangan digital dengan menggunakan sepasang kunci publik dan privat. Dengan sistem ini, komunikasi dapat dilakukan dengan aman tanpa memerlukan pertukaran kunci rahasia secara langsung. Kriptografi modern tidak hanya menekankan aspek kerahasiaan, tetapi juga mempertimbangkan integritas data, keaslian, dan anti-penyangkalan.

4. Evolusi Menuju Kriptografi Kontemporer
Dalam era digitalisasi dan desentralisasi, kriptografi telah berevolusi menjadi elemen penting dalam teknologi saat ini, terutama pada blockchain dan cryptocurrency. Teknologi blockchain menggunakan kriptografi untuk menjamin keamanan, verifikasi, dan pencatatan transaksi dengan cara yang transparan dan tidak dapat diubah. Setiap blok dalam rantai memiliki hash kriptografis yang menjaga integritas data dan mencegah manipulasi. Salah satu contoh paling terkenal adalah cryptocurrency seperti Bitcoin dan Ethereum, yang memanfaatkan tanda tangan digital serta algoritma hash untuk memastikan keamanan dan desentralisasi dalam sistem keuangan digital. Selain itu, kriptografi kontemporer juga mengarah pada perkembangan konsep-konsep inovatif seperti zero-knowledge proofs dan kriptografi pasca-kuantum, yang dirancang untuk menghadapi tantangan keamanan di era komputer kuantum.

**PRINSIP CIA**
Prinsip CIA dalam Keamanan Informasi
Dalam bidang keamanan informasi, ada tiga prinsip pokok yang menjadi landasan perlindungan data, yaitu Kerahasiaan, Keutuhan, dan Ketersediaan. Ketiga prinsip ini dikenal sebagai model CIA, berfungsi untuk melindungi keamanan, keandalan, dan kepercayaan terhadap sistem informasi.

Kerahasiaan
Prinsip ini menekankan bahwa informasi seharusnya hanya dapat diakses oleh orang-orang yang diberi izin. Tujuan utamanya adalah untuk melindungi data dari akses, penggunaan, atau pengungkapan oleh pihak yang tidak berwenang. Upaya untuk menjaga kerahasiaan dapat dilakukan dengan metode seperti enkripsi, penggunaan kata sandi, autentikasi ganda, dan kontrol akses berdasarkan peran. Sebagai contoh, data pengguna dalam aplikasi perbankan dilindungi dengan sistem login dan protokol keamanan SSL untuk mencegah kebocoran kepada pihak ketiga.

Keutuhan
Prinsip keutuhan menjamin bahwa data tetap benar, lengkap, dan tidak boleh mengalami perubahan tanpa izin selama penyimpanan atau pengiriman. Ini berarti data yang sampai harus identik dengan data yang dikirimkan, tanpa ada manipulasi atau modifikasi. Teknik seperti hashing, tanda tangan digital, dan sistem pengendalian versi digunakan untuk menjamin integritas. Contohnya, tanda tangan digital pada dokumen elektronik memastikan bahwa isi dokumen tetap tidak berubah setelah proses penandatanganan.

Ketersediaan
Prinsip ini menjamin bahwa sistem dan data selalu dapat diakses saat dibutuhkan oleh pengguna yang berwenang. Ketersediaan dijaga melalui pemeliharaan sistem, pencadangan data secara teratur, serta penerapan langkah-langkah keamanan seperti firewall dan sistem deteksi intrusi. Sebagai contoh, server layanan berbasis cloud harus beroperasi 24 jam sehari, 7 hari seminggu agar pengguna dapat mengakses data kapan saja diperlukan.

**QUIZ SINGKAT**
1. Siapa tokoh yang dianggap sebagai bapak kriptografi modern? Claude shannon (1916–2001)
2. Sebutkan algoritma kunci publik yang populer digunakan saat ini.
   RSA (Rivest–Shamir–Adleman) → digunakan untuk enkripsi dan tanda tangan digital.
   ECC (Elliptic Curve Cryptography) → menawarkan keamanan tinggi dengan ukuran kunci lebih kecil dibanding RSA.
   DSA (Digital Signature Algorithm) → digunakan khusus untuk tanda tangan digital.
   ElGamal → digunakan untuk enkripsi dan pertukaran kunci secara aman
3. Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
   Kriptografi klasik menggunakan teknik sederhana seperti Caesar Cipher dan Vigenère Cipher yang berbasis pergeseran huruf, sedangkan kriptografi modern              menggunakan algoritma matematika kompleks seperti AES dan RSA. Jika kriptografi klasik mudah dipecahkan, kriptografi modern jauh lebih aman karena melibatkan       kunci publik dan privat serta perhitungan komputasi yang sulit diuraikan.
--- **Dokumentasi**
   ![Setup GitHub](screenshots/repo_setup.png)

```
