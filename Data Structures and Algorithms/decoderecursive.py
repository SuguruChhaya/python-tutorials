def decodeHelper(root, s, originalNode, finalString):
    #Accomodating for the final case. 
    if len(s) == 0:
        if root.data != None:
            finalString += root.data
            return finalString
            
    else:
        if root.left == None and root.right == None:
            finalString += root.data
            return decodeHelper(originalNode, s, originalNode, finalString)
        else:
            if s[0] == '0':
                return decodeHelper(root.left, s[1:], originalNode, finalString)
            else:
                return decodeHelper(root.right, s[1:], originalNode, finalString)

def decodeHuff(root, s):
    originalNode = root
    finalString = ""
    print(decodeHelper(root, s, originalNode, finalString))