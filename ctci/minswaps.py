def sort(arr):
  sarr = arr[:]
  sarr.sort()
  return sarr

def solve(arr):
  sorted = sort(arr)
  items = {}

  # Helper structure
  for i, v in enumerate(sorted):
    items[v] = {
      "correctIndex": i,
      "visited": False
    }

  stepCounts = 0
  loops = 0

  # Main algorithm loop
  # It has to find the loops and count the steps
  # Every n-steps loop is found, there will be [n-1] swap to do for sorting
  for i, v in enumerate(arr):
    if items[v]["visited"]:
      continue

    steps = 0
    currIndex = i

    while not items[arr[currIndex]]["visited"]:
      steps += 1
      # Mark as visited
      items[arr[currIndex]]["visited"] = True
      # Go to the array position in wich this item should be
      currIndex = items[arr[currIndex]]["correctIndex"]

    if steps > 0:
      stepCounts += steps
      loops += 1

  return stepCounts - loops

assert(solve([7, 15, 12, 3]) == 2)
assert(solve([3, 5, 2, 8, 1, 6]) == 5)
assert(solve([3, 2, 4]) == 1)
assert(solve([4, 3]) == 1)
assert(solve([1, 2, 3, 4, 5]) == 0)