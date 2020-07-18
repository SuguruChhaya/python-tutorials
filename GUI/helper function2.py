def recognizer(string):
    recognize = []
    for char in range(0, len(string)):
        if string[char] == "+" or string[char] == "-" or \
            string[char] == "*" or string[char] == "/":
            recognize.append(char)
    return recognize


print(recognizer("2+3*"))