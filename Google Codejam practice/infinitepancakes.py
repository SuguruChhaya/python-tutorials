
#*Objective: end breakfast as quickly as possible. 
#*Though sounds kind of difficult, the best strategy is to move half of the guy with the most pancakes to someone else. 

#*Cases
#1 2 1 7

#*I think the important numbers are the largest and 
#*The optimial solution would NEVER be to give pancakes with someone who already has them since more time to finish. 
#*To make sure everyone is working, optimal would be to make a move right away. 
#!Never is it mentioned that there will only be 1 special minute! Can have as many special minutes as possible. 
#*When will a special minute be beneficial?
#*It isn't necessarily the case that if the 1st and 2nd most pancake eaters are tied, not beneficial to spread pancakes. 
#*Because if I had 1000, 1000 for example, it would be dumb to let the 2 just eat. 
#*"if newmax+1 <=oldmax then beneficial" is kind of a flawed thought process because what about cases like
#25, 25, 25, 25? best way is to divide into 12, 13, 25, 25 first but that doesn't change the total. 
#*I want to code the brute force solution but HOW?
#*I cannot just focus on the the largest number because I also have to consider the other small numbers. 

#!NO WAY I am going to get this question. 

def main(arr):
    pass

numTests = int(input())
for i in range(numTests):
    a = input()
    arr = input().split(" ")
    for j in range(len(arr)):
        arr[j] = int(arr[j])
    print(f"Case #{i+1}: {main(arr)}")
