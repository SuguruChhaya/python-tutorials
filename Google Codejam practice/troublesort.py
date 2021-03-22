
#!Doesn't work for cases like 8, 9, 7 which makes sense. 

#*Really easy problem since I just have to run trouble sort and compare it with a manually sorted array. 
'''
def main(arr):
    #*Convert all elements into integer. 
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    #Copy of usually sorted array. 
    correct = sorted(arr)

    #!The trick is that many people will end up doing trouble sort and not realize easier way. 
    #Trouble sort
    done = False
    while done == False:
        done = True
        for i in range(0, len(arr)-2, 1):
            if arr[i] > arr[i+2]:
                done = False

                arr[i], arr[i+2] = arr[i+2], arr[i]
    
    for i in range(len(correct)):
        if correct[i] != arr[i]:
            return i

    return "OK"
'''

def main(arr):

    #*First convert all to integers so I can correctly sort all of them. 
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    #*Then create a list comprising of the odd indices and even indices. 
    correct = sorted(arr)
    even = []
    odd = []
    #!To shave off time, I can just do it with 1 pass. 
    #!I don't understand why case 2 just ends up with an OK.
    for i in range(0, len(arr), 1):
        if i % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])

    even.sort()
    odd.sort()

    #Merge them like merge sort with complexity of O(m+n)
    #!We aren't doing merge sort!! (Cuz if I do, it will always be sorted in correct order)
    #*Instead we are intertwining the arrays. 
    merged = []
    a = 0
    b = 0
    oddPointer = 0
    for i in even:
        merged.append(i)
        if oddPointer < len(odd):
            merged.append(odd[oddPointer])
            oddPointer += 1

    for i in range(len(merged)):
        if correct[i] != merged[i]:
            return i
    return "OK"


numTests = int(input())
for i in range(numTests):
    #The second input doesn't really matter. 
    a = input()
    arr = input().split(" ")
    print(f"Case #{i+1}: {main(arr)}")