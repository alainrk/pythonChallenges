def getPermutations(array):
	res = []
	if len(array) == 0:
		return res
	for i in range(len(array)):
		rest = getPermutations(array[:i] + array[i+1:])
		if not rest:
			res.append([array[i]])
		for r in rest:
			res.append([array[i]] + r)
	return res