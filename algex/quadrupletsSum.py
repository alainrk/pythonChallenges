def fourNumberSum(array, targetSum):
	solution = []
	sums = {}
	for a in range(len(array)- 1):
		for b in range(a + 1, len(array)):
			s = array[a] + array[b]
			d = targetSum - s
			if d in sums:
				for rest in sums[d]:
					solution.append(rest + [array[a], array[b]])
		for c in range(0, a):
			s = array[a] + array[c]
			if s not in sums:
				sums[s] = []
			sums[s].append([array[c], array[a]])
	return solution

