# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: Diffie-Hellman Key Exchange 
Nama: Maulia Endika Putri 
NIM: 230202766
Kelas: 5 IKRA

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).

---

## 2. Dasar Teori
Diffie–Hellman Key Exchange adalah metode kriptografi kunci publik yang memungkinkan dua pihak membentuk kunci rahasia bersama melalui jaringan publik secara aman. Algoritma ini diperkenalkan oleh Whitfield Diffie dan Martin Hellman pada tahun 1976 dan menjadi dasar penting dalam sistem keamanan komunikasi modern.

Mekanisme Diffie–Hellman memanfaatkan aritmetika modulo dan kompleksitas masalah logaritma diskret. Dengan menyepakati parameter publik dan menggunakan nilai rahasia masing-masing, kedua pihak dapat menghasilkan kunci yang sama tanpa perlu mengirimkan kunci rahasia tersebut. Keamanan metode ini bergantung pada kesulitan pihak ketiga untuk menurunkan kunci rahasia dari informasi publik, sehingga banyak diterapkan pada protokol keamanan seperti SSL/TLS dan VPN.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```Simulasi Diffie-Hellman
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Mengapa Diffie–Hellman dapat digunakan pada saluran publik?
Diffie–Hellman memungkinkan pertukaran kunci melalui saluran publik karena kunci rahasia tidak pernah dikirimkan secara langsung. Hanya nilai publik hasil perhitungan matematika yang dipertukarkan, sementara keamanan dijaga oleh sulitnya memecahkan masalah logaritma diskret.

2. Apa kelemahan utama Diffie–Hellman murni?
Kelemahan utama Diffie–Hellman murni adalah tidak adanya autentikasi, sehingga protokol ini rentan terhadap serangan Man-in-the-Middle (MITM), di mana penyerang dapat menyamar sebagai pihak yang sah.

3. Bagaimana mencegah serangan MITM?
Serangan MITM dapat dicegah dengan menambahkan mekanisme autentikasi, seperti sertifikat digital, tanda tangan digital, pre-shared key, atau sistem PKI, sehingga identitas pihak yang berkomunikasi dapat diverifikasi.
)
---

## 8. Kesimpulan
Diffie–Hellman adalah mekanisme pertukaran kunci yang memungkinkan dua pihak membentuk kunci rahasia bersama melalui saluran tidak aman. Keamanannya didasarkan pada operasi matematika pangkat modulo, sehingga nilai publik yang dipertukarkan tidak dapat digunakan untuk menurunkan kunci rahasia, meskipun dapat diakses oleh pihak lain.

Namun, Diffie–Hellman murni tidak menyediakan autentikasi, sehingga rentan terhadap serangan Man-in-the-Middle (MITM). Tanpa verifikasi identitas, penyerang dapat menyamar sebagai pihak yang sah dan membentuk kunci berbeda dengan masing-masing pihak.

Untuk mengatasi kelemahan tersebut, Diffie–Hellman perlu dikombinasikan dengan mekanisme autentikasi seperti tanda tangan digital atau sertifikat digital. Dengan autentikasi, keaslian kunci publik dapat diverifikasi sehingga pertukaran kunci berlangsung aman, sebagaimana diterapkan pada protokol TLS/HTTPS.

---

## 9. Daftar Pustaka
Diffie, W., & Hellman, M. (1976). New Directions in Cryptography. IEEE Transactions on Information Theory, 22(6), 644–654.

Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
