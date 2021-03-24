

#*What I noticed is that there are many of those "best strategy" type problems. 
#*What I can do after this is kind of review all of them and see whether there are commonalities between these types of questions. 
#*Just because there are so many of them. 

#*I think the idea here is to check every time I have an option to buy a farm and pre-calculate whether it will be faster to not get or get. 

def helper(c, f, x, currentNum, result, currentSpeed):
    #!Since these variables aren't mutable, I am going to change them in helper function and then return it. 
    #*We don't know if it changes yet so assign if needed
    currentSpeed += f #-> 
    #currentNum = 0
    return x / currentSpeed

def main(c, f, x):
    c, f, x = float(c), float(f), float(x)
    currentNum = 0
    result = 0
    currentSpeed = 2

    #!I don't think less than x will be that accurate because we might go a lot over goal line and we might have some extra time. 
    #*After exiting subtract the time. 
    while currentNum < x:
        #!It doesn't really make sense to calculate ahead and then not use the value so might want to create helper function for that. 
        #*First check whether we can buy farm. 
        if currentNum >= c:
            #*Deduct overtime and reset position. 
            result -= (currentNum - c) / currentSpeed
            currentNum = c
            withoutBuy = (x-currentNum) / currentSpeed
            withBuy = helper(c, f, x, currentNum, result, currentSpeed)
            if withoutBuy < withBuy:
                #*Go without it and exit. 
                result += withoutBuy
                return round(result, 7)
            else:
                currentSpeed += f
                #result += withBuy -> Shouldn't add at this point because might have to go through more checking
                #!We still cannot return the result because we might have to go for another farm. 
                currentNum = 0
                #return result
        else:
            currentNum += currentSpeed #*I suspect that currentNum is often tipping over c for example 32 and 30 so it takes somemore time. Whenever I check, I should deduct the overtime. 
            result += 1

    result -= (currentNum - x) / currentSpeed
    return round(result, 7)


numTests = int(input())
for i in range(numTests):
    c, f, x = input().split(" ")
    print(f"Case #{i+1}: {main(c, f, x)}")