def createSolution(m, i, j, c):
  return True

def solveBT(arr, i, j, c, m, p):
  if str(c) in m[i][j] and m[i][j][str(c)] == True:
    return createSolution(m, i, j, c)

  n = j - i + 1
  upperBound = n * (n - 1) // 2
  if c > upperBound:
    raise Exception('c is gt upperBound')

  if n == 1:
    

  for k in range(i, j + 1):
    if i == j:
      m[i][j][str(k)] = True
      continue
    try:
      if (k - 1) > i:
        c1 = solveBT(m, i, k - 1, c - (n - 1), m, k)
      if (k + 1) < j:
        c2 = solveBT(m, k + 1, j, c - (n - 1), m, k)
    except:
      pass

def solve(n, c):
  arr = [x for x in range(1, n + 1)]
  m = [[{} for x in range(n)] for x in range(n)]

  print(arr)
  for r in m:
    print(r)

  solveBT(arr, 0, n-1, c, m, -1)

solve(10, 5)