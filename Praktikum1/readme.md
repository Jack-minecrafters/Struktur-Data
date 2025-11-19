# Implementasi Queue pada Python
Queue itu kalau diterjemahkan simpel saja: antrian. Gambarannya gampang, kayak barisan orang di kafe, siapa yang datang duluan, dia yang dilayani lebih dulu. Program kecil ini nunjukkin cara kerja struktur data Queue di Python dengan memanfaatkan list sebagai tempat nyimpan datanya. Prinsipnya FIFO (First In, First Out), jadi elemen yang masuk paling awal bakal keluar terlebih dulu. Dengan begitu, alurnya tetap rapi dan masuk akal saat data dikelola.

### Kode Program
---
```
queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# Dequeue
element = queue.pop(0)
print("Dequeue: ", element)

# Peek
frontElement = queue[0]
print("Peek: ", frontElement)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))
```
### Penjelasan
---
1. Inisalisasi "wadah queue":
```
queue = []
```
---
Bayangkan kamu lagi buka jalur antrian yang benar-benar kosong. Belum ada satu pun orang di dalamnya. Kita tinggal bikin variabel queue dan ngasih nilai berupa list kosong []. Itu tandanya antriannya masih bersih, belum terisi apa pun, dan nanti bisa diisi lewat operasi seperti enqueue.

2. Enqueue, nambahin antrain:
```
queue.append('A')
queue.append('B')
queue.append('C')
```
---
Ini seperti pelanggan baru yang bergabung di belakang antrian. Kita pakai append() untuk menambah 'A', 'B', dan 'C' ke akhir list, sehingga antrian bertambah panjang. Setelah itu, kita cetak isi antrian untuk lihat siapa saja yang nunggu.  

3. Dequeue, antrian kelaur:
```
element = queue.pop(0)
```
Ini seperti pelanggan pertama di depan antrian yang sudah dilayani dan pergi. Kita pakai pop(0) untuk ambil elemen pertama ('A') dari list dan simpan di variabel element, lalu cetak apa yang dikeluarkan.  

4. Peek, intip:
```
frontElement = queue[0]
```
---
Ini seperti mengintip siapa yang di depan antrian tanpa mengusirnya. Kita ambil elemen pertama dari list dengan queue[0] dan simpan di frontElement, lalu cetak untuk tahu siapa yang berikutnya giliran.  

5. isEmpty, cek apakah kosong:
```
isEmpty = not bool(queue)
```
---
Ini seperti melihat apakah antrian masih ada orang atau sudah sepi. Kita pakai not bool(queue)jika list kosong, hasilnya True (antrian kosong); kalau ada isi, False. Lalu cetak statusnya.  

6. size/length, melihat panjang antrian:
```
print("Size: ", len(queue))
```
---
Ini seperti menghitung berapa pelanggan di antrian. Kita pakai len(queue) untuk dapatkan jumlah elemen di list, lalu cetak angka itu biar tahu antriannya panjang atau pendek.

### Output
---
```
Queue:  ['A', 'B', 'C']
Dequeue:  A
Peek:  B
isEmpty:  False
Size:  2
```
### Kesimpulan
---
Sebagai penutup, inti dari contoh ini adalah menunjukkan gimana sebuah antrian bisa dibangun dan dijalankan dengan cara yang sederhana di Python. Mulai dari bikin tempat kosong untuk antrian, nambahin elemen satu per satu, ngeluarin yang paling depan, sampai ngecek siapa yang sedang di posisi pertama, apakah antriannya masih ada orangnya, dan berapa panjangnya sekarang. Semua langkah itu nunjukkin kalau konsep FIFO benar-benar diterapkan, mirip cara kerja antrian di dunia nyata yaitu tertib, urut, dan mudah diprediksi.

# Implementasi Stack pada Python

### Kode Program
---
Stack itu bisa dibayangkan kayak tumpukan barang yang kamu simpan satu per satu di atas. Yang terakhir kamu taruh, dialah yang paling dulu kamu ambil lagi. Contoh program sederhana ini nunjukin gimana struktur data Stack di Python bekerja dengan memakai list sebagai tempat nyimpen datanya. Aturannya LIFO (Last In, First Out), jadi elemen yang baru masuk justru jadi yang pertama keluar. Dengan cara ini, urutan prosesnya terasa jelas dan gampang diikuti, karena semuanya bergantung pada posisi paling atas dari tumpukan.
```
stack = []

#Push
stack.append('A')
stack.append ('B')
stack.append('C')
print("stack: ", stack)

# Pop
element = stack.pop()
print("Pop: ", element)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))
```
### Penjelasan
---
1. Inisialisasi “wadah stack”:
```
stack = []
```
---
Bayangkan kamu sedang nyiapin tempat kosong buat naro tumpukan barang. Belum ada apa-apa di sana, cuma ruang kosong yang siap diisi. Kita bikin variabel stack dan ngasihnya list kosong []. Artinya, tumpukannya masih bersih dan siap menerima elemen baru lewat operasi push.

2. Push, nambahin elemen ke tumpukan:
```
stack.append('A')
stack.append('B')
stack.append('C')
```
---
Bagian ini mirip saat kamu nyelempitkan barang satu per satu ke bagian paling atas dari tumpukan. Fungsi append() dipakai buat naro 'A', 'B', dan 'C' di atas stack. Setelah itu kita cetak hasilnya biar kelihatan urutan tumpukannya sekarang.

3. Pop, ngambil elemen paling atas:
```
element = stack.pop()
```
----
Ini bisa dianalogikan kayak kamu ngambil barang yang paling terakhir kamu taruh—yang ada di posisi paling atas. Fungsi pop() tanpa parameter otomatis ngambil elemen paling atas stack, lalu kita simpan ke variabel element supaya bisa ditampilkan.

4. Peek, ngintip elemen teratas:
```
topElement = stack[-1]
```
---
Bagian ini ibarat kamu cuma melirik barang paling atas tanpa ngegeser atau mindahin apa pun. Dengan stack[-1], kita lihat elemen di posisi paling atas dan nyimpen nilainya ke topElement buat ditampilkan.

5. isEmpty, ngecek apakah tumpukan kosong:
```
isEmpty = not bool(stack)
```
---
Ibarat kamu ngecek apakah tumpukanmu masih ada isinya atau udah kosong sama sekali. Kalau list-nya kosong, bool(stack) bakal jadi False, lalu kebalikannya True—artinya stack kosong. Hasil itu kita cetak buat nunjukkin status tumpukannya.

6. Size, menghitung berapa banyak isi stack:
```
print("Size: ", len(stack))
```
---
Ini sama aja kayak ngitung berapa barang yang lagi numpuk. Kita tinggal pakai len(stack) buat dapetin jumlah elemennya, lalu dicetak supaya keliatan seberapa tinggi tumpukannya sekarang.

### Kesimpulan
---
Sebagai penutup, contoh di atas sebenarnya nunjukkin cara kerja sebuah stack dari awal sampai akhir dengan langkah yang sederhana. Kamu mulai dari tumpukan kosong, nambahin elemen satu per satu, ngambil elemen paling atas, ngintip isi teratas tanpa ngubah apa pun, ngecek apakah tumpukannya masih ada isinya, sampai ngitung total elemen yang lagi numpuk. Semua proses itu ngejelasin dengan jelas prinsip LIFO, yang terakhir masuk, dia yang pertama diambil. Jadi alur pengelolaan datanya tetap teratur dan gampang diikuti.