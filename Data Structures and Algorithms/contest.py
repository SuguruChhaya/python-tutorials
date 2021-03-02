
'''
word1 = "cacb"
word2 = "cbba"

sub1 = []
sub2 = []
for i in range(len(word1)):
    for j in range(len(word1)+1):
        sub1.append(word1[i:j])

for a in range(len(word2)):
    for b in range(len(word2)+1):
        sub2.append(word2[a:b])
        
pList = []
for a in range(len(sub1)):
    full = sub1[a][::-1]
    part = sub1[a][:-1][::-1]
    for b in range(len(sub2)):
        if full in sub2[b]:
            pList.append(sub1[a] + full)
        elif part in sub2[b]:
            pList.append(sub1[a] + part)
            
maxLen = 0
for item in pList:
    if len(item) > maxLen:
        maxLen = len(item)
        
print(maxLen)
'''
class Solution:
    def maximumScore(self, nums, multipliers) -> int:
        #Since we want the maximum value and the value from multipliers is fixed, I can just try multiplying with both the beginning and the end and see which one comes out to be larger. 
        #I honestly think there will be a possibility for picking bad option now to get better option later but I won't consider that for now. 
        '''
        score = 0
        for i in range(len(multipliers)):
            start = nums[0] * multipliers[i]
            end = nums[-1] * multipliers[i]
            if start >= end:
                score += start
                nums = nums[1:]
            else:
                score += end
                nums = nums[:len(nums)-1]
                
        return score
        '''
        #I cannot really see the max value, thats the thing. 
        return self.maxRecursion(nums, multipliers, 0, 0, len(nums)-1)
    
    #The key here is to be able to recognize whether being greedy right now will be helpful or no. 
    #If I don't come up with any inspiration, I will just submit. 
    
    #Maximum score possible after performing given operations on an Array
    #Uses the concept of prefix sum array?
    #Concept similar to https://www.geeksforgeeks.org/maximum-score-possible-after-performing-given-operations-on-an-array/
    
        #For recursion, I will define another function with additional values for indices. 
        #I am not too sure about the one indexed thing
        
    def maxRecursion(self, nums, multipliers, multiplierIndex, start, end):
        if start > end or multiplierIndex >= len(multipliers):
            return 0
        
        #Just checking whether only one element remains or not. 
        #if start - 1 >= 0:
        choose_start = nums[start] * multipliers[multiplierIndex] + self.maxRecursion(nums, multipliers, multiplierIndex+1, start+1, end)
        choose_end = nums[end] * multipliers[multiplierIndex] + self.maxRecursion(nums, multipliers, multiplierIndex+1, start, end-1)
        larger = max(choose_start, choose_end)
        '''
        else:
            choose_start = nums[start] * multipliers[multiplierIndex] + self.maxRecursion(nums, multipliers, multiplierIndex+1, start+1, end)
            #There is really only one option
            larger = nums[start] * multipliers[multiplierIndex] + self.maxRecursion(nums, multipliers, multiplierIndex+1, start+1, end)
        '''
        return larger


a = Solution()
a.maximumScore([1, 2, 3], [3, 2, 1])
            
            
                