class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def enqueue(self, nama, penyakit, prioritas):
        data = (nama, penyakit, prioritas)

        # Masukkan data sesuai urutan prioritas (angka kecil = lebih prioritas)
        if self.is_empty():
            self.queue.append(data)
        else:
            inserted = False
            for i in range(len(self.queue)):
                # jika prioritas pasien baru lebih tinggi (angka lebih kecil)
                if prioritas < self.queue[i][2]:
                    self.queue.insert(i, data)
                    inserted = True
                    break
            if not inserted:
                self.queue.append(data)

        print(f"Pasien {nama} (Penyakit: {penyakit}, Prioritas: {prioritas}) masuk antrian.")

    def dequeue(self):
        if not self.is_empty():
            keluar = self.queue.pop(0)
            print(f"Pasien {keluar[0]} (Prioritas {keluar[2]}) telah ditangani dan keluar dari antrian.")
            return keluar
        else:
            print("Antrian kosong. Tidak ada pasien yang keluar.")
            return None

    def display(self):
        if self.is_empty():
            print("Antrian kosong.")
        else:
            print("Antrian pasien (berdasarkan prioritas):")
            for i in range(len(self.queue)):
                nama, penyakit, prioritas = self.queue[i]
                print(f"{nama} ({penyakit}) [Prioritas: {prioritas}]", end='')
                if i != len(self.queue) - 1:
                    print(" <- ", end='')
            print()

    def delete_all(self):
        konfirmasi = input("Yakin ingin reset semua data? (y/n): ").lower()
        if konfirmasi == 'y':
            self.queue.clear()
            print("Antrian telah di-reset.")
        else:
            print("Reset dibatalkan.")


# ========== Program Utama ==========
pq = PriorityQueue()
running = True

while running:
    print()
    print(' MENU ANTRIAN PASIEN '.center(50, "="))
    print('1. Tambah antrian pasien')
    print('2. Tampilkan antrian')
    print('3. Tangani pasien (dequeue)')
    print('4. Reset antrian')
    print('0. Keluar')
    print("".center(50,"="))

    try:
        choice = int(input('Masukkan pilihan anda: '))
    except ValueError:
        print('Input harus angka!')
        continue

    if choice == 1:
        try:
            jumlah = int(input('Berapa pasien yang ingin ditambahkan?: '))
        except ValueError:
            print('Input harus angka!')
            continue

        for i in range(1, jumlah+1):
            nama = input(f"Nama pasien ke-{i}: ")
            penyakit = input(f"Penyakit pasien ke-{i}: ")
            prioritas = int(input(f"Tingkat prioritas (1 = darurat, makin besar makin rendah): "))
            pq.enqueue(nama, penyakit, prioritas)

    elif choice == 2:
        pq.display()

    elif choice == 3:
        pq.dequeue()

    elif choice == 4:
        pq.delete_all()

    elif choice == 0:
        print("Program selesai. Semua pasien telah ditangani.")
        running = False

    else:
        print("Pilihan tidak valid.")
