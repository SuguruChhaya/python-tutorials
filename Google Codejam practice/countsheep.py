'''
def main(n):
    if n==0:
        return "INSOMNIA"
    seen = set()
    original = n
    n = str(n)
    i = 1
    #!The whole idea of until *10 will work might not be applying here. 
    #!Even inspecting 2, It must have been satisfied until 99 because otherwise it is probably the same thing agian. 
    #*But then this test condition fails for cases like 0 because it never goes ahead. 
    while len(n) - 1 <= len(str(original)):
        n = str(original * i)

        #Now iterate and add into set. 
        for j in n:
            seen.add(j)

        #*Since we are looking for last number, we can check here. 
        allThere = True
        for a in range(0, 10):
            if str(a) not in seen:
                allThere = False
                break

        if allThere:
            return n
        i+=1
'''

'''
I can know for sure that as soon as I reach the next P value: https://codingcompetitions.withgoogle.com/codejam/round/0000000000201bee/0000000000201c8a#analysis
I just have to run the value until I reach 9P because then leftmost value must have gone through all 1-9. 
So keep running until I reach that condition. 
'''

def main(n):
    if n==0:
        return "INSOMNIA"
    
    seen = set()
    original = n
    n = str(n)

    #*Find the smallest power of 10 that is larger or equal to the given number.
    i = 0
    while 10 ** i < original:
        i += 1
    
    maxReach = 9 * (10 ** i)
    j = 1
    while int(n) <= maxReach:
        n = str(original * j)
        for a in n:
            seen.add(a)
        
        allThere = True
        for b in range(0, 10):
            if str(b) not in seen:
                allThere = False
                break

        if allThere:
            return n
        j+=1

    return "INSOMNIA"
    
    

numTests=int(input())
for i in range(numTests):
    n = int(input())
    print(f"Case #{i+1}: {main(n)}")