# O(nlogn + mlogm) T | O(1) S
def smallestDifference(a, b):
	a.sort()
	b.sort()
	l, r = 0, 0
	minVal, minCouple = float('inf'), None

	while l < len(a) and r < len(b):
		diff = abs(a[l] - b[r])
		if diff < minVal:
			minVal, minCouple = diff, [a[l], b[r]]
		if a[l] < b[r]:
			l += 1
		elif a[l] > b[r]:
			r += 1
		else:
			break # 0 diff case
	return minCouple