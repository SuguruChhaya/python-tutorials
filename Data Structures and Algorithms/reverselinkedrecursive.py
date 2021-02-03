#Code to reverse a singly linked list recursively. 
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to reverse the linked list 
    def reverseList(self, node):
        if node.next == None:
            self.head = node
            return
        
        self.reverseList(node=node.next)
        next_node = node.next 
        next_node.next = node
        node.next = None



        
          
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data) 
        
            temp = temp.next
  
  
# Driver program to test above functions 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 
  
print("Given Linked List")
llist.printList() 
llist.reverseList(llist.head) 
print("\nReversed Linked List")
llist.printList() 
  