def bsearch(array, target):
	l, r = 0, len(array) - 1
	while l <= r:
		curr = (r + l) // 2
		if target < array[curr]:
			r = curr - 1
		elif target > array[curr]:
			l = curr + 1
		else:
			return curr
	return -1

def searchInSortedMatrix(matrix, target):
	for i, row in enumerate(matrix):
		if row[0] > target:
			break
		if row[0] <= target <= row[-1]:
			j = bsearch(row, target)
			if j >= 0:
				return [i, j]
	return [-1, -1]