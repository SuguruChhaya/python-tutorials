def partitionHoare(arr, l, r):
    left_pointer = l
    right_pointer = r
    while left_pointer != right_pointer:
        
        #<= allows sorting of duplicates
        #Have to accomodate for duplicates or else they we will go through this whole while loop just stuck at
        # a duplicate and array won't be partitioned fully. 
        while (arr[left_pointer] <= arr[right_pointer] and left_pointer != right_pointer):
            left_pointer += 1

        arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]


        while (arr[left_pointer] <= arr[right_pointer] and left_pointer != right_pointer):
            right_pointer -= 1

    
        arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]

    return left_pointer


def qsHoare(arr, l, r):
    if l >= r:
        return None

    p = partitionHoare(arr, l, r)
    qsHoare(arr, l, p-1)
    qsHoare(arr, p+1, r)

arr1 = [10, 7, 8, 9, 1, 5]
arr2= [32, 23, 1, 423, 2]
arr3 = [1, 3, 1, 3, 2]
qsHoare(arr1, 0, len(arr1)-1) 
qsHoare(arr2, 0, len(arr2) - 1)
qsHoare(arr3, 0, len(arr3) - 1)
print("Sorted arr1 is:" + str(arr1)) 
print("Sorted arr2 is:" + str(arr2)) 
print("Sorted arr3 is:" + str(arr3)) 