def maxSubsetSumNoAdjacent(array, sums=0):
  if len(array) == 0:
    return 0
  if len(array) < 2:
    return array[0]
  first, second = max(array[:2]), array[0]
  for i in range(2, len(array)):
    curr = max(first, second + array[i])
    print(f'first, second + array[i]={first}, {second} + {array[i]}')
    print(f'curr={curr}\nfirst={first}\nsecond={second}\n')
    first, second = curr, first
  return first

def maxSubsetSumNoAdjacentRec(array, sums=0):
	if len(array) == 0:
		return sums
	including = maxSubsetSumNoAdjacent(array[2:], sums + array[0])
	excluding = maxSubsetSumNoAdjacent(array[1:], sums)
	return including if including > excluding else excluding

maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135])