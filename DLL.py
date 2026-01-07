class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print("None")
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        new_node.prev = current
        
    def insert_at_position(self, pos, data):
        
        if pos == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        
        for _ in range(pos-1):
            if not current:
                print("Position out of bound")
                return
            current = current.next
            
        new_node.next = current.next
        new_node.prev = current
        
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        
    def delete_from_beginning(self):
        if not self.head:
            return False
        if self.head.next:
            self.head.next.prev = None
        self.head = self.head.next
        
    def delete_from_end(self):
        if not self.head:
            return
        
        if not self.head.next:
            self.head = None
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.prev.next = None
        current.prev = None
        
    def delete_by_value(self, value):
        current = self.head
        while current:
            
            if current.data == value:
                
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
        
        
DLL = DoublyLinkedList()

DLL.insert_at_beginning(15)
DLL.insert_at_beginning(10)
DLL.insert_at_beginning(5)

DLL.insert_at_end(20)

DLL.insert_at_position(2,13)

DLL.delete_from_beginning()
DLL.delete_from_end()
DLL.delete_by_value(13)


DLL.traverse_forward()
        
        
        
        
        
