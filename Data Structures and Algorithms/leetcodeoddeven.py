# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #I think one approach is like the quicksort approach where everytime I have 2 pointers. 
        #Slow pointer is pointing at the last odd number. 
        #Fast pointer is the one checking whether the value is odd or not 
        #If odd, add it after the node slow pointer is pointing at. 
        #Unlike quicksort, I don't need to do it recursively. 
        #Possible edge cases:
        #1. No nodes in the list. 
        #2. Only one node in the list (odd or even). 
        #3. Only odd or even nodes. 
        
        #First I could explicitly specify pointers and later see whether I can just use "curr"
        #Data I need to change/store
        #1. The node fast is pointing to
        #2. The node slow is pointing to. 
        #3. The node before the fast node -> To address this issue, I will check current.next instead of current -> To make sure I check the head node, I will make a dummy node. 

        #We aren't going to check the dummy node so I can just leave as 0. 
        '''
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        slow = dummy
        
        while fast.next
            #Checking if even. 
            if fast.next.val % 2 == 0:
                #Need to accomodate order for the case when the first node is even
                slow.next = fast.next
                fast.next = fast.next.next
        '''
                
        #Honestly, the easiest solution is to probably link all odd nodes first then iterate again to link all the even nodes. O(2n) complexity but whatever. 
        
        #In this scenario, we are checking whether curr.next is odd or even. 
        #We have to store head since we want to loop twice
        '''
        head_copy = head
        curr = head
        #I still have to counter the edge case when the beginning node is even. In this case just advance.
        while curr and curr.val % 2 == 0:
            curr = curr.next
        #The head I am going to return
        #new_head only received the single curr value and it is not updated from there on. 
        new_head = curr
        
        #If I add this condition, the last node won't be checked. -> Not true because last node is checked when curr is the second last node. 
        while curr and curr.next:
            if curr.next.val % 2 == 0:
                #curr remains, just curr.next changes
                curr.next = curr.next.next
            else:
                #Add to new_head
                new_head.next = curr.next
                #curr is just acting as a pointer, not the entire linked list. 
                curr = curr.next
                
        #Check even. 
        even = head
        while even and even.next:
            if even.next.val % 2 == 0:
                curr.next = even.next
                #Save into new_head
                new_head.next = curr.next
                #curr.next = even.next
                curr = curr.next #->even
            else:
                even.next = even.next.next
                
        return new_head
        '''
        
        #This time, I want to make it s that it filters based on the values. 
        #head -> always points at beginning
        #odd -> pointer at the first odd value
        #evenHead -> always points at the beginning
        #even -> pointer at the first even value. 
        #odd and even are just pointer at the end of the branches. They don't traverse the whole linked list. 
        #Need to think about whether to make copy of head or no. 
        #Or I can create dummy nodes for both of them and when combining, remove dummy node. 
        oddHead = ListNode()
        odd = oddHead
        evenHead = ListNode()
        even = evenHead
        #print(self.showList(oddHead))
        #print(self.showList(evenHead))
        
        curr = head
        while curr:
            #print("while")
            if curr.val % 2 == 1:
                #print("odd")
                #The problem with adding current is that it carries on everything that is attached to curr.
                #Therefore, I have to explicitly set .next to 0. 
                odd.next = ListNode(curr.val)
                #odd.next.next = None
                odd = odd.next
                #odd.next = None
            else:
                #print("even")
                #I am getting mutability issues
                even.next = ListNode(curr.val)
                #I want to just affect event.next.next
                #even.next.next = None
                even = even.next
                #even.next = None
            curr = curr.next
            #print(self.showList(evenHead))

            
        #print(self.showList(oddHead))
        #print(self.showList(evenHead))
            
        odd.next = evenHead.next
        return oddHead.next
    
    def showList(self, head):
        curr = head
        l = []
        while curr:
            l.append(curr.val)
            curr = curr.next
        return l
        
        
                
        
        