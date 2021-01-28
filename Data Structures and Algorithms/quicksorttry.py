#CS DOJO CODE without comments
def partition(arr, l, r):

    pivot = arr[r]
    
    i = l - 1

    
    for j in range(l, r+1) :

        if arr[j] <= pivot:
            i += 1

            arr[i], arr[j] = arr[j], arr[i]
        #?But my questions is: Why did we have to do this step separately? Can't we loop through all the elements including the pivot and modify the conditions a little bit so we don't have to do the extra step outside the for loop?
    #arr[i+1], arr[r] = arr[r], arr[i+1]

    #Adjusting the range and returning i works just fine. 
    #I haven't done a million tests on this so I am not completely sure but this code should work the same as previous
    #because the last element will always be switched in either case. I have to change i+1 to i because 1 will already be added to i at that point. 
    
    return i
    
def qs(arr, l, r):
    if l >= r:
        return None

    p = partition(arr, l, r)
    qs(arr, l, p-1)
    qs(arr, p+1, r)

arr = [1, 2, 3, 5, 4] 
n = len(arr) 
qs(arr, 0, n-1) 
print("Sorted array is:") 
for i in range(n):
    print("%d" % arr[i]), 

