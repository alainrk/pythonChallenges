def lineThroughPoints(points):
	maxPoints = 1

	for i in range(len(points) - 1):
		lines = {}
		for j in range(i + 1, len(points)):
			x1, y1 = points[i]
			x2, y2 = points[j]

			line = getLine(x1, y1, x2, y2)
			if line not in lines:
				lines[line] = 1
			lines[line] += 1

			maxPoints = max(maxPoints, lines[line])

	return maxPoints

def getLine(x1, y1, x2, y2):
	if x2 == x1:
		return (None, x1)
	m = (y2-y1)/(x2-x1)
	q = y1 - (m * x1)
	return (m, q)