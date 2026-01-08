#Brute

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
        
    def is_palindrome(self):
        stack = []
        current = self.head 
        while current:
            stack.append(current.data)
            current = current.next
            
        current = self.head
        while current:
            if current.data != stack.pop():
                return False
            current = current.next
        return True
    
    
        
LL = LinkedList()

LL.insert_At_Start(25)
LL.insert_At_Start(20)
LL.insert_At_Start(15)
LL.insert_At_Start(20)
LL.insert_At_Start(25)

LL.traverse()

isPalindrome = LL.is_palindrome()
print("is the linked list palindrome:",isPalindrome )

#optimal  
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
        
    def reverse_LL(self,middle):
        prev = None
        current = middle
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node 
        
        return prev
        
    
    def is_middle(self):
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True
        
        first_middle = self.is_middle()
    
        second_half_head = self.reverse_LL(first_middle.next)
        
        first = self.head
        second = second_half_head
        
        while second:
            if first.data != second.data:
                return False
            first = first.next
            second = second.next
        return True
    
        
LL = LinkedList()

LL.insert_At_Start(25)
LL.insert_At_Start(20)
LL.insert_At_Start(15)
LL.insert_At_Start(20)
LL.insert_At_Start(25)

print("Linked List is",LL.traverse())

isPalindrome = LL.is_palindrome()
print("is the linked list palindrome:",isPalindrome )

        
