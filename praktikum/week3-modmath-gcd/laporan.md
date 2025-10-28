# Laporan Praktikum Kriptografi
Minggu ke-: 3 
Topik: Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit) 
Nama: Maulia Endika Putri
NIM: 230202766 
Kelas: 5IKRA

---

## 1. Tujuan
mampu menyelesaikan operasi aritmetika modular, menentukan bilangan prima serta menghitung GCD (Greatest Common Divisor), dan menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Dalam kriptografi, aritmetika modular digunakan untuk melakukan operasi matematika dalam ruang bilangan terbatas, seperti pada algoritma RSA dan Diffie-Hellman, agar hasil perhitungan tetap aman dan efisien. Bilangan prima berperan penting karena digunakan dalam pembentukan kunci rahasia; keamanan sistem kriptografi modern bergantung pada sulitnya memfaktorkan hasil perkalian dua bilangan prima besar. GCD (Greatest Common Divisor) digunakan dalam algoritma Euclidean untuk mencari invers modulo, yang dibutuhkan dalam proses pembangkitan kunci publik dan privat. Sedangkan logaritma diskrit merupakan kebalikan dari operasi perpangkatan dalam aritmetika modular dan menjadi dasar keamanan algoritma seperti Diffie-Hellman dan ElGamal, karena sulitnya menemukan nilai eksponen yang memenuhi persamaan modular tersebut.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Source Code
1. Aritmetika Modular
```
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))
2. GCD & Algoritma Euclidean
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))
3.Extended Euclidean Algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4
4.  Logaritma Diskrit (Discrete Log)
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4
5. 
~~~
---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
Kode pertama memperlihatkan cara melakukan operasi dasar seperti penjumlahan, perkalian, dan perpangkatan secara efisien dalam sistem modular. Proses ini merupakan fondasi untuk enkripsi dan dekripsi dalam algoritma seperti RSA. Selanjutnya, kode untuk menghitung GCD dan invers modular sangat penting dalam memastikan hubungan antara dua bilangan. GCD digunakan untuk mengecek apakah dua bilangan bersifat relatif prima, sementara invers modular memungkinkan pembalikan dari proses enkripsi ke dekripsi pada sistem dengan kunci publik. Tanpa invers modular, pesan yang telah dienkripsi tidak dapat didekripsi dengan benar. Akhirnya, kode yang berkaitan dengan logaritma diskrit menggambarkan betapa sulitnya menemukan eksponen 𝑥 dari persamaan 𝑎 𝑥 ≡ 𝑏 ( mod 𝑛) a x. Kesulitan ini menjadi dasar utama dari kekuatan keamanan algoritma seperti Diffie-Hellman. Secara keseluruhan, keempat kode ini menggambarkan hubungan yang erat antara konsep matematika dasar dengan implementasinya dalam menjaga keamanan informasi digital melalui kriptografi.

---

## 7. Jawaban Pertanyaan
1. Apa peran aritmetika modular dalam kriptografi modern? Aritmetika modular memungkinkan operasi matematis dilakukan dalam ruang bilangan terbatas, memastikan enkripsi dan dekripsi yang efisien dan aman dalam algoritma seperti RSA dan Diffie-Hellman.
2. Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)? Invers modular berfungsi untuk membalik proses enkripsi menjadi dekripsi. Dalam RSA, nilai invers modular digunakan untuk menghasilkan kunci privat dari kunci publik sehingga pesan yang dienkripsi hanya dapat dibuka oleh pihak yang memiliki kunci tersebut.
3. Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar? Logaritma diskrit sulit diselesaikan pada modulus besar karena tidak ada metode efisien untuk menemukan eksponen yang sesuai, sehingga masalah ini menjadi dasar kekuatan keamanan algoritma seperti Diffie-Hellman dan ElGamal.

---

## 8. Kesimpulan
Aritmetika Modular adalah metode perhitungan berdasarkan sisa bagi, yang memungkinkan operasi dilakukan dalam ruang bilangan terbatas. Ini sangat efisien untuk komputasi besar. GCD digunakan untuk memeriksa apakah dua bilangan relatif prima, yang penting untuk menghitung invers modular. Keduanya adalah dasar dari banyak algoritma kriptografi, seperti RSA dan Diffie-Hellman. Aritmetika modular mendukung enkripsi dan dekripsi berbasis pangkat modulo, sedangkan GCD membantu dalam memilih kunci publik dan menghitung invers modular. Logaritma diskrit sulit diselesaikan untuk modulus besar, yang memberikan dasar keamanan pada sistem seperti RSA dan ECC.

---

## 9. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Mauliaendikaputrii@gmail.com
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
