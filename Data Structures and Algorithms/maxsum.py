    #If every sum ends up being smaller than 0, I can simply return 0. 
    #I obviously need an algorithm that finds the total number of patterns I can make. 
    #I think dynammic programming could be useful here if I store for example 3+2. This case when I calculate 3+2+5, I can just pick up the 3+2 part and do 5+5=10. 
    #I sus maybe this problem is kind of like the staircase problem. I just cannot go adjacent but I can go any further. 
    #However, the difference is that I don't neccesarily have to reach to the end of the list. I get to stop at every point I pass through. 
    #However, if I find the solutions to the one that reaches till the end, I can just subtract one element at a time and that will also be a possibility. 
    #Also we don't need to start at the beginning but we can start at any element except the last one and the second from last one. 
    #Just because I don't know if I am doing this right, I will first try naive recursive approach.
    #Another idea might be to find possibilities of getting from anywhere to the top. 
    #Then use the bottom up approach to find sums for all the intermediate parts while contributing to find paths for future paths. 
    #The little complicated part is that I do not just have to calculate the total # of possibilities this time. I have to save all the combinations. 
    #At every point, we get to move 2 all the way up to < len(arr)
    #I at least have to pick 2 elements because they have to be a sum?


    #Now I came up with a totally different approach of how I might be able to do this. 
    #Consider the array [0, 1, 2, 3, 4]. 
    #I first place a pointer at 4 and say, in how many different ways can I get here? 
    #Now I place a second pointer at 2 (we skip 3 because cannot be adjacent) and say "how many different ways can we go from 2 to 4?"
    #(in this example, there is only 1 way I can go from 2 to 4)
    #Then I ask, "how many different ways can I "

    #I came up with another possible way I could tackle this problem:)
    #The number of ways I can go from one index to that index + n index is always constant, no matter where the starting index is.
    #Then I record the possible way I can go... but than I have to check for the same thing anyways. 

def maxSubsetSum(arr):
    #Starting points can be all from start to (len - 2)th index
    sums = []
    #I wanted to make this nested that stores len(arr) number of nested lists contain more nested lists for the different numbers we can add based on that sequence starting on that specific number. 
    #At this point I can exclude len(arr)-1 and len(arr)-2
    nested = []
    for i in range(0, len(arr)-2):
        nested.append([])

    #This is the loop when I fill the nested list using bottom up. 
    for i in range(0, len(arr)-2):
        #We are going to try the staircase type thing for every of them.
        #Pointer is the starting point of counting up until the end. Since I don't want to mess with i, I copied the initial value.  
        pointer = i
        for j in range()
        









arr = [2, 5, 1, 6]
maxSubsetSum(arr)


#Answer approach. 
'''
When passing through the elements, I have 2 choices, either include it to get the maximum number, 
or exclude it and move on the next number. 
https://www.hackerrank.com/challenges/max-array-sum/editorial?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming 
So basically, 

One similarity between this and the staircase problem
1. Here, we are looking at sums. So we look at possibilities of sums until a certain index and choose maximum. 
2. In the staircase problem, we are looking at ways to get somewhere. So we look at at possibilities of ways we can get to a certain index (though we don't choose max and all). 
'''
