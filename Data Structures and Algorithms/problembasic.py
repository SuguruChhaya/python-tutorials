#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. STRING_ARRAY labels
#  3. INTEGER dailyCount
#

def maxCost(cost, labels, dailyCount):
    # Write your code here
    finalCost = 0
    #Pointing at a certain index on cost and labels
    pointer = 0
    #Going to store how many were produced in that specific day. After day end, switch back to 0. 
    dayCount = 0
    #List to store daycount for everyday
    dayCountList = [0] * len(cost)
    #First we have to make sure we get through all laptops
    remove = False
    while pointer <len(cost):
        #Then we should check whether the dailyCount is met.
        tempCost = 0
        while dayCount < dailyCount:
            #I need a way so that I don't get stuck in this loop.
            #That is going to happen when pointer finally exceeds len(cost) inside this loop.
            #To prevent this, I will first store daily costs in a list. 
            #If I realize that I am stuck at the end, I will remove the last element since it doesn't count toward the final cost. 
            if pointer >= len(cost):
                #I will eventually have to do something here. 
                #I should have a variable that turns true so that I can remove the final item from the list. 
                remove = True
                break
            if labels[pointer] == 'legal':
                dayCount += 1
            #I shouldn't just add the finalCost right away but set it in the list. 
            tempCost += cost[pointer]
            pointer += 1

        if remove == False:
            #Pointer is adding wrong value. Since I just added 1 to pointer, I need to do pointer-1
            #Since the first day is day 0 and my list could go out of index, pointer-1 
            #!I need to add a temporary cost because in this case, only the legal one's cost is added. 
            dayCountList[pointer-1] += tempCost

        remove = False
            
        #Once I break from this loop, I have to  reset dayCount
        dayCount =0
        
    return max(dayCountList)
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cost_count = int(input().strip())

    cost = []

    for _ in range(cost_count):
        cost_item = int(input().strip())
        cost.append(cost_item)

    labels_count = int(input().strip())

    labels = []

    for _ in range(labels_count):
        labels_item = input()
        labels.append(labels_item)

    dailyCount = int(input().strip())

    result = maxCost(cost, labels, dailyCount)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
