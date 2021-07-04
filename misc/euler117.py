# f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4)
# f(n) = 0 for n < 0
# f(0) = 1
def solve(n, minp, maxp):
  return _solveGen(n, minp, maxp, {})
  # return _solve(n, {})

def _solve(n, memo):
  if n in memo:
    return memo[n]

  # At least put one piece
  count = 1

  for i in range(n - 2 + 1):
    count += _solve(n - i - 2, memo)

  for i in range(n - 3 + 1):
    count += _solve(n - i - 3, memo)

  for i in range(n - 4 + 1):
    count += _solve(n - i - 4, memo)

  memo[n] = count
  return count

# Generalized
def _solveGen(n, minp, maxp, memo):
  count = 1

  if n < minp:
    return count

  if n in memo:
    return memo[n]

  for p in range(minp, maxp + 1):
    for i in range(n - p + 1):
      # print(f'Calls n - i - p = [{n},{i},{p}] = {n - i - p}')
      res = _solveGen(n - i - p, minp, maxp, memo)
      count += res
      # print(f'Solved n = {n}\tp = {p}\ti = {i}\tSol = {res}')
  memo[n] = count
  return count

print(solve(50, 2, 4))
print(solve(8, 2, 4))
print(solve(1, 2, 4))