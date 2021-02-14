class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    
        

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        current = self.root
        counter = 0
        #We have to prevent error message when index is invalid. 
        while counter < index:
            if current.next:
                current = current.next
                counter += 1
            else:
                #get failing another test case at 
                return -1

        return current.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = Node(val)
        #First have to check whether a node is already present or not. 
        if self.root:
            newNode.next = self.root
            self.root = newNode
        
        else:
            self.root = newNode

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val)
        if self.root:
            current = self.root
            while current.next:
                current = current.next
            current.next = newNode

        else:
            self.root = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        #I guess I can first find the length of the linked list. 
        current = self.root
        length = 0
        prev = None
        while current:
            length += 1
            #Just so I can use prev when index==length
            prev = current
            current = current.next


        if index > length:
            pass

        elif index == length:
            prev.next = Node(val)

        else:
            counter = 0
            current = self.root
            prev = None
            while current:
                if counter == index:
                    newNode = Node(val)
                    prev.next, newNode.next = newNode, prev.next
                    break
                else:
                    counter += 1
                    prev = current
                    current = current.next
                    
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        #We first have to check whether the index is valid so we check the length as we did for add. 
        current = self.root
        length = 0
        #If there are no values or only the root in the list, just make self.root=None

        while current:
            length += 1
            #Just so I can use prev when index==length
            prev = current
            current = current.next

        #We cannot delete a Node at index==length
        if index >= length:
            pass

        else:
            counter = 0
            current = self.root
            prev = None
            while current:
                if counter == index:
                    #Check if prev exists
                    if prev:
                        prev.next = current.next
                    else:
                        self.root = None
                    break
                else:
                    counter += 1
                    prev = current
                    current = current.next

    def print_list(self):
        #Just so I can comment easier, make it a returning function. 
        finalList = []
        current = self.root
        while current:
            finalList.append(current.val)
            current = current.next

        return finalList


a = MyLinkedList()
print(a.print_list())
a.addAtHead(1)
print(a.print_list())
a.addAtTail(3)
print(a.print_list())
a.addAtIndex(1, 2)
print(a.print_list())
print(a.get(1))
print(a.print_list())
print(a.deleteAtIndex(1))
print(a.print_list())
#Have to fix whatever error .get is giving me. 
print(a.get(1))
print(a.print_list())

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)