arr = [4, 5, 6, 7, 6, 5]
left = 6
right = 6
k = 3
n = len(arr)
total = 0

#!Can calculate sum in constant time. 
total += arr[k]
if left!=None:
    startingIndex = (k-1) - left + 1
    if startingIndex < 0:
        startingIndex = 0
    length = (k-1) - startingIndex + 1
    #!Have to recheck. 
    endingValue = left - length +1 
    #*I cannot simplify this part because decrease might not reach 1. 
    
    total += ((left+endingValue) * length) / 2

#*Now that I have managed the stairs, just add the 1s. 
    total += 1 * startingIndex

if right!=None:
    #!Really just need to jump by 4
    endingIndex = (k+1) + right - 1
    if endingIndex >=n:
        endingIndex = n-1
    length = endingIndex - (k+1) + 1
    endingValue = right - length + 1

    total += ((right+endingValue) * length) / 2
    total += n-endingIndex-1

print(f"sum:  {sum(arr)}")
print(total)
