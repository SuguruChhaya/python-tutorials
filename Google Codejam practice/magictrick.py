
#*With the first try, the magician already limited his options to 4 cards. He then separed these 4 cards to different rows and got the correct one. 

#*Pretty easy to determine. 


def main(firstCorrect, firstArr, secondCorrect, secondArr):
    #*Some kind of data structure that can store all elements in a given row. 
    #*Since no duplicate elements, set would be fine. 
    firstList = []
    for i in firstArr[firstCorrect-1]:
        firstList.append(i)
    
    #Stores the rows every element 
    #!I think I can first check whether volunteer cheated because that is easier. 
    secondList = []
    for j in secondArr[secondCorrect-1]:
        secondList.append(j)

    #*Really, the point is not to check whether there is an intersection but rather to check how many. 
    #0-> Volunteer cheated. 
    #1-> Correct element
    #2-> Bad magician. 

    #!I think ran than running this algorithm in O(n**2) complexity, I can run it in O(2nlog(n) + m+n) time by sorting and advancing pointers. 
    #*To do so, I need to use a list instead of set. 
    #*Because 
    common = []

    firstList.sort()
    secondList.sort()
    
    a = 0
    b = 0
    while a < len(firstList) and b < len(secondList):
        if firstList[a] == secondList[b]:
            common.append(firstList[a])
            a += 1
            b += 1
        elif firstList[a] < secondList[b]:
            a += 1
        else:
            b += 1
    
    
    #*False negative. 
    if len(common) == 1:
        return common[0]
    elif len(common) == 0:
        return "Volunteer cheated!"
    elif len(common) >= 2:
        return "Bad magician!"

numTests = int(input())
for i in range(numTests):
    firstCorrect = int(input())
    firstArr = []
    for a in range(4):
        firstArr.append(input().split(" "))
        '''
        #*Converts everything into an integer. Maybe not necessary. 
        for j in range(4):
            firstArr[-1][j] = int(firstArr[-1][j])
        '''
    secondCorrect = int(input())
    secondArr = []
    for b in range(4):
        secondArr.append(input().split(" "))
    

    
    print(f"Case #{i+1}: {main(firstCorrect, firstArr, secondCorrect, secondArr)}")