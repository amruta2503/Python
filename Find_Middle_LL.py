#Brute force solution
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
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def size_of_list(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count    
        
    def middle_node(self,count):
        mid = count //2
        current = self.head
       
        for _ in range(mid):
            current = current.next
            
        return current.data
        
LL = LinkedList()

LL.insert_At_Start(25)
LL.insert_At_Start(20)
LL.insert_At_Start(15)
LL.insert_At_Start(10)
# LL.insert_At_Start(25)

LL.traverse()

count = LL.size_of_list()
print(f"Count of linked list is: {count}")

middle = LL.middle_node(count)
print(f"Middle node of the list is: {middle}")

#Optimal 
        
