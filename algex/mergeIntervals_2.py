def mergeOverlappingIntervals(intervals):
	intervals.sort(key=lambda i: i[0]) # O(nlogn)
	result = [intervals[0]]
	curr = 0
	for following in intervals:
		if intersects(result[curr], following):
			result[curr] = merge(result[curr], following)
		else:
			# I'm done with the merges, go on
			result.append(following)
			curr += 1
	return result

def intersects(intA, intB):
	if intA[0] > intB[0]:
		return False
	if intA[1] >= intB[0]:
		return True
	return False

def merge(intA, intB):
	return [min(intA[0], intB[0]), max(intA[1], intB[1])]

