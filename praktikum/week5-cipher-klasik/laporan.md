# Laporan Praktikum Kriptografi
Minggu ke-: 5
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)
Nama: Maulia Endika Putri
NIM: 230202766 
Kelas: 5IKRA

---

## 1. Tujuan
menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi, menggunakan algoritma Vigenère Cipher dengan variasi kunci, mengimplementasikan algoritma transposisi sederhana, serta menjelaskan kelemahan yang terdapat pada algoritma kriptografi klasik.

---

## 2. Dasar Teori
a. Caesar Cipher
Caesar Cipher adalah metode kriptografi substitusi sederhana yang mengenkripsi pesan dengan menggeser setiap huruf plaintext sejumlah langkah tetap dalam alfabet.
Mekanisme
Setiap huruf digeser ke kanan atau kiri sesuai nilai shift.
Proses dekripsi dilakukan dengan menggeser huruf kembali ke posisi semula.
Kelebihan
Sangat mudah dipahami dan diimplementasikan.
Cocok sebagai pengenalan konsep dasar kriptografi.

b. Vigenère Cipher
Vigenère Cipher merupakan metode substitusi polialfabetik yang menggunakan kata kunci untuk menentukan besar pergeseran huruf pada plaintext.
Mekanisme
Kunci diulang sepanjang pesan.
Setiap huruf plaintext digeser berdasarkan nilai huruf pada kunci.
Dekripsi dilakukan dengan menggeser huruf ke arah sebaliknya menggunakan kunci yang sama.
Kelebihan
Lebih kuat dibanding Caesar karena pola pergeseran tidak tetap.
Mengurangi kemudahan analisis frekuensi.

c. Cipher Transposisi
Cipher transposisi mengubah posisi huruf tanpa mengganti bentuk huruf itu sendiri, sehingga menghasilkan susunan huruf yang tampak acak.
Mekanisme
Huruf plaintext ditata ke dalam pola tertentu (misalnya tabel).
Pesan dienkripsi dengan membaca huruf berdasarkan urutan baru.
Dekripsi mengembalikan huruf ke posisi asli sesuai aturan transposisi.
Kelebihan
Lebih sulit dipecahkan dibanding cipher substitusi sederhana karena pola huruf tidak berubah tetapi posisinya diacak.
Tetap mempertahankan struktur alfabet sehingga tidak memerlukan perhitungan kompleks.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan

Implementasi Caesar Cipher
```def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
Implementasi Vigenère Cipher
```
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

```
Implementasi Transposisi Sederhana
```
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

---

## 5. Hasil dan Pembahasan
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

## 6. Jawaban Pertanyaan
1. Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher? Kelemahan utama Caesar Cipher adalah ruang kuncinya sangat kecil sehingga mudah dipecahkan dengan brute force atau analisis frekuensi. Vigenère Cipher meskipun lebih kuat, tetap lemah jika panjang kuncinya pendek, karena pola pergeseran dapat dianalisis menggunakan metode seperti Kasiski test sehingga kunci dapat ditebak.
2. Mengapa cipher klasik mudah diserang dengan analisis frekuensi? Cipher klasik mudah diserang analisis frekuensi karena mereka mempertahankan pola kemunculan huruf dari bahasa asli. Pola ini dapat dikenali oleh penyerang, sehingga struktur bahasa dan huruf yang paling sering muncul dapat digunakan untuk membongkar ciphertext tanpa mengetahui kuncinya.
3. Bandingkan kelebihan dan kelemahan cipher substitusi vs transposisi.
Cipher substitusi mengubah setiap huruf menjadi huruf lain.
Kelebihan: Lebih sulit ditebak dibanding Caesar sederhana, dapat menggunakan banyak variasi.
Kelemahan: Masih mempertahankan frekuensi huruf, sehingga rentan terhadap analisis frekuensi.
Cipher transposisi hanya menukar posisi huruf tanpa mengubah bentuk huruf.
Kelebihan: Tidak mempertahankan pola posisi asli sehingga struktur pesan lebih acak.
Kelemahan: Jika pola transposisi diketahui, pesan dapat dipulihkan dengan mudah; serta sering tidak sekuat substitusi jika digunakan sendirian.

---

## 7. Kesimpulan
Cipher klasik bermanfaat sebagai dasar pembelajaran kriptografi, namun tidak aman karena pola bahasa masih terlihat dan mudah diserang dengan analisis frekuensi. Kelemahan ruang kunci kecil dan pola yang mudah ditebak membuat algoritma klasik tidak cocok untuk keamanan modern.

---

## 8. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Maulia Endika Putri <mauliaendikaputrii@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
