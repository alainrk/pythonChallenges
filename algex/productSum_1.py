def productSumHelper(array, level):
	result = 0
	for item in array:
		result += level * (item if type(item) is int else productSumHelper(item, level+1))
	return result

def productSum(array):
	return productSumHelper(array, 1)