def combinations(arr):
  if len(arr) == 0:
    return [[]]
  res = []
  combs = combinations(arr[1:])
  for c in combs:
    res.append([arr[0]] + c)
    res.append(c)
  return res

print(combinations([1, 2, 3]))
