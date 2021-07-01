def searchForRange(array, target):
	l = binsearch(array, target, 0, len(array) - 1, 'left')
	if l < 0:
		return [-1, -1]
	r = binsearch(array, target, l, len(array) - 1, 'right')
	return [l, r]

def binsearch(array, target, i, j, direction):
	while i <= j:
		m = (i + j) // 2
		if array[m] == target:
			if direction == 'left':
				if (m == 0 or array[m-1] < target): # find the leftmost
					return m
				j = m - 1
				continue
			else:
				if (m == len(array) -1 or array[m+1] > target): # find the rightmost
					return m
				i = m + 1
				continue
		if target < array[m]:
			j = m - 1
		else:
			i = m + 1
	return -1
