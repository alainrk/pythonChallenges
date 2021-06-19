def canSum(arr, num):
  sums = [0] * (num + 1)
  sums[0] = 1

  '''
  [3, 4, 5], 7

  0th step => True, apply
  [1, 0, 0, 0, 0, 0, 0, 0]
   |______+3|  |  |
   |_________+4|  |
   |____________+5|

  [1, 0, 0, 1, 1, 1, 0, 0]
   |______+3|  |  |
   |_________+4|  |
   |____________+5|


  1th, 2th steps => False, so only go on
  [1, 0, 0, 1, 1, 1, 0, 0]
      |______+3|  |  |
      |_________+4|  |
      |____________+5|

  3th step => True, apply
  [1, 0, 0, 1, 1, 1, 1, 1] x
            |______+3|  |  |
            |_________+4|  |
            |____________+5|
  '''
  for s in range(len(sums)):
    for n in range(len(arr)):
      if sums[s] < 1:
        continue
      print(s, arr[n], sums)
      currSum = s + arr[n]
      if currSum <= num:
        sums[currSum] += 1

  return sums[num]

assert(canSum([1], 7) == 1)
assert(canSum([1, 1], 7) == 2)
assert(canSum([1, 1, 1], 7) == 3)
assert(canSum([5, 3, 4], 7) == 2)
assert(canSum([3, 4], 5) == 0)