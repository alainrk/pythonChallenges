def removeIslands(matrix):
	w, h = len(matrix[0]), len(matrix)
	landCells = getNonIslandCells(matrix, w, h)
	for land in landCells:
		i, j = land
		if matrix[i][j] == 0 or matrix[i][j] == 2:
			continue
		if matrix[i][j] == 1:
			propagateLand(matrix, i, j, w, h)
	for r in range(len(matrix)):
		for c in range(len(matrix[0])):
			matrix[r][c] = 1 if matrix[r][c] == 2 else 0
	return matrix

def propagateLand(matrix, i, j, w, h):
	if matrix[i][j] == 0 or matrix[i][j] == 2:
		return
	matrix[i][j] = 2
	for neigh in getNeighbours(matrix, i, j, w, h):
		propagateLand(matrix, neigh[0], neigh[1], w, h)

def getNeighbours(matrix, i, j, w, h):
	result = []
	if i > 1: # up
		result.append((i-1, j))
	if i < h-1: # down
		result.append((i+1, j))
	if j > 1: # left
		result.append((i, j-1))
	if j < w-1: # right
		result.append((i, j+1))
	return result

def getNonIslandCells(matrix, w, h):
	result = []
	for i in range(h):
		result.append((i, 0))
		result.append((i, w-1))
	for j in range(w):
		result.append((0, j))
		result.append((h-1, j))
	return result