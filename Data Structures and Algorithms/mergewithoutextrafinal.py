#The different concerns
#1. Whether to iterate from the left or the right
#2. Whether to iterate the first array or the second array. (Goes hand in hand with #1)
#3. Whether place then figure out its correct location or figure out correct location then place

class Solution:
    #!When iterating from the left, I must choose to iterate over arr1 because I need to lock in the smallest values. 
    
    #Iterate from left, iterate the first array and place value then figure out correct position. 
    #This is the method striver used in his video. 
    def s1(self, arr1, arr2, m, n):
        for i in range(m):
            if arr1[i] > arr2[0]:
                arr1[i], arr2[0] = arr2[0], arr1[i]
                j = 0
                #>= because have to get through the first element
                while j < n and arr2[0] >= arr2[j]:
                    j += 1
                arr2.insert(j, arr2[0])
                del(arr2[0])

    #Iterate from the left, iterate the first array and figure out the correct order then place the value. 
    def s2(self, arr1, arr2, m, n):
        for i in range(m):
            last = arr2[0]
            #?Why can't we start at a 0? Because we are shifting everything to the left (we won't get index error for index -1 but we will get something different)
            j = 1
            while j<n and arr2[j] < arr1[i]:
                arr2[j-1] = arr2[j]
                j+=1
            
            #For the case of j!=1, arr2[j] and arr2[j-1] will be duplicates. 
            if (j != 1 or last < arr1[i]):
                arr2[j-1] = arr1[i]
                arr1[i] = last

    #!When iterating from the right, I must choose to iterate over arr2 because I need to lock in the largest values. 
    
    #Iterate from the right. Iterate the second array and place value then figure out the correct position. 
    def s3(self, arr1, arr2, m, n):
        for i in range(n-1, -1, -1):
            if arr2[i] < arr1[-1]: #Or arr1[m-1]
                arr2[i], arr1[-1] = arr1[-1], arr2[i]
                j = m-1
                while j >=0 and arr1[-1] <= arr1[j]:
                    j -= 1
                #!A little different from previous case of insertion because inserting larger number
                arr1.insert(j+1, arr1[-1])
                del(arr1[-1])

    def s4(self, arr1, arr2, m, n):
        #*This is the solution provided by geeksforgeeks
        for i in range(n-1, -1, -1):
            last = arr1[m-1]
            j=m-2
            while(j >= 0 and arr1[j] > arr2[i]):
                arr1[j+1] = arr1[j]
                j-=1
            if (j != m-2 or last > arr2[i]):
                arr1[j+1] = arr2[i]
                arr2[i] = last
        

arr1 = [0, 1, 5, 7]
arr2 = [0, 2, 6, 8, 9]

test = Solution()
test.s1(arr1, arr2, len(arr1), len(arr2))

print(f"arr1: {arr1}")
print(f"arr2: {arr2}")