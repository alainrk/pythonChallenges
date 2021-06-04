def sortedSquaredArray(array):
	squares = [None for x in array]
	left, right = 0, len(array) - 1
	curr = len(array) - 1
	while curr >= 0:
		if abs(array[left]) <= abs(array[right]):
			squares[curr] = array[right] ** 2
			right -= 1
		else:
			squares[curr] = array[left] ** 2
			left += 1
		curr -= 1
	return squares
