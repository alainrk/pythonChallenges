def solve1(n, queries):
  arr = [0] * (n + 1)
  for q in queries:
    a, b, k = q
    # arr[a] += k
    # arr[b] += k
    for i in range(a, b + 1):
      arr[i] += k
  print(max(arr))
  print(arr)

def solve(n, queries):
  arr = [0] * (n + 1)
  for q in queries:
    a, b, k = q
    arr[a] += k
    if b + 1 <= n:
      arr[b + 1] -= k

  s, smax = 0, float('-inf')
  for i in arr:
    s += i
    smax = max(smax, s)

  print(smax, arr)
  return smax

solve(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]])