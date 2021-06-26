# s(n) = { 0 n<l, s(n-l) + 1 + s(n-1)}
def solve(n, l):
  return _solve(n, l, {})

def _solve(n, l, memo):
  if n < l:
    return 0
  if n in memo:
    return memo[n]
  memo[n] = _solve(n - l, l, memo) + 1 + _solve(n - 1, l, memo)
  return memo[n]

print(solve(50, 2) + solve(50, 3) + solve(50, 4))
print(solve(5, 2))
print(solve(5, 3))
print(solve(5, 4))
