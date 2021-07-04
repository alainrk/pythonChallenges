# s(n) = { 0 n<l, s(n-l) + 1 + s(n-1)}
def solve(n, l):
  dp = [0] * (n + 1)

  for i in range(len(dp) - 1):
    dp[i + 1] += dp[i]
    if i + l <= n:
      dp[i + l] += dp[i] + 1
  return dp[-1]

print(solve(50, 2) + solve(50, 3) + solve(50, 4))
print(solve(5, 2))
print(solve(5, 3))
print(solve(5, 4))
print(solve(500, 2))
