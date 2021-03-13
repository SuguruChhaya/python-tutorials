class Solution:
    '''
    def reverseWords(self, s: str) -> str:
        #OK my initial thought was to break them up and add them all to a list, reverse them, detect spaces, and then reverse index-1th. 
        #Maybe if I use 2 pointers, it would be relatively easy to detect where exactly I have to reverse.
        
        arr = []
        
        for letter in s:
            arr.append(letter)
            
        arr.reverse()
        
        fast = 0
        slow = -1
        
        while fast < len(arr):
            if arr[fast] == " ":
                self.reverse(arr, slow+1, fast-1)
                slow = fast
                
            #I also have to reverse the last word. 
            elif fast == len(arr)-1:
                self.reverse(arr, slow+1, fast)
                
            fast += 1
            
        #So far so good just gotta remove extra spaces. 
        #print(arr)
        fast = 0
        shouldInsert = False
        while fast < len(arr):
            if arr[fast] == " ":
                del(arr[fast])
                #Should only become true if fast != 0 because then we don't want to insert. 
                if fast != 0:
                    shouldInsert = True
            else:
                #Conviniently, all trailing 0s will be removed because we will never reach this condition again. 
                if shouldInsert:
                    arr.insert(fast, " ")
                    shouldInsert = False
                fast += 1
                
        return "".join(arr)
    
    #O(n) for appending
    #O(n) for reverse
    #2 traversals with insert so worst case is close to O(n + n**2)
    '''
    def reverseWords(self, s: str) -> str:
        #Probably O(n) time and O(n) space is where I traverse from back, find word using 2 pointers, and add it to a new string string maybe with a space. 
        
        front = len(s) - 1
        #Don't even have to make into list cuz I don't need item assignment. 
        back = front + 1
        
        #For this approach, I think I have to be aware of certain things. 
        #1. What if there are trailing 0s. (where I start)
        #2. What if there are starting 0s? (where I end)
        #3. 
        result = ""
        while front >= 0:
            if s[front] == " ":
                if back-1!=front:
                    result +=  s[front+1:back] + " "
                back = front
            front -= 1
        
        #*Try the final adding. 
        if back-1!=front:
            result += s[front+1:back] + " "
        a = result[:len(result)-1]
        print(a)
        print(len(a))


        #*There is no space between and last word is omitted but other than that is good. 
        #!For the last word thing, I think I can just manually add a starting " ". -> Since strings are immutable, not possible. 

        
                
    
            
    def reverse(self, arr, start, end):
        while start <=end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
            

class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        arr = []
        
        for letter in s:
            arr.append(letter)
        
        fast = 0
        slow = -1
        
        while fast < len(arr):
            if arr[fast] == " ":
                self.reverse(arr, slow+1, fast-1)
                slow = fast
                
            #I also have to reverse the last word. 
            elif fast == len(arr)-1:
                self.reverse(arr, slow+1, fast)
                
            fast += 1
            
        return "".join(arr)
        '''
        
        #I probably don't even have to copy it in an array. 
        #What I want to do is manually code the following line. Do the same thing without built-in methods. 
        #return " ".join(s[::-1].split()[::-1])
        
        #For this case, I could just blindly add a space just to register the last word. 
        s=s[::-1] 
        result = ""
        
        fast = 0
        slow = -1
        #The region I will sandwich is s[slow+1:fast]
        
        while fast < len(s):
            if s[fast] == " ":
                #Check how I should insert the word. 
                #Based on how video did it. 
                #I can just simply add because I know word is only separated by one space and no 
                #*If I want to eliminate in-between space I can check for sandwich. 
                #if slow+1<fast:
                    if result == "":
                        result = s[slow+1:fast]
                    else:
                        #!Again, there is no problem with the slicing but problem with adding " " no matter what. 
                        result = s[slow+1:fast] + " " + result
                    slow = fast
            fast += 1

        #*Finally check for the end. 
        if s[fast-1] != " ":
            if result == "":
                result = s[slow+1:fast]
            else:
                result = s[slow+1:fast] + " " + result
                
        return result
        
            
    def reverse(self, arr, start, end):
        while start <=end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
a = Solution()
#*Trailspaces will be eliminated in the above case. 
#?But how can I eliminate head spaces?
b = a.reverseWords("    the     sky is blue   ")
print(b)
print(len(b))
"the sky is blue"
"  hello world  "
"a good   example"
"  Bob    Loves  Alice   "
"Alice does not even like bob"
