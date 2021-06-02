def sameBsts(arrayOne, arrayTwo):
	if len(arrayOne) != len(arrayTwo):
		return False
	if len(arrayOne) == len(arrayTwo) == 0:
		return True
	if arrayOne[0] != arrayTwo[0]:
		return False

	leftOne = list(filter(lambda x: x < arrayOne[0], arrayOne[1:]))
	rightOne = list(filter(lambda x: x >= arrayOne[0], arrayOne[1:]))

	leftTwo = list(filter(lambda x: x < arrayTwo[0], arrayTwo[1:]))
	rightTwo = list(filter(lambda x: x >= arrayTwo[0], arrayTwo[1:]))

	return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)