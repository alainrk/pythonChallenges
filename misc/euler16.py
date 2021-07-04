def solve(r):
  s = 0
  while r > 0:
    r, c = r // 10, r % 10
    s += c
  return s

print(solve(2**1000))