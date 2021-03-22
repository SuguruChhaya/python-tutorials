
def main(arr):
    #*Maybe kind of use merge intervals-type thought process. 
    #*Definitely first sort the arr based on the starting time. 
    #!Have to covert all to integer. 
    #*Ultimately, I think I can make every element of arr len 4 and the fourth element contains "J" or "C". 
    #*At the end, I can sort the array based on the 3rd element. 

    for i in range(len(arr)):
        arr[i][0], arr[i][1] = int(arr[i][0]), int(arr[i][1])
    #print(arr)
    arr.sort()
    #*If I am going to store the information in the big array, I just need to store the end time.

    julieEnd = 0    
    cameronEnd = 0

    #Loop through every element in the array and add them if the starting value is larger than ending value. 
    #*Start looking with julie. 

    
    for i in arr:

        if i[0] >= julieEnd:
            julieEnd = i[1]
            i[3] = "J"
        #*Otherwise check cameron. 
        elif i[0] >= cameronEnd:
            cameronEnd = i[1]
            i[3] = "C"
        else:
            return "IMPOSSIBLE"
        #print(f"julieList: {julieArr}")
        #print(f"CameronList: {cameronArr}")
    #Sort based on index 2 element in each element. 
    arr.sort(key = lambda x: x[2])

    result = ""
    for i in arr:
        result += i[3]

    return result

numTestcases = int(input())

for i in range(numTestcases):
    numActivities = int(input())
    arr = []
    for j in range(numActivities):
        a = input().split(" ")
        a.append(j)
        a.append(None)
        arr.append(a)
        
    print(f"Case #{i+1}: {main(arr)}")

'''
One solution apprantly involves graphs so I won't worry about it. 

Apparantly the constraints matter when picking solutions. 

First sort activity by starting time. 

Maximum number of independent ranges?


#First handle all the input coming in: first forloop of william lin. 
def solve():
	iterate from the end of the array somehow. 

Creating a string to result. 
Errichto 
If cameron is available take it. 	

'''

#!I think the issue I might be facing is the returning order. 
#*I probably have to return them in the correct order as they were inputted. 
#*That explains why both william and errichto kept an index so it returns it correctly. 