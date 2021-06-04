from random import randint

def quickSort(array):
	if len(array) < 2:
		return array
	pivot = randint(0, len(array) - 1)
	left, right = [], []
	for idx, val in enumerate(array):
		if idx == pivot:
			continue
		if val <= array[pivot]:
			left.append(val)
		else:
			right.append(val)
	return quickSort(left) + [array[pivot]] + quickSort(right)
