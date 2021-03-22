class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Supposed to do an in-place sort, I need a variable that stores the replaced value so I don't lose it. 
        #(x, y) -> (y, maxColumn-x) probably works for everything. 
        '''
        rowLen = len(matrix)
        columnLen = len(matrix[0])
        
        temp = matrix[0][0]
        #I cannot go in order. If I replace a value, I have to look at that value next otherwise no point in storing that value. 
        #The time complexity is rowLen*columnLen so I can use that as forloop counter. 
        row = 0
        column = 0
        #!This kind of motion is problematic because it will only land on the edge corners and keep going. And I don't know how to effectively make it switch. 
    
        for i in range(rowLen*columnLen):
            temp, matrix[column][columnLen-1-row] = matrix[column][columnLen-1-row], temp
            row, column = column, columnLen-1-row
        '''

        #*At least solve it using brute force. 

        rowLen = len(matrix)
        columnLen = len(matrix[0])
        new = []
        for i in range(rowLen):
            temp = [0] * columnLen
            new.append(temp)

        for i in range(rowLen):
            for j in range(columnLen):
                new[j][columnLen-1-i] = matrix[i][j]

        matrix[:] = new
a = Solution()
arr=[[1,2,3],[4,5,6],[7,8,9]]
a.rotate(arr)
print(arr)