import functools

def mergeOverlappingIntervals(intervals):
	intervals.sort(key=functools.cmp_to_key(compare)) # O(nlogn)
	result = []
	curr = 0
	currMerge = None
	following = None
	while True:
		if curr == len(intervals):
			break

		if currMerge is None:
			currMerge = intervals[curr][:]
			following = curr + 1

		if following == len(intervals):
			result.append(currMerge)
			break

		if intersects(currMerge, intervals[following]):
			currMerge = merge(currMerge, intervals[following])
		else:
			# I'm done with the merges, go on
			result.append(currMerge)
			currMerge = None
			curr = following

		following += 1
	return result

'''
[   A   ]
[ B ]
    [ B ]
	[   B   ]
	    [  B    ]

[  A  ]
     [B]
'''
def intersects(intA, intB):
	if intA[0] > intB[0]:
		return False
	if intA[1] >= intB[0]:
		return True
	return False

def merge(intA, intB):
	return [min(intA[0], intB[0]), max(intA[1], intB[1])]

def compare(intA, intB):
	for i in range(2):
		if intA[i] < intB[i]:
			return -1
		elif intB[i] > intB[i]:
			return 1
	return 0

'''
current => move on when following is not mergeable
following => move on when merge happens or not (in any case)
[1, 3] [2, 3] [3, 5] [3, 7] [8, 10]
[1, 3]
[1, 7]
'''

