class Solution:
    def merge(self, intervals):
        #Never mentions that the intervals are going to be sorted. 
        #Checking last and first will only work if the entire thing is sorted. 
        #The .sort() automatically does this for me. 
        #Just because 2 intervals are overlapping doesn't mean they are the only ones overlapping. I should probably run a while loop to continue checking for further intervals. 
        #E.g. [[1, 3], [2, 6], [5, 8]]
        intervals.sort()
        i = 0
        prevMax = 0
        result = []
        while i < len(intervals):
            j=i
            #This component is the hard part because I also have to look at the ends. 
            #I also have to consider cases like [[1, 4], [2, 3]] where [1, 4] encapsulates the whole interval
            #For every time j moves, I can store the maximun ending it covers. 
            maxEnding = intervals[j][1]
            while j + 1 < len(intervals) and intervals[j][1] >= intervals[j+1][0]: #and intervals[j][1] <=intervals[j+1][1]:
                
                j+=1
                maxEnding = max(maxEnding, intervals[j][1])

            #Before appending, I should check whether intervals[i][1] is larger than max ending
            if maxEnding > prevMax:
                result.append([intervals[i][0], maxEnding])
            i = j+1
            
            prevMax = max(prevMax, maxEnding)
            
        return result


    def merge(self, intervals):
        intervals.sort()

        result = []
        for i in range(len(intervals)):
            #Do I have to first check whether they exist or do I have to do the merging first?
            #I think I can first check. 
            willMerge = True
            for j in range(len(result)):
                #Check whether lies in anything. 
                if result[j][0] <= intervals[i][0] and result[j][1] >= intervals[i][1]:
                    willMerge = False

            if willMerge:
                lowerbound = intervals[i][0]
                upperbound = intervals[i][1]
                for a in range(i, len(intervals)):
                    #!The commented out really isn't the correct criteria to carry out a swap. 
                    '''
                    if intervals[a][0]<lowerbound:
                        lowerbound = intervals[a][0]
                    if intervals[a][1]>upperbound:
                        upperbound = intervals[a][1]
                    '''
                    #*The correct definition is probably this:
                    if lowerbound <= intervals[a][0] <= upperbound or lowerbound <= intervals[a][1] <=upperbound:
                        lowerbound = min(lowerbound, intervals[a][0])
                        upperbound = max(upperbound, intervals[a][1])

                result.append([lowerbound, upperbound])

        return result

a=Solution()
arr = [[1,4],[4,5]]
print(a.merge(arr))
'''
Sorted or not -> caught that. 
Brute force -> sort all intervals. 
'''

https://leetcode.com/submissions/detail/467855759/
https://github.com/SuguruChhaya/python-tutorials/blob/master/Data%20Structures%20and%20Algorithms/mergeintervalfinal.py

'''
So far, striver's better approach is to place one value to hold a temporary array that can be expanded. When merging, only change the last value. When no change needs to be made, add to final array. 
This prevents checking all the time but do I really have to check everything. -> No. In previous I had to do so. 
'''


def merge(self, intervals):
	result = []
	curr = intervals[0]
	l = len(intervals)
	for i in range(1, l):
		if intervals[i][0] <= curr[1]:
			curr[1] = max(intervals[i][1], curr[1])

		else:
			result.append(curr)
			curr = intervals[i]
	return result


Since sorting, overlapping intervals must be consecutive. 
		