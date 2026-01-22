# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: Secret Sharing (Shamir’s Secret Sharing)
Nama: Maulia Endika Putri
NIM: 230202766
Kelas: 5IKRA  

---

## 1. Tujuan
1.Menjelaskan konsep Shamir Secret Sharing (SSS).
2.Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3.Menganalisis keamanan skema distribusi rahasia.

---

## 2. Dasar Teori
Dengan menggunakan metode kriptografi Shamir's Secret Sharing (SSS), informasi rahasia dibagi menjadi beberapa bagian (share) dan didistribusikan ke berbagai pihak. Metode ini menjamin bahwa informasi rahasia hanya dapat diketahui kembali apabila jumlah share yang dikumpulkan memenuhi batas minimum.
Metode ini didasarkan pada konsep interpolasi polinomial dan pertama kali diperkenalkan oleh Adi Shamir. Nilai rahasia disimpan sebagai konstanta dalam sebuah polinomial, dan polinomial tersebut kemudian dievaluasi beberapa kali untuk memberi masing-masing pihak bagian yang berbeda.
Keamanan Pembagian Rahasia Shamir tidak memberikan informasi tentang rahasia yang dilindungi karena prinsip bahwa polinomial hanya dapat direkonstruksi jika jumlah saham mencukupi.

---

## 3. Alat dan Bahan
(- Python 3.x
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Source Code
```
from secretsharing import SecretSharer

# Rahasia yang ingin dibagi
secret = "KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:", shares)

# Rekonstruksi rahasia dari 3 shares
recovered = SecretSharer.recover_secret(shares[:3])
print("Recovered secret:", recovered)

```
---

## 6. Hasil dan Pembahasan

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)


---

## 7. Jawaban Pertanyaan
1. Tingkat keamanan yang lebih tinggi adalah keunggulan utama Shamir Secret Sharing dibandingkan dengan pembagian salinan kunci secara langsung. Metode ini membuat kunci rahasia tidak disimpan atau dibagikan dalam bentuk utuh, tetapi dipecah menjadi beberapa bagian. Dengan demikian, jika salah satu pihak kehilangan atau bocor bagian mereka, rahasia tetap aman karena tidak dapat direkonstruksi tanpa memenuhi jumlah bagian yang minimal.
2. Threshold (k), jumlah minimum persentase yang diperlukan untuk mengembalikan rahasia asli, memastikan bahwa kerja sama sejumlah pihak diperlukan untuk mengakses rahasia, sehingga dapat mencegah akses ilegal dan meningkatkan kontrol keamanan dalam sistem pembagian rahasia.
3. Contoh penerapan Shamir Secret Sharing dapat ditemukan pada sistem manajemen kunci kriptografi di perusahaan atau organisasi besar. Kunci penting dibagi kepada beberapa pejabat, dan hanya dapat digunakan jika sejumlah pejabat tertentu bekerja sama, sehingga mengurangi risiko penyalahgunaan atau kebocoran data oleh satu pihak saja.
---

## 8. Kesimpulan
Dengan membagi kunci menjadi beberapa bagian, Shamir Secret Sharing meningkatkan keamanan penyimpanan dan pembagian informasi rahasia. Dengan adanya mekanisme batas, rahasia hanya dpat direkokontrusksi melalui kerja sama sejumlah orang tertentu, mengurangi kemungkinan kebocoran karena penyimpanan atau pembagian kunci secara langsung. Untuk sistem keamnan informasi, Shamir Secret Sharing sangat membantu karena mampu mencegah penyalahgunaan oleh satu pihak dan meningkatkan keandalan  dan perlindungan data rahasia

---

## 10. Commit Log

commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
