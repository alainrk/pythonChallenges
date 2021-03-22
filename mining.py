def solve(n, k, minesGolds):
  matrix = {}
  mines = set()
  for x in minesGolds:
    mines.add(x[0])
    for y in minesGolds:
      print(x, y)
      matrix[(x[0], y[0])] = abs(x[0] - y[0]) * x[1]

  res = "\t" + "\t".join([str(m) for m in mines]) + "\tTotMove"
  columnCost = {}
  for x in mines:
    res += f'\n{x}\t'
    rowCount = 0
    for y in mines:
      cost = matrix[(x, y)]
      res += f'{cost}\t'
      rowCount += cost
      columnCost[y] = cost if y not in columnCost else columnCost[y] + cost
    res += str(rowCount)
  res += "\nTotRecv\t" + "\t".join([str(columnCost[c]) for c in columnCost])

  print(res)

solve(
  6, 2, [
  (10, 15),
  (12, 17),
  (16, 18),
  (18, 13),
  (30, 10),
  (32, 1)
])