def solveSudoku(board):
	backtrackSolve(board, 0, 0)
	return board

def backtrackSolve(board, row, col):
	if col == 9:
		row += 1
		col = 0

	if row == 9 and col == 9:
		return True

	if board[row][col] == 0:
		possibleValues = getPossibleValues(board, row, col)
		for value in possibleValues:
			board[row][col] = value
			if backtrackSolve(board, row, col):
				return True
			board[row][col] = 0
			return False
	else:
		backtrackSolve(board, row, col + 1)

def isSolution(board):
	for r in board:
		for c in r:
			if c == 0:
				return False
	return True

def getPossibleValues(board, i, j):
	valids = { v for v in range(1, 10) }
	for x in range(9):
		valids.discard(board[i][x]) # check row
		valids.discard(board[x][j]) # check column
	if len(valids) == 0:
		return valids
	for cell in getCellsOfThisSquare(i, j):
		valids.discard(board[cell[0]][cell[1]])
	return valids

def getCellsOfThisSquare(i, j):
	cells = set()
	topleft = (3 * (i // 3), 3 * (j // 3))
	for r in range(3):
		for c in range(3):
			cells.add((topleft[0] + r, topleft[1] + c))
	return cells

print(solveSudoku([
    [0, 0, 0, 0, 3, 0, 0, 0, 9],
    [0, 4, 0, 5, 0, 0, 0, 7, 8],
    [2, 9, 0, 0, 0, 1, 0, 5, 0],
    [0, 7, 8, 0, 0, 3, 0, 0, 6],
    [0, 3, 0, 0, 6, 0, 0, 8, 0],
    [6, 0, 0, 8, 0, 0, 9, 3, 0],
    [0, 6, 0, 9, 0, 0, 0, 2, 7],
    [7, 2, 0, 0, 0, 5, 0, 6, 0],
    [8, 0, 0, 0, 7, 0, 0, 0, 0]
]))


print(isSolution([[7, 8, 5, 4, 3, 9, 1, 2, 6],
 [6, 1, 2, 8, 7, 5, 3, 4, 9],
 [4, 9, 3, 6, 2, 1, 5, 7, 8],
 [8, 5, 7, 9, 4, 3, 2, 6, 1],
 [2, 6, 1, 7, 5, 8, 9, 3, 4],
 [9, 3, 4, 1, 6, 2, 7, 8, 5],
 [5, 7, 8, 3, 9, 4, 6, 1, 2],
 [1, 2, 6, 5, 8, 7, 4, 9, 3],
 [3, 4, 9, 2, 1, 6, 8, 5, 7]]))