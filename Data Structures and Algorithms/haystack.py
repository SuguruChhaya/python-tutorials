class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        #"", "a" -> -1
        if len(needle) == 0:
            return 0
        elif len(haystack)==0:
            return -1
        elif len(needle) > len(haystack):
            return 0
        
        #I think I can kind of use the 2 pointer method. 
        haystackPointer = 0
        #I need 2 pointers to loop and check. 
        needlePointer = 0
        
        #I guess one thing to note is that both haystack and needle could be 0. 
        for i in range(len(haystack)):
            #I need to first check whether the pointer will be in range or not. 
            
            while haystackPointer < len(haystack) and haystack[haystackPointer] == needle[needlePointer]:
                needlePointer += 1
                haystackPointer += 1
                if needlePointer == len(needle):
                    #I think I can return the index based on the current value of haystackPointer. 
                    return haystackPointer - len(needle)
                
                
            needlePointer = 0
            haystackPointer += 1
        
        
        return -1
        '''
        '''
        #!The previous issue I had was once I get through, I cannot check anything intermediate. Therefore, I should first check only for first element. 
        if len(needle) == 0:
            return 0
        elif len(haystack)==0 or len(needle)>len(haystack):
            return -1

        possibilities = []
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                possibilities.append(i)

        for a in possibilities:
            #*Start checking
            b = a
            #Needle pointer
            c = 0
            #*We also have to make sure index is in range
            while b < len(haystack) and b < a + len(needle) and haystack[b] == needle[c]:
                #*In the loop, I want to return true. 
                if c + 1 == len(needle):
                    #*Original index
                    return a
                b += 1
                c += 1
        return -1
        '''
        #This approach definitely does work but checking so many times is very annoying. 

        #*When adding in possibilities I can do a quick check for length and whether the last elements match. 
        #*This might get rid of a lot of clearly wrong options. 

        #!The previous issue I had was once I get through, I cannot check anything intermediate. Therefore, I should first check only for first element. 
        if len(needle) == 0:
            return 0
        elif len(haystack)==0 or len(needle)>len(haystack):
            return -1

        possibilities = []
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and i+len(needle)-1 < len(haystack) and haystack[i+len(needle)-1] == needle[-1]:
                possibilities.append(i)

        for a in possibilities:
            #*Start checking
            b = a
            #Needle pointer
            c = 0
            #*We also have to make sure index is in range
            while b < len(haystack) and b < a + len(needle) and haystack[b] == needle[c]:
                #*In the loop, I want to return true. 
                if c + 1 == len(needle):
                    #*Original index
                    return a
                b += 1
                c += 1
        return -1


a = Solution()
print(a.strStr("mississippi", "issip")) 