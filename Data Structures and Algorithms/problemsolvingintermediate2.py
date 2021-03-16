
#*Sounds complcicated but not in reality. 
#*To save space and perform quicksort, I could use one big array and keep track of indices. 

def sortedSum(arr):
    #Rather than a quicksort nlogn solution, since in the big array everything until previous is sorted
    #I could just traverse linearly (or better maybe binary search for logn) to find where the element belongs and insert it there. 
    #Instead of insert, I traverse from the end and shift until we reach because .insert() will take a lot of time. 
    l = len(arr)

    copy = [0] * l
    sum = 0
    for end in range(l):
        backTraversal = end-1
        while backTraversal >= 0 and copy[backTraversal] > arr[end]:
            copy[backTraversal+1] = copy[backTraversal]
            backTraversal -= 1
        copy[backTraversal+1] = arr[end]
            
        for j in range(end+1):
            sum += (j+1) * copy[j]

    return sum % (10**9+7)

arr = [5, 9]
print(sortedSum(arr))