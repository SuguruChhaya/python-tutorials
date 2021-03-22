
#*My guess for this problem is that I have swap any shoot with charge for the back because that is when shoot does more damage. 
#*Therefore, I can iterate from the back and swap any "CS" pattern to "SC". 

def main(largest, arr):
    result = 0
    #*Can change in place if I split into array. 
    #*When I make a modification, I should have a system that can calculate the new amount of damage without re-looping through the 10**9 characters. 

    #*To store info, I could build a hashtable but will cost so much memory. 
    #*Don't need to. Just subtract after linear traversal. 
    #*This problem has so many possiblilites for optimization. 
    #*Realistically, I could just start traversing from the last shooting so that I can prevent all the extra "C"s on the end. 
    #*If that is the one being switched, I can change the value too. 

    #Initial traversal to computer total. 
    #print(largest)
    #print(arr)
    laser = 1
    damage = 0
    for i in arr:
        if i=="S":
            damage += laser
        else:
            laser *= 2

    lastS = None
    lastSLaser = laser
    #*Going to find the laser value at the last S value. 
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == "S":
            lastS = i
            break
        else:
            lastSLaser /= 2
    #*If lastS is still none, that means no laser is being shot at so I can return 0. 
    #*Or if the damage is already less than largest
    if lastS == None or damage <= largest:
        return 0

    

    #!To effectively tell what is the current power stored, I must keep track of that in the first iteration. 
    #*NVM laser does that. 
    #*Because we start iteration from the last laser shot. 
    currLaser = lastSLaser
    #!The whole idea is to re-check from lastS but a forloop doesn't do so so while loop is better. 
    j = lastS
    while j > 0:
        if arr[j] == "S" and arr[j-1] == "C":
            #*Have to check whether it is the last element becasue if so, we have to adjust lastS.

            arr[j], arr[j-1] = arr[j-1], arr[j]
            damage -= (currLaser - currLaser/2)
            #!Modification of currLaser must come after I subtract damage. 
            if j == lastS:
                lastS -= 1
                #!I think currlaser should be changed here. 
                currLaser /= 2
            result += 1
            j = lastS
        elif arr[j] == "C":
            currLaser /= 2
            j-=1
        elif arr[j] == "S":
            j-=1
        if damage <= largest:
            return result
    return "IMPOSSIBLE"
    '''
    for j in range(lastS, 0, -1):
        if arr[j] == "S" and arr[j-1] == "C":
            #*Have to check whether it is the last element becasue if so, we have to adjust lastS.
            if j == lastS:
                j-=1
            arr[j], arr[j-1] = arr[j-1], arr[j]
            damage -= (currLaser - currLaser/2)
            result += 1
        elif arr[j] == "C":
            currLaser /= 2
        if damage <= largest:
            return result
    '''
    





numTests = int(input())
for i in range(numTests):
    a = input().split(" ")
    largest = int(a[0])

    #*Paste into array so that easy to modify in-place
    arr = []
    for j in a[1]:
        arr.append(j)
    #main(largest, arr)
    #a = main(largest)
    print(f"Case #{i+1}: {main(largest, arr)}")