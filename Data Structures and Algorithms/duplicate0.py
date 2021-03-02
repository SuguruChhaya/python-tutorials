class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        
        #First method using the built-in method. 
        a = 0
        #Has to be compared to initial length
        l = len(arr)
        #We have to cut out everything else.
        while a < l:
            if arr[a] == 0:
                #.insert does mess up a lot in a forloop. 
                arr.insert(a+1, 0)
                a += 2
            else:
                a += 1

        
        del(arr[l:])
        #Get the current length and start removing
        l = len(arr)
        while l < len(arr):
            del(arr[l])
        #I am guessing that arr = arr[0:l] creates a new array and the program blocks that kind of stuff. 
        """
        
        #For fun, let me do solution using some extra space. 
        newList = []
        a = len(arr)
        for i in range(a):
            newList.append(arr[i])
            if arr[i] == 0:
                newList.append(0)
        
        arr = newList[0:a-1]

a = Solution()
arr = [1,0,2,3,0,4,5,0]
a.duplicateZeros(arr)
print(arr)