import itertools

def solve2(s):
  groups = [(c, sum(1 for x in l)) for c, l in itertools.groupby(s)]
  print("groups", groups)

  multiple = sum(x[1] > 1 for x in groups)
  print("multiple", multiple)

  arr = []
  fence = 0
  for i in range(1, len(groups) - 1):
    previousGroup = groups[i - 1]
    nextGroup = groups[i + 1]
    currentGroup = groups[i]

    if previousGroup[0] == nextGroup[0] and groups[i][1] == 1:
      print("single fenced by equals -- previous: {}, current: {}, next: {}".format(previousGroup, currentGroup, nextGroup))
      fence += 1

  # fence = sum(groups[i - 1][0] == groups[i + 1][0] and groups[i][1] == 1 for i in range(1, len(groups) - 1))
  print("fence", fence)

  gauss = len(groups) * (len(groups) - 1) // 2
  print("gauss", gauss)
  result = multiple + gauss - fence
  print("RESULT:", result, "\n")

  return result

def bruteforce(s):
  b = set()
  d = {}
  for p in range(len(s)):
    for q in range(len(s)):
      if p == q:
        continue
      x = ""
      for i in range(len(s)):
        if i == p or i == q:
          continue
        x += s[i]
      print(p, q, x)
      if x not in d:
        d[x] = []
      d[x].append({"p": p, "q": q})
      b.add(x)
  print(len(b), b)

  for item in d:
    print(item, d[item])
# solve2('rrrazzaaaiouoqeuruuuue')
# solve2('fdf')
# solve2('abba')
# solve2('abcdef')

bruteforce('abcdef')