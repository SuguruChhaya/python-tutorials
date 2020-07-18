test = "53*25/40"


def open_position(string):
    open_pos = []
    for char in range(0, len(string)):
        if string[char] == "(":
            open_pos.append(char)
    return open_pos


a = open_position(test)
print(type(a))

def close_position(string):
    closed_pos = []
    for haha in range(0, len(string)):
        if string[haha] == ")":
            closed_pos.append(haha)
    return closed_pos


b = close_position(test)
print(type(b))

def bracket_matcher(open_pos, close_pos):
    if len(open_pos) == len(close_pos):
        difference = 10000
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


c = bracket_matcher(a, b)
print(c)
print(type(c))

def bracket_preparation(seq):
    new = []
    for item in seq:
        item[1] = int(item[1]) + 1
        new = new + [item]
    return new


d = bracket_preparation(c)
print(d)
print(type(d))

def all_recognizer(string):
    all = []
    for char in range(0, len(string)):
        if string[char] =="+" or\
            string[char] == "-" or\
                string[char] == "*" or\
                    string[char] == "/":
            all.append(char)
    return all

e = all_recognizer(test)
print(e)
print(type(e[0]))

def bedmas_recognizer(string):
    multiply = []
    divide = []
    add = []
    subtract = []
    for char in range(0, len(string)):
        if string[char] == "*":
            multiply.append(char)
        elif string[char] == "/":
            divide.append(char)
        elif string[char] == "+":
            add.append(char)
        elif string[char] == "-":
            subtract.append(char)
    return [multiply,divide,add,subtract]


f = bedmas_recognizer(test)
print(f)
print(type(f[0][0]))

#!These are times when classes are helpful because they can store info of wheter a sign
#!is for multiplication or division etc



            






