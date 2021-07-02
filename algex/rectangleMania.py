'''
  0 1 2 3
0 . .   .
1 . . . .
2   .   .
'''

def rectangleMania(coords):
	n = 100
	matrix = [[0 for _ in range(n)] for _ in range(n)]
	for p in coords:
		matrix[p[0]][p[1]] = 1
	count = 0
	for i in range(n):
		for j in range(n):
			if matrix[i][j] == 0:
				continue
			for i1 in range(i + 1, n):
				for j1 in range(j + 1, n):
					if matrix[i1][j] == matrix[i][j1] == matrix[i1][j1] == 1:
						count += 1
	return count