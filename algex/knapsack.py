def knapsackProblem(items, capacity):
	# [[v0, w0], [v1, w1]]
	caps = [None for _ in range(capacity + 1)]
	vals = [0 for _ in range(capacity + 1)]
	used = [set() for _ in range(capacity + 1)]
	caps[0] = []
	maxCap = 0

	for c in range(len(caps)):
		if caps[c] is None:
			continue
		for i, item in enumerate(items):
			value, weight = item
			if i in used[c]:
				continue
			totalWeight = c + weight
			totalVal = vals[c] + value
			if totalWeight > capacity:
				continue
			if totalVal < vals[totalWeight]:
				continue
			maxCap = max(maxCap, totalWeight)
			vals[totalWeight] = totalVal
			caps[totalWeight] = caps[c] + [i]
			used[totalWeight] = set(caps[totalWeight])
	return [vals[maxCap], caps[maxCap]]


# print(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10))

print(knapsackProblem([
    [465, 100],
    [400, 85],
    [255, 55],
    [350, 45],
    [650, 130],
    [1000, 190],
    [455, 100],
    [100, 25],
    [1200, 190],
    [320, 65],
    [750, 100],
    [50, 45],
    [550, 65],
    [100, 50],
    [600, 70],
    [240, 40]
		], 200) == [1500, [3, 12, 14]])