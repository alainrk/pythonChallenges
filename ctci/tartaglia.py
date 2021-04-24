def solve(x):
  s = x[:2]
  for k,v in itertools.groupby(x[2:]):
    s += k

  tartaglia = [[0 for x in range(len(s) - 2)] for y in range(len(s))]

  x = 0
  for row in tartaglia:
    x += 1
    y = 0

    for col in row:
      y += 1
      if x == 1 and (y == 1 or y == 2):
        tartaglia[x-1][y-1] = 1
        continue
      if x == 1:
        tartaglia[x-1][y-1] = 0
        continue
      if y == 1:
        tartaglia[x-1][y-1] = 1
        continue
      tartaglia[x-1][y-1] = tartaglia[x-1 - 1][y-1] + tartaglia[x-1 -1][y-1 - 1]

  # for row in tartaglia:
  #   print(row)

  return tartaglia[len(s) - 1][len(s)-2 - 1]