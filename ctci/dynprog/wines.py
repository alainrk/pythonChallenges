# It's possible to get rid of year dimension to simplify (using L and R to calculate Y at runtime)
# state = (Year, LeftIdx, RightIdx) = (Y, L, R) => (L, R)
#
# y = i + (n - j)
# _ _ 2 _ _ 5 _ _ => 4 year passed, ergo 5° year now
# 2 + (9-5) - 1 = 5
#

######### BOTTOM UP SOLUTION #########
# "What is the best score we can get for this remaining interval?"
#
# dp(l, r) = max(dp(l+1, r) + y * w[l], dp(l, r-1) + y * w[r])
#
# At each state, I want to maximize:
# - the DP of next one without the leftmost (sold) + currYear * price
# - the DP of next one without the rightmost (sold) + currYear * price
def sellWinesBottomUp(wines):
  return __sellWinesBottomUp(wines, 0, len(wines) - 1, {})

def __sellWinesBottomUp(wines, l, r, memo={}):
  if l > r:
    return 0
  if (l, r) in memo:
    return memo[(l, r)]
  year = l + (len(wines) - r)
  pickLeft = __sellWinesBottomUp(wines, l+1, r, memo) + (year * wines[l])
  pickRight = __sellWinesBottomUp(wines, l, r-1, memo) + (year * wines[r])
  memo[(l, r)] = max(pickLeft, pickRight)
  return memo[(l, r)]


######### TOP DOWN SOLUTION #########
# "What is important so far?" (After got some decision on the present) =>  (L, R, [year=Implicit in L, R], [score=DP State]) => (L, R)
#
# dp(l - 1, r) = max(dp(l, r) + y * w[l], dp(l - 1, r))   => dp(0, r) = max(dp())
# dp(l, r - 1) = max(dp(l, r) + y * w[r], dp(l, r - 1))
#
# At each state, I want to maximize:
# - my current state previously set
# - the DP of next one without the rightmost/leftmost (sold) + currYear * price
def sellWinesTopDown(wines):
  dp = [[float('-inf') for _ in range(len(wines))] for _ in range(len(wines))]
  dp[0][len(wines) - 1] = 0 # starting point

  for l in range(len(dp)):
    for r in range(len(dp) - 1, l, -1):
      year = l + (len(wines) - r)
      dp[l + 1][r] = max(dp[l][r] + year * wines[l], dp[l + 1][r])
      dp[l][r - 1] = max(dp[l][r] + year * wines[r], dp[l][r - 1])

  # search solution
  maxSell = 0
  for i in range(len(wines)):
    maxSell = max(maxSell, dp[i][i] + len(wines) * wines[i])

  return maxSell


# https://www.youtube.com/watch?v=pwpOC1dph6U&ab_channel=Errichto

# Sell only leftmost or rightmost every year, ONE per year
# Each year the price is [y * price(i)]
# Best selling order?

# print(sellWinesBottomUp([2, 4, 6, 2, 5])) # 64
# print(sellWinesBottomUp([2])) # 2
# print(sellWinesBottomUp([2, 2])) # 6
# print(sellWinesBottomUp([1, 1])) # 3
# print(sellWinesBottomUp([2, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5])) # 3709

print(sellWinesTopDown([2, 4, 6, 2, 5])) # 64
print(sellWinesTopDown([2])) # 2
print(sellWinesTopDown([2, 2])) # 6
print(sellWinesTopDown([1, 1])) # 3
print(sellWinesTopDown([2, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5, 4, 6, 2, 5])) # 3709