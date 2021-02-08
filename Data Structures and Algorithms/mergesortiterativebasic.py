#Actual iterative merge sort iterative code based on C++ code in Python 3. 
#I accomodated this file based on https://www.youtube.com/watch?v=Eid6JEHZ7nw 
#For a modification with less copying, check out: 
'''
Some diffences from original video. 
1. I named variables differently (you should be able to handle that.)
2. Instead of having 4 variables (low1, up1, low2, up2), I only used 3 (l, m, r), using the fact that low2 = up1+1
Basically l = low1, m = up1, m+1=low
'''

def merge(arr, arrEmpty, l, m, r):
    a = l
    #Beginning of second subarray
    b = m + 1
    #Beginning of big array Empty
    c = l

    while a < m+1 and b <r+1:
        if arr[a] <= arr[b]:
            arrEmpty[c] = arr[a]
            a+=1

        else:
            arrEmpty[c] = arr[b]
            b+=1
        c+=1

    while a < m+1:
        arrEmpty[c] = arr[a]
        a+=1
        c+=1
    while b < r+1:
        arrEmpty[c] = arr[b]
        b+=1
        c+=1

def merge_pass(arr, arrEmpty, size, lenArr):
    #Unlike the C++ code, I will only define 3 variables: l, m, and r
    l = 0
    while l + size < lenArr:
        #This is the part where we figure out all the indices. 
        m = l + size - 1
        #Don't need for low2
        r = m + 1 + size - 1
        if r >=lenArr:
            r = lenArr-1
        merge(arr, arrEmpty, l, m, r, size)
        l = r+1

    #All the subarrays in the original list has been merged at this point. Now we copy it back to the original. But I have no idea what is going on right here. 
    for i in range(l, lenArr):
        arrEmpty[i] = arr[i]
    for j in range(0, lenArr):
        arr[j] = arrEmpty[j]

def mergesort(arr):
    #I will need a temporary list to store processes. 
    lenArr = len(arr)
    arrEmpty = [0] * lenArr

    subArraySize = 1
    while subArraySize < lenArr:
        merge_pass(arr, arrEmpty, subArraySize, lenArr)
        subArraySize *= 2

arr = [5, 2, 4, 1, 84, 2, 5, 2]
mergesort(arr)
print(arr)

#Merge pass is a method which moves onto the method which actually merges the left array and the right aray. 
#If the subarray is equal to or larger than the length of the array, there is only one subarray, the left one. 
#There is no right subarray to merge to. 
#If the arr passed has one element, subarraysize, which is 1, will be equal to lenArr, hence merge_pass won't be called. 
#That's OK because there is no second subarray to merge. 