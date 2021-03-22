def main(matrix, numRows):
    diagonal = 0
    #diagonalSet = set()
    for i in range(numRows):
        diagonal += int(matrix[i][i])

    rowTotal = 0

    for i in range(numRows):
        #*Iterate over everything. 
        rowSet = set()
        #*Doesn't matter how many duplicates exist in the same row. Just need to check. 
        tempRow = 0
        for j in range(numRows):
            if matrix[i][j] in rowSet:
                tempRow = 1
            else:
                rowSet.add(matrix[i][j])  
        rowTotal += tempRow

    colTotal = 0
    for column in range(numRows):
        columnSet = set()
        tempCol = 0
        for row in range(numRows):
            if matrix[row][column] in columnSet:
                tempCol = 1
            else:
                columnSet.add(matrix[row][column])
        colTotal += tempCol
    
    return diagonal, rowTotal, colTotal


#!I have to be able to append to handle the data and place it into a 2D matrix. 
numTests = int(input())
for i in range(numTests):
    numRows = int(input())
    matrix = []
    for j in range(numRows):
        #I have to split the numbers and put them into list. 
        matrix.append(input().split(" "))

    diagonal, row, column = main(matrix, numRows)
    print(f"Case #{i+1}: {diagonal} {row} {column}")

#Improve my solution with william lin video. 

I don't necessarily have to add all the parenthesis at first. 
I can just use nesting depth logic like william lin is. 

