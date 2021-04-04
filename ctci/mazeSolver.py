# Backtracking maze solver

import os

MAZE_MAP = ["_", "X", "o", "E"]
DEBUG = True if os.environ.get("DEBUG") else False

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
    self.exitRow = nrows - 1
    self.exitCol = ncols - 1

  def __str__(self):
    string = "  " + "|".join([str(r) for r in range(self.ncols)]) + '\n'
    for r, row in enumerate(self.maze):
      strRow = []
      string += f'{r} '
      for c, col in enumerate(row):
        strRow.append(MAZE_MAP[col])
      string += "|"
      string += "|".join(strRow)
      string += "|\n"
    return string

  def handleSolution(self, solution, k):
    strSolution = [f'({str(s.row)}, {str(s.col)})' for s in solution]
    self.finished = True
    print(f'Solution: {" => ".join(strSolution)}')

  def isValidMove(self, row, col, prevRow, prevCol):
    okBoundaries, noPreviousCell, noWalls, noLoops = (False for i in range(4))

    okBoundaries = 0 <= row < self.nrows and 0 <= col < self.ncols
    noPreviousCell = not (prevRow == row and prevCol == col)

    if okBoundaries:
      noWalls = self.maze[row][col] != 1
    if okBoundaries:
      noLoops = self.maze[row][col] != 2

    if DEBUG:
      print(f'isValidMove: row {row}, col {col}, prevRow {prevRow}, prevCol {prevCol}')
      print(f'okBoundaries {okBoundaries}, noPreviousCell {noPreviousCell}, noWalls {noWalls}, noLoops {noLoops}\n')
    return okBoundaries and noPreviousCell and noWalls and noLoops

  def constructMoves(self, solution, k):
    moves = []
    currentMove = solution[k - 2]

    up = (currentMove.row - 1, currentMove.col)
    right = (currentMove.row, currentMove.col + 1)
    down = (currentMove.row + 1, currentMove.col)
    left = (currentMove.row, currentMove.col - 1)

    if self.isValidMove(up[0], up[1], currentMove.prevRow, currentMove.prevCol):
      moves.append(SolutionNode(up[0], up[1], currentMove.row, currentMove.col))

    if self.isValidMove(right[0], right[1], currentMove.prevRow, currentMove.prevCol):
      moves.append(SolutionNode(right[0], right[1], currentMove.row, currentMove.col))

    if self.isValidMove(down[0], down[1], currentMove.prevRow, currentMove.prevCol):
      moves.append(SolutionNode(down[0], down[1], currentMove.row, currentMove.col))

    if self.isValidMove(left[0], left[1], currentMove.prevRow, currentMove.prevCol):
      moves.append(SolutionNode(left[0], left[1], currentMove.row, currentMove.col))

    if DEBUG:
      print("Possible moves:", list(map(lambda m: str(m), moves)))
    return moves

  def isSolution(self, solution, k):
    currentMove = solution[k - 1]
    return currentMove.row == self.exitRow and currentMove.col == self.exitCol

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

      print('\n', str(self))
      self.backtrack(solution, k)

      # Comment this to find all the possibile solutions
      if self.finished:
        return

      # Undo
      solution.pop()
      self.maze[ak.row][ak.col] = 0

def main():
  # mazeMatrix = [
  #   [2, 1, 0, 1, 1, 1, 0],
  #   [0, 1, 0, 0, 0, 1, 0],
  #   [0, 0, 0, 1, 0, 1, 0],
  #   [0, 1, 0, 0, 0, 0, 0],
  #   [0, 1, 1, 0, 0, 1, 0],
  #   [0, 0, 1, 0, 1, 1, 0],
  #   [1, 0, 1, 0, 0, 0, 0],
  # ]

  mazeMatrix = [
    [2, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 0, 0],
  ]

  maze = Maze(mazeMatrix, len(mazeMatrix), len(mazeMatrix[0]))
  maze.backtrack([SolutionNode(0, 0, 0, 0)], 1)

if __name__ == "__main__":
  main()