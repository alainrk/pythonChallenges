def solve(n):
  n += 1
  dp = [[0 for _ in range(n)] for _ in range(n)]
  dp[0][0] = 1

  for i in range(n):
    for j in range(n):
      if i < n - 1: # down
        dp[i + 1][j] += dp[i][j]
      if j < n - 1: # right
        dp[i][j + 1] += dp[i][j]
  return dp[-1][-1]

print(solve(2))
print(solve(20))