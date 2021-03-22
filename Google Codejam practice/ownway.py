#*I do have to find the shortest path that exists. -> No! All paths are the shortest. 


#*2 approaches. 
#*Generate multiple paths and see which one has no matches with prev. -> Might take time. 
#* I notice that if she takes a east move, I can simply take a south move and that will work. 
#*Kind of symmetrical but reach goal. 

def main(prev):
    result = ""
    for i in prev:
        if i=="E":
            result += "S"
        else:
            result += "E"
    return result

numTests = int(input())
for i in range(numTests):
    a = input()
    print(f"Case #{i+1}: {main(input())}")
