def countInversions(array):
	count = 0
	sortedArr = []
	for i in range(len(array) - 1, -1, -1):
		idx = bsearch(sortedArr, array[i])
		sortedArr.insert(idx, array[i])
		count += idx
	return count

def bsearch(array, v):
	if len(array) == 0:
		return 0
	start, end = 0, len(array) - 1
	while start <= end:
		mid = (start + end) // 2
		if isRightSpot(array, mid, v):
			return mid
		elif v <= array[mid]:
			end = mid - 1
		else:
			start = mid + 1
	return -1

def isRightSpot(array, idx, val):
	if array[idx] == val:
		return True
	if idx == 0 and val < array[0]:
		return True
	if idx == len(array) - 1 and val > array[-1]:
		return True
	if idx > 0 and idx < len(array) - 1 and array[idx - 1] < val < array[idx + 1]:
		return True
	return False

countInversions([2, 3, 3, 1, 9, 5, 6])