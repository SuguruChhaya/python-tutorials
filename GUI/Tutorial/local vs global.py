total = 0  # This is global variable.
# Function definition is here


def sum(arg1, arg2):
    global total
    #!If you delete that global arguement above, the 'outside
    #!the function global total' value becomes 0
    #!"global" connects the 'total =0' part and changes it outside the function
    # Add both the parameters and return them."
    total = arg1 + arg2  # Here total is local variable.
    print("Inside the function local total : " + str(total))
    return total


# Now you can call sum function
sum(10, 20)
print("Outside the function global total : " + str(total))



def sum(num1, num2):
    print("I ran the function")
    final = num1 + num2
    return final


#!If you run the code below, without adding "print" doesn't print the "return part"
#!It only prints follows the instruction in the function except "return"
sum(1, 2)
print("")
print(sum(1, 2))
