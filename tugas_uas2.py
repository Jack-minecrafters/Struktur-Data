class Queue:
    def __init__(self):
        self.clist = []

    def is_empty(self):
        return len(self.clist) == 0

    def __len__(self):
        return len(self.clist)

    def enqueue(self, nama, pesanan):
        self.clist.append((nama, pesanan))
        print(f"{nama} dengan pesanan '{pesanan}' masuk antrian.")

    def dequeue(self):
        if not self.is_empty():
            keluar = self.clist.pop(0)
            print(f"{keluar[0]} dengan pesanan '{keluar[1]}' telah selesai dilayani dan keluar dari antrian.")
            return keluar
        else:
            print("Antrian kosong. Tidak ada yang keluar.")
            return None

    def display(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada data yang dapat ditampilkan")
        else:
            for i in range(len(self.clist)):
                nama, pesanan = self.clist[i]
                print(f"{nama}({pesanan})", end='')
                if i != len(self.clist) - 1:
                    print(' <- ', end='')
            print()

    def delete_all(self):
        konfirmasi = input("Yakin ingin reset semua data? (y/n): ").lower()
        if konfirmasi == 'y':
            self.clist.clear()
            print("Antrian telah di-reset.")
        else:
            print("Reset dibatalkan.")


# ======= Program Utama =======
cQueue = Queue()
running = True

while running:
    print()
    print(' MENU KAFE '.center(45, "="))
    print('1. Tambah antrian pengunjung')
    print('2. Tampil antrian')
    print('3. Layani (hapus dari antrian)')
    print('4. Reset antrian')
    print('0. Keluar')
    print("".center(45,"="))

    try:
        choice = int(input('Masukkan pilihan anda: '))
    except ValueError:
        print('Input harus berupa angka!')
        continue

    if choice == 1:
        try:
            add = int(input('Berapa pengunjung yang ingin ditambahkan?: '))
        except ValueError:
            print('Input harus berupa angka!')
            continue

        if add <= 0:
            print('Jumlah pengunjung minimal 1!!')
        else:
            for i in range(1, add + 1):
                nama = input(f'Masukkan nama pengunjung ke-{i}: ')
                pesanan = input(f'Masukkan pesanan pengunjung ke-{i}: ')
                cQueue.enqueue(nama, pesanan)

    elif choice == 2:
        print('\nAntrian Saat Ini:')
        cQueue.display()

    elif choice == 3:
        cQueue.dequeue()

    elif choice == 4:
        cQueue.delete_all()

    elif choice == 0:
        print('Sampai jumpa, kafe tutup')
        running = False

    else:
        print('Pilihan tidak ada')
