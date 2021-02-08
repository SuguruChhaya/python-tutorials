#Practicing mergeosrt iterative
def merge(arr, arrEmpty, l, m, r):
    #Define 3 pointers
    #Beginning of first subarray
    a = l
    #Beginning of second subarray
    b = m+1
    #Beginning of big subarray we are copying into
    c = l

    #I think I can check for special case. I can do it after the solution works. 

    #When there are elements left in both subarrays. 
    while a < m+1 and b < r+1:
        if arr[a] <= arr[b]:
            arrEmpty[c] = arr[a]
            a += 1
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

    


def merge_pass(arr, arrEmpty, lenArr, size, moveToarrEmpty):
    #Initially set the starting l value
    l = 0
    #Could be a little confusing but I thought of it this way. 
    #If l = 0 and size = 2, and lenArr = 3, this should be permitting because we will still have 1 element as the right subarray. But when size=3, that shouldn't be allowed because no room for right subarray. 
    #Or more simply, index_based + len_based = len_based. Since we are comparing 2 len_based items, a simple < will work. 
    while l + size < lenArr:
        #Set mid. 
        m = l+size-1
        r = m+1+size-1
        #Depending on which one list we are copying into, we have to pass different.

        #I have to add a specific case for r
        #Remember that even if left subarray is huge, right subarray could only be len 1. 
        #For example, if I sort arr with length 5, the final step will be to combine subarray with len 4 and 1. 
        #In this case, r will be incorrect so we have to check for this case.
        if r >= lenArr:
            r = lenArr-1
        if moveToarrEmpty:
            merge(arr, arrEmpty, l, m, r)
        else:
            merge(arrEmpty, arr, l, m, r)

        #Update l
        l = r+1

    #Copy remaining elements
    if moveToarrEmpty:
        #We have to copy anthing remaining in arr to arrEmpty
        #Go from the last l to index lenArr -1 so go through all elements.
        for i in range(l, lenArr):
            arrEmpty[i] = arr[i]
    else:
        for i in range(l, lenArr):
            arr[i] = arrEmpty[i]

def mergesort(arr):
    #Set the initial subarray size
    size = 1
    #Find the length
    lenArr = len(arr)
    #We will initially move the items into arrEmpty
    moveToarrEmpty = True

    #Create empty list
    arrEmpty = [0] * lenArr
    #Both based on length
    while size < lenArr:
        merge_pass(arr, arrEmpty, lenArr, size, moveToarrEmpty)
        size *= 2
        moveToarrEmpty = not moveToarrEmpty

arr = [3, 1, 6, 2, 5, 0, 5, 1, 3, 5.6, 4, 1, 0]
mergesort(arr)
print(arr)