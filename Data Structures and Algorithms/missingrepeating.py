#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        #I think I saw a version where I check it as negative to check that I saw it. 
        #However, I will first put it in set and 
        
        #Finding the missing will be quite easy but finding the duplicate will be harder. 
        a = set(arr)
        sumArr = sum(arr)
        
        #Calculate the correct sum mathematically
        sumCorrect = int((1+n) * n / 2)
        print(sumCorrect)
        
        for i in range(1,n+1):
            if i not in a:
                #Do the calculation. 
                return [i+(sumArr-sumCorrect), i]

a = Solution()
b = a.findTwoElement([2,2], 2)
print(b)