class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode

    def insert_before(self, data, value):
        newNode = Node(data)
        if self.is_empty():
            self.head = self.tail = newNode
        else:
            current = self.head
            while current:
                if current.data == value:
                    newNode.next = current
                    current.previous.next = newNode
                    newNode.previous = current.previous
                    current.previous = newNode
                    return
                else:
                    current = current.next

    def insert_after(self, data, value):
        newNode = Node(data)
        if self.is_empty():
            self.head = self.tail = newNode
        else:
            current = self.head
            while current:
                if current.data == value:
                    newNode.next = current.next
                    current.next.previous = newNode
                    newNode.previous = current
                    current.next = newNode
                    return
                else:
                    current = current.next

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def delete_from_beginning(self):
        if self.is_empty():
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        return data

    def delete_at_middle(self,data):
        if self.is_empty():
            return None
        else:
            current = self.head
            while current:
                if current.data == data:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    return 
                else:
                    current = current.next

    def delete_from_end(self):
        if self.is_empty():
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        return data

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.previous
        print()

# Example usage:
dll = DoubleLinkedList()

print('Tambah Data 5 & 10 di bagian depan')
print('Tambah Data 20 & 30 di bagian belakang')
dll.insert_at_beginning(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_beginning(5)
print()

print('Menampilkan data dari depan ke belakang: ', end ='')
dll.display_forward() # Output: 5 10 20 30
print('Menampilkan data dari belakang ke depan: ', end ='')
dll.display_backward() # Output: 30 20 105
print()


print('Menambahkan simpul 25 sebelum simpul 30: ', end ='')
dll.insert_before(25,30)
dll.display_forward() # Output: 5 10 20 25 30
print('Menambahkan simpul 17 setelah simpul 10: ', end ='') 
dll.insert_after(17,10)
dll.display_forward() # Output: 5 10 17 20 25 30
print()

print('Menghapus data di bagian depan')
dll.delete_from_beginning()
print('Menghapus data di bagian belakang')
dll.delete_from_end()
print()

print('Menampilkan data linked list setelah delete data: ', end ='')
dll.display_forward() # Output: 10 17 20 25
print()
print('Delete simpul 20')
dll.delete_at_middle(20)
print()
print('Data linked list setelah dihapus: ', end = '')
dll.display_forward() # Output: 10 17 25