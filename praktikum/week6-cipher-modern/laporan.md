# Laporan Praktikum Kriptografi
Minggu ke-: 6
Topik: Cipher Modern (DES, AES, RSA)
Nama: Maulia Endika Putri  
NIM: 230202766  
Kelas: 5IKRA

---

## 1. Tujuan
mengimplementasikan algoritma DES untuk blok data sederhana, menerapkan AES dengan kunci 128 bit, serta menjelaskan proses pembangkitan kunci publik dan privat pada RSA.

---

## 2. Dasar Teori
Cipher modern merupakan algoritma kriptografi yang digunakan untuk mengamankan data digital dengan tingkat keamanan yang jauh lebih kuat dibanding cipher klasik. DES (Data Encryption Standard) adalah algoritma enkripsi simetris berbasis blok 64-bit yang menggunakan kunci 56-bit, bekerja melalui 16 putaran Feistel namun kini dianggap kurang aman karena panjang kunci yang kecil. AES (Advanced Encryption Standard) merupakan algoritma simetris generasi baru yang menggunakan ukuran blok 128-bit dan kunci 128/192/256 bit, memberikan keamanan tinggi, efisiensi, serta menjadi standar global untuk enkripsi data. Sementara itu, RSA adalah algoritma kriptografi kunci publik yang menggunakan pasangan kunci publik dan privat berdasarkan konsep faktorisasi bilangan prima besar, sehingga banyak digunakan untuk enkripsi, autentikasi, dan digital signature. Ketiga algoritma ini menjadi fondasi utama keamanan informasi modern karena tingkat perlindungan data yang kuat pada berbagai aplikasi digital.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 5. Source Code
1. Implementasi DES (Opsional, Simulasi)
```python
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
```
2. Implementasi AES-128
```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128 bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
3. Implementasi RSA
```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
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
1. Apa perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan? DES dan AES adalah cipher simetris yang menggunakan kunci yang sama untuk enkripsi dan dekripsi, sedangkan RSA adalah cipher asimetris yang memakai kunci publik dan kunci privat. DES memiliki kunci pendek (56-bit) sehingga mudah dibobol, AES memiliki kunci kuat (128–256 bit), sedangkan keamanan RSA bergantung pada sulitnya memfaktorkan bilangan prima besar.
2. Mengapa AES lebih banyak digunakan dibanding DES di era modern? Karena AES jauh lebih aman, memiliki ukuran kunci lebih besar, lebih efisien, dan tahan brute force, sementara DES dianggap tidak aman karena kunci 56-bit dapat ditembus komputer modern.
3. Mengapa RSA dikategorikan sebagai algoritma asimetris, dan bagaimana proses pembangkitan kuncinya? RSA disebut asimetris karena menggunakan dua kunci berbeda, yaitu kunci publik untuk enkripsi dan kunci privat untuk dekripsi. Kuncinya dibuat dengan memilih dua bilangan prima besar, menghitung modulus n, menentukan nilai e (public exponent), lalu menghitung d (private exponent) yang menjadi kunci privat.

---

## 8. Kesimpulan
Algoritma kriptografi modern seperti DES, AES, dan RSA menjadi fondasi penting dalam pengamanan data digital. DES kini dianggap tidak aman karena ukuran kuncinya kecil, sementara AES menjadi standar utama karena tingkat keamanan dan efisiensinya yang tinggi. RSA berperan sebagai algoritma asimetris yang memungkinkan pertukaran kunci dan autentikasi secara aman melalui penggunaan kunci publik dan privat. Secara keseluruhan, kombinasi algoritma simetris dan asimetris ini membentuk sistem keamanan informasi yang kuat dan banyak digunakan di berbagai aplikasi teknologi modern.

---

## 9. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Maulia Endika Putri <Mauliaendikaputrii@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
