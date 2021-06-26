def knapsackProblem(items, capacity):
	# [[v0, w0], [v1, w1]]
	caps = [{} for _ in range(capacity + 1)]
	caps[0][0] = set()
	weightWithMaxVal, maxVal = 0, 0

	for c in range(len(caps)):
		if not len(caps[c]):
			continue

		for i, item in enumerate(items):
			# for j, _cap in enumerate(caps):
			# 	print(j, _cap)
			# print('_____')
			value, weight = item

			for cval, celems in caps[c].items():
				if i in celems:
					continue

				totalWeight = c + weight
				if totalWeight > capacity:
					continue

				totalVal = cval + value
				caps[totalWeight][totalVal] = celems.union(set([i]))

				if totalVal > maxVal:
					weightWithMaxVal, maxVal = totalWeight, totalVal


	maxVal, maxElems = 0, []
	for val, elems in caps[weightWithMaxVal].items():
		if maxVal <= val:
			maxVal, maxElems = val, [x for x in elems]

	# print([maxVal, maxElems])
	return [maxVal, maxElems]


# print(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10))

print(knapsackProblem([
    [350, 45],
    [550, 65],
    [100, 50],
    [600, 70],
		], 200) == [1500, [3, 12, 14]])

# print(knapsackProblem([
# [1, 100],
# [350, 45],
# [550, 65],
# [600, 70],
# ], 200) == [1500, [3, 12, 14]])


