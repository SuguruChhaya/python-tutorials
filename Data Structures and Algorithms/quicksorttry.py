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

def merge(arr, l, m, r, arrEmpty):
    #We are going to create an empty array to merge the lists. 
    len_tempLM = m - l + 1
    #Don't have to add +1 because starts at m+1
    len_tempMR = r -m

    #Now the third optimization method in the video is trying to say that this step of making copies again and again can also be prevented by making a big copy of the original list once and reuse it. 
    
    #Copy the elements in the first subarray in the exact spots in the big array. 
    #m+1 because have to include m
    for i in range(l, m+1):
        arrEmpty[i] = arr[i]


    #initial index of the subarray IN THE EMPTY ARRAY. HAVE THE SAME POSITION AS IT WOULD IN ORIGINAL ARRAY. 
    i = l
    #Initial index of subarray2
    j = m+1
    #initial index of merged array
    k = l

    #We just have to go through the messy combinations. 

    #Scenario where we have to compare items from both arrays. 
    #We cannot make this <= because len_temp represents length of array while i and j represent indices. len_temp will always be 1 larger than max index. This way, we know we went through everything. 

    #r+1 corresponds to the end length of the beginning of the original array to end of the section we are sorting. Pretty much end index + 1, which is like length
    #i<m+1 because starting index of subarray1 in Empty array is l and ending is m. We want to go through all of them. 

    #Added if statement to check for special case
    if arrEmpty[m] <= arr[m+1]:
        print("special case")
        print(f"First portion: {arr[l]} to {arr[m]}")
        print(f"Second portion: {arr[m+1]} to {arr[r]}")
        #Just so I don't have to worry about modifying the following algorithm, I will properly increment the three variables I introduced. 
        while i < m+1:
            arr[k] = arr[i]
            i+=1
            j+=1
            k+=1
    while i < (m+1) and j < (r+1):
        if arrEmpty[i] <= arr[j]:
            #Modifying the original array
            #We start changing from the beginning of the array starting at index k
            arr[k] = arrEmpty[i]
            i += 1
        else:
            arr[k] = arr[j]
            j += 1
        k += 1

    while i < (m+1):
        #Nothing to compare with
        arr[k] = arrEmpty[i]
        i += 1
        k += 1

    while j < (r+1):
        arr[k] = arr[j]
        j += 1
        k += 1
    



def mergesort(arr, l, r, arrEmpty):
    if r <= l:
        return 
    mid = (l+r) // 2
    
    #*We are still always passing the original array into the merge method. The merge method just keeps making small changes. 

    mergesort(arr, l, mid, arrEmpty)
    mergesort(arr, mid+1, r, arrEmpty)
    merge(arr, l, mid, r, arrEmpty)