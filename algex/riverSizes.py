def riverSizes(matrix):
	counts = []
	for r in range(len(matrix)):
		for c in range(len(matrix[0])):
			if matrix[r][c] == 1:
				count = markRiverDFS(matrix, r, c)
				counts.append(count)
	return counts

def markRiverDFS(matrix, r, c):
	if r < 0 or r > len(matrix) - 1 or c < 0 or c > len(matrix[0]) - 1 or matrix[r][c] != 1:
		return 0
	matrix[r][c] = 2
	up = markRiverDFS(matrix, r - 1, c)
	right = markRiverDFS(matrix, r, c + 1)
	down = markRiverDFS(matrix, r + 1, c)
	left = markRiverDFS(matrix, r, c - 1)
	return 1 + up + right + down + left

riverSizes([[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]])