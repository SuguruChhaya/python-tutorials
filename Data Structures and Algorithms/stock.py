class Solution:
    def maxProfit(self, prices) -> int:
        #The intuition is quite simple: find 2 elements with the greates difference where the earlier element is larger. 
        #maxProfit = 0
        #Brute force is easy to implement.
        #Obviously time limit exceeded. 
        '''
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                maxProfit = max(maxProfit, prices[j]-prices[i])
                
        return maxProfit
        '''
        
        #My intuition is kind of traversing from the back and shifting to find a better option or kind of like sliding window. 
        
        #Find the upper point and lower points. 
        maxList = []
        minList = []
        for i in range(len(prices)):
            if i == 0:
                if prices[i] >= prices[i+1]:
                    maxList.append(i)
                elif prices[i] <= prices[i+1]:
                    minList.append(i)
            elif i == len(prices)-1:
                if prices[i] <= prices[i-1]:
                    minList.append(i)
                elif prices[i] >= prices[i-1]:
                    maxList.append(i)
                    
            else:
                if prices[i] >= prices[i-1] and prices[i] >= prices[i+1]:
                    maxList.append(i)
                elif prices[i] <= prices[i-1] and prices[i] <= prices[i+1]:
                    minList.append(i)
                    
        result = 0
        for i in range(len(minList)):
            for j in range(len(maxList)-1, -1, -1):
                #!First have to check whether in minList position is smaller. 
                if minList[i] < maxList[j]:
                    result = max(prices[maxList[j]]-prices[minList[i]], result)
                else:
                    break
        return result

a = Solution()
print(a.maxProfit([2, 2, 5]))