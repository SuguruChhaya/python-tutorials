class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        #*The brute force approach will be do copy everything and then linear traverse -> O(m*n * 2)
        arr = []
        for row in matrix:
            for item in row:
                arr.append(item)
                
        '''
        for item in arr:
            if item == target:
                return True
        return False
        '''
        
        #To make better, I can do this in binary search. 
        low = 0
        high = len(arr)-1
        
        while low <= high:
            mid = (low+high) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid+1
            elif arr[mid] > target:
                high = mid-1
        
        return False
    
arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
a = Solution()
a.searchMatrix(arr, target)