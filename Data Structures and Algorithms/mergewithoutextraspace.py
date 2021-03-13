#User function Template for python3
class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        #I think this is related to https://leetcode.com/problems/merge-sorted-array/ so will try that first. 
        
        #For the leetcode one, I had extra space. 
        '''
        new = []
        
        a1 = 0
        a2 = 0
        
        
        while a1 < n and a2 < m:
            if arr1[a1] < arr2[a2]:
                new.append(arr1[a1])
                a1+=1
            else:
                new.append(arr2[a2])
                a2+=1
        
        while a1 < n:
            new.append(arr1[a1])
            a1 += 1
        
        while a2 < m:
            new.append(arr2[a2])
            a2 += 1
        
        arr1[:] = new[:n]
        arr2[:] = new[n:]
        #print(arr1)
        #print(arr2)
        '''
        
        '''
        
        j = 0
        for i in range(n):
            arr1[i] = new[j]
            j+=1
            
        for a in range(m):
            arr2[a] = new[j]
            j += 1
        '''
        
        
        #Pointer for arr1
        #a1 = 0
        #Pointer for arr2
        '''
        a2 = 0

        #Traverse all elements in the first array. 
        for i in range(n):
            if arr1[i] > arr2[a2]:
                #First swap. 
                #?a2 might always just be 0.
                arr1[i], arr2[a2] = arr2[a2], arr1[i]
                tempVal = arr2[a2]
                #!We will always start at same value so no point just doing "<". If I do so, I will never loop. 
                while a2 < m and arr2[a2] <= tempVal:
                    a2 += 1
                arr2.insert(a2, tempVal)
                #!Have to delete. 
                del(arr2[0])
                a2 = 0
        '''
        
        #Another similar way from striver. I think I could do something similar from the beginning too. 
        for i in range(m-1, -1, -1):
            #Store value because it might get changed. 
            last = arr1[n-1]
            #Have to set to m-2 because we are going to push to the j+1 index and if I start at end I will go out of index. 
            j = n-2
            while (j>=0 and arr1[j] > arr2[i]):
                arr1[j+1] = arr1[j]
                j-=1
                
            #Reached the point where arr1 value is smaller than last element. 
            #Cannot swap for cases like [1,2], [3, 4] because j will remain at m-2
            #Swap for [8, 9], [1, 2]. But I don't know why I have to add last > arr2[i] because I think that is assumed. 
            #!This last > arr2[i] does play some kind of role!!
            if j!=n-2 or last > arr2[i]:
                arr1[j+1] = arr2[i]
                arr2[i] = last
                
            
a = Solution()
arr1 = [1, 5, 7]
arr2 = [2, 3, 9]

a.merge(arr1, arr2, len(arr1), len(arr2))
print(arr1)
print(arr2)

#?GFG sets this as solution but it still exceeds time. 


'''
#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends
'''

'''
3 confusing aspects of this problem that I noticed:

1. Does it matter which array I iterate over (arr1 or arr2)?
-> It doesn't matter. However, we have to deal with the 2 arrays differently. -> ACTUALLY DOES MATTER because cannot just choose any possibility. 
e.g. In striver's example, he iterated over arr1 (the first array). Notice how the arr1 gets naturally sorted, while striver had to manually sort arr2?
This is probably the key distinction between the iterated and non-iterated array. In the iterated array, values fit into their correct place one by one. 
However, in the non-iterated array, we just kind of dump an element from the iterated array (arr1 in video) and manually sort it. -> this statement is correct. 



Difference between striver's code and geeksforgeeks solution:
Geeks for geeks approach:
Iterate from behind (you could iterate from ahead, but checking condition changes)
1. Store the last element (because you might lose it in step 2)
2. Look for the correct place to insert arr2[i] in arr1 by looping from the end. Until we find the correct spot, shift the elements to the right to make space for incoming element. 
3. Insert the element from arr2 into the correct spot and insert the last element of arr1 into ith index of arr2. 

Striver's approach
Iterate from front (doesn't really matter which way you iterate from)
1. Swap arr1[i] and arr2[0] is arr2[i] < 
'''