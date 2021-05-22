from functools import reduce
def waterArea(heights):
  maxh = 0
  maxes = [0] * len(heights)
  res = [0] * len(heights)

# --->
for i in range(len(heights)):
  maxes[i] = maxh = max(maxh, heights[i])
  res[i] = maxes[i] - heights[i]

# init again
maxh = 0
# <---
for i in range(len(heights) - 1, -1, -1):
  maxes[i] = maxh = max(maxh, heights[i])
  res[i] = min(maxes[i] - heights[i], res[i])
return reduce(lambda acc, x: acc + x, res, 0)