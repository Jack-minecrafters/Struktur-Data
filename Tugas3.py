# ==========================
# Definisi Node Double Linked List
# ==========================
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# ==========================
# Definisi Double Linked List (pakai tail)
# ==========================
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None   # ✅ pointer ke node terakhir

    # ======================
    # Tambah di akhir
    # ======================
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # list kosong
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node   # hubungkan tail lama ke node baru
            new_node.prev = self.tail
            self.tail = new_node        # perbarui tail ke node baru

    # ======================
    # Tampilkan isi list
    # ======================
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "\n")
            current = current.next

    # ======================
    # 1. Hapus data sebelum node tertentu
    # ======================
    def delete_before(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next

        if not current:
            print(f"Data {key} tidak ditemukan.")
            return

        target = current.prev
        if not target:
            print(f"Tidak ada data sebelum {key}")
            return

        if target.prev:
            target.prev.next = current
            current.prev = target.prev
        else:
            # target adalah head
            self.head = current
            current.prev = None

        print(f"Data sebelum {key} ({target.data}) telah dihapus.")

    # ======================
    # 2. Hapus data setelah node tertentu
    # ======================
    def delete_after(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next

        if not current:
            print(f"Data {key} tidak ditemukan.")
            return

        target = current.next
        if not target:
            print(f"Tidak ada data setelah {key}")
            return

        if target.next:
            current.next = target.next
            target.next.prev = current
        else:
            # target adalah tail
            current.next = None
            self.tail = current  # ✅ tail diperbarui

        print(f"Data setelah {key} ({target.data}) telah dihapus.")

    # ======================
    # 3. Tambah data di tengah
    # ======================
    def insert_at_middle(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        # Hitung panjang list
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next

        mid = length // 2
        current = self.head
        for _ in range(mid - 1):
            current = current.next

        next_node = current.next
        current.next = new_node
        new_node.prev = current
        new_node.next = next_node
        if next_node:
            next_node.prev = new_node
        else:
            # kalau disisipkan di akhir, tail diperbarui
            self.tail = new_node

        print(f"Data {data} telah ditambahkan di tengah.")

# ==========================
# Demo Program
# ==========================
dll = DoubleLinkedList()

# Buat list awal
for nim in [2,4,0,7,0,5,1,0,7]:
    dll.append(nim)

print("Data awal:")
dll.display()
print(f"Tail saat ini: {dll.tail.data}")

# Hapus sebelum data tertentu
dll.delete_before(0)
dll.display()
print(f"Tail saat ini: {dll.tail.data}")

# Hapus setelah data tertentu
dll.delete_after(0)
dll.display()
print(f"Tail saat ini: {dll.tail.data}")

# Tambah data di tengah
dll.insert_at_middle(7)
dll.display()
print(f"Tail saat ini: {dll.tail.data}")
