##string = "2*3/3"
#!e = [1,3]
#!bracket=[[1],[3],[],[]]

def divmul_calculation(bracket, bedmas, string, d):
    final = string
    if len(d) == 0:
        for multiply in bracket[0]:
            if len(bracket[1]) > 0:
                #! This for loop is a problem because it will iterate forever
                for divide_checker in range(0, len(bracket[1])):
                    if multiply < (bracket[1])[divide_checker]:
                        location = bedmas.index(multiply)
                    else:
                        pass
                    # ?"pass" might cause a bug so I have to look out
                if location == 0:
                    first_num = float(string[:multiply])
                    second_num = float(string[multiply + 1: int(bedmas[location + 1])])
                    result = first_num * second_num
                    final = final.replace(final[:bedmas[location + 1]], str(result))
                elif location == len(string) - 1:
                    first_num = float(string[(bedmas[location - 1]) + 1:multiply])
                    second_num = float(string[multiply + 1:])
                    result = first_num * second_num
                    final = final.replace(final[(bedmas[location - 1]) + 1:], str(result))
                else:
                    first_num = float(string[(bedmas[location - 1]) + 1:multiply])
                    second_num = float(string[multiply + 1: int(bedmas[location + 1])])
                    result = first_num * second_num
                    final = final.replace(final[(bedmas[location - 1]) + 1: bedmas[location + 1]], str(result))
    return final
    #!I have to make a global or local variable to make changes.
#! The problem is not division producing a float number, it is easy to int that.
print(divmul_calculation([[1,3], [5], [], []], [1, 3,5], "2*3*3/2", []))
##string = "2*3/3"
#!e = [1,3]
#!bracket=[[1],[3],[],[]]