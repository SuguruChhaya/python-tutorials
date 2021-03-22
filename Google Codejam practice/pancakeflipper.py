
#*Sound a little challenging. 
#*Apprarantly the edges of the flipper must be included.

#*I think the obvious brute force is to create a long list and swap values one by one. 
#*Iterate and if not + then flip the consecutives. 


def main(arr, n):
    result = 0
    for i in range(len(arr)):
        if arr[i] == False:
            #If no more length, I can just return right away. 
            if i > len(arr) - n:
                return "IMPOSSIBLE"
            for j in range(i, i+n):
                arr[j] = not arr[j]
            result += 1
    
    return result
        

numTests = int(input())
for i in range(numTests):
    s = input().split(" ")
    arr = []
    for j in s[0]:
        #*Way easier if I do true and false. 
        if j == "+":
            arr.append(True)
        else:
            arr.append(False)

    print(f"Case #{i+1}: {main(arr, int(s[1]))}")