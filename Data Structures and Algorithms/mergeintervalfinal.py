class Solution:
    def merge(self, intervals):
        intervals.sort()
        result = []
        for i in range(len(intervals)):
            willMerge = True
            for j in range(len(result)):
                #Check whether interval is already included in result array. 
                if result[j][0] <= intervals[i][0] and result[j][1] >= intervals[i][1]:
                    willMerge = False

            if willMerge:
                lowerbound = intervals[i][0]
                upperbound = intervals[i][1]
                #*Correct way to check overlap
                #The commented portion never really happens because already sorted. 
                #?Why can I not just check the last element instead of checking everything in the data structure? -> Need the forloop to merge correctly. 
                for a in range(i, len(intervals)):
                    #*Correct way to check overlap
                    if lowerbound <= intervals[a][0] <= upperbound:# or lowerbound <= intervals[a][1] <=upperbound:
                        lowerbound = min(lowerbound, intervals[a][0])
                        upperbound = max(upperbound, intervals[a][1])

                result.append([lowerbound, upperbound])

                result.append([lowerbound, upperbound])

        return result

a=Solution()
print(a.merge([[1,3],[2,6],[8,10],[15,18]]))
