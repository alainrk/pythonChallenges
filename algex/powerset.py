from itertools import combinations

def powerset(array):
	result = [[]]
	for x in array:
		for c in range(len(result)):
			result.append(result[c] + [x])
	return result

def powerset2(array):
	result = []
	for i in range(len(array) + 1):
		result += list(combinations(array, i))
	return [[x for x in t] for t in result]