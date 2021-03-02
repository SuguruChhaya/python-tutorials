class Solution:
    def findDisappearedNumbers(self, nums):
        #I am pretty sure I am supposed to utilize the fact that some elements appear twice. However, I don't know how, so I am going to use sets. 
        #Convert list into set for log(n) lookup and loop through range to check whether num exists. If it doesn't, add to separate array. 
        result = []
        
        new = set(nums)
        
        #I don't know what the error is for [1,1]
        #We need to store the length of the original list, not the set. 
        for i in range(1, len(nums)+1):
            if i not in new:
                result.append(i)
                
        return result

a = Solution()
print(a.findDisappearedNumbers([1,1]))