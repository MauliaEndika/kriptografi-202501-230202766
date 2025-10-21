# Laporan Praktikum Kriptografi
Minggu ke-: 2 
Topik: Crypto sistem  
Nama: Maulia Endika Putri
NIM: 230202766 
Kelas: 5IKRA 

---

## 1. Tujuan
mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma), menggambarkan proses enkripsi dan dekripsi sederhana, serta mengklasifikasikan jenis kriptosistem baik simetris maupun asimetris.

---

## 2. Dasar Teori
Kriptosistem merupakan suatu sistem yang berfungsi melindungi data dengan cara mengubah plaintext menjadi ciphertext lewat proses enkripsi, serta sebaliknya melalui dekripsi. Tujuan dari sistem ini adalah untuk melindungi kerahasiaan dan keaslian informasi agar hanya individu yang berwenang yang dapat mengaksesnya.

Elemen-elemen utama dalam kriptosistem meliputi plaintext, ciphertext, algoritma kriptografi, serta kunci. Tingkat keamanan sistem sangat ditentukan oleh kerahasiaan kunci yang diterapkan.

Secara umum, kriptosistem terbagi menjadi dua kategori, yaitu simetris (mengandalkan satu kunci yang sama untuk melakukan enkripsi dan dekripsi) dan asimetris (memanfaatkan dua kunci yang berbeda: kunci publik dan kunci privat).

---

## 3. Klasifikasi Simetris & Asimetris
Dalam kriptografi simetris, proses enkripsi dan dekripsi dilakukan dengan menggunakan satu kunci yang identik. Hal ini berarti bahwa pengirim dan penerima pesan perlu memiliki serta menjaga kerahasiaan kunci tersebut agar komunikasi tetap terlindungi. Keuntungan dari sistem ini adalah kecepatannya yang sangat tinggi karena algoritmanya sederhana dan efektif, sehingga sangat sesuai untuk mengenkripsi data dalam jumlah besar seperti file, database, atau komunikasi secara real-time. Namun, salah satu kelemahannya adalah dalam pengaturan distribusi kunci — jika kunci tersebut berhasil dicuri atau bocor saat dalam pengiriman, maka seluruh pesan yang dienkripsi dengan kunci itu bisa dengan mudah diakses oleh pihak yang tidak berhak. Dua algoritma terkenal yang menerapkan metode simetris adalah AES (Standar Enkripsi Lanjut) dan DES (Standar Enkripsi Data).

Di sisi lain, kriptografi asimetris menggunakan dua kunci yang berbeda, yaitu kunci publik dan kunci privat. Kunci publik dapat dibagikan secara bebas kepada siapapun untuk tujuan enkripsi, sementara kunci privat hanya diakses oleh pemilik dan digunakan untuk dekripsi. Dengan sistem ini, persoalan distribusi kunci dapat diatasi karena tidak perlu mengirimkan kunci rahasia melalui saluran komunikasi. Keuntungan utama dari kriptografi asimetris adalah tingkat keamanannya lebih tinggi saat bertukar data atau dalam proses otentikasi identitas, meskipun kecepatan prosesnya lebih lambat dibandingkan kriptografi simetris karena memerlukan perhitungan matematis yang lebih rumit. Contoh algoritma yang menerapkan pendekatan ini antara lain RSA (Rivest–Shamir–Adleman) dan ECC (Kriptografi Kurva Eliptik), yang sering digunakan dalam sistem keamanan modern seperti tanda tangan digital, sertifikat SSL, dan enkripsi data dalam komunikasi internet.

---

## 4. Pertanyaan Diskusi
1.Sebutkan komponen utama dalam sebuah kriptosistem
Jawab: Komponen utama dalam kriptosistem meliputi plaintext sebagai pesan asli, ciphertext sebagai hasil enkripsi, algoritma kriptografi sebagai aturan pengubahan data, kunci (key) sebagai elemen rahasia, serta proses enkripsi dan dekripsi untuk mengamankan dan mengembalikan pesan ke bentuk semula.
2.Apa kelebihan dan kelemahan sistem simetris dibandingkan asimetris?
Jawab: Sistem kriptografi simetris memiliki keuntungan karena cara enkripsi dan dekripsinya lebih cepat dan efisien bila dibandingkan dengan sistem asimetris, sehingga sangat sesuai untuk melindungi data dalam volume besar. Namun, kelemahannya terdapat pada tantangan dalam distribusi kunci, karena kunci yang sama harus dirahasiakan oleh kedua pihak yang berinteraksi. Di sisi lain, sistem asimetris menawarkan keamanan yang lebih tinggi dalam proses pertukaran kunci dengan memanfaatkan pasangan kunci publik dan privat, meskipun kecepatan prosesnya lebih lambat disebabkan oleh perhitungan yang lebih rumit.
3.Mengapa distribusi kunci menjadi masalah utama dalam kriptografi simetris? 
Distribusi kunci menjadi isu penting dalam kriptografi simetris karena kunci yang digunakan untuk melakukan enkripsi dan dekripsi adalah identik, sehingga dua pihak yang terlibat dalam komunikasi harus secara aman memiliki salinan kunci yang serupa. Apabila kunci tersebut terbongkar atau diintip saat proses pengiriman, orang yang tidak berwenang dapat mengakses seluruh pesan yang telah dienkripsi. Oleh sebab itu, memastikan keamanan dalam pengiriman dan penyimpanan kunci menjadi tantangan utama dalam sistem kriptografi simetris.

---
## 5. Hasil dan Pembahasan
![Hasil Eksekusi](screenshots/hasil_eksekusi.png)

