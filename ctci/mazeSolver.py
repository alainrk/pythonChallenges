# Backtracking maze solver

class SolutionNode:
  def __init__(self, row, col, prevRow, prevCol):
    self.row = row
    self.col = col
    self.prevRow = prevRow
    self.prevCol = prevCol

  def __str__(self):
    return f'row: {self.row}, col: {self.col}'

class Maze:
  def __init__(self, maze, nrows, ncols):
    self.maze = maze
    self.nrows = nrows
    self.ncols = ncols
    self.finished = False

  def handleSolution(self, solution, k):
    print(f'Solution: {solution}')

  # Check boundary constraints
  # Check avoiding get back to the previous cell
  # Check wall constraints
  # Check path loops
  def isValidMove(self, row, col, prevRow, prevCol):
    okBoundaries = 0 <= row < self.nrows and 0 <= col < self.ncols
    noPreviousCell = not (prevRow == row and prevRow == col)
    noWalls = self.maze[row][col] != 1
    noLoops = self.maze[row][col] != 2

    print(f'isValidMove: row {row}, col {col}, prevRow {prevRow}, prevCol {prevCol}')
    print(f'okBoundaries {okBoundaries}, noPreviousCell {noPreviousCell}, noWalls {noWalls}, noLoops {noLoops}\n')
    return okBoundaries and noPreviousCell and noWalls

  def constructMoves(self, solution, k):
    moves = []
    currentMove = solution[k - 2]

    up = (currentMove.row - 1, currentMove.col)
    right = (currentMove.row, currentMove.col + 1)
    down = (currentMove.row + 1, currentMove.col)
    left = (currentMove.row, currentMove.col - 1)

    # if (0 <= up[0] < self.nrows and 0 <= up[1] < self.ncols) and (currentMove.prevRow != up[0] and currentMove.prevRow != up[1]):
    if self.isValidMove(up[0], up[1], currentMove.row, currentMove.col):
      moves.append(SolutionNode(up[0], up[1], currentMove.row, currentMove.col))

    # if (0 <= right[0] < self.nrows and 0 <= right[1] < self.ncols) and (currentMove.prevRow != right[0] and currentMove.prevRow != right[1]):
    if self.isValidMove(right[0], right[1], currentMove.row, currentMove.col):
      moves.append(SolutionNode(right[0], right[1], currentMove.row, currentMove.col))

    # if (0 <= down[0] < self.nrows and 0 <= down[1] < self.ncols) and (currentMove.prevRow != down[0] and currentMove.prevRow != down[1]):
    if self.isValidMove(down[0], down[1], currentMove.row, currentMove.col):
      moves.append(SolutionNode(down[0], down[1], currentMove.row, currentMove.col))

    # if (0 <= left[0] < self.nrows and 0 <= left[1] < self.ncols) and (currentMove.prevRow != left[0] and currentMove.prevRow != left[1]):
    if self.isValidMove(left[0], left[1], currentMove.row, currentMove.col):
      moves.append(SolutionNode(left[0], left[1], currentMove.row, currentMove.col))

    print("Possible moves:", list(map(lambda m: str(m), moves)))
    return moves

  def isSolution(self, solution, k):
    return solution[k - 1].row == self.nrows - 1 and solution[k - 1].col == self.ncols - 1

  def backtrack(self, solution, k):
    if self.isSolution(solution, k):
      self.handleSolution(solution, k)
      return

    k += 1
    sk = self.constructMoves(solution, k)
    while len(sk):
      ak = sk.pop()

      # Apply
      solution.append(ak)
      self.maze[ak.row][ak.col] = 2

      self.backtrack(solution, k)

      # Undo
      solution.pop(ak)
      self.maze[ak.row][ak.col] = 0

    if self.finished:
      return

mazeMatrix = [
  [0, 1, 0, 1, 1, 1, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 0, 0, 1, 0, 1, 0],
  [0, 1, 0, 0, 0, 0, 0],
  [0, 1, 1, 0, 0, 1, 0],
  [0, 0, 1, 0, 1, 1, 0],
  [1, 0, 1, 0, 0, 0, 1],
]
maze = Maze(mazeMatrix, 7, 7)
maze.backtrack([SolutionNode(0, 0, 0, 0)], 1)