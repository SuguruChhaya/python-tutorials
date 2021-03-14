
class Solution:
    def maxSubArray(self, nums) -> int:
        #The obvious brute force is to calculate all possible contiguous sums. However, using my knowledge, I think I can make a prefix sum table and calculate all the prefix sums, do subtractions and find out. 
        #Don't know if I can do a sliding window approach though. 
        small = -9999999999
        l = len(nums)
        prefixTable = [nums[0]]
        for i in range(1, l):
            prefixTable.append(prefixTable[i-1] + nums[i])
            
        tempMax = -1
        #Store a bunch of indices
        indexTable = []
        
        #To prevent repetitiveness, control with a while loop. 
        low = 0
        while low < l:
            if low <= tempMax:
                indexTable.append(tempMax)
                low += 1
            else:
                tempMax = None
                for high in range(low, l):
                    #We cannot always count on it to be larger. We have to find over again. 
                    if tempMax==None or prefixTable[high] > prefixTable[tempMax]:
                        tempMax = high
                
        #print(prefixTable)      
        #print(indexTable)
            

        result = small
        for low in range(l):
            result = max(result, prefixTable[indexTable[low]] - prefixTable[low] + nums[low])

        print(result)


        '''
        result = small

        
        low = 0
        high = 0
        #For every forloop, I want to reach the position with the largest prefix sum. 
        for low in range(l):
            
            #If possible, I want to reduce this search for the highest value. 
            #I might be able to store the value of tempMax in a list with index and value. If smaller or equal to the index of tempMax, just calculate using that. 
            #If not, find again and replace tempMax.
            #Or I could just do this step outside of the forloop. 
            #if tempMax == small or 
            
            for high in range(low, l):
                tempMax = max(tempMax, [prefixTable[high])
            #Calculate 
            result = max(result, tempMax-table[low]+nums[low])
            
        return result
        '''
a=Solution()
arr = [5,4,-1,7,8]
a.maxSubArray(arr)

Kadane's algorithm. 

Carrying a sum of negative is no use since it will only reduce the value. 
max variable and sum value. Sum can be 0 is we traverse a negative. Max variable solely contains proper sum of subarrays. 
Intuition: keep carrying as long as it gives a positive sum. 
If the whole subarray carries a positive value, it will be worth keeping it and adding it to next possible positive values. This is the whole intuition. 

def maxSubArray(nums):
	sum = 0
	max = -9999999
	for i in nums:
		sum+=i
		max = max(sum, max)
		if sum < 0:
			sum=0

	return max


I kind of had a good starting intuition asking, "what's the maxium subarray ending at this index?" So think about ending. 
The way he explained it makes it sound a little different but finding max between [1, -3, 2] and [2] essentially asks whether [1, -3] ends up being positive or negative. 

maxCurrent = arr[0]
#The final best. 
maxGlobal = arr[0]

Have to start at 1 because maxCurrent is already initialized to arr[0]
for i in range(1, len(arr)):
	#Since both options include an A[i], it will definitely be contiguous. maxGlobal doesn't always have to be contiguous. 
	maxCurrent = max(A[i], maxCurrent+arr[i])
	if maxCurrent > maxGlobal:
		maxGlobal = maxCurrent

return maxGlobal

#Seems kind of similar to the sliding window problems but...

Dynamic programming approach with kadane algorithm. Important idea is what is max that ends here. Either continue with it or start new subarray. 

I noticed how many videos explain the process by saying temporaryMax = max(temporaryMax+arr[i], arr[i]). At first I was a little confused between what striver
explained and all the other guys but when I think about it, max(temporaryMax+arr[i], arr[i]) == arr[i] if and only if temporaryMax < 0 because if temporaryMax 
carries a negative value, there is no point adding it. So striver is basically touching on the same thing. 