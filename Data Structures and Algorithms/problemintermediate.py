#.1. Maximizing elements with constraints. 
#2. Equalizing array elements. 
#Maybe related: https://www.hackerrank.com/challenges/equality-in-a-array/problem

#
# Complete the 'maxElement' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER maxSum
#  3. INTEGER k
#

def maxElement(n, maxSum, k):
    # Write your code here
    #We can first set the largest element. 
    #Then we can try to add elements next to it based on the first one. 
    #We can first try maxSum for the index and decrement by 1 until we exit from the loop. 

    #First we obviously need to make make array.
    #Array is giving me memory error. 
    #!I mean if I tried, I could just store in variable and not array...
    tempSum = 99999999999999
    #arr = [99999999999999] * n
    
    tempMax = maxSum
    
    while tempSum > maxSum:
        #For every new time I am going through this loop, tempSum must be resetted. 
        tempSum = tempMax
        #tempSum = tempMax
        smallerCounter = tempMax - 1
        biggerCounter = tempMax - 1
        for i in range(k-1, -1, -1):
            #Decrement by 1
            tempSum += smallerCounter
            #Must consist of positive integers so if tempMax
            #!Remember that this excludes 0 as well
            if smallerCounter <= 1:
                pass
            else:
                smallerCounter -= 1

        
                
        for bigger in range(k+1, n, 1):
            tempSum += biggerCounter
            if smallerCounter <= 1:
                pass
            else:
                smallerCounter -= 1
        tempMax -= 1

    return tempMax+1

    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    maxSum = int(input().strip())

    k = int(input().strip())

    result = maxElement(n, maxSum, k)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()