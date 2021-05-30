def getStartingPoints(board, words):
	startingPoints = {}
	firstCharWords = {}

	for word in words:
		startingPoints[word] = []
		if word[0] not in firstCharWords:
			firstCharWords[word[0]] = []
		firstCharWords[word[0]].append(word)

	for row in range(len(board)):
		for col in range(len(board[0])):
			if board[row][col] in firstCharWords:
				for word in firstCharWords[board[row][col]]:
					startingPoints[word].append((row, col))
	return startingPoints

def validNextPositions(board, findChar, currentPos, visited):
	nrows, ncols = len(board), len(board[0])
	r, c = currentPos
	positions = [
		(r - 1, c - 1),
		(r - 1, c),
		(r - 1, c + 1),
		(r, c + 1),
		(r + 1, c + 1),
		(r + 1, c),
		(r + 1, c - 1),
		(r, c - 1)
	]
	validPositions = []
	for pos in positions:
		x, y = pos
		if 0 > x or nrows <= x or 0 > y or ncols <= y:
			continue
		if board[x][y] != findChar:
			continue
		if pos in visited:
			continue
		validPositions.append(pos)
	return validPositions

def backtrackIsAPath(board, startingPoint, word, visited):
	visited.add(startingPoint)

	if len(word) == 1:
		return True

	nextPositions = validNextPositions(board, word[1], startingPoint, visited)
	pathExists = False

	for nextPos in nextPositions:
		pathExists = backtrackIsAPath(board, nextPos, word[1:], visited)
		if pathExists:
			break
	if not pathExists:
		visited.discard(startingPoint)
		return False
	return True

def wordExists(board, wordStartingPoints, word):
	for startingPoint in wordStartingPoints:
		visited = set()
		exists = backtrackIsAPath(board, startingPoint, word, visited)
		if exists:
			return True

def boggleBoard(board, words):
	results = []
	startingPoints = getStartingPoints(board, words)
	for word in words:
		if wordExists(board, startingPoints[word], word):
			results.append(word)
	return results


board = [
  ['c', 'x', 'x'],
  ['u', 'a', 'x'],
  ['b', 'y', 'r'],
]

words = ['cub', 'test', 'xxx', 'bar']

boggleBoard(board, words)