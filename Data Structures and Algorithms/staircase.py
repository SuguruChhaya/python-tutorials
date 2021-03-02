class Solution:
    def climbStairs(self, n: int, l=[1, 1]) -> int:
        #The brute force solution will be to just hardcore recursion. 
        #But obviously time limit exceeded. 
        '''
        for i in range(2, n+1):
            l.append(None)

        if l[n] == None:
            l[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return l[n]
        '''
        
        #Bottom up approach
        for i in range(2, n+1):
            l[0], l[1] = l[1], l[0]+l[1]
            print(l)
        return l[1]

a = Solution()
print(a.climbStairs(3))