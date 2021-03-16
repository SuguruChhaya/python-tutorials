


def merge(intervals):
	intervals.sort()
	result = []
	curr = intervals[0]
	l = len(intervals)
	for i in range(1, l):
		if intervals[i][0] <= curr[1]:
			curr[1] = max(intervals[i][1], curr[1])
		else:
			result.append(curr)	
			curr = intervals[i]
	result.append(curr)
	return result


print(merge([[1,4],[0,4]]))