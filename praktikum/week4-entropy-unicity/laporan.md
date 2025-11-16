# Laporan Praktikum Kriptografi
Minggu ke-: 4
Topik: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)
Nama: Maulia Endika Putri
NIM: 230202766
Kelas: 5IKRA

---

## 1. Tujuan
menyelesaikan perhitungan sederhana terkait entropi kunci, menggunakan teorema Euler untuk perhitungan modular dan invers, menghitung unicity distance pada ciphertext, menganalisis kekuatan kunci berdasarkan entropi serta unicity distance, dan mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
Entropi merupakan ukuran tingkat keacakan atau ketidakteraturan dalam suatu sistem. Secara sederhana, entropi menjelaskan seberapa besar ketidakpastian yang dimiliki sebuah sistem. Semakin tinggi nilai entropi, semakin sulit sistem tersebut diprediksi dan semakin acak perilakunya. Dalam kriptografi, entropi menggambarkan berapa banyak informasi (dalam satuan bit) yang diperlukan untuk merepresentasikan sebuah kunci. Nilai entropi biasanya dihitung menggunakan konsep yang diperkenalkan oleh Claude Shannon (1948):
H(X) = –∑ pi log₂ pi.

Makna Entropi dalam Kriptografi:
a. Ketika setiap kunci memiliki peluang yang sama untuk muncul, nilai entropi mencapai tingkat maksimum. Misalnya, sebuah kunci 8 bit memiliki 256 kemungkinan nilai, sehingga entropinya adalah: H = log₂ 256 = 8 bit.
b. Entropi yang rendah menunjukkan bahwa kunci kurang acak, sehingga lebih mudah ditebak, terutama jika kunci berasal dari kebiasaan manusia, seperti kata sandi yang umum digunakan.

Hubungan dengan Brute Force
Serangan brute force adalah teknik mencoba seluruh kombinasi kunci satu per satu sampai menemukan kunci yang benar. Kemampuan bertahan sebuah kunci terhadap brute force bergantung pada banyaknya kemungkinan kunci, yang dapat ditulis sebagai: N = 2ᴴ. Semakin besar nilai entropi (H), semakin banyak kombinasi yang harus diuji, dan semakin lama waktu yang dibutuhkan untuk melakukan brute force.

Unicity Distance (UD) merupakan jumlah minimum ciphertext yang diperlukan agar hanya tersisa satu kunci yang mungkin cocok dengan pesan terenkripsi tersebut. Dengan kata lain, unicity distance menunjukkan seberapa banyak data yang dibutuhkan agar sebuah kriptosistem dapat diuraikan secara teoretis melalui analisis statistik. Konsep ini diperkenalkan oleh Claude Shannon dan dirumuskan sebagai:
U = H(K) / R,
dengan:
– U = unicity distance (dinyatakan dalam karakter atau bit pesan),
– H(K) = entropi kunci atau jumlah informasi yang terkandung dalam kunci,
– R = redundansi pesan atau tingkat pengulangan informasi dalam plaintext.

---

## 3. Source Code
```
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")
```
```
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))
```
```
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
```
---
Hasil eksekusi program

---

## 4. Jawaban Pertanyaan
1. Apa arti dari nilai entropy dalam konteks kekuatan kunci?
Nilai entropy menunjukkan tingkat keacakan atau ketidakpastian suatu kunci. Semakin tinggi entropy, semakin besar jumlah kemungkinan kombinasi kunci, sehingga kunci menjadi lebih sulit ditebak atau dipecahkan. Dalam konteks keamanan, entropy yang tinggi berarti kunci memiliki kekuatan yang lebih besar terhadap serangan brute force maupun serangan statistik karena penyerang harus mencoba lebih banyak kemungkinan.
2. Mengapa unicity distance penting dalam menentukan keamanan suatu cipher?
Unicity distance penting karena menentukan seberapa banyak ciphertext yang diperlukan untuk menemukan satu-satunya kunci yang cocok dengan pesan terenkripsi. Jika jumlah ciphertext yang tersedia kurang dari unicity distance, maka banyak kunci masih mungkin menghasilkan ciphertext yang sama, sehingga cipher tetap aman dari analisis statistik. Nilai unicity distance yang tinggi menunjukkan cipher lebih sulit dipecahkan karena membutuhkan lebih banyak data sebelum penyerang dapat mengidentifikasi kunci yang benar.
3. Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat?
Brute force tetap menjadi ancaman karena metode ini tidak bergantung pada kelemahan algoritma, melainkan pada percobaan seluruh kombinasi kunci. Meskipun algoritma kriptografi modern kuat secara teori, brute force tetap efektif terhadap kunci yang terlalu pendek, implementasi yang salah, penggunaan kata sandi lemah, atau ketika daya komputasi penyerang meningkat. Dengan kata lain, keamanan tidak hanya bergantung pada algoritma, tetapi juga pada panjang kunci, kualitas random number generator, dan cara algoritma tersebut digunakan.
---

## 5. Kesimpulan
Entropy menunjukkan tingkat keacakan kunci sehingga semakin tinggi entropy, semakin sulit kunci ditebak. Unicity distance menentukan jumlah ciphertext yang dibutuhkan untuk memastikan satu kunci yang benar, sehingga semakin besar nilainya, semakin aman cipher dari analisis statistik. Meskipun algoritma kriptografi kuat, brute force tetap menjadi ancaman jika kunci lemah, terlalu pendek, atau implementasinya tidak aman.

---

## 10. Commit Log
```
commit abc12345
Author: Maulia Endika Putri <mauliaendikaputrii@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
