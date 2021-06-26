def spiralTraverse(array):
	leftBound, rightBound = 0, len(array[0]) - 1
	upBound, bottomBound = 0, len(array) - 1
	res = []

	while leftBound <= rightBound and upBound <= bottomBound:
		# right
		res += array[upBound][leftBound:rightBound + 1]
		# down
		res += getColumn(array, rightBound)[upBound + 1:bottomBound + 1]
		# left
		for col in reversed(range(leftBound, rightBound)):
			if upBound == bottomBound:
				break
			res.append(array[bottomBound][col])
		# up
		for row in reversed(range(upBound + 1, bottomBound)):
			if leftBound == rightBound:
				break
			res.append(array[row][leftBound])
		leftBound += 1
		rightBound -= 1
		upBound += 1
		bottomBound -= 1
	return res


def getColumn(array, idx):
	return [array[r][idx] for r in range(len(array))]