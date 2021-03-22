class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, a,n):
        # Your Code Here
        #Naive solution. 
        #Easiest optimization idea is to eliminate the necessity of the second loop. 
        '''
        result= 0
        for i in range(n):
            for j in range(i, n, 1):
                if a[i] > a[j]:
                    result += 1
        
        return result
        '''
        #I cannot simply modify based on previous. 
        '''
        result = 0
        temp = 0
        for i in range(n):
            if i==0:
                for j in range(i, n,1):
                    if a[i] > a[j]:
                        temp+=1
            
            else:
                if 
        '''
        result = [0]
        big = [0] * n
        self.mergesort(a, 0, n-1, result, big)
        
        return result[0]
        
    def mergesort(self, arr, l, h, result, big):
        #No need if it is the same. 
        if l < h:
            mid = (l+h) // 2
            self.mergesort(arr, l, mid, result, big)
            self.mergesort(arr, mid+1, h, result, big)
            
            #I can just pass a mutable array with one number (which is the result count. )
            self.merge(arr, l, mid, h, result, big)
            
    def merge(self, arr, l, m, h, result, big):
        lenLM = m-l + 1
        lenMH = h-m
        
        #!Somehow exceeds time limit so add some merge sort optimizations. 
        #*Use a big array instead of extra arrays. 
        #LM = [0] * lenLM
        #MH = [0] * lenMH
        
        #Copy into the temporary arrays. 
        #*Have to change the range so copies in correct place. 
        for i in range(l, m+1):
            big[i] = arr[i]
            
        for j in range(m+1,h+1):
            big[j] = arr[j]
        
        #I can calculate the remianing length by subracting the pointer value from the length. 
        i = l
        j = m+1
        #In place sort so start right away
        k = l
        #!GFG accepts some times and not others so I have to waste the time bruh. 
        while i < m+1 and j < h+1:
            if big[i] <= big[j]:
                #Modifying the original array
                #We start changing from the beginning of the array starting at index k
                arr[k] = big[i]
                i += 1
            else:
                arr[k] = big[j]
                #I have to do the calculation here. 
                #Have to do this step based on i
                result[0] += (m+1-i)
                j += 1
            k += 1
            
        while i < lenLM:
            #Nothing to compare with
            arr[k] = big[i]
            i += 1
            k += 1
    
        while j < lenMH:
            arr[k] = big[j]
            j += 1
            k += 1
        
a = Solution()
print(a.inversionCount([4, 5, 1, 2, 8, 3, 9], 7))


#{ 
#  Driver Code Starts
#Initial Template for Python 3
'''
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends
'''