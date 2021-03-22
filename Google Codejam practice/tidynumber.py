
#*Start from n and go backwards. I could split number into array and sort them and check if match sorted. 
#*But this won't work for big 10**18 data sets. 
#*Split into list. Subtract 1, make the next one into 9. but if already 9, don't subtract and just make next one 9. 
#*Actually, that doesn't work because what if I get like 9134. I would make it 9934 which is larger. 
#*If the number has already been made smaller, change boolean value to allow unlimited 9s. 
#*In fact, after one number changes, every thing else becomes 9 anyways. 

'''
def main(num):
    #*Split into array and modify. Cannot split integer so keep it as string. 
    #*Even when joining string format is preffered. 
    arr = []
    for i in num:
        arr.append(i)
    
    for i in range(len(num)-1, 0, -1):
        if int(arr[i]) < int(arr[i-1]):
            #*What if we run into a scenario like 111111111111111110
            #*Doesn't work for cases like 1000 because gives 900. 
            #*Might have to do another traversal. 
            arr[i] = "9"
            arr[i-1] = str(int(arr[i-1])-1)

    #*Do another traversal that checks for 
    #*What about edge cases like 1001
    #*I cannot just simply subtract 1 because then I will get negative elements. 
    #!I could continue with this method but I could also try to find the smallest number type that works. like 1, 11, 22, 33 and so on somehow. 
    #*I definitely have to do two pass. 
    #First pass for turning into 9. 
    #*Don't even continue subtracting. Once when one value has been turned into 9, just turn everything else into 9 as well. 
    #Second pass from the back 

    return int("".join(arr))
'''

def main(arr):
    turned9 = False
    for i in range(len(arr)):
        if turned9:
            arr[i] = "9"
        #*First check whether an element exists to the right of the element. 
        elif i + 1 < len(arr) and int(arr[i]) > int(arr[i+1]):
            arr[i] = str(int(arr[i])-1)
            arr[i+1] = "9"
            turned9 = True
    
    print(arr)


numTests = int(input())
for i in range(numTests):
    print(f"Case #{i+1}: {main(input())}")