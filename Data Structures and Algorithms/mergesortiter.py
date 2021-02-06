#Actual iterative merge sort code based on C++ code. 
#I will first follow the C++ code completely and make tweeks of my own. 

def merge(arr, arrEmpty, l, m, r, size):
    #Pointers: similar to previous merging methods.
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
        #I am not yet accomodating for only 1 side copying. 
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
        #I understand why the value of l will be so large. It is because it has been incremented a lot to the point that l+size<lenArr.
    #Also, it's funny how when stepping through code, the stepper bases off lines and if I add comments it will get confused. 
    print(f"lenArr: {lenArr}")
    print(f"arr: {arr}")
    print(f"arrEmpty: {arrEmpty}")
    print(f"l: {l}")

    #The next for loop is pretty much for the case when we have an odd number of sublists and we have 1 sublist that won't 
    #be merged that round. The pointer l will be pointing to the beginning item of the un-merging sublist. We shouldn't do anything 
    #to that sublist for that round so we can just copy it from the original to the arrEmpty. This is important because we are copying
    #the entire arrEmpty array into the arr next round, so we want to make sure arrEmpty has all the correct values. 
    for i in range(l, lenArr):
        print(f"i: {i}")
        arrEmpty[i] = arr[i]
    print(f"lenArr: {lenArr}")
    print(f"arr: {arr}")
    print(f"arrEmpty: {arrEmpty}")
    print(f"l: {l}")
    for j in range(0, lenArr):
        print(f"j: {j}")
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

