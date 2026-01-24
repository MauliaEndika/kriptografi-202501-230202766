# Laporan Praktikum Kriptografi
Minggu ke-: 15  
Topik: Tinycoin  
Nama: Maulia Endika Putri  
NIM: 230202766  
Kelas: 5IKRA  

---

## 1. Tujuan
1. Mengembangkan proyek sederhana berbasis algoritma kriptografi.
2. Mendokumentasikan proses implementasi proyek ke dalam repository Git.
3. Menyusun laporan teknis hasil proyek akhir.

---

## 2. Dasar Teori
ERC20 adalah standar token di blockchain etherium yang menetapkan fungsi dan event tertentu supaya token bisa beroprasi secara seragam dengan dompet digital, bursa dan samrt contarct lainya. Dengan standar ini, token memiliki fitur dasar sperti memeriksa saldo, melakukan transfer, serta memberikan izin penggunaan token kepada piha lain

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
# Langkah 1 — Membuat Kontrak ERC20
Contoh kontrak sederhana TinyCoin.sol:

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        _mint(msg.sender, initialSupply);
    }
}

# Langkah 2 — Deploy Kontrak
Buka Remix IDE → buat file TinyCoin.sol.
Kompilasi dengan Solidity Compiler.
Deploy ke jaringan JavaScript VM atau testnet Ethereum.
Catat alamat kontrak hasil deployment.

# Langkah 3 — Uji Fungsionalitas
Cek saldo awal dengan fungsi balanceOf(address).
Lakukan transfer token dengan fungsi transfer(address, amount).
Uji apakah total supply tetap konsisten setelah transaksi.

# Langkah 4 — Dokumentasi
Simpan tangkapan layar proses deployment & transaksi.
Dokumentasikan alur kontrak (fungsi utama: constructor, mint, transfer).
Tambahkan analisis singkat tentang potensi keamanan smart contract (contoh: reentrancy, overflow – walaupun mitigasi sudah ada di Solidity >=0.8).

---

## 5. Source Code


```python
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        _mint(msg.sender, initialSupply);
    }
}
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
1. Fungsi utama ERC20 adalah menjadi standar umum untuk token di blockchain etherium, supaya token dapat berinteraksi dengan wallet, apliasi, dan platform lain secara konsisten dan mudah
2. Mekanisme transfer token di ERC20 melibatkan fungsu transfer yang digunakan untuk mengurangi saldo pengirim dan menambah saldo penerima, dan memicu event transfer untuk pencatatan dan tranparansi transaksi
3. Resiko utama smart contract adalah bug kode, celah keamanan dan overlow/underlow. Mitigasinya berupa audit kode, penggunaan pustaka yang sudah teruji, pengujian menyeluruh, dan pembaruan kontrak bila ditemukan masalah
---

## 8. Kesimpulan
TInyCoin ERC20 adalah token digital berbasis standar ERC20 ETherium yang memungkinkan transaksi aman dan transparan melalui smart contract, memanfaatkan interoperabilitas dan otomatisasi dalam ekosistem blockchain

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

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
