# Laporan Praktikum Kriptografi
Minggu ke-: 10
Topik: Public Key Infrastructure (PKI & Certificate Authority)
Nama: Maulia Endika Putri
NIM: 230202766 
Kelas: 5 IKRA 

---

## 1. Tujuan
1. Membuat sertifikat digital sederhana.
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).

---

## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah sistem keamanan yang mengelola penggunaan kunci publik dengan mengaitkannya pada identitas melalui sertifikat digital, sehingga komunikasi berbasis kriptografi kunci publik dapat berlangsung secara aman di jaringan terbuka.

Certificate Authority (CA) berperan sebagai pihak tepercaya dalam PKI yang menerbitkan dan mengelola sertifikat digital setelah melakukan verifikasi identitas pemilik kunci publik. Sertifikat ini mendukung proses enkripsi, autentikasi, dan tanda tangan digital.

PKI dan CA banyak digunakan pada berbagai layanan keamanan modern seperti TLS/SSL dan S/MIME. Melalui mekanisme rantai kepercayaan dan manajemen sertifikat, PKI memastikan keaslian identitas serta keamanan komunikasi digital.

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
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")
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
1. Verifikasi sertifikat HTTPS oleh browser
Browser memvalidasi sertifikat HTTPS dengan mengecek rantai kepercayaan hingga CA tepercaya, memastikan masa berlaku, kecocokan domain, dan keabsahan tanda tangan digital. Jika semua valid, koneksi dinyatakan aman.

2. Dampak CA palsu
CA palsu dapat digunakan untuk memalsukan identitas situs dan melakukan serangan Man-in-the-Middle. Namun, browser akan menolak sertifikat dari CA yang tidak tepercaya, dan CA yang terbukti bermasalah dapat dicabut dari sistem kepercayaan.

3. Pentingnya PKI
PKI berperan penting dalam menjamin keaslian identitas dan keamanan komunikasi digital. Tanpa PKI, transaksi online dan pertukaran data sensitif tidak dapat dilakukan secara aman.
---

## 8. Kesimpulan
Public Key Infrastructure (PKI) berperan sebagai dasar keamanan komunikasi digital dengan mengelola kunci publik dan memastikan keaslian identitas. Certificate Authority (CA) bertindak sebagai pihak tepercaya yang menerbitkan sertifikat digital untuk mendukung autentikasi dan enkripsi. Dengan demikian, PKI mengurangi risiko pemalsuan identitas dan serangan Man-in-the-Middle, serta menjadi komponen penting dalam layanan keamanan modern seperti HTTPS dan transaksi online.

---

## 9. Daftar Pustaka
- Adams, C., & Lloyd, S. (2003). Understanding PKI: Concepts, Standards, and Deployment Considerations. Addison-Wesley.
- Kahn Academy. (n.d.). Public Key Infrastructure (PKI).

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
