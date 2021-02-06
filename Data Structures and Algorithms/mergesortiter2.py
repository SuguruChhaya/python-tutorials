#Trying to implement the bottom up approach with the list optimization to avoid so much copying. 

#!The problem I have with this approach of switching parameters is that we are direct
def merge(arr, arrEmpty, l, m, r):

    a = l
    #Beginning of second subarray
    b = m + 1
    #Beginning of big array (very similar to previous method. )
    c = l
    '''
    if arrEmpty[m] <= arr[m+1]:
        while a < m+1:
            arr[c] = arrEmpty[a]
            a+=1
            b+=1
            c+=1
    '''

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
    #First set the left pointer to 0. 
    l = 0
    #I understand that we actually need to have at least one element for the right side of the array.
    #However l+size is based on index and lenArr is just length. So l+size < lenArr assumes that at lease 1 element will be included on the right side. 
    
    #In this method, all elements are merged once. But we would either have to store checker as global variable or pass it into the function. mergeSort can manage this. 
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


arr = [1, 0, 54, 2]
mergeSort(arr)
print(arr)