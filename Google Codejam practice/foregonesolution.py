
#*I think the brute force is to try every single number and return the earliest that doesn't include 4. 

def main(num):
    #*Another cannot be 0. 
    '''
    for i in range(1, num):
        if "4" not in str(i) and "4" not in str(num-i):
            return i, num-i
    '''
    #!Correct but terrible time complexity solution. 
    #*A better solution: Everytime I see a 4, subtract 1 from face value and add it into the second value. 
    #!Should work because maximum of 1 edit. 
    
    #*Split the number and add into list so that I can access using index. 
    num = str(num)
    arr = []
    for i in range(len(num)):
        arr.append(num[i])
    #*The new array should have the same length as previous just that all elements will be 0 at first. 
    new = ["0"] * len(arr)
    for i in range(len(arr)):
        if arr[i] == "4":
            arr[i] = "3"
            new[i] = "1"

    #Simple but should work. 
    return int("".join(new)), int("".join(arr))

numTests = int(input())
for i in range(numTests):
    num = int(input())
    first, second = main(num)
    print(f"Case #{i+1}: {first} {second}")