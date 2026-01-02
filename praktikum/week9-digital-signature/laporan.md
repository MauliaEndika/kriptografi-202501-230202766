# Laporan Praktikum Kriptografi
Minggu ke-: 9  
Topik: Digital Signature (RSA/DSA)
Nama: Maulia Endika Putri 
NIM: 230202766  
Kelas: 5 IKRA

---

## 1. Tujuan
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2. Memverifikasi keaslian tanda tangan digital.
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data

---

## 2. Dasar Teori
Digital Signature adalah teknik kriptografi yang berfungsi untuk menjamin keaslian pengirim, keutuhan data, dan non-repudiation dalam komunikasi digital. Proses penandatanganan dilakukan menggunakan kunci privat, sedangkan verifikasi menggunakan kunci publik, sehingga penerima dapat memastikan bahwa pesan berasal dari pihak yang sah dan tidak mengalami perubahan.

RSA dan DSA merupakan algoritma tanda tangan digital yang banyak digunakan. RSA bekerja dengan menandatangani nilai hash pesan menggunakan kunci privat dan keamanannya bergantung pada kesulitan faktorisasi bilangan besar, sedangkan DSA menggunakan perhitungan logaritma diskret dan bilangan acak rahasia dalam proses pembentukan tanda tangan.

Tanda tangan digital dengan RSA dan DSA  diterapkan pada berbagai sistem keamanan seperti TLS/SSL, S/MIME, dan sertifikat digital, serta berperan penting dalam menjaga keamanan dan kepercayaan pertukaran data pada jaringan terbuka.

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

```
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")
# Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
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
1. Perbedaan enkripsi RSA dan tanda tangan digital RSA
Enkripsi RSA bertujuan menjaga kerahasiaan pesan dengan menggunakan kunci publik penerima dan kunci privat untuk dekripsi. Sebaliknya, tanda tangan digital RSA digunakan untuk memastikan keaslian dan integritas pesan dengan memanfaatkan kunci privat pengirim dan diverifikasi melalui kunci publiknya.

2. Alasan tanda tangan digital menjamin integritas dan otentikasi
Integritas terjamin karena tanda tangan dibuat dari nilai hash pesan, sehingga perubahan data akan terdeteksi saat verifikasi. Otentikasi tercapai karena hanya pemilik kunci privat yang dapat menghasilkan tanda tangan yang sah.

3. Peran Certificate Authority (CA)
CA berfungsi sebagai pihak tepercaya yang mengaitkan identitas dengan kunci publik melalui sertifikat digital, sehingga memungkinkan verifikasi identitas dan mencegah pemalsuan atau serangan Man-in-the-Middle.
---

## 8. Kesimpulan
Digital Signature berbasis RSA dan DSA merupakan mekanisme kriptografi yang penting untuk menjamin keaslian pengirim, keutuhan data, dan non-repudiation dalam komunikasi digital. Dengan memanfaatkan pasangan kunci publik dan privat serta fungsi hash, tanda tangan digital memungkinkan verifikasi bahwa pesan benar-benar berasal dari pihak yang sah dan tidak mengalami perubahan. Dukungan sertifikat digital dan Certificate Authority semakin memperkuat keamanannya, sehingga Digital Signature RSA/DSA banyak digunakan pada berbagai sistem keamanan modern seperti TLS/SSL dan sertifikat digital.

---

## 9. Daftar Pustaka
- Rivest, R. L., Shamir, A., & Adleman, L. (1978). A Method for Obtaining Digital Signatures and Public-Key Cryptosystems. Communications of the ACM, 21(2), 120–126.
- National Institute of Standards and Technology (NIST). (2013). Digital Signature Standard (DSS). FIPS PUB 186-4.
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
