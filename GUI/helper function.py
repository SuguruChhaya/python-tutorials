entry = "(2*(3+5))"
# I am trying to make something which can correspond open brackets with closed brackets.
# I have realized that the corresponding closed bracket is the closest closed bracket counting to
# the right of the open bracket.

def open_position(string):
    open_pos = []
    for char in range(0, len(string)):
        if string[char] == "(":
            open_pos.append(char)
    return open_pos

def close_position(string):
    closed_pos = []
    for haha in range(0, len(string)):
        if string[haha] == ")":
            closed_pos.append(haha)
    return closed_pos


def bracket_matcher(open_pos, close_pos):
    if len(open_pos) == len(close_pos):
        difference =10000
        final = []
        for close in close_pos:
            for open in open_pos:
                if int(close) - int(open) > 0 and\
                        int(close) - int(open) < difference:
                    difference = int(close) - int(open)
                    winner = [open, close]
            open_pos.remove(winner[0])
            final = final + [winner]
            difference = 100000
        return final
    else:
        return "Error"


print(bracket_matcher(open_position(entry), close_position(entry)))
#To be used for slicing, it must be open bracket index +1. close value 
#doesn't need change
#!First, the computer needs to recognize the signs, (just like brackets) 
#!to recognize numbers. For this, I will make a function which sorts the 
#!Breaking point.

def preparation(seq):
    new = []
    for item in seq:
        item[1] = int(item[1]) + 1
        new = new + [item]
    return new

print(preparation([[3,7],[0,8]]))










