class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.next = pointer 

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            
            # node = Node(data)
            current.next = Node(data)
    
    def insert_at(self, index, data):
        if index < 0 or index > self.length() -1:
            print("Invalid Index")
        
        elif index == 0:
            self.insert_at_beginning(data)
        
        else:
            urutan = 0
            current = self.head

            while urutan < index -1:
                current = current.next
                urutan += 1

                node = Node(data, current.next)
                current.next = node
    
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            text_print = ""
            current = self.head

            while current:
                text_print += str(current.data) + " → "
                current = current.next

            print(text_print)
    
    def length(self):
        urutan = 0
        current = self.head

        while current:
            urutan += 1
            current = current.next
        
        return urutan

ll = LinkedList()

ll.insert_at_beginning("jeruk")
ll.insert_at_beginning("mangga")
ll.insert_at_beginning("manggis")
ll.insert_at_end("apel")
ll.insert_at(2, "anggur")

ll.print_list()
print("Panjang linked list:", ll.length())