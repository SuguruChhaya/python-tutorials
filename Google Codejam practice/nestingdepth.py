#My initial thought is to just put brackets around all at first and then look for )( pairs since I can eliminate these. 
'''
def main(s):
    new = []
    result = []
    result = []
    for i in range(len(s)):
        for opening in range(int(s[i])):
            new.append("(")
            result.append("(")

        new.append(s[i])
        result.append(s[i])
        for closing in range(int(s[i])):
            new.append(")")
            result.append(")")

    firstNum = 0
    lastNum = 0
    while lastNum < len(new):
        #Ahead pointer has to stop before end. 
        #!We have to make sure we know that we have settled to the last element. 
        if new[firstNum] == "(" or new[firstNum]==")":
            firstNum+=1
            lastNum+= 1

        #!Rather than deleting and runing the original array, I should copy the array blankify incorrect places. 
        else:
            #*Start the inward move or not. 
            #!I have to make sure lastNum is larger than firstNum. 
            if lastNum > firstNum and new[lastNum] != ")" and new[lastNum] != "(":
                #!Before going into the loop, I think I should store the location of lastNum just so I don't lose it. 
                temp = lastNum
                while firstNum < lastNum:
                    if new[firstNum] == ")" and new[lastNum] == "(":
                        result[firstNum] = ""
                        result[lastNum] = ""
                    firstNum += 1
                    lastNum -= 1
                firstNum = lastNum = temp
            else:
                lastNum += 1

    return "".join(result)

'''



'''
When I encounter a 1, we want to make nesting depth = 1 so we add a bracket. 
When we then reach 0, we want to make nesting depth 1-1=0 so we add 1 ending brace. 

(((3))1)
For this case we need to add 3-1=2 ending brackets. 

And to finish, as william mentioned, I have to pretend like a zero exists maybe add or maybe not. 
I think I should preserve the original string (check when I reach 0) and keep adding to the result string. 
'''

def main(s):
    nestingDepth = 0
    result = ""
    for i in range(len(s)):
        if int(s[i]) - nestingDepth > 0:
            result += "(" * (int(s[i])-nestingDepth)
        else:
            result += ")" * (nestingDepth-int(s[i]))
        result += s[i]  
        nestingDepth = int(s[i])

        #*After adding the result, I have to check if it is the last element. 
        if i == len(s) - 1:
            result += ")" * nestingDepth
    return result
                
 
numTestcases = int(input())
for i in range(numTestcases):
    string = input()
    print(f"Case #{i+1}: {main(string)}")