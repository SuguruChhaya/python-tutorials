class Solution:
    def reverseWords(self, s: str) -> str:
        #Just to really ponder on these questions and make sure the thought process comes naturally. 
        #Other than the split method I think I came up with several other methods. 
        #1. Reverse then reverse all words and add it to a result string. 
        #2. Don't even reverse and start from the end. 
        #3. Probably work for both methods: only use 1 pointer and create second when I reach something and want to check. 
        #4. Iterate from the beginning, find words and add it to the the end of the result array. 
        
        #1. 
        s = s[::-1]
        
        fast = 0
        #Have to include when there are no heading spaces. 
        slow = -1
        result = ""
        while fast < len(s):
            #*However, adding a condition here prevents deleting heading. 
            if s[fast] == " ":
                if fast>slow+1:
                    if result == "":
                        result += s[slow+1:fast][::-1]
                    else:
                        #!I think adding the string in itself isn't doing any harm but " " is. 
                        result += " "+s[slow+1:fast][::-1]
                slow = fast
            #Accomodate for ending.
            
            #fast>slow+1 isn't an accurate measure here because the last letter could be a detached single letter. 
            elif s[fast]!=" " and fast+1==len(s):
                if result == "":
                    result += s[slow+1:fast+1][::-1]
                else:
                    result += " "+s[slow+1:fast+1][::-1]
                
            
            fast += 1
            
        return result

a = Solution()
print(a.reverseWords("  hello world  "))