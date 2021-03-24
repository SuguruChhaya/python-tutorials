
#*When flipping the pancakes, obviously the sides change but we are also reversing the position. 
#!Our priority is to get the bottom of the stack to be happy so we don't have to deal with it. 

#*Whenever we encouter a -, we must flip that at somepoint. 
#*Really, it is only beneficial if I flip when end of pancake are --
#!Kind of similar to the space protect in the sense that iterate from back and find most beneficial. 

def flip(arr, l, h):
    a = l
    b = h
    while l <= h:
        #*Pre-changing becomes a problem when I am only flipping one pancake like [+, -]
        #[+, +, -]
        #!Even though it eats some time, it is more accurate to swap first then change signs.
        
        arr[l], arr[h] = arr[h], arr[l]
        l+=1
        h-=1
    
    for i in range(a, b+1):
        if arr[i] == "+":
            arr[i] = "-"
        else:
            arr[i] = "+"

#!+- is taking some time. 
'''
def main(arr):
    #*Len 100 so shouldn't have problem but still shave off time. 

    result = 0
    #!After finishing loop, lastNegative must become -1 because no more negatives. 
    #!For cases where it is all positive in the first place, getting through the while loop will cause the result to be at least 1. 
    #*Have to find the correct negative value through a traversal before. 
    lastNegative = None
    #!Cannot forget to break since there might be multiple negatives and I want to address from the back. 
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == "-":
            lastNegative = i
            break
    
    if lastNegative == None:
        return 0

    while lastNegative != -1:
        isNegative = False
        for i in range(lastNegative, -1, -1):
            #*Find the last -
            if arr[i] == "-":
                lastNegative = i
                isNegative = True
                break

        #!I have to implement something similar to the previous lastnegative thing in this loop: maybe a boolean to check whether there even is a negative value. 
        if isNegative == False:
            return result
        if arr[0] == "-":
            flip(arr, 0, lastNegative)
            lastNegative -= 1
        else:
            for i in range(lastNegative, -1, -1):
                if arr[i] == "+":
                    break
        
            flip(arr, 0, i)
        result+=1

    return result
'''

#*A more logical (not based on pattern) way of solving this problem. 
def main(arr):
    #*I really just needed to think in terms of greedy and analyze: "What is the characteristics of a goal state"?
    result = 0
    for i in range(len(arr)-1):
        if arr[i] == "+" and arr[i+1] == "-":
            result += 1
        elif arr[i] == "-" and arr[i+1] == "+":
            result += 1
    if arr[-1] == "-":
        result += 1
    return result

numTests = int(input())
for i in range(numTests):
    s = input()
    arr =[]
    for j in s:
        arr.append(j)
    print(f"Case #{i+1}: {main(arr)}")