class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def traverse(self):
        temp = self.head
        
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")
        
    def insert_At_Start(self,data):
        new_node = Node(10)
        new_node.next = self.head
        self.head = new_node
    
    def insert_At_End(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        
    def insert_At_Position(self, data,pos):
        if pos == 0:
            self.insert_At_Start(data)
            return

        new_node = Node(data)
        current = self.head
        
        for _ in range(pos-1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        
    def delete_from_beginning(self):
        if self.head:
            self.head = self.head.next
            
    def delete_from_end(self):
        if not self.head:
            return
            
        if not self.head.next:
            self.head = None
            return
            
        current = self.head
            
        while current.next.next:
            current = current.next
        current.next = None
        
    def delete_at_position(self,pos):
        
        if not self.head:
            return
        
        if not self.head.next:
            self.head = None
            return
        
        current = self.head
        for _ in range(pos-1):
            
            if not current.next:
                print("Position is out of bound")
                return 
            current = current.next
            
        
        if not current.next:
            print("Position is greated than size of the Linked List")
            return 
        current.next = current.next.next
    
    def delete_by_value(self,key):
        
        if not self.head:
            return
        
        if self.head.data == key:
            self.head = self.head.next
            
        current = self.head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next
        print(f"Key not found {key}")
                
        
    def count(self):
        if not self.head:
            return
        
        current = self.head
        
        count = 0
        while current:
            count+=1
            current = current.next
            
        print("Count of elements in the linked list:",count)
        
    
    def search(self,key):
        if not self.head:
            return
        
        current = self.head
        
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    
LL = LinkedList()

LL.insert_At_Start(10)

LL.insert_At_End(20)

LL.insert_At_Position(15,1)

LL.insert_At_Position(25,3)

# LL.delete_from_beginning()

# LL.delete_from_end()

# LL.delete_at_position(4)

# LL.delete_by_value(20)
# LL.delete_by_value(100)

print(LL.search(100))

LL.count()
LL.traverse()
