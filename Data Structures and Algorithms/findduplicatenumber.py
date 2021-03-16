arr = [1,1,2]
'''
slow = arr[arr[0]]
fast = arr[slow]

#!The key is that there can be more than 1 element involved outside the cycle. Doesn't necessarily have to be 1. 
while fast != slow:
    slow = arr[slow]
    fast = arr[arr[fast]]
'''
slow = fast = arr[0]
#*Have to know whether initial meeting or after. Check using a boolean.
initial = True
while slow != fast or initial:
    initial = False
    slow = arr[slow]
    fast = arr[arr[fast]]

fast = arr[0]

while slow != fast:
    slow = arr[slow] 
    fast = arr[fast]

print(slow)
            