class Queue:
    def __init__(self):
        self.clist = []

    def is_empty(self):
        return len(self.clist) == 0

    def __len__(self):
        return len(self.clist)

    def enqueue(self, data):
        self.clist.append(data)

    def dequeue(self):
        if not self.is_empty():
            keluar = self.clist.pop(0)
            print(f"{keluar} keluar antrian.")
            return keluar
        else:
            print("Antrian kosong. Tidak ada yang keluar.")
            return None

    def display(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada data yang dapat ditampilkan")
        else:
            for i in range(len(self.clist)):
                print(self.clist[i], end='')
                if i != len(self.clist) - 1:
                    print(' <- ', end='')
            print()  # biar rapi barisnya

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
    print(' MENU '.center(35, "="))
    print('1. Tambah antrian konsumen')
    print('2. Tampil antrian konsumen')
    print('3. Hapus antrian konsumen')
    print('4. Reset')
    print('0. Quit')
    print("".center(35,"="))

    #try-except
    try:
        choice = int(input('Masukkan pilihan anda: '))
    except ValueError:
        print('Input harus berupa angka!')
        continue

    if choice == 1:
        #try-except
        try:
            add = int(input('Berapa orang?: '))
        except ValueError:
            print('Input harus berupa angka!')
            continue

        if add <= 0:
            print('Jumlah data minimal 1!!')
        else:
            for i in range(1, add + 1):
                data = input(f'Masukkan data ke-{i}: ')
                cQueue.enqueue(data)

    elif choice == 2:
        print('Isi Queue: ')
        cQueue.display()

    elif choice == 3:
        cQueue.dequeue()

    elif choice == 4:
        cQueue.delete_all()

    elif choice == 0:
        print('Bye~~~')
        running = False

    else:
        print('Pilihan tidak ada')