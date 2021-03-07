class Solution:
    def spiralOrder(self, matrix):
        #Always stored in local storage.
        #!Have to first check whether certain things exist
        if matrix == None or len(matrix)==0 or len(matrix[0])==0:
            return matrix
        row = 0
        column = 0
        allEdges = set()
        allEdges.add((0, 0))
        #print(allEdges)
        allEdges.add((0, len(matrix[0])))
        allEdges.add((len(matrix), len(matrix[0])-1))
        allEdges.add((len(matrix)-1, -1))
        rowIncrease = 0
        columnIncrease = 1
        result = []
        
        while True:
            result.append(matrix[row][column])
            allEdges.add((row, column))
            #!We won't know whether they will be in edges so I think I should just store all places I have gone to. 
            if (row+rowIncrease, column + columnIncrease) in allEdges:
                #*Since the next is an edge, we want to add to edges

                if [rowIncrease, columnIncrease] == [-1, 0]:# or [rowIncrease, columnIncrease] == [0, 0] or 
                    rowIncrease, columnIncrease = 0, 1
                elif [rowIncrease, columnIncrease] == [0, 1]:
                    rowIncrease, columnIncrease = 1, 0
                elif [rowIncrease, columnIncrease] == [1, 0]:
                    rowIncrease, columnIncrease = 0, -1

                elif [rowIncrease, columnIncrease] == [0, -1]:
                    rowIncrease, columnIncrease = -1, 0
                '''
                elif [rowIncrease, columnIncrease] == [-1, 0]:
                    rowIncrease, columnIncrease = 0, 1
                '''
                if (row+rowIncrease, column+columnIncrease) in allEdges:
                    break

            #!I think all elements must have the increases added to them. 

            row += rowIncrease
            column += columnIncrease

        return result

a = Solution()
#!1 column matrices aren't working because of default. 
print(a.spiralOrder([[1], [3]]))