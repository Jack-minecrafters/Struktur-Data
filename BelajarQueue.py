class Queue:
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self.qlist)
    
    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        if self.isEmpty():
            print('Queue kosong. Tidak ada data yang dapat di-dequeue.')
            return None
        else:
            return self.qlist.pop(0)

    def peek(self):
        if self.isEmpty():
            print('Queue kosong. Tidak ada data yang dapat diintip.')
            return None
        else:
            return self.qlist[0]
    
    def display(self):
        if self.isEmpty():
            print('Queue kosong.')
        else:
            for item in self.qlist:
                print(item, end=' ')
            print()  # baris baru
    
    def delete_all(self):
        while not self.isEmpty():
            self.dequeue()
