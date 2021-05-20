from functools import reduce

def productSumHelper(array, level):
	return reduce(lambda acc, item: acc + level * (item if type(item) is int else productSumHelper(item, level+1)), array, 0)

def productSum(array):
	return productSumHelper(array, 1)