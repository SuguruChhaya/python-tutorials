class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        #There were several ideas here. 
        #1. Brute force where I set every element as a starting point, every following element as an ending point and looping through these indices and adding up the sum. -> use 3 for loops.
        #2. A better brute force in which I precompute the sum until that specific index. Use a formula to calculate sum between index. -> use 2 for loops. 
        #3. Do #2. except in binary search so that the time complexity gets reduced to logn instead of n. 
        #4. The slidingw window technique in which iterate through every starting point. Once the tail extends enough, the head starts to shorten. 
        '''
        #1. Brute force. passes 18/19 so correct
        large = 999999999999
        result = large
        l = len(nums)
        for a in range(l):
            for b in range(a, l):
                s = 0
                length = 0
                #probably have to do b+1 to include index b. 
                for c in range(a, b+1):
                    #Can naively add. 
                    s += nums[c]
                    length += 1
                if s >= target:
                    result = min(result, length)
                
        #I have to do a final check 
        if result == large:
            return 0
        return result
        '''
        
        #2. Improved brute force. Uses concept of prefix sum/culminative sum to prevent 3rd loop. 18/19 cases passed so correct.
        '''
        large = 99999999999
        result = large
        sums = [nums[0]]
        l = len(nums)
        for i in range(1, l):
            sums.append(nums[i] + sums[i-1])
        #print(sums)
        #prefix sum is calculated. 
        for a in range(l):
            for b in range(a, l):
                s = sums[b] - sums[a] + nums[a]
                if s >= target:
                    result = min(result, b-a+1)
                    
        if result == large:
            return 0
        return result
        '''
        
        #3. Using binary search instead of checking linearly. 
        large = 99999999999
        result = large
        sums = [nums[0]]
        l = len(nums)
        for i in range(1, l):
            sums.append(nums[i] + sums[i-1])
            
        print(sums)
            
        for a in range(l):
            start = a
            #End is initially at the end index
            end = l - 1

            while start <= end:
                #Have to define a midpoint. 
                mid = (start+end) // 2
                #Tricky: have to add from i to mid
                s = sums[mid] - sums[a] + nums[a]
                print(f"start: {start}")
                print(f"end: {end}")
                print(f"mid: {mid}")
                print(f"sums[mid]: {sums[mid]}")
                print(f"sums[i]: {sums[a]}")
                print(f"nums[i]: {nums[a]}")
                print(f"s:{s}")
                if s >= target:
                    #First possibly change result
                    #Length also involves i because total length. 
                    result = min(result, mid-a+1)
                    #Have to decrease end. 
                    '''
                    print(f"second start: {start}")
                    print(f"second end: {end}")
                    print(f"second mid: {mid}")
                    '''
                    end-=1

                else:
                    #Increase start
                    start = mid+1
        if result==large:
            return 0
        return result
    #Check binary search order

a = Solution()
print(a.minSubArrayLen(7, [2,3,1,2,4,3]))