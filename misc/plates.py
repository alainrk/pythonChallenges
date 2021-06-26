def platesBruteForce(leftStack, rightStack, p):
  maxSum, maxL, maxR = 0, 0, 0
  for l in range(len(leftStack) + 1):
    for r in range(len(rightStack) + 1):
      if l+r > p:
        continue
      s = sum(leftStack[:l]) + sum(rightStack[:r])
      if s > maxSum:
        maxSum, maxL, maxR = s, l, r
  return [maxL, maxR]

def plates(leftStack, rightStack, p):
  _, picks = platesHelper(leftStack, rightStack, p, 0, [0, 0], {})
  return picks

for i [1, N]:
 for j [0, P]:
  dp[i][j] := 0
   for x [0, min(j, K)]:
    dp[i][j] = max(dp[i][j], sum[i][x]+dp[i-1][j-x])

def platesHelper(leftStack, rightStack, p, totalSum, picks, memo):
  if p == 0:
    return totalSum, picks
  if len(leftStack) == 0:
    rsum = sum(rightStack[:p])
    return totalSum + rsum, [picks[0], picks[1] + rsum]
  if len(rightStack) == 0:
    lsum = sum(leftStack[:p])
    return totalSum + lsum, [picks[0] + lsum, picks[1]]

  key = f'{picks[0]}.{p}'
  if key in memo:
    return memo[key]

  # sumPickLeft = 0
  # sumPickRight = 0
  # if len(leftStack) > 0:
  #   sumPickLeft, picksLeft = platesHelper(leftStack[1:], rightStack, p-1, totalSum + leftStack[0], [picks[0] + 1, picks[1]], memo)
  # if len(rightStack) > 0:
  #   sumPickRight, picksRight = platesHelper(rightStack[1:], rightStack[1:], p-1, totalSum + rightStack[0], [picks[0], picks[1] + 1], memo)

  sumPickLeft, picksLeft = platesHelper(leftStack[1:], rightStack, p-1, totalSum + leftStack[0], [picks[0] + 1, picks[1]], memo)
  sumPickRight, picksRight = platesHelper(rightStack[1:], rightStack[1:], p-1, totalSum + rightStack[0], [picks[0], picks[1] + 1], memo)

  if sumPickLeft > sumPickRight:
    memo[key] = (sumPickLeft, picksLeft)
  else:
    memo[key] = (sumPickRight, picksRight)
  return memo[key]

# assert(plates([3, 5, 1, 20], [1, 2, 10, 3], 1) == [1, 0])
assert(plates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7], 11) == [0, 11])
# assert(plates([3, 5, 1, 20], [1, 2, 10, 3], 2) == [2, 0])
# assert(plates([3, 5, 1, 20], [1, 2, 10, 3], 3) == [0, 3])
# assert(plates([3, 5, 1, 20], [1, 2, 10, 3], 4) == [4, 0])

# l = [1] * 1000
# r = [1] * 1000
# l.append(4)
# r.append(3)
# print(plates(l, r, 1001))