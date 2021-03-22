class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        if len(nums) == 1:
            return nums
        
        left = len(nums) - 2
        right = len(nums)-1
        
        #*Isn't as simple as just swapping 2 numbers next to each other. 
        while left >= 0:
            if nums[left] < nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                break
            left-=1
            right-=1
            
        if left == -1:
            nums.reverse()
        '''
        '''
        #My entire thought process is incorrect. 
        #If find the biggest value and whenever I encounter a smaller value I swap. 
        if len(nums)==1:
            return nums
        
        last = nums[-1]
        #Use a while loop to better track the numbers. 
        i = len(nums)-2
        while i >= 0:
            if nums[i] < last:
                nums[i], nums[-1] = nums[-1], nums[i]
                break
            i-=1
        
        if i == -1:
            nums.reverse()
        '''
            
        #Problem solving thought process:
        #The last bump must be very important. 
        #How about cases like 4675 -> actually, that's just 4765
        #Cases like 946874 are confusing too, they end up being 947468
        #Might have to sort somewhere...
        
        #Iterate from the back. 
        #Check i-1
        #Index of the first bump index
        first = None
        #Index of the last bump index
        last = None
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                first = i-1
                last = i
                break
        #No bump
        if first == None:
            #Just reverse it since max.
            nums.reverse()
            
        else:
            #Run another loop starting at last. 
            currPos = last
            #Check for larger than first but smallest as possible. 
            for i in range(last, len(nums)):
                #!I don't necessarily think they have to be in between eachother. 
                if nums[first] < nums[i] < nums[currPos]:
                    currPos = i
            
            nums[first], nums[currPos] = nums[currPos], nums[first]
            
            #Quicksort in-place
            self.quicksort(nums, last, len(nums)-1)
            
    def quicksort(self, nums, low, high):
        if low >= high:
            #Not actually meant to return. Just to break. 
            return
        
        p = self.partition(nums, low, high)
        self.quicksort(nums, low, p-1)
        self.quicksort(nums, p+1, high)
        
    def partition(self, nums, low, high):
        pivot = nums[high] 
        #pointer
        i = low - 1
        #Forever stuck at 2s and 1s. 
        for j in range(low, high):
            if nums[j] < pivot :
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        nums[i + 1], nums[high] = nums[high], nums[i+1]
        return i+1
    
    def nextPermutation(self, nums):
        #The brute force. 
        #Well how do I do the brute force tho?
        #Generate 
        #Check and give the next. 
        hasFound = False
        #I guess I was almost there. Reverse would take much less time than quicksort...
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                hasFound=True
                break
              
        if hasFound == False:
            nums.reverse()
            return
        #Can reuse value for i. 
        for j in range(len(nums)-1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
                
        #Reverse from i+1 till the end. 
        a = i+1
        b = len(nums)-1
        
        while a <= b:
            nums[a], nums[b] = nums[b], nums[a]
            a += 1
            b-=1
            
        #print(nums)

a=Solution()
a.nextPermutation([3, 2, 1])