# Laporan Praktikum Kriptografi
Minggu ke-: 13  
Topik: TinyChain – Proof of Work (PoW  
Nama: Maulia Endika Putri  
NIM: 230202766
Kelas:5IKRA  

---

## 1. Tujuan
Menjelaskan peran hash function dalam blockchain, melakukan simulasi sederhana Proof of Work (PoW), menganalisis keamanan cryptocurrency berbasis kriptografi.

---

## 2. Dasar Teori
TinyChain adalah contoh sederhana dari teknologi blockchain yang digunakan sebagai alat untuk mempelajari konsep dasar blockchain. Salah satu mekanisme utama TinyChain adalah Proof of Work (PoW), metode konsensus yang dimaksudkan untuk secara aman memvalidasi transaksi dan menambahkan blok baru ke dalam rantai blok.Proof of Work bekerja dengan memaksa node atau penambang (miner) untuk menyelesaikan masalah komputasi tertentu, biasanya melalui pencarian nilai hash yang menyelesaikan masalah tertentu. Karena prosesnya membutuhkan banyak waktu dan sumber daya komputasi, orang jahat sulit memanipulasi data blockchain.

PoW digunakan oleh TinyChain untuk mensimulasikan proses diverifikasi blok sebelum ditambahkan ke blockchain. Ini memastikan bahwa setiap blok yang dibuat telah melalui proses validasi, menjaga integritas data, dan mencegah perubahan data yang tidak diinginkan dalam sistem blockchain

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Source Code

```import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")...
```
```
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Uji coba blockchain
my_chain = Blockchain()
print("Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))
```
---


## 7. Jawaban Pertanyaan
1. fungsi hash sangat penting dalam blockchain karena berfusngsi untuk menjaga intergritas dan keamanan data, fungsi hash sangat penting dalam blockchain. Hash dari blok sebelumnya membentuk rantai, yang membentuk rantai, yang membuatnya sulit untuk dimanipulasi atau dipalsukan. Hash fungsinya satu arah, sehingga data asli tidak dapat dengan mudah direntruksi dari nilai hash, dan konsisten dan unik, sehingga blockchain sulit untuk dimanipulasi atau dipalsukan
2. Proof of Work mewajibkan setiap transaksi melalui proses komputasi yang kompleks sebelum dimasukan ke dalam blockchain, mencegah pembelajaran berlebihan. Untuk menghasilkan blok yang sah, penambang harus menyelesaikan teka teki kriptografi. Karena proses ini membutuhkan banyak waktu dan sumber daya, satu transaksi hanya dapat dicatat dalam satu blok yang diakui oleh jaringan, jika ada upaya untuk menggandakan transaksi, jaringan akan menolaknya karena tidak sesuai dengan sejarah tervalidasi dan terpanjang blockchain. Akibatnya, transaksi ganda tidak dapat dikonfirmasi secara bermasamaan.
3. Salah satu kelemahan Proof of Work adalah pengunaan energi yang sangat tinggi. Meskipun hanya satu penambang yang akhirnya bershasil menambahakan blok, proses penambaangan membutuhkan perangkat keras untuk menyelesaikan perhitungan kriptografi. Akibatnya, banyak energi dibuang tanpa menghasilkan output langsung. Ini menyebabkan biaya operasional yang tinggi, jejak karbon yang signifikam, dan hasil yang kurang ramah lingkungan. Karena hal ini, mekanisme konsensus alternatif seperti Proof of Stake(PoS) yang lebih hemat energi muncul.
---

## 8. Kesimpulan
fungsi hash dan mekanisme Proof of Work (PoW) memiliki peran yang sangat penting dalam menjaga keamanan dan integritas sistem blockchain. Fungsi hash digunakan untuk mengamankan data dalam setiap blok serta membentuk keterkaitan antarblok sehingga data yang telah tercatat tidak dapat diubah tanpa memengaruhi seluruh rantai blockchain.

Simulasi TinyChain menunjukkan bagaimana Proof of Work bekerja melalui proses pencarian nilai nonce untuk menghasilkan hash dengan tingkat kesulitan tertentu. Proses ini membuktikan bahwa penambahan blok ke dalam blockchain memerlukan usaha komputasi yang signifikan, sehingga mempersulit terjadinya manipulasi data maupun serangan seperti double spending.

Namun demikian, mekanisme Proof of Work memiliki kelemahan utama berupa konsumsi energi yang tinggi dan efisiensi yang rendah. Hal ini mendorong pengembangan mekanisme konsensus alternatif seperti Proof of Stake (PoS) yang lebih ramah lingkungan. Meskipun begitu, PoW tetap menjadi fondasi penting dalam pengembangan awal teknologi blockchain dan cryptocurrency berbasis kriptografi.

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
Author: Maulia Endika Putri <mauliaendikaputrii@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
