#from _typeshed import StrPath


def maxElement(n, maxSum, k):

    # Write your code here
    #First code the brute force. 
    starting = 1
    total=0
    #Actually don't even have to build the array.
    #!We shouldn't continue when it is equal. 
    while total < maxSum:
        highest = starting + k
        ending = highest + (k - (n-1))
        sumStarting = ((starting + highest) * (k+1)) / 2
        sumEnding = ((highest+ending) * (n-k)) / 2
        #highest overlaps
        total = sumStarting + sumEnding - highest
        starting += 1

    #!If starting remains at 1, we shouldn't just return highest but further flatten out to make max value smaller. 
    return highest

def maxElement(n, maxSum, k):
    #*2nd intuition is to actually build an array of all 1s. 2 pointers at the end and which close in, advancing elements in that range by 1. 
    #*Whenever maxSum exceeds, we stop. If the 2 pointers cross eachother, start increasing every element by 1
    #!A couple of exceptions might be [1, 1] when maxSum might be 3 and k=1. If we keep incrementing with two pointers, never gonna get to 2
    pass

#!8/15 Only think holding back is time limit.   
def maxElement(n, maxSum, k):
    currMax = 1
    prevMax = 1
    #*Might be way better to just use array. When adding, I can check if it goes below 1. If it does, I can just add 1. 
    #*Handy way is to just use sum() but I can save sum time. 
    total = 0
    #resultList = []
    #!We must return prev, which applied for total <= maxSum. Since it will give me an extra round, always record prev. 
    while total < maxSum:
        #*Start adding into arr. 
        #*Don't need to do anything for currMax
        total = currMax
        #!2 value storers: left and right
        left = total
        right = total
        #!My code is running properly so I think I can just try simply adding it. 
        #!One way of possibly shrimming off some time is automatically knowing until what point I have to keep subtracting. After I hit 1, I can just add the big chunk of 1s.
        for lower in range(k-1, -1, -1):
            if left == 1:
                total += 1
            else:
                left -= 1
                total += left
        
        for higher in range(k+1, n, 1):
            if right == 1:
                total += 1
            else:
                right -= 1
                total += right

        #!prevMax is ultimately just copying the bad value of 
        #*Rather than dealing with so many variables, just store it in a list and iterate it from the back. 
        #!It's not about the currMax, it's more about the 
        #resultList.append(currMax)
        #!We can only copy if it is correct. 
        if total <= maxSum:
            prevMax = currMax
        currMax += 1

    return prevMax
        

def maxElement(n, maxSum, k):
    currMax = 1
    prevMax = 1
    #*Might be way better to just use array. When adding, I can check if it goes below 1. If it does, I can just add 1. 
    #*Handy way is to just use sum() but I can save sum time. 
    total = 0
    #resultList = []
    #!We must return prev, which applied for total <= maxSum. Since it will give me an extra round, always record prev. 
    while total < maxSum:
        #*Start adding into arr. 
        #*Don't need to do anything for currMax
        total = currMax
        #!2 value storers: left and right
        left = total
        right = total
        #!My code is running properly so I think I can just try simply adding it. 
        #!One way of possibly shrimming off some time is automatically knowing until what point I have to keep subtracting. After I hit 1, I can just add the big chunk of 1s.
        for lower in range(k-1, -1, -1):
            #!The improvement I can make here is not manually keep on adding but adding all at once of decrease and 1s. 
            #!I already solved the issue of 1s. 
            if left == 1:
                #!I could just add all at once and break out of the loop. 
                #*I could actually use the lower counter. 
                #total += 1
                total += lower + 1 #*1
                break
            else:
                left -= 1
                total += left
        
        for higher in range(k+1, n, 1):
            if right == 1:
                #total += 1
                total += n - higher #*1
                break
            else:
                right -= 1
                total += right

        #!prevMax is ultimately just copying the bad value of 
        #*Rather than dealing with so many variables, just store it in a list and iterate it from the back. 
        #!It's not about the currMax, it's more about the 
        #resultList.append(currMax)
        #!We can only copy if it is correct. 
        if total <= maxSum:
            prevMax = currMax
        currMax += 1

    return prevMax


def maxElement(n, maxSum, k):
    currMax = 1
    prevMax = 1
    #*Might be way better to just use array. When adding, I can check if it goes below 1. If it does, I can just add 1. 
    #*Handy way is to just use sum() but I can save sum time. 
    total = 0
    #resultList = []
    #!We must return prev, which applied for total <= maxSum. Since it will give me an extra round, always record prev. 
    while total < maxSum:
        #*Start adding into arr. 
        #*Don't need to do anything for currMax
        total = currMax
        #!2 value storers: left and right, starting from adjacent places of the maximum value. 
        #*Initialize them to None so I can later check whether they exist and sum things up. 
        left = None
        right = None

        if k-1>=0:
            left = total - 1
        if k+1<n:
            right = total - 1

        #total += arr[k]
        if left!=None:
            #?What happens for cases like [1, 2, 1]? Gives correct answer but...
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


        '''
        for lower in range(k-1, -1, -1):
            #!The improvement I can make here is not manually keep on adding but adding all at once of decrease and 1s. 
            #!I already solved the issue of 1s. 
            if left == 1:
                #!I could just add all at once and break out of the loop. 
                #*I could actually use the lower counter. 
                #total += 1
                total += lower + 1 #*1
                break
            else:
                left -= 1
                total += left
        
        for higher in range(k+1, n, 1):
            if right == 1:
                #total += 1
                total += n - higher #*1
                break
            else:
                right -= 1
                total += right
        '''

        #!prevMax is ultimately just copying the bad value of 
        #*Rather than dealing with so many variables, just store it in a list and iterate it from the back. 
        #!It's not about the currMax, it's more about the 
        #resultList.append(currMax)
        #!We can only copy if it is correct. 
        if total <= maxSum:
            prevMax = currMax
        currMax += 1

    return prevMax



print(maxElement(3, 7, 1))

#*Always getting something 1 less than actual. 
#https://www.hackerrank.com/test/6ln9g5g0r6f
