# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik:  Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit) 
Nama: Maulia Endika Putri 
NIM: 230202766
Kelas: 5IKRA  

---

## 1. Tujuan
menyelesaikan operasi aritmetika modular, menentukan bilangan prima serta menghitung GCD, dan menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Dalam bidang kriptografi, matematika modular merupakan pondasi utama dalam proses mengenkripsi dan mendekripsi data.
Aritmetika modular adalah cara menghitung dengan batas tertentu, disebut modulus.
Hasil dari operasi seperti tambah, kali, atau pangkat selalu berada dalam rentang 0 hingga n−1. Konsep ini memastikan hasil tetap stabil meskipun menggunakan bilangan yang sangat besar, dan sering digunakan dalam algoritma seperti RSA dan Diffie-Hellman.
FPB atau GCD adalah cara untuk mencari bilangan terbesar yang bisa membagi dua angka tanpa menyisakan sisa.
Dalam kriptografi, FPB digunakan untuk memastikan dua bilangan memiliki faktor bersama hanya 1, yang merupakan syarat penting dalam pembuatan kunci enkripsi.
Bilangan prima adalah bilangan yang hanya bisa dibagi oleh 1 dan bilangan itu sendiri.
Bilangan prima yang besar digunakan dalam sistem enkripsi karena sulit difaktorkan, sehingga memperkuat keamanan sistem seperti RSA.
Logaritma diskrit adalah kebalikan dari operasi perpangkatan dalam sistem modular.
Masalah logaritma diskrit dianggap sulit untuk dipecahkan, terutama ketika modulusnya besar, sehingga menjadi dasar keamanan algoritma seperti Diffie-Hellman dan ElGamal.
Secara keseluruhan, keempat konsep ini saling terkait dan menjadi dasar penting dalam membangun sistem kriptografi modern yang aman dan efisien.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Source Code
1. Aritmatika modular
```
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))
```
2. GCD & Algoritma Euclidean
```
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))
```
3. Extended Euclidean Algorithm
```
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
```
4. Logaritma Diskrit (Discrete Log)
```
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4
```
---

## 5. Hasil dan Pembahasan
Kode pertama memperlihatkan bagaimana operasi dasar seperti penjumlahan, perkalian, dan perpangkatan dapat dilakukan secara efisien dalam sistem aritmetika modular. Operasi ini menjaga hasil perhitungan tetap dalam batas tertentu (modulus) dan menjadi dasar utama dalam proses enkripsi serta dekripsi pada algoritma kriptografi seperti RSA.

Selanjutnya, kode GCD dan invers modular memiliki peran penting dalam memastikan keterkaitan antarbilangan. GCD digunakan untuk memeriksa apakah dua bilangan bersifat relatif prima, yang menjadi syarat utama dalam pembentukan kunci kriptografi. Sementara itu, invers modular memungkinkan proses pembalikan dari enkripsi menjadi dekripsi pada sistem kunci publik — tanpa adanya invers modular, pesan yang telah dienkripsi tidak dapat dikembalikan ke bentuk semula.

Kemudian, kode logaritma diskrit menunjukkan tingkat kesulitan dalam mencari nilai eksponen 𝑥 dari persamaan 𝑎 𝑥 ≡ 𝑏 ( mod 𝑛) a x ≡b(modn). Kompleksitas perhitungan ini menjadi dasar keamanan algoritma seperti Diffie–Hellman dan ElGamal, karena sangat sulit diselesaikan jika modulusnya besar.

Secara keseluruhan, hasil dari keempat kode tersebut menunjukkan keterkaitan erat antara konsep matematika dasar dan penerapannya dalam kriptografi. Melalui operasi modular, GCD, invers modular, dan logaritma diskrit, sistem kriptografi modern mampu melindungi kerahasiaan dan keaslian data digital secara efektif.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Apa peran aritmetika modular dalam kriptografi modern? Aritmetika modular menjadi dasar utama dalam kriptografi karena memungkinkan operasi matematika seperti penjumlahan, perkalian, dan perpangkatan dilakukan dengan hasil yang terbatas oleh modulus. Prinsip ini digunakan dalam algoritma seperti RSA dan Diffie-Hellman untuk menjaga hasil perhitungan tetap aman dan efisien.
2. Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)? Invers modular digunakan untuk membalikkan proses enkripsi menjadi dekripsi. Dalam algoritma RSA, nilai invers modular menentukan kunci privat, yang memungkinkan pesan terenkripsi dikembalikan ke bentuk aslinya. Tanpa invers modular, proses dekripsi tidak dapat dilakukan.
3. Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar? Logaritma diskrit sulit diselesaikan karena tidak ada metode cepat untuk mencari nilai eksponen 
𝑥 pada persamaan ax≡b(modn)
---

## 8. Kesimpulan
Aritmetika modular adalah cara menghitung yang berdasarkan sisa dari pembagian, di mana setiap operasi dilakukan dalam batas nilai tertentu yang disebut modulus. Sistem ini memastikan hasil perhitungan tetap dalam rentang bilangan yang terbatas, sehingga lebih efisien ketika digunakan untuk menghitung angka yang besar. Dalam kriptografi, aritmetika modular digunakan dalam proses enkripsi dan dekripsi yang melibatkan perpangkatan modulo, seperti pada algoritma RSA dan Diffie–Hellman.

GCD (Greatest Common Divisor) digunakan untuk mengetahui apakah dua bilangan saling relatif prima, yaitu tidak memiliki faktor yang sama selain 1.
Hal ini penting karena hanya bilangan yang saling relatif prima yang bisa digunakan untuk menghitung invers modular. Invers modular berfungsi sebagai penghubung antara kunci publik dan kunci privat, sehingga pesan yang telah dienkripsi dapat dikembalikan ke bentuk aslinya secara tepat.

Sementara itu, logaritma diskrit menjelaskan kesulitan dalam mencari nilai eksponen x dari persamaan ax ≡ b (mod n).
Untuk modulus yang besar, tidak ada algoritma yang efisien untuk menyelesaikan masalah ini secara cepat. Kompleksitasnya itulah yang menjadi dasar keamanan dalam berbagai algoritma kriptografi modern seperti RSA, Diffie–Hellman, dan Elliptic Curve Cryptography (ECC).

---

## 9. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Maulia Endika Putri <mauliaendikaputrii@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
