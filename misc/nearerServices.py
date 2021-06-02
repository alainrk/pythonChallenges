import copy

def solve(buildings):
  current = copy.deepcopy(buildings[0])
  infinity = len(buildings) + 1
  nservices = 0

  for service in buildings[0].keys():
    # Init with max distance possible
    current[service] = infinity
    nservices += 1

  # Build init DB
  distances = [copy.deepcopy(current) for x in buildings]

  for i in range(len(buildings)):
    # Update current
    for service in buildings[i]:
      if buildings[i][service]:
        current[service] = 0
      else:
        current[service] += 1

    # Update distances => Forward
    for service in buildings[i]:
      if distances[i][service] > current[service]:
        distances[i][service] = current[service]

  # Reset current
  for service in buildings[0].keys():
    # Init with max distance possible
    current[service] = infinity

  # Best finding variables
  bestBuildingIndex = -1
  minSumDistance = infinity * nservices

  # Update distances => Backward
  for i in range(len(buildings) - 1, -1, -1):
    # Update current
    for service in buildings[i]:
      if buildings[i][service]:
        current[service] = 0
      else:
        current[service] += 1

    # Update distances
    sumDistance = 0
    for service in buildings[i]:
      if distances[i][service] > current[service]:
        distances[i][service] = current[service]
      sumDistance += distances[i][service]

    if sumDistance < minSumDistance:
      minSumDistance = sumDistance
      bestBuildingIndex = i

  return bestBuildingIndex


buildings = [
  { "bar": False, "gym": False, "office": True },
  { "bar": False, "gym": False, "office": False },
  { "bar": False, "gym": True, "office": True },
  { "bar": False, "gym": True, "office": False },
  { "bar": True, "gym": False, "office": False },
  { "bar": False, "gym": False, "office": False }
]

expected = [
  { "bar": 4, "gym": 2, "office": 0 },
  { "bar": 3, "gym": 1, "office": 1 },
  { "bar": 2, "gym": 0, "office": 0 }, # Best
  { "bar": 1, "gym": 0, "office": 1 }, # Best
  { "bar": 0, "gym": 1, "office": 2 },
  { "bar": 1, "gym": 2, "office": 3 },
]

bestBuildingIndex = solve(buildings)
assert(bestBuildingIndex == 2 or bestBuildingIndex == 3)
