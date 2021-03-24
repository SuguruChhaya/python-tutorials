#User function Template for python3
class Solution:
	def matSearch(self,matrix, N, M, X):
		# Complete this function
		#Brute force: look into everythin

        row = len(matrix)-1
        column = 0
        while row >= 0 and column < len(matrix[0]):
            if matrix[row][column] == X:
                return 1
            elif matrix[row][column] < X:
                column += 1
            elif matrix[row][column] >X:
                row -= 1
        return 0
		
		#Honestly, the only better solution I can come up with involves checking the endpoint of each ow 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

a = Solution()
arr = [[18], [21], [27], [38],[55],[67]]
print(a.matSearch(arr, len(arr), len(arr[0]), 55))

