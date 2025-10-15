class RestaurantQueue:
    def __init__(self, kapasitas):
        self.queue = []
        self.kapasitas = kapasitas

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.kapasitas

    def __len__(self):
        return len(self.queue)

    def enqueue(self, nama, waktu):
        if self.is_full():
            print(f"Restoran penuh! {nama} harus menunggu atau datang lagi.")
        else:
            self.queue.append((nama, waktu))
            print(f"Pengunjung {nama} masuk restoran dan akan berada selama {waktu} menit.")

    def dequeue(self):
        if not self.is_empty():
            keluar = self.queue.pop(0)
            print(f"Pengunjung {keluar[0]} telah selesai (habis waktunya) dan keluar dari restoran.")
            return keluar
        else:
            print("Tidak ada pengunjung yang keluar.")
            return None

    def tick(self, menit=1):
        """Simulasi berjalannya waktu: setiap menit, waktu pelanggan berkurang"""
        if self.is_empty():
            print("Restoran kosong.")
            return

        print(f"\nSimulasi waktu berjalan {menit} menit...")
        for i in range(len(self.queue)):
            nama, waktu = self.queue[i]
            self.queue[i] = (nama, waktu - menit)

        # Cek siapa saja yang waktunya habis dan keluar
        keluar_list = []
        while self.queue and self.queue[0][1] <= 0:
            keluar_list.append(self.dequeue())

        if not keluar_list:
            print("Belum ada pengunjung yang keluar.")

    def display(self):
        if self.is_empty():
            print("Tidak ada pengunjung di restoran.")
        else:
            print("Antrian pengunjung saat ini:")
            for i in range(len(self.queue)):
                nama, waktu = self.queue[i]
                print(f"{nama} ({waktu} menit)", end='')
                if i != len(self.queue) - 1:
                    print(" <- ", end='')
            print()

    def delete_all(self):
        konfirmasi = input("Yakin ingin reset semua data? (y/n): ").lower()
        if konfirmasi == 'y':
            self.queue.clear()
            print("Restoran dikosongkan.")
        else:
            print("Reset dibatalkan.")


# ========== Program Utama ==========
kapasitas = int(input("Masukkan kapasitas restoran (max pengunjung): "))
resto = RestaurantQueue(kapasitas)
running = True

while running:
    print()
    print(' MENU RUMAH MAKAN '.center(50, "="))
    print('1. Tambah pengunjung')
    print('2. Tampilkan pengunjung')
    print('3. Jalankan waktu (simulasi)')
    print('4. Reset restoran')
    print('0. Keluar')
    print("".center(50, "="))

    try:
        choice = int(input('Masukkan pilihan anda: '))
    except ValueError:
        print('Input harus angka!')
        continue

    if choice == 1:
        try:
            jumlah = int(input('Berapa pengunjung yang ingin masuk?: '))
        except ValueError:
            print('Input harus angka!')
            continue

        for i in range(1, jumlah+1):
            nama = input(f"Nama pengunjung ke-{i}: ")
            waktu = int(input(f"Waktu berada (menit): "))
            resto.enqueue(nama, waktu)

    elif choice == 2:
        resto.display()

    elif choice == 3:
        try:
            menit = int(input("Masukkan berapa menit waktu berjalan: "))
        except ValueError:
            print("Input harus angka!")
            continue
        resto.tick(menit)

    elif choice == 4:
        resto.delete_all()

    elif choice == 0:
        print("Program selesai. Restoran ditutup.")
        running = False

    else:
        print("Pilihan tidak valid.")
