import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    #If every sum ends up being smaller than 0, I can simply return 0. 
    #I obviously need an algorithm that finds the total number of patterns I can make. 
    #I think dynammic programming could be useful here if I store for example 3+2. This case when I calculate 3+2+5, I can just pick up the 3+2 part and do 5+5=10. 
    #I sus maybe this problem is kind of like the staircase problem. I just cannot go adjacent but I can go any further. 
    #However, the difference is that I don't neccesarily have to reach to the end of the list. I get to stop at every point I pass through. 
    #However, if I find the solutions to the one that reaches till the end, I can just subtract one element at a time and that will also be a possibility. 
    #Also we don't need to start at the beginning but we can start at any element except the last one and the second from last one. 
    #Just because I don't know if I am doing this right, I will first try naive recursive approach. 
    
    n = len(arr)
    #Create the dynamic programming storage array
    memo = [0, 0]
    memo[0] = max(0, arr[0])
    memo[1] = max(memo[0], arr[1])
    for i in range(2, n):
        memo.append(None)
    for i in range(2, n):
        #We are going to add the values
        memo[i] = max(memo[i-2]+arr[i], arr[i], memo[i-1])
    return memo[-1]
    
    #I want to try solving this recursively. 
    #Recursion is taking up too much time and failing all the big cases so I want to use memoization now. 
    
def maxSubsetIndex(arr, index, memo):
    if index == 0:
        memo[index] = max(0, arr[0])
        return memo[index]

    #I have to check all of them before doing the max thing. 
    #Checking for index-2 + current

    if memo[index-1] == -10001:
        memo[index-1] = maxSubsetIndex(arr, index-1, memo)
        
    if index == 1:
        memo[index] = max(arr[1], memo[index - 1])
        return memo[index]
        
    if memo[index-2] == -10001:
        memo[index-2] = maxSubsetIndex(arr, index-2, memo)
    
    memo[index] = max(memo[index-2] + arr[index], memo[index-1], arr[index])

    return memo[index]
    
def maxSubsetSum(arr):
    #Maybe this the computer is confused with the 0 vs None thing because in the super big testcases there are often negative numbers and numbers stay 0 so the computer recalculates it. 
    memo = [-10001] * len(arr)
    return    maxSubsetIndex(arr, len(arr)-1, memo)

    

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    print(res)
