class Solution:
	def matSearch(self,matrix, N, M, X):
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