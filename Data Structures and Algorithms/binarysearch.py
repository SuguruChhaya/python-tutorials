#Practice of binary search recursion
#Even though the array will be reused, we must have a clear lowerbound and upperbound. 
def binaryRecur(arr, value, lowerbound, upperbound):
    if lowerbound <= upperbound:
        mid = int((lowerbound + upperbound) / 2)
        if arr[mid] == value:
            print('1')
            return mid
        elif arr[mid] > value:
            print('2')
            upperbound = mid - 1
        elif arr[mid] < value:
            print('3')
            lowerbound = mid + 1
        #I have to return a value or else nothing recursion doesn't work properly. 
        print(arr)
        return binaryRecur(arr, value, lowerbound=lowerbound, upperbound=upperbound)
        

    else:
        return None

#!OBVIOUSLY, I forget that a binary search tree list has to be sorted. LOL wasted 45 minutes on this. 
arr1 = sorted([2, 3, 1, 67, 74, 3])
print(binaryRecur(arr1, 3, 0, len(arr1) -1))


def recursiveBinary(input_array, value, lowerbound, upperbound):

    if lowerbound <= upperbound:
        mid = int((lowerbound + upperbound) / 2)
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            lowerbound = mid + 1
            return recursiveBinary(input_array=input_array, value=value, lowerbound=lowerbound, upperbound=upperbound)

        else:
            upperbound = mid - 1
            #This +1 thing isn't working so I have to adjust. 
            return recursiveBinary(input_array=input_array, value=value, lowerbound=lowerbound, upperbound=upperbound)
    else:
        return None


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
test_val3 = 1
test_val4 = 29
print(recursiveBinary(input_array=test_list, value=test_val1, lowerbound=0, upperbound=len(test_list)-1))
print(recursiveBinary(input_array=test_list, value=test_val2, lowerbound=0, upperbound=len(test_list)-1))
print(recursiveBinary(input_array=test_list, value=test_val3, lowerbound=0, upperbound=len(test_list)-1))
print(recursiveBinary(input_array=test_list, value=test_val4, lowerbound=0, upperbound=len(test_list)-1)) 
