from functools import reduce

def arraySolver(acc, item, level):
	return acc + level * (item if type(item) is int else productSumHelper(item, level+1))

def productSumHelper(array, level):
	def f (acc, item):
		return arraySolver(acc, item, level)
	return reduce(f, array, 0)

def productSum(array):
	return productSumHelper(array, 1)