#!THE MOST IMPORTANT AND INTERESTING THING ABOUT THIS APPROACH IS THAT WHENEVER WE ARE INSERTING A NEW NODE (HEAD OR ANYWHERE ELSE), WE ALWAYS HAVE A VALUE BEFORE AND AFTER IT.
#*This is because the '0' nodes at the beginning and end sandwich the actual linked list. 

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        #!There seems to be a constant sandwich composed by the head and tail nodes with a value of 0. 
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        #!Can check this normally because self.size doesn't include the 2 zeros that sandwich the actual nodes.
        if index < 0 or index >= self.size:
            return -1
        if index < self.size - index:
            cur = self.head
            for _ in range(index + 1):
                cur = cur.next

        #!Makes sense. We are just trying to reach the 
        else:
            #?These are very confusing loops but
            #For index=1 in [0, 1, 2, 3, 0] array with size 3. 
            #At the end of first loop, prev = actual last element.
            #At the end of second loop, prev = second to last element. 
            cur = self.tail
            for _ in range(self.size - index):
                cur = cur.prev
                
        return cur.val

    #An additional method I coded just to understand the structure better. 
    def getHead(self):
        return self.head.next.val

    def getTail(self):
        return self.tail.prev.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        pred, succ = self.head, self.head.next
        #print(self.showList())
        self.size += 1
        to_add = ListNode(val)
        #print(self.showList())
        to_add.next = succ
        #print(self.showList())
        to_add.prev = pred
        #print(self.showList())
        pred.next = to_add
        #print(self.showList())
        succ.prev = to_add
        #print(self.showList())
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        pred, succ = self.tail.prev, self.tail
        #print(self.showList())
        self.size += 1
        to_add = ListNode(val)
        to_add.next = succ
        #print(self.showList())
        to_add.prev = pred
        #print(self.showList())
        pred.next = to_add
        #print(self.showList())
        succ.prev = to_add
        #print(self.showList())
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        
        if index < 0:
            index = 0
            
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        
        self.size += 1
        to_add = ListNode(val)
        to_add.next = succ
        #print(self.showList())
        to_add.prev = pred
        #print(self.showList())
        #pred.next = to_add
        #print(self.showList())
        succ.prev = to_add
        #print(self.showList())

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return None
        self.size -= 1
        #!In this case, pred and succ aren't next to each other. Rather, they sandwich the values which are to be deleted. 
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev.prev
            
        pred.next = succ
        succ.prev = pred

    def showList(self):
        outputList = []
        current = self.head
        if self.head:
            while current:
                if current.next:
                    if current.prev:
                        outputList.append([f"current: {current.val}, next: {current.next.val}, prev: {current.prev.val}"])
                    else:
                        outputList.append([f"current: {current.val}, next: {current.next.val}, prev: {None}"])
                else:
                    if current.prev:
                        outputList.append([f"current: {current.val}, next: {None}, prev: {current.prev.val}"])
                    else:
                        outputList.append([f"current: {current.val}, next: {None}, prev: {None}"])
                current = current.next
            
        return outputList

obj = MyLinkedList()
obj.addAtIndex(0, 2)
obj.addAtHead(1)
print(obj.getHead())
print(obj.getTail())