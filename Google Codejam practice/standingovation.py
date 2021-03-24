
#!Try to think through what the wrong answer choice may be. 
#!Run slow loop through all example testcases. 

def main(s):
    numStanding = 0
    result = 0
    #prevResult = 0
    #!I don't even have to create prevResult. I can just add directly (just be careful not to add result)
    for i in range(len(s)):
        #!There isn't a guarantee that I have to check all the time!! I only have to check when there is a value of 1 or larger!!
        #!Overall, even if it is working, I think I should check whether it is working the way I intended it to work or not!!
        
        #*I don't even know what I am missing on. 
        if int(s[i]) > 0:
            if  numStanding >= i:
                #numStanding += int(s[i])
                pass

                #!We cannot reach to this point if there are 0 ppl at that shyness level. 
            else:
                #*If I REALLY want to do this, I should implement prevResult and add the increase, not result itself. 
                result += (i - numStanding)
                numStanding += (i-numStanding)
                #!Since I have now fixed the issue, I must add!
            numStanding += int(s[i])
            #prevResult = result
        
    return result

numTests = int(input())
for i in range(numTests):
    #I can really just ignore the first input
    arr = input().split(" ")
    print(f"Case #{i+1}: {main(arr[1])}")