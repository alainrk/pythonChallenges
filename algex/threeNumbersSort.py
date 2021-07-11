def threeNumberSort(array, order):
	counts = { n: 0 for n in order }
	for n in array:
		counts[n] += 1
	res = []
	for n in order:
		res.extend([n] * counts[n])
	return res