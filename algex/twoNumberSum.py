def solve(array, targetSum):
  # Dict with diffs execluding x | 2x=targetSum
  diffs = { targetSum-v: i for (i, v) in enumerate(array) if targetSum - v != v }
  for x in array:
    if x in diffs:
      return [x, targetSum - x]
  return []

assert solve([1, 2, 3, 4], 6) == [2, 4]