def solveSudoku(board):
	backtrackSolve(board, 0, 0)
	return board

def backtrackSolve(board, row, col):
	if col == 9:
		row += 1
		col = 0
		if row == 9:
			return True

	if board[row][col] == 0:
		return tryPosition(board, row, col)

	return backtrackSolve(board, row, col + 1)

def tryPosition(board, row, col):
	possibleValues = getPossibleValues(board, row, col)
	for value in possibleValues:
		board[row][col] = value
		if backtrackSolve(board, row, col + 1):
			return True
	board[row][col] = 0
	return False

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

board = [
	[0, 2, 0, 0, 9, 0, 1, 0, 0],
	[0, 0, 7, 8, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 3, 6, 0],
	[0, 0, 1, 9, 0, 4, 0, 0, 0],
	[0, 0, 0, 6, 0, 5, 0, 0, 7],
	[8, 0, 0, 0, 0, 0, 0, 0, 9],
	[0, 0, 0, 0, 2, 0, 0, 0, 0],
	[7, 0, 0, 0, 0, 0, 0, 8, 5],
	[4, 9, 0, 0, 3, 0, 0, 0, 0]
]

print("Sudoku:")
for r in board:
	print(' | '.join(list(map(str, r))).replace('0', ' '))
	print('-'*34)

solveSudoku(board)

print("\nSolution:")
for r in board:
	print(' | '.join(list(map(str, r))).replace('0', ' '))
	print('-'*34)