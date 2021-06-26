def spiralTraverse(array):
	leftBound = 0
	rightBound = len(array[0]) - 1
	upBound = 0
	bottomBound = len(array) - 1

	r, c = 0, 0
	res = []
	direction = 'R'

	while leftBound <= c <= rightBound and upBound <= r <= bottomBound:
		res.append(array[r][c])
		if direction == 'R':
			if c < rightBound:
				c += 1
			else:
				r += 1
				upBound += 1
				direction = 'D'
		elif direction == 'L':
			if c > leftBound:
				c -= 1
			else:
				r -= 1
				bottomBound -= 1
				direction = 'U'
		elif direction == 'D':
			if r < bottomBound:
				r += 1
			else:
				c -= 1
				rightBound -= 1
				direction = 'L'
		elif direction == 'U':
			if r > upBound:
				r -= 1
			else:
				c += 1
				leftBound += 1
				direction = 'R'
	return res

