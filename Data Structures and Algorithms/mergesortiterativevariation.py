#Actual iterative merge sort iterative code based on C++ code in Python 3. 
#I got the basic version of this code from https://www.youtube.com/watch?v=Eid6JEHZ7nw. Code: 
#I am following the optimization described at 18:31 on https://www.youtube.com/watch?v=k3oezbZgfDs. 
#I followed the optimization for iterative mergesort which is not to copy all elements into second array every time.
#This reduces the number of copying (obviously). 
#I tracked which array are we copying into using the "moveToEmpty" boolean. 

#!The problem I have with this approach of switching parameters is that we are direct
def merge(arr, arrEmpty, l, m, r):

    a = l
    #Beginning of second subarray
    b = m + 1
    #Beginning of big array (very similar to previous method. )
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


def merge_pass(arr, arrEmpty, size, lenArr, moveToEmpty):
    l = 0

    while l + size < lenArr:
        #Size is based on length
        m = l + size - 1
        r = m + 1 + size - 1
        #Since r is based on index and lenArr is based on length, if they are equal, we know that r has exceeded the array
        if r >= lenArr:
            r = lenArr - 1
        if moveToEmpty:
            merge(arr, arrEmpty, l, m, r)
        else:
            merge(arrEmpty, arr, l, m, r)
        l = r+1

    #Even if we change the order, we still have to copy remaining elements. 
    if moveToEmpty:
        for i in range(l, lenArr):
            arrEmpty[i] = arr[i]

    else:
        for i in range(l, lenArr):
            arr[i] = arrEmpty[i]

    #We don't need to copy all the individual elements anymore -> Less copying. 

    




def mergeSort(arr):
    lenArr = len(arr)
    arrEmpty = [0] * lenArr
    size = 1
    #This is implicitly checking for the case when lenArr = 1 and array is already sorted
    moveToEmpty = True
    while size < lenArr:
        merge_pass(arr, arrEmpty, size, lenArr, moveToEmpty)
        size *=2 
        moveToEmpty = not moveToEmpty


arr = [1, 0, 54, 2, 1, 4, 21, 43, 56,1, 3, 0.3, 4]
mergeSort(arr)
print(arr)