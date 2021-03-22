#*Based on striver's explanations, there are 2 more different types of problem types for pascal's triangle. 

#*Leetcode problem is obviously O(n**2) complexity. 
#*Finding just the value at the row numbers and column number. 

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)
def findValue(row, column):
    #*First check for special cases. 
    if row == 1 or column == 1 or column == row:
        return 1
    return int(factorial(row-1)/ (factorial(column-1) * factorial((row-1)-(column-1))))

def findRow(row):
    num = 1
    result = [1]
    #*O(n) solution without solving solving everything.     
    for i in range(row-1):
        num *= (row-1-i)
        num /= (i+1)
        result.append(int(num))

    return result

#print(findValue(5, 5))

print(findRow(5))