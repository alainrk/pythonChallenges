def tandemBicycle(reds, blues, fastest):
  reds.sort()
  blues.sort()
  length = len(reds)

  redRange = range(length) if fastest else range(length - 1, -1, -1)
  b = length - 1

  result = 0
  for r in redRange:
    result += max(reds[r], blues[b])
    b -= 1
  return result

'''
Assuming they're sorted
if want minimize i want all the fastest together so they cancel each other out
if want maximize i want the fastest with the slowest so they can minimize theier effect
'''